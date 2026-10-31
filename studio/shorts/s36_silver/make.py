import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s36_silver"
SIL = (0.82, 0.85, 0.92)
CAPS = [
    "Silver was ₹3.1 lakh a kg in May. Now? ₹2 lakh. Down about 35%.",
    "Sid bought near the top because 'silver only goes up'. Now he wants to panic-sell.",
    "What happened? Fear of another US Fed rate hike. Higher rates make metals that pay no interest less attractive.",
    "Plus costly crude, rising yields, and a tech-stock sell-off that forced leveraged traders to sell.",
    "October alone: silver fell about 15%. Last week (24-31 Oct): down around 9%.",
    "Silver swings much harder than gold. Big rallies, big falls. That's normal for it.",
    "Rule: keep metals a SMALL slice of your money, buy in parts, never with borrowed money.",
    "MORAL: Don't chase a rally. Don't panic in a fall.",
    "Send this to the friend who bought silver at the very top.",
]
HOOK = [("SILVER DOWN 35%", WHITE), ("FROM ITS PEAK", RED), ("WHY + WHAT TO DO", YEL)]
SRC = "Source: Goodreturns India rates (31 Oct 2026)"
sh = None


def scene(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash, ticker="SILVER")
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def bar(c, x, y, w, h, a=1.0):
    c.move_to(x + 30, y); c.line_to(x + w - 30, y); c.line_to(x + w, y + h); c.line_to(x, y + h); c.close_path()
    c.set_source_rgba(*SIL, a); c.fill()
    c.move_to(x + 30, y); c.line_to(x + w - 30, y); c.line_to(x + w - 50, y + 16); c.line_to(x + 50, y + 16); c.close_path()
    c.set_source_rgba(1, 1, 1, 0.5 * a); c.fill()


PTS = [0.30, 0.55, 0.95, 0.80, 0.72, 0.62, 0.52, 0.40, 0.22, 0.08]


def o_peak(c, t, lt):
    st = sh.s(1)
    U.dim(c, 0.85)
    T(c, "SILVER, ₹ PER KG", 540, 400, 60, SIL, k(t, st + 0.1, st + 0.4), lw=8)
    TR.line(c, t, st + 0.3, 140, 520, 800, 420, PTS, RED, 2.6, 12)
    if t > st + 0.9:
        T(c, "₹3.1 lakh (13 May)", 380, 500, 44, WHITE, k(t, st + 0.9, st + 1.2), lw=6)
    if t > st + 2.4:
        T(c, "₹2 lakh (31 Oct)", 760, 1010, 44, WHITE, k(t, st + 2.4, st + 2.7), lw=6)
        T(c, "-35%", 540, 1150, 130, RED, k(t, st + 3.0, st + 3.3), lw=14)


def o_sid(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    bar(c, 380, 950, 320, 110, k(t, st + 0.2, st + 0.5))
    K.rows(c, t, st, [("'only goes UP'", WHITE, 56, 0.8)], y0=1140)
    K.stamp(c, t, st + 2.8, "PANIC SELL?", 540, 1270, RED, 58, -0.05)


def o_fed(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "REASON 1", 540, 400, 60, GREY, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "US FED RATE", 540, 540, 100, WHITE, k(t, st + 0.6, st + 0.9), lw=12)
    T(c, "HIKE FEARS", 540, 660, 100, RED, k(t, st + 0.6, st + 0.9), lw=12)
    if t > st + 2.4:
        T(c, "higher rates = metals look", 540, 850, 50, WHITE, k(t, st + 2.4, st + 2.7), lw=6)
        T(c, "less attractive (no interest)", 540, 920, 50, YEL, k(t, st + 2.4, st + 2.7), lw=6)


def o_more(c, t, lt):
    st = sh.s(4)
    K.panel(c, 860, 520)
    T(c, "REASONS 2-4", 540, 950, 54, GREY, stroke=None)
    K.rows(c, t, st, [("Costly crude oil", WHITE, 46, 0.6), ("Rising bond yields", WHITE, 46, 1.4),
                      ("Tech sell-off > forced selling", RED, 44, 2.4)], y0=1060, gap=100)


def o_month(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "OCTOBER 2026", 540, 420, 64, GREY, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "-15%", 540, 610, 160, RED, k(t, st + 0.6, st + 0.9), lw=16)
    if t > st + 2.2:
        T(c, "last week (24-31 Oct)", 540, 790, 50, GREY, k(t, st + 2.2, st + 2.5), lw=6)
        T(c, "-9%", 540, 930, 130, RED, k(t, st + 2.4, st + 2.7), lw=14)


def o_swing(c, t, lt):
    st = sh.s(6)
    U.dim(c, 0.88)
    T(c, "SILVER vs GOLD", 540, 400, 72, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    gpts = [0.5, 0.55, 0.6, 0.58, 0.62, 0.6, 0.64, 0.62]
    spts = [0.5, 0.75, 0.95, 0.6, 0.85, 0.35, 0.7, 0.3]
    TR.line(c, t, st + 0.6, 140, 520, 800, 380, gpts, YEL, 2.0, 9)
    TR.line(c, t, st + 0.6, 140, 520, 800, 380, spts, SIL, 2.0, 9)
    if t > st + 2.8:
        T(c, "gold", 200, 980, 44, YEL, k(t, st + 2.8, st + 3.1), stroke=None, anchor="left")
        T(c, "silver = WILDER swings", 880, 980, 44, SIL, k(t, st + 2.8, st + 3.1), stroke=None, anchor="right")
        T(c, "(illustration)", 540, 1050, 34, GREY, k(t, st + 2.8, st + 3.1), stroke=None)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "METALS RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Keep it a SMALL slice", WHITE, 42, 0.8, "left", 140),
                      ("2. Buy in parts, not all at once", GRN, 40, 2.2, "left", 140),
                      ("3. NEVER with borrowed money", RED, 42, 3.6, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "DON'T CHASE A RALLY,", "DON'T PANIC IN A FALL")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO BOUGHT AT THE TOP", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), aw(crash=3, mouth='o', eyes=1.3), (1.9, 1000, 480), (2.1, 1000, 450), o_peak, 'red'),
        (s(2), s(3), aw(crash=3, mouth='grit', squint=0.4, **ph), (1.9, 1000, 480), (2.0, 1000, 460), o_sid, 'red'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_fed, 'studio'),
        (s(4), s(5), aw(crash=2, mouth='frown'), (1.9, 1000, 500), (2.0, 1000, 470), o_more, 'night'),
        (s(5), s(6), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_month, 'red'),
        (s(6), s(7), sw(), (1.78, 960, 540), (1.85, 960, 520), o_swing, 'studio'),
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
