"""Same Bro GAMES: NUMBER SEQUENCE memory engine (campaign100, 11 Nov 2026) — 'which order was it?'.
N digits flash one by one in the centre (big card, progress dots), then 3 option cards A/B/C with the full sequence
(two decoys have one adjacent swap each) and a short timer. Freeze 'STOP! WHICH ORDER? COMMENT A, B or C' + 3-2-1,
then the right card goes green, decoys dim with the swapped digits marked red, and the sequence replays small on top.
Loop ending ('PLAY AGAIN').
Voice: one take, 3 lines (intro / freeze / reveal) like memgame.MemGame (audio + render + preview reused from OddGrid).
Usage: see studio/shorts/c141_numseq/make.py."""
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
INK = (0.12, 0.12, 0.16)
DIGC = [(0.95, 0.45, 0.35), (0.35, 0.7, 0.95), (0.98, 0.8, 0.3), (0.45, 0.85, 0.5), (0.8, 0.5, 0.95),
        (0.98, 0.6, 0.2), (0.4, 0.9, 0.85), (0.95, 0.5, 0.7), (0.7, 0.8, 0.4)]


class NumSeq(OG.OddGrid):
    def __init__(self, d, segs, caps, title, series, seq="4719382", options=("4791382", "4719382", "4719832"),
                 answer='B', step=0.85, t0=1.6, hunt=4.0, mood='chill', ask="WHICH ORDER? COMMENT A, B or C"):
        self.d, self.segs, self.caps, self.title, self.series, self.mood = d, segs, caps, title, series, mood
        self.seq, self.options, self.answer, self.step, self.ask = seq, options, answer, step, ask
        assert options['ABC'.index(answer)] == seq
        self.t_flash0 = t0
        self.t_flash1 = t0 + step * len(seq)
        self.t_opts = self.t_flash1 + 0.4
        self.t_freeze = self.t_opts + hunt
        self.lv = [[0.05, self.t_freeze, 0, None, (0, 0)]]
        v2 = segs[1][1] - segs[1][0]
        self.t_count = self.t_freeze + v2 + 0.2
        self.t_reveal = self.t_count + 3.0
        self.dur = self.t_reveal + max(segs[2][1] - segs[2][0], 3.0) + 1.4
        self.voice_at = [0.0, self.t_freeze, self.t_reveal]
        json.dump(dict(answer=answer, seq=seq, options=list(options), dur=self.dur), open(f"{d}/game.json", "w"))

    # ---------- drawing ----------
    def big_digit(self, c, t):
        i = int((t - self.t_flash0) / self.step)
        f = (t - self.t_flash0 - i * self.step) / self.step
        if not (0 <= i < len(self.seq)):
            return
        dg = self.seq[i]
        col = DIGC[int(dg) % len(DIGC)]
        sc = U.eob(min(1, f / 0.18)) * (1 if f < 0.8 else max(0.0, 1 - (f - 0.8) / 0.2))
        c.save(); c.translate(540, 900); c.scale(max(0.02, sc), max(0.02, sc))
        S.rrect(c, -230, -280, 460, 560, 60); c.set_source_rgb(0.96, 0.95, 0.92); c.fill()
        S.rrect(c, -230, -280, 460, 560, 60); c.set_source_rgb(*col); c.set_line_width(16); c.stroke()
        T(c, dg, 0, 150, 420, INK, stroke=None)
        c.restore()
        # progress dots
        n = len(self.seq)
        for j in range(n):
            x = 540 + (j - (n - 1) / 2) * 70
            c.arc(x, 1300, 18, 0, 2 * math.pi)
            c.set_source_rgba(*(YEL if j <= i else (1, 1, 1)), 1 if j <= i else 0.25); c.fill()

    def opt_card(self, c, t, idx, a=1.0, state=None):
        lab = 'ABC'[idx]
        s = self.options[idx]
        y = 560 + idx * 300
        S.rrect(c, 90, y, 900, 240, 44)
        bg = (0.12, 0.13, 0.2)
        if state == 'right':
            bg = (0.08, 0.4, 0.17)
        c.set_source_rgba(*bg, 0.96 * a); c.fill()
        if state == 'right':
            S.rrect(c, 90, y, 900, 240, 44); c.set_source_rgba(*GRN, a); c.set_line_width(10); c.stroke()
        c.arc(190, y + 120, 62, 0, 2 * math.pi); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 190, y + 148, 80, (0.08, 0.08, 0.1), a, stroke=None)
        dim = 0.35 if state == 'wrong' else 1.0
        for j, ch in enumerate(s):
            x = 330 + j * 92
            bad = state == 'wrong' and ch != self.seq[j]
            if bad:
                c.arc(x, y + 112, 46, 0, 2 * math.pi); c.set_source_rgba(*RED, 0.9 * a); c.fill()
            T(c, ch, x, y + 150, 100, WHITE, a * (1.0 if bad else dim), stroke=None)
        if state == 'wrong':
            c.move_to(110, y + 20); c.line_to(970, y + 220); c.set_source_rgba(*RED, 0.6 * a); c.set_line_width(8); c.stroke()

    def frame(self, i):
        t = i / FPS
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        c = cairo.Context(sf)
        g = cairo.LinearGradient(0, 0, 0, VH)
        g.add_color_stop_rgb(0, 0.08, 0.06, 0.16); g.add_color_stop_rgb(1, 0.04, 0.03, 0.07)
        c.set_source(g); c.paint()
        if t < self.t_flash0:
            # 'get ready' card with the question so the game is clear in the first seconds
            pulse = 1 + 0.04 * math.sin(t * 8)
            c.save(); c.translate(540, 900); c.scale(pulse, pulse)
            S.rrect(c, -230, -280, 460, 560, 60); c.set_source_rgb(0.25, 0.2, 0.55); c.fill()
            T(c, "?", 0, 150, 420, (0.6, 0.55, 0.95), stroke=None)
            c.restore()
        elif t < self.t_opts:
            self.big_digit(c, t)
        else:
            rv = t >= self.t_reveal
            for j in range(3):
                d0 = self.t_opts + j * 0.25
                a = k(t, d0, d0 + 0.3)
                if a <= 0:
                    continue
                st = None
                if rv:
                    st = 'right' if 'ABC'[j] == self.answer else 'wrong'
                self.opt_card(c, t, j, a, st)
            if rv:   # replay the sequence small on top
                for j, ch in enumerate(self.seq):
                    a = k(t, self.t_reveal + 0.6 + j * 0.15, self.t_reveal + 0.8 + j * 0.15)
                    x = 540 + (j - (len(self.seq) - 1) / 2) * 96
                    S.rrect(c, x - 40, 1430, 80, 100, 16); c.set_source_rgba(0.96, 0.95, 0.92, a); c.fill()
                    T(c, ch, x, 1510, 76, INK, a, stroke=None)
        sf.flush()
        rgb = VS.FXV.post(sf, 'studio', i, 0)
        ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        o = cairo.Context(ov)
        self.overlay(o, t)
        ov.flush()
        cb = np.ndarray((VH, VW, 4), np.uint8, ov.get_data())
        al = cb[..., 3:4].astype(np.float32) / 255.0
        return np.clip(rgb.astype(np.float32) * (1 - al) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)

    def timer(self, o, fr):
        S.rrect(o, 110, 400, 860, 24, 12); o.set_source_rgba(1, 1, 1, 0.12); o.fill()
        S.rrect(o, 110, 400, max(24, 860 * fr), 24, 12); o.set_source_rgba(*(RED if fr < 0.3 else GRN), 0.95); o.fill()

    def overlay(self, o, t):
        S.rrect(o, 300, 60, 480, 58, 29); o.set_source_rgba(*YEL, 0.95); o.fill()
        T(o, self.series, 540, 100, 30, (0.08, 0.08, 0.1), stroke=None)
        if t < self.t_opts:
            T(o, self.title[0], 540, 225, 80, WHITE, lw=12)
            T(o, self.title[1], 540, 318, 50, YEL, lw=10)
            if t >= self.t_flash0:
                self.timer(o, 1 - (t - self.t_flash0) / (self.t_flash1 - self.t_flash0))
        elif t < self.t_freeze:
            T(o, "WHICH ORDER WAS IT?", 540, 240, 72, WHITE, lw=12)
            T(o, "A, B or C", 540, 330, 56, YEL, lw=10)
            self.timer(o, 1 - (t - self.t_opts) / (self.t_freeze - self.t_opts))
        elif t < self.t_reveal:
            T(o, "STOP!", 540, 250, 120, RED, lw=14)
            S.rrect(o, 100, 320, 880, 96, 48); o.set_source_rgba(0.05, 0.05, 0.08, 0.92); o.fill()
            T(o, self.ask, 540, 384, 42, YEL, stroke=None)
            if t > self.t_count:
                m = 3 - int(t - self.t_count)
                f = (t - self.t_count) % 1
                sc = 1.4 - 0.4 * U.eob(min(1, f / 0.2))
                o.save(); o.translate(940, 200); o.scale(sc, sc)
                o.arc(0, 0, 80, 0, 2 * math.pi); o.set_source_rgba(0.05, 0.05, 0.08, 0.9); o.fill()
                T(o, str(max(1, m)), 0, 38, 110, WHITE, lw=8)
                o.restore()
        else:
            T(o, f"ANSWER: {self.answer}!", 540, 270, 96, GRN, k(t, self.t_reveal + 0.3, self.t_reveal + 0.6), lw=12)
            T(o, "Red = swapped numbers", 540, 360, 44, WHITE, k(t, self.t_reveal + 1.0, self.t_reveal + 1.3), lw=8)
            if t > self.dur - 2.4:
                K.stamp(o, t, self.dur - 2.4, "PLAY AGAIN >", 540, 1610, RED, 54, -0.04)
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
                        T(o, " ".join(g), 540, 1730, 58, WHITE, lw=12)
                        break
                    tc += dd
        S.rrect(o, 425, 1838, 230, 56, 28); o.set_source_rgb(0.06, 0.06, 0.08); o.fill_preserve()
        o.set_source_rgb(*YEL); o.set_line_width(4); o.stroke()
        T(o, "SAME BRO", 540, 1877, 30, YEL, stroke=None)
