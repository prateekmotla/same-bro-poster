"""Same Bro GAMES: COUNT THE TRIANGLES engine (campaign100, 11 Nov 2026).
A big triangle cut by lines from the apex to the base (n_rays lines incl. the 2 sides) and by horizontal cross lines
(levels incl. the base). Every triangle = apex + 2 rays + 1 horizontal, so total = C(n_rays, 2) x len(levels).
The engine enumerates them, checks the count, and at the reveal fills each triangle one by one with a running number.
Timing/overlay/audio reused from countgame.CountGame (3 voice lines: intro / freeze / reveal).
Usage: see studio/shorts/c137_triangles/make.py."""
import itertools
import json
import math
import sys

import cairo
import numpy as np

sys.path.insert(0, "/home/claude/sid/shorts")
import countgame as CG  # noqa: E402
import vshort as VS  # noqa: E402
from kit import T, k, U, S, YEL, GRN, WHITE  # noqa: E402

VW, VH, FPS = CG.VW, CG.VH, CG.FPS
TCOLS = [(0.95, 0.35, 0.35), (0.3, 0.75, 0.95), (0.98, 0.78, 0.25), (0.45, 0.85, 0.45), (0.8, 0.5, 0.95), (1.0, 0.6, 0.3)]


class TriCount(CG.CountGame):
    def __init__(self, d, segs, caps, title, series, apex=(540, 560), base_y=1300, base_xs=(160, 420, 660, 920),
                 levels=(1000, 1300), hunt=10.0, seed=1, mood='chill', step=0.45):
        self.d, self.segs, self.caps, self.title, self.series, self.mood = d, segs, caps, title, series, mood
        self.total, self.step, self.apex = False, step, apex
        ax, ay = apex
        self.rays = [(bx, base_y) for bx in base_xs]
        self.levels = list(levels)

        def at(ray, y):
            bx, by = ray
            return (ax + (bx - ax) * (y - ay) / (by - ay), y)
        self.at = at
        tris = []
        for y in self.levels:
            for i, j in itertools.combinations(range(len(self.rays)), 2):
                tris.append((apex, at(self.rays[i], y), at(self.rays[j], y)))
        # reveal order: small ones first, then bigger
        tris.sort(key=lambda tr: (abs((tr[1][0] - tr[2][0]) * (tr[1][1] - ay)), tr[1][0]))
        self.tris = tris
        assert len(tris) == math.comb(len(self.rays), 2) * len(self.levels)
        self.targets = [((a[0] + b[0] + c_[0]) / 3, (a[1] + b[1] + c_[1]) / 3 + 40) for a, b, c_ in tris]
        self.values = [1] * len(tris)
        self.items = []
        t0, t1 = 0.05, 0.05 + hunt
        self.lv = [[t0, t1, 0, None, (0, 0)]]
        self.t_freeze = t1
        v2 = segs[1][1] - segs[1][0]
        self.t_count = self.t_freeze + v2 + 0.2
        self.t_reveal = self.t_count + 3.0
        self.dur = self.t_reveal + max(segs[2][1] - segs[2][0], step * len(tris) + 2.5) + 1.4
        self.voice_at = [0.0, self.t_freeze, self.t_reveal]
        self.answer = len(tris)
        json.dump(dict(answer=self.answer, dur=self.dur), open(f"{d}/game.json", "w"))

    def figure(self, c, a=1.0):
        ax, ay = self.apex
        for r in self.rays:
            c.move_to(ax, ay); c.line_to(*r)
        for y in self.levels:
            c.move_to(*self.at(self.rays[0], y)); c.line_to(*self.at(self.rays[-1], y))
        c.set_source_rgba(1, 1, 1, a); c.set_line_width(12); c.set_line_cap(cairo.LINE_CAP_ROUND); c.stroke()

    def frame(self, i):
        t = i / FPS
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        c = cairo.Context(sf)
        g = cairo.LinearGradient(0, 0, 0, VH)
        g.add_color_stop_rgb(0, 0.08, 0.06, 0.16); g.add_color_stop_rgb(1, 0.04, 0.03, 0.07)
        c.set_source(g); c.paint()
        S.rrect(c, 60, 470, 960, 1000, 30); c.set_source_rgba(1, 1, 1, 0.05); c.fill()
        n_on = 0
        if t >= self.t_reveal:
            for n, (a, b, cc) in enumerate(self.tris):
                t_on = self.t_reveal + 0.2 + n * self.step
                if t < t_on:
                    break
                n_on = n + 1
                cur = t < t_on + self.step
                al = 0.85 if cur else 0.18
                c.move_to(*a); c.line_to(*b); c.line_to(*cc); c.close_path()
                c.set_source_rgba(*TCOLS[n % len(TCOLS)], al); c.fill()
        self.figure(c, U.eob(k(t, 0.05, 0.5)))
        if n_on:
            n = n_on - 1
            if t < self.t_reveal + 0.2 + n_on * self.step or True:
                x, y = self.targets[n]
                c.arc(x, y, 40, 0, 2 * math.pi); c.set_source_rgba(*GRN, 1); c.fill()
                T(c, str(n_on), x, y + 15, 44, (0.03, 0.1, 0.05), stroke=None)
        sf.flush()
        rgb = VS.FXV.post(sf, 'studio', i, 0)
        ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        o = cairo.Context(ov)
        self.overlay(o, t)
        ov.flush()
        cb = np.ndarray((VH, VW, 4), np.uint8, ov.get_data())
        al = cb[..., 3:4].astype(np.float32) / 255.0
        return np.clip(rgb.astype(np.float32) * (1 - al) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)
