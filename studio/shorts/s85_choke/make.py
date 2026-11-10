"""BRAVE vs NORMAL — WHO'S RIGHT? #5: friend choking at a cafe (engine: studio/shorts/dilemma.py).
Fact: Red Cross adult choking first aid — if the person can't cough, speak or breathe: 5 back blows between the
shoulder blades, then 5 abdominal thrusts, repeat until the object comes out; call 112. Water can't clear a blocked airway."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
from kit import T, S, RED, GRN, WHITE  # noqa: E402
import body as B  # noqa: E402

D = "/home/claude/sid/shorts/s85_choke"
CAPS = [
    "Friend is CHOKING while eating, can't even speak. Brave: give him water. Normal: hit his back hard. Whose side are you on?",
    "Brave quickly puts a water bottle to his mouth. But his airway is BLOCKED. Where will the water go?",
    "Normal bends him forward and gives 5 hard BACK BLOWS between the shoulder blades.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Red Cross rule: 5 BACK BLOWS, then 5 ABDOMINAL THRUSTS. Until the object comes out.",
    "If the airway is blocked, water clears nothing, it can make it worse. And call 112 right away.",
    "Learn these 2 moves, you could save a life. What would YOU do first?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #5", question=("FRIEND IS CHOKING.", "WHAT DO YOU DO?"),
           brave="GIVE HIM WATER", normal="5 HARD BACK BLOWS", answer='N', grade='studio',
           why_title="CHOKING? DO THIS",
           why_rows=[("Can't speak = airway blocked", RED), ("Water can't clear it", WHITE),
                     ("5 BACK BLOWS (shoulders)", WHITE), ("5 ABDOMINAL THRUSTS", WHITE),
                     ("Repeat till out. Call 112.", GRN)],
           src="SRC: Red Cross first aid (adult choking)", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

SKIN = (0.66, 0.43, 0.29)
_V = dict(HAIR=B.S.C('1E1A18'), HAIR_HI=B.S.C('4A3A30'), HOOD=B.S.C('2F7A55'), HOOD_SH=B.S.C('20563B'),
          HOOD_HI=B.S.C('46A070'), HOOD_LN=B.S.C('0E2A1C'))


def _vb(c, x, y, s, t, **kw):
    B.CH._swap(_V); B.S.torso(c, x, y, s, t, **kw); B.CH._swap(B.CH._SID)


def _vh(c, x, y, s, t, **e):
    B.CH._swap(_V); e.setdefault('stubble', 0.3); B.S.head(c, x, y, s, t, **e); B.CH._swap(B.CH._SID)


def victim(c, t, x, y, s=0.42, lean=0.0, throat=True, **kw):
    fb, fh = B.friend_body, B.friend_head
    B.friend_body, B.friend_head = _vb, _vh
    try:
        B.figure(c, x, y, s, t, who='friend', arms=((-20, 160), (-20, 160)) if throat else ((14, -10), (14, -10)),
                 lean=lean, **kw)
    finally:
        B.friend_body, B.friend_head = fb, fh
    if throat:   # both hands clutching the throat (universal choking sign)
        nx = x
        for dx in (-16, 16):
            c.arc(nx + dx * s / 0.42, y + 72 * s / 0.42, 15 * s / 0.42, 0, 2 * math.pi); c.set_source_rgb(*SKIN); c.fill()


def bg(c, t):
    g = cairo.LinearGradient(0, 0, 0, 700)
    g.add_color_stop_rgb(0, 0.86, 0.72, 0.55); g.add_color_stop_rgb(1, 0.72, 0.55, 0.4)
    c.rectangle(-400, 0, 1880, 700); c.set_source(g); c.fill()
    # wood panel lower wall
    c.rectangle(-400, 470, 1880, 230); c.set_source_rgb(0.45, 0.28, 0.17); c.fill()
    for x in range(-400, 1480, 90):
        c.rectangle(x, 470, 4, 230); c.set_source_rgba(0, 0, 0, 0.2); c.fill()
    # window with city
    S.rrect(c, 860, 90, 420, 300, 12); c.set_source_rgb(0.3, 0.25, 0.2); c.fill()
    c.rectangle(875, 105, 390, 270); c.set_source_rgb(0.62, 0.8, 0.95); c.fill()
    for j, (bx, bh) in enumerate(((880, 150), (950, 210), (1040, 120), (1110, 190), (1190, 160))):
        c.rectangle(bx, 375 - bh, 70, bh); c.set_source_rgb(0.5, 0.58, 0.68); c.fill()
    c.rectangle(1065, 105, 10, 270); c.set_source_rgb(0.3, 0.25, 0.2); c.fill()
    # menu board
    S.rrect(c, -320, 110, 360, 250, 14); c.set_source_rgb(0.12, 0.14, 0.13); c.fill()
    T(c, "MENU", -140, 170, 40, (0.95, 0.9, 0.7), stroke=None)
    for j, it in enumerate(("CHAI  20", "SAMOSA  15", "MAGGI  40")):
        T(c, it, -140, 225 + j * 42, 26, (0.9, 0.9, 0.85), stroke=None, bold=False)
    # pendant lamps
    for lx in (200, 760):
        c.move_to(lx, 0); c.line_to(lx, 70); c.set_source_rgb(0.1, 0.1, 0.1); c.set_line_width(3); c.stroke()
        c.move_to(lx - 40, 110); c.line_to(lx - 20, 70); c.line_to(lx + 20, 70); c.line_to(lx + 40, 110); c.close_path()
        c.set_source_rgb(0.15, 0.15, 0.15); c.fill()
        c.arc(lx, 112, 12, 0, math.pi); c.set_source_rgb(1, 0.92, 0.6); c.fill()
    # floor
    c.rectangle(-400, 690, 1880, 310); c.set_source_rgb(0.33, 0.27, 0.24); c.fill()
    for x in range(-400, 1480, 120):
        c.move_to(x, 690); c.line_to(x - 80, 1000); c.set_source_rgba(0, 0, 0, 0.15); c.set_line_width(3); c.stroke()
    # table with plate on the far right
    c.rectangle(1000, 520, 380, 22); c.set_source_rgb(0.55, 0.35, 0.2); c.fill()
    c.rectangle(1170, 542, 26, 150); c.fill()
    c.save(); c.translate(1120, 512); c.scale(1, 0.3); c.arc(0, 0, 60, 0, 2 * math.pi); c.restore()
    c.set_source_rgb(0.96, 0.96, 0.94); c.fill()
    c.save(); c.translate(1260, 500); c.rectangle(-18, -30, 36, 34); c.restore(); c.set_source_rgb(0.95, 0.85, 0.7); c.fill()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x + w / 2, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def bottle(c, x, y, ang, fill=0.7):
    c.save(); c.translate(x, y); c.rotate(ang)
    S.rrect(c, -22, -70, 44, 120, 12); c.set_source_rgba(0.75, 0.9, 1, 0.85); c.fill()
    c.rectangle(-20, -70 + 120 * (1 - fill), 40, 120 * fill - 2); c.set_source_rgba(0.35, 0.65, 0.95, 0.6); c.fill()
    c.rectangle(-10, -92, 20, 24); c.set_source_rgb(0.2, 0.45, 0.9); c.fill()
    c.restore()


def scene(c, side, t, p):
    bg(c, t)
    shake = 4 * math.sin(t * 40)
    vx, vy = 660, 255
    if side == 'B':
        if p < 0.12:
            victim(c, t, vx + shake, vy, mouth='o', eyes=1.3, sweat=1, angry=0.4)
            K.sid(c, t, 380, vy, 0.42, mouth='o', eyes=1.2, look=(0.6, 0))
            bottle(c, 470, 470, 0)
        else:
            q = S.ease(min(1, (p - 0.12) / 0.25))
            victim(c, t, vx + shake, vy, mouth='o', eyes=1.3, sweat=1, angry=0.5, tilt=-6 * q)
            K.sid(c, t, 380 + 60 * q, vy, 0.42, mouth='smirk' if p < 0.5 else 'o', eyes=1.0 if p < 0.5 else 1.3,
                  arms=((14, -10), (14 + 76 * q, -10 + 10 * q)), look=(0.6, 0), lean=-4 * q)
            bx, by = 470 + (vx - 60 - 470) * q, 470 + (vy + 70 - 470) * q
            bottle(c, bx, by, -1.9 * q, 0.7 - 0.3 * max(0, p - 0.35))
            if p > 0.35:   # water just spills down
                for j in range(9):
                    yy = vy + 90 + ((t * 260 + j * 41) % 260)
                    c.arc(vx - 30 + 8 * math.sin(j * 3.1), yy, 7, 0, 2 * math.pi)
                    c.set_source_rgba(0.45, 0.75, 1, 0.8); c.fill()
            if p > 0.5:
                bubble(c, 300, 70, "AIRWAY BLOCKED!", (1, 0.82, 0.8))
                S.rrect(c, 790, 200, 100, 100, 18); c.set_source_rgba(1, 0.2, 0.15, 0.9 * (int(t * 4) % 2)); c.fill()
                T(c, "!", 840, 280, 80, WHITE, int(t * 4) % 2, stroke=None)
    else:
        q = S.ease(min(1, p / 0.18))
        ld = 14 * q
        out = p > 0.84
        victim(c, t, vx + 60 * q + (shake if not out else 0), vy + 15 * q, lean=ld, throat=not out,
               mouth='smile' if out else 'o', eyes=1.0 if out else 1.3, sweat=0 if out else 1)
        hit = 0
        if 0.2 < p < 0.84:
            ph = (p - 0.2) / 0.64 * 5
            hit = int(ph) + 1
            sw = ph % 1
            arm = ((14, -10), (110 - 60 * min(1, sw * 3), 30)) if sw < 0.35 else ((14, -10), (110, 40))
        else:
            arm = ((14, -10), (14, -10))
        B.figure(c, 470 + 40 * q, 255, 0.42, t, who='friend', mouth='flat', angry=0.3, arms=arm, look=(0.6, 0.2))
        if hit:
            sw = ((p - 0.2) / 0.64 * 5) % 1
            hx, hy = vx - 40, vy + 130
            if sw < 0.4:
                for r in range(8):
                    a = r / 8 * 2 * math.pi
                    c.move_to(hx + 30 * math.cos(a), hy + 30 * math.sin(a))
                    c.line_to(hx + (55 + 30 * sw) * math.cos(a), hy + (55 + 30 * sw) * math.sin(a))
                    c.set_source_rgba(1, 0.95, 0.4, 1 - sw * 2); c.set_line_width(6); c.stroke()
            c.arc(770, 115, 60, 0, 2 * math.pi); c.set_source_rgba(0.05, 0.05, 0.08, 0.85); c.fill()
            T(c, str(hit), 770, 146, 84, (1, 0.85, 0.2), stroke=None)
            T(c, "BACK BLOWS", 770, 212, 26, WHITE)
        if out:
            r = min(1, (p - 0.84) / 0.1)
            c.arc(vx + 20 + 180 * r, vy + 70 - 120 * r + 200 * r * r, 13, 0, 2 * math.pi); c.set_source_rgb(0.85, 0.65, 0.3); c.fill()
            bubble(c, 600, 80, "IT'S OUT!", (0.8, 1, 0.82))


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
