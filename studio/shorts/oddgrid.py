"""Same Bro GAMES: ODD ONE OUT grid engine (campaign100, 9 Nov 2026).
Levels of N x N vector icons with exactly one odd icon; timer bar per level, fair reveal (ring + 'C4!').
The last level freezes: 'COMMENT ROW + COLUMN' + 3-2-1, then the reveal. Rows A.., columns 1...
Voice: one take, 3 lines (intro / last-level freeze / reveal), split by time ranges like game.CupGame.
Icon sets are pluggable: icon(c, x, y, r, variant) where variant is None (normal) or the level's odd kind.
Usage: see studio/shorts/s72_oddemoji/make.py."""
import json
import math
import os
import random
import subprocess
import sys

import cairo
import numpy as np
from PIL import Image

sys.path.insert(0, "/home/claude/sid/shorts")
sys.path.insert(0, "/home/claude/sid/v2")
import kit as K  # noqa: E402
import music2 as M2  # noqa: E402
import vshort as VS  # noqa: E402
from kit import T, k, U, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

VW, VH, FPS = 1080, 1920, 30
GX0, GY0, GW = 110, 560, 920   # grid box


def face(c, x, y, r, var=None):
    """Smiley face icon. variants: 'frown', 'wink', 'look', 'brow', 'tint'."""
    col = (1.0, 0.8, 0.18) if var != 'tint' else (1.0, 0.74, 0.18)
    c.arc(x, y, r, 0, 2 * math.pi); c.set_source_rgb(*col); c.fill_preserve()
    c.set_source_rgb(0.75, 0.5, 0.05); c.set_line_width(max(1.5, r * 0.06)); c.stroke()
    ex, ey, er = r * 0.34, -r * 0.18, r * 0.13
    for sx in (-1, 1):
        if var == 'wink' and sx == 1:
            c.move_to(x + sx * ex - er, y + ey); c.line_to(x + sx * ex + er, y + ey)
            c.set_source_rgb(0.2, 0.12, 0.05); c.set_line_width(r * 0.08); c.stroke()
            continue
        c.arc(x + sx * ex, y + ey, er, 0, 2 * math.pi); c.set_source_rgb(0.2, 0.12, 0.05); c.fill()
        dx = -er * 0.5 if var == 'look' else 0
        c.arc(x + sx * ex + dx + er * 0.25, y + ey - er * 0.3, er * 0.35, 0, 2 * math.pi); c.set_source_rgb(1, 1, 1); c.fill()
        if var == 'brow':
            c.move_to(x + sx * ex - er * 1.3, y + ey - er * 2.0 + (sx * er * 0.6)); c.line_to(x + sx * ex + er * 1.3, y + ey - er * 2.0 - (sx * er * 0.6))
            c.set_source_rgb(0.2, 0.12, 0.05); c.set_line_width(r * 0.07); c.stroke()
    c.set_line_width(r * 0.09); c.set_line_cap(cairo.LINE_CAP_ROUND); c.set_source_rgb(0.25, 0.12, 0.05)
    if var == 'frown':
        c.arc_negative(x, y + r * 0.62, r * 0.38, -0.5, -math.pi + 0.5)
    else:
        c.arc(x, y + r * 0.05, r * 0.42, 0.5, math.pi - 0.5)
    c.stroke()


