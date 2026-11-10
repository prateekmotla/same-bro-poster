"""BRAVE vs NORMAL — WHO'S RIGHT? #4: building fire, lift vs stairs (engine: studio/shorts/dilemma.py).
Fact: fire services everywhere (e.g. US Fire Administration high-rise guidance; Indian fire & emergency services
do's and don'ts): never use a lift/elevator in a fire, use the stairs; stay low under smoke; India fire 101, emergency 112."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s81_fire"
CAPS = [
    "Fire in the building, and you're on the 8th floor. Brave: let's take the lift, it's faster. Normal: the stairs. Whose side are you on?",
    "Brave gets into the lift. But in a fire, a lift can stop midway, and smoke fills the shaft.",
    "Normal hits the fire alarm, stays low to avoid the smoke, and walks down the stairs.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Fire services' first rule: NEVER take the lift in a fire. If the power cuts, you're trapped inside.",
    "Take the stairs, stay low if there's smoke, and call 101 or 112.",
    "Not fast, SAFE is the goal. What would YOU do first?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #4", question=("FIRE ON YOUR FLOOR.", "LIFT OR STAIRS?"),
           brave="TAKE THE LIFT, FASTER", normal="TAKE THE STAIRS", answer='N', grade='studio',
           why_title="IN A FIRE: NEVER THE LIFT",
           why_rows=[("Lift can stop midway", RED), ("Smoke fills the lift shaft", WHITE),
                     ("Power cut = trapped inside", WHITE), ("Stairs + stay low in smoke", WHITE),
                     ("Call 101 (fire) or 112", GRN)],
           src="SRC: Fire services high-rise safety advice", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))
FLOOR = 880


def corridor(c, t):
    c.rectangle(-400, 0, 1880, 1000); c.set_source_rgb(0.62, 0.6, 0.56); c.fill()
    c.rectangle(-400, FLOOR, 1880, 120); c.set_source_rgb(0.3, 0.28, 0.27); c.fill()
    # stair door + EXIT sign
    c.rectangle(170, 380, 200, 500); c.set_source_rgb(0.55, 0.15, 0.12); c.fill()
    c.arc(340, 640, 10, 0, 2 * math.pi); c.set_source_rgb(0.85, 0.85, 0.8); c.fill()
    S.rrect(c, 190, 300, 160, 60, 8); c.set_source_rgb(0.1, 0.65, 0.3); c.fill()
    T(c, "EXIT", 270, 345, 40, WHITE, stroke=None)
    # fire alarm box
    S.rrect(c, 420, 500, 70, 90, 8); c.set_source_rgb(0.85, 0.12, 0.1); c.fill()
    T(c, "FIRE", 455, 555, 22, WHITE, stroke=None)
    # lift
    c.rectangle(600, 300, 300, 580); c.set_source_rgb(0.45, 0.45, 0.48); c.fill()
    S.rrect(c, 690, 220, 120, 60, 8); c.set_source_rgb(0.05, 0.05, 0.05); c.fill()
    c.arc(940, 560, 18, 0, 2 * math.pi); c.set_source_rgb(0.8, 0.8, 0.82); c.fill()
    # fire glow from the right
    r = cairo.RadialGradient(1400, 700, 50, 1400, 700, 700)
    r.add_color_stop_rgba(0, 1, 0.45, 0.1, 0.7 + 0.1 * math.sin(t * 9)); r.add_color_stop_rgba(1, 1, 0.4, 0.1, 0)
    c.set_source(r); c.rectangle(-400, 0, 1880, 1000); c.fill()


def smoke(c, t, dense=1.0):
    for j in range(14):
        x = -380 + j * 140 + 30 * math.sin(t * 0.7 + j)
        y = 90 + 40 * math.sin(t * 0.9 + j * 1.7)
        c.arc(x, y, 130, 0, 2 * math.pi); c.set_source_rgba(0.25, 0.25, 0.27, 0.55 * dense); c.fill()


def lift_doors(c, op):
    gap = 140 * op
    for x0, x1 in ((605, 750 - gap), (750 + gap, 895)):
        c.rectangle(x0, 305, x1 - x0, 575); c.set_source_rgb(0.7, 0.72, 0.76); c.fill()
        c.rectangle(x0, 305, x1 - x0, 575); c.set_source_rgba(0, 0, 0, 0.4); c.set_line_width(3); c.stroke()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x + w / 2, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def scene(c, side, t, p):
    corridor(c, t)
    smoke(c, t, 1.0 if side == 'B' else 0.8)
    if side == 'B':
        if p < 0.4:
            op = min(1, max(0, (p - 0.08) / 0.1)) if p < 0.3 else max(0, 1 - (p - 0.3) / 0.1)
            if op > 0:
                c.rectangle(610, 305, 280, 575); c.set_source_rgb(0.2, 0.2, 0.22); c.fill()
            x = 520 if p < 0.16 else 520 + (750 - 520) * min(1, (p - 0.16) / 0.12)
            if p < 0.3:
                K.sid(c, t, x, 430, 0.42, mouth='smirk', arms=((14, -10), (90, -10)) if p < 0.1 else ((14, -10), (14, -10)), pose='stand')
            lift_doors(c, op)
            T(c, "8", 750, 266, 40, (1, 0.3, 0.2), stroke=None)
        else:
            lift_doors(c, 0)
            fl = 7 if p < 0.5 else 6
            if p < 0.55:
                T(c, str(fl), 750, 266, 40, (1, 0.3, 0.2), stroke=None)
            else:
                T(c, "STOP", 750, 266, 30, (1, 0.2, 0.15), int(t * 3) % 2 or 0.3, stroke=None)
            for j in range(6):   # smoke leaking from the shaft
                y = 300 - ((t * 80 + j * 40) % 200)
                c.arc(750 + 30 * math.sin(t + j), y + 20, 40, 0, 2 * math.pi); c.set_source_rgba(0.2, 0.2, 0.22, 0.6); c.fill()
            if p > 0.55:
                bubble(c, 170, 330, "LIFT STUCK! SMOKE IN SHAFT", (1, 0.82, 0.8))
                S.rrect(c, 830, 380, 110, 110, 18); c.set_source_rgba(1, 0.2, 0.15, 0.9 * (int(t * 4) % 2)); c.fill()
                T(c, "!", 885, 466, 84, WHITE, int(t * 4) % 2, stroke=None)
    else:
        lift_doors(c, 0)
        T(c, "8", 750, 266, 40, (1, 0.3, 0.2), stroke=None)
        if p >= 0.12:
            a = 0.5 + 0.5 * math.sin(t * 14)
            c.arc(455, 470, 26, 0, 2 * math.pi); c.set_source_rgba(1, 0.2, 0.1, a); c.fill()
        if p < 0.12:
            B.figure(c, 560, 430, 0.42, t, who='friend', mouth='flat', arms=((14, -10), (14, -10)), look=(-0.6, 0))
        elif p < 0.35:
            B.figure(c, 540, 430, 0.42, t, who='friend', mouth='o', arms=((14, -10), (150, 20)), look=(-0.6, -0.2))
            T(c, "ALARM!", 460, 420, 40, (1, 0.9, 0.3))
        elif p < 0.7:
            q = (p - 0.35) / 0.35
            x = 540 - (540 - 300) * q
            B.figure(c, x, 470, 0.42, t, who='friend', mouth='flat', arms=((40, 30), (40, 30)), lean=-18, pose='walk', ph=t * 1.6)
            T(c, "STAY LOW", 330, 280 + 0 * q, 40, WHITE)
        else:
            c.rectangle(170, 380, 200, 500); c.set_source_rgb(0.15, 0.14, 0.14); c.fill()
            for j in range(6):
                c.rectangle(180 + j * 30, 420 + j * 75, 190 - j * 30, 14); c.set_source_rgb(0.55, 0.55, 0.55); c.fill()
            c.move_to(370, 380); c.line_to(440, 400); c.line_to(440, 860); c.line_to(370, 880); c.close_path()
            c.set_source_rgb(0.55, 0.15, 0.12); c.fill()
            bubble(c, 470, 330, "STAIRS + CALL 101", (0.85, 1, 0.85))


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
