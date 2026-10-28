"""Shared overlay helpers for Same Bro shorts (s15+)."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402,F401
import body as B  # noqa: E402
import env as V  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

GREY = (0.55, 0.57, 0.65)
BLUE = (0.35, 0.65, 1.0)
PINK = (1.0, 0.4, 0.6)


def panel(c, y=880, h=480, x=90, w=900, a=0.92):
    S.rrect(c, x, y, w, h, 30); c.set_source_rgba(0.05, 0.06, 0.1, a); c.fill()


def rows(c, t, st, items, y0=960, gap=100, x=540):
    """items: (text, col, size, dt) or (text, col, size, dt, anchor, xx)."""
    for i, it in enumerate(items):
        txt, col, size, dt = it[:4]
        anchor = it[4] if len(it) > 4 else "center"
        xx = it[5] if len(it) > 5 else x
        a = k(t, st + dt, st + dt + 0.25)
        if a > 0:
            T(c, txt, xx, y0 + i * gap, size, col, a, stroke=None, anchor=anchor)


def full(c, t, st, items, y0=430, gap=150, dim=0.86):
    U.dim(c, dim)
    for i, it in enumerate(items):
        txt, col, size, dt = it[:4]
        a = k(t, st + dt, st + dt + 0.25)
        if a > 0:
            sc = 1 + 0.25 * (1 - U.eob(a))
            c.save(); c.translate(540, y0 + i * gap); c.scale(sc, sc)
            T(c, txt, 0, 0, size, col, a, lw=max(8, size // 8))
            c.restore()


def stamp(c, t, t0, txt, x=540, y=1300, col=RED, size=50, rot=-0.06):
    if t < t0:
        return
    a = k(t, t0, t0 + 0.15)
    sc = 1 + 0.5 * (1 - U.eob(a))
    c.save(); c.translate(x, y); c.rotate(rot); c.scale(sc, sc)
    w = len(txt) * size * 0.62 + 60
    S.rrect(c, -w / 2, -size * 0.95, w, size * 1.7, 18); c.set_source_rgba(*col, a); c.fill()
    T(c, txt, 0, size * 0.3, size, WHITE, a, stroke=None)
    c.restore()


def hbar(c, t, t0, x, y, w, h, frac, col, label, val, dur=0.6):
    g = U.eob(k(t, t0, t0 + dur))
    if t < t0:
        return
    a = k(t, t0, t0 + 0.2)
    S.rrect(c, x, y, w, h, h / 2); c.set_source_rgba(1, 1, 1, 0.08 * a); c.fill()
    S.rrect(c, x, y, max(h, w * frac * g), h, h / 2); c.set_source_rgba(*col, a); c.fill()
    T(c, label, x, y - 22, 40, WHITE, a, stroke=None, anchor="left")
    T(c, val, x + w, y - 22, 44, col, a, stroke=None, anchor="right")


def bill_screen(title, items, total, show=99, hi=None, total_col=(0.1, 0.1, 0.12), btn="PLACE ORDER"):
    """Checkout/bill phone screen. items: (label, amount_str). show = how many lines visible."""
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
        c.rectangle(0, 0, w, 120); c.set_source_rgb(0.15, 0.35, 0.9); c.fill()
        T(c, title, w / 2, 85, 44, WHITE, stroke=None)
        y = 180
        for i, (lab, amt) in enumerate(items[:show]):
            if hi is not None and i in hi:
                S.rrect(c, 20, y - 46, w - 40, 64, 12); c.set_source_rgb(1, 0.88, 0.88); c.fill()
                col = RED
            else:
                col = (0.15, 0.15, 0.18)
            T(c, lab, 40, y, 32, col, stroke=None, anchor="left", bold=False)
            T(c, amt, w - 40, y, 34, col, stroke=None, anchor="right")
            y += 62
        c.move_to(30, y - 30); c.line_to(w - 30, y - 30); c.set_source_rgb(0.8, 0.8, 0.84); c.set_line_width(3); c.stroke()
        T(c, "TOTAL", 40, y + 30, 40, (0.1, 0.1, 0.12), stroke=None, anchor="left")
        T(c, total, w - 40, y + 30, 48, total_col, stroke=None, anchor="right")
        S.rrect(c, 40, h - 110, w - 80, 80, 40); c.set_source_rgb(1, 0.6, 0.1); c.fill()
        T(c, btn, w / 2, h - 57, 36, WHITE, stroke=None)
    return f


def sms_screen(sender, lines, t0=0.0):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.07, 0.08, 0.1); c.fill()
        T(c, "Messages", w / 2, 90, 36, WHITE, stroke=None)
        S.rrect(c, 30, 170, w - 60, 100 + 75 * len(lines), 24); c.set_source_rgb(0.18, 0.2, 0.25); c.fill()
        T(c, sender, 60, 225, 30, GREY, stroke=None, anchor="left")
        for i, (ln, col) in enumerate(lines):
            T(c, ln, 60, 305 + i * 75, 46 if i == 0 else 34, col, stroke=None, anchor="left")
    return f


def packet(c, x, y, s, label, grams, col=(0.95, 0.75, 0.2), a=1.0):
    """Generic biscuit/noodle packet, centre (x,y)."""
    c.save(); c.translate(x, y); c.scale(s, s)
    c.push_group()
    S.rrect(c, -150, -210, 300, 420, 30); c.set_source_rgb(*col); c.fill()
    S.rrect(c, -150, -210, 300, 70, 30); c.set_source_rgb(col[0] * 0.8, col[1] * 0.8, col[2] * 0.8); c.fill()
    for zx in range(-150, 151, 20):
        c.move_to(zx, -210); c.line_to(zx + 10, -222); c.line_to(zx + 20, -210)
    c.set_source_rgb(col[0] * 0.8, col[1] * 0.8, col[2] * 0.8); c.fill()
    T(c, label, 0, -40, 48, (0.6, 0.1, 0.1), stroke=None)
    S.rrect(c, -90, 40, 180, 90, 20); c.set_source_rgb(1, 1, 1); c.fill()
    T(c, grams, 0, 102, 50, (0.1, 0.1, 0.12), stroke=None)
    T(c, "₹10", 0, 180, 40, (0.1, 0.1, 0.12), stroke=None)
    c.pop_group_to_source(); c.paint_with_alpha(a)
    c.restore()


def end_card(c, a1, a2, col2=YEL):
    panel(c, 900, 230, 140, 800, 0.9)
    T(c, a1, 540, 1000, 60, WHITE, stroke=None)
    T(c, a2, 540, 1085, 56 if len(a2) < 24 else 46, col2, stroke=None)


def sid(c, t, x=1000, y=330, s=0.5, **kw):
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    B.figure(c, x, y, s, t, **d)
