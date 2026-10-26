"""Same Bro LONG 02 — Why You Can't Stop Scrolling at 2 AM. Uses long1 engine (render_long) with new shots."""
import json
import math
import random
import sys
import wave

import cairo
import numpy as np
from PIL import Image

sys.path.insert(0, "/home/claude/sid/long1")
import render_long as R  # noqa: E402
import body as B  # noqa: E402
import env as V  # noqa: E402
import props as P  # noqa: E402
import sid2 as S  # noqa: E402
import chars as CH  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/long2"
FPS = R.FPS
L = [None] + json.load(open(f"{D}/lines.json"))
R.L = L
with wave.open(f"{D}/vo16.wav") as wv:
    _a = np.frombuffer(wv.readframes(wv.getnframes()), np.int16).astype(np.float32) / 32768
_hop = 16000 // FPS
_e = np.array([np.sqrt((_a[i:i + _hop] ** 2).mean() + 1e-12) for i in range(0, len(_a), _hop)])
R._env = np.convolve(np.clip((20 * np.log10(_e + 1e-9) + 45) / 30, 0, 1), [0.25, 0.5, 0.25], mode="same")
DUR = 168.0


def s(n):
    return L[n][0]


def e(n):
    return L[n][1]


# ---------------- widgets ----------------
def clock(c, x, y, txt, size=90, col=(0.4, 1.0, 0.6)):
    S.rrect(c, x - size * 1.7, y - size * 0.95, size * 3.4, size * 1.3, 18)
    c.set_source_rgb(0.03, 0.03, 0.04); c.fill()
    T(c, txt, x, y, size, col, stroke=None)


def reel_tile(c, w, h, seed, label):
    rnd = random.Random(seed)
    g = cairo.LinearGradient(0, 0, w, h)
    a = (rnd.random(), rnd.random() * 0.6, rnd.random())
    b = (rnd.random() * 0.4, rnd.random(), rnd.random() * 0.8)
    g.add_color_stop_rgb(0, *a); g.add_color_stop_rgb(1, *b)
    c.set_source(g); c.rectangle(0, 0, w, h); c.fill()
    c.arc(w / 2, h * 0.42, w * 0.18, 0, 2 * math.pi); c.set_source_rgba(1, 1, 1, 0.25); c.fill()
    T(c, label, w / 2, h * 0.78, w * 0.08, WHITE, lw=6)
    for i, ic in enumerate(("♥", "◆", "➤")):
        c.arc(w * 0.88, h * (0.5 + i * 0.1), w * 0.035, 0, 2 * math.pi); c.set_source_rgba(1, 1, 1, 0.8); c.fill()


LABELS = ["meme page", "gym transformation", "podcast clip", "car edit", "comedy skit", "motivation", "food vlog",
          "dance trend", "prank", "travel", "cricket", "movie scene"]


def scr_feed(speed=1.0, t0=0.0, gray=0.0):
    def f(c, w, h, t):
        pos = (t - t0) * speed
        n = int(pos)
        fr = pos - n
        ease = fr ** 3 if fr < 1 else 1
        off = -ease * h if (pos % 1) > 0.75 else 0
        sh = (pos % 1 - 0.75) / 0.25 if (pos % 1) > 0.75 else 0
        off = -U.clamp(sh) ** 2 * h
        for j in (0, 1):
            c.save(); c.translate(0, off + j * h)
            reel_tile(c, w, h, n + j + 7, LABELS[(n + j) % len(LABELS)])
            c.restore()
        if gray > 0:
            c.set_operator(cairo.OPERATOR_HSL_SATURATION)
            c.set_source_rgba(0.5, 0.5, 0.5, gray); c.rectangle(0, 0, w, h); c.fill()
            c.set_operator(cairo.OPERATOR_OVER)
    return f


def sid_bed(c, t, mode='night', glow=1.0, **e):
    V.room(c, t, mode)
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=glow, mouth='flat', look=(0.5, 0.3), eyes=0.75,
             bags=0.7)
    d.update(e)
    B.figure(c, 1000, 330, 0.5, t, **d)


