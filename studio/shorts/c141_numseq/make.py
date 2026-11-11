"""Same Bro Games #23: memory flash, 7 numbers one by one, which order was it? (NEW engine: studio/shorts/numseq.py).
Sequence 4 7 1 9 3 8 2. Options: A 4791382 (1/9 swapped), B 4719382 (right), C 4719832 (3/8 swapped). Answer: B."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import numseq as NS  # noqa: E402

D = "/home/claude/sid/shorts/c141_numseq"
SEGS = [(0.0, 7.61), (8.08, 10.10), (10.53, 14.25)]  # vo.mp3 line ranges (silencedetect gaps 7.61-8.08, 10.10-10.53)
CAPS = ["MEMORY TEST! 7 numbers will flash one by one. Remember them, then tell me the right order.",
        "STOP! A, B or C? Comment.",
        "The answer is B! Got it? Then your memory is sharp. Try again."]

g = NS.NumSeq(D, SEGS, CAPS, ("MEMORIZE 7 NUMBERS", "THEN PICK THE RIGHT ORDER"), "SAME BRO GAMES #23",
              seq="4719382", options=("4791382", "4719382", "4719832"), answer='B', step=0.85, t0=1.6, hunt=4.0,
              mood='chill')

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.5, 2.0, 4.6, g.t_opts + 1.5, g.t_freeze + 0.5, g.t_count + 1.5, g.t_reveal + 1.5, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
