import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
import fest as F  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s42_dhanteras"
GOLD = F.GOLD
CAPS = [
    "Guess: if you buy gold on Dhanteras, does it ALWAYS go up?",
    "Every Dhanteras Sid's family buys gold. 'Shubh hai, and the rate will surely rise!'",
    "Let's check: gold rate on Dhanteras vs the NEXT Dhanteras, 2011 to 2025.",
    "4 times, gold was CHEAPER a year later: 2013, 2014, 2015 and 2021.",
    "Gold moves with global prices, the dollar and the rupee. Not with the festival date.",
    "Same bro? 'It's Dhanteras, rate toh upar hi jayega'?",
    "Rule: buy for tradition, sure. But INVEST with a plan: small amounts, over years, BIS hallmark checked.",
    "MORAL: The date is shubh. The profit isn't guaranteed.",
    "Send this to the friend who says gold only goes up.",
]
HOOK = [("GOLD AFTER", WHITE), ("DHANTERAS?", GOLD), ("ALWAYS UP?", RED)]
SRC = "Source: 24K Dhanteras rates 2010-2025 (Sahi data table)"
sh = None
# Dhanteras 24K Rs/10g (Sahi table); YoY sign used only for the red/green tiles
YRS = [(2011, 1), (2012, 1), (2013, -1), (2014, -1), (2015, -1), (2016, 1), (2017, 0), (2018, 1),
       (2019, 1), (2020, 1), (2021, -1), (2022, 1), (2023, 1), (2024, 1), (2025, 1)]


def scene(c, t, lt, **kw):
    F.room(c, t, lt, **kw)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def bar(c, x, y, w, h, a=1.0):
    c.move_to(x + 30, y); c.line_to(x + w - 30, y); c.line_to(x + w, y + h); c.line_to(x, y + h); c.close_path()
    c.set_source_rgba(*GOLD, a); c.fill()
    T(c, "999", x + w / 2, y + h * 0.68, h * 0.42, (0.5, 0.35, 0.05), a, stroke=None)


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "DHANTERAS GOLD", 540, 960, 50, YEL, k(t, st + 0.2, st + 0.5), stroke=None)
    bar(c, 400, 1000, 280, 100, k(t, st + 0.5, st + 0.8))
    T(c, "ALWAYS UP?", 540, 1230, 80, WHITE, k(t, st + 1.2, st + 1.5), stroke=None)


def o_family(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    for i in range(3):
        bar(c, 250 + i * 200, 1000 - i * 10, 180, 70, k(t, st + 0.3 + i * 0.3, st + 0.5 + i * 0.3))
    K.rows(c, t, st, [("'SHUBH HAI!'", YEL, 66, 1.2), ("'rate toh badhega hi'", WHITE, 46, 2.4)], y0=1180, gap=95)


def o_check(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.9)
    T(c, "DHANTERAS vs NEXT DHANTERAS", 540, 400, 50, GREY, k(t, st + 0.2, st + 0.5), lw=7)
    for i, (y, sg) in enumerate(YRS):
        r, cc = divmod(i, 5)
        a = k(t, st + 0.6 + i * 0.12, st + 0.8 + i * 0.12)
        x, yy = 150 + cc * 160, 470 + r * 150
        S.rrect(c, x, yy, 140, 120, 16); c.set_source_rgba(0.14, 0.15, 0.22, a); c.fill()
        T(c, str(y), x + 70, yy + 72, 38, WHITE, a, stroke=None)


def o_four(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "CHEAPER A YEAR LATER", 540, 400, 56, GREY, k(t, st + 0.1, st + 0.4), lw=7)
    for i, (y, sg) in enumerate(YRS):
        r, cc = divmod(i, 5)
        x, yy = 150 + cc * 160, 470 + r * 150
        col = RED if sg < 0 else ((0.4, 0.42, 0.5) if sg == 0 else GRN)
        a = k(t, st + 0.4, st + 0.8) if sg < 0 else 1
        S.rrect(c, x, yy, 140, 120, 16); c.set_source_rgba(*col, 0.85 * a if sg < 0 else 0.35); c.fill()
        T(c, str(y), x + 70, yy + 72, 38, WHITE, stroke=None)
    if t > st + 1.2:
        T(c, "4 TIMES", 540, 1020, 120, RED, k(t, st + 1.2, st + 1.5), lw=12)


def o_drivers(c, t, lt):
    st = sh.s(5)
    K.panel(c, 860, 520)
    T(c, "WHAT MOVES GOLD", 540, 950, 54, YEL, stroke=None)
    K.rows(c, t, st, [("Global gold price", WHITE, 48, 0.4), ("Dollar", WHITE, 48, 1.2), ("Rupee", WHITE, 48, 2.0)],
           y0=1060, gap=85)
    K.stamp(c, t, st + 3.0, "NOT THE DATE", 540, 1330, RED, 50, -0.05)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 900, 420)
    T(c, "'UPAR HI JAYEGA'", 540, 1040, 76, GOLD, k(t, st + 0.2, st + 0.4), stroke=None)
    K.stamp(c, t, st + 1.0, "SAME BRO?", 540, 1210, YEL, 64, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "GOLD RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Tradition? Buy, enjoy it", WHITE, 42, 0.6, "left", 140),
                      ("2. Invest = small amounts, years", GRN, 40, 2.4, "left", 140),
                      ("3. Check the BIS HALLMARK", WHITE, 42, 4.0, "left", 140)], y0=1070, gap=100)
    if t > st + 5.0:
        T(c, "education only, not advice", 540, 1350, 32, GREY, k(t, st + 5.0, st + 5.3), stroke=None)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "THE DATE IS SHUBH.", "PROFIT ISN'T GUARANTEED", GOLD)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO SAYS GOLD ONLY GOES UP", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'warm'
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), rw(mouth='o', eyes=1.2), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'warm'),
        (s(2), s(3), rw(mouth='bigsmile', eyes=1.2, arms=((60, 120), (14, -10))), (2.0, 1000, 470), (2.15, 1000, 450), o_family, 'warm'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_check, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_four, 'red'),
        (s(5), s(6), sw(), (1.78, 960, 540), (1.85, 960, 520), o_drivers, 'money'),
        (s(6), s(7), rw(mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), rw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw(mouth='bigsmile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
