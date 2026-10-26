import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import envx as X  # noqa: E402
import body as B  # noqa: E402
import env as V  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s08_sale"
CAPS = [
    "BIG SALE! 70% OFF! Sid filled his cart.",
    "But one audit tracked 325 products across the 2024 and 2025 festive sales.",
    "1 in 5 products got MORE EXPENSIVE right before the sale. Then came the \"discount\".",
    "And that 70% off is often calculated from MRP, not from the price it actually sold at last month.",
    "So the discount looks BIG. The saving isn't.",
    "Plus \"only 2 left\", \"sale ends in 10 minutes\". All built so you don't get time to think.",
    "The trick: note the price 2 weeks BEFORE the sale, or check its price history. Then decide.",
    "Send this to the friend who buys something in EVERY sale.",
]
HOOK = [("THE SALE TRICK", YEL), ("NOBODY TELLS", WHITE), ("YOU ABOUT", WHITE)]
SRC = "Source: PriceHistory audit, 325 products (2024-25)"
sh = None


def w_room(c, t, lt):
    V.room(c, t, 'night')
    B.figure(c, 1000, 330, 0.5, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1, mouth='bigsmile',
             eyes=1.1)


def o_phone(c, t, lt):
    U.phone_frame(c, 240, 260, 600, 1080, X.shop_phone_screen(2999, 9999, 70, t), t, tilt=-2 + 3 * lt)
    n = 1 + int(4 * k(t, 1.2, 3.5))
    c.arc(880, 330, 50, 0, 2 * math.pi); c.set_source_rgb(*RED); c.fill()
    T(c, str(n), 880, 350, 50, WHITE, stroke=None)


def o_audit(c, t, lt):
    U.dim(c, 0.6)
    v = int(325 * k(t, sh.s(2) + 2.0, sh.s(2) + 3.5))
    T(c, f"{v}", 540, 700, 260, YEL, lw=22)
    T(c, "PRODUCTS TRACKED", 540, 820, 64, WHITE)
    T(c, "Big festive sales · 2024 + 2025", 540, 900, 40, (0.8, 0.82, 0.9), stroke=None)


def o_raise(c, t, lt):
    U.dim(c, 0.75)
    for i in range(5):
        x = 170 + i * 185
        hit = i == 2 and t > sh.s(3) + 1.5
        U.ppl(c, x, 560, 120, RED if hit else (0.55, 0.57, 0.65))
    if t > sh.s(3) + 1.5:
        T(c, "1 IN 5", 540, 380, 150, RED, k(t, sh.s(3) + 1.5, sh.s(3) + 1.8), lw=16)
    # price line
    c.save(); c.translate(140, 820)
    pts = [(0, 200), (200, 200), (380, 200), (480, 60), (620, 60), (700, 190), (800, 190)]
    n = int(len(pts) * k(t, sh.s(3) + 2.0, sh.s(3) + 4.5)) + 1
    c.move_to(*pts[0])
    for p in pts[1:n]:
        c.line_to(*p)
    c.set_source_rgb(*YEL); c.set_line_width(12); c.stroke()
    if n >= 4:
        T(c, "price UP", 430, 30, 40, RED, stroke=None)
    if n >= 6:
        T(c, "\"SALE\"", 700, 260, 44, GRN, stroke=None)
    c.restore()


def o_mrp(c, t, lt):
    U.dim(c, 0.8)
    rows = [("MRP", "₹9,999", (0.6, 0.62, 0.7), sh.s(4) + 0.3), ("LAST MONTH", "₹3,999", WHITE, sh.s(4) + 3.0),
            ("SALE", "₹2,999", GRN, sh.s(4) + 1.2)]
    for i, (a, b, col, t0) in enumerate(rows):
        al = k(t, t0, t0 + 0.3)
        S.rrect(c, 120, 380 + i * 220, 840, 180, 26); c.set_source_rgba(0.08, 0.09, 0.13, 0.95 * al); c.fill()
        T(c, a, 170, 490 + i * 220, 50, (0.8, 0.82, 0.9), al, stroke=None, anchor="left")
        T(c, b, 910, 500 + i * 220, 80, col, al, stroke=None, anchor="right")
    if t > sh.s(4) + 1.2:
        T(c, "\"70% OFF\"", 540, 300, 80, YEL, k(t, sh.s(4) + 1.2, sh.s(4) + 1.5))
    if t > sh.s(5) - 0.5:
        T(c, "REAL SAVING: 25%", 540, 1110, 76, RED, k(t, sh.s(5) - 0.5, sh.s(5) - 0.2))


def o_urgency(c, t, lt):
    U.dim(c, 0.5)
    U.phone_frame(c, 240, 260, 600, 1080, X.shop_phone_screen(2999, 9999, 70, t, stock="Only 2 left!",
                  timer=f"Ends in 0{9 - int((t * 3) % 10)}:{59 - int(t * 30) % 60:02d}"), t,
                  tilt=math.sin(t * 25) * 1.5)


def w_think(c, t, lt):
    V.room(c, t, 'day')
    B.figure(c, 900, 330, 0.55, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=0.3, mouth='smirk',
             squint=0.4)


def o_rule(c, t, lt):
    S.rrect(c, 90, 860, 900, 480, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
    T(c, "BEFORE ANY SALE", 540, 950, 62, YEL, stroke=None)
    T(c, "1. Note the price 2 weeks before", 140, 1060, 42, WHITE, k(t, sh.s(7) + 1.5, sh.s(7) + 1.8), stroke=None, anchor="left")
    T(c, "2. Check price history", 140, 1150, 42, WHITE, k(t, sh.s(7) + 3.5, sh.s(7) + 3.8), stroke=None, anchor="left")
    T(c, "3. THEN decide", 140, 1240, 42, GRN, k(t, sh.s(7) + 5.5, sh.s(7) + 5.8), stroke=None, anchor="left")


def w_end(c, t, lt):
    V.room(c, t, 'day')
    B.figure(c, 1000, 330, 0.5, t, pose='stand', mouth='smile', arms=((14, -10), (100, 40)))


def o_end(c, t, lt):
    S.rrect(c, 140, 260, 800, 230, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    T(c, "SEND TO THE", 540, 360, 64, WHITE, stroke=None)
    T(c, "SALE ADDICT", 540, 445, 76, YEL, stroke=None)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    sh.shots = [
        (0, s(2), w_room, (1.9, 1000, 480), (2.1, 1000, 450), o_phone, 'phone'),
        (s(2), s(3), w_room, (1.78, 960, 540), (1.9, 960, 520), o_audit, 'night'),
        (s(3), s(4), w_room, (1.78, 960, 540), (1.85, 1000, 540), o_raise, 'red'),
        (s(4), s(6), w_room, (1.78, 960, 540), (1.85, 900, 540), o_mrp, 'night'),
        (s(6), s(7), w_room, (1.9, 1000, 480), (2.0, 1000, 460), o_urgency, 'red'),
        (s(7), s(8), w_think, (1.9, 900, 480), (2.0, 900, 460), o_rule, 'morning'),
        (s(8), sh.dur + 1, w_end, (1.9, 1000, 480), (2.1, 1000, 440), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview([1, 3.5, 6, 11, 13, 17, 21, 25, 30, 33, 38, 42, 45], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
