"""BRAVE vs NORMAL — WHO'S RIGHT? #24: hand burnt while making chai (engine: studio/shorts/dilemma.py).
Facts: British Red Cross 'Burns' first aid: cool the burn under cold running water for at least 20 minutes;
butter, cream or toothpaste will not cool the area (oils retain heat); after cooling, loosely cover with cling film
or a clean plastic bag; seek medical advice for burns to the face, or if in doubt. NHS 'Burns and scalds -
treatment': do not use ice, iced water, creams or greasy substances like butter.
Brand-safe: no wound shown, only a small pink mark; Brave ends on the red WRONG freeze."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import dilemma as DL  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, S, RED, GRN, WHITE, YEL  # noqa: E402

D = "/home/claude/sid/shorts/c150_burn"
CAPS = [
    "Making chai and you BURN your hand. Brave: rub ice, then toothpaste. Normal: hold it under cool running water. You?",
    "Brave rubs ice, then smears toothpaste. Feels cool for a bit, but the burn isn't cooled.",
    "Normal puts the hand under the tap. 20 minutes of cool running water.",
    "WHO'S RIGHT? Comment B or N.",
    "NORMAL is right. Red Cross: at least 20 MINUTES of cool running water.",
    "Toothpaste and butter don't cool a burn, and the NHS says no ice either.",
    "Then cover it loosely with cling film. Big burn or on the face? Straight to a doctor.",
    "Real brave = doing it right. What would YOU do?",
]
ROLES = dict(intro=[1], brave=[2], normal=[3], ask=[4], reveal=[5], why=[6, 7], end=[8])
CFG = dict(series="BRAVE vs NORMAL #24", question=("BURNT YOUR HAND?", "WHAT DO YOU DO?"),
           brave="ICE + TOOTHPASTE", normal="COOL RUNNING WATER", answer='N', grade='warm',
           why_title="BURN? DO THIS",
           why_rows=[("Cool running water", WHITE), ("At least 20 minutes", GRN), ("NO ice", RED),
                     ("NO toothpaste / butter", RED), ("Cover loosely: cling film", WHITE), ("Big or on face? Doctor", YEL)],
           src="SRC: British Red Cross + NHS burns first aid", end=("BRAVE OR SMART?", "COMMENT  B  or  N"))

GROUND = 880


def kitchen(c, t):
    c.rectangle(-400, 0, 1880, GROUND); c.set_source_rgb(0.93, 0.88, 0.78); c.fill()
    for j in range(16):            # wall tiles
        for r in range(5):
            S.rrect(c, -380 + j * 120, 330 + r * 70, 112, 62, 6); c.set_source_rgb(0.86, 0.92, 0.9); c.fill()
    S.rrect(c, -100, 90, 380, 200, 16); c.set_source_rgb(0.55, 0.38, 0.25); c.fill()       # cabinet
    S.rrect(c, 780, 90, 380, 200, 16); c.fill()
    c.rectangle(-400, 690, 1880, 40); c.set_source_rgb(0.25, 0.25, 0.28); c.fill()        # counter top
    c.rectangle(-400, 730, 1880, GROUND - 730); c.set_source_rgb(0.6, 0.42, 0.28); c.fill()
    # stove + chai pan with steam
    S.rrect(c, 700, 650, 300, 40, 8); c.set_source_rgb(0.15, 0.15, 0.17); c.fill()
    S.rrect(c, 760, 580, 180, 70, 14); c.set_source_rgb(0.7, 0.7, 0.74); c.fill()
    c.rectangle(940, 600, 110, 14); c.fill()
    for j in range(3):
        ph = (t * 0.6 + j / 3) % 1
        c.arc(800 + j * 50 + 15 * math.sin(t * 2 + j), 560 - ph * 160, 18 + ph * 14, 0, 2 * math.pi)
        c.set_source_rgba(1, 1, 1, 0.5 * (1 - ph)); c.fill()
    c.rectangle(-400, GROUND, 1880, 220); c.set_source_rgb(0.5, 0.4, 0.33); c.fill()


def sink(c, t, flow=False):
    S.rrect(c, 120, 640, 300, 60, 10); c.set_source_rgb(0.8, 0.82, 0.85); c.fill()
    c.rectangle(250, 470, 22, 120); c.set_source_rgb(0.65, 0.66, 0.7); c.fill()
    c.rectangle(250, 470, 110, 22); c.fill()
    c.rectangle(340, 470, 22, 50); c.fill()
    if flow:
        for j in range(8):
            ph = (t * 3 + j / 8) % 1
            c.rectangle(343 + 6 * math.sin(j), 520 + ph * 130, 16, 22); c.set_source_rgba(0.5, 0.78, 1.0, 0.85); c.fill()


def bubble(c, x, y, txt, col=(1, 1, 1)):
    w = len(txt) * 23 + 60
    S.rrect(c, x - w / 2, y, w, 74, 30); c.set_source_rgba(*col, 0.95); c.fill()
    T(c, txt, x, y + 50, 34, (0.1, 0.1, 0.15), stroke=None)


def scene(c, side, t, p):
    kitchen(c, t)
    if side == 'B':
        K.sid(c, t, 380, 330, 0.42, mouth='o' if p > 0.55 else 'smile', look=(0.6, 0.3),
              arms=((60, 60), (90, 50)), eyes=1.1)
        hx, hy = 470, 640
        c.arc(hx, hy, 12, 0, 2 * math.pi); c.set_source_rgba(0.95, 0.5, 0.5, 0.8); c.fill()      # small pink mark
        if p < 0.45:   # ice cube
            S.rrect(c, hx + 20 + 10 * math.sin(t * 9), hy - 40, 56, 56, 10); c.set_source_rgba(0.8, 0.93, 1.0, 0.95); c.fill()
            bubble(c, 540, 220, "RUB SOME ICE!", (1, 0.85, 0.8))
        else:          # toothpaste tube
            c.save(); c.translate(hx + 60, hy - 60); c.rotate(-0.6)
            S.rrect(c, -20, -70, 40, 130, 10); c.set_source_rgb(1, 1, 1); c.fill()
            c.rectangle(-20, -70, 40, 30); c.set_source_rgb(0.2, 0.5, 0.95); c.fill()
            c.restore()
            c.arc(hx, hy, 22, 0, 2 * math.pi); c.set_source_rgba(1, 1, 1, 0.9); c.fill()
            bubble(c, 540, 220, "TOOTHPASTE ON IT!", (1, 0.85, 0.8))
        if p > 0.6:
            S.rrect(c, 300, 310, 480, 56, 20); c.set_source_rgba(*RED, 0.92); c.fill()
            T(c, "BURN NOT COOLED!", 540, 348, 30, WHITE, stroke=None)
    else:
        sink(c, t, flow=p > 0.12)
        B.figure(c, 500, 330, 0.42, t, who='friend', mouth='flat', look=(-0.6, 0.3),
                 arms=((-150, 55), (40, 40)))
        msg = "UNDER THE TAP" if p < 0.4 else "COOL RUNNING WATER"
        bubble(c, 540, 220, msg)
        # 20 minute timer
        m = int(20 * S.ease(min(1, p / 0.95)))
        c.arc(820, 420, 70, 0, 2 * math.pi); c.set_source_rgba(0.05, 0.4, 0.15, 0.92); c.fill()
        c.set_line_width(10); c.set_source_rgb(*GRN)
        c.arc(820, 420, 70, -math.pi / 2, -math.pi / 2 + 2 * math.pi * m / 20); c.stroke()
        T(c, f"{m} MIN", 820, 435, 34, WHITE, stroke=None)


def build():
    return DL.Dilemma(D, CAPS, ROLES, scene, CFG, mood='tense')


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview(sh.preview_times(), f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in sh.L])
    else:
        sh.render(f"{D}/short.mp4")