def sid_sleeping(c, t, x=660, y=545, s=0.36):
    """Head on the pillow, eyes closed, blanket up to the chin."""
    c.save(); c.translate(x, y); c.rotate(math.radians(-78)); c.translate(-x, -y)
    CH.sid_head(c, x, y, s, t, eyes=0.0, mouth='smile', tilt=0)
    c.restore()
    c.move_to(700, 560); c.curve_to(900, 520, 1200, 590, 1410, 560); c.line_to(1410, 660); c.line_to(700, 660)
    c.close_path(); c.set_source_rgb(0.15, 0.22, 0.36); c.fill()
    for i in range(3):
        a = (t * 0.6 + i * 0.33) % 1
        T(c, "z", 720 + a * 60 + i * 10, 470 - a * 120, 40 + i * 10, WHITE, 1 - a, stroke=None)


# ---------------- shots ----------------
def sh_hook(c, t, lt):
    sid_bed(c, t)
    clock(c, 1450, 170, "2:00 AM")
    return 'phone'


def sh_feed(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.65)
    U.phone_frame(c, 700, 40, 520, 1000, scr_feed(1.6, s(2)), t, tilt=-2 + 2 * lt)
    for i, w_ in enumerate(("1 reel", "+1", "+1", "+1", "+1")):
        T(c, w_, 360, 220 + i * 140, 60, YEL if i == 0 else WHITE, k(t, s(2) + i * 1.3, s(2) + i * 1.3 + 0.2))
    return 'phone'


def sh_clock310(c, t, lt):
    sid_bed(c, t, eyes=1.2, mouth='o', **{'raise': 0.8})
    clock(c, 1450, 170, "3:10 AM", col=RED)
    if t > s(4):
        S.rrect(c, 1250, 260, 600, 120, 20); c.set_source_rgba(0.95, 0.95, 0.97, 0.95); c.fill()
        T(c, "Meeting · 9:00 AM", 1550, 335, 44, (0.6, 0.1, 0.15), stroke=None)
    return 'phone'


def sh_design(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.7)
    T(c, "Not your fault.", 960, 420, 110, WHITE, k(t, s(5) + 1.5, s(5) + 1.8))
    T(c, "It's the DESIGN.", 960, 580, 120, YEL, k(t, s(5) + 3.9, s(5) + 4.2))
    return 'night'


def sh_ey(c, t, lt):
    V.studio(c, t); U.dim(c, 0.85)
    T(c, "EY REPORT · 2024", 960, 140, 44, (0.8, 0.82, 0.9), stroke=None)
    T(c, "1.1 TRILLION", 960, 380, 150, YEL, k(t, s(7) + 4.2, s(7) + 4.5))
    T(c, "hours on phones in India", 960, 470, 50, WHITE, k(t, s(7) + 4.6, s(7) + 4.9), stroke=None)
    if t > s(7) + 6.8:
        T(c, "≈ 5 HOURS / DAY", 960, 620, 100, WHITE, k(t, s(7) + 6.8, s(7) + 7.1))
    if t > s(8):
        fr = 0.7 * k(t, s(8) + 0.5, s(8) + 2.0)
        c.save(); c.translate(760, 840)
        c.arc(0, 0, 110, 0, 2 * math.pi); c.set_source_rgba(1, 1, 1, 0.12); c.fill()
        c.move_to(0, 0); c.arc(0, 0, 110, -math.pi / 2, -math.pi / 2 + 2 * math.pi * fr); c.close_path()
        c.set_source_rgb(*RED); c.fill()
        c.restore()
        T(c, "~70%", 1060, 840, 90, RED, k(t, s(8) + 1.8, s(8) + 2.1))
        T(c, "social · games · video", 1100, 900, 40, WHITE, k(t, s(8) + 2.0, s(8) + 2.3), stroke=None)
    return 'night'


def sh_survey(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.75)
    T(c, "SLEEP SURVEY · 2025", 960, 140, 44, (0.8, 0.82, 0.9), stroke=None)
    U.bar(c, 260, 330, 1400, 100, 0.84 * k(t, s(9) + 1.5, s(9) + 2.6), YEL, "use the phone right before bed", "84%")
    U.bar(c, 260, 590, 1400, 100, 0.58 * k(t, s(9) + 5.5, s(9) + 6.5), RED, "sleep after 11 PM", "58%")
    return 'night'


def sh_question(c, t, lt):
    sid_bed(c, t, eyes=0.6, mouth='frown', sad=0.5)
    T(c, "Why is it SO hard to stop?", 960, 160, 80, WHITE, k(t, s(10) + 1.0, s(10) + 1.3))
    return 'phone'


