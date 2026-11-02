import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
import fest as F  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s50_making"
GOLD = F.GOLD
CAPS = [
    "Guess: you buy gold jewellery for ₹1 lakh. How much is GONE the moment you leave the shop?",
    "This Diwali, Sid's family buys a chain. 'Gold hai, investment hai, value badhegi!'",
    "But the bill has MAKING CHARGES: usually 10 to 25% of the price. Plus GST.",
    "Sell or exchange it later? The jeweller pays only for the gold weight. Making charges back: ₹0.",
    "So gold has to rise a LOT just to get you back to zero.",
    "Same bro? 'Jewellery = investment'?",
    "Rule: buy jewellery to WEAR. To invest in gold, look at regulated options with no making charges, like gold ETFs or gold funds.",
    "MORAL: Jewellery is for wearing, not investing.",
    "Send this to the friend who calls every chain an 'investment'.",
]
HOOK = [("GOLD JEWELLERY", WHITE), ("= INVESTMENT?", GOLD), ("10-25% GONE", RED)]
SRC = "Source: Angel One; Shriram Finance (2026)"
sh = None


def scene(c, t, lt, **kw):
    F.room(c, t, lt, **kw)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def chain(c, x, y, r, a=1.0):
    for i in range(22):
        ang = math.pi * 0.1 + i * math.pi * 0.8 / 21
        cx, cy = x + r * math.cos(ang), y + r * 0.8 * math.sin(ang)
        c.save(); c.translate(cx, cy); c.rotate(ang); c.scale(1, 0.6)
        c.arc(0, 0, 14, 0, 2 * math.pi); c.restore()
        c.set_source_rgba(*GOLD, a); c.set_line_width(6); c.stroke()


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    chain(c, 540, 930, 220, k(t, st + 0.2, st + 0.5))
    T(c, "₹1,00,000", 540, 1170, 90, WHITE, k(t, st + 0.8, st + 1.1), stroke=None)
    K.stamp(c, t, st + 2.6, "HOW MUCH GONE?", 540, 1290, RED, 54, -0.05)


def o_family(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    chain(c, 540, 930, 200, k(t, st + 0.2, st + 0.5))
    K.stamp(c, t, st + 2.0, "'INVESTMENT HAI!'", 540, 1210, GRN, 56, -0.05)


def o_bill(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 170, 360, 740, 620, 24); c.set_source_rgba(0.97, 0.96, 0.92, k(t, st + 0.1, st + 0.4)); c.fill()
    dark = (0.1, 0.1, 0.12)
    T(c, "JEWELLERY BILL", 540, 440, 52, dark, k(t, st + 0.1, st + 0.4), stroke=None)
    rows = [("Gold value", "₹XX,XXX", dark, 0.5), ("MAKING CHARGES", "10-25%", RED, 1.0), ("GST", "+3%", dark, 3.2)]
    for i, (a_, b_, col, dt) in enumerate(rows):
        a = k(t, st + dt, st + dt + 0.3)
        T(c, a_, 220, 560 + i * 120, 46, col, a, stroke=None, anchor="left")
        T(c, b_, 860, 560 + i * 120, 50, col, a, stroke=None, anchor="right")


def o_resale(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "SELL / EXCHANGE LATER", 540, 400, 64, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "paid for: gold WEIGHT only", 540, 520, 52, YEL, k(t, st + 1.6, st + 1.9), lw=7)
    T(c, "MAKING CHARGES BACK", 540, 700, 60, GREY, k(t, st + 3.2, st + 3.5), lw=8)
    T(c, "₹0", 540, 900, 200, RED, k(t, st + 3.6, st + 3.9), lw=16)


def o_zero(c, t, lt):
    st = sh.s(5)
    K.panel(c, 820, 560)
    T(c, "GOLD MUST RISE A LOT", 540, 920, 56, WHITE, k(t, st + 0.2, st + 0.5), stroke=None)
    TR.line(c, t, st + 0.6, 160, 980, 760, 300, [0.0, 0.1, 0.25, 0.4, 0.6, 0.8], col=GOLD, dur=1.8)
    if t > st + 2.2:
        T(c, "...just to get back to ZERO", 540, 1330, 46, YEL, k(t, st + 2.2, st + 2.5), stroke=None)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("JEWELLERY", GOLD, 70, 0.2), ("= INVESTMENT?", WHITE, 64, 0.8)], y0=1000, gap=115)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Jewellery = to WEAR", GOLD, 44, 0.5, "left", 140),
                      ("2. Investing in gold? Regulated", WHITE, 40, 2.4, "left", 140),
                      ("    options, NO making charges", WHITE, 40, 2.4, "left", 140),
                      ("    (gold ETFs / gold funds)", GRN, 40, 5.0, "left", 140)], y0=1060, gap=82)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "JEWELLERY IS FOR", "WEARING, NOT INVESTING", GOLD)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "'EVERY CHAIN = INVESTMENT'", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'warm'
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), rw(mouth='o', eyes=1.2), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'warm'),
        (s(2), s(3), rw(mouth='bigsmile', arms=((60, 120), (14, -10))), (2.0, 1000, 470), (2.15, 1000, 450), o_family, 'warm'),
        (s(3), s(4), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_bill, 'studio'),
        (s(4), s(5), sw(mouth='frown', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_resale, 'red'),
        (s(5), s(6), rw(mouth='frown'), (1.9, 1000, 480), (2.0, 1000, 460), o_zero, 'warm'),
        (s(6), s(7), rw(mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), rw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
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
