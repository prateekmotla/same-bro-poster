import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s23_airport"
CAPS = [
    "Sid at the airport. One chai: ₹250. Outside the airport? ₹20.",
    "Same chai. Same paper cup. So why does it cost SO much more?",
    "Hidden reason 1: outlets pay the airport HIGH rent and fees. That cost goes into your chai.",
    "Hidden reason 2: after security, you can't step out. No competition = they can charge anything.",
    "A LocalCircles survey of flyers: about HALF said they paid 2x to 3x the city price.",
    "Since Dec 2024, some airports have an UDAN Yatri Cafe: water at ₹10, cheap chai and samosa.",
    "Rule: EMPTY bottle, refill after security. Pack snacks. Find the UDAN Yatri Cafe.",
    "Send this to the friend who paid ₹300 for one airport coffee.",
]
HOOK = [("WHY AIRPORT CHAI", WHITE), ("COSTS ₹250", RED), ("THE HIDDEN REASON", YEL)]
SRC = "Source: LocalCircles (Dec 2024); IANS on UDAN Yatri Cafe"
sh = None


def airport(c, t):
    box, lingrad = V.box, V.lingrad
    c.set_source(lingrad(c, 0, 0, 0, 780, [(0, (0.78, 0.84, 0.9)), (1, (0.9, 0.92, 0.94))])); c.rectangle(0, 0, 1920, 780); c.fill()
    # big glass wall with runway
    box(c, 80, 90, 1760, 520, (0.45, 0.68, 0.9), 0, (0.3, 0.32, 0.36), 10)
    box(c, 80, 470, 1760, 140, (0.5, 0.52, 0.55))
    for i in range(9):
        box(c, 80 + i * 220, 90, 10, 520, (0.3, 0.32, 0.36))
    # plane silhouette taxiing
    px = 300 + (t * 40) % 1600
    c.save(); c.translate(px, 430)
    c.set_source_rgb(0.95, 0.95, 0.97)
    S.rrect(c, -220, -30, 440, 60, 30); c.fill()
    c.move_to(-40, 0); c.line_to(60, 0); c.line_to(-60, 110); c.line_to(-110, 110); c.close_path(); c.fill()
    c.move_to(-180, -20); c.line_to(-150, -20); c.line_to(-200, -110); c.line_to(-230, -110); c.close_path(); c.fill()
    c.restore()
    # gate sign
    box(c, 1460, 40, 340, 90, (0.12, 0.14, 0.2), 14)
    T(c, "GATE 12", 1630, 102, 48, YEL, stroke=None)
    # cafe counter
    box(c, 0, 780, 1920, 300, (0.62, 0.62, 0.64))
    box(c, 120, 600, 560, 200, (0.35, 0.22, 0.14), 10)
    box(c, 120, 560, 560, 50, (0.2, 0.12, 0.08), 10)
    T(c, "CAFE", 400, 598, 40, WHITE, stroke=None)
    V.light(c, 960, 0, 1100, (1, 1, 1), 0.1)