REASONS = [("INFINITE SCROLL", "no stopping cue"), ("SLOT MACHINE", "maybe the next one"), ("15 SECONDS", "just one more"),
           ("ALGORITHM", "learns your weakness"), ("REVENGE", "bedtime procrastination")]


def sh_five(c, t, lt):
    V.studio(c, t); U.dim(c, 0.8)
    T(c, "5 REASONS", 960, 200, 100, YEL, k(t, s(11), s(11) + 0.3))
    for i, (a, b) in enumerate(REASONS):
        U.icon_card(c, 110 + i * 350, 380, 320, 420, i + 1, a, b, k(t, s(11) + 0.5 + i * 0.25, s(11) + 0.9 + i * 0.25),
                    col=[YEL, RED, GRN, (0.4, 0.6, 1), (0.9, 0.4, 0.9)][i])
    return 'studio'


def sh_oldweb(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.6)

    def scr(c2, w, h, tt):
        U.scr_fill(c2, w, h, (0.96, 0.96, 0.98))
        sc = -k(tt, s(12) + 1.5, s(12) + 4.5) * 500
        for i in range(8):
            S.rrect(c2, 60, 60 + i * 110 + sc, w - 120, 80, 10); c2.set_source_rgb(0.85, 0.87, 0.92); c2.fill()
        S.rrect(c2, 60, 940 + sc, w - 120, 120, 14); c2.set_source_rgb(0.2, 0.2, 0.25); c2.fill()
        T(c2, "END OF PAGE", w / 2, 1015 + sc, 44, WHITE, stroke=None)
    U.laptop(c, 460, 140, 1000, 600, scr, t)
    T(c, "OLD INTERNET: pages ENDED", 960, 90, 60, WHITE)
    return 'night'


def sh_noend(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.65)
    U.phone_frame(c, 690, 40, 540, 1000, scr_feed(2.4, s(13)), t)
    T(c, "NO END.", 360, 500, 110, RED, k(t, s(13), s(13) + 0.3))
    if t > s(13) + 3.1:
        S.rrect(c, 1290, 380, 560, 200, 26); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
        T(c, "Its own designer", 1570, 460, 40, WHITE, stroke=None)
        T(c, "said he regrets it", 1570, 525, 40, YEL, stroke=None)
    return 'phone'


def sh_slot(c, t, lt):
    V.studio(c, t); U.dim(c, 0.6)
    c.save(); c.translate(960, 560)
    S.rrect(c, -520, -330, 1040, 660, 60); c.set_source_rgb(0.75, 0.1, 0.15); c.fill()
    S.rrect(c, -460, -230, 920, 380, 30); c.set_source_rgb(0.98, 0.96, 0.9); c.fill()
    syms = ["meh", "LOL", "boring", "WOW", "meh", "ad", "FIRE", "cringe"]
    for i in range(3):
        stop = s(14) + 2.5 + i * 0.6 + (s(15) - s(14))
        spin = t < stop
        idx = int(t * 14 + i * 3) % len(syms) if spin else [1, 3, 6][i]
        x = -300 + i * 300
        S.rrect(c, x - 130, -200, 260, 320, 20); c.set_source_rgb(1, 1, 1); c.fill()
        T(c, syms[idx], x, -20, 60, (0.1, 0.1, 0.12) if spin else RED, stroke=None)
    T(c, "NEXT REEL?", 0, 250, 60, YEL, stroke=None)
    c.restore()
    c.move_to(1500, 380); c.line_to(1580, 260); c.set_line_width(20); c.set_source_rgb(0.7, 0.7, 0.75); c.stroke()
    c.arc(1585, 250, 40, 0, 2 * math.pi); c.set_source_rgb(*RED); c.fill()
    if t > s(15) + 4.7:
        T(c, "Casinos use the same trick.", 960, 990, 54, WHITE, k(t, s(15) + 4.7, s(15) + 5.0))
    return 'warm'


def sh_15sec(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.7)
    U.phone_frame(c, 260, 60, 500, 960, scr_feed(1.0, s(16)), t, tilt=-3)
    T(c, "15 sec", 1300, 330, 140, WHITE, k(t, s(16) + 1.8, s(16) + 2.1))
    T(c, "\"just one more\"", 1300, 470, 64, YEL, k(t, s(16) + 5.3, s(16) + 5.6))
    if t > s(17):
        n = int(100 * k(t, s(17) + 0.3, s(17) + 2.0))
        T(c, f"× {n} times", 1300, 650, 80, WHITE)
        T(c, "= 25 MINUTES", 1300, 820, 110, RED, k(t, s(17) + 2.3, s(17) + 2.6))
    return 'phone'


