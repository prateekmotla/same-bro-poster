"""Same Bro Games #24: FESTIVAL odd one out — find the different diya, 3 levels (engine: studio/shorts/oddgrid.py).
Level variants (odd diya only): L1 'noflame' (unlit), L2 'lean' (flame leans the other way), L3 'dots' (2 dots
instead of 3 on the clay bowl). Fair: every difference is visible at a pause, nothing moves."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import oddgrid as OG  # noqa: E402

D = "/home/claude/sid/shorts/c145_odddiya"
SEGS = [(0.0, 7.34), (7.7, 13.04), (13.3, 18.54)]  # vo.mp3 line ranges (silence gaps 7.34-7.73, 13.04-13.33)
CAPS = ["FESTIVAL SPECIAL, ODD ONE OUT! Every level has ONE diya that's different. Find it before the timer ends.",
        "STOP! Last level. Found it? Comment row and column, like C5.",
        "It's HERE! Got all 3 levels? Your eyes are sharp. Play again."]


def diya(c, x, y, r, var=None):
    # flame (behind the bowl rim)
    if var != 'noflame':
        lean = -1 if var == 'lean' else 1
        c.save(); c.translate(x, y - r * 0.18)
        c.move_to(-r * 0.2, 0)
        c.curve_to(-r * 0.25, -r * 0.4, r * 0.05 * lean + r * 0.12 * lean, -r * 0.6, r * 0.28 * lean, -r * 0.95)
        c.curve_to(r * 0.25 * lean - r * 0.02, -r * 0.55, r * 0.3, -r * 0.3, r * 0.2, 0)
        c.close_path(); c.set_source_rgb(1.0, 0.62, 0.12); c.fill()
        c.move_to(-r * 0.09, -r * 0.02)
        c.curve_to(-r * 0.1, -r * 0.25, r * 0.12 * lean, -r * 0.4, r * 0.16 * lean, -r * 0.62)
        c.curve_to(r * 0.12 * lean, -r * 0.35, r * 0.14, -r * 0.2, r * 0.09, -r * 0.02)
        c.close_path(); c.set_source_rgb(1.0, 0.93, 0.5); c.fill()
        c.restore()
    else:   # unlit wick
        c.move_to(x, y - r * 0.15); c.line_to(x + r * 0.05, y - r * 0.38)
        c.set_source_rgb(0.25, 0.2, 0.18); c.set_line_width(r * 0.07); c.stroke()
    # clay bowl
    c.move_to(x - r * 0.95, y - r * 0.15)
    c.curve_to(x - r * 0.85, y + r * 0.6, x + r * 0.85, y + r * 0.6, x + r * 0.95, y - r * 0.15)
    c.close_path(); c.set_source_rgb(0.78, 0.33, 0.14); c.fill()
    c.save(); c.translate(x, y - r * 0.15); c.scale(1, 0.22); c.arc(0, 0, r * 0.95, 0, 2 * math.pi); c.restore()
    c.set_source_rgb(0.55, 0.2, 0.08); c.fill()
    # dots on the bowl
    n = 2 if var == 'dots' else 3
    for q in range(n):
        dx = (q - (n - 1) / 2) * r * 0.42
        c.arc(x + dx, y + r * 0.2, r * 0.1, 0, 2 * math.pi); c.set_source_rgb(1.0, 0.85, 0.3); c.fill()


g = OG.OddGrid(D, SEGS, CAPS, ("FESTIVAL: ODD ONE OUT", "FIND THE DIFFERENT DIYA"), "SAME BRO GAMES #24", seed=1451,
               mood='warm', icon=diya, levels=((6, 'noflame', 5.0), (7, 'lean', 5.8), (8, 'dots', 6.6)))

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        L = g.lv
        ts = [0.3, 2.0, L[0][1] + 0.6, L[1][0] + 2, L[1][1] + 0.6, L[2][0] + 2, g.t_freeze + 1, g.t_count + 1.5,
              g.t_reveal + 0.6, g.t_reveal + 2.5, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "answers", [f"{'ABCDEFG'[p[0]]}{p[1]+1}" for *_, p in g.lv])
    else:
        g.render(f"{D}/short.mp4")
