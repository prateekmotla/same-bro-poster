"""Same Bro Games #15: memory flash, 6 phone apps, which app vanished? (engine: studio/shorts/memgame.py, items=,
3x2 grid). Generic, unbranded app icons. Answer: CAMERA."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import memgame as MG  # noqa: E402
from memgame import S, T  # noqa: E402

D = "/home/claude/sid/shorts/c109_memapps"
SEGS = [(0.0, 6.29), (6.77, 9.05), (9.48, 14.4)]  # vo.mp3 line ranges (gaps 6.29-6.77, 9.05-9.48)
CAPS = ["MEMORY TEST! 6 apps on a phone, just a few seconds. Watch closely, then one will VANISH.",
        "STOP! Which app vanished? Comment.",
        "The answer is CAMERA! Got it? Then your memory is sharp. Try again."]


def app(bg, glyph, label):
    def f(c):
        S.rrect(c, -82, -95, 164, 164, 40); c.set_source_rgb(*bg); c.fill()
        c.save(); c.translate(0, -13); glyph(c); c.restore()
        T(c, label, 0, 112, 30, (0.15, 0.15, 0.2), stroke=None)
    return f


W = (1, 1, 1)


def g_camera(c):
    S.rrect(c, -50, -30, 100, 66, 14); c.set_source_rgb(*W); c.fill()
    c.rectangle(-18, -42, 36, 14); c.fill()
    c.arc(0, 3, 22, 0, 2 * math.pi); c.set_source_rgb(0.2, 0.2, 0.25); c.fill()
    c.arc(0, 3, 11, 0, 2 * math.pi); c.set_source_rgb(0.5, 0.75, 1.0); c.fill()


def g_music(c):
    c.set_source_rgb(*W)
    c.arc(-22, 30, 15, 0, 2 * math.pi); c.fill(); c.arc(28, 20, 15, 0, 2 * math.pi); c.fill()
    c.rectangle(-9, -40, 9, 70); c.fill(); c.rectangle(41, -50, 9, 70); c.fill()
    c.move_to(-9, -40); c.line_to(50, -50); c.line_to(50, -34); c.line_to(-9, -24); c.close_path(); c.fill()


def g_maps(c):
    c.move_to(0, 48); c.curve_to(-40, 0, -40, -45, 0, -45); c.curve_to(40, -45, 40, 0, 0, 48)
    c.set_source_rgb(*W); c.fill()
    c.arc(0, -10, 14, 0, 2 * math.pi); c.set_source_rgb(0.9, 0.3, 0.25); c.fill()


def g_chat(c):
    S.rrect(c, -50, -40, 100, 70, 26); c.set_source_rgb(*W); c.fill()
    c.move_to(-28, 25); c.line_to(-38, 48); c.line_to(-6, 28); c.fill()
    for dx in (-24, 0, 24):
        c.arc(dx, -5, 7, 0, 2 * math.pi); c.set_source_rgb(0.2, 0.65, 0.4); c.fill()


def g_mail(c):
    c.rectangle(-52, -32, 104, 68); c.set_source_rgb(*W); c.fill()
    c.move_to(-52, -32); c.line_to(0, 8); c.line_to(52, -32); c.set_source_rgb(0.85, 0.35, 0.3); c.set_line_width(7); c.stroke()


def g_weather(c):
    c.arc(-12, -10, 26, 0, 2 * math.pi); c.set_source_rgb(1, 0.85, 0.2); c.fill()
    c.set_source_rgb(*W)
    c.arc(5, 22, 22, 0, 2 * math.pi); c.fill(); c.arc(32, 18, 18, 0, 2 * math.pi); c.fill()
    c.arc(-20, 26, 16, 0, 2 * math.pi); c.fill(); c.rectangle(-20, 26, 52, 16); c.fill()


ITEMS = dict(CAMERA=app((0.25, 0.27, 0.33), g_camera, "CAMERA"), MUSIC=app((0.9, 0.3, 0.45), g_music, "MUSIC"),
             MAPS=app((0.25, 0.6, 0.35), g_maps, "MAPS"), CHAT=app((0.15, 0.5, 0.35), g_chat, "CHAT"),
             MAIL=app((0.3, 0.45, 0.85), g_mail, "MAIL"), WEATHER=app((0.35, 0.65, 0.95), g_weather, "WEATHER"))

g = MG.MemGame(D, SEGS, CAPS, ("MEMORIZE 6 APPS", "ONE WILL VANISH"), "SAME BRO GAMES #15", missing='CAMERA',
               mem=8.0, hunt=5.0, seed=109, mood='chill', items=ITEMS,
               gone_title=("ONE APP IS GONE!", "They got SHUFFLED too"), ask="WHICH APP VANISHED? COMMENT")

if __name__ == "__main__":
    if sys.argv[1] == "preview":
        ts = [0.3, 3.0, g.t_mem + 0.2, g.t_mem + 0.6, g.t_back + 1, g.t_freeze + 1, g.t_count + 1.5,
              g.t_reveal + 1.0, g.t_reveal + 3.0, g.dur - 1]
        g.preview(ts, f"{D}/prev.png")
        print("dur", round(g.dur, 1), "freeze", round(g.t_freeze, 1), "reveal", round(g.t_reveal, 1), g.qslot, g.pos1[g.missing])
    else:
        g.render(f"{D}/short.mp4")
