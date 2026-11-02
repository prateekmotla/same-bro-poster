import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s48_mtf"
CAPS = [
    "Guess: the stock falls 25% and you bought with 4x margin. How much of YOUR money is left?",
    "Sid has ₹25,000. The app says: 'Buy ₹1 lakh with MTF!' He does.",
    "Stock falls 25%. ₹1 lakh becomes ₹75,000. The broker wants its ₹75,000 back, with interest.",
    "Sid's ₹25,000? ZERO. A 25% fall = 100% of his money gone.",
    "MTF isn't free money. It's a LOAN, with interest every single day.",
    "Same bro? 'Margin mil raha hai toh badi position'?",
    "Rule: don't buy with borrowed money until you can take the full loss. Start with your own cash, small.",
    "MORAL: Leverage multiplies mistakes, not just profits.",
    "Send this to the friend who loves 'MTF 4x'.",
]
HOOK = [("STOCK -25%", WHITE), ("YOUR MONEY -100%?", RED), ("MTF 4x TRAP", YEL)]
SRC = "Source: MTF leverage up to 4x (PPFAS via Business Today, Feb 2026)"
sh = None


def scene(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "STOCK", 300, 980, 46, GREY, k(t, st + 0.2, st + 0.5), stroke=None)
    T(c, "-25%", 300, 1110, 110, RED, k(t, st + 0.4, st + 0.7), stroke=None)
    T(c, "YOUR MONEY", 780, 980, 46, GREY, k(t, st + 2.4, st + 2.7), stroke=None)
    T(c, "??", 780, 1110, 110, YEL, k(t, st + 2.6, st + 2.9), stroke=None)
    T(c, "with 4x margin", 540, 1260, 46, WHITE, k(t, st + 1.6, st + 1.9), stroke=None)


def o_sid(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    T(c, "SID'S CASH: ₹25,000", 540, 990, 56, WHITE, k(t, st + 0.2, st + 0.5), stroke=None)
    S.rrect(c, 200, 1060, 680, 110, 30); c.set_source_rgba(*GRN, k(t, st + 1.6, st + 1.9)); c.fill()
    T(c, "BUY ₹1 LAKH (MTF)", 540, 1132, 50, (0.05, 0.1, 0.05), k(t, st + 1.6, st + 1.9), stroke=None)
    K.stamp(c, t, st + 3.0, "4x!", 540, 1280, YEL, 70, -0.06)


def o_fall(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "STOCK -25%", 540, 400, 76, RED, k(t, st + 0.1, st + 0.4), lw=9)
    T(c, "₹1,00,000 > ₹75,000", 540, 540, 70, WHITE, k(t, st + 0.9, st + 1.2), lw=9)
    T(c, "BROKER WANTS BACK", 540, 700, 60, GREY, k(t, st + 2.4, st + 2.7), lw=8)
    T(c, "₹75,000 + interest", 540, 810, 70, YEL, k(t, st + 2.9, st + 3.2), lw=9)


def o_zero(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "SID'S ₹25,000", 540, 420, 76, WHITE, k(t, st + 0.1, st + 0.4), lw=9)
    T(c, "₹0", 540, 650, 220, RED, k(t, st + 0.7, st + 1.0), lw=18)
    T(c, "25% fall = 100% gone", 540, 860, 64, YEL, k(t, st + 1.8, st + 2.1), lw=8)


def o_loan(c, t, lt):
    st = sh.s(5)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("MTF ≠ FREE MONEY".replace("≠", "IS NOT"), WHITE, 54, 0.2), ("IT'S A LOAN", RED, 76, 1.4), ("interest EVERY day", YEL, 50, 2.6)], y0=990, gap=115)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("'MARGIN MIL RAHA HAI'", WHITE, 54, 0.2), ("BADI POSITION?", YEL, 70, 1.0)], y0=1000, gap=115)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. No borrowed money until", WHITE, 44, 0.5, "left", 130),
                      ("    you can take FULL loss", RED, 44, 0.5, "left", 130),
                      ("2. Own cash first", GRN, 44, 3.4, "left", 130),
                      ("3. Start SMALL", GRN, 44, 4.6, "left", 130)], y0=1060, gap=82)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "LEVERAGE MULTIPLIES", "MISTAKES TOO", RED)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO LOVES 'MTF 4x'", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'tense'
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), aw(crash=2, mouth='o', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'red'),
        (s(2), s(3), aw(mouth='bigsmile', **ph), (2.0, 1000, 470), (2.15, 1000, 450), o_sid, 'night'),
        (s(3), s(4), aw(crash=3, mouth='frown', squint=0.5, **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_fall, 'red'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_zero, 'red'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_loan, 'studio'),
        (s(6), s(7), aw(mouth='smirk', **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'night'),
        (s(7), s(8), aw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'night'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, aw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'night'),
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
