"""Same Bro Games #18: spot 3 differences at a chai stall (engine: studio/shorts/spotdiff.py).
Differences (B only): price board CHAI Rs 10 > Rs 15, rusk-jar lid red > blue, extra kulhad on the bench.
Generic stall, no brand names."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import spotdiff as SD  # noqa: E402
import kit as K  # noqa: E402
from kit import T, S  # noqa: E402

D = "/home/claude/sid/shorts/c121_spotchai"
SEGS = [(0.0, 7.0), (7.3, 11.0), (11.35, 17.0)]  # vo.mp3 line ranges (silence gaps ~7.17, ~11.2)
CAPS = ["SPOT THE DIFFERENCE! Chai stall: A on top, B below. 3 things are different. Timer's on, find them.",
        "STOP! How many did you find? Comment 1, 2 or 3.",
        "Here are all 3! Got them all? Your eyes are stronger than kadak chai. Look again."]


def board(c, price):
    S.rrect(c, 560, 70, 800, 150, 20); c.set_source_rgb(0.75, 0.12, 0.1); c.fill()
    S.rrect(c, 575, 85, 770, 120, 14); c.set_source_rgb(0.95, 0.85, 0.3); c.fill()
    T(c, f"CHAI  ₹{price}", 960, 172, 82, (0.45, 0.08, 0.06), stroke=None)


def jar(c, lid):
    S.rrect(c, 1180, 420, 150, 190, 26); c.set_source_rgba(0.85, 0.92, 0.95, 0.85); c.fill()
    for j in range(3):
        S.rrect(c, 1200, 470 + j * 42, 110, 30, 8); c.set_source_rgb(0.85, 0.62, 0.3); c.fill()
    S.rrect(c, 1170, 395, 170, 40, 12); c.set_source_rgb(*lid); c.fill()


def kulhad(c, x, y, s=1.0):
    c.move_to(x - 30 * s, y - 50 * s); c.line_to(x + 30 * s, y - 50 * s); c.line_to(x + 22 * s, y); c.line_to(x - 22 * s, y)
    c.close_path(); c.set_source_rgb(0.72, 0.36, 0.2); c.fill()
    c.save(); c.scale(1, 0.3); c.arc(x, (y - 50 * s) / 0.3, 30 * s, 0, 2 * math.pi); c.restore()
    c.set_source_rgb(0.85, 0.65, 0.42); c.fill()


def scene(c, t):
    c.rectangle(0, 0, 1920, 1080); c.set_source_rgb(0.93, 0.83, 0.66); c.fill()            # wall
    for j in range(0, 1920, 160):
        c.rectangle(j, 0, 4, 640); c.set_source_rgba(0, 0, 0, 0.05); c.fill()
    c.rectangle(0, 640, 1920, 440); c.set_source_rgb(0.55, 0.5, 0.46); c.fill()              # road
    # tarp roof
    for j in range(8):
        c.move_to(400 + j * 140, 230); c.line_to(470 + j * 140, 300); c.line_to(540 + j * 140, 230); c.close_path()
        c.set_source_rgb(0.15, 0.45, 0.8) if j % 2 else c.set_source_rgb(0.95, 0.95, 0.95); c.fill()
    c.rectangle(400, 220, 1120, 16); c.set_source_rgb(0.3, 0.3, 0.35); c.fill()
    board(c, 10)
    # counter
    c.rectangle(420, 610, 1080, 300); c.set_source_rgb(0.55, 0.36, 0.2); c.fill()
    for j in range(5):
        c.rectangle(420, 640 + j * 56, 1080, 6); c.set_source_rgba(0, 0, 0, 0.15); c.fill()
    # stove + kettle
    c.rectangle(560, 560, 260, 50); c.set_source_rgb(0.2, 0.2, 0.22); c.fill()
    c.arc(690, 480, 95, math.pi, 2 * math.pi); c.rectangle(595, 480, 190, 80); c.set_source_rgb(0.78, 0.78, 0.8); c.fill()
    c.move_to(785, 500); c.line_to(860, 440); c.set_source_rgb(0.7, 0.7, 0.72); c.set_line_width(18); c.stroke()
    for j in range(3):   # steam (same in both)
        ph = (t * 0.5 + j / 3) % 1
        c.arc(870 + 20 * math.sin(ph * 6), 420 - ph * 160, 18 + 12 * ph, 0, 2 * math.pi)
        c.set_source_rgba(1, 1, 1, 0.5 * (1 - ph)); c.fill()
    # kulhad stack
    for j in range(4):
        kulhad(c, 960 + j * 50, 610)
    jar(c, (0.85, 0.15, 0.15))
    # bench
    c.rectangle(80, 760, 300, 26); c.set_source_rgb(0.4, 0.27, 0.16); c.fill()
    for lx in (100, 340):
        c.rectangle(lx, 786, 20, 120); c.fill()
    K.sid(c, 1.0, 1650, 420, 0.42, mouth='smile', arms=((14, -10), (40, 110)))
    kulhad(c, 1700, 735, 0.8)


def board_b(c, t):
    board(c, 15)


def jar_b(c, t):
    S.rrect(c, 1170, 395, 170, 40, 12); c.set_source_rgb(0.15, 0.4, 0.9); c.fill()


def cup_b(c, t):
    kulhad(c, 240, 760, 0.9)


DIFFS = [(960, 145, 240, board_b), (1255, 415, 110, jar_b), (240, 735, 80, cup_b)]
g = SD.SpotDiff(D, SEGS, CAPS, ("SPOT 3 DIFFERENCES", "AT THE CHAI STALL"), "SAME BRO GAMES #18", scene, DIFFS, hunt=16.0,
                mood='warm', label="CHAI STALL")

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.2, 3.0, 12.0, g.t_freeze + 1, g.t_count + 1.5, g.t_reveal + 0.6, g.t_reveal + 2.6, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
