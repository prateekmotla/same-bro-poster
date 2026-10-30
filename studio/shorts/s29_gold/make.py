import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s29_gold"
CAPS = [
    "Dhanteras: 6 Nov. Mom: 'Gold le aana.' Sid checks the price... it FELL?",
    "Record, 29 Jan 2026: about ₹1.79 lakh per 10 g. 30 Oct: about ₹1.42 lakh.",
    "That's around 20% below peak. In October alone, gold fell nearly 5%.",
    "Why? Hot US inflation data. Markets now expect US interest rates to stay HIGH.",
    "Gold pays no interest. When rates stay high, FDs and bonds look better, so gold cools.",
    "Hidden cost: jewellery adds MAKING charges plus 3% GST. That part is not 'investment'.",
    "Rule: check the HUID hallmark (BIS Care app). Jewellery is to WEAR. Saving needs a plan.",
    "MORAL: Buy gold with a plan, not because of one day's price.",
    "Send this to the friend who buys gold only on Dhanteras.",
]
HOOK = [("GOLD FELL 20%", WHITE), ("BEFORE DHANTERAS?", RED), ("THE REAL REASON", YEL)]
SRC = "Source: Goodreturns (30 Oct 2026); ratestoday.in"
GOLD = (1.0, 0.78, 0.25)
sh = None


def diya(c, x, y, t, s=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.move_to(-40, 0); c.curve_to(-30, 30, 30, 30, 40, 0); c.close_path()
    c.set_source_rgb(0.75, 0.35, 0.15); c.fill()
    fl = 1 + 0.12 * math.sin(t * 13 + x)
    c.save(); c.scale(1, fl)
    c.move_to(0, -48); c.curve_to(14, -20, 10, -4, 0, -2); c.curve_to(-10, -4, -14, -20, 0, -48)
    c.set_source_rgb(1, 0.75, 0.2); c.fill(); c.restore()
    V.light(c, 0, -20, 90, (1, 0.7, 0.3), 0.35)
    c.restore()


def shop(c, t, lt, **kw):
    c.set_source(V.lingrad(c, 0, 0, 0, 780, [(0, (0.35, 0.12, 0.1)), (1, (0.55, 0.22, 0.14))]))
    c.rectangle(0, 0, 1920, 780); c.fill()
    c.set_source(V.lingrad(c, 0, 780, 0, 1080, [(0, (0.3, 0.2, 0.14)), (1, (0.16, 0.1, 0.07))]))
    c.rectangle(0, 780, 1920, 300); c.fill()
    # display shelves with necklaces
    for sx in (560, 1180):
        V.box(c, sx, 140, 300, 300, (0.12, 0.05, 0.05), 10, GOLD, 4)
        for j in range(2):
            cx, cy = sx + 150, 210 + j * 130
            c.arc(cx, cy - 30, 70, math.radians(20), math.radians(160))
            c.set_source_rgb(*GOLD); c.set_line_width(8); c.stroke()
            c.arc(cx, cy + 42, 12, 0, 2 * math.pi); c.fill()
    # string lights (Diwali)
    for i in range(40):
        x = 20 + i * 48
        y = 40 + 18 * math.sin(i * 0.7)
        on = 0.6 + 0.4 * math.sin(t * 4 + i * 1.3)
        col = [(1, 0.8, 0.3), (1, 0.4, 0.3), (0.5, 0.9, 1)][i % 3]
        c.arc(x, y, 8, 0, 2 * math.pi); c.set_source_rgba(*col, on); c.fill()
        V.light(c, x, y, 30, col, 0.25 * on)
    # glass counter
    V.box(c, 1160, 620, 760, 260, (0.6, 0.75, 0.8), 8, (0.9, 0.9, 0.95), 4)
    V.box(c, 1160, 620, 760, 30, (0.85, 0.9, 0.95), 6)
    for i in range(3):
        diya(c, 1260 + i * 120, 610, t, 0.8)
    for i in range(2):
        diya(c, 760 + i * 120, 760, t, 0.9)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_check(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "DHANTERAS: FRI 6 NOV", 540, 960, 48, YEL, stroke=None)
    K.rows(c, t, st, [("GOLD PRICE", WHITE, 70, 2.0)], y0=1110)
    K.stamp(c, t, st + 3.6, "IT FELL?!", 540, 1280, RED, 56)


PTS = [0.3, 0.55, 0.92, 0.7, 0.6, 0.66, 0.5, 0.56, 0.48, 0.42, 0.35]


def o_peak(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "24K GOLD IN INDIA, 2026", 540, 380, 62, WHITE, lw=8)
    T(c, "(simplified chart, per 10 g)", 540, 440, 32, GREY, lw=5)
    x, y, w, h = 160, 560, 760, 560
    TR.line(c, t, st + 0.3, x, y, w, h, PTS, GOLD, dur=3.2, lw=10)
    px, py = x + w * 2 / 10, y + h * (1 - PTS[2])
    TR.marker(c, t, st + 0.3 + 3.2 * 0.2, px, py, "₹1.79 L", YEL, 50)
    if t > st + 1.2:
        T(c, "29 Jan", px + 40, py + 20, 34, GREY, k(t, st + 1.2, st + 1.5), lw=5, anchor="left")
    ex, ey = x + w, y + h * (1 - PTS[-1])
    TR.marker(c, t, st + 3.6, ex, ey, "", RED)
    if t > st + 3.6:
        T(c, "₹1.42 L", ex - 10, ey + 70, 50, RED, k(t, st + 3.6, st + 3.9), lw=8, anchor="right")
        T(c, "30 Oct", ex - 10, ey + 120, 34, GREY, k(t, st + 3.6, st + 3.9), lw=5, anchor="right")


def o_drop(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "-20%", 540, 560, 200, RED, k(t, st + 0.3, st + 0.6), lw=16)
    T(c, "from the January peak", 540, 680, 52, GREY, k(t, st + 0.6, st + 0.9), lw=6)
    K.hbar(c, t, st + 2.4, 140, 900, 800, 80, 0.5, YEL, "October only", "-5%")


def o_why(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "WHY?", 540, 400, 110, YEL, k(t, st + 0.2, st + 0.5), lw=12)
    K.rows(c, t, st, [("US inflation: HOT", WHITE, 64, 0.9), (">", GREY, 60, 1.6), ("US rates stay HIGH", RED, 64, 2.2),
                      (">", GREY, 60, 3.0), ("gold cools", GOLD, 70, 3.6)], y0=560, gap=110)


def o_rates(c, t, lt):
    st = sh.s(5)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("FD / BONDS: pay interest", GRN, 50, 0.5), ("GOLD: pays ₹0 interest", GOLD, 50, 1.6)], y0=980, gap=105)
    K.stamp(c, t, st + 3.4, "HIGH RATES = GOLD LESS SHINY", 540, 1290, BLUE, 34, 0.02)


