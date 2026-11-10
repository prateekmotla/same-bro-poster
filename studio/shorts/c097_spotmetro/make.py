"""Same Bro Games #12: spot 3 differences in a metro coach (engine: studio/shorts/spotdiff.py).
Differences (B only): door sign LEFT > RIGHT, backpack blue > red, water bottle on the seat."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import spotdiff as SD  # noqa: E402
import kit as K  # noqa: E402
from kit import V, T, S  # noqa: E402

D = "/home/claude/sid/shorts/c097_spotmetro"
SEGS = [(0.0, 6.82), (7.26, 10.98), (11.32, 16.45)]  # vo.mp3 line ranges (silence gaps 6.82-7.26, 10.98-11.32)
CAPS = ["SPOT THE DIFFERENCE! Metro coach: A on top, B below. 3 things are different. Timer's on, find them.",
        "STOP! How many did you find? Comment 1, 2 or 3.",
        "Here are all 3! Got them all? Your eyes are sharp even in the metro. Look again."]


def sign(c, word):
    S.rrect(c, 540, 88, 840, 84, 14); c.set_source_rgb(0.1, 0.12, 0.18); c.fill()
    T(c, f"DOORS OPEN ON THE {word}", 960, 147, 50, (1, 0.8, 0.2), stroke=None)


def bag(c, col):
    S.rrect(c, 560, 540, 150, 110, 30); c.set_source_rgb(*col); c.fill()
    S.rrect(c, 590, 580, 90, 50, 14); c.set_source_rgba(0, 0, 0, 0.18); c.fill()
    c.arc(635, 545, 30, math.pi, 2 * math.pi); c.set_source_rgb(*col); c.set_line_width(10); c.stroke()


def scene(c, t):
    V.metro(c, 0.0)
    sign(c, "LEFT")
    bag(c, (0.2, 0.4, 0.85))
    K.sid(c, 1.0, 1180, 420, 0.42, mouth='smile', arms=((14, -10), (14, -10)))


def sign_b(c, t):
    sign(c, "RIGHT")


def bag_b(c, t):
    bag(c, (0.85, 0.2, 0.2))


def bottle(c, t):
    S.rrect(c, 290, 520, 64, 125, 16); c.set_source_rgba(0.6, 0.85, 1.0, 0.95); c.fill()
    c.rectangle(305, 496, 34, 30); c.set_source_rgb(0.15, 0.45, 0.9); c.fill()


DIFFS = [(960, 130, 330, sign_b), (635, 595, 110, bag_b), (322, 585, 80, bottle)]
g = SD.SpotDiff(D, SEGS, CAPS, ("SPOT 3 DIFFERENCES", "IN THE METRO"), "SAME BRO GAMES #12", scene, DIFFS, hunt=15.0,
                mood='chill', label="METRO")

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.2, 3.0, 12.0, g.t_freeze + 1, g.t_count + 1.5, g.t_reveal + 0.6, g.t_reveal + 2.6, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
