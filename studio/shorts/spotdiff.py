"""Same Bro GAMES: SPOT THE DIFFERENCE engine (campaign100, 10 Nov 2026).
Two copies of one vector scene (A top, B bottom). B gets N small, fair changes (colour swap / extra object / changed
detail) drawn by the topic. Timer bar while hunting, freeze 'STOP! HOW MANY? COMMENT 1, 2 or 3' + 3-2-1, then each
difference is circled on BOTH pictures, one by one, numbered. Loop ending ('PLAY AGAIN').
Voice: one take, 3 lines (intro / freeze / reveal), split by time ranges like oddgrid.OddGrid (audio/render reused).
Topic supplies scene(c, t) in a 1920x1080 world and diffs = [(x, y, r, draw_b)] where draw_b(c, t) paints the change
on picture B only (world coords). Usage: see studio/shorts/s76_spot/make.py."""
import json
import math
import sys

import cairo
import numpy as np

sys.path.insert(0, "/home/claude/sid/shorts")
import oddgrid as OG  # noqa: E402
import kit as K  # noqa: E402
import vshort as VS  # noqa: E402
from kit import T, k, U, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

VW, VH, FPS = OG.VW, OG.VH, OG.FPS
PX, PW = 40, 1000
SC = PW / 1920
PH = 1080 * SC
PY = (450, 450 + PH + 36)          # A, B panel tops


