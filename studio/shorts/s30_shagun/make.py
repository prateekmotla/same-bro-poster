import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
import fest as F  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s30_shagun"
CAPS = [
    "Diwali envelope: ₹501. Not ₹500. Why that extra ₹1, EVERY single time?",
    "Reason 1: in tradition, zero means an END. ₹1 more = a fresh START.",
    "Reason 2: ₹501 can't be split equally. So the blessing stays WHOLE, never divided.",
    "Reason 3: the coin is metal, seen as a form of Goddess Lakshmi.",
    "Reason 4: that ₹1 is a SEED. It's meant to be saved or invested, so it grows.",
    "It also means continuity: the relationship doesn't end here. The giving goes on.",
    "Money rule: don't spend the whole envelope. Keep a part aside and let it grow.",
    "MORAL: Every big amount starts with ₹1 saved.",
    "Send this to the friend who spends all the shagun the same day.",
]
HOOK = [("WHY SHAGUN", WHITE), ("ENDS IN ₹1", RED), ("THE REAL REASON", YEL)]
SRC = "Source: IANS via Tribune (2024); The Quint"
sh = None


def scene(c, t, lt, **kw):
    F.room(c, t, lt, **kw)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_open(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    F.envelope(c, 540, 1060, 420, 240, "₹501", k(t, st + 0.3, st + 0.6))
    K.stamp(c, t, st + 3.4, "WHY +₹1?", 540, 1290, RED, 50)


def o_zero(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "₹500", 540, 520, 160, WHITE, k(t, st + 0.3, st + 0.6), lw=14)
    if t > st + 1.2:
        T(c, "zero = END", 540, 650, 64, RED, k(t, st + 1.2, st + 1.5), lw=8)
    if t > st + 2.8:
        T(c, "₹501", 540, 900, 160, GRN, k(t, st + 2.8, st + 3.1), lw=14)
        T(c, "one = fresh START", 540, 1030, 64, YEL, k(t, st + 3.2, st + 3.5), lw=8)


def o_split(c, t, lt):
    st = sh.s(3)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("₹500 / 2 = ₹250", WHITE, 56, 0.4), ("₹501 / 2 = ₹250.50", YEL, 56, 1.5)], y0=990, gap=110)
    K.stamp(c, t, st + 3.0, "BLESSING STAYS WHOLE", 540, 1290, GRN, 40, 0.02)


def o_coin(c, t, lt):
    st = sh.s(4)
    K.panel(c, 870, 500)
    a = k(t, st + 0.3, st + 0.6)
    F.coin(c, 540, 1040, 110, "₹1", a)
    if t > st + 1.6:
        T(c, "METAL (DHATU)", 540, 1240, 54, WHITE, k(t, st + 1.6, st + 1.9), stroke=None)
        T(c, "= a form of Lakshmi", 540, 1310, 46, YEL, k(t, st + 2.4, st + 2.7), stroke=None)


def o_seed(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "₹1 = A SEED", 540, 420, 100, YEL, k(t, st + 0.3, st + 0.6), lw=12)
    F.coin(c, 540, 1000, 80, "₹1", k(t, st + 0.3, st + 0.6))
    g = U.eob(U.clamp((t - st - 1.2) / 2.5))
    if g > 0:
        top = 920 - 380 * g
        c.move_to(540, 920); c.line_to(540, top)
        c.set_source_rgb(*GRN); c.set_line_width(14); c.stroke()
        for j, f in enumerate((0.35, 0.6, 0.85)):
            if g > f:
                yy = 920 - 380 * f
                sgn = -1 if j % 2 == 0 else 1
                c.save(); c.translate(540, yy); c.scale(sgn, 1)
                c.move_to(0, 0); c.curve_to(40, -60, 110, -50, 130, -20); c.curve_to(90, 10, 40, 10, 0, 0)
                c.set_source_rgb(*GRN); c.fill(); c.restore()
    if t > st + 4.0:
        T(c, "save it, so it grows", 540, 1170, 58, WHITE, k(t, st + 4.0, st + 4.3), lw=8)


def o_cont(c, t, lt):
    st = sh.s(6)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("₹500 = deal closed", GREY, 54, 0.4), ("₹501 = it CONTINUES", GRN, 58, 1.8)], y0=1010, gap=130)
    if t > st + 3.2:
        T(c, "the giving goes on", 540, 1300, 46, YEL, k(t, st + 3.2, st + 3.5), stroke=None)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "SHAGUN RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Don't spend it all", WHITE, 46, 0.8, "left", 170),
                      ("2. Keep a part aside", GRN, 46, 2.0, "left", 170),
                      ("3. Let it GROW", WHITE, 46, 3.2, "left", 170)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "EVERY BIG AMOUNT", "STARTS WITH ₹1 SAVED")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO SPENDS ALL THE SHAGUN", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), rw(mouth='o', eyes=1.25, arms=((60, 120), (14, -10))), (1.9, 1000, 480), (2.1, 1000, 450), o_open, 'warm'),
        (s(2), s(3), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_zero, 'studio'),
        (s(3), s(4), rw(mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_split, 'warm'),
        (s(4), s(5), rw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 470), o_coin, 'warm'),
        (s(5), s(6), sw(), (1.78, 960, 540), (1.85, 960, 520), o_seed, 'studio'),
        (s(6), s(7), rw(mouth='bigsmile'), (1.9, 1000, 500), (2.0, 1000, 470), o_cont, 'warm'),
        (s(7), s(8), rw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
