"""Same Bro GAMES: COUNT IT engine (campaign100, 10 Nov 2026).
A pile of mixed objects (default: Indian coins ₹1/₹2/₹5/₹10, each clearly labelled) scattered on a table; count only
the target kind before the timer ends. Freeze 'STOP! HOW MANY? COMMENT THE NUMBER' + 3-2-1, then each target is ringed
and numbered one by one, total stamped. Loop ending ('PLAY AGAIN').
Voice: one take, 3 lines (intro / freeze / reveal) like oddgrid.OddGrid (audio + render reused from it).
Usage: see studio/shorts/s80_coins/make.py."""
import json
import math
import random
import sys

import cairo
import numpy as np

sys.path.insert(0, "/home/claude/sid/shorts")
import oddgrid as OG  # noqa: E402
import kit as K  # noqa: E402
import vshort as VS  # noqa: E402
from kit import T, k, U, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

VW, VH, FPS = OG.VW, OG.VH, OG.FPS
BOX = (60, 470, 960, 1180)   # table area x, y, w, h
SILV = (0.78, 0.79, 0.83)
GOLD = (0.86, 0.7, 0.3)


def coin(c, x, y, kind, rot=0.0, a=1.0):
    """kind: 1, 2, 5 or 10 (generic, labelled; ₹10 is bimetallic)."""
    r = {1: 40, 2: 46, 5: 44, 10: 50}[kind]
    c.save(); c.translate(x, y); c.rotate(rot)
    if kind == 10:
        c.arc(0, 0, r, 0, 2 * math.pi); c.set_source_rgba(*GOLD, a); c.fill()
        c.arc(0, 0, r * 0.7, 0, 2 * math.pi); c.set_source_rgba(*SILV, a); c.fill()
    elif kind == 5:
        c.arc(0, 0, r, 0, 2 * math.pi); c.set_source_rgba(0.85, 0.72, 0.42, a); c.fill()
    else:
        c.arc(0, 0, r, 0, 2 * math.pi); c.set_source_rgba(*SILV, a); c.fill()
    c.arc(0, 0, r * 0.92, 0, 2 * math.pi); c.set_source_rgba(0.45, 0.45, 0.5, a); c.set_line_width(3); c.stroke()
    T(c, f"₹{kind}", 0, r * 0.2, r * 0.62 if kind < 10 else r * 0.55, (0.25, 0.2, 0.1), a, stroke=None)
    c.restore()


