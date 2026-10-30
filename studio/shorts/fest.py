"""Diwali decor for Same Bro festive shorts: diyas, string lights, festive room, coin, envelope."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

GOLD = (1.0, 0.78, 0.25)


def diya(c, x, y, t, s=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.move_to(-40, 0); c.curve_to(-30, 30, 30, 30, 40, 0); c.close_path()
    c.set_source_rgb(0.75, 0.35, 0.15); c.fill()
    fl = 1 + 0.12 * math.sin(t * 13 + x)
    c.save(); c.scale(1, fl)
    c.move_to(0, -48); c.curve_to(14, -20, 10, -4, 0, -2); c.curve_to(-10, -4, -14, -20, 0, -48)
    c.set_source_rgb(1, 0.75, 0.2); c.fill(); c.restore()
    V.light(c, 0, -20, 90, (1, 0.7, 0.3), 0.35)
    c.restore()


def lights(c, t, y0=40, x0=20, n=40):
    for i in range(n):
        x = x0 + i * 48
        y = y0 + 18 * math.sin(i * 0.7)
        on = 0.6 + 0.4 * math.sin(t * 4 + i * 1.3)
        col = [(1, 0.8, 0.3), (1, 0.4, 0.3), (0.5, 0.9, 1)][i % 3]
        c.arc(x, y, 8, 0, 2 * math.pi); c.set_source_rgba(*col, on); c.fill()
        V.light(c, x, y, 30, col, 0.25 * on)


def room(c, t, lt=0, **kw):
    """Sid's night room dressed for Diwali; Sid standing at head (1000,330)."""
    V.room(c, t, 'night', fan=False)
    lights(c, t, 60)
    lights(c, t, 300, 560, 18)
    for i in range(3):
        diya(c, 760 + i * 110, 770, t, 0.9)
    for i in range(2):
        diya(c, 1200 + i * 110, 770, t, 0.9)
    V.light(c, 960, 700, 600, (1, 0.6, 0.2), 0.10)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def coin(c, x, y, r, txt="₹1", a=1.0):
    c.arc(x, y, r, 0, 2 * math.pi); c.set_source_rgba(0.85, 0.65, 0.2, a); c.fill()
    c.arc(x, y, r * 0.82, 0, 2 * math.pi); c.set_source_rgba(1.0, 0.82, 0.35, a); c.fill()
    T(c, txt, x, y + r * 0.28, r * 0.8, (0.45, 0.3, 0.05), a, stroke=None)


def envelope(c, x, y, w, h, txt, a=1.0):
    S.rrect(c, x - w / 2, y - h / 2, w, h, 16); c.set_source_rgba(0.85, 0.15, 0.2, a); c.fill()
    c.move_to(x - w / 2, y - h / 2); c.line_to(x, y); c.line_to(x + w / 2, y - h / 2)
    c.set_source_rgba(*GOLD, a); c.set_line_width(6); c.stroke()
    T(c, txt, x, y + h * 0.32, h * 0.32, GOLD, a, stroke=None)
