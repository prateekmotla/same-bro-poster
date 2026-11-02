import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s49_free"
CHOC = (0.45, 0.25, 0.12)
CAPS = [
    "Guess: a chocolate got just 1 cent cheaper, and almost 4x more people grabbed it. Why?",
    "Sid adds a ₹99 thing he doesn't even need. Why? 'FREE delivery above ₹499!'",
    "MIT test: Hershey's at 1 cent, Lindt at 14 cents. Only 8% picked Hershey's.",
    "Then: Hershey's FREE, Lindt 13 cents. Now 31% picked Hershey's. Same 1-cent gap.",
    "'FREE' switches off your maths. Companies know it: free delivery, free gift, buy 1 get 1.",
    "Same bro? Bought extra just to get something 'free'?",
    "Rule: before adding stuff for FREE, ask: 'Would I buy this extra thing alone?' No? Pay the fee.",
    "MORAL: FREE is the most expensive price.",
    "Send this to the friend who fills the cart for free delivery.",
]
HOOK = [("1 CENT CHEAPER", WHITE), ("= 4x MORE BUYERS?", YEL), ("THE 'FREE' TRAP", RED)]
SRC = "Source: Shampanier, Mazar & Ariely (2007), Zero as a Special Price"
sh = None


def scene(c, t, lt, **kw):
    V.room(c, t, 'night', fan=False)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def canteen(c, t, lt, **kw):
    V.canteen(c, t)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def choc(c, x, y, s, label, price, pcol, a=1.0):
    S.rrect(c, x - 130 * s, y - 80 * s, 260 * s, 160 * s, 20 * s); c.set_source_rgba(*CHOC, a); c.fill()
    T(c, label, x, y + 14 * s, 44 * s, WHITE, a, stroke=None)
    T(c, price, x, y + 150 * s, 64 * s, pcol, a, stroke=None)


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    choc(c, 540, 1040, 1.1, "CHOCOLATE", "-1 CENT", GRN, k(t, st + 0.2, st + 0.5))
    K.stamp(c, t, st + 2.4, "4x MORE PICKED IT", 540, 1290, YEL, 52, -0.05)


def o_cart(c, t, lt):
    st = sh.s(2)
    K.panel(c, 820, 560)
    T(c, "CART: ₹420", 540, 900, 56, WHITE, k(t, st + 0.1, st + 0.4), stroke=None)
    S.rrect(c, 160, 950, 760, 100, 26); c.set_source_rgba(0.12, 0.14, 0.2, 0.96 * k(t, st + 0.8, st + 1.1)); c.fill()
    T(c, "+ random thing  ₹99", 540, 1015, 48, YEL, k(t, st + 0.8, st + 1.1), stroke=None)
    T(c, "TOTAL ₹519", 540, 1130, 60, WHITE, k(t, st + 1.6, st + 1.9), stroke=None)
    K.stamp(c, t, st + 3.0, "FREE DELIVERY!", 540, 1290, GRN, 58, -0.05)


def o_test1(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.9)
    T(c, "MIT TEST #1", 540, 380, 62, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    choc(c, 300, 560, 0.9, "HERSHEY'S", "1¢".replace("¢", " cent"), WHITE, k(t, st + 0.5, st + 0.8))
    choc(c, 780, 560, 0.9, "LINDT", "14 cents", WHITE, k(t, st + 1.2, st + 1.5))
    K.hbar(c, t, st + 2.6, 140, 800, 800, 100, 0.08 / 0.4, RED, "picked Hershey's", "8%")


def o_test2(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "MIT TEST #2", 540, 380, 62, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    choc(c, 300, 560, 0.9, "HERSHEY'S", "FREE", GRN, k(t, st + 0.3, st + 0.6))
    choc(c, 780, 560, 0.9, "LINDT", "13 cents", WHITE, k(t, st + 1.0, st + 1.3))
    K.hbar(c, t, st + 2.4, 140, 800, 800, 100, 0.31 / 0.4, GRN, "picked Hershey's", "31%")
    if t > st + 3.6:
        T(c, "SAME 1-CENT GAP", 540, 1010, 58, YEL, k(t, st + 3.6, st + 3.9), lw=7)


def o_brain(c, t, lt):
    st = sh.s(5)
    K.panel(c, 820, 560)
    T(c, "'FREE' = MATHS OFF", 540, 900, 60, RED, k(t, st + 0.2, st + 0.5), stroke=None)
    K.rows(c, t, st, [("free delivery", WHITE, 50, 2.0), ("free gift", WHITE, 50, 2.8), ("buy 1 get 1", WHITE, 50, 3.6)], y0=1030, gap=95)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("BOUGHT EXTRA", WHITE, 60, 0.2), ("TO GET IT 'FREE'?", YEL, 60, 0.8)], y0=1000, gap=110)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("Ask: would I buy this", WHITE, 46, 0.8, "left", 140),
                      ("extra thing ALONE?", WHITE, 46, 0.8, "left", 140),
                      ("No? PAY THE FEE.", GRN, 52, 3.6, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "FREE IS THE MOST", "EXPENSIVE PRICE", RED)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO FILLS CARTS FOR 'FREE'", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    cw = lambda **kw: (lambda c, t, lt: canteen(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), cw(mouth='o', eyes=1.2), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'warm'),
        (s(2), s(3), rw(mouth='bigsmile', **ph), (2.0, 1000, 470), (2.15, 1000, 450), o_cart, 'night'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_test1, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_test2, 'money'),
        (s(5), s(6), rw(mouth='frown', squint=0.3, **ph), (1.9, 1000, 480), (2.0, 1000, 460), o_brain, 'night'),
        (s(6), s(7), cw(mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), cw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, cw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