def o_cost(c, t, lt):
    st = sh.s(6)
    K.panel(c, 870, 500)
    T(c, "YOUR JEWELLERY BILL", 540, 950, 46, GREY, stroke=None)
    K.rows(c, t, st, [("Gold value", WHITE, 52, 0.4), ("+ MAKING charges", RED, 54, 1.4), ("+ 3% GST", RED, 54, 2.2)],
           y0=1050, gap=95)
    K.stamp(c, t, st + 3.6, "NOT INVESTMENT", 540, 1330, RED, 40, -0.03)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Check HUID (BIS Care app)", WHITE, 42, 0.8, "left", 140),
                      ("2. Jewellery = to WEAR", GRN, 42, 2.2, "left", 140),
                      ("3. Saving? Plan, not one day", WHITE, 42, 3.6, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "BUY GOLD WITH A PLAN,", "NOT ONE DAY'S PRICE")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO BUYS GOLD ONLY ON DHANTERAS", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    gw = lambda **kw: (lambda c, t, lt: shop(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), gw(mouth='o', eyes=1.25, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_check, 'warm'),
        (s(2), s(3), sw(), (1.78, 960, 540), (1.85, 960, 520), o_peak, 'studio'),
        (s(3), s(4), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_drop, 'red'),
        (s(4), s(5), sw(), (1.78, 960, 540), (1.85, 960, 520), o_why, 'studio'),
        (s(5), s(6), gw(mouth='flat', squint=0.3, arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 470), o_rates, 'warm'),
        (s(6), s(7), gw(mouth='frown', **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_cost, 'warm'),
        (s(7), s(8), gw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, gw(mouth='bigsmile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
