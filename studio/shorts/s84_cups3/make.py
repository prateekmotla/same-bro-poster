"""Same Bro Games #6: cup shuffle IMPOSSIBLE, 4 cups, full speed (engine: studio/shorts/game.py, ncups=4)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import game as G  # noqa: E402

D = "/home/claude/sid/shorts/s84_cups3"
SEGS = [(0.0, 6.5), (6.6, 11.45), (11.5, 16.72)]  # vo.mp3 line ranges (silence gaps 6.31-6.76, 11.26-11.70)
CAPS = ["IMPOSSIBLE level. 4 cups, FULL speed. Let's see if you can track it. Don't blink.",
        "STOP! Which cup has the ball? Comment 1, 2, 3 or 4.",
        "It's HERE! Got it? Then you're a LEGEND. Missed it? Watch again."]
g = G.CupGame(D, SEGS, CAPS, ("IMPOSSIBLE LEVEL.", "TRACK THE BALL."), "SAME BRO GAMES #6", seed=73, mood='tense',
              levels=((7, 0.5), (8, 0.34), (10, 0.26)), ncups=4, start_cup=3, cup_col=(0.12, 0.55, 0.38))

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.2, 1.5, 3.3, g.swaps[2][0] + 0.2, g.swaps[8][0] + 0.15, g.swaps[18][0] + 0.1, g.t_freeze + 1, g.t_count + 0.5,
              g.t_count + 2.5, g.t_reveal + 0.5, g.t_reveal + 2.5, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answer", g.final_slot + 1, "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
