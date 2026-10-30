import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s26_average"
CAPS = [
    "Sid's stock falls from ₹100 to ₹60. He buys MORE. 'Average down, bro!'",
    "₹60 to ₹30, buys more. ₹30 to ₹10, more. Now HALF his money is in ONE stock.",
    "Hidden math: a stock down 90% needs a 900% rise just to get back to start.",
    "Real case, Yes Bank: ₹382 in Aug 2018. On 6 Mar 2020: ₹5.55.",
    "About 98% down. Every 'average' on the way made the loss BIGGER.",
    "A falling price is not a discount. Sometimes the BUSINESS itself is breaking.",
    "Rule: average only if the business is still GOOD. Cap how much goes into one stock.",
    "MORAL: Average a good business, not a falling price.",
    "Send this to the friend who says 'average kar lete hain' every time.",
]
HOOK = [("AVERAGING DOWN", WHITE), ("A FALLING STOCK?", RED), ("READ THIS FIRST", YEL)]
SRC = "Source: Business Today (6 Mar 2020); Kuvera"
sh = None


def scene(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)




def o_avg(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "SID'S STOCK", 540, 960, 48, GREY, stroke=None)
    K.rows(c, t, st, [("₹100  >  ₹60", RED, 84, 0.5)], y0=1110)
    K.stamp(c, t, st + 2.6, "BUY MORE!", 540, 1280, GRN, 54)


def o_more(c, t, lt):
    st = sh.s(2)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("₹60 > ₹30:  BUY", WHITE, 56, 0.3), ("₹30 > ₹10:  BUY", WHITE, 56, 2.0),
                      ("HALF HIS MONEY", RED, 62, 3.8), ("IN ONE STOCK", RED, 62, 4.2)], y0=970, gap=105)


def o_math(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "THE HIDDEN MATH", 540, 380, 70, WHITE, lw=8)
    rows = [("DOWN 50%", "needs +100%", 0.6), ("DOWN 75%", "needs +300%", 1.4), ("DOWN 90%", "needs +900%", 2.4)]
    for i, (a_, b_, dt) in enumerate(rows):
        al = k(t, st + dt, st + dt + 0.25)
        if al > 0:
            big = i == 2
            T(c, a_, 330, 560 + i * 150, 62 if big else 52, WHITE, al, lw=8)
            T(c, b_, 760, 560 + i * 150, 62 if big else 52, RED if big else YEL, al, lw=8)
    if t > st + 3.8:
        T(c, "just to get back to start", 540, 1060, 50, GREY, k(t, st + 3.8, st + 4.1), lw=6)


PTS = [0.95, 0.9, 0.82, 0.7, 0.6, 0.5, 0.42, 0.3, 0.22, 0.12, 0.03]


def o_yes(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "YES BANK SHARE", 540, 380, 74, WHITE, lw=8)
    T(c, "(simplified chart)", 540, 440, 32, GREY, lw=5)
    x, y, w, h = 160, 540, 760, 600
    TR.line(c, t, st + 1.2, x, y, w, h, PTS, RED, dur=3.0, lw=10)
    TR.marker(c, t, st + 1.2, x, y + h * (1 - PTS[0]), "", YEL)
    if t > st + 1.2:
        T(c, "₹382", x + 40, y + 20, 56, YEL, k(t, st + 1.2, st + 1.5), lw=8, anchor="left")
        T(c, "Aug 2018", x + 40, y + 76, 36, GREY, k(t, st + 1.2, st + 1.5), lw=6, anchor="left")
    if t > st + 4.2:
        T(c, "₹5.55", x + w - 30, y + h - 110, 64, RED, k(t, st + 4.2, st + 4.5), lw=8, anchor="right")
        T(c, "6 Mar 2020", x + w - 30, y + h - 56, 36, GREY, k(t, st + 4.2, st + 4.5), lw=6, anchor="right")


def o_98(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "-98%", 540, 620, 220, RED, k(t, st + 0.3, st + 0.6), lw=16)
    for i in range(4):
        dt = 1.6 + i * 0.5
        T(c, "AVG", 220 + i * 210, 860, 50, YEL, k(t, st + dt, st + dt + 0.2), lw=6)
    if t > st + 3.8:
        T(c, "= BIGGER LOSS", 540, 1020, 84, WHITE, k(t, st + 3.8, st + 4.1), lw=10)


def o_biz(c, t, lt):
    st = sh.s(6)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("Falling price", WHITE, 56, 0.3), ("is NOT a discount", RED, 62, 1.2),
                      ("sometimes the", GREY, 46, 2.6), ("BUSINESS is breaking", YEL, 58, 3.0)], y0=970, gap=105)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Check: is the business OK?", WHITE, 42, 0.8, "left", 140),
                      ("2. Average only if YES", GRN, 42, 2.2, "left", 140),
                      ("3. Cap money in one stock", WHITE, 42, 3.6, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "AVERAGE A GOOD BUSINESS,", "NOT A FALLING PRICE")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "'AVERAGE KAR LETE HAIN'", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), aw(crash=5, mouth='smirk', **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_avg, 'night'),
        (s(2), s(3), aw(crash=2, mouth='o', eyes=1.3, **ph), (1.9, 1000, 480), (2.0, 1000, 460), o_more, 'red'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_math, 'studio'),
        (s(4), s(5), sw(), (1.78, 960, 540), (1.85, 960, 520), o_yes, 'studio'),
        (s(5), s(6), sw(mouth='frown'), (1.78, 960, 540), (1.85, 960, 520), o_98, 'red'),
        (s(6), s(7), aw(crash=2, mouth='frown', squint=0.4), (1.9, 1000, 500), (2.0, 1000, 470), o_biz, 'night'),
        (s(7), s(8), aw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'night'),
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