class OddGrid:
    def __init__(self, d, segs, caps, title, series, levels=((6, 'frown', 5.0), (7, 'wink', 5.6), (8, 'look', 6.2)),
                 seed=7, mood='chill', icon=face, labels=("EASY", "HARD", "IMPOSSIBLE")):
        self.d, self.segs, self.caps, self.title, self.series, self.mood, self.icon = d, segs, caps, title, series, mood, icon
        self.labels = labels
        rnd = random.Random(seed)
        t = 0.05
        self.lv = []   # (t0, t1, n, kind, (row, col), t_reveal_end)
        for li, (n, kind, dur) in enumerate(levels):
            pos = (rnd.randrange(n), rnd.randrange(n))
            last = li == len(levels) - 1
            self.lv.append([t, t + dur, n, kind, pos])
            t += dur + (0 if last else 1.6)
        self.t_freeze = self.lv[-1][1]
        v2 = segs[1][1] - segs[1][0]
        self.t_count = self.t_freeze + v2 + 0.2
        self.t_reveal = self.t_count + 3.0
        self.dur = self.t_reveal + (segs[2][1] - segs[2][0]) + 1.4
        self.voice_at = [0.0, self.t_freeze, self.t_reveal]
        r, c_ = self.lv[-1][4]
        self.answer = f"{'ABCDEFGHIJ'[r]}{c_ + 1}"
        json.dump(dict(answers=[f"{'ABCDEFGHIJ'[p[0]]}{p[1] + 1}" for (*_, p) in self.lv], dur=self.dur),
                  open(f"{d}/game.json", "w"))

    def level_at(self, t):
        for i, L in enumerate(self.lv):
            if t < L[1] + (1.6 if i < len(self.lv) - 1 else 1e9):
                return i
        return len(self.lv) - 1

    def grid(self, c, t, li, reveal_a):
        t0, t1, n, kind, (rr, cc) = self.lv[li]
        cell = GW / n
        a = k(t, t0, t0 + 0.25)
        S.rrect(c, GX0 - 20, GY0 - 20, GW + 40, GW + 40, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
        for j in range(n):
            T(c, 'ABCDEFGHIJ'[j], GX0 - 52, GY0 + cell * (j + 0.5) + 14, 34, GREY, a, stroke=None)
            T(c, str(j + 1), GX0 + cell * (j + 0.5), GY0 - 34, 34, GREY, a, stroke=None)
        for i in range(n):
            for j in range(n):
                x, y = GX0 + cell * (j + 0.5), GY0 + cell * (i + 0.5)
                pop = U.eob(k(t, t0 + (i + j) * 0.012, t0 + 0.25 + (i + j) * 0.012))
                if pop <= 0:
                    continue
                c.save(); c.translate(x, y); c.scale(pop, pop)
                self.icon(c, 0, 0, cell * 0.4, kind if (i, j) == (rr, cc) else None)
                c.restore()
        if reveal_a > 0:
            x, y = GX0 + cell * (cc + 0.5), GY0 + cell * (rr + 0.5)
            c.arc(x, y, cell * 0.55 * (1.6 - 0.6 * U.eob(reveal_a)), 0, 2 * math.pi)
            c.set_source_rgba(*GRN, reveal_a); c.set_line_width(10); c.stroke()
            lab = f"{'ABCDEFGHIJ'[rr]}{cc + 1}!"
            K.stamp(c, self._now, self._rv_t0, lab, 540, GY0 + GW + 110, GRN, 64, -0.04)

    def frame(self, i):
        t = i / FPS
        self._now = t
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        c = cairo.Context(sf)
        g = cairo.LinearGradient(0, 0, 0, VH)
        g.add_color_stop_rgb(0, 0.08, 0.06, 0.16); g.add_color_stop_rgb(0.6, 0.13, 0.07, 0.2); g.add_color_stop_rgb(1, 0.04, 0.03, 0.07)
        c.set_source(g); c.paint()
        li = self.level_at(t)
        t0, t1 = self.lv[li][0], self.lv[li][1]
        last = li == len(self.lv) - 1
        self._rv_t0 = self.t_reveal if last else t1
        ra = k(t, self._rv_t0, self._rv_t0 + 0.35)
        self.grid(c, t, li, ra)
        sf.flush()
        rgb = VS.FXV.post(sf, 'studio', i, 0)
        ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        o = cairo.Context(ov)
        self.overlay(o, t, li, t0, t1, last)
        ov.flush()
        cb = np.ndarray((VH, VW, 4), np.uint8, ov.get_data())
        al = cb[..., 3:4].astype(np.float32) / 255.0
        return np.clip(rgb.astype(np.float32) * (1 - al) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)

    def overlay(self, o, t, li, t0, t1, last):
        S.rrect(o, 300, 60, 480, 58, 29); o.set_source_rgba(*YEL, 0.95); o.fill()
        T(o, self.series, 540, 100, 30, (0.08, 0.08, 0.1), stroke=None)
        if t < self.t_freeze:
            T(o, self.title[0], 540, 225, 84, WHITE, lw=12)
            T(o, self.title[1], 540, 320, 62, YEL, lw=10)
            col = [GRN, YEL, RED][min(2, li)]
            S.rrect(o, 340, 380, 400, 74, 37); o.set_source_rgba(0.05, 0.05, 0.08, 0.85); o.fill()
            T(o, f"LEVEL {li + 1}: {self.labels[li]}", 540, 430, 38, col, stroke=None)
            if t0 <= t < t1:  # timer bar
                fr = 1 - (t - t0) / (t1 - t0)
                S.rrect(o, 110, 478, 860, 22, 11); o.set_source_rgba(1, 1, 1, 0.12); o.fill()
                S.rrect(o, 110, 478, max(22, 860 * fr), 22, 11); o.set_source_rgba(*(RED if fr < 0.3 else col), 0.95); o.fill()
        else:
            if t < self.t_reveal:
                T(o, "STOP!", 540, 250, 120, RED, lw=14)
                S.rrect(o, 120, 330, 840, 100, 50); o.set_source_rgba(0.05, 0.05, 0.08, 0.92); o.fill()
                T(o, "COMMENT ROW + COLUMN", 540, 398, 52, YEL, stroke=None)
                if t > self.t_count:
                    n = 3 - int(t - self.t_count)
                    f = (t - self.t_count) % 1
                    sc = 1.4 - 0.4 * U.eob(min(1, f / 0.2))
                    o.save(); o.translate(950, 230); o.scale(sc, sc)
                    o.arc(0, 0, 80, 0, 2 * math.pi); o.set_source_rgba(0.05, 0.05, 0.08, 0.9); o.fill()
                    T(o, str(max(1, n)), 0, 38, 110, WHITE, lw=8)
                    o.restore()
            else:
                T(o, "DID YOU GET IT?", 540, 300, 84, WHITE, k(t, self.t_reveal + 1.0, self.t_reveal + 1.3), lw=12)
                if t > self.dur - 2.4:
                    K.stamp(o, t, self.dur - 2.4, "PLAY AGAIN >", 540, 420, RED, 54, -0.04)
        for n_, (a0, a1) in enumerate(self.segs):
            st = self.voice_at[n_]
            ln = a1 - a0
            if st <= t < st + ln + 0.2:
                ws = self.caps[n_].split()
                groups, cur = [], []
                for w in ws:
                    cur.append(w)
                    if len(cur) >= 4 or w[-1] in ".,?!:":
                        groups.append(cur); cur = []
                if cur:
                    groups.append(cur)
                tot = sum(len(g) for g in groups)
                tc = st
                for g in groups:
                    dd = ln * len(g) / tot
                    if tc <= t < tc + dd or g is groups[-1]:
                        T(o, " ".join(g), 540, 1750, 58, WHITE, lw=12)
                        break
                    tc += dd
        S.rrect(o, 425, 1838, 230, 56, 28); o.set_source_rgb(0.06, 0.06, 0.08); o.fill_preserve()
        o.set_source_rgb(*YEL); o.set_line_width(4); o.stroke()
        T(o, "SAME BRO", 540, 1877, 30, YEL, stroke=None)

    def audio(self):
        SR = M2.SR
        N = int(SR * self.dur)
        v = M2._read_audio(f"{self.d}/vo.mp3")
        voice = np.zeros(N)
        for (a0, a1), at in zip(self.segs, self.voice_at):
            seg = v[int(a0 * SR):int(a1 * SR)]
            fade = np.minimum(1, np.minimum(np.arange(len(seg)), np.arange(len(seg))[::-1]) / (0.01 * SR))
            i0 = int(at * SR)
            voice[i0:i0 + len(seg)] += (seg * fade)[:N - i0]
        sfx = np.zeros(N)

        def put(sig, at, g):
            i0 = int(at * SR)
            sfx[i0:i0 + len(sig)] += g * sig[:N - i0]
        tt = np.arange(int(0.05 * SR)) / SR
        tick = np.sin(2 * np.pi * 1500 * tt) * np.exp(-tt * 70)
        td = np.arange(int(0.9 * SR)) / SR
        ding = (np.sin(2 * np.pi * 1318.5 * td) + 0.6 * np.sin(2 * np.pi * 1975.5 * td)) * np.exp(-td * 5)
        for L in self.lv[:-1]:
            for j in range(3):
                put(tick, L[1] - 3 + j, 0.18)
            put(ding, L[1] + 0.1, 0.16)
        for j in range(3):
            put(tick, self.t_count + j, 0.25)
        put(ding, self.t_reveal + 0.15, 0.18)
        seed = os.path.basename(self.d.rstrip('/'))
        info = M2.mix(voice, self.dur, seed, self.mood, f"{self.d}/mix.wav", sfx=sfx)
        json.dump(info, open(f"{self.d}/music.json", "w"))
        return info

    def preview(self, times, out):
        ims = [Image.fromarray(self.frame(int(tt * FPS))).resize((270, 480)) for tt in times]
        sheet = Image.new("RGB", (270 * min(8, len(ims)), 480 * ((len(ims) + 7) // 8)))
        for k_, im in enumerate(ims):
            sheet.paste(im, ((k_ % 8) * 270, (k_ // 8) * 480))
        sheet.save(out)

    def render(self, out):
        print("audio", self.audio())
        n = int(self.dur * FPS)
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{VW}x{VH}",
                              "-r", str(FPS), "-i", "-", "-i", f"{self.d}/mix.wav",
                              "-filter_complex", "[1:a]aresample=44100,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
                              "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-b:v", "4M",
                              "-maxrate", "5M", "-bufsize", "8M", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                              "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        for i in range(n):
            p.stdin.write(self.frame(i).tobytes())
        p.stdin.close()
        p.wait()
