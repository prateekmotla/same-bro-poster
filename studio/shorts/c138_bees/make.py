"""BRAVE vs NORMAL — WHO'S RIGHT? #21: bee swarm in a park (engine: studio/shorts/dilemma.py).
Facts: CDC / NIOSH 'Insects and Scorpions' (outdoor workers page, updated Sep 2026): if attacked by several stinging
insects at once, run to get away from them; go indoors (a shaded area is better than an open area); "Do not jump into
water since some insects will hover above water"; swatting may cause stings; stings release a chemical that attracts
other bees. Covering the face/head while running is standard bee-safety advice (protects eyes, nose, mouth).
Brand-safe: no stings or injury on screen; Brave ends on the red WRONG freeze."""
import math
import random
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c138_bees"
CAPS = [
    "A whole swarm of bees is chasing you in the park. Brave: jump in the pond. Normal: cover your face and run. You?",
    "Brave jumps straight into the water and hides under it.",
    "Normal covers his face with his shirt and runs straight into the nearby building.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Jump in water and the bees just hover above it. Come up to breathe, and they sting.",
    "US CDC says: run, get indoors, DON'T jump into water. Cover your face and don't swat.",
    "The real brave one runs the right way. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #21", question=("BEE SWARM CHASING YOU!", "WHAT DO YOU DO?"),
           brave="JUMP INTO THE POND", normal="COVER FACE, RUN INSIDE", answer='N', grade='warm',
           why_title="BEE SWARM? DO THIS",
           why_rows=[("DON'T jump into water", RED), ("Bees wait above it", WHITE), ("Run, straight away", WHITE),
                     ("Get indoors / in a car", WHITE), ("Cover face + head", GRN), ("Don't swat at them", YEL)],
           src="SRC: US CDC / NIOSH stinging insects advice", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

GROUND = 880
RND = random.Random(138)
BEES = [(RND.uniform(-1, 1), RND.uniform(-1, 1), RND.uniform(0, 6.28), RND.uniform(1.5, 3.5)) for _ in range(70)]


def park(c, t):
    c.rectangle(-400, 0, 1880, GROUND); c.set_source_rgb(0.62, 0.82, 0.95); c.fill()
    c.arc(1200, 130, 70, 0, 2 * math.pi); c.set_source_rgb(1, 0.92, 0.6); c.fill()
    for x, h in ((-300, 260), (-120, 200), (60, 300)):      # far trees
        c.arc(x, GROUND - h, 130, 0, 2 * math.pi); c.set_source_rgb(0.3, 0.6, 0.35); c.fill()
    c.rectangle(-400, GROUND - 120, 1880, 340); c.set_source_rgb(0.42, 0.72, 0.36); c.fill()
    # building on the right with an open door
    c.rectangle(720, 330, 800, GROUND - 330); c.set_source_rgb(0.86, 0.78, 0.66); c.fill()
    for j in range(4):
        c.rectangle(760 + j * 140, 390, 90, 90); c.set_source_rgb(0.45, 0.6, 0.75); c.fill()
    c.rectangle(760, 600, 150, GROUND - 600); c.set_source_rgb(0.25, 0.18, 0.12); c.fill()
    T(c, "ENTRY", 835, 585, 26, (0.3, 0.2, 0.1), stroke=None)
    # tree with hive (left-centre)
    c.rectangle(210, 300, 50, GROUND - 300); c.set_source_rgb(0.45, 0.3, 0.18); c.fill()
    c.arc(235, 260, 170, 0, 2 * math.pi); c.set_source_rgb(0.24, 0.52, 0.28); c.fill()
    c.save(); c.translate(320, 360); c.scale(0.8, 1.1); c.arc(0, 0, 40, 0, 2 * math.pi); c.restore()
    c.set_source_rgb(0.85, 0.65, 0.25); c.fill()


def pond_back(c):
    c.save(); c.translate(560, GROUND + 40); c.scale(1, 0.28); c.arc(0, 0, 330, 0, 2 * math.pi); c.restore()
    c.set_source_rgb(0.2, 0.5, 0.75); c.fill()


def pond_front(c, t, y):
    c.rectangle(200, y, 720, GROUND + 140 - y); c.set_source_rgba(0.18, 0.46, 0.72, 0.93); c.fill()
    for j in range(4):
        c.move_to(230 + j * 170, y + 6 + 4 * math.sin(t * 3 + j)); c.rel_curve_to(40, -10, 80, 10, 120, 0)
        c.set_source_rgba(1, 1, 1, 0.6); c.set_line_width(4); c.stroke()


def swarm(c, t, cx, cy, r, a=1.0):
    for (ux, uy, ph, sp) in BEES:
        x = cx + r * (ux + 0.25 * math.sin(t * sp + ph))
        y = cy + r * 0.6 * (uy + 0.25 * math.cos(t * sp * 1.3 + ph))
        c.save(); c.translate(x, y)
        c.save(); c.scale(1.4, 1); c.arc(0, 0, 7, 0, 2 * math.pi); c.restore()
        c.set_source_rgba(0.98, 0.78, 0.15, a); c.fill()
        c.rectangle(-2, -7, 3, 14); c.set_source_rgba(0.1, 0.1, 0.1, a); c.fill()
        c.arc(-3, -7, 5, 0, 2 * math.pi); c.set_source_rgba(1, 1, 1, 0.6 * a); c.fill()
        c.restore()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 23 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 34, (0.1, 0.1, 0.15), stroke=None)


