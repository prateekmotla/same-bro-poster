"""Same Bro Games #21: cup shuffle FAKE-OUT round: some swaps are fake (cups start to cross, then go back)
(engine: studio/shorts/game.py, new fakes= option: swap indices that only fake the move, no real swap)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import game as G  # noqa: E402

D = "/home/claude/sid/shorts/c133_cupfake"
SEGS = [(0.0, 6.79), (7.07, 11.05), (11.37, 16.11)]  # vo.mp3 line ranges (silencedetect gaps 6.79-7.12, 11.05-11.42)
CAPS = ["FAKE-OUT ROUND! 3 cups, 1 ball. Careful, some swaps are FAKE. The cups move, then go back.",
        "STOP! Which cup has the ball? Comment 1, 2 or 3.",
        "HERE it is! Dodged the fake swaps? Then you're a legend. No? Watch again."]
g = G.CupGame(D, SEGS, CAPS, ("FAKE-OUT ROUND", "SOME SWAPS ARE FAKE"), "SAME BRO GAMES #21", seed=133, mood='chill',
              levels=((6, 0.62), (7, 0.46), (8, 0.34)), start_cup=0, cup_col=(0.2, 0.55, 0.9),
              fakes=(2, 6, 10, 14, 18))

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.2, 1.5, 3.3, (g.swaps[2][0] + g.swaps[2][1]) / 2, g.swaps[9][0] + 0.1, (g.swaps[18][0] + g.swaps[18][1]) / 2, g.t_freeze + 1,
              g.t_count + 0.5, g.t_reveal + 0.5, g.t_reveal + 2.5, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answer", g.final_slot + 1, "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
