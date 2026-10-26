import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import envx as X  # noqa: E402
import body as B  # noqa: E402
import env as V  # noqa: E402
import props as P  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s07_gym"
CAPS = [
    "Sid joined a gym. ₹2,000 a month. Or ₹10,000 for a YEAR. Yearly felt smart.",
    "3 weeks later, Sid stopped going. And the gym doesn't mind.",
    "Because a gym's business runs on you NOT showing up.",
    "One branch of a big US gym chain had about 6,500 MEMBERS. Space inside? Only 300 PEOPLE.",
    "If everyone came on the same day, there'd be no room to stand. But they know you won't.",
    "That's why the yearly deal looks so cheap. They're selling your JANUARY motivation.",
    "Next time, take ONE month first. Go regularly for 4 weeks, THEN buy the year.",
    "Send this to the friend whose gym card is in his wallet... and he's at home.",
]
HOOK = [("YOUR GYM WANTS", WHITE), ("YOU TO", WHITE), ("NOT COME", RED)]
SRC = "Source: NPR Planet Money (2014)"
sh = None


def w_reception(c, t, lt):
    X.reception(c, t)
    B.figure(c, 760, 330, 0.55, t, pose='stand', mouth='smile', look=(0.8, -0.1), blush=0.3)


def w_home(c, t, lt):
    V.room(c, t, 'night')
    B.figure(c, 1000, 330, 0.5, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1, mouth='flat', eyes=0.7)
    S.rrect(c, 1450, 700, 220, 120, 30); c.set_source_rgb(0.15, 0.15, 0.18); c.fill()
    T(c, "GYM", 1560, 775, 40, (1, 0.3, 0.4), stroke=None)


def o_week(c, t, lt):
    S.rrect(c, 140, 930, 800, 200, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9 * k(t, sh.s(2) + 0.3, sh.s(2) + 0.6)); c.fill()
    T(c, "WEEK 3: 0 VISITS", 540, 1055, 76, RED, k(t, sh.s(2) + 0.3, sh.s(2) + 0.6))


def w_owner(c, t, lt):
    X.reception(c, t)
    B.figure(c, 1000, 300, 0.55, t, who='bhai', pose='stand', mouth='bigsmile', arms=((70, 120), (70, 120)), glasses=False)
    for i in range(10):
        ph = (t * 0.6 + i / 10) % 1
        P.coin(c, 780 + (i * 61) % 450, 100 + ph * 600, 22, 1 - ph)


