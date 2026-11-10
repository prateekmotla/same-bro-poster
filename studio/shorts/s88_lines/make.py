"""SAME BRO GAMES #7: 3 optical illusions (engine: studio/shorts/illusion.py).
Level 1 Muller-Lyer (fins), level 2 Ponzo (railway track), level 3 Ebbinghaus (circle surround). In every level the two
targets are drawn with EXACTLY the same size in code (fair game; the answer is 'same')."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import illusion as IL  # noqa: E402
from illusion import T, YEL, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s88_lines"
CAPS = [
    "Level 1. Which line is LONGER? A or B? Comment!",
    "Answer: both are EXACTLY the same. The arrow ends FOOL your brain.",
    "Level 2. Two lines between the tracks. Is the TOP one longer, or the BOTTOM one?",
    "SAME again! The tracks going back make the top one look BIGGER.",
    "FINAL level. Which orange circle is BIGGER? Left or right?",
    "SAME size! What's your score? Comment, and watch again.",
]
LINE = (0.95, 0.95, 0.98)
ORANGE = (1.0, 0.55, 0.12)


def seg(c, x0, y0, x1, y1, col=LINE, w=14, a=1.0):
    c.set_line_cap(1); c.move_to(x0, y0); c.line_to(x1, y1); c.set_source_rgba(*col, a); c.set_line_width(w); c.stroke()


def muller(c, t, r):
    L, xa, xb = 520, 280, 800
    for y, out in ((720, False), (1120, True)):
        seg(c, xa, y, xb, y)
        fa = 1 - 0.75 * r
        for x, sd in ((xa, -1), (xb, 1)):
            d = 90 * (sd if out else -sd)
            seg(c, x, y, x + d, y - 80, w=12, a=fa)
            seg(c, x, y, x + d, y + 80, w=12, a=fa)
    if r > 0:
        IL.dashed(c, xa, 560, xa, 1280, YEL, r); IL.dashed(c, xb, 560, xb, 1280, YEL, r)
        T(c, "520 px", 540, 690, 40, YEL, r, stroke=None); T(c, "520 px", 540, 1090, 40, YEL, r, stroke=None)


def ponzo(c, t, r):
    c.set_line_cap(1)
    for i in range(14):   # sleepers
        f = i / 13
        y = 1480 - 1060 * (1 - (1 - f) ** 1.6)
        hw = 330 - 250 * (1480 - y) / 1060
        seg(c, 540 - hw - 30, y, 540 + hw + 30, y, (0.45, 0.33, 0.22), 16 - 9 * f)
    seg(c, 170, 1500, 470, 420, (0.7, 0.72, 0.78), 14); seg(c, 910, 1500, 610, 420, (0.7, 0.72, 0.78), 14)
    w = 220
    for y in (640, 1240):
        seg(c, 540 - w / 2, y, 540 + w / 2, y, YEL, 22)
    if r > 0:
        IL.dashed(c, 540 - w / 2, 560, 540 - w / 2, 1320, GRN, r); IL.dashed(c, 540 + w / 2, 560, 540 + w / 2, 1320, GRN, r)


def ebbing(c, t, r):
    cy, rr = 960, 58
    lx, rx = 300, 810
    for j in range(6):
        a = j / 6 * 2 * math.pi
        c.arc(lx + 150 * math.cos(a), cy + 150 * math.sin(a), 70, 0, 2 * math.pi); c.set_source_rgb(0.55, 0.58, 0.7); c.fill()
    for j in range(8):
        a = j / 8 * 2 * math.pi
        c.arc(rx + 102 * math.cos(a), cy + 102 * math.sin(a), 26, 0, 2 * math.pi); c.set_source_rgb(0.55, 0.58, 0.7); c.fill()
    for x in (lx, rx):
        c.arc(x, cy, rr, 0, 2 * math.pi); c.set_source_rgb(*ORANGE); c.fill()
    if r > 0:
        IL.dashed(c, 60, cy - rr, 1020, cy - rr, GRN, r); IL.dashed(c, 60, cy + rr, 1020, cy + rr, GRN, r)


LEVELS = [
    dict(name="LEVEL 1", q="WHICH LINE IS LONGER?", ans="BOTH THE SAME!", draw=muller, labels=[("A", 100, 720), ("B", 100, 1120)],
         stamp="SAME LENGTH"),
    dict(name="LEVEL 2", q="TOP OR BOTTOM LONGER?", ans="SAME AGAIN!", draw=ponzo, labels=[("A", 790, 640), ("B", 790, 1240)],
         stamp="SAME LENGTH"),
    dict(name="FINAL LEVEL", q="WHICH ORANGE IS BIGGER?", ans="SAME SIZE!", draw=ebbing, labels=[("A", 300, 1300), ("B", 810, 1300)],
         stamp="SAME SIZE"),
]

if __name__ == "__main__":
    g = IL.Illusion(D, CAPS, LEVELS, "SAME BRO GAMES #7", ("WHICH IS LONGER?", "TRUST YOUR EYES?"), mood='chill')
    if sys.argv[1] == "preview":
        g.preview([0.5, 3.0, 6.5, 9.0, 12, 15.5, 18, 21, 24.5, 27], f"{D}/prev.png")
        print("dur", round(g.dur, 1), [round(a, 1) for a, b in g.L])
    else:
        g.render(f"{D}/short.mp4")
