"""Same Bro Games #1: cup shuffle (engine: studio/shorts/game.py)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import game as G  # noqa: E402

D = "/home/claude/sid/shorts/s64_cups"
SEGS = [(0.0, 3.70), (3.80, 8.20), (8.25, 13.44)]  # vo.mp3 line ranges (silence gaps at 3.55-3.97 and 8.01-8.41)
CAPS = ["Keep your eyes on the ball. Track it and you're a LEGEND.",
        "STOP! Which cup has the ball? Comment 1, 2 or 3.",
        "It's HERE! Same bro? Lost it halfway? Watch again. It won't get slower."]
g = G.CupGame(D, SEGS, CAPS, ("TRACK THE BALL", "ONLY LEGENDS CAN"), "SAME BRO GAMES #1", seed=11, mood='chill')

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.2, 1.5, 3.3, g.swaps[2][0] + 0.2, g.swaps[6][0] + 0.15, g.swaps[10][0] + 0.1, g.t_freeze + 1, g.t_count + 0.5,
              g.t_count + 2.5, g.t_reveal + 0.5, g.t_reveal + 2.5, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answer", g.final_slot + 1, "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
