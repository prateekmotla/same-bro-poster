"""BRAVE vs NORMAL — WHO'S RIGHT? #7: lost in a forest at dusk (engine: studio/shorts/dilemma.py).
Fact: search-and-rescue advice (B.C. AdventureSmart / BC Search and Rescue, Global News 25 Jan 2023): STOP = Stop,
Think, Observe, Plan; 'It's always harder (for search teams to find you) if you move.' Stay put, make yourself visible
and heard, save phone battery. India emergency 112. Audio sped 1.06x (42.2 s take > 39.8 s)."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
from kit import T, S, RED, GRN, WHITE  # noqa: E402
import body as B  # noqa: E402

D = "/home/claude/sid/shorts/s93_lost"
CAPS = [
    "Trek. You lost your group, you're LOST in the forest, and it's getting dark. Brave: keep walking. Normal: stay right here. Whose side are you on?",
    "Brave walks fast, a new path at every turn, and goes even DEEPER into the forest.",
    "Normal stays put, stays calm, tries 112 on the phone, and keeps blowing a whistle.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Search and rescue says: STOP. Stop, Think, Observe, Plan. Keep moving and you get HARDER to find.",
    "Stay in one place, show bright clothes, blow a whistle, and save your phone battery.",
    "Lost? Don't be the hero, STAY PUT. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #7", question=("LOST IN A FOREST.", "WHAT DO YOU DO?"),
           brave="KEEP WALKING", normal="STAY PUT, CALL", answer='N', grade='studio',
           why_title="LOST? DO THIS",
           why_rows=[("STOP: Stop, Think, Observe, Plan", WHITE), ("DON'T keep wandering", RED),
                     ("Stay in one open spot", WHITE), ("Bright clothes + whistle", WHITE),
                     ("Call 112, save battery", GRN)],
           src="SRC: Search & Rescue (AdventureSmart) advice", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

_V = dict(HAIR=B.S.C('1E1A18'), HAIR_HI=B.S.C('4A3A30'), HOOD=B.S.C('C8642A'), HOOD_SH=B.S.C('9A4A1E'),
          HOOD_HI=B.S.C('E08A50'), HOOD_LN=B.S.C('4A2410'))


def bg(c, t, dark=0.0):
    g = cairo.LinearGradient(0, 0, 0, 700)
    g.add_color_stop_rgb(0, 0.42 - 0.2 * dark, 0.36 - 0.18 * dark, 0.5 - 0.15 * dark)
    g.add_color_stop_rgb(1, 0.85 - 0.3 * dark, 0.55 - 0.2 * dark, 0.38 - 0.15 * dark)
    c.rectangle(-400, 0, 1880, 700); c.set_source(g); c.fill()
    for j, x in enumerate(range(-380, 1500, 110)):
        h = 0.6 + 0.4 * math.sin(j * 1.9)
        c.rectangle(x, 80, 30 + 12 * h, 600); c.set_source_rgb(0.18 - 0.08 * dark, 0.13 - 0.06 * dark, 0.09); c.fill()
        c.arc(x + 18, 120, 110 + 50 * h, 0, 2 * math.pi)
        c.set_source_rgb(0.1, 0.24 + 0.05 * h - 0.1 * dark, 0.14 - 0.04 * dark); c.fill()
    c.rectangle(-400, 640, 1880, 400); c.set_source_rgb(0.3 - 0.1 * dark, 0.26 - 0.08 * dark, 0.16); c.fill()
    for x in range(-390, 1480, 46):
        c.move_to(x, 650); c.rel_line_to(6, -24 - 10 * math.sin(x)); c.set_source_rgb(0.2, 0.36 - 0.1 * dark, 0.16)
        c.set_line_width(4); c.stroke()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 24 + 60
    S.rrect(c, x, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x + w / 2, y + 50, 36, (0.1, 0.1, 0.15), stroke=None)


def normal_friend(c, t, x, y, s, **kw):
    def _b(c_, x_, y_, s_, t_, **k_):
        B.CH._swap(_V); B.S.torso(c_, x_, y_, s_, t_, **k_); B.CH._swap(B.CH._SID)

    def _h(c_, x_, y_, s_, t_, **k_):
        B.CH._swap(_V); k_.setdefault('stubble', 0.3); B.S.head(c_, x_, y_, s_, t_, **k_); B.CH._swap(B.CH._SID)
    fb, fh = B.friend_body, B.friend_head
    B.friend_body, B.friend_head = _b, _h
    try:
        B.figure(c, x, y, s, t, who='friend', **kw)
    finally:
        B.friend_body, B.friend_head = fb, fh


def scene(c, side, t, p):
    if side == 'B':
        bg(c, t, dark=0.2 + 0.6 * p)
        # Brave walks off deeper: drifts right and shrinks
        q = S.ease(min(1, p / 0.9))
        x, y, s = 520 + 380 * q, 280 + 120 * q, 0.42 - 0.2 * q
        K.sid(c, t, x, y, s, pose='walk', ph=t * 1.6, mouth='o' if p > 0.5 else 'smirk', look=(0.6, 0.2))
        if p < 0.45:
            bubble(c, 160, 70, "KEEP WALKING!", (1, 0.85, 0.8))
        else:
            bubble(c, 160, 70, "WHERE AM I...?", (1, 0.82, 0.8))
            for j in range(3):   # crossing trails
                c.move_to(-200 + j * 300, 990); c.curve_to(200 + j * 150, 820, 500 - j * 200, 760, 900 + j * 160, 690)
                c.set_source_rgba(0.55, 0.45, 0.3, 0.5); c.set_line_width(26); c.stroke()
            T(c, "?", 1080 + 40 * math.sin(t * 3), 260, 120, (1, 0.9, 0.4))
            T(c, "?", 300 + 30 * math.sin(t * 2.4), 420, 90, (1, 0.9, 0.4))
    else:
        bg(c, t, dark=0.35)
        # small clearing + bright jacket on a branch
        c.save(); c.translate(540, 760); c.scale(1, 0.35); c.arc(0, 0, 420, 0, 2 * math.pi); c.restore()
        c.set_source_rgb(0.42, 0.36, 0.24); c.fill()
        calling = 0.25 < p < 0.6
        whistle = p >= 0.6
        normal_friend(c, t, 540, 300, 0.42, pose='sit', mouth='o' if whistle else 'flat',
                      arms=((14, -10), (40, 110)) if calling else (((14, -10), (60, 120)) if whistle else ((14, -10), (14, -10))),
                      phone=1 if calling else None, glow=0.6 if calling else 0.0, look=(0.3, 0.2))
        if whistle:   # whistle + sound rings
            c.rectangle(560, 372, 40, 16); c.set_source_rgb(0.95, 0.8, 0.1); c.fill()
            for r in range(3):
                rr = 40 + ((t * 90 + r * 45) % 140)
                c.arc(610, 380, rr, -0.7, 0.7); c.set_source_rgba(1, 1, 1, max(0, 1 - rr / 180)); c.set_line_width(6); c.stroke()
            bubble(c, 160, 70, "TWEET! TWEET!")
        elif calling:
            bubble(c, 160, 70, "CALLING 112...")
        else:
            bubble(c, 160, 70, "STOP. STAY HERE.")
        # bright orange jacket hung on a tree as a marker
        c.move_to(740, 330); c.line_to(860, 330); c.set_source_rgb(0.2, 0.14, 0.08); c.set_line_width(10); c.stroke()
        S.rrect(c, 760, 336, 80, 110, 12); c.set_source_rgb(1, 0.5, 0.1); c.fill()
        T(c, "VISIBLE", 800, 500, 34, (1, 0.95, 0.4))


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
