import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
import fest as F  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s31_sale"
CAPS = [
    "Festive sale: '70% OFF!' Sid's cart is full. So how do companies still make money?",
    "Secret 1: VOLUME. Redseer: about ₹24,000 crore of online sales in the first 2 days.",
    "Secret 2: some prices go UP before the sale. The 'discount' just cancels the hike.",
    "Techarc checked 50 phones in a July 2026 sale: 68% still cost MORE than launch price.",
    "Secret 3: sales clear old stock and pull in new buyers for the whole year.",
    "So the 'sale' is a planned business event. Not charity, bro.",
    "Rule: track prices for weeks, compare with launch price, buy only what's on your list.",
    "MORAL: A discount you didn't need is not saving.",
    "Send this to the friend whose cart is full before the sale even starts.",
]
HOOK = [("EVERYTHING ON SALE", WHITE), ("HOW DO THEY", RED), ("STILL EARN?", YEL)]
SRC = "Source: Redseer via BW Disrupt (Oct 2026); Techarc"
sh = None


def scene(c, t, lt, **kw):
    F.room(c, t, lt, **kw)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_cart(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    K.stamp(c, t, st + 0.3, "70% OFF!", 540, 1000, RED, 70, -0.04)
    K.rows(c, t, st, [("CART: 14 items", WHITE, 54, 1.6)], y0=1170)
    if t > st + 3.4:
        T(c, "how do THEY earn?", 540, 1300, 50, YEL, k(t, st + 3.4, st + 3.7), stroke=None)


def o_volume(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "SECRET 1: VOLUME", 540, 400, 74, YEL, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "₹24,000 Cr", 540, 640, 140, GRN, k(t, st + 1.2, st + 1.5), lw=14)
    T(c, "online sales, first 2 days", 540, 760, 52, WHITE, k(t, st + 1.8, st + 2.1), lw=6)
    T(c, "(Redseer estimate, 2026)", 540, 830, 38, GREY, k(t, st + 1.8, st + 2.1), lw=5)
    if t > st + 3.4:
        T(c, "small margin x HUGE orders", 540, 1010, 58, YEL, k(t, st + 3.4, st + 3.7), lw=8)


def o_hike(c, t, lt):
    st = sh.s(3)
    K.panel(c, 870, 500)
    T(c, "SECRET 2 (example)", 540, 950, 48, GREY, stroke=None)
    K.rows(c, t, st, [("Before sale: ₹10,000", WHITE, 50, 0.5), ("Hiked to: ₹11,000", RED, 50, 1.6),
                      ("'Sale': ₹10,000", GRN, 50, 2.8)], y0=1040, gap=95)
    K.stamp(c, t, st + 4.0, "SAME PRICE", 540, 1335, RED, 40, 0.03)


def o_phones(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "TECHARC: 50 PHONES", 540, 400, 70, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    T(c, "festive sale, July 2026", 540, 470, 38, GREY, k(t, st + 0.3, st + 0.6), lw=5)
    for i in range(50):
        r, col_ = divmod(i, 10)
        x = 175 + col_ * 81
        y = 580 + r * 105
        dt = 1.0 + i * 0.04
        a = k(t, st + dt, st + dt + 0.15)
        if a > 0:
            cc = RED if i < 34 else GREY
            S.rrect(c, x - 22, y - 38, 44, 76, 10); c.set_source_rgba(*cc, a); c.fill()
    if t > st + 3.4:
        T(c, "68% cost MORE", 540, 1180, 90, RED, k(t, st + 3.4, st + 3.7), lw=10)
        T(c, "than launch price, even after the sale", 540, 1250, 38, WHITE, k(t, st + 3.4, st + 3.7), lw=5)


def o_stock(c, t, lt):
    st = sh.s(5)
    K.panel(c, 870, 500)
    T(c, "SECRET 3", 540, 950, 48, GREY, stroke=None)
    K.rows(c, t, st, [("Old stock: CLEARED", YEL, 54, 0.6), ("New buyers: HOOKED", GRN, 54, 2.0),
                      ("they shop all year", WHITE, 46, 3.2)], y0=1050, gap=105)


def o_plan(c, t, lt):
    st = sh.s(6)
    U.dim(c, 0.88)
    T(c, "SALE =", 540, 520, 100, WHITE, k(t, st + 0.3, st + 0.6), lw=12)
    T(c, "A PLANNED", 540, 680, 110, YEL, k(t, st + 0.9, st + 1.2), lw=12)
    T(c, "BUSINESS EVENT", 540, 810, 96, YEL, k(t, st + 0.9, st + 1.2), lw=12)
    K.stamp(c, t, st + 2.4, "NOT CHARITY", 540, 1020, RED, 56, -0.04)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "SALE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Track the price for weeks", WHITE, 42, 0.8, "left", 140),
                      ("2. Compare with launch price", GRN, 42, 2.2, "left", 140),
                      ("3. Buy only from your list", WHITE, 42, 3.6, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "DIDN'T NEED IT?", "THEN IT'S NOT SAVING")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WITH A FULL CART ALREADY", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), rw(mouth='bigsmile', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_cart, 'warm'),
        (s(2), s(3), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_volume, 'studio'),
        (s(3), s(4), rw(mouth='o', eyes=1.3, **ph), (1.9, 1000, 480), (2.0, 1000, 460), o_hike, 'warm'),
        (s(4), s(5), sw(), (1.78, 960, 540), (1.85, 960, 520), o_phones, 'studio'),
        (s(5), s(6), rw(mouth='flat', squint=0.3, **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_stock, 'warm'),
        (s(6), s(7), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_plan, 'studio'),
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
