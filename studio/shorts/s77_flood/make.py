"""BRAVE vs NORMAL — WHO'S RIGHT? #3: car at a flooded underpass (engine: studio/shorts/dilemma.py).
Fact: US National Weather Service 'Turn Around, Don't Drown' — about 12 inches (1 ft) of moving water can carry away
most cars; you can't judge depth or the road under floodwater. If a car stalls in rising water, get out to higher
ground. (Matches NDMA/IMD flood do's and don'ts: don't drive through flooded roads.)"""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
from kit import T, S, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s77_flood"
CAPS = [
    "Rain, and the underpass is full of water. Brave: it'll make it, drive in. Normal: stop, turn back. Whose side are you on?",
    "Brave drives into the water. The engine dies halfway, and the water is up to the doors.",
    "Normal stopped before the water, reversed, and took another route on higher ground.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Just 1 foot of moving water can sweep away most cars. And you can't tell how deep an underpass is from the top.",
    "The rule is simple: TURN AROUND, DON'T DROWN. If your car gets stuck in water, get out right away and go to higher ground.",
    "Being brave is cool. Staying alive matters more. What would YOU do first?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #3", question=("FLOODED UNDERPASS.", "WHAT DO YOU DO?"),
           brave="DRIVE THROUGH IT", normal="STOP & TURN BACK", answer='N', grade='studio',
           why_title="TURN AROUND, DON'T DROWN",
           why_rows=[("1 ft moving water can sweep a car", RED), ("You can't see how deep it is", WHITE),
                     ("Never drive into floodwater", WHITE), ("Stuck? Get out, go to high ground", WHITE),
                     ("Take another route", GRN)],
           src="SRC: US National Weather Service; NDMA flood tips", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

ROAD_Y, DIP_Y = 700, 830
X1, X2, X3, X4 = 420, 620, 840, 1040      # slope down X1-X2, flat bottom X2-X3, slope up X3-X4
WATER0 = 760


def road_y(x):
    if x < X1 or x > X4:
        return ROAD_Y
    if X2 <= x <= X3:
        return DIP_Y
    if x < X2:
        return ROAD_Y + (DIP_Y - ROAD_Y) * (x - X1) / (X2 - X1)
    return DIP_Y - (DIP_Y - ROAD_Y) * (x - X3) / (X4 - X3)


def bg(c, t):
    g = cairo.LinearGradient(0, 0, 0, 700)
    g.add_color_stop_rgb(0, 0.32, 0.35, 0.4); g.add_color_stop_rgb(1, 0.55, 0.57, 0.6)
    c.rectangle(-400, 0, 1880, 1000); c.set_source(g); c.fill()
    for x in range(-400, 1500, 130):     # far buildings
        h = 180 + 90 * math.sin(x * 0.07)
        c.rectangle(x, 520 - h, 110, h + 200); c.set_source_rgb(0.38, 0.4, 0.45); c.fill()
    # ground block + road
    c.move_to(-400, ROAD_Y)
    for x in range(-400, 1481, 10):
        c.line_to(x, road_y(x))
    c.line_to(1480, 1000); c.line_to(-400, 1000); c.close_path(); c.set_source_rgb(0.22, 0.22, 0.24); c.fill()
    c.move_to(-400, ROAD_Y)
    for x in range(-400, 1481, 10):
        c.line_to(x, road_y(x))
    c.set_source_rgb(0.85, 0.85, 0.8); c.set_line_width(5); c.stroke()
    # overpass bridge
    c.rectangle(-400, 300, 1880, 70); c.set_source_rgb(0.6, 0.6, 0.62); c.fill()
    c.rectangle(-400, 285, 1880, 18); c.set_source_rgb(0.75, 0.75, 0.77); c.fill()
    for px in (X1 - 40, X4 + 10):
        c.rectangle(px, 370, 50, road_y(px) - 370 if px < X2 else ROAD_Y - 370); c.set_source_rgb(0.5, 0.5, 0.52); c.fill()
    # warning sign
    c.rectangle(240, 560, 10, 140); c.set_source_rgb(0.3, 0.3, 0.3); c.fill()
    c.move_to(245, 480); c.line_to(305, 580); c.line_to(185, 580); c.close_path(); c.set_source_rgb(0.95, 0.75, 0.1); c.fill()
    T(c, "!", 245, 568, 64, (0.1, 0.1, 0.1), stroke=None)


def water(c, t, level):
    w = cairo.LinearGradient(0, level, 0, DIP_Y)
    w.add_color_stop_rgba(0, 0.45, 0.36, 0.22, 0.72); w.add_color_stop_rgba(1, 0.3, 0.24, 0.15, 0.9)
    c.move_to(-400, level)
    for x in range(-400, 1481, 16):
        c.line_to(x, level + 4 * math.sin(x * 0.04 + t * 4))
    c.line_to(1480, 1000); c.line_to(-400, 1000); c.close_path()
    c.save()
    c.move_to(-400, 0)
    for x in range(-400, 1481, 10):
        c.line_to(x, road_y(x) + 4)
    c.line_to(1480, 0); c.close_path(); c.clip()       # only inside the dip (above the road surface)
    c.restore()
    # clip to the dip region explicitly
    c.save()
    c.move_to(X1 - 60, level - 20)
    for x in range(X1 - 60, X4 + 61, 10):
        c.line_to(x, max(level - 20, road_y(x)))
    c.line_to(X4 + 60, level - 20); c.close_path(); c.clip()
    c.move_to(X1 - 60, level)
    for x in range(X1 - 60, X4 + 61, 16):
        c.line_to(x, level + 4 * math.sin(x * 0.04 + t * 4))
    c.line_to(X4 + 60, DIP_Y + 10); c.line_to(X1 - 60, DIP_Y + 10); c.close_path(); c.set_source(w); c.fill()
    c.restore()


def rain(c, t):
    for j in range(70):
        x = (j * 97 + t * 260) % 1880 - 400
        y = (j * 53 + t * 900) % 1000
        c.move_to(x, y); c.rel_line_to(-8, 30); c.set_source_rgba(0.85, 0.9, 1, 0.35); c.set_line_width(2.5); c.stroke()


def car(c, x, yb, col, tilt=0.0, face=(0.86, 0.63, 0.47), mouth='flat', flip=False):
    """side view car, x = centre, yb = wheel bottom."""
    c.save(); c.translate(x, yb); c.rotate(tilt)
    if flip:
        c.scale(-1, 1)
    c.move_to(-140, -30); c.line_to(-140, -75); c.line_to(-95, -82); c.line_to(-55, -140); c.line_to(55, -140)
    c.line_to(95, -85); c.line_to(140, -75); c.line_to(140, -30); c.close_path(); c.set_source_rgb(*col); c.fill()
    c.move_to(-45, -130); c.line_to(45, -130); c.line_to(80, -88); c.line_to(-80, -88); c.close_path()
    c.set_source_rgb(0.7, 0.85, 0.95); c.fill()
    c.arc(18, -102, 17, 0, 2 * math.pi); c.set_source_rgb(*face); c.fill()
    c.arc(18, -106, 18, math.pi, 2 * math.pi); c.set_source_rgb(0.12, 0.09, 0.08); c.fill()
    c.arc(27, -103, 3.5, 0, 2 * math.pi); c.set_source_rgb(0.1, 0.1, 0.1); c.fill()
    if mouth == 'o':
        c.arc(30, -92, 4.5, 0, 2 * math.pi); c.set_source_rgb(0.3, 0.1, 0.1); c.fill()
    c.rectangle(128, -68, 12, 14); c.set_source_rgb(1, 0.95, 0.6); c.fill()
    for wx in (-85, 85):
        c.arc(wx, -28, 28, 0, 2 * math.pi); c.set_source_rgb(0.1, 0.1, 0.1); c.fill()
        c.arc(wx, -28, 12, 0, 2 * math.pi); c.set_source_rgb(0.6, 0.6, 0.62); c.fill()
    c.restore()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x + w / 2, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


ORANGE_CAR = (0.95, 0.5, 0.15)
BLUE_CAR = (0.25, 0.5, 0.9)


def scene(c, side, t, p):
    bg(c, t)
    if side == 'B':
        if p < 0.1:
            x = 200
            tilt, lvl = 0.0, WATER0
        elif p < 0.45:
            q = S.ease((p - 0.1) / 0.35)
            x = 200 + (730 - 200) * q
            tilt, lvl = 0.0, WATER0
        else:
            x = 730
            tilt = 0.03 * math.sin(t * 2.5)
            lvl = WATER0 - 45 * S.ease(min(1, (p - 0.45) / 0.4))
        yb = road_y(x)
        if X1 < x < X2:
            tilt = 0.32
        car(c, x, yb, ORANGE_CAR, tilt, mouth='o' if p > 0.45 else 'flat')
        water(c, t, lvl)
        if 0.2 < p < 0.45:
            for j in range(6):
                c.arc(x - 150 - j * 25, lvl - 10 - 30 * math.sin(j + t * 9), 9, 0, 2 * math.pi)
                c.set_source_rgba(0.75, 0.65, 0.5, 0.8); c.fill()
        if p > 0.5:
            bubble(c, 380, 430, "ENGINE OFF!", (1, 0.82, 0.8))
            S.rrect(c, 800, 150, 110, 110, 18); c.set_source_rgba(1, 0.2, 0.15, 0.9 * (int(t * 4) % 2)); c.fill()
            T(c, "!", 855, 236, 84, WHITE, int(t * 4) % 2, stroke=None)
    else:
        if p < 0.08:
            x = 120
        elif p < 0.3:
            q = S.ease((p - 0.08) / 0.22)
            x = 120 + (270 - 120) * q
        elif p < 0.65:
            q = S.ease((p - 0.3) / 0.35)
            x = 270 - 330 * q
        else:
            x = -60
        water(c, t, WATER0)
        car(c, x, ROAD_Y, BLUE_CAR, 0.0)
        if 0.22 < p < 0.45:
            bubble(c, 330, 420, "STOP.", (0.85, 1, 0.85))
        if 0.3 <= p < 0.65:
            T(c, "< REVERSE", 330, 560, 44, WHITE)
        if p >= 0.6:
            bubble(c, 260, 420, "OTHER ROUTE >", (0.85, 1, 0.85))
    rain(c, t)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
