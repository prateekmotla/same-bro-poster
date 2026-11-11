"""BRAVE vs NORMAL — WHO'S RIGHT? #20: crowd crush at a mela (engine: studio/shorts/dilemma.py).
Facts: crowd-safety experts (Prof. G. Keith Still, crowd science; Mehdi Moussaid, Max Planck Institute — via NZ Herald /
CGTN / BOOM explainers after the 2022 Seoul crush): don't fight / push against the crowd; go with the surge and move
diagonally (sideways) towards the edge in the lulls between waves; keep your arms up in front of your chest like a
boxer to protect breathing space; stay on your feet, if you fall get up fast. India emergency 112.
Brand-safe: faceless silhouettes, no one hurt on screen; Brave ends on the red WRONG freeze."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c134_crowd"
CAPS = [
    "The mela crowd suddenly starts CRUSHING. Hard to breathe. Brave: push back and get out. Normal: go out diagonally. You?",
    "Brave pushes AGAINST the crowd with full force.",
    "Normal keeps his arms in front of his chest and slips out diagonally, to the side, between the waves.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Fight the crowd and you lose your strength AND your breath. Crowd experts say: go with the wave, exit diagonally.",
    "Arms up like a boxer in front of your chest to keep breathing space. Stay on your feet, if you fall, get up fast.",
    "The real brave one escapes with his brain. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #20", question=("CROWD CRUSH AT A MELA!", "WHAT DO YOU DO?"),
           brave="PUSH BACK AGAINST IT", normal="GO WITH IT, EXIT DIAGONALLY", answer='N', grade='warm',
           why_title="CAUGHT IN A CROWD CRUSH?",
           why_rows=[("DON'T push against it", RED), ("Go with the wave", WHITE), ("Exit diagonally, to the side", WHITE),
                     ("Arms up at chest, like a boxer", WHITE), ("Stay on your feet", GRN), ("Fell? Get up fast", YEL)],
           src="SRC: crowd-safety experts (G. Keith Still)", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

GROUND = 900
COLS = [(0.32, 0.3, 0.42), (0.42, 0.28, 0.3), (0.25, 0.36, 0.4), (0.4, 0.38, 0.3), (0.3, 0.3, 0.33), (0.45, 0.33, 0.42)]


def mela(c, t):
    g_top = (0.12, 0.1, 0.28)
    c.rectangle(-400, 0, 1880, GROUND); c.set_source_rgb(*g_top); c.fill()
    c.rectangle(-400, 260, 1880, GROUND - 260); c.set_source_rgb(0.2, 0.15, 0.3); c.fill()
    # stalls
    for j, x in enumerate(range(-380, 1500, 300)):
        c.rectangle(x, 150, 240, 120); c.set_source_rgb(*((0.85, 0.35, 0.2) if j % 2 else (0.95, 0.75, 0.25))); c.fill()
        for q in range(6):
            c.move_to(x + q * 40, 150); c.line_to(x + q * 40 + 20, 190); c.line_to(x + q * 40 + 40, 150)
        c.set_source_rgb(0.98, 0.95, 0.9); c.fill()
    # string lights
    for q in range(40):
        x = -400 + q * 48
        y = 70 + 25 * math.sin(q * 0.7)
        c.arc(x, y, 7, 0, 2 * math.pi)
        c.set_source_rgba(1, 0.85, 0.4, 0.6 + 0.4 * math.sin(t * 4 + q)); c.fill()
    # Ferris wheel silhouette
    c.arc(1250, 120, 110, 0, 2 * math.pi); c.set_source_rgba(0.6, 0.6, 0.75, 0.35); c.set_line_width(6); c.stroke()


def person(c, x, y, s, col):
    c.save(); c.translate(x, y); c.scale(s, s)
    S.rrect(c, -58, 30, 116, 300, 50); c.set_source_rgb(*col); c.fill()
    c.arc(0, 0, 38, 0, 2 * math.pi); c.set_source_rgb(col[0] * 0.75, col[1] * 0.75, col[2] * 0.75); c.fill()
    c.restore()


def crowd(c, t, rows, surge=1.0):
    for r in rows:
        y = 330 + r * 95
        s = 0.85 + r * 0.12
        dx = surge * 28 * math.sin(t * 2.6 - r * 0.6)
        off = 60 if int(r) % 2 else 0
        for q in range(-4, 16):
            x = q * 125 + off + dx
            person(c, x, y, s, COLS[(q * 7 + int(r) * 3) % len(COLS)])


def arrow(c, x, y, ang, col, a=0.85, ln=150):
    c.save(); c.translate(x, y); c.rotate(ang)
    c.rectangle(0, -14, ln - 40, 28); c.move_to(ln - 40, -40); c.line_to(ln + 10, 0); c.line_to(ln - 40, 40); c.close_path()
    c.set_source_rgba(*col, a); c.fill()
    c.restore()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 23 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 34, (0.1, 0.1, 0.15), stroke=None)


def scene(c, side, t, p):
    mela(c, t)
    crowd(c, t, [0, 1])
    for q in range(4):  # surge direction
        arrow(c, -200 + q * 450 + 40 * math.sin(t * 2.6), 300, 0, (1, 0.35, 0.3), 0.55)
    if side == 'B':
        sh = 6 * math.sin(t * 30) if p > 0.2 else 0
        K.sid(c, t, 560 + sh, 430, 0.42, mouth='o' if p > 0.3 else 'flat', look=(-0.8, 0),
              arms=((100, 20), (100, 20)) if p > 0.15 else ((14, -10), (14, -10)), eyes=1.15, lean=-8 if p > 0.15 else 0)
        if p > 0.15:
            arrow(c, 470, 560, math.pi, (1, 0.6, 0.2), 0.95, 120)
        crowd(c, t, [3.4, 4.3])
        bubble(c, 540, 250, "I'LL PUSH THROUGH!", (1, 0.85, 0.8))
        if p > 0.55:
            S.rrect(c, 240, 730, 600, 60, 22); c.set_source_rgba(*RED, 0.92); c.fill()
            T(c, "FIGHTING THE CROWD = NO AIR", 540, 770, 28, WHITE, stroke=None)
    else:
        q = S.ease(min(1, max(0, (p - 0.15) / 0.75)))
        fx, fy = 500 + 300 * q, 430 + 30 * q
        c.save(); c.set_dash([24, 16]); c.move_to(500, 640); c.line_to(860, 720)
        c.set_source_rgba(*GRN, 0.9); c.set_line_width(10); c.stroke(); c.restore()
        arrow(c, 830, 712, 0.22, GRN, 0.95, 60)
        B.figure(c, fx, fy, 0.42, t, who='friend', mouth='flat', look=(0.6, 0.1),
                 arms=((40, 140), (40, 140)) if p > 0.1 else ((14, -10), (14, -10)))
        crowd(c, t, [3.4, 4.3])
        bubble(c, 540, 250, "GO WITH IT. DIAGONAL." if p < 0.7 else "OUT. SPACE TO BREATHE.")
        if p > 0.35:
            S.rrect(c, 300, 730, 480, 60, 22); c.set_source_rgba(0.05, 0.4, 0.15, 0.92); c.fill()
            T(c, "ARMS UP = BREATHING SPACE", 540, 770, 28, WHITE, stroke=None)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
