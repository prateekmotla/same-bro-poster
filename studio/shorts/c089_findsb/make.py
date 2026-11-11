"""Same Bro Games #10: find the real SAME BRO among fakes, 3 levels (engine: studio/shorts/oddgrid.py).
Level decoys: SAME BOR (5x5), SANE BRO (6x6), SAME 8RO (7x7); exactly one tile per level reads SAME BRO."""
import json
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import oddgrid as OG  # noqa: E402
from kit import T, S  # noqa: E402

D = "/home/claude/sid/shorts/c089_findsb"
SEGS = json.load(open(f"{D}/segs.json"))
CAPS = ["Find the real SAME BRO! In every level only ONE box says SAME BRO correctly. The rest are fake. Timer's on.",
        "STOP! Last level. Found it? Comment row and column, like C4.",
        "It's HERE! Got all 3? Then you're a real Same Bro fan. Try again."]
DECOY = {'BOR': ("SAME", "BOR"), 'SANE': ("SANE", "BRO"), '8RO': ("SAME", "8RO")}
CUR = ['BOR']


def tile(c, x, y, r, var=None):
    top, bot = ("SAME", "BRO") if var else DECOY[CUR[0]]
    S.rrect(c, x - r * 1.05, y - r * 0.85, r * 2.1, r * 1.7, r * 0.25); c.set_source_rgb(0.98, 0.84, 0.2); c.fill()
    sz = r * 0.62
    T(c, top, x, y - r * 0.08, sz, (0.08, 0.08, 0.1), stroke=None)
    T(c, bot, x, y + r * 0.62, sz, (0.08, 0.08, 0.1), stroke=None)


g = OG.OddGrid(D, SEGS, CAPS, ("FIND THE REAL", "SAME BRO"), "SAME BRO GAMES #10", seed=89, mood='chill', icon=tile,
               levels=((5, 'BOR', 5.0), (6, 'SANE', 5.6), (7, '8RO', 6.4)))
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
