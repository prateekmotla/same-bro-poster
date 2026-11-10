"""BRAVE vs NORMAL — WHO'S RIGHT? #11: swept away by a river current (engine: studio/shorts/dilemma.py).
Fact: Water Safety NZ 'Survival Swimming' — if swept down a river use the Whitewater Position: float on your back,
face downstream with feet at the surface, head up; propel yourself toward an exit point; putting your feet down can trap
a foot under rocks. US National Park Service river safety: don't try to swim against the current, fatigue sets in
quickly; get on your back, feet pointed downstream to push off obstacles, flow with the current toward shore.
Voice take sped 1.1x (43.9 s > 40.0 s)."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c098_river"
CAPS = [
    "Crossing a river on a trek, your foot slips and the current sweeps you away. Brave: swim hard AGAINST the current. Normal: float on your back, feet first. Whose side are you on?",
    "Brave keeps swimming against the current. In two minutes his arms are dead, and he's still in the same spot.",
    "Normal lies on his back, feet in front, head up, and slowly moves towards the bank.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Water safety experts say: don't fight the current, you'll tire fast. On your back, feet first, to push off rocks.",
    "Don't put your feet down, they can get stuck in rocks. Go with the current, slowly towards the bank.",
    "Fighting the current isn't brave, it's exhausting. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #11", question=("SWEPT AWAY BY A RIVER!", "WHAT DO YOU DO?"),
           brave="SWIM AGAINST THE CURRENT", normal="FLOAT ON BACK, FEET FIRST", answer='N', grade='studio',
           why_title="SWEPT BY A CURRENT? DO THIS",
           why_rows=[("Don't fight the current", RED), ("Float on your back", WHITE), ("Feet first, pointing downstream", WHITE),
                     ("Never stand up in fast water", RED), ("Angle slowly to the bank", GRN)],
           src="SRC: Water Safety NZ & US NPS river safety", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

SKIN = (0.86, 0.63, 0.47)
WT, WB = 430, 1000          # water top / bottom in the virtual box
BANK_X = 900               # right bank (exit)


def bg(c, t, flow=1.0):
    g = cairo.LinearGradient(0, 0, 0, WT)
    g.add_color_stop_rgb(0, 0.5, 0.68, 0.88); g.add_color_stop_rgb(1, 0.82, 0.86, 0.84)
    c.rectangle(-400, 0, 1880, WT); c.set_source(g); c.fill()
    c.move_to(-400, WT)                      # mountains
    for x in range(-400, 1500, 50):
        c.line_to(x, 250 - 90 * abs(math.sin(x * 0.004)) - 25 * math.sin(x * 0.02))
    c.line_to(1480, WT); c.close_path(); c.set_source_rgb(0.33, 0.45, 0.4); c.fill()
    for x in range(-380, 1500, 64):          # pines
        h = 90 + 30 * math.sin(x * 0.11)
        c.move_to(x, WT); c.line_to(x + 26, WT - h); c.line_to(x + 52, WT); c.close_path()
        c.set_source_rgb(0.15, 0.3, 0.2); c.fill()
    w = cairo.LinearGradient(0, WT, 0, WB)
    w.add_color_stop_rgb(0, 0.28, 0.5, 0.55); w.add_color_stop_rgb(1, 0.1, 0.25, 0.32)
    c.rectangle(-400, WT, 1880, WB - WT); c.set_source(w); c.fill()
    # bank on the right (exit point)
    c.move_to(BANK_X, WT); c.curve_to(BANK_X - 40, 650, BANK_X + 20, 820, BANK_X - 30, WB)
    c.line_to(1480, WB); c.line_to(1480, WT); c.close_path(); c.set_source_rgb(0.45, 0.36, 0.22); c.fill()
    c.rectangle(BANK_X - 10, WT - 12, 300, 16); c.set_source_rgb(0.3, 0.52, 0.25); c.fill()
    # flow streaks (current runs right-to-left = downstream is LEFT)
    for j in range(26):
        y = WT + 30 + (j * 53) % (WB - WT - 40)
        x = (1300 - ((t * 420 * flow + j * 211) % 1900))
        c.move_to(x, y); c.rel_line_to(110 + 40 * (j % 3), 0)
        c.set_source_rgba(1, 1, 1, 0.28); c.set_line_width(5); c.stroke()
    # rocks
    for rx, ry, rr in ((240, 900, 55), (-100, 640, 45), (700, 950, 50)):
        c.save(); c.translate(rx, ry); c.scale(1, 0.55); c.arc(0, 0, rr, 0, 2 * math.pi); c.restore()
        c.set_source_rgb(0.38, 0.38, 0.4); c.fill()
        c.save(); c.translate(rx + 30, ry); c.scale(1, 0.3); c.arc(0, 0, rr * 0.9, 0, math.pi); c.restore()
        c.set_source_rgba(1, 1, 1, 0.45); c.set_line_width(4); c.stroke()
    # DOWNSTREAM label
    S.rrect(c, 190, 450, 300, 56, 20); c.set_source_rgba(0, 0, 0, 0.45); c.fill()
    T(c, "< CURRENT", 340, 490, 34, WHITE, stroke=None)


def head(c, x, y, hair=(0.12, 0.09, 0.08), mouth='flat', tired=0.0):
    c.arc(x, y, 40, 0, 2 * math.pi); c.set_source_rgb(*SKIN); c.fill()
    c.arc(x, y - 6, 42, math.pi * 1.05, math.pi * 1.95); c.set_source_rgb(*hair); c.set_line_width(20); c.stroke()
    for ex in (-14, 14):
        if tired > 0.5:
            c.move_to(x + ex - 7, y - 2); c.line_to(x + ex + 7, y - 2); c.set_source_rgb(0.1, 0.08, 0.08)
            c.set_line_width(4); c.stroke()
        else:
            c.arc(x + ex, y - 3, 5.5, 0, 2 * math.pi); c.set_source_rgb(0.1, 0.08, 0.08); c.fill()
    if mouth == 'o':
        c.arc(x, y + 18, 8, 0, 2 * math.pi); c.set_source_rgb(0.35, 0.1, 0.1); c.fill()
    else:
        c.move_to(x - 10, y + 18); c.line_to(x + 10, y + 18); c.set_source_rgb(0.3, 0.1, 0.1); c.set_line_width(4); c.stroke()


def splash(c, x, y, t, n=6, a=0.8):
    for j in range(n):
        ang = j / n * math.pi + 0.3 * math.sin(t * 9 + j)
        r = 50 + 25 * ((t * 3 + j * 0.3) % 1)
        c.arc(x + r * math.cos(ang), y - r * 0.6 * math.sin(ang), 9, 0, 2 * math.pi)
        c.set_source_rgba(0.88, 0.96, 1, a); c.fill()


def meter(c, val, label):
    S.rrect(c, 260, 70, 560, 110, 26); c.set_source_rgba(0.03, 0.03, 0.06, 0.85); c.fill()
    T(c, label, 540, 112, 30, WHITE, stroke=None)
    S.rrect(c, 290, 130, 500, 28, 14); c.set_source_rgba(1, 1, 1, 0.15); c.fill()
    col = GRN if val > 0.6 else (YEL if val > 0.3 else RED)
    S.rrect(c, 290, 130, max(28, 500 * val), 28, 14); c.set_source_rgb(*col); c.fill()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def scene(c, side, t, p):
    if side == 'B':
        bg(c, t, 1.3)
        x, y = 540 + 10 * math.sin(t * 2), 700 + 6 * math.sin(t * 5)
        tired = min(1, max(0, (p - 0.15) / 0.7))
        # arms (front crawl, facing upstream = right)
        sp = 9 * (1 - 0.6 * tired)
        for sd in (0, math.pi):
            a = t * sp + sd
            c.move_to(x + 10, y + 10); c.line_to(x + 70 + 60 * math.cos(a), y - 50 * max(0, math.sin(a)) + 20)
            c.set_source_rgb(*SKIN); c.set_line_width(20); c.set_line_cap(cairo.LINE_CAP_ROUND); c.stroke()
        head(c, x, y - 10, (0.12, 0.09, 0.08), 'o' if tired > 0.3 else 'flat', tired)
        c.rectangle(x - 300, y + 18, 600, 400); c.set_source_rgba(0.2, 0.42, 0.48, 0.55); c.fill()
        splash(c, x + 80, y + 20, t, 7, 0.8 * (1 - 0.5 * tired))
        meter(c, 1 - 0.95 * tired, "ENERGY" if tired < 0.8 else "ENERGY: EMPTY")
        bubble(c, 540, 230, "STILL IN THE SAME SPOT!" if p > 0.45 else "FIGHT THE CURRENT!", (1, 0.85, 0.8))
        if p > 0.45:
            for j in range(3):   # sweat drops
                c.arc(x - 50 + j * 50, y - 80 - (t * 60 + j * 20) % 40, 7, 0, 2 * math.pi)
                c.set_source_rgba(0.7, 0.85, 1, 0.9); c.fill()
    else:
        bg(c, t, 1.0)
        q = S.ease(min(1, p / 0.9))
        # floats on back: head upstream (right), feet downstream (left); drifts left while angling to the bank (right)
        x = 470 + 300 * q
        y = 720 - 180 * q + 6 * math.sin(t * 3)
        ang = -0.18
        c.save(); c.translate(x, y); c.rotate(ang); c.scale(0.8, 0.8)
        S.rrect(c, -200, -26, 190, 52, 26); c.set_source_rgb(0.25, 0.45, 0.85); c.fill()     # torso (blue tee)
        for dy in (-12, 12):                                                                 # legs + feet up
            c.move_to(-200, dy); c.line_to(-330, dy * 0.6); c.set_source_rgb(0.2, 0.2, 0.28); c.set_line_width(22)
            c.set_line_cap(cairo.LINE_CAP_ROUND); c.stroke()
        c.arc(-345, -8, 13, 0, 2 * math.pi); c.set_source_rgb(*SKIN); c.fill()
        c.arc(-345, 14, 13, 0, 2 * math.pi); c.fill()
        a = math.sin(t * 2.5) * 0.5
        c.move_to(-60, 20); c.line_to(-40 + 60 * math.cos(a), 70); c.set_source_rgb(*SKIN); c.set_line_width(16); c.stroke()
        head(c, 30, -8, (0.2, 0.12, 0.08), 'flat')
        c.restore()
        c.save(); c.translate(x, y + 15); c.rotate(ang)
        c.rectangle(-290, 0, 340, 50); c.restore(); c.set_source_rgba(0.22, 0.44, 0.5, 0.5); c.fill()
        meter(c, 0.95 - 0.1 * q, "ENERGY")
        if p < 0.3:
            bubble(c, 540, 230, "ON YOUR BACK, FEET FIRST")
        elif p < 0.9:
            bubble(c, 540, 230, "ANGLE SLOWLY TO THE BANK")
        else:
            bubble(c, 540, 230, "SAFE ON THE BANK.")
        # exit arrow
        if p < 0.9:
            c.move_to(x + 70, y - 40); c.line_to(860, 470); c.set_source_rgba(*GRN, 0.8); c.set_line_width(8); c.stroke()
            c.move_to(860, 470); c.line_to(820, 468); c.line_to(845, 500); c.close_path(); c.fill()


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
