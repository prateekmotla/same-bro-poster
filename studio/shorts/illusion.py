"""SAME BRO GAMES: optical-illusion quiz engine (campaign100, 10 Nov 2026).
Levels alternate question line / answer line in vo.txt. Each level supplies draw(c, t, r) where r = reveal 0..1
(0 during the question, eases to 1 on the answer line) — the level draws its figure plus its own measuring guides.
Usage: see studio/shorts/s88_lines/make.py.  levels: list of dict(name, draw, labels=[(txt, x, y)], q='WHICH IS LONGER?',
ans='SAME LENGTH!'), one per (question, answer) line pair."""
import math
import sys

import cairo
import numpy as np

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from vshort import S, U, T, YEL, RED, GRN, WHITE, FXV  # noqa: E402

VW, VH, FPS = VS.VW, VS.VH, VS.FPS
k = U.k


def dashed(c, x0, y0, x1, y1, col=YEL, a=1.0, w=5, dash=18):
    c.save(); c.set_dash([dash, dash * 0.7]); c.move_to(x0, y0); c.line_to(x1, y1)
    c.set_source_rgba(*col, a); c.set_line_width(w); c.stroke(); c.restore()


class Illusion(VS.Short):
    def __init__(self, d, caps, levels, series, title, mood='chill'):
        super().__init__(d, caps, [], [], None)
        assert len(self.txt) == len(caps) == 2 * len(levels), "need one question + one answer line per level"
        self.levels, self.series, self.title, self.mood = levels, series, title, mood

    def frame(self, i):
        t = i / FPS
        idx = next((j for j, (a, b) in enumerate(self.L) if t < b), len(self.L) - 1)
        lv = self.levels[idx // 2]
        ans = idx % 2 == 1
        st, en = self.L[idx]
        r = U.eob(k(t, st + 0.3, st + 1.3)) if ans else 0.0
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        c = cairo.Context(sf)
        g = cairo.LinearGradient(0, 0, 0, VH)
        g.add_color_stop_rgb(0, 0.1, 0.09, 0.16); g.add_color_stop_rgb(1, 0.05, 0.05, 0.09)
        c.rectangle(0, 0, VW, VH); c.set_source(g); c.fill()
        # soft spotlight
        rg = cairo.RadialGradient(540, 960, 50, 540, 960, 900)
        rg.add_color_stop_rgba(0, 1, 1, 1, 0.06); rg.add_color_stop_rgba(1, 1, 1, 1, 0)
        c.rectangle(0, 0, VW, VH); c.set_source(rg); c.fill()
        intro = k(t, st, st + 0.25) if not ans else 1.0
        c.save()
        sc = 0.92 + 0.08 * U.eob(intro)
        c.translate(540, 960); c.scale(sc, sc); c.translate(-540, -960)
        lv['draw'](c, t, r)
        if not ans:
            for txt, x, y in lv.get('labels', []):
                c.arc(x, y, 46, 0, 2 * math.pi); c.set_source_rgba(*YEL, intro); c.fill()
                T(c, txt, x, y + 18, 50, (0.08, 0.08, 0.1), intro, stroke=None)
        c.restore()
        sf.flush()
        rgb = FXV.post(sf, 'studio', i, 0)
        ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        o = cairo.Context(ov)
        # top: series pill + level + question
        S.rrect(o, 270, 60, 540, 56, 28); o.set_source_rgba(*YEL, 0.95); o.fill()
        T(o, self.series, 540, 99, 30, (0.08, 0.08, 0.1), stroke=None)
        if t < 2.2:
            a = min(1, t / 0.15) * min(1, (2.2 - t) / 0.3)
            S.rrect(o, 60, 150, 960, 230, 30); o.set_source_rgba(0.02, 0.02, 0.04, 0.85 * a); o.fill()
            T(o, self.title[0], 540, 245, 74, WHITE, a, lw=10)
            T(o, self.title[1], 540, 335, 64, YEL, a, lw=10)
        else:
            T(o, lv['name'], 540, 210, 44, (0.75, 0.75, 0.85), stroke=None)
            T(o, lv.get('q', 'WHICH IS LONGER?') if not ans else lv.get('ans', 'SAME!'), 540, 300, 72,
              WHITE if not ans else GRN, lw=10)
        if not ans:
            fr = k(t, en - 1.6, en)
            if fr > 0:
                o.set_line_width(12); o.set_source_rgba(*YEL, 0.95)
                o.arc(540, 1560, 50, -math.pi / 2, -math.pi / 2 + 2 * math.pi * (1 - fr)); o.stroke()
                T(o, "COMMENT NOW", 540, 1660, 40, YEL, stroke=None)
        else:
            K.stamp(o, t, st + 1.2, lv.get('stamp', 'SAME!'), 540, 1560, GRN, 64, -0.05)
        self.caption(o, t)
        S.rrect(o, 425, 1838, 230, 56, 28); o.set_source_rgb(0.06, 0.06, 0.08); o.fill_preserve()
        o.set_source_rgb(*YEL); o.set_line_width(4); o.stroke()
        T(o, "SAME BRO", 540, 1877, 30, YEL, stroke=None)
        ov.flush()
        cb = np.ndarray((VH, VW, 4), np.uint8, ov.get_data())
        al = cb[..., 3:4].astype(np.float32) / 255.0
        return np.clip(rgb.astype(np.float32) * (1 - al) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)

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
                    hi = any((w.strip('".,:?!').isupper() and len(w.strip('".,:?!')) > 1) for w in g)
                    c.save(); c.translate(540, 1765); c.scale(0.85 + 0.15 * kk, 0.85 + 0.15 * kk)
                    T(c, txt, 0, 0, 60 if len(txt) < 20 else 52, YEL if hi else WHITE, lw=12)
                    c.restore()
                    return
                tc += dd
            return
