"""BRAVE vs NORMAL — WHO'S RIGHT? #9: lightning in an open ground (engine: studio/shorts/dilemma.py).
Fact: IMD 'Thunderstorm & Lightning: Do's and Don'ts' (mausam.imd.gov.in, 2025) + NDMA lightning awareness: don't take
shelter under isolated/tall trees; go inside a pucca building or a hard-top vehicle (windows closed); if caught in the
open with no shelter, crouch low with feet together and head down, don't lie flat on the ground. Lightning tends to
strike the tallest object around. Voice take sped 1.1x (42.0 s > 38.2 s). Nobody is struck on screen."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c090_lightning"
CAPS = [
    "Open ground, and suddenly LOUD lightning starts. Brave: let's go under that big tree. Normal: away from the tree, get inside a building. Whose side are you on?",
    "Brave goes and stands under the lone tall tree. But lightning usually hits the TALLEST thing around.",
    "Normal runs away from the tree, into the nearby pucca building.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. IMD and NDMA advice: in lightning, never stay under a lone tree.",
    "A pucca house or a closed car is safest. Stuck in the open? Squat low, feet together, head down. Don't lie flat.",
    "Lightning? Not a tree, find a roof. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #9", question=("LIGHTNING IN THE OPEN!", "WHAT DO YOU DO?"),
           brave="HIDE UNDER THE TREE", normal="GET INSIDE A BUILDING", answer='N', grade='studio',
           why_title="LIGHTNING? DO THIS",
           why_rows=[("NEVER under a lone tree", RED), ("Go inside a pucca building", WHITE), ("or a closed car", WHITE),
                     ("No shelter? squat, feet together", WHITE), ("Don't lie flat on the ground", GRN)],
           src="SRC: IMD & NDMA lightning do's and don'ts", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

GROUND = 760
TREE = (330, GROUND)


def bg(c, t, flash=0.0):
    g = cairo.LinearGradient(0, 0, 0, GROUND)
    g.add_color_stop_rgb(0, 0.16 + 0.5 * flash, 0.18 + 0.5 * flash, 0.26 + 0.5 * flash)
    g.add_color_stop_rgb(1, 0.36 + 0.4 * flash, 0.38 + 0.4 * flash, 0.44 + 0.4 * flash)
    c.rectangle(-400, 0, 1880, GROUND); c.set_source(g); c.fill()
    for j in range(7):                      # clouds
        x = -350 + j * 290 + 20 * math.sin(t * 0.3 + j)
        for r, dx, dy in ((110, 0, 0), (90, 110, 20), (80, -100, 25)):
            c.arc(x + dx, 90 + dy + (j % 2) * 30, r, 0, 2 * math.pi)
        c.set_source_rgba(0.12, 0.13, 0.18, 0.95); c.fill()
    c.rectangle(-400, GROUND, 1880, 300); c.set_source_rgb(0.3, 0.42, 0.22); c.fill()
    for x in range(-390, 1480, 40):
        c.move_to(x, GROUND + 8); c.rel_line_to(5, -20 - 8 * math.sin(x)); c.set_source_rgb(0.22, 0.34, 0.16)
        c.set_line_width(4); c.stroke()
    for j in range(40):                     # rain
        x = (j * 97 + t * 400) % 1880 - 400
        y = (j * 151 + t * 900) % 900
        c.move_to(x, y); c.rel_line_to(-8, 30); c.set_source_rgba(0.75, 0.82, 0.95, 0.35); c.set_line_width(3); c.stroke()
    # lone tall tree (left)
    x, y = TREE
    c.rectangle(x - 22, y - 430, 44, 430); c.set_source_rgb(0.3, 0.2, 0.12); c.fill()
    for r, dx, dy in ((150, 0, -470), (120, -110, -400), (120, 110, -400), (110, 0, -560)):
        c.arc(x + dx, y + dy, r, 0, 2 * math.pi)
    c.set_source_rgb(0.12, 0.3, 0.16); c.fill()
    # pucca building (right)
    c.rectangle(740, 380, 600, GROUND - 380); c.set_source_rgb(0.74, 0.7, 0.62); c.fill()
    c.move_to(720, 380); c.line_to(1040, 270); c.line_to(1360, 380); c.close_path(); c.set_source_rgb(0.5, 0.3, 0.25); c.fill()
    c.rectangle(800, 540, 120, GROUND - 540); c.set_source_rgb(0.35, 0.24, 0.16); c.fill()
    c.rectangle(980, 450, 110, 90); c.set_source_rgb(0.95, 0.85, 0.5); c.fill()


def bolt(c, x, y, a):
    pts = [(x + 60, -20), (x + 10, y * 0.3), (x + 50, y * 0.45), (x - 10, y * 0.75), (x + 20, y * 0.8), (x, y)]
    c.move_to(*pts[0])
    for p_ in pts[1:]:
        c.line_to(*p_)
    c.set_source_rgba(1, 0.97, 0.6, a); c.set_line_width(16); c.stroke_preserve()
    c.set_source_rgba(1, 1, 1, a); c.set_line_width(6); c.stroke()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def scene(c, side, t, p):
    fl = max(0.0, math.sin(t * 2.3)) ** 30         # periodic sky flash
    if side == 'B':
        strike = p > 0.5
        f = fl if not strike else max(fl, max(0.0, 1 - ((t * 1.3) % 1) * 3))
        bg(c, t, f * 0.6)
        q = S.ease(min(1, p / 0.45))
        x = 600 - 190 * q
        K.sid(c, t, x, 300, 0.42, pose='walk' if q < 1 else 'stand', ph=t * 2, mouth='smirk' if not strike else 'o',
              look=(-0.6, -0.3), eyes=1.2 if strike else 1.0)
        if strike:
            bolt(c, TREE[0], TREE[1] - 690, f)
            c.arc(TREE[0], TREE[1] - 640, 80 + 6 * math.sin(t * 9), 0, 2 * math.pi)
            c.set_source_rgba(*RED, 0.9); c.set_line_width(10); c.stroke()
            bubble(c, 560, 800, "TALLEST THING = TARGET", (1, 0.82, 0.8))
        else:
            bubble(c, 560, 95, "UNDER THE TREE, CHILL!", (1, 0.85, 0.8))
    else:
        bg(c, t, fl * 0.5)
        q = S.ease(min(1, p / 0.7))
        x = 420 + 400 * q
        B.figure(c, x, 300, 0.42 - 0.06 * q, t, who='friend', pose='walk' if q < 1 else 'stand', ph=t * 2.2,
                 mouth='flat', look=(0.7, 0))
        if p > 0.12:
            c.arc(TREE[0], TREE[1] - 470, 200, 0, 2 * math.pi); c.set_source_rgba(*RED, 0.5); c.set_line_width(8); c.stroke()
            T(c, "AWAY FROM TREE", TREE[0], 330, 34, (1, 0.6, 0.55), stroke=None)
        bubble(c, 560, 95, "INSIDE, NOW!" if p < 0.75 else "SAFE INSIDE", (0.8, 1, 0.85) if p > 0.75 else (1, 1, 1))


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
