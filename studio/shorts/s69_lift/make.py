"""BRAVE vs NORMAL — WHO'S RIGHT? #1: stuck in a lift (engine: studio/shorts/dilemma.py)."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, S, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s69_lift"
CAPS = [
    "Lift stuck between floors. Brave: force the doors open. Normal: press the alarm and wait. Whose side are you on?",
    "Brave pulls the doors open by hand. A wall in front, the floor half up. Now he climbs out?",
    "Normal presses the ALARM button, calls the guard on his phone, and waits calmly.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. A stuck lift can start moving anytime. If it moves while you're climbing out, that's the real danger.",
    "Lifts don't free fall. They have safety brakes, and there's enough air. So press the alarm, call, and wait for help.",
    "Being brave is cool. Being smart matters more. What would YOU do first?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #1", question=("STUCK IN A LIFT.", "WHAT DO YOU DO?"),
           brave="FORCE THE DOORS OPEN", normal="PRESS ALARM & WAIT", answer='N', grade='studio',
           why_title="WHY NORMAL WINS",
           why_rows=[("Lift can restart anytime", RED), ("Don't force doors or climb out", WHITE),
                     ("Safety brakes stop free fall", WHITE), ("There's enough air inside", WHITE),
                     ("Press ALARM. Call. Wait.", GRN)],
           src="SRC: Lift safety guidance (Northeastern Univ. Police)", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

STEEL = (0.52, 0.56, 0.62)


def lift(c, t, side, p):
    # back wall (brushed steel, emergency-dim)
    g = cairo.LinearGradient(-400, 0, 1480, 0)
    for j in range(12):
        f = j / 11
        sh = 0.33 + 0.06 * math.sin(j * 1.7)
        g.add_color_stop_rgb(f, sh * 0.95, sh, sh * 1.08)
    c.rectangle(-400, 0, 1880, 1000); c.set_source(g); c.fill()
    for x in range(-400, 1480, 180):
        c.rectangle(x, 0, 4, 900); c.set_source_rgba(0, 0, 0, 0.25); c.fill()
    # ceiling + flickering light strip
    c.rectangle(-400, 0, 1880, 40); c.set_source_rgb(0.15, 0.15, 0.18); c.fill()
    fl = 0.35 + 0.25 * (math.sin(t * 23) > 0.6)
    c.rectangle(-100, 22, 1280, 14); c.set_source_rgba(1, 0.92, 0.7, fl); c.fill()
    # handrail
    c.rectangle(-400, 560, 960, 16); c.set_source_rgb(0.7, 0.72, 0.76); c.fill()
    # floor
    c.rectangle(-400, 880, 1880, 120); c.set_source_rgb(0.18, 0.17, 0.17); c.fill()
    # floor indicator
    S.rrect(c, 790, 60, 120, 54, 10); c.set_source_rgb(0.03, 0.03, 0.03); c.fill()
    T(c, "3" if int(t * 2) % 2 else "--", 850, 101, 38, (1, 0.25, 0.2), stroke=None)
    # button panel
    S.rrect(c, 560, 360, 64, 270, 10); c.set_source_rgb(0.25, 0.26, 0.3); c.fill()
    for j in range(5):
        c.arc(592, 390 + j * 42, 13, 0, 2 * math.pi); c.set_source_rgb(0.75, 0.77, 0.8); c.fill()
    pressed = side == 'N' and p > 0.12
    c.arc(592, 600, 20, 0, 2 * math.pi); c.set_source_rgb(1, 0.85, 0.1) if pressed else c.set_source_rgb(0.85, 0.7, 0.1); c.fill()
    T(c, "!", 592, 612, 28, (0.2, 0.1, 0.0), stroke=None)
    if pressed and p < 0.55:
        for r in range(3):
            rr = 30 + ((t * 80 + r * 25) % 75)
            c.arc(592, 600, rr, -0.9, 0.9); c.set_source_rgba(1, 0.85, 0.1, 1 - (rr - 30) / 75); c.set_line_width(5); c.stroke()
    # doors
    op = 0.0
    if side == 'B':
        op = S.ease(max(0, min(1, (p - 0.12) / 0.55)))
    edge = 850 - 170 * op
    # shaft behind gap
    if op > 0.01:
        c.rectangle(edge, 120, 850 - edge, 760); c.set_source_rgb(0.12, 0.11, 0.1); c.fill()
        c.rectangle(edge, 120, 850 - edge, 250); c.set_source_rgb(0.75, 0.72, 0.65); c.fill()   # landing outside
        c.rectangle(edge, 370, 850 - edge, 90); c.set_source_rgb(0.45, 0.43, 0.4); c.fill()    # floor slab half up
        c.rectangle(edge, 366, 850 - edge, 8); c.set_source_rgb(0.95, 0.75, 0.1); c.fill()
        for yy in range(500, 880, 60):
            c.rectangle(edge, yy, 850 - edge, 3); c.set_source_rgba(0, 0, 0, 0.4); c.fill()
        r = cairo.RadialGradient(765, 420, 10, 765, 420, 260)
        r.add_color_stop_rgba(0, 1, 0.1, 0.05, 0.35 * op); r.add_color_stop_rgba(1, 1, 0.1, 0.05, 0)
        c.set_source(r); c.rectangle(500, 120, 500, 760); c.fill()
    for x0, x1 in ((640, edge), (850, 1060)):
        c.rectangle(x0, 120, x1 - x0, 760); c.set_source_rgb(*STEEL); c.fill()
        c.rectangle(x0, 120, x1 - x0, 760); c.set_source_rgba(0, 0, 0, 0.5); c.set_line_width(4); c.stroke()
    c.rectangle(630, 110, 440, 10); c.set_source_rgb(0.3, 0.3, 0.34); c.fill()
    # people
    if side == 'B':
        x = 666 - 170 * op if p > 0.1 else 470
        if p < 0.1:
            K.sid(c, t, 470, 430, 0.42, mouth='smirk', arms=((14, -10), (14, -10)))
        elif p < 0.72:
            K.sid(c, t, x, 430, 0.42, mouth='frown', angry=0.6, sweat=1, lean=-6, arms=((60, 30), (90, 0)))
        else:
            K.sid(c, t, 496, 430, 0.42, mouth='o', eyes=1.2, sweat=1, arms=((150, 10), (150, 10)), look=(0.6, -0.6))
            S.rrect(c, 520, 200, 120, 100, 16); c.set_source_rgba(1, 0.2, 0.15, 0.9 * (int(t * 4) % 2)); c.fill()
            T(c, "!", 580, 278, 80, WHITE, int(t * 4) % 2, stroke=None)
    else:
        if p < 0.08:
            B.figure(c, 380, 430, 0.42, t, who='friend', mouth='flat', arms=((14, -10), (14, -10)))
        elif p < 0.4:
            B.figure(c, 380, 430, 0.42, t, who='friend', mouth='flat', arms=((14, -10), (85, -5)), look=(0.6, 0))
        elif p < 0.72:
            B.figure(c, 380, 430, 0.42, t, who='friend', mouth='smile', arms=((14, -10), (40, 110)), phone=1, glow=0.6)
            bubble(c, 180, 200, "CALLING GUARD...")
        else:
            B.figure(c, 380, 430, 0.42, t, who='friend', mouth='smile', arms=((14, -10), (14, -10)))
            bubble(c, 200, 200, "HELP IS COMING")


def bubble(c, x, y, txt):
    w = len(txt) * 22 + 60
    S.rrect(c, x, y, w, 70, 30); c.set_source_rgba(1, 1, 1, 0.95); c.fill()
    T(c, txt, x + w / 2, y + 47, 34, (0.1, 0.1, 0.15), stroke=None)


import body as B  # noqa: E402


def build():
    return DL.Dilemma(D, CAPS, ROLES, lambda c, side, t, p: lift(c, t, side, p), CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
