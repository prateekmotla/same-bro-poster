"""Same Bro Games #16: cup shuffle SPEED RUN, 3 cups, 1 ball, fast swaps (engine: studio/shorts/game.py)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import game as G  # noqa: E402

D = "/home/claude/sid/shorts/c113_cupspeed"
SEGS = [(0.0, 5.47), (5.81, 9.74), (10.1, 14.67)]  # vo.mp3 line ranges (gaps 5.47-5.81, 9.74-10.10)
CAPS = ["SPEED RUN! 3 cups, 1 ball, and this time the shuffle is DOUBLE speed. Don't blink.",
        "STOP! Which cup has the ball? Comment 1, 2 or 3.",
        "HERE it is! Got it? Then your eyes are FAST. No? Watch again."]
g = G.CupGame(D, SEGS, CAPS, ("SPEED RUN", "DOUBLE SPEED SHUFFLE"), "SAME BRO GAMES #16", seed=113, mood='tense',
              levels=((6, 0.38), (7, 0.28), (8, 0.22)), start_cup=1, cup_col=(0.95, 0.5, 0.1))

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.2, 1.5, 3.3, g.swaps[2][0] + 0.1, g.swaps[10][0] + 0.1, g.swaps[18][0] + 0.08, g.t_freeze + 1, g.t_count + 0.5,
              g.t_reveal + 0.5, g.t_reveal + 2.5, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answer", g.final_slots[0] + 1 if hasattr(g, 'final_slots') else None, "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
