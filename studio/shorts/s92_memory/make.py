"""Same Bro Games #8: memory flash, which item vanished? (engine: studio/shorts/memgame.py). Answer: SUNGLASSES."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import memgame as MG  # noqa: E402

D = "/home/claude/sid/shorts/s92_memory"
SEGS = [(0.0, 5.5), (5.75, 8.4), (8.6, 14.15)]  # vo.mp3 line ranges (gaps 5.41-5.85, 8.26-8.67)
CAPS = ["MEMORY TEST! Look at these items carefully, just a few seconds. Then one will VANISH.",
        "STOP! Which item vanished? Comment.",
        "The answer is SUNGLASSES! Got it? Then your memory is sharp. Try again."]
g = MG.MemGame(D, SEGS, CAPS, ("MEMORIZE THESE 9", "ONE WILL VANISH"), "SAME BRO GAMES #8", missing='SUNGLASSES',
               mem=9.0, hunt=6.0, seed=81, mood='chill')

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.3, 3.0, 7.5, g.t_mem + 0.2, g.t_mem + 0.6, g.t_back + 1, g.t_freeze + 1, g.t_count + 1.5,
              g.t_reveal + 1.0, g.t_reveal + 3.0, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1), g.qslot, g.pos1[g.missing])
    else:
        g.render(f"{D}/short.mp4")
