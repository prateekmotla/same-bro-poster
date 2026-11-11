"""BRAVE vs NORMAL — WHO'S RIGHT? #22: friend faints at a college function (engine: studio/shorts/dilemma.py).
Facts: MedlinePlus 'Unconsciousness - first aid' (reviewed Jan 2025): lay the person flat and raise the feet about
12 inches (30 cm); do not give an unconscious person any food or drink; do not slap or splash water on the face to
revive them; call emergency services if they do not return to consciousness quickly (within a minute). St John
Ambulance Victoria 'Fainting first aid' (Sep 2024): on the back with legs elevated to restore blood flow to the brain,
don't splash the face with water, water only once fully conscious. India emergency 112.
Brand-safe: no injury; Brave freezes holding the bottle, then the red WRONG freeze. Victim lying = rotated figure."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c142_faint"
CAPS = [
    "At a college function a friend suddenly FAINTS. Brave: splash water on his face, make him drink. Normal: lay him flat, legs up. You?",
    "Brave throws water on his face and pushes a bottle to his mouth.",
    "Normal lays him flat on his back and rests his legs on a bag, about a foot up.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Give water to someone unconscious and he can CHOKE. And splashing water on the face is a no too.",
    "Legs up sends blood back to the brain. Not awake within a minute? Call 112 right away.",
    "The real brave one knows the right first aid. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #22", question=("FRIEND JUST FAINTED!", "WHAT DO YOU DO?"),
           brave="SPLASH WATER + MAKE HIM DRINK", normal="LAY HIM FLAT, LEGS UP", answer='N', grade='warm',
           why_title="SOMEONE FAINTED? DO THIS",
           why_rows=[("Lay flat on the back", WHITE), ("Raise legs ~30 cm", GRN), ("NO water while out", RED),
                     ("No splashing the face", RED), ("Give air, loosen collar", WHITE), ("Not awake in 1 min? 112", YEL)],
           src="SRC: MedlinePlus + St John Ambulance first aid", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

GROUND = 880


def hall(c, t):
    c.rectangle(-400, 0, 1880, GROUND); c.set_source_rgb(0.32, 0.22, 0.42); c.fill()
    # stage banner + bunting
    S.rrect(c, 120, 120, 840, 130, 20); c.set_source_rgb(0.95, 0.75, 0.3); c.fill()
    T(c, "ANNUAL FEST", 540, 210, 64, (0.35, 0.15, 0.3), stroke=None)
    for q in range(30):
        x = -300 + q * 70
        c.move_to(x, 40); c.line_to(x + 35, 95); c.line_to(x + 70, 40)
        c.set_source_rgb(*((0.95, 0.4, 0.35), (0.35, 0.75, 0.95), (0.98, 0.85, 0.3))[q % 3]); c.fill()
    for j in range(6):   # stage lights
        x = 60 + j * 200
        c.arc(x, 300, 22, 0, 2 * math.pi); c.set_source_rgba(1, 0.95, 0.7, 0.6 + 0.3 * math.sin(t * 3 + j)); c.fill()
    # audience silhouettes in the back
    for j in range(14):
        x = -300 + j * 120 + (30 if j % 2 else 0)
        S.rrect(c, x - 45, 640, 90, 120, 40); c.set_source_rgba(0.18, 0.12, 0.25, 0.9); c.fill()
        c.arc(x, 615, 32, 0, 2 * math.pi); c.fill()
    c.rectangle(-400, GROUND, 1880, 220); c.set_source_rgb(0.62, 0.5, 0.42); c.fill()


def victim(c, t, x, legs_up=False, wet=False):
    """friend lying on the floor, head on the left. No injury shown."""
    if legs_up:   # bag under the feet, body tilted so the legs rest ~30 cm up
        S.rrect(c, x + 10, GROUND - 60, 130, 70, 16); c.set_source_rgb(0.2, 0.35, 0.6); c.fill()
    c.save(); c.translate(x - 150, GROUND - 80); c.rotate(-math.pi / 2 - (0.2 if legs_up else 0))
    B.figure(c, 0, 0, 0.28, t, who='bhai', mouth='flat', look=(0, 0), arms=((14, -10), (14, -10)), bob=False)
    c.restore()
    if legs_up:
        T(c, "LEGS ~30 cm UP", x, GROUND - 190, 30, GRN, stroke=None)
    if wet:
        for j in range(6):
            ph = (t * 1.5 + j / 6) % 1
            c.arc(x - 170 + 25 * math.sin(j * 2), GROUND - 140 + ph * 70, 8, 0, 2 * math.pi)
            c.set_source_rgba(0.5, 0.75, 1.0, 1 - ph); c.fill()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 23 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 34, (0.1, 0.1, 0.15), stroke=None)


def bottle(c, x, y, rot=0.0):
    c.save(); c.translate(x, y); c.rotate(rot)
    S.rrect(c, -22, -70, 44, 140, 12); c.set_source_rgba(0.7, 0.9, 1.0, 0.95); c.fill()
    c.rectangle(-12, -92, 24, 24); c.set_source_rgb(0.2, 0.5, 0.95); c.fill()
    c.restore()


def scene(c, side, t, p):
    hall(c, t)
    if side == 'B':
        victim(c, t, 660, wet=p > 0.2)
        q = S.ease(min(1, p / 0.45))
        K.sid(c, t, 300 + 120 * q, 420, 0.42, mouth='o' if p > 0.5 else 'smile', look=(0.8, 0.2),
              arms=((100, 20), (40, -60)), eyes=1.15)
        bottle(c, 470 + 40 * q, 560 + 160 * q, -1.6 * q)
        if p > 0.5:
            S.rrect(c, 330, 350, 420, 56, 20); c.set_source_rgba(*RED, 0.92); c.fill()
            T(c, "HE'S UNCONSCIOUS!", 540, 388, 28, WHITE, stroke=None)
            bubble(c, 540, 250, "DRINK! WAKE UP!", (1, 0.82, 0.8))
        else:
            bubble(c, 540, 250, "WATER ON THE FACE!", (1, 0.85, 0.8))
    else:
        victim(c, t, 640, legs_up=p > 0.3)
        B.figure(c, 300, 420, 0.42, t, who='friend', mouth='flat', look=(0.7, 0.2),
                 arms=((40, 110), (100, 40)) if p > 0.2 else ((100, 20), (100, 20)))
        msg = "LAY HIM FLAT" if p < 0.3 else ("LEGS UP ON THE BAG" if p < 0.65 else "GIVE HIM AIR")
        bubble(c, 540, 250, msg)
        if p > 0.6:
            S.rrect(c, 360, 350, 360, 50, 18); c.set_source_rgba(0.05, 0.4, 0.15, 0.9); c.fill()
            T(c, "BLOOD BACK TO BRAIN", 540, 384, 26, WHITE, stroke=None)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
