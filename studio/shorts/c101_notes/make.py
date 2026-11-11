"""Same Bro Games #13: add up all the notes on the table (engine: studio/shorts/countgame.py, total=True).
Generic labelled notes (not replicas): 2x10, 2x20, 2x50, 3x100, 1x200, 1x500 = Rs 1,160."""
import json
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import countgame as CG  # noqa: E402
from kit import T, S  # noqa: E402

D = "/home/claude/sid/shorts/c101_notes"
SEGS = json.load(open(f"{D}/segs.json"))
CAPS = ["TOTAL THE NOTES! Different notes lying on the table. Add them ALL up, timer's on.",
        "STOP! What's the total? Comment it in rupees.",
        "The total is ₹1,160! Added it right? Then your mental math is top class. Try again."]
COL = {10: (0.78, 0.6, 0.45), 20: (0.85, 0.8, 0.35), 50: (0.45, 0.78, 0.82), 100: (0.7, 0.62, 0.85),
       200: (0.95, 0.7, 0.3), 500: (0.7, 0.72, 0.68)}


def note(c, x, y, kind, rot=0.0, a=1.0):
    w, h = 190, 96
    c.save(); c.translate(x, y); c.rotate(rot * 0.5)
    S.rrect(c, -w / 2 + 4, -h / 2 + 6, w, h, 8); c.set_source_rgba(0, 0, 0, 0.3 * a); c.fill()
    S.rrect(c, -w / 2, -h / 2, w, h, 8); c.set_source_rgba(*COL[kind], a); c.fill()
    S.rrect(c, -w / 2 + 8, -h / 2 + 8, w - 16, h - 16, 6); c.set_source_rgba(1, 1, 1, 0.35 * a); c.set_line_width(3); c.stroke()
    c.arc(-w / 2 + 40, 0, 24, 0, 2 * math.pi); c.set_source_rgba(1, 1, 1, 0.35 * a); c.fill()
    T(c, f"₹{kind}", 22, 16, 44, (0.12, 0.1, 0.12), a, stroke=None)
    c.restore()


g = CG.CountGame(D, SEGS, CAPS, ("TOTAL THE NOTES", "ADD THEM ALL"), "SAME BRO GAMES #13", total=True,
                 others=((10, 2), (20, 2), (50, 2), (100, 3), (200, 1), (500, 1)), hunt=13.0, seed=101, mood='chill',
                 draw=note, gap=230, step=0.5, margin=120)
assert g.answer == 1160, g.answer

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.3, 1.5, 9.0, g.t_freeze + 1, g.t_count + 1.5, g.t_reveal + 1.5, g.t_reveal + 5.0, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answer", g.answer, len(g.targets))
    else:
        g.render(f"{D}/short.mp4")
