"""Voiced remake of a text-only short (tshort.TextShort make.py) with an ElevenLabs voiceover.

Overlays/shots in the old make.py are written against the text-reading timeline (sh.s(n) + offsets).
VoicedText keeps that timeline (self.P) and time-warps it, line by line, onto the real voice timing
(self.L from vo.mp3 silence gaps), so every visual beat lands on the line being spoken.
Captions (English) + hook + source use real time. Audio = voice + low ducked music bed (vshort.render)."""
import json
import math
import sys

import cairo
import numpy as np

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import tshort as TS  # noqa: E402
from vshort import S, U, T, YEL, FXV  # noqa: E402

VW, VH, FPS = VS.VW, VS.VH, VS.FPS


class VoicedText(VS.Short):
    def __init__(self, d, caps, hook, shots, sources=None, start=0.4, tail=2.2):
        super().__init__(d, caps, hook, shots, sources)  # voice timing -> self.L, self.dur
        assert len(self.txt) == len(caps), f"vo.txt has {len(self.txt)} lines, CAPS has {len(caps)}"
        t, P = start, []
        for cp in caps:
            dd = TS.line_dur(cp)
            P.append([t, t + dd]); t += dd
        self.P, self.pdur = P, t + tail
        json.dump({"voice": self.L, "plan": P}, open(f"{d}/lines.json", "w"))

    def s(self, n):  # plan-timeline start of line n (what the overlays were written against)
        return self.P[n - 1][0]

    def warp(self, t):
        L, P = self.L, self.P
        if t <= L[0][0]:
            return P[0][0] * t / max(0.01, L[0][0])
        for (a, b), (A, B) in zip(L, P):
            if t < b:
                return A + (t - a) * (B - A) / max(0.01, b - a)
        return P[-1][1] + (t - L[-1][1])

    def frame(self, i):
        t = i / FPS
        tw = self.warp(t)
        idx = next((j for j, sh in enumerate(self.shots) if sh[0] <= tw < sh[1]), len(self.shots) - 1)
        st, en, world, cam0, cam1, over, grade = self.shots[idx]
        lt = (tw - st) / max(0.01, en - st)
        e = S.ease(min(1, max(0, lt)))
        z, cx, cy = [a + (b - a) * e for a, b in zip(cam0, cam1)]
        cx += math.sin(t * 1.3) * 5
        cy += math.sin(t * 1.1 + 1) * 4
        punch = 1 + 0.06 * max(0, 1 - (tw - st) / 0.15) if st > 0 else 1
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        c = cairo.Context(sf)
        c.set_source_rgb(0.03, 0.03, 0.05); c.paint()
        if world:
            c.save(); c.translate(VW / 2, VH / 2); c.scale(z * punch, z * punch); c.translate(-cx, -cy)
            world(c, tw, lt)
            c.restore()
        if over:
            over(c, tw, lt)
        sf.flush()
        rgb = FXV.post(sf, grade, i, 0)
        ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        o = cairo.Context(ov)
        if t < 2.6:  # hook title
            a = min(1, t / 0.15) * min(1, (2.6 - t) / 0.3)
            S.rrect(o, 40, 170, 1000, 60 + 110 * len(self.hook), 30); o.set_source_rgba(0.02, 0.02, 0.04, 0.82 * a); o.fill()
            for k_, (txt, col) in enumerate(self.hook):
                T(o, txt, 540, 270 + k_ * 110, 92 if len(txt) < 15 else 74 if len(txt) < 20 else 60, col, a, lw=12)
        if self.sources and t > 2.6:
            S.rrect(o, 140, 60, 800, 46, 23); o.set_source_rgba(0, 0, 0, 0.5); o.fill()
            T(o, self.sources, 540, 92, 24, (0.85, 0.87, 0.95), stroke=None, bold=False)
        self.caption(o, t)
        S.rrect(o, 425, 1740, 230, 62, 31); o.set_source_rgb(0.06, 0.06, 0.08); o.fill_preserve()
        o.set_source_rgb(*YEL); o.set_line_width(4); o.stroke()
        T(o, "SAME BRO", 540, 1782, 32, YEL, stroke=None)
        ov.flush()
        cb = np.ndarray((VH, VW, 4), np.uint8, ov.get_data())
        al = cb[..., 3:4].astype(np.float32) / 255.0
        return np.clip(rgb.astype(np.float32) * (1 - al) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)
