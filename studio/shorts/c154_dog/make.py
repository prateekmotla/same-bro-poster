"""BRAVE vs NORMAL — WHO'S RIGHT? #25: an unknown dog comes barking at you in the gali (engine: studio/shorts/dilemma.py).
Facts: US CDC 'Staying Safe Around Dogs' (reviewed Aug 2026): do not approach an unfamiliar dog, remain motionless if
one approaches you, avoid direct eye contact. Running = the dog chases (dogs chase what runs; standard dog-bite
prevention advice). If bitten: wash the wound with soap and running water for ~15 minutes and see a doctor the same
day (WHO rabies first aid; anti-rabies care). Brand-safe: no bite shown; Brave just runs with the dog behind him,
then the red WRONG freeze. Cartoon street dog of our own design."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c154_dog"
CAPS = [
    "In the gali an unknown dog comes BARKING at you. Brave: RUN! Normal: stop, don't move at all. You?",
    "Brave runs, and the dog runs right behind him.",
    "Normal stays put. Hands by his side, no staring into its eyes.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. US CDC: if an unknown dog comes close, stay STILL,",
    "and avoid direct eye contact. Run, and it will chase you.",
    "And if it bites: wash with soap and water for 15 minutes and see a doctor the SAME day.",
    "Real brave = doing it right. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6, 7], end=[8])
CFG = dict(series="BRAVE vs NORMAL #25", question=("DOG CHARGING AT YOU!", "WHAT DO YOU DO?"),
           brave="RUN!", normal="STAND STILL", answer='N', grade='warm',
           why_title="DOG COMING AT YOU?",
           why_rows=[("Stand still, don't run", GRN), ("Hands by your side", WHITE), ("No direct eye contact", WHITE),
                     ("Running = it chases", RED), ("Bitten? Soap + water 15 min", YEL), ("Doctor the same day", YEL)],
           src="SRC: US CDC 'Staying Safe Around Dogs' + WHO", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

GROUND = 880


def gali(c, t):
    c.rectangle(-400, 0, 1880, GROUND); c.set_source_rgb(0.98, 0.85, 0.62); c.fill()
    cols = [(0.85, 0.55, 0.45), (0.6, 0.75, 0.85), (0.92, 0.8, 0.45), (0.7, 0.82, 0.62)]
    for j in range(7):              # house fronts
        x = -400 + j * 280
        c.rectangle(x, 120, 270, GROUND - 120); c.set_source_rgb(*cols[j % 4]); c.fill()
        S.rrect(c, x + 40, 220, 80, 100, 8); c.set_source_rgb(0.3, 0.35, 0.45); c.fill()
        S.rrect(c, x + 150, 220, 80, 100, 8); c.fill()
        S.rrect(c, x + 90, 560, 100, GROUND - 560, 8); c.set_source_rgb(0.45, 0.3, 0.2); c.fill()
    for j in range(20):             # wires
        pass
    c.move_to(-400, 100); c.curve_to(200, 160, 800, 60, 1480, 120); c.set_source_rgb(0.15, 0.15, 0.15)
    c.set_line_width(4); c.stroke()
    c.rectangle(-400, GROUND, 1880, 220); c.set_source_rgb(0.55, 0.53, 0.5); c.fill()


def dog(c, t, x, bark=True, run=0.0, face=-1):
    """simple cartoon street dog; face=-1 looks left."""
    c.save(); c.translate(x, GROUND - 100); c.scale(face, 1)
    leg = 18 * math.sin(t * 18) * run
    c.set_source_rgb(0.72, 0.5, 0.3)
    for lx, ph in ((-60, 1), (-30, -1), (40, 1), (70, -1)):
        S.rrect(c, lx + leg * ph * 0.5, 20, 20, 80, 8); c.fill()
    S.rrect(c, -90, -40, 190, 80, 38); c.fill()                        # body
    c.move_to(-85, -20); c.line_to(-140, -60 + 8 * math.sin(t * 10)); c.set_line_width(12); c.stroke()  # tail
    c.arc(120, -60, 44, 0, 2 * math.pi); c.fill()                      # head
    S.rrect(c, 140, -60, 60, 36, 14); c.fill()                         # snout
    c.set_source_rgb(0.55, 0.35, 0.2)
    c.move_to(95, -95); c.line_to(105, -130); c.line_to(125, -98); c.fill()   # ear
    c.arc(132, -70, 7, 0, 2 * math.pi); c.set_source_rgb(0.08, 0.08, 0.1); c.fill()
    c.arc(198, -50, 8, 0, 2 * math.pi); c.fill()
    c.restore()
    if bark and int(t * 4) % 2 == 0:
        T(c, "WOOF!", x + (-120 if face < 0 else 120), GROUND - 240, 40, (0.6, 0.15, 0.1), stroke=None)


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 23 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 34, (0.1, 0.1, 0.15), stroke=None)


def scene(c, side, t, p):
    gali(c, t)
    if side == 'B':
        q = S.ease(min(1, p / 0.9))
        sx = 420 - 110 * q
        K.sid(c, t, sx, 400, 0.42, mouth='o' if p > 0.15 else 'flat', look=(-0.8 if p > 0.1 else 0.8, 0),
              arms=((60 + 40 * math.sin(t * 14), 30), (60 - 40 * math.sin(t * 14), 30)), eyes=1.15)
        dog(c, t, 880 - 280 * q, run=1.0 if p > 0.05 else 0.3)
        bubble(c, 540, 230, "RUN!!", (1, 0.85, 0.8))
        if p > 0.45:
            S.rrect(c, 330, 330, 420, 56, 20); c.set_source_rgba(*RED, 0.92); c.fill()
            T(c, "DOG CHASES HIM!", 540, 368, 30, WHITE, stroke=None)
    else:
        q = S.ease(min(1, p / 0.5))
        B.figure(c, 330, 400, 0.42, t, who='friend', mouth='flat', look=(0.0, 0.5), arms=((14, -10), (14, -10)))
        dog(c, t, 900 - 220 * q, bark=p < 0.6, run=1.0 - q)
        msg = "STAND STILL" if p < 0.35 else ("HANDS BY YOUR SIDE" if p < 0.7 else "NO EYE CONTACT")
        bubble(c, 540, 230, msg)
        if p > 0.55:
            S.rrect(c, 380, 330, 320, 50, 18); c.set_source_rgba(0.05, 0.4, 0.15, 0.9); c.fill()
            T(c, "CALM + STILL", 540, 364, 26, WHITE, stroke=None)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