def o_biz(c, t, lt):
    S.rrect(c, 80, 900, 920, 260, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    T(c, "THEIR PROFIT =", 540, 1000, 64, WHITE, k(t, sh.s(3) + 0.8, sh.s(3) + 1.1))
    T(c, "YOUR ABSENCE", 540, 1100, 84, YEL, k(t, sh.s(3) + 1.6, sh.s(3) + 1.9))


def w_empty(c, t, lt):
    X.gym(c, t, crowd=0)
    B.figure(c, 960, 350, 0.5, t, who='friend', pose='stand', mouth='flat')


def o_numbers(c, t, lt):
    U.dim(c, 0.55)
    v = int(6500 * k(t, sh.s(4) + 2.5, sh.s(4) + 4.0))
    T(c, f"{v:,}", 540, 520, 200, YEL, lw=20)
    T(c, "MEMBERS", 540, 620, 64, WHITE)
    if t > sh.s(4) + 5.2:
        T(c, "300", 540, 900, 200, RED, k(t, sh.s(4) + 5.2, sh.s(4) + 5.5), lw=20)
        T(c, "CAN FIT INSIDE", 540, 1000, 60, WHITE, k(t, sh.s(4) + 5.4, sh.s(4) + 5.7))


def w_crowd(c, t, lt):
    X.gym(c, t, crowd=2 + 22 * k(t, sh.s(5), sh.s(5) + 2.5))


def o_crowd(c, t, lt):
    if t > sh.s(5) + 3.6:
        S.rrect(c, 120, 300, 840, 170, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
        T(c, "They KNOW you won't come.", 540, 405, 52, YEL)


def w_jan(c, t, lt):
    V.room(c, t, 'day')
    hype = 1 - k(t, sh.s(6) + 2.5, sh.s(6) + 5.5)
    B.figure(c, 760, 330, 0.55, t, pose='stand', mouth='bigsmile' if hype > 0.5 else 'frown',
             arms=((70, 120), (70, 120)) if hype > 0.5 else ((14, -10), (14, -10)), sad=0 if hype > 0.5 else 0.7)


def o_jan(c, t, lt):
    c.save(); c.translate(540, 470)
    S.rrect(c, -230, -250, 460, 500, 30); c.set_source_rgb(0.97, 0.97, 0.98); c.fill()
    S.rrect(c, -230, -250, 460, 120, 30); c.set_source_rgb(*RED); c.fill()
    T(c, "JANUARY", 0, -170, 60, WHITE, stroke=None)
    hype = 1 - k(t, sh.s(6) + 2.5, sh.s(6) + 5.5)
    fl = 120 * (0.2 + hype)
    c.move_to(0, 160); c.curve_to(-fl, 80, -fl * 0.5, -40, 0, -60 - fl * 0.3); c.curve_to(fl * 0.5, -40, fl, 80, 0, 160)
    c.set_source_rgb(1, 0.55, 0.1); c.fill()
    c.restore()
    T(c, "MOTIVATION FOR SALE", 540, 860, 66, YEL, k(t, sh.s(6) + 3.5, sh.s(6) + 3.8))


def w_rule(c, t, lt):
    X.gym(c, t, crowd=3)
    B.figure(c, 900, 330, 0.55, t, pose='walk', ph=t * 0.9, mouth='smile')


def o_rule(c, t, lt):
    S.rrect(c, 90, 820, 900, 560, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
    T(c, "1 MONTH FIRST", 540, 920, 70, YEL, stroke=None)
    for i in range(4):
        a = k(t, sh.s(7) + 2.5 + i * 0.6, sh.s(7) + 2.7 + i * 0.6)
        T(c, f"Week {i + 1}", 330, 1030 + i * 85, 50, WHITE, stroke=None, anchor="left")
        if a > 0:
            T(c, "DONE", 750, 1030 + i * 85, 50, GRN, a, stroke=None)
    T(c, "THEN buy the year", 540, 1350, 44, (0.8, 0.82, 0.9), k(t, sh.s(7) + 5.0, sh.s(7) + 5.3), stroke=None)


def w_end(c, t, lt):
    V.room(c, t, 'night')
    B.figure(c, 1000, 330, 0.5, t, pose='sit', mouth='smirk', arms=((14, -10), (100, 40)))


def o_end(c, t, lt):
    S.rrect(c, 140, 300, 800, 230, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    T(c, "SEND TO THAT", 540, 400, 64, WHITE, stroke=None)
    T(c, "FRIEND", 540, 485, 76, YEL, stroke=None)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    sh.shots = [
        (0, s(2), w_reception, (1.9, 900, 420), (2.1, 1100, 400), None, 'warm'),
        (s(2), s(3), w_home, (1.9, 1100, 500), (2.2, 1050, 450), o_week, 'night'),
        (s(3), s(4), w_owner, (1.8, 1000, 520), (2.0, 1000, 480), o_biz, 'warm'),
        (s(4), s(5), w_empty, (1.78, 960, 540), (1.9, 960, 520), o_numbers, 'night'),
        (s(5), s(6), w_crowd, (1.78, 700, 560), (1.78, 1250, 560), o_crowd, 'red'),
        (s(6), s(7), w_jan, (1.9, 760, 520), (2.0, 760, 480), o_jan, 'morning'),
        (s(7), s(8), w_rule, (1.85, 900, 520), (1.85, 950, 520), o_rule, 'night'),
        (s(8), sh.dur + 1, w_end, (1.9, 1000, 480), (2.1, 1000, 440), o_end, 'night'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview([1, 4, 8.5, 12, 17, 21, 25, 28.5, 32, 35, 38, 42, 45], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
