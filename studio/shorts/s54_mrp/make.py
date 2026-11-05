import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s54_mrp"
CAPS = [
    "Guess: water bottle ₹20 outside, ₹100 at the multiplex counter. Is that even legal?",
    "Sid at the movies, thirsty. Pays ₹100, turns the bottle around... printed MRP: ₹20.",
    "Rule: no shop can sell a packed product above its printed MRP. Not airports. Not malls.",
    "And since 1 Jan 2018, the same packed product can't carry two different MRPs.",
    "So a ₹20-MRP bottle sold at ₹100 = overcharging. (A sit-down restaurant serving you is a different case.)",
    "Same bro? Paid ₹100 and thought 'it's the airport, it's fine'?",
    "Fix: check the MRP before you pay. Overcharged? Ask for a bill, complain to National Consumer Helpline 1915.",
    "MORAL: MRP is the MAXIMUM price. Not a suggestion.",
    "Send this to the friend who buys water at the airport.",
]
HOOK = [("₹20 WATER", WHITE), ("SOLD FOR ₹100?", YEL), ("IS THAT LEGAL?", RED)]
SRC = "Source: Legal Metrology (Packaged Commodities) Rules; no dual MRP since 1 Jan 2018"
sh = None
DK = (0.12, 0.12, 0.14)


def canteen(c, t, lt, **kw):
    V.canteen(c, t)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def metro(c, t, lt, **kw):
    V.metro(c, t)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def bottle(c, x, y, s, a=1.0, label=True, mrp=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.push_group()
    S.rrect(c, -30, -260, 60, 50, 10); c.set_source_rgb(0.15, 0.4, 0.85); c.fill()
    c.move_to(-35, -210); c.line_to(35, -210); c.line_to(90, -120); c.line_to(90, 230)
    c.curve_to(90, 260, 70, 270, 50, 270); c.line_to(-50, 270); c.curve_to(-70, 270, -90, 260, -90, 230)
    c.line_to(-90, -120); c.close_path(); c.set_source_rgba(0.75, 0.88, 1, 0.85); c.fill()
    if label:
        c.rectangle(-90, -40, 180, 160); c.set_source_rgb(0.1, 0.45, 0.8); c.fill()
        T(c, "AQUA", 0, 30, 46, WHITE, stroke=None)
        T(c, "1 LITRE", 0, 90, 30, WHITE, stroke=None)
    c.pop_group_to_source(); c.paint_with_alpha(a)
    c.restore()
    if mrp > 0:
        S.rrect(c, x - 20 * s, y + 140 * s, 260 * s, 110 * s, 14 * s); c.set_source_rgba(1, 1, 1, a * mrp); c.fill()
        T(c, "MRP ₹20", x + 110 * s, y + 215 * s, 54 * s, DK, a * mrp, stroke=None)


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 760, 600, a=0.85)
    T(c, "OUTSIDE", 300, 840, 46, GREY, k(t, st + 0.2, st + 0.5), stroke=None)
    T(c, "MULTIPLEX", 780, 840, 46, GREY, k(t, st + 1.8, st + 2.1), stroke=None)
    bottle(c, 300, 1060, 0.6, k(t, st + 0.2, st + 0.5), mrp=0)
    bottle(c, 780, 1060, 0.6, k(t, st + 1.8, st + 2.1), mrp=0)
    T(c, "₹20", 300, 1300, 70, GRN, k(t, st + 0.8, st + 1.1), stroke=None)
    T(c, "₹100", 780, 1300, 70, RED, k(t, st + 2.4, st + 2.7), stroke=None)


def o_buy(c, t, lt):
    st = sh.s(2)
    K.panel(c, 760, 600, a=0.85)
    T(c, "PAID: ₹100", 540, 840, 56, RED, k(t, st + 0.2, st + 0.5), stroke=None)
    bottle(c, 430, 1060, 0.75, k(t, st + 0.6, st + 0.9), mrp=k(t, st + 3.8, st + 4.2))
    K.stamp(c, t, st + 5.0, "WAIT...", 780, 1000, YEL, 60, -0.08)


def o_rule(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "THE RULE", 540, 430, 64, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    K.rows(c, t, st, [("Packed product?", WHITE, 60, 1.0), ("NEVER above", WHITE, 66, 1.8),
                      ("PRINTED MRP", YEL, 84, 2.6)], y0=600, gap=120)
    K.stamp(c, t, st + 4.6, "AIRPORT / MALL / CINEMA TOO", 540, 1050, RED, 50, -0.03)


def o_dual(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "SINCE 1 JAN 2018", 540, 430, 64, YEL, k(t, st + 0.1, st + 0.4), lw=8)
    T(c, "SAME PACKED PRODUCT", 540, 600, 56, WHITE, k(t, st + 1.6, st + 1.9), lw=8)
    T(c, "= ONE MRP ONLY", 540, 700, 66, GRN, k(t, st + 2.4, st + 2.7), lw=8)
    K.stamp(c, t, st + 3.6, "DUAL MRP BANNED", 540, 900, RED, 60, -0.04)


def o_over(c, t, lt):
    st = sh.s(5)
    K.panel(c, 820, 560)
    K.rows(c, t, st, [("MRP ₹20, charged ₹100", WHITE, 52, 0.3), ("= OVERCHARGING", RED, 66, 1.6),
                      ("(Table-service restaurant", GREY, 38, 3.6), ("= a different case)", GREY, 38, 3.6)], y0=950, gap=100)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("PAID ₹100 AND THOUGHT", WHITE, 54, 0.2), ("'AIRPORT HAI, CHALTA HAI'?", YEL, 50, 1.2)], y0=1000, gap=110)
    K.stamp(c, t, st + 2.2, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(7)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Check MRP before paying", WHITE, 44, 0.3, "left", 130),
                      ("2. Overcharged? Ask for a bill", WHITE, 44, 2.6, "left", 130),
                      ("3. Complain: NCH 1915", GRN, 48, 4.4, "left", 130)], y0=1020, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "MRP = MAXIMUM PRICE.", "NOT A SUGGESTION.", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO BUYS WATER AT AIRPORTS", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    cw = lambda **kw: (lambda c, t, lt: canteen(c, t, lt, **kw))
    mw = lambda **kw: (lambda c, t, lt: metro(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), cw(mouth='o', eyes=1.2), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'warm'),
        (s(2), s(3), cw(mouth='frown', squint=0.3), (1.9, 1000, 480), (2.05, 1000, 455), o_buy, 'warm'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_rule, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_dual, 'studio'),
        (s(5), s(6), mw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 470), o_over, 'night'),
        (s(6), s(7), mw(mouth='frown'), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'night'),
        (s(7), s(8), cw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, mw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'night'),
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