class SpotDiff(OG.OddGrid):
    def __init__(self, d, segs, caps, title, series, scene, diffs, hunt=14.0, mood='chill', label="SID'S ROOM"):
        self.d, self.segs, self.caps, self.title, self.series, self.mood = d, segs, caps, title, series, mood
        self.scene, self.diffs, self.label = scene, diffs, label
        t0, t1 = 0.05, 0.05 + hunt
        self.lv = [[t0, t1, 0, None, (0, 0)]]
        self.t_freeze = t1
        v2 = segs[1][1] - segs[1][0]
        self.t_count = self.t_freeze + v2 + 0.2
        self.t_reveal = self.t_count + 3.0
        self.dur = self.t_reveal + max(segs[2][1] - segs[2][0], 0.7 * len(diffs) + 1.5) + 1.4
        self.voice_at = [0.0, self.t_freeze, self.t_reveal]
        self.answer = len(diffs)
        json.dump(dict(diffs=[(x, y) for x, y, *_ in diffs], dur=self.dur), open(f"{d}/game.json", "w"))

    def pic(self, c, t, which):
        y0 = PY[which]
        c.save()
        S.rrect(c, PX - 8, y0 - 8, PW + 16, PH + 16, 18); c.set_source_rgb(0.95, 0.95, 0.97); c.fill()
        c.rectangle(PX, y0, PW, PH); c.clip()
        c.translate(PX, y0); c.scale(SC, SC)
        self.scene(c, 1.0)          # static scene (t fixed: no motion = fair game)
        if which == 1:
            for x, y, r, draw_b in self.diffs:
                draw_b(c, 1.0)
        c.restore()
        S.rrect(c, PX + 14, y0 + 14, 70, 60, 14); c.set_source_rgba(0.05, 0.05, 0.08, 0.85); c.fill()
        T(c, "AB"[which], PX + 49, y0 + 58, 40, YEL, stroke=None)

    def rings(self, c, t):
        for n, (x, y, r, _) in enumerate(self.diffs):
            a = k(t, self.t_reveal + 0.2 + n * 0.7, self.t_reveal + 0.5 + n * 0.7)
            if a <= 0:
                continue
            for which in (0, 1):
                cx, cy = PX + x * SC, PY[which] + y * SC
                rr = r * SC * (1.7 - 0.7 * U.eob(a))
                c.arc(cx, cy, rr, 0, 2 * math.pi); c.set_source_rgba(*GRN, a); c.set_line_width(9); c.stroke()
                c.arc(cx + rr * 0.75, cy - rr * 0.75, 26, 0, 2 * math.pi); c.set_source_rgba(*GRN, a); c.fill()
                T(c, str(n + 1), cx + rr * 0.75, cy - rr * 0.75 + 12, 34, (0.03, 0.1, 0.05), a, stroke=None)

    def frame(self, i):
        t = i / FPS
        self._now = t
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        c = cairo.Context(sf)
        g = cairo.LinearGradient(0, 0, 0, VH)
        g.add_color_stop_rgb(0, 0.08, 0.06, 0.16); g.add_color_stop_rgb(0.6, 0.13, 0.07, 0.2); g.add_color_stop_rgb(1, 0.04, 0.03, 0.07)
        c.set_source(g); c.paint()
        pop = U.eob(k(t, 0.0, 0.35))
        for which in (0, 1):
            c.save(); c.translate(540, PY[which] + PH / 2); c.scale(pop, pop); c.translate(-540, -(PY[which] + PH / 2))
            self.pic(c, t, which)
            c.restore()
        self.rings(c, t)
        sf.flush()
        rgb = VS.FXV.post(sf, 'studio', i, 0)
        ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        o = cairo.Context(ov)
        self.overlay(o, t)
        ov.flush()
        cb = np.ndarray((VH, VW, 4), np.uint8, ov.get_data())
        al = cb[..., 3:4].astype(np.float32) / 255.0
        return np.clip(rgb.astype(np.float32) * (1 - al) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)

    def overlay(self, o, t):
        S.rrect(o, 300, 60, 480, 58, 29); o.set_source_rgba(*YEL, 0.95); o.fill()
        T(o, self.series, 540, 100, 30, (0.08, 0.08, 0.1), stroke=None)
        t0, t1 = self.lv[0][0], self.lv[0][1]
        n = len(self.diffs)
        if t < self.t_freeze:
            T(o, self.title[0], 540, 225, 84, WHITE, lw=12)
            T(o, self.title[1], 540, 318, 58, YEL, lw=10)
            fr = 1 - (t - t0) / (t1 - t0)
            S.rrect(o, 110, 372, 860, 24, 12); o.set_source_rgba(1, 1, 1, 0.12); o.fill()
            S.rrect(o, 110, 372, max(24, 860 * fr), 24, 12); o.set_source_rgba(*(RED if fr < 0.3 else GRN), 0.95); o.fill()
        elif t < self.t_reveal:
            T(o, "STOP!", 540, 240, 120, RED, lw=14)
            S.rrect(o, 90, 310, 900, 96, 48); o.set_source_rgba(0.05, 0.05, 0.08, 0.92); o.fill()
            T(o, "HOW MANY? COMMENT " + ", ".join(str(j + 1) for j in range(n - 1)) + f" or {n}", 540, 374, 44, YEL,
              stroke=None)
            if t > self.t_count:
                m = 3 - int(t - self.t_count)
                f = (t - self.t_count) % 1
                sc = 1.4 - 0.4 * U.eob(min(1, f / 0.2))
                o.save(); o.translate(960, 220); o.scale(sc, sc)
                o.arc(0, 0, 80, 0, 2 * math.pi); o.set_source_rgba(0.05, 0.05, 0.08, 0.9); o.fill()
                T(o, str(max(1, m)), 0, 38, 110, WHITE, lw=8)
                o.restore()
        else:
            T(o, f"ALL {n} DIFFERENCES", 540, 250, 70, GRN, k(t, self.t_reveal + 0.2, self.t_reveal + 0.5), lw=12)
            if t > self.dur - 2.4:
                K.stamp(o, t, self.dur - 2.4, "PLAY AGAIN >", 540, 370, RED, 54, -0.04)
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
                        T(o, " ".join(g), 540, 1720, 58, WHITE, lw=12)
                        break
                    tc += dd
        S.rrect(o, 425, 1838, 230, 56, 28); o.set_source_rgb(0.06, 0.06, 0.08); o.fill_preserve()
        o.set_source_rgb(*YEL); o.set_line_width(4); o.stroke()
        T(o, "SAME BRO", 540, 1877, 30, YEL, stroke=None)
