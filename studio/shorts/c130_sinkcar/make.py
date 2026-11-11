"""BRAVE vs NORMAL — WHO'S RIGHT? #19: car falls into a canal at night (engine: studio/shorts/dilemma.py).
Facts: Prof. Gordon Giesbrecht (Univ. of Manitoba) 'Seatbelts, Windows, Children, Out' (NPR 26 Mar 2024, Kids and
Cars 'Sixty seconds'): you have roughly the first minute while the car floats; don't call for help first; water
pressure outside makes the doors almost impossible to open; unbuckle, open (or break) a SIDE window right away,
push children out first, then get out and up. Windscreens are laminated and hard to break: break a side window with
an escape tool. Brand-safe: no one drowns; Brave freezes pushing the stuck door, then the red WRONG freeze.
Voice take sped 1.06x."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c130_sinkcar"
CAPS = [
    "At night the car falls into a canal and water is coming in. Brave: open the door and get out. Normal: seatbelt first, then the window. You?",
    "Brave pushes the door with full force. But the water outside is pressing it shut. It won't even move.",
    "Normal unbuckles, rolls the window down at once, and gets out through the window, UP.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. The water pressure outside keeps the door shut. Your escape window is just the first minute.",
    "Seatbelt, window, children first, then OUT. Window won't open? Break a SIDE window. Keep an escape hammer in the car.",
    "Don't waste time on the phone. Get out first. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #19", question=("CAR SINKING IN A CANAL!", "HOW DO YOU GET OUT?"),
           brave="FORCE THE DOOR OPEN", normal="SEATBELT, THEN WINDOW", answer='N', grade='night',
           why_title="CAR SINKING? S-W-C-O",
           why_rows=[("S: Seatbelt off", WHITE), ("W: Window open NOW", WHITE), ("C: Children out first", WHITE),
                     ("O: Out and up", GRN), ("Door won't open: pressure", RED), ("Keep an escape hammer", YEL)],
           src="SRC: Prof. Giesbrecht, Univ. of Manitoba (NPR)", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

CX, CY = 540, 600          # car centre
WIN = (330, 420, 420, 140)  # window x, y, w, h


def night(c, t, wl):
    g = c
    c.rectangle(-400, 0, 1880, 1100); c.set_source_rgb(0.05, 0.07, 0.15); c.fill()
    c.arc(1150, 120, 50, 0, 2 * math.pi); c.set_source_rgb(0.95, 0.95, 0.85); c.fill()
    for j in range(25):
        x = (j * 197) % 1800 - 300; y = (j * 89) % 300 + 20
        c.arc(x, y, 2.5, 0, 2 * math.pi); c.set_source_rgba(1, 1, 1, 0.5 + 0.5 * math.sin(t * 2 + j)); c.fill()
    # canal banks
    c.rectangle(-400, 300, 400, 800); c.set_source_rgb(0.18, 0.2, 0.16); c.fill()
    c.rectangle(1100, 300, 400, 800); c.fill()
    return g


def roof(c):
    x, y = CX, CY
    c.move_to(x - 240, y - 50); c.line_to(x - 180, y - 190); c.line_to(x + 160, y - 190); c.line_to(x + 250, y - 50)
    c.close_path(); c.set_source_rgb(0.7, 0.13, 0.13); c.fill()
    wx, wy, ww, wh = WIN
    c.rectangle(wx, wy, ww, wh); c.set_source_rgb(0.2, 0.18, 0.22); c.fill()        # dark cabin


def car(c, t, glass=1.0):
    x, y = CX, CY
    wx, wy, ww, wh = WIN
    if glass > 0:
        c.rectangle(wx, wy + wh * (1 - glass), ww, wh * glass); c.set_source_rgba(0.6, 0.8, 1.0, 0.3); c.fill()
    c.set_source_rgb(0.15, 0.15, 0.18); c.set_line_width(8); c.rectangle(wx, wy, ww, wh); c.stroke()
    S.rrect(c, x - 360, y - 50, 720, 160, 40); c.set_source_rgb(0.78, 0.16, 0.16); c.fill()   # body
    c.rectangle(x - 200, y - 40, 260, 140); c.set_source_rgba(0, 0, 0, 0.5); c.set_line_width(5); c.stroke()
    S.rrect(c, x - 30, y, 50, 14, 6); c.set_source_rgb(0.9, 0.9, 0.9); c.fill()
    for wx_ in (x - 230, x + 230):
        c.arc(wx_, y + 115, 55, 0, 2 * math.pi); c.set_source_rgb(0.08, 0.08, 0.1); c.fill()


def water(c, t, wl):
    c.move_to(-400, wl)
    for x in range(-400, 1500, 40):
        c.line_to(x, wl + 8 * math.sin(x / 50 + t * 3))
    c.line_to(1480, 1100); c.line_to(-400, 1100); c.close_path()
    c.set_source_rgba(0.08, 0.28, 0.45, 0.7); c.fill()


def person(c, t, who, x, y, arms, mouth='flat'):
    if who == 'B':
        K.sid(c, t, x, y, 0.3, mouth=mouth, look=(-0.6, 0.1), arms=arms, eyes=1.15)
    else:
        B.figure(c, x, y, 0.3, t, who='friend', mouth=mouth, look=(0.3, -0.4), arms=arms)


def badge(c, txt, col, y=150):
    w = len(txt) * 20 + 60
    S.rrect(c, 540 - w / 2, y, w, 60, 24); c.set_source_rgba(*col, 0.92); c.fill()
    T(c, txt, 540, y + 42, 32, WHITE, stroke=None)


def scene(c, side, t, p):
    if side == 'B':
        wl = 560 - 80 * p
        night(c, t, wl)
        roof(c)
        c.save(); c.rectangle(WIN[0], WIN[1], WIN[2], WIN[3]); c.clip()
        person(c, t, 'B', 560, 470, ((100, 40), (100, 60)), 'o' if p > 0.4 else 'flat')
        c.restore()
        car(c, t)
        water(c, t, wl)
        # pressure arrows pushing on the door
        for j in range(3):
            ph = (t * 1.2 + j / 3) % 1
            ax = 250 + 40 * ph; ay = 560 + j * 50
            c.move_to(ax - 80, ay); c.line_to(ax, ay); c.line_to(ax - 22, ay - 16); c.move_to(ax, ay); c.line_to(ax - 22, ay + 16)
            c.set_source_rgba(0.6, 0.9, 1.0, 0.9); c.set_line_width(8); c.stroke()
        T(c, "WATER PRESSURE", 330, 730, 32, (0.7, 0.92, 1.0), stroke=None)
        if p > 0.35:
            badge(c, "DOOR WON'T MOVE!", RED, 270)
        badge(c, "PUSH! PUSH!", (0.75, 0.35, 0.1))
    else:
        wl = 560 - 40 * p
        night(c, t, wl)
        out = S.ease(min(1, max(0, (p - 0.55) / 0.35)))
        glass = 1.0 - S.ease(min(1, max(0, (p - 0.25) / 0.25)))
        py = 470 - 330 * out
        roof(c)
        if out < 0.05:
            c.save(); c.rectangle(WIN[0], WIN[1], WIN[2], WIN[3]); c.clip()
            person(c, t, 'N', 540, py, ((14, -10), (100, -60)) if p > 0.25 else ((40, 80), (14, -10)))
            c.restore()
        car(c, t, glass)
        water(c, t, wl)
        if out >= 0.05:
            person(c, t, 'N', 540 + 30 * out, py, ((100, -80), (100, -80)), 'smile')
        msg = ("1. SEATBELT OFF" if p < 0.25 else "2. WINDOW DOWN NOW" if p < 0.55 else "3. OUT THROUGH WINDOW, UP")
        badge(c, msg, (0.05, 0.4, 0.15))
        if p < 0.25:
            c.arc(470, 520, 30, 0, 2 * math.pi); c.set_source_rgba(*GRN, 0.9); c.fill()
            T(c, "CLICK", 470, 470, 30, YEL, stroke=None)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
