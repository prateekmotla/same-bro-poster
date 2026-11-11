"""BRAVE vs NORMAL — WHO'S RIGHT? #17: friend has heatstroke after cricket (engine: studio/shorts/dilemma.py).
Facts: heatstroke = medical emergency, call an ambulance (108/112 in India). HealthLink BC 'Emergency First Aid for
Heatstroke': move to a cool place out of the sun, remove extra clothing, sponge/spray with cool water + fan, ice packs
on neck, groin, armpits; "If the person is awake and alert enough to swallow, give the person fluids" — "most people
with heatstroke have an altered level of consciousness and cannot safely be given fluids". MedlinePlus 'Heat
emergencies': cool wet cloths + fan, cold compresses on neck/groin/armpits; nothing by mouth if vomiting/unconscious,
sips only if alert. NDMA heat-wave guidance: move to shade, cool the body, get medical help.
Brand-safe: no injury; Brave freezes holding the bottle, then the red WRONG freeze. Voice take sped 1.07x."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c122_heatstroke"
CAPS = [
    "May afternoon, after cricket a friend COLLAPSES. Body burning hot, talking nonsense. Brave: give him cold water. Normal: get him to the shade first. You?",
    "Brave grabs an ice-cold bottle and starts forcing it into his mouth.",
    "Normal takes him to the shade, calls 108, loosens his clothes, wet cloth and air.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. This is HEATSTROKE, an emergency. Force water on someone not fully conscious and he can CHOKE.",
    "Cool the body first: wet cloth, air, cold packs on neck and armpits. Only if he's alert, small sips of water.",
    "The real hero knows the right first aid. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #17", question=("FRIEND HAS HEATSTROKE!", "WHAT DO YOU DO?"),
           brave="FORCE ICE WATER", normal="SHADE + COOL + 108", answer='N', grade='warm',
           why_title="HEATSTROKE? DO THIS",
           why_rows=[("Call 108 / 112 first", WHITE), ("Shade, loosen clothes", WHITE), ("Wet cloth + fan him", WHITE),
                     ("Cold packs: neck, armpits", WHITE), ("Not alert? NO water", RED), ("Alert? Small sips only", GRN)],
           src="SRC: heatstroke first aid (HealthLink BC, MedlinePlus)", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

GROUND = 880


def ground(c, t, shade):
    g = c  # sky + sun
    c.rectangle(-400, 0, 1880, GROUND); c.set_source_rgb(0.98, 0.86, 0.6); c.fill()
    for r, a in ((260, 0.15), (170, 0.25), (95, 1.0)):
        c.arc(1250, 140, r, 0, 2 * math.pi); c.set_source_rgba(1, 0.75 + 0.2 * (r < 100), 0.3, a); c.fill()
    for j in range(5):   # heat shimmer lines
        y = 380 + j * 60 + 6 * math.sin(t * 3 + j)
        c.move_to(-300, y)
        for x in range(-300, 1500, 60):
            c.line_to(x, y + 8 * math.sin(x / 40 + t * 4 + j))
        c.set_source_rgba(1, 1, 1, 0.12); c.set_line_width(4); c.stroke()
    c.rectangle(-400, GROUND, 1880, 220); c.set_source_rgb(0.72, 0.58, 0.36); c.fill()       # dusty ground
    # stumps far left
    for j in range(3):
        c.rectangle(-180 + j * 26, 700, 12, 180); c.set_source_rgb(0.95, 0.92, 0.85); c.fill()
    if shade:
        # big neem tree with shade
        c.save(); c.scale(1, 0.18); c.arc(470, GROUND / 0.18 + 120, 420, 0, 2 * math.pi); c.restore()
        c.set_source_rgba(0, 0, 0, 0.22); c.fill()
        c.rectangle(690, 250, 60, GROUND - 250); c.set_source_rgb(0.45, 0.3, 0.18); c.fill()
        for cx, cy, r in ((720, 200, 190), (560, 260, 150), (880, 260, 150), (720, 330, 150)):
            c.arc(cx, cy, r, 0, 2 * math.pi); c.set_source_rgb(0.22, 0.48, 0.24); c.fill()
        c.rectangle(-400, 0, 1880, 1100); c.set_source_rgba(0.1, 0.2, 0.3, 0.12); c.fill()


def victim(c, t, x, cool=False):
    """friend lying on the ground (heat), head on the left; sweat drops unless cooled. No injury shown."""
    c.save(); c.translate(x - 150, GROUND - 80); c.rotate(-math.pi / 2)
    B.figure(c, 0, 0, 0.28, t, who='bhai', mouth='flat', look=(0, 0), arms=((14, -10), (14, -10)), bob=False)
    c.restore()
    hx, hy = x - 150, GROUND - 80
    if not cool:
        for j in range(3):
            ph = (t * 0.8 + j / 3) % 1
            c.arc(hx - 40 + j * 50, hy - 70 - ph * 50, 9, 0, 2 * math.pi); c.set_source_rgba(0.5, 0.75, 1.0, 1 - ph); c.fill()
        T(c, "BURNING HOT", x, GROUND - 170, 32, RED, stroke=None)
    else:
        S.rrect(c, hx - 60, hy - 30, 40, 60, 10); c.set_source_rgba(0.6, 0.85, 1.0, 0.9); c.fill()   # wet cloth


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 23 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 34, (0.1, 0.1, 0.15), stroke=None)


def bottle(c, x, y, rot=0.0):
    c.save(); c.translate(x, y); c.rotate(rot)
    S.rrect(c, -22, -70, 44, 140, 12); c.set_source_rgba(0.7, 0.9, 1.0, 0.95); c.fill()
    c.rectangle(-12, -92, 24, 24); c.set_source_rgb(0.2, 0.5, 0.95); c.fill()
    for j in range(3):
        c.move_to(-14, -40 + j * 30); c.line_to(14, -30 + j * 30)
    c.set_source_rgba(1, 1, 1, 0.8); c.set_line_width(3); c.stroke()
    c.restore()


def scene(c, side, t, p):
    if side == 'B':
        ground(c, t, shade=False)
        victim(c, t, 660)
        q = S.ease(min(1, p / 0.45))
        K.sid(c, t, 300 + 120 * q, 420, 0.42, mouth='o' if p > 0.5 else 'smile', look=(0.8, 0.2),
              arms=((100, 20), (40, -60)), eyes=1.15)
        bottle(c, 470 + 40 * q, 560 + 160 * q, -1.6 * q)
        if p > 0.5:
            S.rrect(c, 330, 350, 420, 56, 20); c.set_source_rgba(*RED, 0.92); c.fill()
            T(c, "HE'S NOT EVEN ALERT!", 540, 388, 28, WHITE, stroke=None)
            bubble(c, 540, 250, "DRINK! DRINK FAST!", (1, 0.82, 0.8))
        else:
            bubble(c, 540, 250, "ICE WATER, BRO!", (1, 0.85, 0.8))
    else:
        ground(c, t, shade=True)
        moved = p > 0.2
        vx = 600 if moved else 940
        victim(c, t, vx, cool=p > 0.55)
        B.figure(c, 300, 420, 0.42, t, who='friend', mouth='flat', look=(0.7, 0.2),
                 arms=((40, 110), (100, 40)) if p > 0.3 else ((100, 20), (100, 20)),
                 phone=1 if 0.3 < p < 0.6 else None)
        if p > 0.6:   # fanning
            sw = 0.4 * math.sin(t * 14)
            c.save(); c.translate(420, 560); c.rotate(sw)
            S.rrect(c, -10, -90, 20, 90, 6); c.set_source_rgb(0.95, 0.95, 0.9); c.fill()
            c.restore()
            for j in range(3):
                c.move_to(450, 520 + j * 30); c.rel_curve_to(30, -10, 50, 10, 80, 0)
            c.set_source_rgba(1, 1, 1, 0.7); c.set_line_width(4); c.stroke()
        msg = "TO THE SHADE" if p < 0.3 else ("CALLING 108" if p < 0.6 else "COOL HIM DOWN")
        bubble(c, 540, 250, msg)
        if p > 0.6:
            S.rrect(c, 390, 350, 300, 50, 18); c.set_source_rgba(0.05, 0.4, 0.15, 0.9); c.fill()
            T(c, "COOLING DOWN", 540, 384, 26, WHITE, stroke=None)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