def scene(c, side, t, p):
    park(c, t)
    if side == 'B':
        pond_back(c)
        q = S.ease(min(1, max(0, (p - 0.1) / 0.3)))
        sy = 430 + 330 * q
        K.sid(c, t, 560, sy, 0.42, mouth='o' if p > 0.4 else 'smile', look=(0, -0.8) if p > 0.4 else (0.6, 0),
              arms=((100, 20), (100, 20)) if p < 0.4 else ((14, -10), (14, -10)), eyes=1.15)
        pond_front(c, t, GROUND - 40)
        swarm(c, t, 380 + 180 * q, 600 - 40 * q, 150 + 60 * q)
        bubble(c, 540, 250, "INTO THE WATER!" if p < 0.4 else "...NEED AIR...", (1, 0.85, 0.8))
        if p > 0.5:
            S.rrect(c, 240, 350, 600, 60, 22); c.set_source_rgba(*RED, 0.92); c.fill()
            T(c, "BEES WAIT ABOVE THE WATER", 540, 390, 28, WHITE, stroke=None)
    else:
        q = S.ease(min(1, max(0, (p - 0.1) / 0.75)))
        fx = 360 + 475 * q
        c.save(); c.set_dash([24, 16]); c.move_to(360, 900); c.line_to(840, 900)
        c.set_source_rgba(*GRN, 0.9); c.set_line_width(10); c.stroke(); c.restore()
        B.figure(c, fx, 430, 0.42, t, who='friend', mouth='flat', look=(0.8, 0),
                 arms=((60, 160), (60, 160)) if p > 0.1 else ((14, -10), (14, -10)))
        if p > 0.1:   # shirt pulled over the face
            S.rrect(c, fx - 55, 418, 110, 50, 22); c.set_source_rgba(0.3, 0.55, 0.85, 0.95); c.fill()
        swarm(c, t, 130 + 260 * q, 520, 160, 1.0 - 0.6 * q)
        bubble(c, 540, 250, "FACE COVERED. RUN!" if p < 0.7 else "INSIDE. DOOR SHUT.")
        if p > 0.35:
            S.rrect(c, 280, 350, 520, 56, 20); c.set_source_rgba(0.05, 0.4, 0.15, 0.92); c.fill()
            T(c, "RUN + GET INDOORS", 540, 388, 28, WHITE, stroke=None)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