def sh_algo(c, t, lt):
    V.studio(c, t); U.dim(c, 0.82)
    # eye
    c.save(); c.translate(960, 330)
    c.move_to(-260, 0); c.curve_to(-120, -170, 120, -170, 260, 0); c.curve_to(120, 170, -120, 170, -260, 0)
    c.set_source_rgb(0.95, 0.95, 0.97); c.fill()
    c.arc(math.sin(t * 1.3) * 60, 0, 90, 0, 2 * math.pi); c.set_source_rgb(0.2, 0.45, 0.95); c.fill()
    c.arc(math.sin(t * 1.3) * 60, 0, 40, 0, 2 * math.pi); c.set_source_rgb(0.02, 0.02, 0.03); c.fill()
    c.restore()
    T(c, "THE ALGORITHM", 960, 120, 64, YEL)
    sameness = k(t, s(18) + 3.5, s(18) + 6.0)
    for i in range(8):
        lab = "gym transformation" if (i < int(8 * sameness)) else LABELS[(i * 5) % len(LABELS)]
        c.save(); c.translate(150 + i * 210, 640)
        S.rrect(c, 0, 0, 190, 330, 16); c.clip()
        reel_tile(c, 190, 330, 3 if lab == "gym transformation" else i + 20, lab)
        c.restore()
    if t > s(18) + 6.0:
        T(c, "It learns your weakness", 960, 1010 - 60, 54, RED, k(t, s(18) + 6.0, s(18) + 6.3))
    return 'night'


def sh_revenge(c, t, lt):
    V.studio(c, t); U.dim(c, 0.85)
    T(c, "YOUR DAY", 960, 150, 70, WHITE)
    segs = [("COLLEGE / OFFICE", 9, (0.4, 0.42, 0.5)), ("TRAVEL", 2, (0.5, 0.45, 0.4)), ("FAMILY", 3, (0.45, 0.5, 0.42)),
            ("MINE", 3, YEL)]
    x = 160
    tot = 17
    for i, (lab, hrs, col) in enumerate(segs):
        a = k(t, s(19) + 2.0 + i * 0.7, s(19) + 2.3 + i * 0.7) if i < 3 else k(t, s(20) + 0.8, s(20) + 1.2)
        w_ = 1600 * hrs / tot
        S.rrect(c, x, 400, w_ - 10, 160, 18); c.set_source_rgba(*col, a); c.fill()
        T(c, lab, x + w_ / 2, 500, 36 if i < 3 else 52, WHITE if i < 3 else (0.1, 0.1, 0.1), a, stroke=None)
        x += w_
    if t > s(20) + 3.0:
        T(c, "...stolen from SLEEP", 1500, 680, 54, RED, k(t, s(20) + 3.0, s(20) + 3.3))
    if t > s(20) + 5.0:
        T(c, "REVENGE BEDTIME", 960, 860, 90, YEL, k(t, s(20) + 5.0, s(20) + 5.3))
        T(c, "PROCRASTINATION", 960, 960, 90, YEL, k(t, s(20) + 5.3, s(20) + 5.6))
    return 'night'


def sh_morning_alarm(c, t, lt):
    V.room(c, t, 'day')
    sid_sleeping(c, t)
    shake = math.sin(t * 60) * 6 if (int(t * 2) % 2 == 0) else 0
    U.phone_frame(c, 1180 + shake, 120, 420, 760, lambda c2, w, h, tt: (
        U.scr_fill(c2, w, h, (0.08, 0.08, 0.1)),
        T(c2, "8:47", w / 2, 300, 130, WHITE, stroke=None),
        T(c2, "SNOOZE ×3", w / 2, 450, 50, RED, stroke=None)), t, tilt=4, glow=0.2)
    for i, (w_, t0) in enumerate((("LATE", s(22) + 2.5), ("GYM: SKIP", s(22) + 3.1), ("FOCUS: 0", s(22) + 3.9))):
        T(c, w_, 560, 220 + i * 120, 70, RED, k(t, t0, t0 + 0.2))
    return 'morning'


