"""SAME BRO GAMES #20: find the fake Rs 500 note, 3 levels (engine: studio/shorts/illusion.py, question/answer pairs).
Security features (RBI 'Know your banknote' / paisaboltahai.rbi.org.in, Rs 500 Mahatma Gandhi New Series):
 L1 windowed security thread colour shifts GREEN to BLUE when the note is tilted > fake = B (stays green)
 L2 Mahatma Gandhi portrait + electrotype '500' watermark visible against light > fake = C (no watermark)
 L3 number panel: numerals grow from small to big (ascending font) > fake = A (all the same size)
Notes are deliberately CARTOON: no portrait, no real design, 'GAME NOTE' printed on each, so nothing here could pass as
currency. Answers are revealed on screen after each level."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import illusion as IL  # noqa: E402
from illusion import T, YEL, GRN, WHITE, S  # noqa: E402

D = "/home/claude/sid/shorts/c129_fakenote"
CAPS = [
    "SAME BRO GAMES! 3 notes, ONE fake. Level 1: tilt the note. A real thread turns from green to blue. Which is FAKE? A, B or C?",
    "B! Its thread stayed green.",
    "Level 2. Hold it to the light. A real note shows a watermark. Which is fake?",
    "C! No watermark.",
    "FINAL level. Look at the number panel. On a real note the digits grow from small to big. Which is fake?",
    "A! All digits the same size. Your score? Comment, and watch again.",
]
NOTE = (0.72, 0.68, 0.72)       # generic stone-grey cartoon note colour
GRN_ = (0.1, 0.75, 0.35)
BLU_ = (0.2, 0.45, 1.0)
DARK = (0.15, 0.13, 0.2)
YS = (560, 950, 1340)           # note centres (y)
LABS = "ABC"


def note(c, x, y, thread=None, wm=None, light=0.0, digits=None):
    """cartoon note 820x330 centred on (x, y)."""
    w, h = 820, 330
    S.rrect(c, x - w / 2, y - h / 2, w, h, 18); c.set_source_rgb(*NOTE); c.fill()
    S.rrect(c, x - w / 2 + 14, y - h / 2 + 14, w - 28, h - 28, 12); c.set_source_rgba(1, 1, 1, 0.25)
    c.set_line_width(4); c.stroke()
    T(c, "500", x - 290, y - 70, 64, DARK, stroke=None)
    T(c, "GAME NOTE", x + 120, y - 90, 30, DARK, stroke=None)
    T(c, "SAME BRO BANK", x + 120, y - 50, 26, DARK, stroke=None)
    # watermark window (left)
    c.arc(x - 290, y + 40, 70, 0, 2 * math.pi); c.set_source_rgba(1, 1, 1, 0.35 + 0.4 * light); c.fill()
    if wm and light > 0:
        c.arc(x - 290, y + 25, 30, 0, 2 * math.pi); c.set_source_rgba(0.45, 0.42, 0.48, 0.8 * light); c.fill()
        c.arc(x - 290, y + 95, 48, math.pi, 2 * math.pi); c.fill()
        T(c, "500", x - 290, y + 100, 24, (0.35, 0.33, 0.38), light, stroke=None)
    # security thread
    if thread is not None:
        for j in range(7):
            c.rectangle(x - 150, y - h / 2 + 10 + j * 46, 22, 28); c.set_source_rgb(*thread); c.fill()
    # number panel
    if digits:
        xx = x + 20
        for j, sz in enumerate(digits):
            T(c, "7", xx, y + 120, sz, DARK, stroke=None, anchor="left")
            xx += sz * 0.62
    else:
        T(c, "7GA 123456", x + 170, y + 120, 34, DARK, stroke=None)


def lerp(a, b, q):
    return tuple(a[i] + (b[i] - a[i]) * q for i in range(3))


def lv1(c, t, r):
    tilt = 0.5 + 0.5 * math.sin(t * 2.4)
    for i, y in enumerate(YS):
        fake = i == 1
        col = GRN_ if fake else lerp(GRN_, BLU_, tilt)
        c.save(); c.translate(560, y); c.transform(__import__('cairo').Matrix(1, 0, -0.18 * (tilt - 0.5), 1, 0, 0))
        note(c, 0, 0, thread=col)
        c.restore()
        if r > 0 and fake:
            S.rrect(c, 130, y - 185, 860, 370, 26); c.set_source_rgba(*GRN, r); c.set_line_width(12); c.stroke()


def lv2(c, t, r):
    light = 0.5 + 0.5 * math.sin(t * 2.0)
    c.arc(990, 330, 60, 0, 2 * math.pi); c.set_source_rgba(1, 0.95, 0.6, 0.25 + 0.4 * light); c.fill()
    for i, y in enumerate(YS):
        fake = i == 2
        note(c, 560, y, thread=BLU_, wm=not fake, light=light)
        if r > 0 and fake:
            S.rrect(c, 130, y - 185, 860, 370, 26); c.set_source_rgba(*GRN, r); c.set_line_width(12); c.stroke()


ASC = [30, 34, 38, 43, 48, 54, 60]
FLAT = [40] * 7


def lv3(c, t, r):
    for i, y in enumerate(YS):
        fake = i == 0
        note(c, 560, y, thread=BLU_, digits=FLAT if fake else ASC)
        if r > 0 and fake:
            S.rrect(c, 130, y - 185, 860, 370, 26); c.set_source_rgba(*GRN, r); c.set_line_width(12); c.stroke()


LABELS = [(L, 110, y) for L, y in zip(LABS, YS)]
LEVELS = [
    dict(name="LEVEL 1: TILT IT", q="WHICH NOTE IS FAKE?", ans="B IS FAKE!", stamp="THREAD STAYS GREEN", draw=lv1, labels=LABELS),
    dict(name="LEVEL 2: HOLD TO LIGHT", q="WHICH NOTE IS FAKE?", ans="C IS FAKE!", stamp="NO WATERMARK", draw=lv2, labels=LABELS),
    dict(name="FINAL: NUMBER PANEL", q="WHICH NOTE IS FAKE?", ans="A IS FAKE!", stamp="DIGITS DON'T GROW", draw=lv3, labels=LABELS),
]

if __name__ == "__main__":
    g = IL.Illusion(D, CAPS, LEVELS, "SAME BRO GAMES #20", ("FIND THE FAKE NOTE", "3 LEVELS"), mood='chill')
    if sys.argv[1] == "preview":
        L = g.L
        g.preview([1.0, 4.0, L[0][1] - 0.5, L[1][0] + 2, L[2][0] + 2, L[3][0] + 1.2, L[4][0] + 3, L[5][0] + 2.5, g.dur - 0.5],
                  f"{D}/prev.png")
        print("dur", round(g.dur, 1), [round(a, 1) for a, b in L])
    else:
        g.render(f"{D}/short.mp4")
