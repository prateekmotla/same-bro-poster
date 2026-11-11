"""Same Bro Games #22: count the triangles (engine: studio/shorts/tricount.py).
Figure: 4 lines from the apex (2 sides + 2 inside) x 2 horizontals (middle line + base) = C(4,2) x 2 = 12 triangles."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tricount as TC  # noqa: E402

D = "/home/claude/sid/shorts/c137_triangles"
SEGS = [(0.0, 6.14), (6.48, 9.14), (9.51, 14.56)]  # vo.mp3 line ranges (silencedetect gaps 6.14-6.53, 9.14-9.56)
CAPS = ["HOW MANY TRIANGLES? Count them! Looks easy, but most people miss a few. Timer's on.",
        "STOP! How many triangles? Comment the number.",
        "The answer is 12! Counted right? Then your eyes are sharp. Try again."]
g = TC.TriCount(D, SEGS, CAPS, ("COUNT THE TRIANGLES", "HOW MANY?"), "SAME BRO GAMES #22", hunt=13.0, seed=137, mood='chill')
assert g.answer == 12, g.answer

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.3, 5.0, g.t_freeze + 1, g.t_count + 1.5, g.t_reveal + 0.5, g.t_reveal + 2.5, g.t_reveal + 5.2, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answer", g.answer)
    else:
        g.render(f"{D}/short.mp4")
