import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
import fest as F  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s32_crackers"
CAPS = [
    "Sid buys Diwali crackers. Same box as last year... but the price is way HIGHER. Why?",
    "Fact: about 90% of India's crackers come from ONE town: Sivakasi, Tamil Nadu.",
    "1,070 licensed units there. Turnover: around ₹7,000 crore a year.",
    "This Diwali, prices may jump 30% to 50%, industry sources told Business Standard.",
    "Why? Chemical costs spiked. Sulphur went from ₹75 to ₹140 a kg, then eased to ₹100.",
    "Costly freight + some units shut. Less supply, same demand. Prices UP.",
    "Rule: fix a cracker budget FIRST, buy only from licensed shops, follow your city's rules.",
    "MORAL: Celebrate big, but don't burn your budget.",
    "Send this to the friend who burns ₹5,000 of crackers in one night.",
]
HOOK = [("90% OF CRACKERS", WHITE), ("FROM ONE TOWN?", RED), ("+ WHY PRICES JUMP", YEL)]
SRC = "Source: Business Standard (16 Oct 2026)"
sh = None


def stall(c, t, lt, **kw):
    V.street(c, t, 0.0, True)
    F.lights(c, t, 60)
    # cracker stall at right
    V.box(c, 1150, 430, 560, 40, (0.85, 0.2, 0.2), 6)
    for i in range(7):
        V.box(c, 1150 + i * 80, 430, 40, 40, (1, 0.85, 0.3))
    V.box(c, 1170, 470, 520, 330, (0.25, 0.15, 0.1), 6)
    rnd = [(0.9, 0.2, 0.2), (0.2, 0.5, 0.9), (1, 0.8, 0.2), (0.3, 0.8, 0.4)]
    for r in range(3):
        for j in range(5):
            V.box(c, 1190 + j * 100, 490 + r * 100, 86, 80, rnd[(r + j) % 4], 8)
    T(c, "CRACKERS", 1430, 462, 30, WHITE, stroke=None)
    for i in range(3):
        F.diya(c, 760 + i * 110, 880, t, 0.9)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def box_(c, x, y, s, price, a=1.0, col=(0.9, 0.2, 0.2)):
    c.save(); c.translate(x, y); c.scale(s, s)
    S.rrect(c, -110, -80, 220, 160, 14); c.set_source_rgba(*col, a); c.fill()
    S.rrect(c, -110, -80, 220, 40, 14); c.set_source_rgba(1, 0.85, 0.3, a); c.fill()
    T(c, price, 0, 50, 54, WHITE, a, stroke=None)
    c.restore()


def o_box(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    box_(c, 300, 1080, 1.1, "₹1,000", k(t, st + 0.4, st + 0.7), (0.4, 0.4, 0.45))
    T(c, "LAST YEAR", 300, 1260, 40, GREY, k(t, st + 0.4, st + 0.7), stroke=None)
    box_(c, 780, 1080, 1.1, "₹1,400", k(t, st + 1.8, st + 2.1))
    T(c, "THIS YEAR", 780, 1260, 40, RED, k(t, st + 1.8, st + 2.1), stroke=None)
    if t > st + 3.4:
        T(c, "(example)", 540, 1330, 32, GREY, k(t, st + 3.4, st + 3.7), stroke=None)


def o_town(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "~90%", 540, 560, 200, YEL, k(t, st + 0.6, st + 0.9), lw=16)
    T(c, "of India's crackers", 540, 680, 56, WHITE, k(t, st + 1.0, st + 1.3), lw=8)
    T(c, "come from ONE town", 540, 760, 56, WHITE, k(t, st + 1.0, st + 1.3), lw=8)
    if t > st + 2.6:
        T(c, "SIVAKASI", 540, 940, 120, RED, k(t, st + 2.6, st + 2.9), lw=14)
        T(c, "Tamil Nadu", 540, 1030, 52, GREY, k(t, st + 2.9, st + 3.2), lw=6)


def o_size(c, t, lt):
    st = sh.s(3)
    K.panel(c, 870, 500)
    T(c, "SIVAKASI", 540, 950, 52, YEL, stroke=None)
    K.rows(c, t, st, [("1,070 licensed units", WHITE, 56, 0.5), ("~₹7,000 Cr a year", GRN, 64, 1.8)], y0=1080, gap=130)


def o_jump(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "PRICES THIS DIWALI", 540, 420, 70, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    T(c, "+30% to +50%", 540, 660, 130, RED, k(t, st + 1.2, st + 1.5), lw=14)
    T(c, "industry sources, Oct 2026", 540, 780, 42, GREY, k(t, st + 1.6, st + 1.9), lw=5)


def o_sulphur(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "SULPHUR (per kg)", 540, 400, 70, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    K.hbar(c, t, st + 1.2, 140, 600, 800, 80, 75 / 150, GREY, "Before", "₹75")
    K.hbar(c, t, st + 2.2, 140, 810, 800, 80, 140 / 150, RED, "Peak", "₹140")
    K.hbar(c, t, st + 3.2, 140, 1020, 800, 80, 100 / 150, YEL, "Now (eased)", "₹100")


def o_supply(c, t, lt):
    st = sh.s(6)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("+ costly freight", WHITE, 52, 0.4), ("+ some units shut", WHITE, 52, 1.4),
                      ("LESS SUPPLY, SAME DEMAND", YEL, 48, 2.6)], y0=980, gap=105)
    K.stamp(c, t, st + 4.0, "PRICES UP", 540, 1320, RED, 46)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "DIWALI RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Fix a budget FIRST", WHITE, 44, 0.8, "left", 160),
                      ("2. Licensed shops only", GRN, 44, 2.2, "left", 160),
                      ("3. Follow your city's rules", WHITE, 44, 3.6, "left", 160)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "CELEBRATE BIG,", "DON'T BURN YOUR BUDGET")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO BURNS ₹5,000 IN ONE NIGHT", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: stall(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), rw(mouth='o', eyes=1.3), (1.9, 1000, 480), (2.1, 1000, 450), o_box, 'night'),
        (s(2), s(3), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_town, 'studio'),
        (s(3), s(4), rw(mouth='smile'), (1.9, 1000, 500), (2.0, 1000, 470), o_size, 'night'),
        (s(4), s(5), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_jump, 'red'),
        (s(5), s(6), sw(), (1.78, 960, 540), (1.85, 960, 520), o_sulphur, 'studio'),
        (s(6), s(7), rw(mouth='frown', squint=0.3), (1.9, 1000, 500), (2.0, 1000, 470), o_supply, 'night'),
        (s(7), s(8), rw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'night'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw(mouth='bigsmile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'night'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1))
    else:
        sh.render(f"{D}/short.mp4")
