"""Vertical (1080x1920) Same Bro short engine: themed 16:9 world scenes framed by a vertical camera + screen overlays."""
import json
import math
import re
import subprocess
import sys
import wave

import cairo
import numpy as np
from PIL import Image

sys.path.insert(0, "/home/claude/sid/long1")
sys.path.insert(0, "/home/claude/sid/v2")
sys.path.insert(0, "/home/claude/sid/v3")
import fx as FXV  # noqa: E402  (1080x1920 grade)
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, YEL, RED, GRN, WHITE  # noqa: E402

VW, VH, FPS = 1080, 1920, 30
FXV.GRADES.setdefault('studio', dict(lift=(0.03, 0.0, 0.05), gain=(1.02, 0.95, 1.08), sat=1.05, vig=0.9, bloom=0.4))
FXV.GRADES.setdefault('red', dict(lift=(0.05, 0.0, 0.01), gain=(1.08, 0.9, 0.9), sat=0.95, vig=1.0, bloom=0.3))
FXV.GRADES.setdefault('money', dict(lift=(0.0, 0.03, 0.02), gain=(0.98, 1.05, 0.98), sat=1.05, vig=0.8, bloom=0.4))


def line_times(d):
    """Line start/end from silence gaps (no transcription needed)."""
    txt = [re.sub(r'\[[^\]]*\]\s*', '', l).strip() for l in open(f"{d}/vo.txt").read().split('\n') if l.strip()]
    out = subprocess.run(["ffmpeg", "-i", f"{d}/vo.mp3", "-af", "silencedetect=n=-35dB:d=0.22", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    ss = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    se = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                f"{d}/vo.mp3"], capture_output=True, text=True).stdout)
    gaps = [((a + b) / 2) for a, b in zip(ss, se) if b - a < 3]
    start = se[0] if ss and ss[0] < 0.05 and se else 0.0
    end = ss[-1] if ss and ss[-1] > dur - 1.5 else dur
    w = [len(t) for t in txt]
    tot = sum(w)
    bounds, acc = [start], start
    for i in range(len(txt) - 1):
        acc += (end - start) * w[i] / tot
        near = min(gaps, key=lambda g: abs(g - acc)) if gaps else acc
        bounds.append(near if abs(near - acc) < 1.2 and near > bounds[-1] + 0.5 else acc)
    bounds.append(end)
    return [[bounds[i], bounds[i + 1]] for i in range(len(txt))], txt, dur


class Short:
    def __init__(self, d, caps, hook, shots, sources=None):
        self.d, self.caps, self.hook, self.shots, self.sources = d, caps, hook, shots, sources
        self.L, self.txt, self.dur = line_times(d)
        json.dump(self.L, open(f"{d}/lines.json", "w"))

    def s(self, n):
        return self.L[n - 1][0]

    def caption(self, c, t):
        for n, (a, b) in enumerate(self.L):
            if not (a - 0.05 <= t <= b + 0.15):
                continue
            ws = self.caps[n].split()
            groups, cur = [], []
            for w in ws:
                cur.append(w)
                if len(cur) >= 4 or w[-1] in ".,?!:":
                    groups.append(cur); cur = []
            if cur:
                groups.append(cur)
            tot = sum(len(g) for g in groups)
            tc = a
            for g in groups:
                dd = (b - a) * len(g) / tot
                if tc - 0.05 <= t < tc + dd:
                    txt = " ".join(g)
                    kk = U.eob((t - tc + 0.05) / 0.12)
                    hi = any((w.strip('".,:?!').isupper() and len(w.strip('".,:?!')) > 1) or '₹' in w or '%' in w for w in g)
                    c.save(); c.translate(540, 1500); c.scale(0.85 + 0.15 * kk, 0.85 + 0.15 * kk)
                    T(c, txt, 0, 0, 74 if len(txt) < 20 else 60, YEL if hi else WHITE, lw=14)
                    c.restore()
                    return
                tc += dd
            return

    def frame(self, i):
        t = i / FPS
        idx = next((j for j, sh in enumerate(self.shots) if sh[0] <= t < sh[1]), len(self.shots) - 1)
        st, en, world, cam0, cam1, over, grade = self.shots[idx]
        lt = (t - st) / max(0.01, en - st)
        e = S.ease(lt)
        z, cx, cy = [a + (b - a) * e for a, b in zip(cam0, cam1)]
        cx += math.sin(t * 1.3) * 5
        cy += math.sin(t * 1.1 + 1) * 4
        punch = 1 + 0.06 * max(0, 1 - (t - st) / 0.15) if st > 0 else 1
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        c = cairo.Context(sf)
        c.set_source_rgb(0.03, 0.03, 0.05); c.paint()
        if world:
            c.save()
            c.translate(VW / 2, VH / 2)
            c.scale(z * punch, z * punch)
            c.translate(-cx, -cy)
            world(c, t, lt)
            c.restore()
        if over:
            over(c, t, lt)
        sf.flush()
        rgb = FXV.post(sf, grade, i, 0)
        ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        o = cairo.Context(ov)
        if t < 2.6:  # hook title
            a = min(1, t / 0.15) * min(1, (2.6 - t) / 0.3)
            S.rrect(o, 40, 170, 1000, 60 + 110 * len(self.hook), 30); o.set_source_rgba(0.02, 0.02, 0.04, 0.82 * a); o.fill()
            for k_, (txt, col) in enumerate(self.hook):
                T(o, txt, 540, 270 + k_ * 110, 92 if len(txt) < 15 else 74, col, a, lw=12)
        if self.sources and t > 2.6:
            S.rrect(o, 140, 60, 800, 46, 23); o.set_source_rgba(0, 0, 0, 0.5); o.fill()
            T(o, self.sources, 540, 92, 24, (0.85, 0.87, 0.95), stroke=None, bold=False)
        self.caption(o, t)
        if t > self.dur - 0.2:
            pass
        S.rrect(o, 425, 1740, 230, 62, 31); o.set_source_rgb(0.06, 0.06, 0.08); o.fill_preserve()
        o.set_source_rgb(*YEL); o.set_line_width(4); o.stroke()
        T(o, "SAME BRO", 540, 1782, 32, YEL, stroke=None)
        ov.flush()
        cb = np.ndarray((VH, VW, 4), np.uint8, ov.get_data())
        al = cb[..., 3:4].astype(np.float32) / 255.0
        return np.clip(rgb.astype(np.float32) * (1 - al) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)

    def preview(self, times, out):
        ims = [Image.fromarray(self.frame(int(tt * FPS))).resize((270, 480)) for tt in times]
        sheet = Image.new("RGB", (270 * min(8, len(ims)), 480 * ((len(ims) + 7) // 8)))
        for k_, im in enumerate(ims):
            sheet.paste(im, ((k_ % 8) * 270, (k_ // 8) * 480))
        sheet.save(out)

    def render(self, out, bed=True):
        n = int((self.dur + 0.8) * FPS)
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{VW}x{VH}",
                              "-r", str(FPS), "-i", "-", "-i", f"{self.d}/vo.mp3", "-i", "/home/claude/sid/shorts/bed.wav",
                              "-filter_complex",
                              "[1:a]aresample=44100,highpass=f=70,apad,volume=1.5,asplit=2[vo][key];[2:a]volume=0.22[b];"
                              "[b][key]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=350[bd];"
                              "[vo][bd]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5[a]",
                              "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-b:v", "4M",
                              "-maxrate", "5M", "-bufsize", "8M", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                              "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        for i in range(n):
            p.stdin.write(self.frame(i).tobytes())
        p.stdin.close()
        p.wait()
