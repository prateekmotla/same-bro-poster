import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s25_dip"
CAPS = [
    "Market falls 5%. Sid throws ALL his savings in. 'Buy the dip, bro!'",
    "Next week it falls AGAIN. He buys again. Now there's no cash left.",
    "Hidden truth: a dip can be the START of a big fall. Nobody knows which one.",
    "Jan 2008: Sensex fell to 17,605. Looked like a dip. People bought.",
    "Oct 2008: Sensex at 8,701. That 'dip' fell about 50% MORE.",
    "Lump sums into every dip = no plan, just FOMO. Cash runs out before the bottom.",
    "Rule: fixed amount every month (SIP), emergency fund first, extra only as per a written plan.",
    "MORAL: Invest with a plan, not with FOMO.",
    "Send this to the friend who says 'buy the dip' every single day.",
]
HOOK = [("'BUY EVERY DIP'", WHITE), ("CAN EMPTY", RED), ("YOUR ACCOUNT", YEL)]
SRC = "Source: BSE Sensex data (Jan & Oct 2008)"
sh = None


def scene(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)



def o_dip(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    K.rows(c, t, st, [("MARKET -5%", RED, 72, 0.3), ("ALL SAVINGS: IN", WHITE, 60, 1.6)], y0=1000, gap=130)
    K.stamp(c, t, st + 3.0, "BUY THE DIP!", 540, 1290, GRN, 52)


def o_again(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    pts = [0.95, 0.8, 0.85, 0.6, 0.65, 0.4, 0.45, 0.2]
    TR.line(c, t, st + 0.3, 180, 930, 720, 260, pts, RED, dur=2.4, lw=8)
    TR.marker(c, t, st + 0.3 + 2.4 * 3 / 7, 180 + 720 * 3 / 7, 930 + 260 * 0.4, "BUY", GRN, 34)
    TR.marker(c, t, st + 0.3 + 2.4 * 5 / 7, 180 + 720 * 5 / 7, 930 + 260 * 0.6, "BUY", GRN, 34)
    if t > st + 3.2:
        T(c, "CASH LEFT: ₹0", 540, 1300, 62, RED, k(t, st + 3.2, st + 3.5), stroke=None)


def o_start(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "IS THIS A DIP...", 540, 460, 80, WHITE, k(t, st + 0.3, st + 0.6), lw=10)
    T(c, "OR THE START", 540, 640, 92, RED, k(t, st + 1.4, st + 1.7), lw=12)
    T(c, "OF A CRASH?", 540, 760, 92, RED, k(t, st + 1.4, st + 1.7), lw=12)
    if t > st + 3.2:
        T(c, "NOBODY KNOWS", 540, 1000, 100, YEL, k(t, st + 3.2, st + 3.5), lw=12)


PTS08 = [0.95, 0.72, 0.8, 0.7, 0.76, 0.6, 0.64, 0.5, 0.42, 0.34, 0.12]


def chart08(c, t, st, upto):
    U.dim(c, 0.88)
    T(c, "SENSEX 2008", 540, 380, 74, WHITE, lw=8)
    T(c, "(simplified chart)", 540, 440, 32, GREY, lw=5)
    n = len(PTS08) - 1
    x, y, w, h = 140, 520, 800, 640
    c.set_source_rgba(1, 1, 1, 0.08); c.rectangle(x, y, w, h); c.fill()
    TR.line(c, t, st + 0.3, x, y, w / n, h, PTS08[:2], RED, dur=1.2, lw=10)
    if upto == 1:
        TR.marker(c, t, st + 1.6, x + w / n, y + h * (1 - PTS08[1]), "17,605", YEL, 44, up=False)
        if t > st + 2.4:
            T(c, "\"just a dip\"", 540, 1260, 70, GRN, k(t, st + 2.4, st + 2.7), lw=10)
    return x, y, w, h, n


def o_jan(c, t, lt):
    chart08(c, t, sh.s(4), 1)


def o_oct(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "SENSEX 2008", 540, 380, 74, WHITE, lw=8)
    T(c, "(simplified chart)", 540, 440, 32, GREY, lw=5)
    n = len(PTS08) - 1
    x, y, w, h = 140, 520, 800, 640
    c.set_source_rgba(1, 1, 1, 0.08); c.rectangle(x, y, w, h); c.fill()
    # fixed first leg + growing rest
    TR.line(c, t, st - 100, x, y, w / n, h, PTS08[:2], RED, dur=1, lw=10)
    TR.line(c, t, st + 0.2, x + w / n, y, w * (n - 1) / n, h, PTS08[1:], RED, dur=2.4, lw=10, a=1.0)
    TR.marker(c, t, st - 100, x + w / n, y + h * (1 - PTS08[1]), "17,605", YEL, 40, up=False)
    TR.marker(c, t, st + 2.6, x + w, y + h * (1 - PTS08[-1]), "8,701", RED, 44, up=True)
    if t > st + 3.2:
        T(c, "~50% MORE DOWN", 540, 1290, 80, RED, k(t, st + 3.2, st + 3.5), lw=10)


def o_fomo(c, t, lt):
    st = sh.s(6)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("Lump sum every dip", WHITE, 52, 0.5), ("= NO PLAN, JUST FOMO", RED, 56, 1.8),
                      ("cash runs out", GREY, 46, 3.2), ("BEFORE the bottom", YEL, 56, 3.6)], y0=970, gap=105)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Fixed amount monthly (SIP)", WHITE, 42, 0.8, "left", 140),
                      ("2. Emergency fund FIRST", GRN, 42, 2.2, "left", 140),
                      ("3. Extra only by written plan", WHITE, 42, 3.6, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "INVEST WITH A PLAN,", "NOT WITH FOMO")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO 'BUYS EVERY DIP'", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), aw(crash=8, mouth='bigsmile', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_dip, 'night'),
        (s(2), s(3), aw(crash=4, mouth='o', eyes=1.3, **ph), (1.9, 1000, 480), (2.0, 1000, 460), o_again, 'red'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_start, 'studio'),
        (s(4), s(5), sw(), (1.78, 960, 540), (1.85, 960, 520), o_jan, 'studio'),
        (s(5), s(6), sw(mouth='frown'), (1.78, 960, 540), (1.85, 960, 520), o_oct, 'red'),
        (s(6), s(7), aw(crash=2, mouth='frown', squint=0.4), (1.9, 1000, 500), (2.0, 1000, 470), o_fomo, 'night'),
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
