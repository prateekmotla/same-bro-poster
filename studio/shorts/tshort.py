"""Text-only Same Bro short (no voiceover): on-screen story text + music bed + pops/whooshes.
Works muted (all info is on screen) and with sound (music + SFX)."""
import json
import math
import subprocess
import sys
import wave

import cairo
import numpy as np

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
from vshort import S, U, T, YEL, WHITE  # noqa: E402

FONT = "Poppins"
SR = 44100


def line_dur(txt):
    w = len(txt.split())
    return max(2.8, 0.9 + w / 2.7)  # ~2.7 words/sec reading speed + settle time


class TextShort(VS.Short):
    def __init__(self, d, caps, hook, shots, sources=None, start=0.4, tail=2.2):
        self.d, self.caps, self.hook, self.shots, self.sources = d, caps, hook, shots, sources
        t, L = start, []
        for cp in caps:
            dd = line_dur(cp)
            L.append([t, t + dd]); t += dd
        self.L, self.txt, self.dur = L, caps, t + tail
        json.dump(self.L, open(f"{d}/lines.json", "w"))

    # word-wrapped story card, words pop in one by one, CAPS / ₹ / % words in yellow
    def caption(self, c, t):
        for n, (a, b) in enumerate(self.L):
            if not (a <= t < (b if n < len(self.L) - 1 else self.dur + 1)):
                continue
            words = self.caps[n].split()
            size = 56
            c.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            c.set_font_size(size)
            sp = c.text_extents(" ").x_advance
            rows, cur, cw = [], [], 0
            for w in words:
                ww = c.text_extents(w).x_advance
                if cur and cw + sp + ww > 880:
                    rows.append((cur, cw)); cur, cw = [], 0
                cur.append((w, ww)); cw += (sp if len(cur) > 1 else 0) + ww
            if cur:
                rows.append((cur, cw))
            lh = 72
            h = len(rows) * lh + 50
            y0 = 1560 - h / 2
            ka = U.eob((t - a) / 0.18)
            S.rrect(c, 60, y0, 960, h, 28); c.set_source_rgba(0.02, 0.02, 0.05, 0.86 * min(1, (t - a) / 0.12)); c.fill()
            reveal = (b - a) * 0.45
            i = 0
            for r, (ws, rw) in enumerate(rows):
                x = 540 - rw / 2
                y = y0 + 25 + lh * r + 54
                for w, ww in ws:
                    tw = a + reveal * i / max(1, len(words))
                    i += 1
                    if t < tw:
                        x += ww + sp
                        continue
                    al = min(1, (t - tw) / 0.12)
                    core = w.strip('".,:?!()')
                    hi = (core.isupper() and len(core) > 1) or '₹' in w or '%' in w or any(ch.isdigit() for ch in w)
                    c.save(); c.translate(x, y + 10 * (1 - al)); c.move_to(0, 0); c.text_path(w)
                    c.set_source_rgba(0, 0, 0, al); c.set_line_width(9); c.set_line_join(cairo.LINE_JOIN_ROUND)
                    c.stroke_preserve()
                    c.set_source_rgba(*(YEL if hi else WHITE), al); c.fill()
                    c.restore()
                    x += ww + sp
            return

    def sfx(self, path):
        n = int((self.dur + 1) * SR)
        out = np.zeros(n, np.float32)
        rng = np.random.default_rng(3)
        # soft pop on each new line
        pt = np.arange(int(0.09 * SR)) / SR
        pop = np.sin(2 * math.pi * (900 - 3000 * pt) * pt) * np.exp(-pt * 45) * 0.35
        for a, _ in self.L:
            i = int(a * SR); out[i:i + len(pop)] += pop[:max(0, min(len(pop), n - i))]
        # whoosh on each shot change (skip t=0)
        wl = int(0.35 * SR)
        noise = rng.standard_normal(wl).astype(np.float32)
        env = np.sin(np.linspace(0, math.pi, wl)) ** 2
        k = np.ones(40, np.float32) / 40
        wh = np.convolve(noise, k, mode='same') * env * 0.5
        for sh in self.shots[1:]:
            i = int(max(0, sh[0] - 0.15) * SR); out[i:i + wl] += wh[:max(0, min(wl, n - i))]
        pcm = (np.clip(out, -1, 1) * 32767).astype(np.int16)
        with wave.open(path, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())

    def render(self, out, bed=True):
        sfx = f"{self.d}/sfx.wav"
        self.sfx(sfx)
        n = int((self.dur + 0.3) * FPS)
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{VS.VW}x{VS.VH}",
                              "-r", str(FPS), "-i", "-", "-stream_loop", "-1", "-i", "/home/claude/sid/shorts/bed.wav", "-i", sfx,
                              "-filter_complex",
                              f"[1:a]aresample=44100,volume=0.9,afade=t=in:d=0.6,afade=t=out:st={self.dur - 1.2:.2f}:d=1.2[b];"
                              "[2:a]aresample=44100,volume=1.0[s];"
                              "[b][s]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5[a]",
                              "-map", "0:v", "-map", "[a]", "-t", f"{self.dur:.2f}", "-c:v", "libx264", "-preset", "medium",
                              "-b:v", "4M", "-maxrate", "5M", "-bufsize", "8M", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                              "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        for i in range(n):
            p.stdin.write(self.frame(i).tobytes())
        p.stdin.close()
        p.wait()


FPS = VS.FPS