def scene(c, t, lt, **kw):
    airport(c, t)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def cup(c, x, y, s, a=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.move_to(-60, -80); c.line_to(60, -80); c.line_to(45, 80); c.line_to(-45, 80); c.close_path()
    c.set_source_rgba(0.96, 0.94, 0.9, a); c.fill()
    c.rectangle(-58, -30, 116, 40); c.set_source_rgba(0.75, 0.45, 0.25, a); c.fill()
    for i in range(3):
        c.move_to(-25 + i * 25, -100); c.curve_to(-40 + i * 25, -130, -10 + i * 25, -150, -25 + i * 25, -180)
        c.set_source_rgba(1, 1, 1, 0.5 * a); c.set_line_width(6); c.stroke()
    c.restore()


def o_price(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480, a=0.85)
    cup(c, 300, 1080, 1.1, k(t, st + 0.5, st + 0.8))
    cup(c, 780, 1080, 1.1, k(t, st + 2.0, st + 2.3))
    T(c, "AIRPORT", 300, 1260, 44, GREY, k(t, st + 0.5, st + 0.8), stroke=None)
    T(c, "₹250", 300, 1330, 70, RED, k(t, st + 0.8, st + 1.1), stroke=None)
    T(c, "OUTSIDE", 780, 1260, 44, GREY, k(t, st + 2.0, st + 2.3), stroke=None)
    T(c, "₹20", 780, 1330, 70, GRN, k(t, st + 2.3, st + 2.6), stroke=None)


def o_why(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.86)
    cup(c, 540, 700, 2.0, k(t, st + 0.3, st + 0.6))
    T(c, "SAME CHAI", 540, 360, 90, WHITE, k(t, st + 0.3, st + 0.6), lw=10)
    T(c, "WHY ₹250?", 540, 1050, 110, RED, k(t, st + 2.0, st + 2.3), lw=12)


def o_rent(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "REASON 1", 540, 380, 60, GREY, lw=8)
    T(c, "HIGH RENT + FEES", 540, 500, 86, YEL, k(t, st + 0.8, st + 1.1), lw=12)
    # flow: outlet -> airport, then -> your cup
    T(c, "CAFE", 280, 720, 64, WHITE, k(t, st + 1.4, st + 1.7), lw=8)
    T(c, "AIRPORT", 800, 720, 64, BLUE, k(t, st + 1.4, st + 1.7), lw=8)
    if t > st + 1.8:
        f = (t - st - 1.8) % 1.2 / 1.2
        T(c, "₹", 420 + 230 * f, 720, 60, GRN, 1 - f, lw=6)
    if t > st + 3.6:
        cup(c, 540, 1040, 1.2, k(t, st + 3.6, st + 3.9))
        T(c, "...added to YOUR chai", 540, 1250, 52, RED, k(t, st + 4.0, st + 4.3), lw=8)


def o_lock(c, t, lt):
    st = sh.s(4)
    K.panel(c, 870, 500)
    T(c, "REASON 2", 540, 950, 50, GREY, stroke=None)
    K.rows(c, t, st, [("After security:", WHITE, 50, 0.8), ("you CAN'T step out", YEL, 56, 1.4),
                      ("NO COMPETITION", RED, 62, 3.0)], y0=1060, gap=105)


def o_survey(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "LOCALCIRCLES SURVEY", 540, 400, 64, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    T(c, "airline passengers, Dec 2024", 540, 470, 40, GREY, k(t, st + 0.3, st + 0.6), lw=6)
    K.hbar(c, t, st + 1.4, 140, 660, 800, 80, 0.20, GREY, "up to 2x", "50%")
    K.hbar(c, t, st + 2.4, 140, 870, 800, 80, 0.50, RED, "2x to 3x city price", "~48%")
    if t > st + 4.2:
        T(c, "HALF of flyers", 540, 1110, 90, YEL, k(t, st + 4.2, st + 4.5), lw=12)


def o_udan(c, t, lt):
    st = sh.s(6)
    K.panel(c, 870, 500)
    T(c, "UDAN YATRI CAFE", 540, 960, 62, GRN, stroke=None)
    K.rows(c, t, st, [("since Dec 2024 · some airports", GREY, 40, 0.6), ("WATER ₹10", WHITE, 58, 2.0),
                      ("cheap chai + samosa", YEL, 50, 3.2)], y0=1050, gap=100)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "NEXT FLIGHT", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Carry an EMPTY bottle", WHITE, 46, 0.8, "left", 160),
                      ("2. Refill after security", GRN, 46, 1.8, "left", 160),
                      ("3. Pack snacks / find UDAN", WHITE, 46, 2.9, "left", 160)], y0=1070, gap=100)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO PAID ₹300 FOR COFFEE", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), lambda c, t, lt: scene(c, t, lt, mouth='o' if t > s(1) + 1.0 else 'smile', eyes=1.25 if t > s(1) + 1.0 else 1),
         (1.9, 1000, 480), (2.1, 1000, 450), o_price, 'day'),
        (s(2), s(3), aw(mouth='frown'), (1.78, 960, 540), (1.85, 960, 520), o_why, 'day'),
        (s(3), s(4), sw(), (1.78, 960, 540), (1.85, 960, 520), o_rent, 'studio'),
        (s(4), s(5), aw(mouth='flat', squint=0.4), (1.9, 1000, 500), (2.0, 1000, 470), o_lock, 'day'),
        (s(5), s(6), sw(), (1.78, 960, 540), (1.85, 960, 520), o_survey, 'studio'),
        (s(6), s(7), aw(mouth='bigsmile'), (1.9, 1000, 500), (2.0, 1000, 470), o_udan, 'warm'),
        (s(7), s(8), aw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
        (s(8), sh.dur + 1, aw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
