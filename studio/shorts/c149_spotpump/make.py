"""Same Bro Games #25: spot 3 differences at a petrol pump (engine: studio/shorts/spotdiff.py).
Differences (B only): sign OPEN 24 HRS > OPEN 12 HRS, right dispenser nozzle green > red, extra traffic cone.
Generic fuel station, no brand names, no prices."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import spotdiff as SD  # noqa: E402
import kit as K  # noqa: E402
from kit import T, S  # noqa: E402

D = "/home/claude/sid/shorts/c149_spotpump"
SEGS = [(0.0, 6.79), (7.2, 10.4), (10.55, 16.3)]  # vo.mp3 line ranges (silence gaps 6.79-7.22, 10.40-10.57)
CAPS = ["SPOT THE DIFFERENCE! Petrol pump: A on top, B below. 3 things are different. Timer's on, find them.",
        "STOP! How many did you find? Comment 1, 2 or 3.",
        "Here are all 3! Got them all? Your eyes are on full tank. Look again."]


def sign(c, hrs):
    S.rrect(c, 1560, 260, 280, 150, 18); c.set_source_rgb(0.1, 0.35, 0.6); c.fill()
    T(c, "OPEN", 1700, 320, 46, (1, 1, 1), stroke=None)
    T(c, f"{hrs} HRS", 1700, 385, 54, (1, 0.85, 0.2), stroke=None)
    c.rectangle(1690, 410, 20, 300); c.set_source_rgb(0.4, 0.4, 0.45); c.fill()


def dispenser(c, x, noz):
    S.rrect(c, x - 90, 420, 180, 290, 18); c.set_source_rgb(0.92, 0.92, 0.94); c.fill()
    S.rrect(c, x - 65, 450, 130, 80, 10); c.set_source_rgb(0.1, 0.12, 0.15); c.fill()
    T(c, "88.8", x, 505, 40, (0.3, 1, 0.5), stroke=None)
    S.rrect(c, x - 90, 600, 180, 30, 6); c.set_source_rgb(0.85, 0.2, 0.15); c.fill()
    S.rrect(c, x + 70, 540, 50, 34, 8); c.set_source_rgb(*noz); c.fill()       # nozzle holder
    c.move_to(x + 95, 574); c.curve_to(x + 140, 640, x + 120, 700, x + 60, 705)
    c.set_source_rgb(0.15, 0.15, 0.18); c.set_line_width(8); c.stroke()


def cone(c, x, y):
    c.move_to(x - 30, y); c.line_to(x, y - 90); c.line_to(x + 30, y); c.close_path(); c.set_source_rgb(1, 0.5, 0.1); c.fill()
    c.rectangle(x - 17, y - 50, 34, 12); c.set_source_rgb(1, 1, 1); c.fill()
    c.rectangle(x - 42, y - 6, 84, 12); c.set_source_rgb(0.9, 0.42, 0.08); c.fill()


def scooter(c, x, y):
    for wx in (x - 110, x + 110):
        c.arc(wx, y, 42, 0, 2 * math.pi); c.set_source_rgb(0.12, 0.12, 0.14); c.fill()
        c.arc(wx, y, 16, 0, 2 * math.pi); c.set_source_rgb(0.7, 0.7, 0.72); c.fill()
    S.rrect(c, x - 150, y - 110, 230, 80, 36); c.set_source_rgb(0.2, 0.6, 0.85); c.fill()
    S.rrect(c, x - 120, y - 135, 150, 32, 14); c.set_source_rgb(0.15, 0.15, 0.18); c.fill()
    c.move_to(x + 70, y - 60); c.line_to(x + 120, y - 190); c.set_source_rgb(0.2, 0.6, 0.85); c.set_line_width(26); c.stroke()
    c.move_to(x + 90, y - 195); c.line_to(x + 160, y - 195); c.set_source_rgb(0.15, 0.15, 0.18); c.set_line_width(12); c.stroke()


def scene(c, t):
    g = __import__('cairo').LinearGradient(0, 0, 0, 700)
    g.add_color_stop_rgb(0, 0.55, 0.78, 0.95); g.add_color_stop_rgb(1, 0.85, 0.92, 0.98)
    c.rectangle(0, 0, 1920, 720); c.set_source(g); c.fill()
    c.rectangle(0, 710, 1920, 370); c.set_source_rgb(0.45, 0.45, 0.48); c.fill()          # forecourt
    for j in range(0, 1920, 240):
        c.rectangle(j, 900, 140, 14); c.set_source_rgb(0.95, 0.9, 0.5); c.fill()
    # tree on the left
    c.rectangle(110, 420, 36, 300); c.set_source_rgb(0.45, 0.3, 0.18); c.fill()
    for (dx, dy, r) in ((0, 380, 110), (-70, 430, 80), (70, 430, 80)):
        c.arc(128 + dx, dy, r, 0, 2 * math.pi); c.set_source_rgb(0.25, 0.55, 0.3); c.fill()
    # canopy
    c.rectangle(330, 150, 1160, 120); c.set_source_rgb(0.97, 0.97, 0.97); c.fill()
    c.rectangle(330, 205, 1160, 30); c.set_source_rgb(0.1, 0.55, 0.3); c.fill()
    T(c, "FUEL STATION", 910, 195, 46, (0.1, 0.35, 0.2), stroke=None)
    for px in (440, 1380):
        c.rectangle(px - 20, 270, 40, 440); c.set_source_rgb(0.85, 0.85, 0.88); c.fill()
    c.rectangle(330, 270, 1160, 10); c.set_source_rgba(0, 0, 0, 0.15); c.fill()
    dispenser(c, 700, (0.15, 0.6, 0.25))
    dispenser(c, 1120, (0.15, 0.6, 0.25))
    S.rrect(c, 600, 700, 620, 30, 8); c.set_source_rgb(0.75, 0.75, 0.7); c.fill()        # island
    sign(c, 24)
    cone(c, 1560, 860)
    scooter(c, 360, 900)
    K.sid(c, 1.0, 900, 420, 0.4, mouth='smile', arms=((14, -10), (100, 40)))


def sign_b(c, t):
    S.rrect(c, 1560, 340, 280, 70, 0); c.set_source_rgb(0.1, 0.35, 0.6); c.fill()
    T(c, "12 HRS", 1700, 385, 54, (1, 0.85, 0.2), stroke=None)


def noz_b(c, t):
    S.rrect(c, 1190, 540, 50, 34, 8); c.set_source_rgb(0.85, 0.12, 0.12); c.fill()


def cone_b(c, t):
    cone(c, 1760, 860)


DIFFS = [(1700, 365, 120, sign_b), (1215, 557, 70, noz_b), (1760, 815, 90, cone_b)]
g = SD.SpotDiff(D, SEGS, CAPS, ("SPOT 3 DIFFERENCES", "AT THE PETROL PUMP"), "SAME BRO GAMES #25", scene, DIFFS, hunt=17.5,
                mood='chill', label="PETROL PUMP")

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.2, 3.0, 12.0, g.t_freeze + 1, g.t_count + 1.5, g.t_reveal + 0.6, g.t_reveal + 2.6, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1))
    else:
        g.render(f"{D}/short.mp4")
