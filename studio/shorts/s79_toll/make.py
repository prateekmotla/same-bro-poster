"""RULES YOU DIDN'T KNOW #5: the viral '100 m queue = free toll' rule is gone.
Sources: NHAI guidelines May 2021 (max 10 s service time; queue beyond 100 m yellow line > barrier lifted);
NHAI circular 19 Aug 2024 deleted the provision (Business Standard, 22 Aug 2024): National Highways Fee Rules 2008
have no exemption / free-flow provision; the rule applied only to new-design plazas after 2021. NHAI helpline 1033."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s79_toll"
CAPS = [
    "100 m long queue at the toll, so you drive through free? That viral rule doesn't work anymore.",
    "In 2021, NHAI issued guidelines: 10 seconds per vehicle, and if the queue crosses the 100 m yellow line, open the barrier.",
    "But in August 2024, NHAI deleted that provision.",
    "Why? The National Highways fee rules have no such free-pass exemption. And the rule was only for new-design plazas.",
    "So even with a long queue, you still pay the toll. Problem at a toll plaza? Call the NHAI helpline, 1033.",
    "Same bro? Did you forward that message too? Comment.",
]
HOOK = [("100 M QUEUE = FREE?", WHITE), ("NOT ANYMORE", RED), ("RULES YOU DIDN'T KNOW #5", GREY)]
SRC = "SRC: NHAI circular, 19 Aug 2024"
sh = None
CARS = [(0.9, 0.3, 0.25), (0.25, 0.5, 0.9), (0.95, 0.95, 0.95), (0.2, 0.2, 0.22), (0.95, 0.7, 0.2), (0.4, 0.7, 0.4)]


def plaza(c, t):
    g = cairo.LinearGradient(0, 0, 0, 600)
    g.add_color_stop_rgb(0, 0.55, 0.75, 0.95); g.add_color_stop_rgb(1, 0.9, 0.88, 0.8)
    c.rectangle(0, 0, 1920, 1080); c.set_source(g); c.fill()
    c.rectangle(0, 560, 1920, 520); c.set_source_rgb(0.3, 0.3, 0.32); c.fill()
    # canopy
    c.rectangle(300, 200, 1400, 70); c.set_source_rgb(0.15, 0.35, 0.65); c.fill()
    T(c, "TOLL PLAZA", 1000, 252, 46, WHITE, stroke=None)
    for x in range(380, 1700, 260):
        c.rectangle(x, 270, 40, 330); c.set_source_rgb(0.8, 0.8, 0.82); c.fill()
        S.rrect(c, x - 30, 430, 100, 170, 10); c.set_source_rgb(0.92, 0.92, 0.9); c.fill()
        c.rectangle(x + 70, 520, 140, 12); c.set_source_rgb(0.95, 0.2, 0.2); c.fill()
    # yellow 100 m line
    c.rectangle(0, 1000, 1920, 14); c.set_source_rgb(0.98, 0.82, 0.1); c.fill()
    T(c, "100 M", 1700, 990, 40, (0.98, 0.82, 0.1), stroke=None)
    # queue of cars (rear view)
    for r in range(3):
        for j in range(6):
            x = 450 + j * 260
            y = 640 + r * 130
            col = CARS[(r * 2 + j) % 6]
            S.rrect(c, x, y, 170, 100, 22); c.set_source_rgb(*col); c.fill()
            c.rectangle(x + 20, y + 15, 130, 35); c.set_source_rgb(0.2, 0.25, 0.3); c.fill()
            c.rectangle(x + 10, y + 70, 30, 12); c.set_source_rgb(1, 0.2, 0.2); c.fill()
            c.rectangle(x + 130, y + 70, 30, 12); c.set_source_rgb(1, 0.2, 0.2); c.fill()


def tz(**kw):
    def f(c, t, lt):
        plaza(c, t)
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
    K.panel(c, 900, 380)
    T(c, "FWD: 'Queue > 100 m?", 540, 1000, 52, WHITE, k(t, st + 0.3, st + 0.6), stroke=None)
    T(c, "Don't pay toll!'", 540, 1075, 52, WHITE, k(t, st + 0.3, st + 0.6), stroke=None)
    K.stamp(c, t, st + 3.6, "WITHDRAWN IN 2024", 540, 1200, RED, 56, -0.04)


def o_2021(c, t, lt):
    st = sh.s(2)
    K.panel(c, 820, 560)
    T(c, "NHAI GUIDELINES, 2021", 540, 905, 54, YEL, k(t, st, st + 0.3), stroke=None)
    K.rows(c, t, st, [("Max 10 sec per vehicle", WHITE, 52, 3.0), ("Queue past 100 m line", WHITE, 52, 4.5),
                      ("= barrier opened", GRN, 56, 6.8)], y0=1020, gap=110)


def o_2024(c, t, lt):
    st = sh.s(3)
    K.full(c, t, st, [("AUGUST 2024", WHITE, 84, 0.1), ("PROVISION", RED, 100, 1.2), ("DELETED", RED, 120, 1.5),
                      ("BY NHAI", GREY, 60, 2.4)], y0=520, gap=180)


def o_why(c, t, lt):
    st = sh.s(4)
    K.panel(c, 820, 560)
    T(c, "WHY?", 540, 905, 66, YEL, stroke=None)
    K.rows(c, t, st, [("NH Fee Rules 2008:", GREY, 46, 0.8, "left", 140), ("no free-pass exemption", WHITE, 52, 1.2, "left", 140),
                      ("+ it was only for", GREY, 46, 4.6, "left", 140), ("new-design plazas", WHITE, 52, 5.0, "left", 140)],
           y0=1000, gap=95)


def o_pay(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("LONG QUEUE?", WHITE, 74, 0.1), ("TOLL STILL APPLIES", YEL, 74, 1.0), ("PROBLEM AT PLAZA?", GREY, 54, 2.8),
                      ("NHAI HELPLINE 1033", GRN, 76, 4.0)], y0=520, gap=180)


def o_end(c, t, lt):
    K.end_card(c, "YOU FORWARDED IT TOO?", "COMMENT YES or NO", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    sh.shots = [
        (0, s(2), tz(mouth='smirk', phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_2021, 'studio'),
        (s(3), s(4), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_2024, 'red'),
        (s(4), s(5), tz(mouth='flat'), (1.9, 1000, 480), (2.0, 1000, 460), o_why, 'warm'),
        (s(5), s(6), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_pay, 'money'),
        (s(6), sh.dur + 1, tz(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 480), (2.1, 1000, 450), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.5, 4.5] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
