"""Trading-desk world + chart overlays for Same Bro trader/SIP-mistake shorts (s24+)."""
import math
import random
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402
import props as P  # noqa: E402


def monitor(c, x, y, w, h, t, seed=1, crash=None, trend=0.0, label="NIFTY"):
    V.box(c, x - 12, y - 12, w + 24, h + 24, (0.05, 0.05, 0.07), 10)
    V.box(c, x, y, w, h, (0.04, 0.06, 0.1), 4)
    T(c, label, x + 20, y + 34, 24, GREY, stroke=None, anchor="left")
    P.candles(c, x + 14, y + 50, w - 28, h - 70, seed=seed, n=14, crash=crash, trend=trend)
    V.box(c, x + w / 2 - 14, y + h + 12, 28, 50, (0.08, 0.08, 0.1))


def desk(c, t, crash=None, mode="night", ticker="NIFTY 50"):
    """Dark trader bedroom: wall of screens behind Sid, LED ticker, desk at right."""
    night = mode == "night"
    wall = (0.08, 0.09, 0.14) if night else (0.55, 0.52, 0.48)
    c.set_source(V.lingrad(c, 0, 0, 0, 780, [(0, (wall[0] * 0.7, wall[1] * 0.7, wall[2] * 0.7)), (1, wall)]))
    c.rectangle(0, 0, 1920, 780); c.fill()
    c.set_source(V.lingrad(c, 0, 780, 0, 1080, [(0, (0.16, 0.14, 0.16)), (1, (0.07, 0.06, 0.07))]))
    c.rectangle(0, 780, 1920, 300); c.fill()
    # LED strip glow
    V.box(c, 0, 40, 1920, 10, (0.5, 0.2, 0.9))
    V.light(c, 960, 45, 900, (0.5, 0.2, 0.9), 0.12)
    # screens
    monitor(c, 560, 150, 360, 240, t, 4, crash, label=ticker)
    monitor(c, 1080, 150, 360, 240, t, 9, crash, label="BANKNIFTY")
    monitor(c, 1480, 220, 300, 200, t, 2, None, 0.6, label="GOLD")
    # ticker tape
    V.box(c, 520, 440, 960, 54, (0.02, 0.02, 0.03), 8)
    c.save(); c.rectangle(520, 440, 960, 54); c.clip()
    tape = "  NIFTY -1.2%   BANKNIFTY -0.8%   SENSEX -1.1%   GOLD +0.4%   SILVER -2.7%   USD/INR 0.1%  "
    off = (t * 120) % 1500
    for j in range(2):
        T(c, tape, 520 - off + j * 1500, 478, 30, (0.55, 0.2, 0.22), stroke=None, anchor="left")
    c.restore()
    # desk + keyboard + mug
    V.box(c, 1240, 700, 680, 30, (0.25, 0.18, 0.13))
    V.box(c, 1270, 730, 28, 220, (0.18, 0.13, 0.1)); V.box(c, 1860, 730, 28, 220, (0.18, 0.13, 0.1))
    V.box(c, 1330, 680, 260, 22, (0.15, 0.15, 0.18), 6)
    V.box(c, 1660, 640, 46, 60, (0.9, 0.9, 0.88), 8)
    # screen glow on Sid
    V.light(c, 1000, 300, 700, (0.3, 0.6, 1.0), 0.10)
    if night:
        V.shade(c, 0.12, (0.02, 0.02, 0.08))


def line(c, t, t0, x, y, w, h, pts, col=GRN, dur=1.6, lw=10, a=1.0):
    """Progressive line chart over [x,x+w]; pts in 0..1 (1 = top)."""
    if t < t0:
        return None
    g = U.clamp((t - t0) / dur)
    n = len(pts) - 1
    m = g * n
    c.set_source_rgba(1, 1, 1, 0.08 * a)
    c.rectangle(x, y, w, h); c.fill()
    c.move_to(x, y + h * (1 - pts[0]))
    last = (x, y + h * (1 - pts[0]))
    for i in range(1, n + 1):
        if i <= m:
            last = (x + w * i / n, y + h * (1 - pts[i]))
        else:
            f = m - (i - 1)
            if f <= 0:
                break
            p = pts[i - 1] + (pts[i] - pts[i - 1]) * f
            last = (x + w * (i - 1 + f) / n, y + h * (1 - p))
        c.line_to(*last)
        if i > m:
            break
    c.set_source_rgba(*col, a); c.set_line_width(lw); c.set_line_join(1); c.stroke()
    c.arc(last[0], last[1], lw * 1.2, 0, 2 * math.pi); c.set_source_rgba(*col, a); c.fill()
    return last


def marker(c, t, t0, x, y, txt, col=YEL, size=40, up=True):
    if t < t0:
        return
    a = k(t, t0, t0 + 0.2)
    c.arc(x, y, 16, 0, 2 * math.pi); c.set_source_rgba(*col, a); c.fill()
    T(c, txt, x, y + (-36 if up else 66), size, col, a, lw=6)


def moral(c, t, st, txt1, txt2, col=YEL):
    """Full dim MORAL card."""
    U.dim(c, 0.9)
    a = k(t, st + 0.2, st + 0.5)
    T(c, "MORAL", 540, 520, 64, GREY, a, lw=8)
    S.rrect(c, 140, 560, 800, 8, 4); c.set_source_rgba(*col, a); c.fill()
    for i, s_ in enumerate((txt1, txt2)):
        b = k(t, st + 0.6 + i * 0.5, st + 0.9 + i * 0.5)
        sc = 1 + 0.2 * (1 - U.eob(b))
        c.save(); c.translate(540, 720 + i * 140); c.scale(sc, sc)
        T(c, s_, 0, 0, 84 if len(s_) < 17 else 66, WHITE if i == 0 else col, b, lw=10)
        c.restore()


def sid(c, t, x=1000, y=330, s=0.5, **kw):
    K.sid(c, t, x, y, s, **kw)
