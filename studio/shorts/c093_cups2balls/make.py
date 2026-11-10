"""Same Bro Games #11: cup shuffle with TWO balls, 4 cups (engine: studio/shorts/game.py, ball2=...)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import game as G  # noqa: E402

D = "/home/claude/sid/shorts/c093_cups2balls"
SEGS = [(0.0, 4.98), (5.4, 9.06), (9.37, 13.95)]  # vo.mp3 line ranges (silence gaps 4.95-5.40, 9.04-9.37)
CAPS = ["This time TWO balls, 4 cups. Track BOTH. Miss one and you lose.",
        "STOP! Which cups have the balls? Comment 2 numbers.",
        "HERE they are! Got both? Then you're a LEGEND. No? Watch again."]
g = G.CupGame(D, SEGS, CAPS, ("TWO BALLS. 4 CUPS.", "TRACK BOTH."), "SAME BRO GAMES #11", seed=93, mood='chill',
              levels=((5, 0.62), (6, 0.46), (7, 0.36)), ncups=4, start_cup=0, ball2=2, cup_col=(0.2, 0.42, 0.85))

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.2, 1.5, 3.3, g.swaps[2][0] + 0.2, g.swaps[8][0] + 0.15, g.swaps[14][0] + 0.1, g.t_freeze + 1, g.t_count + 0.5,
              g.t_count + 2.5, g.t_reveal + 0.5, g.t_reveal + 2.5, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answer", [q + 1 for q in g.final_slots], "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
