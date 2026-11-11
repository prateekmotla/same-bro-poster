"""Same Bro Games #9: odd colour out eye test, 3 levels (engine: studio/shorts/oddgrid.py)."""
import colorsys
import json
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import oddgrid as OG  # noqa: E402

D = "/home/claude/sid/shorts/c085_oddcolour"
SEGS = json.load(open(f"{D}/segs.json"))
CAPS = ["EYE TEST. Every level has ONE circle in a slightly different colour. Find it before the timer ends.",
        "STOP! Last level. Found it? Comment row and column, like B4.",
        "It's HERE! Got all 3 levels? Your eyes are really sharp. Try again."]
HUES = {0.12: 0.58, 0.075: 0.95, 0.045: 0.36}  # level odd-lightness delta -> base hue (blue, rose, green)


def dot(c, x, y, r, var=None, _lvl=[None]):
    # var is the level's delta for the odd circle, None for normal ones; base hue follows the current level
    hue = OG_LEVEL_HUE[0]
    l = 0.55 + (var or 0)
    rr, gg, bb = colorsys.hls_to_rgb(hue, l, 0.62)
    c.arc(x, y, r, 0, 2 * math.pi); c.set_source_rgb(rr, gg, bb); c.fill()


OG_LEVEL_HUE = [0.58]
g = OG.OddGrid(D, SEGS, CAPS, ("EYE TEST", "FIND THE ODD COLOUR"), "SAME BRO GAMES #9", seed=85, mood='chill', icon=dot,
               levels=((5, 0.12, 5.0), (6, 0.075, 5.6), (7, 0.045, 6.4)))
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
