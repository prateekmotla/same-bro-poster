"""BRAVE vs NORMAL — WHO'S RIGHT? #2: friend drowning in a lake (engine: studio/shorts/dilemma.py).
Fact: American Red Cross water safety — 'Reach or throw, don't go': help from land with a pole/rope or throw
something that floats; untrained rescuers who go in can be pulled under by a panicking swimmer. India emergency: 112."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
from kit import T, S, RED, GRN, WHITE  # noqa: E402
import body as B  # noqa: E402

D = "/home/claude/sid/shorts/s73_drown"
CAPS = [
    "Friend drowning in a lake. Brave: I'll jump in and save him. Normal: throw something that floats. Whose side are you on?",
    "Brave jumps straight in. But a panicking person grabs the rescuer and pulls him under.",
    "Normal lies flat on the bank, reaches out a stick, throws an empty bottle, and shouts for help.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Red Cross rule: REACH or THROW, DON'T GO. Jump in without training, and now two people are in danger.",
    "Reach out a hand, stick or rope from the bank. Throw anything that floats. And call 112 right away.",
    "A hero is the one who brings everyone back safe. What would YOU do first?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #2", question=("FRIEND IS DROWNING.", "WHAT DO YOU DO?"),
           brave="JUMP IN & SAVE HIM", normal="REACH / THROW A FLOAT", answer='N', grade='studio',
           why_title="REACH OR THROW, DON'T GO",
           why_rows=[("Panic = he grabs the rescuer", RED), ("Untrained jump: 2 in danger", WHITE),
                     ("REACH: hand, stick, rope", WHITE), ("THROW: anything that floats", WHITE),
                     ("Then call 112. Shout for help.", GRN)],
           src="SRC: American Red Cross water safety", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

BANK_Y, WATER_Y = 700, 735
SKIN = (0.86, 0.63, 0.47)


def bg(c, t):
    g = cairo.LinearGradient(0, 0, 0, WATER_Y)
    g.add_color_stop_rgb(0, 0.55, 0.72, 0.9); g.add_color_stop_rgb(1, 0.85, 0.88, 0.86)
    c.rectangle(-400, 0, 1880, WATER_Y); c.set_source(g); c.fill()
    # far hills + tree line
    c.move_to(-400, 560)
    for x in range(-400, 1500, 60):
        c.line_to(x, 520 - 40 * math.sin(x * 0.006) - 18 * math.sin(x * 0.031))
    c.line_to(1480, WATER_Y); c.line_to(-400, WATER_Y); c.close_path(); c.set_source_rgb(0.25, 0.42, 0.3); c.fill()
    for x in range(-380, 1500, 70):
        h = 60 + 30 * math.sin(x * 0.13)
        c.arc(x, 560 - h * 0.5, h * 0.55, 0, 2 * math.pi); c.set_source_rgb(0.17, 0.33, 0.22); c.fill()
    # water
    w = cairo.LinearGradient(0, WATER_Y, 0, 1000)
    w.add_color_stop_rgb(0, 0.2, 0.42, 0.52); w.add_color_stop_rgb(1, 0.06, 0.18, 0.26)
    c.rectangle(-400, WATER_Y, 1880, 300); c.set_source(w); c.fill()


def water_front(c, t):
    """semi-opaque water drawn over bodies (hides everything under the surface)."""
    w = cairo.LinearGradient(0, WATER_Y, 0, 1000)
    w.add_color_stop_rgba(0, 0.2, 0.44, 0.55, 0.88); w.add_color_stop_rgba(1, 0.05, 0.17, 0.25, 0.98)
    c.move_to(380, WATER_Y)
    for x in range(380, 1500, 20):
        c.line_to(x, WATER_Y + 5 * math.sin(x * 0.05 + t * 3))
    c.line_to(1480, 1000); c.line_to(380, 1000); c.close_path(); c.set_source(w); c.fill()
    for j in range(7):
        x = 460 + j * 150 + 30 * math.sin(t + j)
        c.move_to(x, WATER_Y + 30 + j % 3 * 40); c.rel_line_to(70, 0)
        c.set_source_rgba(1, 1, 1, 0.25); c.set_line_width(4); c.stroke()
    # bank (in front of water edge)
    c.move_to(-400, BANK_Y); c.line_to(330, BANK_Y); c.curve_to(400, BANK_Y + 10, 420, 760, 440, 1000); c.line_to(-400, 1000)
    c.close_path(); c.set_source_rgb(0.42, 0.33, 0.2); c.fill()
    c.rectangle(-400, BANK_Y - 14, 740, 18); c.set_source_rgb(0.3, 0.55, 0.25); c.fill()
    for x in range(-390, 330, 26):
        c.move_to(x, BANK_Y - 10); c.rel_line_to(6, -22 - 8 * math.sin(x)); c.set_source_rgb(0.25, 0.5, 0.2)
        c.set_line_width(4); c.stroke()


def ripples(c, x, y, t, n=3):
    for r in range(n):
        rr = 40 + ((t * 60 + r * 30) % 90)
        c.save(); c.translate(x, y); c.scale(1, 0.25)
        c.arc(0, 0, rr, 0, 2 * math.pi); c.restore()
        c.set_source_rgba(1, 1, 1, 0.5 * (1 - (rr - 40) / 90)); c.set_line_width(3); c.stroke()


def victim(c, t, x, y, mode='wave', tx=None):
    """simple head + arms above water. mode wave | hold (hand reaching to tx) | grab (arms toward the left)."""
    c.set_line_cap(cairo.LINE_CAP_ROUND)
    if mode == 'wave':
        for sd in (-1, 1):
            a = math.sin(t * 7 + sd) * 0.35
            c.move_to(x + sd * 30, y + 20)
            c.line_to(x + sd * (60 + 30 * math.sin(a)), y - 90 - 20 * math.cos(a))
            c.set_source_rgb(*SKIN); c.set_line_width(22); c.stroke()
    elif mode == 'hold' and tx is not None:
        c.move_to(x - 20, y + 25); c.line_to(*tx); c.set_source_rgb(*SKIN); c.set_line_width(22); c.stroke()
        c.move_to(x + 30, y + 20); c.line_to(x + 70, y - 40 + 10 * math.sin(t * 5)); c.stroke()
    elif mode == 'grab':
        for dy in (0, 26):
            c.move_to(x + 20, y + 30 + dy); c.line_to(x - 105, y - 10 + dy); c.set_source_rgb(*SKIN); c.set_line_width(22); c.stroke()
    c.arc(x, y, 46, 0, 2 * math.pi); c.set_source_rgb(*SKIN); c.fill()
    c.arc(x, y - 6, 48, math.pi * 1.05, math.pi * 1.95); c.set_source_rgb(0.12, 0.09, 0.08); c.set_line_width(22); c.stroke()
    for ex in (-16, 16):
        c.arc(x + ex, y - 4, 6.5, 0, 2 * math.pi); c.set_source_rgb(0.1, 0.08, 0.08); c.fill()
    c.save(); c.translate(x, y + 22); c.scale(1, 1.3); c.arc(0, 0, 9, 0, 2 * math.pi); c.restore()
    c.set_source_rgb(0.35, 0.1, 0.1); c.fill()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x + w / 2, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def scene(c, side, t, p):
    bg(c, t)
    bob = 8 * math.sin(t * 4)
    vx, vy = 760, WATER_Y - 10 + bob
    if side == 'B':
        if p < 0.12:
            victim(c, t, vx, vy); ripples(c, vx, WATER_Y + 10, t)
            water_front(c, t)
            K.sid(c, t, 250, 255, 0.42, mouth='smirk', arms=((14, -10), (14, -10)), look=(0.6, 0))
        elif p < 0.38:
            q = (p - 0.12) / 0.26
            x = 250 + (650 - 250) * q
            y = 255 + (WATER_Y - 20 - 255) * q - 260 * math.sin(math.pi * q)
            victim(c, t, vx, vy); ripples(c, vx, WATER_Y + 10, t)
            if q > 0.85:
                water_front(c, t)
                K.sid(c, t, x, y, 0.42, mouth='o', eyes=1.2, arms=((150, 10), (150, 10)), lean=12)
            else:
                K.sid(c, t, x, y, 0.42, mouth='smirk', arms=((150, 10), (150, 10)), lean=20 * q)
                water_front(c, t)
            if q > 0.85:
                for j in range(8):
                    a = j / 8 * math.pi
                    c.arc(650 + 120 * math.cos(a), WATER_Y - 60 * math.sin(a) * (1 - (q - 0.85) * 4), 10, 0, 2 * math.pi)
                    c.set_source_rgba(0.85, 0.95, 1, 0.8); c.fill()
        else:
            sink = 28 * S.ease(max(0, min(1, (p - 0.45) / 0.45)))
            sx, sy = 640, WATER_Y - 62 + sink + bob * 0.6
            K.sid(c, t, sx, sy, 0.42, mouth='o', eyes=1.3, sweat=1, arms=((150, 20), (120, 30)))
            victim(c, t, sx + 120, sy + 4, 'grab')
            ripples(c, sx + 60, WATER_Y + 10, t * 1.6, 4)
            water_front(c, t)
            for j in range(5):
                by = WATER_Y - ((t * 90 + j * 37) % 120)
                c.arc(sx + 40 + j * 22, by, 7, 0, 2 * math.pi); c.set_source_rgba(0.85, 0.95, 1, 0.7); c.fill()
            if p > 0.5:
                bubble(c, 300, 300, "PANIC GRAB!", (1, 0.82, 0.8))
                S.rrect(c, 840, 150, 110, 110, 18); c.set_source_rgba(1, 0.2, 0.15, 0.9 * (int(t * 4) % 2)); c.fill()
                T(c, "!", 895, 236, 84, WHITE, int(t * 4) % 2, stroke=None)
    else:
        fx, fy = 230, 255
        stick = p >= 0.1
        if p < 0.1:
            victim(c, t, vx, vy); ripples(c, vx, WATER_Y + 10, t)
            water_front(c, t)
            B.figure(c, fx, fy, 0.42, t, who='friend', mouth='flat', arms=((14, -10), (14, -10)), look=(0.6, 0))
        elif p < 0.4:
            q = S.ease(min(1, (p - 0.1) / 0.15))
            tip = (330 + (vx - 70 - 330) * q, 560 + (vy + 10 - 560) * q)
            victim(c, t, vx, vy, 'hold' if q > 0.95 else 'wave', tx=tip)
            ripples(c, vx, WATER_Y + 10, t)
            water_front(c, t)
            B.figure(c, fx, fy, 0.42, t, who='friend', mouth='flat', angry=0.3, arms=((14, -10), (70, 10)), look=(0.6, 0.2), lean=16)
            c.set_line_cap(cairo.LINE_CAP_ROUND)
            c.move_to(330, 470); c.line_to(*tip); c.set_source_rgb(0.45, 0.3, 0.15); c.set_line_width(16); c.stroke()
        else:
            q = min(1, (p - 0.4) / 0.2)
            bx = 360 + (vx - 90 - 360) * q
            by = 420 + (WATER_Y - 20 - 420) * q - 200 * math.sin(math.pi * q)
            fl = q >= 1
            victim(c, t, vx, vy, 'hold' if fl else 'wave', tx=(bx + 10, by + 10 + bob * 0.5))
            ripples(c, vx, WATER_Y + 10, t)
            water_front(c, t)
            # bottle (empty, floats)
            c.save(); c.translate(bx, by + (bob * 0.5 if fl else 0)); c.rotate(0 if fl else q * 6)
            S.rrect(c, -40, -20, 80, 40, 14); c.set_source_rgba(0.75, 0.9, 1, 0.9); c.fill()
            c.rectangle(40, -9, 16, 18); c.set_source_rgb(0.2, 0.45, 0.9); c.fill()
            c.restore()
            calling = p > 0.68
            B.figure(c, fx, fy, 0.42, t, who='friend', mouth='o' if calling else 'flat',
                     arms=((14, -10), (40, 110)) if calling else ((14, -10), (150, 30)), phone=1 if calling else None,
                     glow=0.6 if calling else 0.0, look=(0.6, 0))
            if calling:
                bubble(c, 200, 110, "CALLING 112...")
            if fl:
                T(c, "FLOATS!", vx - 250, WATER_Y - 70, 46, (1, 0.95, 0.4))


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
