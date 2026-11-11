"""SAME BRO GAMES #19: which car is faster? 3 logic levels (engine: studio/shorts/illusion.py, question/answer pairs).
L1: A 120 km in 2 h = 60 km/h, B 90 km in 1 h = 90 km/h > B.
L2: A 100 m in 5 s = 20 m/s = 72 km/h, B 1 km in 1 min = 60 km/h > A.
L3: 120 km trip. A at 60 all the way = 2 h. B 60 km at 120 (0.5 h) + 60 km at 40 (1.5 h) = 2 h > TIE (average speed trap).
All maths checked in code below (asserts)."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import illusion as IL  # noqa: E402
from illusion import T, YEL, GRN, WHITE, S  # noqa: E402

assert 120 / 2 == 60 and 90 / 1 == 90
assert abs(100 / 5 * 3.6 - 72) < 1e-9 and 1 / (1 / 60) == 60
assert 120 / 60 == 60 / 120 + 60 / 40 == 2

D = "/home/claude/sid/shorts/c125_carlogic"
CAPS = [
    "Level 1. Car A: 120 km in 2 hours. Car B: 90 km in 1 hour. Which is FASTER? Comment!",
    "B! A does 60, B does 90 km per hour.",
    "Level 2. Car A: 100 metres in 5 seconds. Car B: 1 km in 1 minute. Which is faster?",
    "A! A is 72 km per hour, B only 60.",
    "FINAL level. 120 km. A drives 60 all the way. B does half at 120, the rest at 40. Who arrives FIRST?",
    "TIE! Both take exactly 2 hours. The average speed trap. Your score? Comment, and watch again.",
]
RED_ = (0.95, 0.25, 0.25)
BLU_ = (0.25, 0.55, 1.0)
GREY_ = (0.6, 0.62, 0.7)


def car(c, x, y, col, lab, s=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    S.rrect(c, -150, -40, 300, 80, 26); c.set_source_rgb(*col); c.fill()
    c.move_to(-80, -40); c.line_to(-45, -95); c.line_to(55, -95); c.line_to(95, -40); c.close_path(); c.fill()
    c.move_to(-60, -45); c.line_to(-35, -85); c.line_to(45, -85); c.line_to(75, -45); c.close_path()
    c.set_source_rgba(0.8, 0.92, 1.0, 0.9); c.fill()
    for wx in (-90, 90):
        c.arc(wx, 42, 34, 0, 2 * math.pi); c.set_source_rgb(0.1, 0.1, 0.12); c.fill()
        c.arc(wx, 42, 14, 0, 2 * math.pi); c.set_source_rgb(0.7, 0.7, 0.75); c.fill()
    c.arc(0, -5, 34, 0, 2 * math.pi); c.set_source_rgb(1, 1, 1); c.fill()
    T(c, lab, 0, 12, 46, (0.08, 0.08, 0.1), stroke=None)
    c.restore()


def road(c, y):
    c.rectangle(0, y - 70, 1080, 140); c.set_source_rgb(0.22, 0.23, 0.27); c.fill()
    for j in range(8):
        c.rectangle(30 + j * 140, y - 4, 80, 8); c.set_source_rgba(1, 1, 1, 0.5); c.fill()


def card(c, y, lines, col, a=1.0):
    S.rrect(c, 80, y, 920, 70 * len(lines) + 30, 26); c.set_source_rgba(0.05, 0.06, 0.1, 0.85 * a); c.fill()
    for i, (txt, cc) in enumerate(lines):
        T(c, txt, 540, y + 68 + i * 70, 50, cc or col, a, stroke=None)


def level(a_txt, b_txt, a_res, b_res, win):
    def draw(c, t, r):
        for y, col, lab, txt, res, w in ((620, RED_, "A", a_txt, a_res, win == 'A'), (1180, BLU_, "B", b_txt, b_res, win == 'B')):
            road(c, y)
            drive = (t * 0.25) % 1 if r == 0 else 0.0
            x = 250 + 580 * (r * (1.0 if (w or win == 'T') else 0.62)) + 20 * math.sin(t * 3)
            car(c, x, y - 10, col, lab, 0.8)
            card(c, y + 90, [(t_, WHITE) for t_ in txt], WHITE)
            if r > 0:
                ok = w or win == 'T'
                S.rrect(c, 640, y - 175, 380, 80, 30); c.set_source_rgba(*(GRN if ok else GREY_), 0.95 * r); c.fill()
                T(c, res, 830, y - 120, 46, (0.05, 0.05, 0.08), r, stroke=None)
    return draw


LEVELS = [
    dict(name="LEVEL 1", q="WHICH CAR IS FASTER?", ans="CAR B!", stamp="B WINS",
         draw=level(["120 km in 2 hours"], ["90 km in 1 hour"], "60 km/h", "90 km/h", 'B')),
    dict(name="LEVEL 2", q="WHICH CAR IS FASTER?", ans="CAR A!", stamp="A WINS",
         draw=level(["100 m in 5 seconds"], ["1 km in 1 minute"], "72 km/h", "60 km/h", 'A')),
    dict(name="FINAL LEVEL: 120 km", q="WHO ARRIVES FIRST?", ans="IT'S A TIE!", stamp="BOTH 2 HOURS",
         draw=level(["60 km/h all the way"], ["60 km at 120 km/h", "60 km at 40 km/h"], "2 HOURS", "0.5 + 1.5 = 2 H", 'T')),
]

if __name__ == "__main__":
    g = IL.Illusion(D, CAPS, LEVELS, "SAME BRO GAMES #19", ("WHICH CAR IS FASTER?", "3 LEVELS OF LOGIC"), mood='chill')
    if sys.argv[1] == "preview":
        L = g.L
        g.preview([1.0, 4.0, L[1][0] + 2, L[2][0] + 2, L[3][0] + 2, L[4][0] + 4, L[5][0] + 2.5, g.dur - 0.5], f"{D}/prev.png")
        print("dur", round(g.dur, 1), [round(a, 1) for a, b in L])
    else:
        g.render(f"{D}/short.mp4")
