"""Same Bro GAMES: MEMORY FLASH engine (campaign100, 10 Nov 2026) — 'which item vanished?'.
9 everyday items on cards (3x3) with a MEMORIZE timer; cards flip over (blink); 8 come back SHUFFLED and one card
shows '?'. Freeze 'STOP! WHICH ONE VANISHED? COMMENT' + 3-2-1, then the missing item flies into the '?' card, green
ring + name stamped. Loop ending ('PLAY AGAIN').
Voice: one take, 3 lines (intro / freeze / reveal) like oddgrid.OddGrid (audio + render + preview reused from it).
Usage: see studio/shorts/s92_memory/make.py."""
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
GX, GY, CELL = 90, 470, 300     # grid origin and cell size (3x3 -> 900 px)
INK = (0.12, 0.12, 0.16)


# ---------- item icons, drawn centred at (0, 0), ~ +-90 px ----------
def i_phone(c):
    S.rrect(c, -45, -85, 90, 170, 16); c.set_source_rgb(*INK); c.fill()
    S.rrect(c, -37, -72, 74, 140, 8); c.set_source_rgb(0.3, 0.55, 0.95); c.fill()


def i_key(c):
    c.arc(-40, 0, 32, 0, 2 * math.pi); c.set_source_rgb(0.9, 0.72, 0.2); c.fill()
    c.arc(-40, 0, 12, 0, 2 * math.pi); c.set_source_rgb(1, 1, 1); c.fill()
    c.rectangle(-12, -9, 95, 18); c.set_source_rgb(0.9, 0.72, 0.2); c.fill()
    for dx in (50, 70):
        c.rectangle(dx, 5, 11, 20); c.fill()


def i_glasses(c):
    for sx in (-1, 1):
        c.save(); c.translate(sx * 42, 5); c.scale(1, 0.8); c.arc(0, 0, 36, 0, 2 * math.pi); c.restore()
        c.set_source_rgb(*INK); c.fill()
    c.move_to(-8, -5); c.curve_to(-4, -14, 4, -14, 8, -5); c.set_source_rgb(*INK); c.set_line_width(7); c.stroke()
    c.move_to(-78, -5); c.line_to(-92, -18); c.move_to(78, -5); c.line_to(92, -18); c.stroke()


def i_watch(c):
    c.rectangle(-22, -85, 44, 170); c.set_source_rgb(0.35, 0.22, 0.14); c.fill()
    c.arc(0, 0, 42, 0, 2 * math.pi); c.set_source_rgb(0.75, 0.75, 0.8); c.fill()
    c.arc(0, 0, 34, 0, 2 * math.pi); c.set_source_rgb(1, 1, 1); c.fill()
    c.move_to(0, 0); c.line_to(0, -24); c.move_to(0, 0); c.line_to(16, 6); c.set_source_rgb(*INK); c.set_line_width(5); c.stroke()


def i_cup(c):
    c.move_to(-45, -50); c.line_to(45, -50); c.line_to(35, 60); c.line_to(-35, 60); c.close_path()
    c.set_source_rgb(0.95, 0.95, 0.92); c.fill_preserve(); c.set_source_rgb(0.6, 0.6, 0.6); c.set_line_width(4); c.stroke()
    c.rectangle(-42, -42, 84, 26); c.set_source_rgb(0.72, 0.45, 0.25); c.fill()
    for dx in (-15, 10):
        c.move_to(dx, -62); c.curve_to(dx - 10, -75, dx + 10, -85, dx, -98); c.set_source_rgba(0.7, 0.7, 0.7, 0.8)
        c.set_line_width(4); c.stroke()


def i_coin(c):
    c.arc(0, 0, 62, 0, 2 * math.pi); c.set_source_rgb(0.86, 0.7, 0.3); c.fill()
    c.arc(0, 0, 44, 0, 2 * math.pi); c.set_source_rgb(0.78, 0.79, 0.83); c.fill()
    T(c, "₹10", 0, 14, 36, (0.25, 0.2, 0.1), stroke=None)


def i_headphones(c):
    c.arc(0, 10, 62, math.pi, 2 * math.pi); c.set_source_rgb(*INK); c.set_line_width(14); c.stroke()
    for sx in (-1, 1):
        S.rrect(c, sx * 62 - 20, 0, 40, 70, 14); c.set_source_rgb(0.85, 0.2, 0.25); c.fill()