class CountGame(OG.OddGrid):
    def __init__(self, d, segs, caps, title, series, target=10, n_target=9, others=((1, 6), (2, 6), (5, 7)), hunt=12.0,
                 seed=3, mood='chill', draw=coin, total=False, gap=112, step=0.35, margin=70):
        """total=True: count ALL items and add their values (kinds = values); reveal shows a running ₹ total."""
        self.d, self.segs, self.caps, self.title, self.series, self.mood = d, segs, caps, title, series, mood
        self.draw, self.target, self.total, self.step = draw, target, total, step
        rnd = random.Random(seed)
        kinds = ([] if total else [target] * n_target) + [kk for kk, n in others for _ in range(n)]
        rnd.shuffle(kinds)
        pts = []
        x0, y0, w, h = BOX
        for kd in kinds:
            for _ in range(2000):
                p = (x0 + margin + rnd.random() * (w - 2 * margin), y0 + margin + rnd.random() * (h - 2 * margin))
                if all(math.dist(p, q) > gap for q, _, _ in pts):
                    break
            pts.append((p, kd, rnd.uniform(-0.6, 0.6)))
        self.items = pts
        sel = [(p, kd) for p, kd, _ in pts if total or kd == target]
        sel.sort(key=lambda e: (e[0][1] // 200, e[0][0]))
        self.targets = [p for p, _ in sel]
        self.values = [kd for _, kd in sel]
        if total:
            n_target = sum(self.values)
        t0, t1 = 0.05, 0.05 + hunt
        self.lv = [[t0, t1, 0, None, (0, 0)]]
        self.t_freeze = t1
        v2 = segs[1][1] - segs[1][0]
        self.t_count = self.t_freeze + v2 + 0.2
        self.t_reveal = self.t_count + 3.0
        self.dur = self.t_reveal + max(segs[2][1] - segs[2][0], step * len(self.targets) + 2.5) + 1.4
        self.voice_at = [0.0, self.t_freeze, self.t_reveal]
        self.answer = n_target
        json.dump(dict(answer=n_target, dur=self.dur), open(f"{d}/game.json", "w"))

    def frame(self, i):
        t = i / FPS
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        c = cairo.Context(sf)
        g = cairo.LinearGradient(0, 0, 0, VH)
        g.add_color_stop_rgb(0, 0.08, 0.06, 0.16); g.add_color_stop_rgb(1, 0.04, 0.03, 0.07)
        c.set_source(g); c.paint()
        x0, y0, w, h = BOX
        wood = cairo.LinearGradient(0, y0, 0, y0 + h)
        wood.add_color_stop_rgb(0, 0.45, 0.3, 0.18); wood.add_color_stop_rgb(1, 0.33, 0.21, 0.12)
        S.rrect(c, x0, y0, w, h, 26); c.set_source(wood); c.fill()
        for j in range(9):
            c.move_to(x0 + 10, y0 + 60 + j * 130 + 10 * math.sin(j)); c.rel_curve_to(300, 20, 600, -20, w - 20, 8)
            c.set_source_rgba(0, 0, 0, 0.12); c.set_line_width(4); c.stroke()
        for n, ((x, y), kd, rot) in enumerate(self.items):
            pop = U.eob(k(t, 0.05 + n * 0.03, 0.3 + n * 0.03))
            if pop <= 0:
                continue
            c.save(); c.translate(x, y); c.scale(pop, pop)
            self.draw(c, 0, 0, kd, rot)
            c.restore()
        if t >= self.t_reveal:
            for n, (x, y) in enumerate(self.targets):
                a = k(t, self.t_reveal + 0.2 + n * self.step, self.t_reveal + 0.4 + n * self.step)
                if a <= 0:
                    continue
                c.arc(x, y, 62 * (1.5 - 0.5 * U.eob(a)), 0, 2 * math.pi); c.set_source_rgba(*GRN, a); c.set_line_width(8); c.stroke()
                if self.total:
                    lab = f"+{self.values[n]}"
                    S.rrect(c, x + 10, y - 80, 30 + 22 * len(lab), 50, 25); c.set_source_rgba(*GRN, a); c.fill()
                    T(c, lab, x + 25 + 11 * len(lab), y - 43, 32, (0.03, 0.1, 0.05), a, stroke=None)
                else:
                    c.arc(x + 46, y - 46, 24, 0, 2 * math.pi); c.set_source_rgba(*GRN, a); c.fill()
                    T(c, str(n + 1), x + 46, y - 35, 30, (0.03, 0.1, 0.05), a, stroke=None)
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
        if t < self.t_freeze:
            T(o, self.title[0], 540, 225, 84, WHITE, lw=12)
            T(o, self.title[1], 540, 318, 58, YEL, lw=10)
            fr = 1 - (t - t0) / (t1 - t0)
            S.rrect(o, 110, 380, 860, 24, 12); o.set_source_rgba(1, 1, 1, 0.12); o.fill()
            S.rrect(o, 110, 380, max(24, 860 * fr), 24, 12); o.set_source_rgba(*(RED if fr < 0.3 else GRN), 0.95); o.fill()
        elif t < self.t_reveal:
            T(o, "STOP!", 540, 240, 120, RED, lw=14)
            S.rrect(o, 120, 310, 840, 96, 48); o.set_source_rgba(0.05, 0.05, 0.08, 0.92); o.fill()
            T(o, "TOTAL? COMMENT THE AMOUNT" if self.total else "HOW MANY? COMMENT THE NUMBER", 540, 374, 44, YEL, stroke=None)
            if t > self.t_count:
                m = 3 - int(t - self.t_count)
                f = (t - self.t_count) % 1
                sc = 1.4 - 0.4 * U.eob(min(1, f / 0.2))
                o.save(); o.translate(960, 220); o.scale(sc, sc)
                o.arc(0, 0, 80, 0, 2 * math.pi); o.set_source_rgba(0.05, 0.05, 0.08, 0.9); o.fill()
                T(o, str(max(1, m)), 0, 38, 110, WHITE, lw=8)
                o.restore()
        else:
            n = len(self.targets)
            done = t > self.t_reveal + 0.4 + n * self.step
            if self.total:
                m = sum(1 for j in range(n) if t > self.t_reveal + 0.4 + j * self.step)
                run = sum(self.values[:m])
                T(o, f"TOTAL: ₹{self.answer}" if done else f"₹{run}", 540, 260, 90 if done else 80, GRN if done else WHITE, lw=12)
            else:
                T(o, f"ANSWER: {self.answer}" if done else "COUNTING...", 540, 260, 90 if done else 70, GRN if done else WHITE, lw=12)
            if t > self.dur - 2.4:
                K.stamp(o, t, self.dur - 2.4, "PLAY AGAIN >", 540, 380, RED, 54, -0.04)
        for n_, (a0, a1) in enumerate(self.segs):
            st = self.voice_at[n_]
            ln = a1 - a0
            if st <= t < st + ln + 0.2:
                ws = self.caps[n_].split()
                groups, cur = [], []
                for w_ in ws:
                    cur.append(w_)
                    if len(cur) >= 4 or w_[-1] in ".,?!:":
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
