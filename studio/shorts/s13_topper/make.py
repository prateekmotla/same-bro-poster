import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import body as B  # noqa: E402
import env as V  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s13_topper"
CAPS = [
    "Sid's in the metro. Every coaching poster, the SAME topper. AIR 1. \"Our student.\"",
    "Wait. How is ONE guy a student of FIVE coachings?",
    "Here's the game. The topper maybe took just ONE mock interview, or one test series. That's it. Now he's \"their\" topper.",
    "One big UPSC institute claimed 100+ toppers. The consumer authority checked. Only 3 took its FULL course.",
    "The rest? Test series, mock interviews. Fine: ₹11 LAKH.",
    "So far, 28 coaching institutes have been fined over ₹1 CRORE in total.",
    "Before admission, ask ONE question: which course did this topper actually take? Full classroom, or just one test?",
    "And forget the photos. Ask for YOUR batch's result.",
    "Send this to the friend who's about to join a coaching because of a poster.",
]
HOOK = [("SAME TOPPER", YEL), ("IN EVERY", WHITE), ("COACHING AD?", RED)]
SRC = "Source: CCPA orders on coaching ads (2025)"
sh = None
GREY = (0.55, 0.57, 0.65)


def metro(c, t, lt, **kw):
    V.metro(c, t)
    d = dict(pose='sit', phone=None, arms=((14, -10), (14, -10)), mouth='flat')
    d.update(kw)
    B.figure(c, 960, 330, 0.5, t, **d)


def face(c, x, y, r):
    c.arc(x, y, r, 0, 2 * math.pi); c.set_source_rgb(0.85, 0.65, 0.5); c.fill()
    c.arc(x, y - r * 0.15, r * 1.02, math.pi * 1.05, math.pi * 1.95); c.set_source_rgb(0.12, 0.09, 0.08); c.fill()
    for dx in (-0.35, 0.35):
        c.arc(x + dx * r, y + 0.05 * r, r * 0.09, 0, 2 * math.pi); c.set_source_rgb(0.1, 0.1, 0.1); c.fill()
    c.arc(x, y + 0.35 * r, r * 0.3, 0.2, math.pi - 0.2); c.set_line_width(r * 0.07); c.stroke()
    c.rectangle(x - r * 1.1, y + r * 1.0, r * 2.2, r * 0.9); c.set_source_rgb(0.2, 0.3, 0.6); c.fill()


def mark(c, x, y, ok, a):
    c.set_line_width(12); c.set_line_cap(1)
    if ok:
        c.move_to(x - 25, y); c.line_to(x - 5, y + 22); c.line_to(x + 30, y - 25); c.set_source_rgba(*GRN, a)
    else:
        c.move_to(x - 22, y - 22); c.line_to(x + 22, y + 22); c.move_to(x + 22, y - 22); c.line_to(x - 22, y + 22)
        c.set_source_rgba(*RED, a)
    c.stroke()


NAMES = ["COACHING A", "COACHING B", "COACHING C", "COACHING D"]
COLS = [(0.85, 0.2, 0.25), (0.15, 0.35, 0.8), (0.95, 0.55, 0.1), (0.2, 0.6, 0.35)]


