"""BRAVE vs NORMAL — WHO'S RIGHT? #16: robbed at knifepoint (engine: studio/shorts/dilemma.py).
Fact: police robbery-safety advice (Arlington County Police, Virginia): "Don't resist. The suspect wants your valuables,
not you. Things can always be replaced, but you can't." If the suspect indicates a weapon, assume it is true; notice
details; report to police immediately. India: emergency 112 (ERSS); then block phone/cards. Voice take sped 1.05x.
Brand-safe: robber is a faceless cartoon silhouette, small knife, no contact or injury shown; Brave freezes mid-step,
then the red WRONG freeze."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c118_knife"
CAPS = [
    "Empty lane at night. A guy shows a KNIFE and asks for your phone and wallet. Brave: I'll fight him. Normal: just give it. Whose side are you on?",
    "Brave clenches his fists and steps forward to take him on.",
    "Normal slowly puts the phone and wallet down, shows his hands and steps back.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Police advice is clear: don't resist. He wants your stuff, not you. Stuff can be replaced. You can't.",
    "Remember his face, clothes, which way he ran. Get somewhere safe, call 112, then block your phone and cards.",
    "The real hero is the one who gets home safe. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #16", question=("ROBBED AT KNIFEPOINT!", "WHAT DO YOU DO?"),
           brave="FIGHT HIM", normal="HAND IT OVER", answer='N', grade='studio',
           why_title="FACING A WEAPON?",
           why_rows=[("DON'T resist, don't chase", RED), ("Hand over the stuff, step back", WHITE),
                     ("Note face, clothes, direction", WHITE), ("Safe spot, call 112", WHITE),
                     ("Block phone + cards", GRN)],
           src="SRC: police robbery-safety advice", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

FLOOR = 900


def lane(c, t):
    c.rectangle(-400, 0, 1880, FLOOR); c.set_source_rgb(0.2, 0.22, 0.32); c.fill()        # night wall
    for j in range(-4, 16):
        for r in range(10):
            c.rectangle(j * 120 + (60 if r % 2 else 0), r * 98, 116, 94)
    c.set_source_rgba(0.1, 0.1, 0.18, 0.5); c.set_line_width(3); c.stroke()
    # lamp glow
    for r, a in ((380, 0.08), (220, 0.12), (90, 0.25)):
        c.arc(560, 120, r, 0, 2 * math.pi); c.set_source_rgba(1, 0.85, 0.5, a); c.fill()
    c.rectangle(548, 120, 24, 40); c.set_source_rgb(0.15, 0.15, 0.18); c.fill()
    c.rectangle(-400, FLOOR, 1880, 200); c.set_source_rgb(0.25, 0.25, 0.28); c.fill()       # road
    c.rectangle(-400, FLOOR, 1880, 12); c.set_source_rgb(0.45, 0.45, 0.5); c.fill()


def robber(c, t, x):
    """Faceless dark hooded silhouette holding a small knife toward the left (no contact)."""
    y = 455; s = 0.42
    dk = (0.06, 0.06, 0.09)
    c.set_source_rgb(*dk)
    for lx in (-40, 40):   # legs
        S.rrect(c, x + lx - 22, y + 150, 44, 300, 18); c.fill()
    S.rrect(c, x - 95, y + 30, 190, 210, 50); c.fill()   # torso
    c.arc(x, y - 10, 78, 0, 2 * math.pi); c.fill()       # hood
    c.arc(x - 6, y - 4, 52, 0, 2 * math.pi); c.set_source_rgb(0.12, 0.12, 0.16); c.fill()   # face shadow
    # arm to the left holding the knife
    c.move_to(x - 70, y + 80); c.line_to(x - 175, y + 120)
    c.set_source_rgb(*dk); c.set_line_width(40); c.set_line_cap(1); c.stroke()
    c.rectangle(x - 215, y + 108, 30, 22); c.set_source_rgb(0.25, 0.2, 0.15); c.fill()   # handle
    c.move_to(x - 215, y + 110); c.line_to(x - 275, y + 119); c.line_to(x - 215, y + 128); c.close_path()
    c.set_source_rgb(0.82, 0.84, 0.88); c.fill()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 23 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 34, (0.1, 0.1, 0.15), stroke=None)


def loot(c, x):
    S.rrect(c, x - 70, FLOOR - 30, 54, 26, 6); c.set_source_rgb(0.1, 0.1, 0.12); c.fill()          # phone flat
    S.rrect(c, x + 5, FLOOR - 40, 70, 40, 8); c.set_source_rgb(0.45, 0.28, 0.15); c.fill()         # wallet


def scene(c, side, t, p):
    lane(c, t)
    robber(c, t, 800)
    if side == 'B':
        q = S.ease(min(1, p / 0.5))
        x = 290 + 70 * q
        K.sid(c, t, x, 455, 0.42, mouth='o' if p > 0.55 else 'flat', look=(0.8, 0),
              arms=((100, 20), (100, 20)), eyes=1.2 if p > 0.55 else 1.0)
        if p > 0.55:
            S.rrect(c, 250, 700, 360, 56, 20); c.set_source_rgba(*RED, 0.92); c.fill()
            T(c, "FISTS vs A KNIFE?!", 430, 738, 28, WHITE, stroke=None)
            bubble(c, 540, 250, "WAIT... HE HAS A KNIFE", (1, 0.82, 0.8))
        else:
            bubble(c, 540, 250, "I'LL FIGHT HIM!", (1, 0.85, 0.8))
    else:
        back = S.ease(max(0, min(1, (p - 0.55) / 0.35)))
        x = 380 - 90 * back
        if p > 0.3:
            loot(c, 520)
        hands = ((40, -150), (40, -150)) if p > 0.3 else ((100, 60), (100, 60))
        B.figure(c, x, 455, 0.42, t, who='friend', mouth='flat', arms=hands, look=(0.7, 0))
        if p > 0.55:
            S.rrect(c, 160, 700, 300, 50, 18); c.set_source_rgba(0.05, 0.4, 0.15, 0.9); c.fill()
            T(c, "STEPPING BACK", 310, 734, 26, WHITE, stroke=None)
        msg = "OKAY, OKAY. TAKE IT." if p < 0.55 else "PHONE GONE. I'M SAFE."
        bubble(c, 540, 250, msg)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
