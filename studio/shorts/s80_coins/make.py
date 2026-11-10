"""Same Bro Games #5: count the ₹10 coins (engine: studio/shorts/countgame.py). Answer: 9."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import countgame as CG  # noqa: E402

D = "/home/claude/sid/shorts/s80_coins"
SEGS = [(0.0, 6.4), (6.5, 9.85), (9.95, 15.36)]  # vo.mp3 line ranges (gaps 6.24-6.65, 9.63-10.11)
CAPS = ["COUNT THE ₹10 COINS! Lots of coins on the table, but count ONLY the ₹10 ones. Timer's on.",
        "STOP! How many ₹10 coins? Comment the number.",
        "The answer is 9! Counted right? Then your focus is top class. Try again."]
g = CG.CountGame(D, SEGS, CAPS, ("COUNT THE ₹10 COINS", "ONLY THE ₹10 ONES"), "SAME BRO GAMES #5", target=10, n_target=9,
                 others=((1, 6), (2, 6), (5, 7)), hunt=12.0, seed=69, mood='chill')
assert g.answer == 9

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.3, 1.5, 9.0, g.t_freeze + 1, g.t_count + 1.5, g.t_reveal + 1.5, g.t_reveal + 4.0, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1), len(g.targets))
    else:
        g.render(f"{D}/short.mp4")