def sh_office(c, t, lt):
    V.canteen(c, t)
    U.dim(c, 0.2)
    B.figure(c, 960, 330, 0.55, t, pose='sit', mouth='o', eyes=0.4 + 0.3 * math.sin(t * 2), bags=1, look=(0, 0.5))
    if t > s(22) + 5.8:
        S.rrect(c, 1300, 300, 520, 220, 26); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
        T(c, "59%", 1560, 410, 100, RED, stroke=None)
        T(c, "sleepy at work", 1560, 480, 40, WHITE, stroke=None)
    return 'day'


def sh_cycle(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.6)
    c.save(); c.translate(960, 540); c.rotate(t * 0.8)
    c.arc(0, 0, 300, 0, 2 * math.pi); c.set_source_rgba(*YEL, 0.85); c.set_line_width(18); c.stroke()
    c.restore()
    for i, (lab, ang) in enumerate((("PHONE", -90), ("LATE SLEEP", 30), ("TIRED DAY", 150))):
        x = 960 + math.cos(math.radians(ang)) * 300; y = 540 + math.sin(math.radians(ang)) * 300
        S.rrect(c, x - 170, y - 50, 340, 100, 50); c.set_source_rgb(0.05, 0.06, 0.1); c.fill()
        T(c, lab, x, y + 16, 40, WHITE, stroke=None)
    return 'night'


FIXES = [("CHARGER AWAY", "out of reach"), ("GRAYSCALE", "after 11 PM"), ("APP TIMER", "limit = lock"),
         ("BORING BEDSIDE", "book / audio"), ("30 MIN FOR YOU", "in the day")]


def sh_system(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.75)
    T(c, "Not willpower.", 960, 430, 100, WHITE, k(t, s(24) + 1.2, s(24) + 1.5))
    T(c, "SYSTEM.", 960, 600, 150, GRN, k(t, s(24) + 2.2, s(24) + 2.5))
    return 'night'


