"""Same Bro Games #4: spot 3 differences in Sid's room (engine: studio/shorts/spotdiff.py)."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import spotdiff as SD  # noqa: E402
import kit as K  # noqa: E402
from kit import V  # noqa: E402

D = "/home/claude/sid/shorts/s76_spot"
SEGS = [(0.0, 6.95), (7.1, 11.4), (11.5, 16.48)]  # vo.mp3 line ranges (silence gaps 6.79-7.25, 11.24-11.66)
CAPS = ["SPOT THE DIFFERENCE! Sid's room: A on top, B below. 3 things are different. Timer's on, find them.",
        "STOP! How many did you find? Comment 1, 2 or 3.",
        "Here are all 3! Got them all? Your eyes are sharp. Look again."]


def scene(c, t):
    V.room(c, 1.0, mode='day')
    K.sid(c, 1.0, 300, 420, 0.42, mouth='smile', arms=((14, -10), (14, -10)))


def poster_red(c, t):
    c.rectangle(930, 180, 170, 230); c.set_source_rgb(0.85, 0.27, 0.25); c.fill()
    c.arc(1015, 270, 50, 0, 2 * math.pi); c.set_source_rgb(0.98, 0.9, 0.7); c.fill()


def clock(c, t):
    c.arc(1260, 250, 52, 0, 2 * math.pi); c.set_source_rgb(0.97, 0.97, 0.95); c.fill_preserve()
    c.set_source_rgb(0.2, 0.2, 0.22); c.set_line_width(8); c.stroke()
    c.move_to(1260, 250); c.line_to(1260, 214); c.move_to(1260, 250); c.line_to(1288, 262)
    c.set_line_width(6); c.stroke()


def mug_red(c, t):
    c.rectangle(1750, 600, 44, 40); c.set_source_rgb(0.85, 0.2, 0.2); c.fill()
    c.arc(1798, 618, 12, -1.5, 1.5); c.set_line_width(5); c.stroke()


DIFFS = [(1015, 295, 150, poster_red), (1260, 250, 90, clock), (1775, 620, 70, mug_red)]
g = SD.SpotDiff(D, SEGS, CAPS, ("SPOT 3 DIFFERENCES", "IN SID'S ROOM"), "SAME BRO GAMES #4", scene, DIFFS, hunt=15.0,
                mood='chill')

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.2, 3.0, 12.0, g.t_freeze + 1, g.t_count + 1.5, g.t_reveal + 0.6, g.t_reveal + 2.6, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
