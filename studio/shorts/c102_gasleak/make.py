"""BRAVE vs NORMAL — WHO'S RIGHT? #12: LPG gas smell in the kitchen (engine: studio/shorts/dilemma.py).
Fact: LPG companies' leak advice (TotalEnergies India, SUPERGAS): do NOT switch any electrical switch ON or OFF (a spark
can ignite the gas), put out all flames, turn the regulator/cylinder valve OFF, open all doors and windows (don't turn
on fans), call your distributor / emergency line. IndianOil: '1906' = 24x7 LPG Emergency Helpline for all customers of
the three public-sector OMCs (launched 1 Jan 2016; still listed on iocl.com). No fire or injury shown on screen.
Voice take sped 1.1x (44.2 s > 40.2 s)."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c102_gasleak"
CAPS = [
    "You come home, and there's a strong GAS smell in the kitchen. Brave: switch the light on, let's find the leak. Normal: don't touch ANY switch, open the windows. Whose side are you on?",
    "Brave reaches out to press the light switch. One tiny spark, and the whole gas can catch fire.",
    "Normal turns the regulator off, opens all windows and doors, and doesn't touch any switch, fan or lighter.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Gas companies' safety advice: during a leak, don't switch anything ON or OFF, a spark can start a fire.",
    "Regulator off, windows open, get out of the house, and call the LPG emergency helpline 1906.",
    "Smell gas? Not the light, the window. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #12", question=("GAS SMELL AT HOME!", "WHAT DO YOU DO?"),
           brave="SWITCH ON THE LIGHT", normal="NO SWITCHES, OPEN WINDOWS", answer='N', grade='studio',
           why_title="SMELL GAS? DO THIS",
           why_rows=[("NO switch ON or OFF, no fan", RED), ("No flame, no lighter", RED), ("Turn the regulator OFF", WHITE),
                     ("Open all windows & doors", WHITE), ("Go out, call 1906 (LPG helpline)", GRN)],
           src="SRC: IndianOil 1906 helpline, LPG safety advice", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

FLOOR = 900
SW = (845, 430)       # light switch board centre
WIN = (190, 230, 250, 300)   # window x, y, w, h


def room(c, t, win_open=0.0):
    c.rectangle(-400, 0, 1880, FLOOR); c.set_source_rgb(0.93, 0.87, 0.76); c.fill()
    for j in range(-6, 22):                         # wall tiles behind counter
        c.rectangle(440 + j * 0, 0, 0, 0)
    c.rectangle(450, 470, 470, 170); c.set_source_rgb(0.86, 0.9, 0.92); c.fill()
    for j in range(8):
        c.move_to(450 + j * 60, 470); c.rel_line_to(0, 170)
    for j in range(3):
        c.move_to(450, 470 + j * 57); c.rel_line_to(470, 0)
    c.set_source_rgba(0.6, 0.65, 0.7, 0.6); c.set_line_width(2); c.stroke()
    c.rectangle(-400, FLOOR, 1880, 200); c.set_source_rgb(0.55, 0.42, 0.32); c.fill()
    for j in range(-4, 16):
        c.move_to(j * 110, FLOOR); c.rel_line_to(-60, 100); c.set_source_rgba(0, 0, 0, 0.12); c.set_line_width(3); c.stroke()
    # window
    x, y, w, h = WIN
    sky = cairo.LinearGradient(0, y, 0, y + h)
    sky.add_color_stop_rgb(0, 0.55, 0.75, 0.95); sky.add_color_stop_rgb(1, 0.85, 0.92, 0.98)
    c.rectangle(x, y, w, h); c.set_source(sky); c.fill()
    c.rectangle(x + 20, y + 200, 60, 100); c.set_source_rgb(0.4, 0.6, 0.4); c.fill()   # tree outside
    pw = w / 2 * (1 - 0.8 * win_open)
    for side in (0, 1):
        px = x if side == 0 else x + w - pw
        c.rectangle(px, y, pw, h); c.set_source_rgba(0.7, 0.85, 0.95, 0.85 - 0.3 * win_open); c.fill()
        c.rectangle(px, y, pw, h); c.set_source_rgb(0.95, 0.95, 0.95); c.set_line_width(10); c.stroke()
    c.rectangle(x - 12, y - 12, w + 24, h + 24); c.set_source_rgb(0.98, 0.98, 0.98); c.set_line_width(12); c.stroke()
    # counter + stove + cylinder cabinet
    c.rectangle(440, 640, 490, FLOOR - 640); c.set_source_rgb(0.42, 0.3, 0.22); c.fill()
    c.rectangle(430, 625, 510, 26); c.set_source_rgb(0.2, 0.2, 0.22); c.fill()
    S.rrect(c, 520, 585, 300, 42, 10); c.set_source_rgb(0.12, 0.12, 0.14); c.fill()
    for bx in (590, 750):
        c.save(); c.translate(bx, 588); c.scale(1, 0.3); c.arc(0, 0, 44, 0, 2 * math.pi); c.restore()
        c.set_source_rgb(0.35, 0.35, 0.38); c.set_line_width(6); c.stroke()
    c.rectangle(470, 680, 230, 210); c.set_source_rgb(0.3, 0.21, 0.15); c.fill()    # open cabinet
    # light switch board
    sx, sy = SW
    S.rrect(c, sx - 38, sy - 50, 76, 100, 10); c.set_source_rgb(0.98, 0.98, 0.96); c.fill_preserve()
    c.set_source_rgb(0.6, 0.6, 0.6); c.set_line_width(3); c.stroke()
    for dy in (-20, 20):
        S.rrect(c, sx - 14, sy + dy - 14, 28, 28, 5); c.set_source_rgb(0.85, 0.85, 0.85); c.fill()
    c.rectangle(560, 0, 140, 30); c.set_source_rgb(0.9, 0.9, 0.9); c.fill()    # ceiling light (off)
    c.save(); c.translate(630, 40); c.scale(1, 0.4); c.arc(0, 0, 60, 0, math.pi); c.restore()
    c.set_source_rgb(0.75, 0.75, 0.7); c.fill()


def cylinder(c, reg_off=False):
    x, y = 585, 715
    S.rrect(c, x - 60, y, 120, 175, 40); c.set_source_rgb(0.82, 0.15, 0.15); c.fill()
    c.rectangle(x - 60, y + 60, 120, 14); c.set_source_rgba(1, 1, 1, 0.6); c.fill()
    c.rectangle(x - 22, y - 26, 44, 28); c.set_source_rgb(0.3, 0.3, 0.32); c.fill()        # regulator
    c.arc(x, y - 30, 18, 0, 2 * math.pi); c.set_source_rgb(*(GRN if reg_off else (0.95, 0.6, 0.1))); c.fill()
    c.move_to(x + 22, y - 14); c.curve_to(x + 120, y - 20, x + 80, y - 100, x + 120, y - 120)
    c.set_source_rgb(0.9, 0.5, 0.1); c.set_line_width(8); c.stroke()                          # hose
    if reg_off:
        S.rrect(c, x - 54, y - 92, 108, 40, 14); c.set_source_rgb(*GRN); c.fill()
        T(c, "OFF", x, y - 61, 28, (0.03, 0.1, 0.05), stroke=None)


def gas(c, t, a=1.0):
    if a <= 0:
        return
    for j in range(7):
        ph = (t * 0.35 + j / 7) % 1
        x0 = 520 + (j % 4) * 70
        y0 = 700 - ph * 520
        c.move_to(x0, y0)
        for s in range(6):
            c.rel_curve_to(14, -14, -14, -28, 0, -42)
        c.set_source_rgba(0.55, 0.85, 0.3, a * 0.6 * math.sin(ph * math.pi)); c.set_line_width(7); c.stroke()
    if a > 0.3:
        S.rrect(c, 440, 140, 230, 58, 22); c.set_source_rgba(0.55, 0.85, 0.3, 0.9 * a); c.fill()
        T(c, "GAS SMELL", 555, 180, 32, (0.08, 0.15, 0.05), a, stroke=None)


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def spark_warn(c, t, a):
    sx, sy = SW
    for j in range(8):                                   # tiny spark star at the switch (warning icon, no fire)
        an = j / 8 * 2 * math.pi + t * 2
        c.move_to(sx, sy); c.line_to(sx + 34 * math.cos(an), sy + 34 * math.sin(an))
    c.set_source_rgba(1, 0.9, 0.2, a); c.set_line_width(5); c.stroke()
    c.arc(sx, sy, 80 + 6 * math.sin(t * 10), 0, 2 * math.pi); c.set_source_rgba(*RED, a); c.set_line_width(10); c.stroke()


def scene(c, side, t, p):
    if side == 'B':
        room(c, t, 0.0)
        cylinder(c, False)
        gas(c, t, 1.0)
        q = S.ease(min(1, p / 0.4))
        x = 330 + 330 * q
        reach = p > 0.3
        K.sid(c, t, x, 455, 0.42, mouth='smirk' if p < 0.45 else 'o', look=(0.7, 0),
              arms=((14, -10), (100, 40)) if reach else ((14, -10), (14, -10)), eyes=1.25 if p > 0.45 else 1.0)
        if p > 0.45:
            spark_warn(c, t, min(1, (p - 0.45) * 6))
            bubble(c, 520, 280, "1 SPARK = FIRE RISK!", (1, 0.82, 0.8))
        else:
            bubble(c, 520, 280, "LIGHT ON, FIND THE LEAK!", (1, 0.85, 0.8))
    else:
        reg = p > 0.3
        win = S.ease(max(0, min(1, (p - 0.35) / 0.25)))
        room(c, t, win)
        cylinder(c, reg)
        gas(c, t, 1.0 - 0.85 * win)
        if p < 0.33:
            x, arms, ph = 700, ((14, -10), (150, 30)), None
            msg = "REGULATOR OFF"
        elif p < 0.66:
            x, arms, ph = 310, ((100, 40), (100, 40)), None
            msg = "OPEN ALL WINDOWS"
        else:
            x, arms, ph = 330, ((14, -10), (40, 110)), 1
            msg = "GO OUT, CALL 1906"
        B.figure(c, x, 455, 0.42, t, who='friend', mouth='flat', arms=arms, phone=ph, look=(-0.6, 0) if p > 0.33 else (0.6, 0.2))
        bubble(c, 560, 280, msg)
        if p > 0.15:
            S.rrect(c, 760, 560, 160, 50, 18); c.set_source_rgba(0.05, 0.4, 0.15, 0.9); c.fill()
            T(c, "NO SWITCH", 840, 594, 26, WHITE, stroke=None)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
