"""RULES YOU DIDN'T KNOW #3: flight delayed, what the airline MUST give you (DGCA CAR Sec 3 Series M Part IV)."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s71_flight"
CAPS = [
    "Flight 2 hours late, and the airline says 'just wait'. STOP. The rule says they MUST feed you.",
    "DGCA rule: flight up to 2.5 hrs, delayed 2+ hrs? The airline MUST give meals and refreshments.",
    "Longer flights: same rule at 3 or 4 hours of delay.",
    "Delayed more than 6 hours? The airline must offer another flight or a FULL refund.",
    "Night flight (8 PM-3 AM) delayed 6+ hrs, or any flight 24+ hrs late? A hotel too.",
    "Airline refuses? Complain on AirSewa.",
    "Same bro? Sat hungry through a late flight? Comment: did you ever get food?",
]
HOOK = [("FLIGHT 2 HRS LATE?", WHITE), ("FOOD = YOUR RIGHT", YEL), ("RULES YOU DIDN'T KNOW #3", GREY)]
SRC = "SRC: DGCA CAR Section 3, Series M, Part IV"
sh = None


def airport(c, t):
    g = cairo.LinearGradient(0, 0, 0, 1080)
    g.add_color_stop_rgb(0, 0.82, 0.84, 0.88); g.add_color_stop_rgb(1, 0.62, 0.64, 0.68)
    c.rectangle(0, 0, 1920, 1080); c.set_source(g); c.fill()
    # big window + plane
    sk = cairo.LinearGradient(0, 120, 0, 700)
    sk.add_color_stop_rgb(0, 0.35, 0.55, 0.85); sk.add_color_stop_rgb(1, 0.85, 0.75, 0.6)
    c.rectangle(120, 120, 1680, 560); c.set_source(sk); c.fill()
    c.rectangle(120, 600, 1680, 80); c.set_source_rgb(0.4, 0.42, 0.45); c.fill()
    px = 1300 + math.sin(t * 0.2) * 10
    c.save(); c.translate(px, 520)
    c.move_to(-420, 0); c.curve_to(-420, -60, -380, -70, -300, -70); c.line_to(300, -70); c.curve_to(380, -70, 420, -40, 440, 0)
    c.curve_to(420, 30, 380, 40, 300, 40); c.line_to(-380, 40); c.close_path(); c.set_source_rgb(0.95, 0.96, 0.98); c.fill()
    c.move_to(-360, -70); c.line_to(-420, -220); c.line_to(-330, -220); c.line_to(-250, -70); c.close_path()
    c.set_source_rgb(0.2, 0.35, 0.7); c.fill()
    c.move_to(-80, 10); c.line_to(120, 10); c.line_to(-40, 120); c.line_to(-140, 120); c.close_path(); c.set_source_rgb(0.8, 0.82, 0.86); c.fill()
    for j in range(10):
        c.arc(-200 + j * 50, -30, 9, 0, 6.283); c.set_source_rgb(0.25, 0.3, 0.4); c.fill()
    c.restore()
    for x in range(120, 1801, 280):
        c.rectangle(x - 8, 120, 16, 560); c.set_source_rgb(0.3, 0.32, 0.36); c.fill()
    # departure board
    S.rrect(c, 790, 95, 420, 150, 12); c.set_source_rgb(0.05, 0.06, 0.08); c.fill()
    T(c, "DEL > BOM  18:40", 1000, 150, 36, (1, 0.85, 0.3), stroke=None)
    if int(t * 2) % 2:
        T(c, "DELAYED", 1000, 222, 44, (1, 0.25, 0.2), stroke=None)
    # floor + seats
    c.rectangle(0, 760, 1920, 320); c.set_source_rgb(0.45, 0.43, 0.42); c.fill()
    for x in range(120, 1800, 150):
        if 860 < x < 1160:
            continue
        S.rrect(c, x, 820, 120, 80, 14); c.set_source_rgb(0.18, 0.3, 0.5); c.fill()
        S.rrect(c, x, 760, 120, 70, 14); c.set_source_rgb(0.22, 0.36, 0.58); c.fill()


def ap(**kw):
    def f(c, t, lt):
        airport(c, t)
        d = dict(pose='stand', mouth='flat')
        d.update(kw)
        K.sid(c, t, 1000, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def o_hook(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 330)
    T(c, "WAIT HUNGRY?", 540, 980, 60, WHITE, k(t, st + 0.3, st + 0.6), stroke=None)
    T(c, "OR ASK FOR MEALS?", 540, 1070, 60, YEL, k(t, st + 1.0, st + 1.3), stroke=None)
    K.stamp(c, t, st + 4.6, "MEALS = YOUR RIGHT", 540, 1300, GRN, 52, -0.04)


def table(c, t, st, rows_at):
    K.panel(c, 430, 640, 50, 980)
    T(c, "FLIGHT LENGTH", 110, 520, 34, GREY, stroke=None, anchor="left")
    T(c, "DELAY", 590, 520, 34, GREY, stroke=None, anchor="left")
    T(c, "YOU GET", 960, 520, 34, GREY, stroke=None, anchor="right")
    rows = [("Up to 2.5 hrs", "2+ hrs"), ("2.5 to 5 hrs", "3+ hrs"), ("Over 5 hrs", "4+ hrs")]
    for j, (a_, b_) in enumerate(rows):
        a = k(t, rows_at[j], rows_at[j] + 0.3)
        if a <= 0:
            continue
        y = 610 + j * 150
        S.rrect(c, 80, y - 10, 920, 120, 20); c.set_source_rgba(0.15, 0.17, 0.25, a); c.fill()
        T(c, a_, 110, y + 66, 46, WHITE, a, stroke=None, anchor="left")
        T(c, b_, 590, y + 66, 46, YEL, a, stroke=None, anchor="left")
        T(c, "MEALS", 960, y + 66, 46, GRN, a, stroke=None, anchor="right")


def o_rule(c, t, lt):
    st = sh.s(2)
    table(c, t, st, [st + 1.0, 1e9, 1e9])


def o_rule2(c, t, lt):
    st = sh.s(3)
    table(c, t, st, [0, st + 0.6, st + 2.2])


def o_six(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("DELAYED 6+ HRS?", WHITE, 76, 0.1), ("ANOTHER FLIGHT", YEL, 80, 1.6), ("OR FULL REFUND", GRN, 90, 2.6)],
           y0=560, gap=180)


def o_hotel(c, t, lt):
    st = sh.s(5)
    K.panel(c, 470, 600, 50, 980)
    T(c, "HOTEL TOO, IF:", 540, 570, 66, YEL, k(t, st, st + 0.3), stroke=None)
    K.rows(c, t, st, [("Night flight (8 PM-3 AM)", WHITE, 50, 0.3), ("delayed 6+ hrs", YEL, 56, 1.4),
                      ("OR", GREY, 44, 3.2), ("Any flight 24+ hrs late", WHITE, 50, 3.6)], y0=680, gap=100)


def o_sewa(c, t, lt):
    st = sh.s(6)
    K.full(c, t, st, [("AIRLINE SAYS NO?", WHITE, 74, 0.1), ("COMPLAIN ON", WHITE, 60, 0.9), ("AirSewa", GRN, 120, 1.2)],
           y0=560, gap=180)


def o_end(c, t, lt):
    K.end_card(c, "DID YOU EVER GET FOOD?", "COMMENT YES or NO", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    sh.shots = [
        (0, s(2), ap(mouth='frown', angry=0.4, arms=((60, 120), (60, 120))), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_rule, 'studio'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_rule2, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_six, 'money'),
        (s(5), s(6), ap(mouth='smile'), (1.9, 1000, 500), (2.0, 1000, 470), o_hotel, 'warm'),
        (s(6), s(7), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_sewa, 'money'),
        (s(7), sh.dur + 1, ap(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.5, 4.0, 6.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
