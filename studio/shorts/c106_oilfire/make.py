"""BRAVE vs NORMAL — WHO'S RIGHT? #13: oil pan (kadhai) on fire (engine: studio/shorts/dilemma.py).
Fact: never put water on an oil/chip-pan fire - it turns to steam and throws burning oil out as a fireball (Essex
County Fire & Rescue Service, Aug 2024; West Sussex Fire & Rescue Service kitchen safety). NFPA cooking safety: for a
small grease fire, smother it by sliding a lid over the pan and turning off the stove; leave the pan covered until it
is completely cooled. Don't move the pan. If the fire grows, get everyone out and call the fire service (India: 101).
No injury shown: Brave freezes holding the mug, then the red WRONG freeze."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c106_oilfire"
CAPS = [
    "The oil in the kadhai caught FIRE! Brave: quick, pour water. Normal: wait, get the lid. Whose side are you on?",
    "Brave grabs a mug of water and is about to throw it straight on the fire.",
    "Normal turns the gas off and slides the lid over the kadhai from the side.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Pour water on burning oil and it flashes into steam and blows up into a fireball.",
    "Gas off, lid on, don't move the kadhai, keep it covered till it cools. Fire growing? Get out and call 101.",
    "Oil on fire? Not water, the lid. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #13", question=("KADHAI OIL ON FIRE!", "WHAT DO YOU DO?"),
           brave="THROW WATER ON IT", normal="GAS OFF, COVER WITH LID", answer='N', grade='studio',
           why_title="OIL FIRE? DO THIS",
           why_rows=[("NEVER water: steam = fireball", RED), ("Turn the gas OFF", WHITE), ("Slide a lid over the pan", WHITE),
                     ("Don't move it, let it cool", WHITE), ("Fire growing? Get out, call 101", GRN)],
           src="SRC: NFPA + UK fire & rescue services", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

FLOOR = 900
PAN = (640, 575)   # kadhai centre (rim)


def room(c, t):
    c.rectangle(-400, 0, 1880, FLOOR); c.set_source_rgb(0.93, 0.87, 0.76); c.fill()
    c.rectangle(420, 400, 560, 230); c.set_source_rgb(0.86, 0.9, 0.92); c.fill()
    for j in range(10):
        c.move_to(420 + j * 56, 400); c.rel_line_to(0, 230)
    for j in range(4):
        c.move_to(420, 400 + j * 57); c.rel_line_to(560, 0)
    c.set_source_rgba(0.6, 0.65, 0.7, 0.6); c.set_line_width(2); c.stroke()
    c.rectangle(-400, FLOOR, 1880, 200); c.set_source_rgb(0.55, 0.42, 0.32); c.fill()
    for j in range(-4, 16):
        c.move_to(j * 110, FLOOR); c.rel_line_to(-60, 100); c.set_source_rgba(0, 0, 0, 0.12); c.set_line_width(3); c.stroke()
    # shelf with jars (left)
    c.rectangle(60, 300, 260, 16); c.set_source_rgb(0.45, 0.33, 0.24); c.fill()
    for j, col in enumerate(((0.85, 0.55, 0.2), (0.9, 0.8, 0.3), (0.6, 0.3, 0.2))):
        S.rrect(c, 80 + j * 80, 220, 56, 80, 10); c.set_source_rgb(*col); c.fill()
    # counter + stove
    c.rectangle(420, 640, 560, FLOOR - 640); c.set_source_rgb(0.42, 0.3, 0.22); c.fill()
    c.rectangle(410, 625, 580, 26); c.set_source_rgb(0.2, 0.2, 0.22); c.fill()
    S.rrect(c, 500, 590, 330, 40, 10); c.set_source_rgb(0.12, 0.12, 0.14); c.fill()
    for kx in (560, 770):
        c.arc(kx, 610, 10, 0, 2 * math.pi); c.set_source_rgb(0.7, 0.7, 0.72); c.fill()


def kadhai(c, lid=0.0):
    x, y = PAN
    c.save(); c.translate(x, y)
    c.move_to(-130, 0); c.curve_to(-110, 60, 110, 60, 130, 0); c.close_path()
    c.set_source_rgb(0.18, 0.18, 0.2); c.fill()
    for sx in (-1, 1):
        c.arc(sx * 150, 4, 18, 0, 2 * math.pi); c.set_source_rgb(0.18, 0.18, 0.2); c.set_line_width(7); c.stroke()
    c.save(); c.scale(1, 0.22); c.arc(0, 0, 130, 0, 2 * math.pi); c.restore()
    c.set_source_rgb(0.55, 0.42, 0.12); c.fill()   # oil
    c.restore()
    if lid > 0:
        lx = x + 420 * (1 - lid)
        c.save(); c.translate(lx, y - 8)
        c.save(); c.scale(1, 0.32); c.arc(0, 0, 140, math.pi, 2 * math.pi); c.restore()
        c.set_source_rgb(0.72, 0.74, 0.78); c.fill()
        c.rectangle(-140, -2, 280, 8); c.set_source_rgb(0.55, 0.57, 0.6); c.fill()
        S.rrect(c, -22, -62, 44, 18, 8); c.set_source_rgb(0.15, 0.15, 0.17); c.fill()
        c.restore()


def flames(c, t, a=1.0, h=1.0):
    if a <= 0:
        return
    x, y = PAN
    for j in range(7):
        fx = x - 100 + j * 33
        fh = (120 + 50 * math.sin(t * 9 + j * 1.7)) * h * (0.75 + 0.25 * (j % 3))
        for col, s in (((1.0, 0.45, 0.1), 1.0), ((1.0, 0.8, 0.2), 0.6)):
            c.move_to(fx - 24 * s, y)
            c.curve_to(fx - 26 * s, y - fh * s * 0.5, fx + 8 * math.sin(t * 7 + j), y - fh * s * 0.8, fx, y - fh * s)
            c.curve_to(fx + 10, y - fh * s * 0.6, fx + 26 * s, y - fh * s * 0.4, fx + 24 * s, y)
            c.close_path(); c.set_source_rgba(*col, a * 0.92); c.fill()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def mug(c, x, y):
    S.rrect(c, x - 30, y - 40, 60, 80, 10); c.set_source_rgb(0.25, 0.5, 0.85); c.fill()
    c.arc(x + 36, y, 18, -1.4, 1.4); c.set_source_rgb(0.25, 0.5, 0.85); c.set_line_width(8); c.stroke()
    c.save(); c.translate(x, y - 40); c.scale(1, 0.3); c.arc(0, 0, 28, 0, 2 * math.pi); c.restore()
    c.set_source_rgb(0.6, 0.85, 1.0); c.fill()


def scene(c, side, t, p):
    room(c, t)
    if side == 'B':
        kadhai(c)
        flames(c, t)
        q = S.ease(min(1, p / 0.5))
        x = 200 + 120 * q
        K.sid(c, t, x, 455, 0.42, mouth='o', look=(0.8, 0), arms=((14, -10), (100, -60)), eyes=1.2)
        mug(c, x + 120, 470)
        if p > 0.55:
            S.rrect(c, 330, 380, 210, 56, 20); c.set_source_rgba(*RED, 0.92); c.fill()
            T(c, "WATER + OIL?!", 435, 418, 28, WHITE, stroke=None)
            bubble(c, 540, 260, "STOP! STEAM = FIREBALL", (1, 0.82, 0.8))
        else:
            bubble(c, 540, 260, "POUR WATER, QUICK!", (1, 0.85, 0.8))
    else:
        gas_off = p > 0.2
        lid = S.ease(max(0, min(1, (p - 0.3) / 0.35)))
        kadhai(c)
        flames(c, t, 1.0 - lid, 1.0 - 0.6 * lid)
        kadhai(c, lid) if lid > 0 else None
        B.figure(c, 870, 455, 0.42, t, who='friend', mouth='flat', arms=((150, 30), (14, -10)), look=(-0.7, 0.2))
        if gas_off:
            S.rrect(c, 500, 650, 150, 50, 18); c.set_source_rgba(0.05, 0.4, 0.15, 0.9); c.fill()
            T(c, "GAS OFF", 575, 684, 26, WHITE, stroke=None)
        msg = "WAIT, GET THE LID" if p < 0.12 else "GAS OFF" if p < 0.3 else ("SLIDE THE LID ON" if p < 0.7 else "LEAVE IT COVERED")
        bubble(c, 560, 260, msg)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
