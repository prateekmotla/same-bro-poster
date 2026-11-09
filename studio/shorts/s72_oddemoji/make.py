"""Same Bro Games #3: odd face out, 3 levels (engine: studio/shorts/oddgrid.py)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import oddgrid as OG  # noqa: E402

D = "/home/claude/sid/shorts/s72_oddemoji"
SEGS = [(0.0, 6.25), (6.3, 11.75), (11.8, 16.56)]  # vo.mp3 line ranges (silence gaps 6.06-6.45, 11.61-11.91)
CAPS = ["ODD ONE OUT. Every level has ONE face that's different. Find it before the timer ends.",
        "STOP! Last level. Found it? Comment row and column, like C5.",
        "It's HERE! Got all 3 levels? Your eyes are sharp. Play again."]
g = OG.OddGrid(D, SEGS, CAPS, ("ODD ONE OUT", "FIND THE DIFFERENT FACE"), "SAME BRO GAMES #3", seed=61, mood='chill',
               levels=((6, 'frown', 5.0), (7, 'brow', 5.6), (8, 'wink', 6.4)))

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        L = g.lv
        ts = [0.2, 1.0, 3.0, L[0][1] + 0.6, L[1][0] + 2, L[1][1] + 0.6, L[2][0] + 2, g.t_freeze + 1, g.t_count + 1.5,
              g.t_reveal + 0.6, g.t_reveal + 2.5, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answer", g.answer, "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
