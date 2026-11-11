"""Same Bro Games #26: cup shuffle FINALE - easy, hard and impossible levels back to back in one round, 4 cups
(engine: studio/shorts/game.py CupGame)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import game as G  # noqa: E402

D = "/home/claude/sid/shorts/c153_cupsfinale"
SEGS = [(0.0, 5.9), (6.1, 10.6), (10.9, 16.2)]  # vo.mp3 line ranges (silence gaps 5.81-6.21, 10.54-11.02)
CAPS = ["FINALE! Easy, hard, impossible - all 3 levels in ONE round. Don't blink.",
        "STOP! Which cup has the ball? Comment 1, 2, 3 or 4.",
        "It's HERE! Got it? Then you're a LEGEND. Missed it? Watch again."]
g = G.CupGame(D, SEGS, CAPS, ("THE FINALE.", "ALL 3 LEVELS."), "SAME BRO GAMES #26", seed=153, mood='tense',
              levels=((5, 0.62), (7, 0.4), (9, 0.27)), ncups=4, start_cup=2, cup_col=(0.75, 0.2, 0.25))

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.2, 1.5, 3.3, g.swaps[2][0] + 0.2, g.swaps[8][0] + 0.15, g.swaps[18][0] + 0.1, g.t_freeze + 1, g.t_count + 0.5,
              g.t_count + 2.5, g.t_reveal + 0.5, g.t_reveal + 2.5, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answer", g.final_slot + 1, "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