def sh_fix(c, t, lt, n):
    mode = 'night'
    V.room(c, t, mode)
    if n == 0:
        B.figure(c, 760, 330, 0.5, t, pose='sit', mouth='flat', look=(0.8, 0.2))
        U.phone_frame(c, 1690, 560, 110, 200, scr_feed(0, 0), t, glow=0.5)
        c.move_to(1745, 770); c.curve_to(1745, 850, 1800, 850, 1810, 900); c.set_line_width(8); c.set_source_rgb(0.9, 0.9, 0.9); c.stroke()
    elif n == 1:
        U.dim(c, 0.6)
        U.phone_frame(c, 360, 60, 500, 960, scr_feed(0.6, s(26)), t, tilt=-3)
        U.phone_frame(c, 1060, 60, 500, 960, scr_feed(0.6, s(26), gray=1.0), t, tilt=3)
        T(c, "after 11 PM", 960, 1000 - 40, 48, WHITE, stroke=None)
    elif n == 2:
        U.dim(c, 0.6)

        def scr(c2, w, h, tt):
            U.scr_fill(c2, w, h, (0.08, 0.08, 0.1))
            T(c2, "Time limit reached", w / 2, h * 0.4, 40, WHITE, stroke=None)
            c2.arc(w / 2, h * 0.6, 60, 0, 2 * math.pi); c2.set_source_rgb(*RED); c2.fill()
            S.rrect(c2, w / 2 - 25, h * 0.6 - 10, 50, 50, 8); c2.set_source_rgb(1, 1, 1); c2.fill()
        U.phone_frame(c, 690, 60, 540, 960, scr, t)
    elif n == 3:
        B.figure(c, 1000, 330, 0.5, t, pose='sit', mouth='smile', eyes=0.7, arms=((40, 100), (40, 100)))
        S.rrect(c, 930, 560, 140, 100, 8); c.set_source_rgb(0.85, 0.3, 0.2); c.fill()
        S.rrect(c, 938, 566, 124, 88, 6); c.set_source_rgb(0.97, 0.95, 0.88); c.fill()
    else:
        V.canteen(c, t)
        B.figure(c, 960, 330, 0.55, t, pose='sit', mouth='smile', blush=0.3)
        S.rrect(c, 1300, 250, 520, 160, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
        T(c, "30 MIN = MINE", 1560, 345, 56, YEL, stroke=None)
    a, b = FIXES[n]
    S.rrect(c, 160, 110, 640, 150, 26); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    c.arc(230, 185, 40, 0, 2 * math.pi); c.set_source_rgb(*GRN); c.fill()
    T(c, str(n + 1), 230, 200, 46, (0.05, 0.05, 0.05), stroke=None)
    T(c, a, 290, 180, 46, WHITE, stroke=None, anchor="left")
    T(c, b, 290, 230, 30, (0.75, 0.78, 0.88), stroke=None, anchor="left", bold=False)
    return 'night' if n != 4 else 'day'


def sh_sleep(c, t, lt):
    V.room(c, t, 'night', fan=True)
    sid_sleeping(c, t)
    clock(c, 1450, 170, "12:30 AM", col=GRN)
    U.phone_frame(c, 1700, 560, 110, 200, lambda c2, w, h, tt: U.scr_fill(c2, w, h, (0.02, 0.02, 0.03)), t, glow=0)
    if t > s(30) + 2.6:
        T(c, "Night 1: hard", 400, 300, 60, WHITE, k(t, s(30) + 2.6, s(30) + 2.9))
    if t > s(30) + 4.6:
        T(c, "Night 3: asleep by 12:30", 400, 400, 52, GRN, k(t, s(30) + 4.6, s(30) + 4.9))
    return 'night'


def sh_end(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.75)
    T(c, "Watching this at 2 AM?", 960, 380, 90, WHITE, k(t, s(31) + 1.0, s(31) + 1.3))
    T(c, "PUT THE PHONE DOWN.", 960, 540, 110, YEL, k(t, s(31) + 3.8, s(31) + 4.1))
    T(c, "This video will be here tomorrow.", 960, 680, 56, WHITE, k(t, s(31) + 5.8, s(31) + 6.1), stroke=None)
    S.rrect(c, 820, 80, 280, 70, 35); c.set_source_rgb(0.06, 0.06, 0.08); c.fill_preserve()
    c.set_source_rgb(*YEL); c.set_line_width(4); c.stroke()
    T(c, "SAME BRO", 960, 128, 40, YEL, stroke=None)
    return 'end'


def F(n):
    return lambda c, t, lt: sh_fix(c, t, lt, n)


SHOTS = [
    (0.0, s(2), sh_hook, (1.0, 960, 540, 0), (1.3, 1000, 480, 0), 0),
    (s(2), s(3), sh_feed, (1.0, 960, 540, 0), (1.12, 960, 560, 0), 1),
    (s(3), s(5), sh_clock310, (1.6, 1100, 380, -2), (1.4, 1150, 400, 2), -1),
    (s(5), s(7), sh_design, (1.1, 960, 520, 0), (1.0, 960, 540, 0), 0),
    (s(7), s(9), sh_ey, (1.0, 960, 500, 0), (1.05, 960, 560, 0), 1),
    (s(9), s(10), sh_survey, (1.0, 960, 540, 0), (1.05, 960, 520, 0), -1),
    (s(10), s(11), sh_question, (1.2, 1000, 420, 0), (1.35, 1000, 400, 0), 1),
    (s(11), s(12), sh_five, (1.0, 960, 560, 0), (1.0, 960, 540, 0), -1),
    (s(12), s(13), sh_oldweb, (1.0, 960, 500, 0), (1.12, 960, 480, 0), 1),
    (s(13), s(14), sh_noend, (1.0, 960, 540, 0), (1.08, 1100, 540, 0), -1),
    (s(14), s(16), sh_slot, (1.05, 960, 560, -2), (1.1, 960, 540, 2), 1),
    (s(16), s(18), sh_15sec, (1.0, 960, 540, 0), (1.08, 1150, 540, 0), -1),
    (s(18), s(19), sh_algo, (1.0, 960, 500, 0), (1.06, 960, 600, 0), 1),
    (s(19), s(21), sh_revenge, (1.0, 960, 540, 0), (1.05, 960, 600, 0), -1),
    (s(21), s(22) + 5.0, sh_morning_alarm, (1.0, 960, 540, 0), (1.1, 1000, 500, 0), 0),
    (s(22) + 5.0, s(23), sh_office, (1.05, 960, 540, 0), (1.25, 1000, 460, 0), 1),
    (s(23), s(24), sh_cycle, (1.1, 960, 540, 0), (1.0, 960, 540, 0), -1),
    (s(24), s(25), sh_system, (1.1, 960, 520, 0), (1.0, 960, 540, 0), 0),
    (s(25), s(26), F(0), (1.0, 960, 540, 0), (1.08, 1060, 540, 0), 1),
    (s(26), s(27), F(1), (1.0, 960, 540, 0), (1.05, 960, 540, 0), -1),
    (s(27), s(28), F(2), (1.05, 960, 540, 0), (1.15, 960, 520, 0), 1),
    (s(28), s(29), F(3), (1.05, 960, 520, 0), (1.15, 960, 500, 0), -1),
    (s(29), s(30), F(4), (1.0, 960, 540, 0), (1.06, 1000, 520, 0), 1),
    (s(30), s(31), sh_sleep, (1.0, 960, 540, 0), (1.25, 800, 520, 0), 0),
    (s(31), DUR, sh_end, (1.08, 960, 540, 0), (1.0, 960, 540, 0), -1),
]

CAPS_EN = [
    "2 AM. Sid thought: one reel, then sleep.",
    "One reel. Then another. A meme page. Someone's gym transformation. A random podcast clip.",
    "He checks the time... 3:10 AM.",
    "And there's a 9 AM meeting tomorrow.",
    "If this happens to you, listen. It's less your fault, more the DESIGN.",
    "First, the numbers.",
    "EY: in 2024 Indians spent 1.1 TRILLION hours on phones. That's about 5 HOURS a day.",
    "And nearly 70% of it on social media, games and videos.",
    "In a sleep survey, 84% said they use the phone right before bed. 58% sleep after 11 PM.",
    "So why is it SO hard to put the phone down?",
    "Five reasons. One by one.",
    "#1: INFINITE SCROLL. Websites used to END. Page over, you stopped.",
    "Now there's no end. The stop signal is gone. Its own designer later said he regrets it.",
    "#2: the SLOT MACHINE brain. You don't know if the next reel is good or bad.",
    "That \"maybe the next one's great\" feeling keeps you scrolling. Casinos use the same trick.",
    "#3: reels are SHORT. 15 seconds. Your brain says: 15 seconds is nothing. Just one more.",
    "But 100 × \"just one more\" = 25 MINUTES.",
    "#4: the ALGORITHM knows you better than you. What you watch at night, you get more of. It learns your weakness.",
    "#5, the most real one: all day your time belongs to college, office, family.",
    "At night it finally feels like YOUR time. So you steal it from sleep. It's called REVENGE BEDTIME PROCRASTINATION.",
    "Who pays the bill? The next day.",
    "Alarm, snooze, snooze. LATE. Gym skipped. No focus. In the survey, 59% said they feel sleepy at work.",
    "And at night? Same phone. Same cycle.",
    "So what's the fix? Not willpower. A SYSTEM.",
    "1: Keep the charger AWAY from your bed. The phone's out of reach.",
    "2: After 11 PM, switch the screen to GRAYSCALE. No colour, half the fun.",
    "3: Set an APP TIMER. Limit hit, app locked.",
    "4: Keep something BORING by the bed instead. A book, or audio. No screen.",
    "5: Take 30 minutes for YOURSELF during the day, so the night isn't revenge.",
    "Sid moved his charger across the room. Night 1 was hard. Night 3, he was asleep by 12:30.",
    "And if you're watching this at 2 AM... put the phone down and sleep. This video will be here tomorrow.",
]
R.SHOTS = SHOTS
R.CAPS_EN = CAPS_EN


def disclaimer(c, t):
    if s(7) <= t <= s(10) or s(22) + 5 <= t <= s(23):
        txt = "Sources: EY (2025), Wakefit Great Indian Sleep Scorecard 2025"
    else:
        return
    S.rrect(c, 520, 18, 880, 44, 22); c.set_source_rgba(0, 0, 0, 0.55); c.fill()
    T(c, txt, 960, 48, 22, (0.85, 0.87, 0.95), stroke=None, bold=False)


R.disclaimer = disclaimer
render_frame = R.render_frame

if __name__ == "__main__":
    import subprocess
    if sys.argv[1] != "full":
        for n, tt in enumerate(map(float, sys.argv[1].split(","))):
            Image.fromarray(render_frame(int(tt * FPS))).save(f"p_{n:02d}.png")
    else:
        a, b, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1920x1080",
                              "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                              "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
        for i in range(a, b):
            p.stdin.write(render_frame(i).tobytes())
            if i % 240 == 0:
                print(f"frame {i}/{b}", flush=True)
        p.stdin.close(); p.wait()
