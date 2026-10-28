import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s17_cod"
CAPS = [
    "Sid buys a t-shirt online. ₹399. Picks Cash on Delivery, and the total becomes ₹408.",
    "Where did the extra money come from? One tiny line: HANDLING FEE.",
    "Listen. This is called DRIP PRICING. Show a cheap price first, then add fees one by one at checkout.",
    "Why? By the time you reach checkout, your mind is made up. Who cancels over ₹10-20?",
    "In October 2025, the Consumer Affairs Minister said extra charges on Cash on Delivery are a DARK PATTERN. A probe started.",
    "And as per a LocalCircles survey, only 3% of e-commerce platforms were free of such tricks.",
    "Simple rule: ignore the product page price. Check the FINAL checkout total, then compare with another site.",
    "Send this to the friend who says \"only COD bro, trust issues\".",
]
HOOK = [("₹399 BECAME ₹408?", WHITE), ("THE CASH ON", RED), ("DELIVERY TRICK", YEL)]
SRC = "Source: Inc42 / CCPA probe, Oct 2025; LocalCircles"
sh = None


def room(c, t, lt, mode='night', **kw):
    V.room(c, t, mode)
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1 if mode == 'night' else 0.3)
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_cart(c, t, lt):
    st = sh.s(1)
    cod = t > st + 3.2
    items = [("T-shirt", "₹399"), ("Payment", "COD" if cod else "--")]
    total = "₹408" if t > st + 5.0 else "₹399"
    U.phone_frame(c, 240, 830, 600, 600, K.bill_screen("CHECKOUT", items, total,
                  total_col=RED if t > st + 5.0 else (0.1, 0.1, 0.12)), t, glow=0.2)


def o_fee(c, t, lt):
    st = sh.s(2)
    items = [("T-shirt", "₹399"), ("Payment", "COD"), ("Handling fee", "₹9")]
    hi = [2] if t > st + 2.0 else None
    U.phone_frame(c, 240, 830, 600, 600, K.bill_screen("CHECKOUT", items, "₹408", hi=hi, total_col=RED), t, glow=0.2)


def o_drip(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "DRIP", 540, 400, 150, YEL, k(t, st + 0.8, st + 1.1), lw=14)
    T(c, "PRICING", 540, 540, 110, YEL, k(t, st + 1.1, st + 1.4), lw=12)
    T(c, "₹399", 540, 760, 110, GRN, k(t, st + 2.4, st + 2.7), lw=12)
    fees = ["+ handling fee", "+ platform fee", "+ convenience fee"]
    for i, f in enumerate(fees):
        t0 = st + 3.4 + i * 0.9
        if t < t0:
            continue
        a = k(t, t0, t0 + 0.3)
        y = 880 + i * 110 - 60 * (1 - U.eob(a))
        S.rrect(c, 250, y - 50, 580, 80, 40); c.set_source_rgba(0.5, 0.08, 0.1, a); c.fill()
        T(c, f, 540, y + 5, 44, WHITE, a, stroke=None)


def o_why(c, t, lt):
    st = sh.s(4)
    K.panel(c, 880, 440)
    K.rows(c, t, st, [("At checkout, your mind", WHITE, 46, 0.5),
                      ("is ALREADY MADE UP", YEL, 54, 1.0),
                      ("Cancel for ₹10-20?", WHITE, 48, 2.8),
                      ("Nobody does.", RED, 54, 3.8)], y0=970, gap=100)


def o_govt(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "OCT 2025", 540, 400, 64, GREY, k(t, st + 0.3, st + 0.6), lw=8)
    T(c, "Consumer Affairs Ministry", 540, 500, 54, WHITE, k(t, st + 1.2, st + 1.5), lw=8)
    T(c, "EXTRA COD CHARGES", 540, 680, 84, YEL, k(t, st + 3.0, st + 3.3), lw=12)
    T(c, "= DARK PATTERN", 540, 800, 90, RED, k(t, st + 4.8, st + 5.1), lw=12)
    K.stamp(c, t, st + 7.0, "PROBE STARTED", 540, 1020, RED, 56)


def o_three(c, t, lt):
    st = sh.s(6)
    U.dim(c, 0.9)
    T(c, "ONLY 3%", 540, 420, 150, GRN, k(t, st + 2.4, st + 2.7), lw=14)
    for i in range(100):
        x = 225 + (i % 10) * 70; y = 560 + (i // 10) * 62
        a = k(t, st + 0.5 + i * 0.01, st + 0.7 + i * 0.01)
        col = GRN if (i < 3 and t > st + 2.4) else (RED if t > st + 2.4 else (0.5, 0.52, 0.6))
        c.arc(x, y, 24, 0, 2 * math.pi); c.set_source_rgba(*col, a); c.fill()
    if t > st + 3.2:
        T(c, "of platforms had NO tricks", 540, 1250, 56, WHITE, k(t, st + 3.2, st + 3.5), lw=8)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "BEFORE YOU PAY", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Skip the product price", WHITE, 46, 1.4, "left", 160),
                      ("2. Check FINAL total", GRN, 46, 3.0, "left", 160),
                      ("3. Compare another site", WHITE, 46, 5.0, "left", 160)], y0=1070, gap=100)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE", "\"ONLY COD BRO\" FRIEND", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: room(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), rw(mouth='smile'), (1.9, 1000, 480), (2.1, 1000, 450), o_cart, 'phone'),
        (s(2), s(3), rw(mouth='o', eyes=1.2, raise_=1), (2.0, 1000, 480), (2.1, 1000, 460), o_fee, 'phone'),
        (s(3), s(4), sw(), (1.78, 960, 540), (1.85, 960, 520), o_drip, 'studio'),
        (s(4), s(5), sw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 960, 500), (2.0, 960, 470), o_why, 'studio'),
        (s(5), s(6), sw(), (1.78, 960, 540), (1.85, 960, 520), o_govt, 'studio'),
        (s(6), s(7), sw(), (1.78, 960, 540), (1.85, 960, 520), o_three, 'studio'),
        (s(7), s(8), rw(mode='day', mouth='smirk', squint=0.4), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'morning'),
        (s(8), sh.dur + 1, rw(mode='day', mouth='smile', phone=None, arms=((14, -10), (100, 40))), (1.9, 1000, 500),
         (2.1, 1000, 470), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1, 5.8] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
