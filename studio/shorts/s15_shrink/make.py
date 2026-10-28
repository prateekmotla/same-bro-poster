import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s15_shrink"
CAPS = [
    "Sid buys a ₹10 Parle-G. Same price, same packet. But it feels... LIGHTER.",
    "The ₹10 pack used to have 140g of biscuits. Then it became 110g. SAME PRICE.",
    "Maggi too. A 100g pack became 70g. And the price went from ₹10 to ₹12.",
    "This is called SHRINKFLATION. Don't raise the price, just give you LESS.",
    "Why? ₹10 is fixed in your head. Raise the price, customers run. Cut grams? NOBODY notices.",
    "Same colour, same design, so your eyes can't catch it.",
    "Simple rule: ignore the front price. Check the NET WEIGHT on the back. Work out price per gram, THEN compare.",
    "Send this to the friend who says \"bro, it used to be bigger\".",
]
HOOK = [("SAME ₹10", YEL), ("LESS BISCUIT?", WHITE), ("THE HIDDEN TRICK", RED)]
SRC = "Source: ThePrint, May 2022 (FMCG pack sizes)"
sh = None


def canteen(c, t, lt, **kw):
    V.canteen(c, t)
    K.sid(c, t, 1000, 330, 0.5, pose='sit', **kw)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def room(c, t, lt, **kw):
    V.room(c, t, 'day')
    K.sid(c, t, 1000, 330, 0.5, pose='sit', **kw)


def o_buy(c, t, lt):
    st = sh.s(1)
    K.packet(c, 540, 1160, 0.75, "GLUCO", "110g", a=k(t, st + 0.5, st + 0.8))
    if t > st + 3.0:
        T(c, "?", 760, 1020, 140, YEL, k(t, st + 3.0, st + 3.2), lw=14)


def o_then(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.86)
    T(c, "SAME ₹10 PACK", 540, 400, 72, WHITE, k(t, st + 0.2, st + 0.5), lw=10)
    K.packet(c, 300, 760, 0.85, "GLUCO", "140g", a=k(t, st + 0.8, st + 1.1))
    if t > st + 3.0:
        a = k(t, st + 3.0, st + 3.3)
        T(c, ">", 540, 790, 120, YEL, a, lw=10)
        K.packet(c, 790, 790, 0.7, "GLUCO", "110g", a=a)
    if t > st + 5.0:
        T(c, "30g GONE", 540, 1180, 96, RED, k(t, st + 5.0, st + 5.3), lw=12)
    K.stamp(c, t, st + 6.0, "PRICE SAME", 540, 1330, RED, 50)


def o_maggi(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.86)
    T(c, "NOODLES", 540, 420, 80, WHITE, k(t, st + 0.1, st + 0.4), lw=10)
    T(c, "100g > 70g", 540, 640, 120, YEL, k(t, st + 1.0, st + 1.3), lw=14)
    T(c, "₹10 > ₹12", 540, 860, 120, RED, k(t, st + 3.0, st + 3.3), lw=14)
    if t > st + 4.2:
        T(c, "less food, MORE money", 540, 1060, 58, WHITE, k(t, st + 4.2, st + 4.5), lw=8)


def o_word(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("SHRINK", YEL, 170, 0.8), ("FLATION", RED, 170, 1.1), ("price same, packet less", WHITE, 56, 2.4)],
           y0=560, gap=190)


def o_why(c, t, lt):
    st = sh.s(5)
    K.panel(c, 880, 480)
    K.rows(c, t, st, [("₹10 = FIXED IN YOUR HEAD", YEL, 48, 0.6),
                      ("Price UP = customers leave", WHITE, 46, 2.6),
                      ("Grams DOWN = nobody notices", GRN, 46, 4.6)], y0=980, gap=120)


def o_spot(c, t, lt):
    st = sh.s(6)
    K.panel(c, 860, 520)
    T(c, "SPOT THE DIFFERENCE", 540, 940, 50, YEL, stroke=None)
    K.packet(c, 330, 1140, 0.5, "GLUCO", "140g", a=k(t, st + 0.3, st + 0.6))
    K.packet(c, 750, 1140, 0.5, "GLUCO", "110g", a=k(t, st + 0.6, st + 0.9))


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "BEFORE YOU BUY", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Flip the packet", WHITE, 48, 1.4, "left", 170),
                      ("2. Read NET WEIGHT", GRN, 48, 2.8, "left", 170),
                      ("3. Price per gram", WHITE, 48, 4.6, "left", 170)], y0=1070, gap=100)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE", "\"PEHLE ZYADA AATA THA\" FRIEND", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    cw = lambda **kw: (lambda c, t, lt: canteen(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), cw(mouth='flat', eyes=1.1, arms=((14, -10), (60, 120))), (1.9, 1000, 480), (2.1, 1000, 450), o_buy, 'warm'),
        (s(2), s(3), cw(), (1.78, 960, 540), (1.85, 960, 520), o_then, 'warm'),
        (s(3), s(4), cw(), (1.78, 960, 540), (1.85, 960, 520), o_maggi, 'warm'),
        (s(4), s(5), sw(), (1.78, 960, 540), (1.85, 960, 520), o_word, 'studio'),
        (s(5), s(6), sw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 960, 500), (2.0, 960, 470), o_why, 'studio'),
        (s(6), s(7), cw(squint=0.5, mouth='frown'), (1.9, 1000, 500), (2.0, 1000, 470), o_spot, 'warm'),
        (s(7), s(8), lambda c, t, lt: room(c, t, lt, mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'morning'),
        (s(8), sh.dur + 1, lambda c, t, lt: room(c, t, lt, mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500),
         (2.1, 1000, 470), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1, 3.5] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
