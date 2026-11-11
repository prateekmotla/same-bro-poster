"""BRAVE vs NORMAL — WHO'S RIGHT? #18: friend stuck to a live wire at home (engine: studio/shorts/dilemma.py).
Facts: St John Ambulance / Better Health Channel (Victoria) electric-shock first aid: do NOT touch the person while
they are still in contact with the electrical source, you can get a shock too; switch off the power at the mains /
unplug first; if you can't, stand on something dry and non-conducting and push the source away with a dry wooden
object (broom handle); then call emergency services (112 in India) and give first aid.
Brand-safe: no injury shown; the person is drawn with zig-zag 'current' lines only; Brave freezes reaching out, then
the red WRONG freeze."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c126_shock"
CAPS = [
    "A friend was fixing an iron at home and got an electric SHOCK. He's stuck to the wire. Brave: pull him off. Normal: main switch first. You?",
    "Brave runs straight in and grabs his arm with BARE hands.",
    "Normal flips the main switch, then pushes the wire away with a dry wooden stick.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. The current is still in his body. Touch him and YOU become part of the same circuit.",
    "Cut the power first. Can't find the switch? Stand on dry slippers, push it away with dry wood. Then call 112.",
    "The real hero doesn't become victim number two. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6], end=[7])
CFG = dict(series="BRAVE vs NORMAL #18", question=("FRIEND STUCK TO A LIVE WIRE!", "WHAT DO YOU DO?"),
           brave="PULL HIM OFF BY HAND", normal="MAIN SWITCH OFF FIRST", answer='N', grade='warm',
           why_title="ELECTRIC SHOCK? DO THIS",
           why_rows=[("DON'T touch him", RED), ("Main switch OFF / unplug", WHITE), ("No switch? Stand on dry", WHITE),
                     ("Push wire with dry wood", WHITE), ("Then call 112", GRN), ("Never use wet or metal", RED)],
           src="SRC: electric shock first aid (St John Ambulance)", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

GROUND = 880
SOCK = (990, 640)


def room(c, t):
    c.rectangle(-400, 0, 1880, GROUND); c.set_source_rgb(0.93, 0.88, 0.78); c.fill()
    c.rectangle(-400, GROUND, 1880, 220); c.set_source_rgb(0.55, 0.42, 0.32); c.fill()
    c.rectangle(-400, GROUND - 14, 1880, 14); c.set_source_rgb(0.75, 0.68, 0.58); c.fill()
    # window
    S.rrect(c, 420, 110, 260, 200, 10); c.set_source_rgb(0.62, 0.8, 0.95); c.fill()
    c.rectangle(545, 110, 10, 200); c.set_source_rgb(0.9, 0.9, 0.88); c.fill()
    # socket board on wall
    S.rrect(c, SOCK[0] - 50, SOCK[1] - 50, 100, 100, 12); c.set_source_rgb(0.98, 0.98, 0.96); c.fill()
    for dx in (-15, 15):
        c.arc(SOCK[0] + dx, SOCK[1] + 8, 7, 0, 2 * math.pi); c.set_source_rgb(0.2, 0.2, 0.2); c.fill()
    # table with iron
    c.rectangle(770, 700, 200, 26); c.set_source_rgb(0.45, 0.3, 0.2); c.fill()
    for x in (780, 940):
        c.rectangle(x, 726, 20, GROUND - 726); c.fill()


def mcb(c, on):
    """main switch box on the left wall."""
    S.rrect(c, 180, 380, 150, 200, 14); c.set_source_rgb(0.85, 0.85, 0.82); c.fill()
    T(c, "MAIN", 255, 420, 26, (0.2, 0.2, 0.25), stroke=None)
    S.rrect(c, 230, 445, 50, 100, 10); c.set_source_rgb(0.15, 0.15, 0.18); c.fill()
    S.rrect(c, 238, 452 if on else 495, 34, 44, 8); c.set_source_rgb(*(RED if on else GRN)); c.fill()
    T(c, "ON" if on else "OFF", 255, 610, 30, RED if on else GRN, stroke=None)


def victim(c, t, live, wire_off=False):
    """friend standing at the table, hand on the iron; zig-zag 'current' lines while live. No injury."""
    shake = 4 * math.sin(t * 60) if live else 0
    B.figure(c, 690 + shake, 420, 0.42, t, who='bhai', mouth='o' if live else 'flat', look=(0.5, 0),
             arms=((60, 60), (100, 40)))
    # iron + cord to socket
    ix, iy = 850, 690
    c.move_to(ix - 50, iy); c.line_to(ix + 50, iy); c.line_to(ix + 30, iy - 40); c.line_to(ix - 30, iy - 40); c.close_path()
    c.set_source_rgb(0.3, 0.55, 0.85); c.fill()
    c.move_to(ix + 50, iy - 10)
    if wire_off:
        c.curve_to(ix + 120, iy + 120, SOCK[0] - 40, GROUND - 10, SOCK[0] + 60, GROUND - 6)
    else:
        c.curve_to(ix + 120, iy - 10, SOCK[0] - 60, SOCK[1] + 60, SOCK[0], SOCK[1] + 10)
    c.set_source_rgb(0.1, 0.1, 0.12); c.set_line_width(7); c.stroke()
    if live:
        for j in range(5):
            a = j * 1.26 + t * 9
            x0, y0 = 710 + 140 * math.cos(a), 560 + 200 * math.sin(a)
            c.move_to(x0, y0)
            for q in range(4):
                c.rel_line_to(18 * (1 if q % 2 else -1), 22)
            c.set_source_rgba(1, 0.92, 0.2, 0.6 + 0.4 * math.sin(t * 30 + j)); c.set_line_width(6); c.stroke()
        T(c, "LIVE CURRENT", 700, 330, 34, RED, stroke=None)


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 23 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 34, (0.1, 0.1, 0.15), stroke=None)


def stick(c, x, y, rot):
    c.save(); c.translate(x, y); c.rotate(rot)
    S.rrect(c, -10, -230, 20, 260, 8); c.set_source_rgb(0.62, 0.42, 0.22); c.fill()
    c.restore()


def scene(c, side, t, p):
    room(c, t)
    if side == 'B':
        mcb(c, True)
        victim(c, t, True)
        q = S.ease(min(1, p / 0.5))
        K.sid(c, t, 260 + 210 * q, 420, 0.42, mouth='o' if p > 0.5 else 'smile', look=(0.8, 0.1),
              arms=((100, 20), (100, 20)) if p > 0.3 else ((14, -10), (40, 60)), eyes=1.15)
        if p > 0.55:
            S.rrect(c, 280, 720, 520, 60, 22); c.set_source_rgba(*RED, 0.92); c.fill()
            T(c, "BARE HANDS ON LIVE CURRENT!", 540, 760, 28, WHITE, stroke=None)
        bubble(c, 450, 250, "I'LL PULL HIM!", (1, 0.85, 0.8))
    else:
        on = p < 0.3
        mcb(c, on)
        victim(c, t, on, wire_off=p > 0.65)
        if p < 0.3:
            fx = 400
            B.figure(c, fx, 420, 0.42, t, who='friend', mouth='flat', look=(-0.6, 0), arms=((100, -60), (14, -10)))
            bubble(c, 520, 250, "MAIN SWITCH OFF")
        else:
            q = S.ease(min(1, (p - 0.3) / 0.3))
            fx = 400 + 80 * q
            B.figure(c, fx, 420, 0.42, t, who='friend', mouth='flat', look=(0.7, 0.1), arms=((100, 40), (100, 20)))
            stick(c, fx + 110, 640, 1.0 + 0.4 * S.ease(min(1, max(0, (p - 0.6) / 0.25))))
            bubble(c, 540, 250, "POWER OFF. NOW DRY WOOD" if p < 0.65 else "WIRE AWAY. CALL 112")
            S.rrect(c, 360, 720, 360, 56, 20); c.set_source_rgba(0.05, 0.4, 0.15, 0.9); c.fill()
            T(c, "CURRENT OFF", 540, 758, 30, WHITE, stroke=None)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
