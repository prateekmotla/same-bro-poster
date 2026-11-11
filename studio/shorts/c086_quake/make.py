"""BRAVE vs NORMAL — WHO'S RIGHT? #8: earthquake indoors (engine: studio/shorts/dilemma.py).
Fact: NDMA earthquake Do's & Don'ts (ndma.gov.in/Natural-Hazards/Earthquakes/Dos-Donts) + CDC/FEMA 'Drop, Cover and
Hold On': indoors, DROP to the ground, take COVER under a sturdy table, HOLD ON till the shaking stops; stay away from
glass/windows/things that can fall; stay inside until the shaking stops; don't use lifts; then leave carefully by the
stairs. Most injuries come from falling/flying objects when people try to move during shaking. Voice take sped 1.1x
(42.0 s > 38.2 s). No injury shown on screen."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c086_quake"
CAPS = [
    "Suddenly the building starts shaking. EARTHQUAKE! Brave: run, take the stairs out. Normal: no, get under the table. Whose side are you on?",
    "Brave runs for the shaking stairs. Glass and stuff falling from above, danger on the way itself.",
    "Normal drops down, crawls under a strong table, covers his head and holds on to the table.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. NDMA's rule: Drop, Cover, Hold on. Run while it shakes, and falling glass and things hit you.",
    "Stay inside till the shaking stops, away from windows, NO lift. After it stops, calmly take the stairs out.",
    "Earthquake? Don't run, get down. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #8", question=("EARTHQUAKE INDOORS!", "WHAT DO YOU DO?"),
           brave="RUN DOWN THE STAIRS", normal="DROP, COVER, HOLD ON", answer='N', grade='studio',
           why_title="EARTHQUAKE? DO THIS",
           why_rows=[("DROP to the floor", WHITE), ("COVER under a strong table", WHITE), ("HOLD ON till it stops", WHITE),
                     ("Away from glass & windows", RED), ("NO lift. Stairs AFTER it stops", GRN)],
           src="SRC: NDMA earthquake do's & don'ts", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

FLOOR = 880


def shake(t):
    return 9 * math.sin(t * 43) + 5 * math.sin(t * 71), 4 * math.sin(t * 57)


def room(c, t):
    c.rectangle(-400, 0, 1880, FLOOR); c.set_source_rgb(0.86, 0.84, 0.78); c.fill()
    c.rectangle(-400, FLOOR, 1880, 200); c.set_source_rgb(0.5, 0.4, 0.32); c.fill()
    for j in range(-4, 16):
        c.move_to(j * 120, FLOOR); c.rel_line_to(-50, 120); c.set_source_rgba(0, 0, 0, 0.12); c.set_line_width(3); c.stroke()
    # window (left)
    x, y, w, h = -120, 200, 260, 330
    c.rectangle(x, y, w, h); c.set_source_rgb(0.62, 0.78, 0.93); c.fill()
    c.move_to(x + w / 2, y); c.rel_line_to(0, h); c.move_to(x, y + h / 2); c.rel_line_to(w, 0)
    c.set_source_rgb(0.97, 0.97, 0.97); c.set_line_width(10); c.stroke()
    c.rectangle(x - 8, y - 8, w + 16, h + 16); c.set_line_width(14); c.stroke()
    # bookshelf (right) and stair door
    c.rectangle(1130, 180, 300, FLOOR - 180); c.set_source_rgb(0.62, 0.48, 0.34); c.fill()
    c.rectangle(1150, 200, 260, FLOOR - 230); c.set_source_rgb(0.95, 0.95, 0.95); c.fill()
    T(c, "STAIRS", 1280, 260, 40, (0.1, 0.5, 0.2), stroke=None)
    for j in range(5):
        c.move_to(1150 + j * 52, FLOOR - 30); c.rel_line_to(0, -(j + 1) * 60)
    c.set_source_rgba(0.4, 0.4, 0.4, 0.6); c.set_line_width(4); c.stroke()
    # wall shelf with vases/books
    c.rectangle(700, 300, 330, 18); c.set_source_rgb(0.45, 0.33, 0.24); c.fill()
    for j, col in enumerate(((0.8, 0.3, 0.25), (0.25, 0.45, 0.75), (0.95, 0.75, 0.2), (0.3, 0.6, 0.4))):
        c.rectangle(720 + j * 70, 210 + (j % 2) * 20, 46, 90 - (j % 2) * 20); c.set_source_rgb(*col); c.fill()
    # hanging lamp
    sw = 0.18 * math.sin(t * 6)
    c.save(); c.translate(560, 0); c.rotate(sw)
    c.move_to(0, 0); c.line_to(0, 150); c.set_source_rgb(0.2, 0.2, 0.2); c.set_line_width(4); c.stroke()
    c.move_to(-60, 210); c.line_to(-30, 150); c.line_to(30, 150); c.line_to(60, 210); c.close_path()
    c.set_source_rgb(0.95, 0.8, 0.4); c.fill(); c.restore()


def table(c, x=470):
    c.rectangle(x - 250, 570, 500, 40); c.set_source_rgb(0.5, 0.33, 0.2); c.fill()
    for lx in (x - 235, x + 195):
        c.rectangle(lx, 610, 40, FLOOR - 610); c.set_source_rgb(0.42, 0.27, 0.16); c.fill()


def falling(c, t, a=1.0):
    """books and glass bits dropping from the shelf (objects only, nobody hit)."""
    for j in range(6):
        ph = (t * 0.9 + j / 6) % 1
        x = 760 + j * 48
        y = 320 + ph * 520
        c.save(); c.translate(x, y); c.rotate(ph * 4 + j)
        if j % 2:
            c.rectangle(-20, -28, 40, 56); c.set_source_rgba(0.8, 0.35, 0.25, a); c.fill()
        else:
            c.move_to(0, -18); c.line_to(14, 12); c.line_to(-12, 8); c.close_path()
            c.set_source_rgba(0.75, 0.9, 1.0, a * 0.9); c.fill()
        c.restore()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def scene(c, side, t, p):
    dx, dy = shake(t)
    c.save(); c.translate(dx, dy)
    room(c, t)
    table(c)
    if side == 'B':
        q = S.ease(min(1, p / 0.7))
        x = 500 + 320 * q
        K.sid(c, t, x, 380, 0.42, pose='walk', ph=t * 2.2, mouth='o', look=(0.8, 0), eyes=1.2)
        if p > 0.35:
            falling(c, t)
            bubble(c, 540, 60, "GLASS FALLING!", (1, 0.82, 0.8))
        else:
            bubble(c, 540, 60, "RUN! TAKE THE STAIRS!", (1, 0.85, 0.8))
    else:
        if p < 0.3:
            B.figure(c, 470, 380, 0.42, t, who='friend', mouth='flat', look=(0, 0.3))
            bubble(c, 540, 60, "DROP!")
        else:
            B.figure(c, 470, 680, 0.3, t, who='friend', pose='sit', mouth='flat', arms=((60, -150), (-60, -150)),
                     look=(0, 0.4))
            table(c)
            bubble(c, 540, 60, "COVER!" if p < 0.65 else "HOLD ON!")
            if p > 0.65:
                for sx in (-1, 1):
                    c.arc(470 + sx * 215, 640, 34, 0, 2 * math.pi); c.set_source_rgba(*GRN, 0.8); c.set_line_width(8); c.stroke()
    for j in range(3):
        c.move_to(-60 - j * 22, 360 + j * 50); c.rel_line_to(0, 70); c.move_to(1110 + j * 22, 160 + j * 50); c.rel_line_to(0, 70)
    c.set_source_rgba(0.3, 0.3, 0.3, 0.7); c.set_line_width(6); c.stroke()
    c.restore()


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
