"""Same Bro Games #14: odd number out, 3 levels (engine: studio/shorts/oddgrid.py).
Level tiles: 69 with one 96 (5x5), 808 with one 880 (6x6), 7171 with one 7117 (7x7)."""
import json
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import oddgrid as OG  # noqa: E402
from kit import T, S  # noqa: E402

D = "/home/claude/sid/shorts/c105_oddnum"
SEGS = json.load(open(f"{D}/segs.json"))
CAPS = ["ODD NUMBER OUT! In every level all the numbers are the same, only ONE is different. Find it, timer's on.",
        "STOP! Last level. Found it? Comment row and column, like D2.",
        "It's HERE! Got all 3? Then your brain is sharp. Try again."]
NUM = {'96': ("69", "96"), '880': ("808", "880"), '7117': ("7171", "7117")}
CUR = ['96']


def tile(c, x, y, r, var=None):
    norm, odd = NUM[CUR[0]]
    txt = odd if var else norm
    S.rrect(c, x - r * 1.05, y - r * 0.8, r * 2.1, r * 1.6, r * 0.25); c.set_source_rgb(0.93, 0.94, 0.98); c.fill()
    sz = r * (0.95 if len(txt) <= 2 else 0.78 if len(txt) == 3 else 0.62)
    T(c, txt, x, y + sz * 0.36, sz, (0.1, 0.1, 0.16), stroke=None)


g = OG.OddGrid(D, SEGS, CAPS, ("ODD NUMBER", "OUT"), "SAME BRO GAMES #14", seed=105, mood='chill', icon=tile,
               levels=((5, '96', 5.0), (6, '880', 5.6), (7, '7117', 6.4)))
_orig = g.grid


def grid(c, t, li, ra):
    CUR[0] = g.lv[li][3]
    return _orig(c, t, li, ra)


g.grid = grid

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        L = g.lv
        ts = [0.3, 2.0, L[0][1] + 0.6, L[1][0] + 2, L[1][1] + 0.6, L[2][0] + 2, g.t_freeze + 1, g.t_count + 1.5,
              g.t_reveal + 0.6, g.t_reveal + 2.5, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answers", [f"{'ABCDEFG'[p[0]]}{p[1]+1}" for *_, p in g.lv])
    else:
        g.render(f"{D}/short.mp4")