def o_posters(c, t, lt):
    U.dim(c, 0.75)
    t0 = 0.4
    for i in range(4):
        x = 110 + (i % 2) * 450; y = 330 + (i // 2) * 560
        a = k(t, t0 + i * 0.35, t0 + i * 0.35 + 0.2)
        S.rrect(c, x, y, 410, 520, 24); c.set_source_rgba(*COLS[i], a); c.fill()
        T(c, NAMES[i], x + 205, y + 70, 40, WHITE, a, stroke=None)
        c.save(); c.translate(0, 0)
        if a > 0:
            face(c, x + 205, y + 210, 85)
        c.restore()
        T(c, "AIR 1", x + 205, y + 420, 80, YEL, a, lw=10)
        T(c, "\"OUR STUDENT\"", x + 205, y + 485, 36, WHITE, a, stroke=None)
    if t > sh.s(2):
        a = k(t, sh.s(2) + 0.8, sh.s(2) + 1.0)
        c.save(); c.translate(540, 1460 - 600); c.rotate(-0.15)
        S.rrect(c, -330, -80, 660, 160, 20); c.set_source_rgba(0.05, 0.05, 0.08, 0.92 * a); c.fill()
        T(c, "SAME GUY?!", 0, 35, 100, RED, a, lw=12)
        c.restore()


def o_took(c, t, lt):
    U.dim(c, 0.8)
    S.rrect(c, 110, 330, 860, 900, 30); c.set_source_rgb(0.97, 0.97, 0.95); c.fill()
    T(c, "WHAT HE ACTUALLY TOOK", 540, 430, 50, (0.1, 0.1, 0.12), stroke=None)
    rows = [("Full classroom course", False, 0.5), ("1 mock interview", True, 2.0), ("1 test series", True, 3.4)]
    for i, (txt, ok, dt) in enumerate(rows):
        a = k(t, sh.s(3) + dt, sh.s(3) + dt + 0.25)
        y = 560 + i * 150
        T(c, txt, 170, y, 46, (0.1, 0.1, 0.12), a, stroke=None, anchor="left")
        mark(c, 900, y - 18, ok, a)
    a = k(t, sh.s(3) + 5.5, sh.s(3) + 5.8)
    T(c, "= \"OUR TOPPER\"", 540, 1080, 80, RED, a, lw=10)


def o_count(c, t, lt):
    U.dim(c, 0.85)
    T(c, "100+", 540, 520, 230, YEL, k(t, sh.s(4) + 0.3, sh.s(4) + 0.6), lw=20)
    T(c, "TOPPERS CLAIMED", 540, 630, 64, WHITE, k(t, sh.s(4) + 0.6, sh.s(4) + 0.9))
    show = t > sh.s(4) + 4.5
    for i in range(50):
        x = 150 + (i % 10) * 87; y = 760 + (i // 10) * 100
        col = YEL if (show and i < 3) else GREY
        U.ppl(c, x, y, 70, col, k(t, sh.s(4) + 1.0 + i * 0.02, sh.s(4) + 1.2 + i * 0.02))
    if show:
        T(c, "FULL COURSE: ONLY 3", 540, 1330, 70, YEL, k(t, sh.s(4) + 4.5, sh.s(4) + 4.8), lw=10)


def o_fine(c, t, lt):
    o_count_bg = U.dim(c, 0.85)
    T(c, "THE REST?", 540, 520, 90, WHITE, k(t, sh.s(5), sh.s(5) + 0.2))
    T(c, "test series · mock interview", 540, 640, 50, (0.8, 0.82, 0.9), k(t, sh.s(5) + 0.8, sh.s(5) + 1.1), stroke=None)
    a = k(t, sh.s(5) + 2.4, sh.s(5) + 2.6)
    sc = 1 + 0.6 * (1 - U.eob(a))
    c.save(); c.translate(540, 900); c.rotate(-0.12); c.scale(sc, sc)
    c.set_line_width(14); S.rrect(c, -360, -130, 720, 260, 30); c.set_source_rgba(*RED, a); c.stroke()
    T(c, "FINE", 0, -30, 70, RED, a, stroke=None)
    T(c, "₹11 LAKH", 0, 80, 110, RED, a, stroke=None)
    c.restore()


def o_total(c, t, lt):
    U.dim(c, 0.85)
    n = int(28 * k(t, sh.s(6) + 0.5, sh.s(6) + 2.0))
    T(c, f"{n}", 540, 600, 260, YEL, lw=20)
    T(c, "COACHING INSTITUTES", 540, 720, 64, WHITE)
    T(c, "FINED", 540, 810, 64, WHITE)
    T(c, "₹1 CRORE+", 540, 1010, 140, RED, k(t, sh.s(6) + 3.0, sh.s(6) + 3.3), lw=14)
    T(c, "in total", 540, 1100, 48, (0.8, 0.82, 0.9), k(t, sh.s(6) + 3.3, sh.s(6) + 3.6), stroke=None)


def o_ask(c, t, lt):
    S.rrect(c, 90, 880, 900, 470, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
    T(c, "ASK BEFORE ADMISSION", 540, 970, 58, YEL, stroke=None)
    T(c, "\"Which course did", 540, 1080, 54, WHITE, k(t, sh.s(7) + 2.0, sh.s(7) + 2.3), stroke=None)
    T(c, "this topper take?\"", 540, 1160, 54, WHITE, k(t, sh.s(7) + 2.3, sh.s(7) + 2.6), stroke=None)
    T(c, "Full course  vs  1 test", 540, 1270, 46, GRN, k(t, sh.s(7) + 5.0, sh.s(7) + 5.3), stroke=None)


def o_batch(c, t, lt):
    S.rrect(c, 90, 880, 900, 470, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
    T(c, "TOPPER PHOTOS", 540, 990, 60, GREY, stroke=None)
    c.move_to(260, 975); c.line_to(820, 975); c.set_source_rgb(*RED); c.set_line_width(8); c.stroke()
    T(c, "YOUR BATCH'S", 540, 1130, 76, GRN, k(t, sh.s(8) + 1.4, sh.s(8) + 1.7), stroke=None)
    T(c, "RESULT", 540, 1230, 76, GRN, k(t, sh.s(8) + 1.4, sh.s(8) + 1.7), stroke=None)


def o_end(c, t, lt):
    S.rrect(c, 140, 900, 800, 230, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    T(c, "SEND TO THE FRIEND", 540, 1000, 60, WHITE, stroke=None)
    T(c, "JOINING COACHING", 540, 1085, 66, YEL, stroke=None)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    m = lambda **kw: (lambda c, t, lt: metro(c, t, lt, **kw))
    sh.shots = [
        (0, s(3), m(eyes=1.1), (1.9, 960, 480), (2.1, 960, 450), o_posters, 'studio'),
        (s(3), s(4), m(squint=0.4), (1.78, 960, 540), (1.85, 960, 520), o_took, 'night'),
        (s(4), s(5), m(), (1.78, 960, 540), (1.85, 960, 520), o_count, 'night'),
        (s(5), s(6), m(mouth='o'), (1.78, 960, 540), (1.85, 960, 540), o_fine, 'red'),
        (s(6), s(7), m(), (1.78, 960, 540), (1.85, 960, 540), o_total, 'red'),
        (s(7), s(8), m(mouth='smirk', squint=0.3), (1.9, 960, 520), (2.0, 960, 500), o_ask, 'morning'),
        (s(8), s(9), m(mouth='smile'), (1.9, 960, 520), (2.0, 960, 500), o_batch, 'morning'),
        (s(9), sh.dur + 1, m(mouth='smirk', arms=((14, -10), (100, 40))), (1.9, 960, 520), (2.1, 960, 480), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1, 3.5, (L[1][0] + 1.5)] + [a + (b - a) * 0.8 for a, b in L[2:]], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
