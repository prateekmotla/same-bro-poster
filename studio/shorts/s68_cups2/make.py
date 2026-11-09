"""Same Bro Games #2: cup shuffle HARD, 4 cups (engine: studio/shorts/game.py, ncups=4)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import game as G  # noqa: E402

D = "/home/claude/sid/shorts/s68_cups2"
SEGS = [(0.0, 4.55), (4.65, 9.25), (9.35, 14.16)]  # vo.mp3 line ranges (silence gaps 4.42-4.77, 9.13-9.54)
CAPS = ["Level up. FOUR cups this time. Eyes on the ball, don't blink.",
        "STOP! Which cup has the ball? Comment 1, 2, 3 or 4.",
        "It's HERE! Got it right? Tell us in the comments. Missed it? Watch again."]
g = G.CupGame(D, SEGS, CAPS, ("4 CUPS. 1 BALL.", "CAN YOU TRACK IT?"), "SAME BRO GAMES #2", seed=57, mood='tense',
              levels=((6, 0.72), (7, 0.5), (8, 0.34)), ncups=4, start_cup=2, cup_col=(0.16, 0.42, 0.86))

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.2, 1.5, 3.3, g.swaps[2][0] + 0.2, g.swaps[8][0] + 0.15, g.swaps[14][0] + 0.1, g.t_freeze + 1, g.t_count + 0.5,
              g.t_count + 2.5, g.t_reveal + 0.5, g.t_reveal + 2.5, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answer", g.final_slot + 1, "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
