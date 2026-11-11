"""BRAVE vs NORMAL — WHO'S RIGHT? #14: street dog's small scratch (engine: studio/shorts/dilemma.py).
Fact: WHO rabies fact sheet - first aid after a possible exposure is immediate, extensive washing and flushing of the
wound with soap and water for at least 15 minutes; category II exposure (minor scratches/abrasions without bleeding)
needs immediate vaccination (PEP). Once clinical symptoms appear rabies is virtually 100% fatal; timely PEP prevents it.
India: anti-rabies vaccine at government hospitals. No injury shown: tiny scratch mark only; Brave ends on WRONG."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c110_dogscratch"
CAPS = [
    "A street dog swiped at you, just a tiny scratch. Brave: nothing happened, let's go. Normal: wait, wash it first. Whose side are you on?",
    "Brave rubs some spit on the scratch and says: this happens every day.",
    "Normal opens the tap and starts washing the wound with soap and water, a full 15 minutes.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. WHO says even a small scratch from a rabid animal is risky, and once rabies symptoms start, survival is almost impossible.",
    "Wash with soap and water for 15 minutes, then hospital the SAME day for the anti-rabies vaccine. Vaccine on time = fully safe.",
    "Small scratch, big risk. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #14", question=("DOG SCRATCHED YOU", "TINY SCRATCH. NOW WHAT?"),
           brave="IGNORE IT, WALK ON", normal="WASH 15 MIN + VACCINE", answer='N', grade='warm',
           why_title="DOG SCRATCH? DO THIS",
           why_rows=[("Wash: soap + running water", WHITE), ("Keep washing for 15 MINUTES", YEL),
                     ("Hospital the SAME day", WHITE), ("Get the anti-rabies vaccine", GRN),
                     ("Never: spit, chilli, ignore", RED)],
           src="SRC: WHO rabies fact sheet", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

FLOOR = 880


def street(c, t):
    c.rectangle(-400, 0, 1880, FLOOR); c.set_source_rgb(0.86, 0.78, 0.66); c.fill()       # wall
    for j in range(-4, 16):
        for r in range(9):
            c.rectangle(j * 120 + (60 if r % 2 else 0), r * 98, 116, 94)
    c.set_source_rgba(0.6, 0.5, 0.42, 0.18); c.set_line_width(3); c.stroke()
    c.rectangle(-400, FLOOR, 1880, 200); c.set_source_rgb(0.42, 0.42, 0.45); c.fill()      # road
    c.rectangle(-400, FLOOR, 1880, 14); c.set_source_rgb(0.7, 0.7, 0.72); c.fill()
    # tap + basin (right)
    c.rectangle(880, 520, 26, 120); c.set_source_rgb(0.65, 0.67, 0.7); c.fill()
    c.rectangle(880, 520, 90, 22); c.fill()
    S.rrect(c, 820, 700, 230, 60, 14); c.set_source_rgb(0.85, 0.87, 0.9); c.fill()


def dog(c, x, y, s=1.0):
    """Calm cartoon street dog sitting, facing left (no aggression shown)."""
    c.save(); c.translate(x, y); c.scale(s, s)
    col, dark = (0.78, 0.55, 0.3), (0.55, 0.36, 0.18)
    c.save(); c.scale(1.0, 0.8); c.arc(0, 0, 60, 0, 2 * math.pi); c.restore(); c.set_source_rgb(*col); c.fill()  # body
    c.arc(-55, -60, 38, 0, 2 * math.pi); c.fill()                                                                 # head
    c.save(); c.translate(-92, -52); c.scale(1.2, 0.8); c.arc(0, 0, 18, 0, 2 * math.pi); c.restore(); c.fill()   # snout
    c.arc(-108, -56, 7, 0, 2 * math.pi); c.set_source_rgb(0.1, 0.1, 0.1); c.fill()
    c.arc(-62, -70, 5, 0, 2 * math.pi); c.fill()
    c.move_to(-40, -92); c.line_to(-22, -118); c.line_to(-20, -80); c.close_path(); c.set_source_rgb(*dark); c.fill()
    for dx in (-35, 15):
        c.rectangle(dx, 30, 18, 46); c.set_source_rgb(*col); c.fill()
    c.move_to(55, 0); c.curve_to(95, -20, 100, -60, 85, -80); c.set_source_rgb(*col); c.set_line_width(12); c.stroke()
    c.restore()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def scratch(c, x, y):
    for j in range(3):
        c.move_to(x - 16 + j * 10, y - 12); c.line_to(x - 6 + j * 10, y + 12)
    c.set_source_rgba(0.85, 0.35, 0.35, 0.85); c.set_line_width(3); c.stroke()


def scene(c, side, t, p):
    street(c, t)
    dog(c, 150 if side == 'B' else 120, 800, 0.75)
    if side == 'B':
        q = S.ease(min(1, p / 0.6))
        x = 430 + 80 * q
        K.sid(c, t, x, 455, 0.42, mouth='smirk', look=(0.6, 0), arms=((14, -10), (100, 40)))
        scratch(c, x + 95, 560)
        bubble(c, 540, 250, "IT'S NOTHING, CHAL!" if p < 0.5 else "HAPPENS EVERY DAY", (1, 0.85, 0.8))
        if p > 0.55:
            S.rrect(c, 560, 680, 330, 56, 20); c.set_source_rgba(*RED, 0.92); c.fill()
            T(c, "NO WASH. NO DOCTOR.", 725, 718, 28, WHITE, stroke=None)
    else:
        B.figure(c, 690, 455, 0.42, t, who='friend', mouth='flat', arms=((150, 30), (60, 60)), look=(0.3, 0.4))
        if p > 0.12:   # water stream + soap bubbles
            c.rectangle(954, 542, 12, 150); c.set_source_rgba(0.55, 0.8, 1.0, 0.8); c.fill()
            for j in range(6):
                bx = 880 + 30 * math.sin(t * 3 + j * 1.3) + j * 14
                by = 660 - ((t * 40 + j * 25) % 120)
                c.arc(bx, by, 10 + (j % 3) * 4, 0, 2 * math.pi); c.set_source_rgba(1, 1, 1, 0.75); c.fill()
        mins = int(15 * S.ease(min(1, p / 0.9)))
        S.rrect(c, 380, 140, 260, 90, 30); c.set_source_rgba(0.05, 0.35, 0.15, 0.92); c.fill()
        T(c, f"{mins:02d}:00 / 15:00", 510, 200, 34, WHITE, stroke=None)
        bubble(c, 540, 250, "WAIT, WASH IT FIRST" if p < 0.2 else "SOAP + WATER, 15 MIN")


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
