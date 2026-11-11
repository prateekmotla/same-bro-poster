"""Same Bro Games #17: odd colour out HARD MODE (smaller colour gaps than #9), 3 levels (engine: studio/shorts/oddgrid.py)."""
import colorsys
import json
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import oddgrid as OG  # noqa: E402

D = "/home/claude/sid/shorts/c117_oddhard"
SEGS = json.load(open(f"{D}/segs.json"))
CAPS = ["EYE TEST, HARD MODE. One circle per level is a TINY bit different. Even harder than last time. Find it before the timer ends.",
        "STOP! Last level. Found it? Comment row and column, like C5.",
        "It's HERE! Got all 3? Your eyes are PRO level. Try again."]
HUES = {0.075: 0.08, 0.05: 0.75, 0.032: 0.5}  # level odd-lightness delta -> base hue (orange, purple, teal)


def dot(c, x, y, r, var=None, _lvl=[None]):
    # var is the level's delta for the odd circle, None for normal ones; base hue follows the current level
    hue = OG_LEVEL_HUE[0]
    l = 0.55 + (var or 0)
    rr, gg, bb = colorsys.hls_to_rgb(hue, l, 0.62)
    c.arc(x, y, r, 0, 2 * math.pi); c.set_source_rgb(rr, gg, bb); c.fill()


OG_LEVEL_HUE = [0.58]
g = OG.OddGrid(D, SEGS, CAPS, ("EYE TEST: HARD MODE", "FIND THE ODD COLOUR"), "SAME BRO GAMES #17", seed=1173, mood='chill', icon=dot,
               levels=((6, 0.075, 5.4), (7, 0.05, 6.0), (8, 0.032, 6.8)))
_orig = g.grid


def grid(c, t, li, ra):
    OG_LEVEL_HUE[0] = HUES[g.lv[li][3]]
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