def i_pen(c):
    c.save(); c.rotate(-0.7)
    S.rrect(c, -80, -12, 140, 24, 8); c.set_source_rgb(0.15, 0.35, 0.8); c.fill()
    c.move_to(60, -12); c.line_to(90, 0); c.line_to(60, 12); c.close_path(); c.set_source_rgb(0.9, 0.8, 0.6); c.fill()
    c.rectangle(-70, -18, 40, 6); c.set_source_rgb(0.75, 0.75, 0.8); c.fill()
    c.restore()


def i_wallet(c):
    S.rrect(c, -75, -50, 150, 100, 14); c.set_source_rgb(0.42, 0.26, 0.15); c.fill()
    S.rrect(c, 20, -22, 60, 44, 10); c.set_source_rgb(0.55, 0.36, 0.2); c.fill()
    c.arc(45, 0, 7, 0, 2 * math.pi); c.set_source_rgb(0.9, 0.8, 0.4); c.fill()


ITEMS = dict(PHONE=i_phone, KEYS=i_key, SUNGLASSES=i_glasses, WATCH=i_watch, CHAI=i_cup, COIN=i_coin,
             HEADPHONES=i_headphones, PEN=i_pen, WALLET=i_wallet)


class MemGame(OG.OddGrid):
    def __init__(self, d, segs, caps, title, series, missing='SUNGLASSES', mem=8.0, hunt=5.0, seed=5, mood='chill'):
        self.d, self.segs, self.caps, self.title, self.series, self.mood = d, segs, caps, title, series, mood
        rnd = random.Random(seed)
        names = list(ITEMS)
        rnd.shuffle(names)
        self.pos1 = {n: p for n, p in zip(names, range(9))}           # first layout
        rest = [n for n in names if n != missing]
        slots = list(range(9))
        rnd.shuffle(slots)
        while slots[-1] == self.pos1[missing]:                         # '?' card in a different slot
            rnd.shuffle(slots)
        self.pos2 = {n: s for n, s in zip(rest, slots[:8])}
        self.qslot = slots[8]
        self.missing = missing
        self.t_mem = 0.05 + mem
        self.t_back = self.t_mem + 0.9
        self.lv = [[0.05, self.t_back + hunt, 0, None, (0, 0)]]
        self.t_freeze = self.t_back + hunt
        v2 = segs[1][1] - segs[1][0]
        self.t_count = self.t_freeze + v2 + 0.2
        self.t_reveal = self.t_count + 3.0
        self.dur = self.t_reveal + max(segs[2][1] - segs[2][0], 3.0) + 1.4
        self.voice_at = [0.0, self.t_freeze, self.t_reveal]
        self.answer = missing
        json.dump(dict(answer=missing, dur=self.dur), open(f"{d}/game.json", "w"))

    @staticmethod
    def cell(slot):
        r, cc = divmod(slot, 3)
        return GX + CELL * (cc + 0.5), GY + CELL * (r + 0.5)

    def card(self, c, slot, draw, flip=1.0, hl=None):
        x, y = self.cell(slot)
        c.save(); c.translate(x, y); c.scale(max(0.02, abs(flip)), 1)
        back = flip < 0
        S.rrect(c, -130, -130, 260, 260, 28)
        c.set_source_rgb(*((0.25, 0.2, 0.55) if back else (0.96, 0.95, 0.92))); c.fill()
        if back:
            T(c, "?", 0, 40, 120, (0.6, 0.55, 0.95), stroke=None)
        elif draw:
            draw(c)
        c.restore()

    def frame(self, i):
        t = i / FPS
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        c = cairo.Context(sf)
        g = cairo.LinearGradient(0, 0, 0, VH)
        g.add_color_stop_rgb(0, 0.08, 0.06, 0.16); g.add_color_stop_rgb(1, 0.04, 0.03, 0.07)
        c.set_source(g); c.paint()
        S.rrect(c, GX - 30, GY - 30, CELL * 3 + 60, CELL * 3 + 60, 36); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
        if t < self.t_mem:
            for n, s in self.pos1.items():
                pop = U.eob(k(t, 0.05 + s * 0.04, 0.3 + s * 0.04))
                if pop > 0:
                    x, y = self.cell(s)
                    c.save(); c.translate(x, y); c.scale(pop, pop); c.translate(-x, -y)
                    self.card(c, s, ITEMS[n]); c.restore()
        elif t < self.t_back:
            f = (t - self.t_mem) / (self.t_back - self.t_mem)        # 0..1 flip to back and to new front
            fl = math.cos(f * 2 * math.pi)                            # 1 -> -1 -> 1
            show_new = f > 0.5
            for s in range(9):
                if show_new:
                    n = next((n_ for n_, s_ in self.pos2.items() if s_ == s), None)
                else:
                    n = next((n_ for n_, s_ in self.pos1.items() if s_ == s), None)
                if show_new and s == self.qslot:
                    self.card(c, s, None, -max(0.02, abs(fl)))
                else:
                    self.card(c, s, ITEMS[n] if n else None, fl if fl > 0 else -max(0.02, -fl))
        else:
            for n, s in self.pos2.items():
                self.card(c, s, ITEMS[n])
            ra = k(t, self.t_reveal + 0.1, self.t_reveal + 0.6)
            x, y = self.cell(self.qslot)
            if ra <= 0:
                self.card(c, self.qslot, None, -1)
            else:
                self.card(c, self.qslot, None)
                c.save(); c.translate(x, y); sc = U.eob(ra); c.scale(sc, sc); ITEMS[self.missing](c); c.restore()
                c.arc(x, y, 175 * (1.5 - 0.5 * sc), 0, 2 * math.pi); c.set_source_rgba(*GRN, ra); c.set_line_width(10); c.stroke()
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
        if t < self.t_mem:
            T(o, self.title[0], 540, 225, 84, WHITE, lw=12)
            T(o, self.title[1], 540, 318, 54, YEL, lw=10)
            fr = 1 - t / self.t_mem
            S.rrect(o, 110, 380, 860, 24, 12); o.set_source_rgba(1, 1, 1, 0.12); o.fill()
            S.rrect(o, 110, 380, max(24, 860 * fr), 24, 12); o.set_source_rgba(*(RED if fr < 0.3 else GRN), 0.95); o.fill()
        elif t < self.t_freeze:
            T(o, "ONE IS GONE!", 540, 225, 90, RED, lw=12)
            T(o, "Cards got SHUFFLED too", 540, 318, 50, YEL, lw=10)
            fr = 1 - (t - self.t_back) / (self.t_freeze - self.t_back) if t > self.t_back else 1
            S.rrect(o, 110, 380, 860, 24, 12); o.set_source_rgba(1, 1, 1, 0.12); o.fill()
            S.rrect(o, 110, 380, max(24, 860 * fr), 24, 12); o.set_source_rgba(*(RED if fr < 0.3 else GRN), 0.95); o.fill()
        elif t < self.t_reveal:
            T(o, "STOP!", 540, 240, 120, RED, lw=14)
            S.rrect(o, 100, 310, 880, 96, 48); o.set_source_rgba(0.05, 0.05, 0.08, 0.92); o.fill()
            T(o, "WHICH ONE VANISHED? COMMENT", 540, 374, 42, YEL, stroke=None)
            if t > self.t_count:
                m = 3 - int(t - self.t_count)
                f = (t - self.t_count) % 1
                sc = 1.4 - 0.4 * U.eob(min(1, f / 0.2))
                o.save(); o.translate(960, 220); o.scale(sc, sc)
                o.arc(0, 0, 80, 0, 2 * math.pi); o.set_source_rgba(0.05, 0.05, 0.08, 0.9); o.fill()
                T(o, str(max(1, m)), 0, 38, 110, WHITE, lw=8)
                o.restore()
        else:
            T(o, f"{self.answer}!", 540, 260, 100, GRN, k(t, self.t_reveal + 0.3, self.t_reveal + 0.6), lw=12)
            if t > self.dur - 2.4:
                K.stamp(o, t, self.dur - 2.4, "PLAY AGAIN >", 540, 1460, RED, 54, -0.04)
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
                        T(o, " ".join(g), 540, 1640, 58, WHITE, lw=12)
                        break
                    tc += dd
        S.rrect(o, 425, 1838, 230, 56, 28); o.set_source_rgb(0.06, 0.06, 0.08); o.fill_preserve()
        o.set_source_rgb(*YEL); o.set_line_width(4); o.stroke()
        T(o, "SAME BRO", 540, 1877, 30, YEL, stroke=None)
