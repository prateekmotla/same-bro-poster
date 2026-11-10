"""BRAVE vs NORMAL — WHO'S RIGHT? #6: snake bite on a trek (engine: studio/shorts/dilemma.py).
Fact: WHO snakebite first aid — keep the person calm and still, immobilise the bitten limb, remove rings/watches,
get to a hospital fast (antivenom). Do NOT cut the wound, suck out venom, or apply a tight tourniquet. India ambulance 108/112.
Audio sped 1.1x with atempo (44.6 s take > 40.6 s)."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
from kit import T, S, RED, GRN, WHITE  # noqa: E402
import body as B  # noqa: E402

D = "/home/claude/sid/shorts/s89_snake"
CAPS = [
    "On a trek, a SNAKE bites your friend's leg. Brave: tie it tight and suck the venom out. Normal: keep him still, go to hospital. Whose side are you on?",
    "Brave ties the leg TIGHT with a rope and bends down to suck the venom. Total movie scene.",
    "Normal calms him down, keeps the leg straight and still, and calls 108 for an ambulance right away.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. WHO says: don't CUT the bite, don't SUCK it, don't tie it TIGHT. It doesn't remove venom, it adds damage.",
    "Keep the leg still, take off rings or watch, and get to a hospital with ANTI-VENOM fast.",
    "Don't be the movie hero. The real hero gets him to hospital. What would YOU do first?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #6", question=("SNAKE BITE ON A TREK.", "WHAT DO YOU DO?"),
           brave="TIE TIGHT & SUCK VENOM", normal="KEEP STILL, HOSPITAL", answer='N', grade='studio',
           why_title="SNAKE BITE? DO THIS",
           why_rows=[("NO cutting, NO sucking", RED), ("NO tight tourniquet", RED),
                     ("Keep calm, keep leg still", WHITE), ("Remove rings / watch", WHITE),
                     ("Hospital fast: ANTI-VENOM", GRN)],
           src="SRC: WHO snakebite first aid", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

_V = dict(HAIR=B.S.C('1E1A18'), HAIR_HI=B.S.C('4A3A30'), HOOD=B.S.C('2F7A55'), HOOD_SH=B.S.C('20563B'),
          HOOD_HI=B.S.C('46A070'), HOOD_LN=B.S.C('0E2A1C'))
VX, VY = 650, 300


def _vb(c, x, y, s, t, **kw):
    B.CH._swap(_V); B.S.torso(c, x, y, s, t, **kw); B.CH._swap(B.CH._SID)


def _vh(c, x, y, s, t, **e):
    B.CH._swap(_V); e.setdefault('stubble', 0.3); B.S.head(c, x, y, s, t, **e); B.CH._swap(B.CH._SID)


def victim(c, t, **kw):
    # rock seat
    c.save(); c.translate(VX, VY + 300); c.scale(1, 0.75); c.arc(0, 0, 150, 0, 2 * math.pi); c.restore()
    c.set_source_rgb(0.45, 0.44, 0.42); c.fill()
    fb, fh = B.friend_body, B.friend_head
    B.friend_body, B.friend_head = _vb, _vh
    try:
        B.figure(c, VX, VY, 0.42, t, who='friend', pose='sit', **kw)
    finally:
        B.friend_body, B.friend_head = fb, fh
    # two small bite marks on the right ankle (no blood)
    for dx in (-6, 8):
        c.arc(VX + 52 + dx, VY + 335, 4, 0, 2 * math.pi); c.set_source_rgb(0.35, 0.1, 0.1); c.fill()


def bg(c, t):
    g = cairo.LinearGradient(0, 0, 0, 700)
    g.add_color_stop_rgb(0, 0.62, 0.78, 0.7); g.add_color_stop_rgb(1, 0.8, 0.85, 0.7)
    c.rectangle(-400, 0, 1880, 700); c.set_source(g); c.fill()
    c.rectangle(-400, 160, 1880, 470); c.set_source_rgb(0.24, 0.42, 0.26); c.fill()
    for j, x in enumerate(range(-380, 1500, 130)):
        h = 0.6 + 0.4 * math.sin(j * 1.7)
        c.rectangle(x, 120, 34 + 10 * h, 560); c.set_source_rgb(0.3, 0.22, 0.15); c.fill()
        c.arc(x + 20, 140, 120 + 40 * h, 0, 2 * math.pi); c.set_source_rgb(0.16, 0.36 + 0.06 * h, 0.2); c.fill()
    c.rectangle(-400, 620, 1880, 380); c.set_source_rgb(0.45, 0.36, 0.24); c.fill()
    c.move_to(-400, 700); c.curve_to(200, 640, 800, 760, 1480, 680); c.line_to(1480, 1000); c.line_to(-400, 1000); c.close_path()
    c.set_source_rgb(0.56, 0.45, 0.3); c.fill()
    for x in range(-390, 1480, 40):
        c.move_to(x, 640); c.rel_line_to(5, -20 - 10 * math.sin(x)); c.set_source_rgb(0.25, 0.45, 0.2); c.set_line_width(4); c.stroke()


def snake(c, t, x0, y0, a=1.0):
    c.set_line_cap(1)
    c.move_to(x0, y0)
    for j in range(1, 30):
        c.line_to(x0 + j * 9, y0 + 14 * math.sin(j * 0.5 - t * 8))
    c.set_source_rgba(0.2, 0.42, 0.12, a); c.set_line_width(16); c.stroke()
    c.arc(x0 - 6, y0, 13, 0, 2 * math.pi); c.set_source_rgba(0.16, 0.34, 0.1, a); c.fill()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x + w / 2, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def scene(c, side, t, p):
    bg(c, t)
    if p < 0.15:
        snake(c, t, 760 + 500 * p, 690, 1 - p / 0.15)
    if side == 'B':
        q = S.ease(min(1, p / 0.25))
        victim(c, t, mouth='o', eyes=1.3, sweat=1, angry=0.3)
        if p > 0.12:   # tight rope on the shin
            for j in range(3):
                c.move_to(VX + 22, VY + 285 + j * 12); c.line_to(VX + 84, VY + 289 + j * 12)
                c.set_source_rgb(0.85, 0.15, 0.12); c.set_line_width(7); c.stroke()
        K.sid(c, t, 400 + 30 * q, 255 + 30 * q, 0.42, mouth='o' if p > 0.4 else 'smirk', lean=-18 * q,
              arms=((14, -10), (14 + 60 * q, -10 + 30 * q)), look=(0.6, 0.5))
        if p > 0.3:
            bubble(c, 230, 70, "TIE IT TIGHT!", (1, 0.85, 0.8))
        if p > 0.55:
            bubble(c, 520, 160, "SUCK IT OUT!", (1, 0.82, 0.8))
            S.rrect(c, 800, 330, 100, 100, 18); c.set_source_rgba(1, 0.2, 0.15, 0.9 * (int(t * 4) % 2)); c.fill()
            T(c, "!", 850, 410, 80, WHITE, int(t * 4) % 2, stroke=None)
    else:
        calm = p > 0.15
        victim(c, t, mouth='flat' if calm else 'o', eyes=1.0 if calm else 1.3, sweat=0 if calm else 1)
        if p > 0.35:   # loose splint keeps the leg still
            c.set_line_cap(1)
            c.move_to(VX + 92, VY + 220); c.line_to(VX + 92, VY + 360); c.set_source_rgb(0.5, 0.33, 0.18); c.set_line_width(12); c.stroke()
            for yy in (VY + 250, VY + 330):
                c.move_to(VX + 22, yy); c.line_to(VX + 98, yy); c.set_source_rgba(0.95, 0.95, 0.92, 0.9); c.set_line_width(10); c.stroke()
        calling = p > 0.6
        B.figure(c, 400, 255, 0.42, t, who='friend', mouth='o' if calling else 'flat',
                 arms=((14, -10), (40, 110)) if calling else ((14, -10), (100, 40)), phone=1 if calling else None,
                 glow=0.6 if calling else 0.0, look=(0.6, 0.3))
        if calm and p < 0.6:
            bubble(c, 230, 70, "STAY CALM. DON'T MOVE.")
        if calling:
            bubble(c, 230, 70, "CALLING 108...")
        if p > 0.35:
            T(c, "LEG STILL", VX + 100, VY + 430, 40, (1, 0.95, 0.4))


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
