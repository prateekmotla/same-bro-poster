"""Scene props for Same Bro v3: phone UIs, live stream, candles, money flow, stats, etc."""
import math
import random

import cairo

import sys
sys.path.insert(0, "/home/claude/sid/v2")
import sid2 as S  # noqa: E402

FONT = "Poppins"
YEL = (1.0, 0.80, 0.16)
RED = (0.94, 0.25, 0.27)
GRN = (0.22, 0.85, 0.48)
INK = (0.05, 0.05, 0.07)
W, H = 1080, 1920


def ease(t):
    return S.ease(t)


def eob(t, s=1.7):
    return S.ease_out_back(t, s)


def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def text(c, txt, x, y, size, fill=(1, 1, 1), stroke=(0, 0, 0), lw=12, alpha=1.0, weight=cairo.FONT_WEIGHT_BOLD,
         font=FONT, anchor="center", slant=cairo.FONT_SLANT_NORMAL):
    c.select_font_face(font, slant, weight)
    c.set_font_size(size)
    e = c.text_extents(txt)
    dx = {"center": e.width / 2 + e.x_bearing, "left": 0, "right": e.x_advance}[anchor]
    c.move_to(x - dx, y)
    c.text_path(txt)
    if stroke:
        c.set_source_rgba(*stroke, alpha)
        c.set_line_width(lw)
        c.set_line_join(cairo.LINE_JOIN_ROUND)
        c.stroke_preserve()
    c.set_source_rgba(*fill, alpha)
    c.fill()
    c.new_path()
    return e.x_advance


def grad(c, stops, x0, y0, x1, y1):
    g = cairo.LinearGradient(x0, y0, x1, y1)
    for o, col in stops:
        g.add_color_stop_rgba(o, *col, 1) if len(col) == 3 else g.add_color_stop_rgba(o, *col)
    c.set_source(g)


def glow(c, x, y, r, col, a):
    g = cairo.RadialGradient(x, y, 0, x, y, r)
    g.add_color_stop_rgba(0, *col, a)
    g.add_color_stop_rgba(1, *col, 0)
    c.arc(x, y, r, 0, 2 * math.pi)
    c.set_source(g)
    c.fill()


# ---------------- backgrounds ----------------
def bg_trading_room(c, t, tone=1.0):
    grad(c, [(0, (0.05 * tone, 0.07 * tone, 0.13 * tone)), (1, (0.02, 0.02, 0.04))], 0, 0, 0, H)
    c.paint()
    # monitor wall
    for i, (x, y, w, h) in enumerate(((60, 300, 440, 280), (580, 300, 440, 280), (320, 620, 440, 260))):
        S.rrect(c, x, y, w, h, 16)
        c.set_source_rgb(0.04, 0.05, 0.08)
        c.fill()
        c.save()
        S.rrect(c, x + 10, y + 10, w - 20, h - 20, 10)
        c.clip()
        c.set_source_rgb(0.03, 0.08, 0.1)
        c.paint()
        candles(c, x + 20, y + 30, w - 40, h - 60, seed=i + 3, t=t * 0.3, n=16, alpha=0.8)
        c.restore()
    glow(c, 540, 600, 700, (0.2, 0.6, 1.0), 0.12)
    # desk
    grad(c, [(0, (0.12, 0.1, 0.1)), (1, (0.05, 0.04, 0.04))], 0, 1300, 0, H)
    c.rectangle(0, 1300, W, H - 1300)
    c.fill()


def bg_night_room(c, t):
    grad(c, [(0, (0.07, 0.09, 0.17)), (1, (0.03, 0.035, 0.07))], 0, 0, 0, H)
    c.paint()
    S.rrect(c, 640, 180, 360, 470, 14)
    grad(c, [(0, (0.12, 0.16, 0.32)), (1, (0.18, 0.22, 0.4))], 0, 180, 0, 650)
    c.fill()
    c.arc(880, 300, 44, 0, 2 * math.pi)
    c.set_source_rgb(0.95, 0.95, 0.85)
    c.fill()
    c.set_source_rgb(0.04, 0.04, 0.07)
    c.set_line_width(14)
    S.rrect(c, 640, 180, 360, 470, 14)
    c.stroke()
    c.move_to(820, 180); c.line_to(820, 650); c.stroke()
    c.move_to(640, 650); c.line_to(1000, 650); c.line_to(700, 1900); c.line_to(80, 1900); c.close_path()
    c.set_source_rgba(0.5, 0.6, 1.0, 0.06)
    c.fill()


def bg_studio(c, t):
    """Streamer's studio: RGB lights, ring light."""
    grad(c, [(0, (0.12, 0.05, 0.18)), (1, (0.03, 0.02, 0.06))], 0, 0, 0, H)
    c.paint()
    for i in range(6):
        x = 80 + i * 180
        col = [(0.9, 0.2, 0.6), (0.3, 0.4, 1.0), (0.2, 0.9, 0.8)][i % 3]
        c.rectangle(x, 120, 22, 900)
        c.set_source_rgba(*col, 0.5 + 0.3 * math.sin(t * 2 + i))
        c.fill()
        glow(c, x + 11, 560, 260, col, 0.12)
    c.set_line_width(26)
    c.arc(540, 640, 300, 0, 2 * math.pi)
    c.set_source_rgba(1, 1, 1, 0.85)
    c.stroke()
    glow(c, 540, 640, 520, (1, 1, 1), 0.10)


def bg_void(c, col=(0.02, 0.02, 0.04)):
    c.set_source_rgb(*col)
    c.paint()


def bg_grid(c, t, col=(0.04, 0.05, 0.09)):
    c.set_source_rgb(*col)
    c.paint()
    c.set_line_width(2)
    c.set_source_rgba(1, 1, 1, 0.05)
    off = (t * 40) % 80
    for x in range(-80, W + 80, 80):
        c.move_to(x + off, 0); c.line_to(x + off, H)
    for y in range(-80, H + 80, 80):
        c.move_to(0, y + off); c.line_to(W, y + off)
    c.stroke()


# ---------------- charts ----------------
def candles(c, x, y, w, h, seed=1, t=0.0, n=20, trend=0.0, crash=None, alpha=1.0, grow=1.0):
    rnd = random.Random(seed)
    vals = [0.5]
    for i in range(n + 5):
        d = rnd.uniform(-0.08, 0.08) + trend * 0.03
        if crash is not None and i >= crash:
            d = -abs(d) - 0.06
        vals.append(clamp(vals[-1] + d, 0.05, 0.95))
    cw = w / n
    shown = int(n * clamp(grow)) if grow < 1 else n
    for i in range(shown):
        o, cl = vals[i], vals[i + 1]
        hi, lo = max(o, cl) + rnd.uniform(0, 0.04), min(o, cl) - rnd.uniform(0, 0.04)
        col = GRN if cl >= o else RED
        cx = x + i * cw + cw / 2
        c.set_source_rgba(*col, alpha)
        c.set_line_width(max(2, cw * 0.08))
        c.move_to(cx, y + h * (1 - hi)); c.line_to(cx, y + h * (1 - lo)); c.stroke()
        top, bot = y + h * (1 - max(o, cl)), y + h * (1 - min(o, cl))
        c.rectangle(cx - cw * 0.32, top, cw * 0.64, max(3, bot - top))
        c.fill()
    return vals


def equity_curve(c, x, y, w, h, pts, k, col=GRN, lw=10):
    n = max(2, int(len(pts) * clamp(k)))
    c.set_line_width(lw)
    c.set_line_cap(cairo.LINE_CAP_ROUND)
    c.set_line_join(cairo.LINE_JOIN_ROUND)
    for i in range(n):
        px, py = x + w * i / (len(pts) - 1), y + h * (1 - pts[i])
        (c.move_to if i == 0 else c.line_to)(px, py)
    c.set_source_rgb(*col)
    c.stroke()
    px, py = x + w * (n - 1) / (len(pts) - 1), y + h * (1 - pts[n - 1])
    glow(c, px, py, 60, col, 0.5)
    c.arc(px, py, 12, 0, 2 * math.pi)
    c.set_source_rgb(1, 1, 1)
    c.fill()
    return px, py


# ---------------- phone / app ----------------
def phone(c, x, y, w, h, draw_screen, t, tilt=0.0, glow_a=0.35):
    c.save()
    c.translate(x + w / 2, y + h / 2)
    c.rotate(math.radians(tilt))
    c.translate(-w / 2, -h / 2)
    glow(c, w / 2, h / 2, max(w, h) * 0.9, (0.45, 0.65, 1.0), glow_a)
    S.rrect(c, 0, 0, w, h, w * 0.12)
    grad(c, [(0, (0.18, 0.18, 0.21)), (1, (0.06, 0.06, 0.08))], 0, 0, w, h)
    c.fill()
    m = w * 0.04
    S.rrect(c, m, m * 1.2, w - 2 * m, h - 2.4 * m, w * 0.09)
    c.save()
    c.clip()
    c.translate(m, m * 1.2)
    draw_screen(c, w - 2 * m, h - 2.4 * m, t)
    c.restore()
    S.rrect(c, w * 0.38, m * 1.8, w * 0.24, w * 0.05, w * 0.025)
    c.set_source_rgb(0.02, 0.02, 0.03)
    c.fill()
    c.restore()


def screen_trade_app(pnl, k_chart=1.0, crash=None, seed=7, label="NIFTY 24500 CE"):
    def draw(c, w, h, t):
        c.set_source_rgb(0.06, 0.07, 0.1)
        c.paint()
        text(c, label, w / 2, h * 0.09, w * 0.06, fill=(0.85, 0.88, 0.95), stroke=None)
        candles(c, w * 0.05, h * 0.14, w * 0.9, h * 0.42, seed=seed, n=18, crash=crash, grow=k_chart, t=t)
        col = GRN if pnl >= 0 else RED
        S.rrect(c, w * 0.08, h * 0.62, w * 0.84, h * 0.16, w * 0.05)
        c.set_source_rgba(*col, 0.16)
        c.fill()
        text(c, "P&L", w / 2, h * 0.67, w * 0.05, fill=(0.7, 0.72, 0.8), stroke=None)
        sign = "+" if pnl >= 0 else "−"
        text(c, f"{sign}₹{abs(int(pnl)):,}", w / 2, h * 0.75, w * 0.12, fill=col, stroke=None)
        for i, (lab, col2) in enumerate((("BUY", GRN), ("SELL", RED))):
            S.rrect(c, w * (0.08 + i * 0.44), h * 0.84, w * 0.4, h * 0.09, w * 0.04)
            c.set_source_rgb(*col2)
            c.fill()
            text(c, lab, w * (0.28 + i * 0.44), h * 0.9, w * 0.06, fill=(1, 1, 1), stroke=None)
    return draw


def screen_live(t0, comments, viewers="12.4K"):
    def draw(c, w, h, t):
        bg_studio_mini(c, w, h, t)
        S.rrect(c, w * 0.05, h * 0.03, w * 0.2, h * 0.04, h * 0.01)
        c.set_source_rgb(*RED)
        c.fill()
        text(c, "LIVE", w * 0.15, h * 0.06, w * 0.05, fill=(1, 1, 1), stroke=None)
        text(c, viewers + " watching", w * 0.42, h * 0.06, w * 0.045, fill=(1, 1, 1), stroke=None)
        # streamer silhouette
        c.arc(w / 2, h * 0.3, w * 0.13, 0, 2 * math.pi)
        c.set_source_rgb(0.15, 0.12, 0.18)
        c.fill()
        S.rrect(c, w * 0.27, h * 0.38, w * 0.46, h * 0.3, w * 0.12)
        c.fill()
        # chat
        k = int((t - t0) * 2.5)
        for i in range(min(6, k)):
            msg = comments[(k - 1 - i) % len(comments)]
            yy = h * (0.92 - i * 0.065)
            S.rrect(c, w * 0.04, yy - h * 0.045, w * 0.84, h * 0.055, h * 0.02)
            c.set_source_rgba(0, 0, 0, 0.45 * (1 - i / 7))
            c.fill()
            text(c, msg, w * 0.07, yy - h * 0.008, w * 0.042, fill=(1, 1, 1), stroke=None, anchor="left",
                 alpha=1 - i / 7)
    return draw


def bg_studio_mini(c, w, h, t):
    grad(c, [(0, (0.28, 0.1, 0.38)), (1, (0.06, 0.03, 0.12))], 0, 0, 0, h)
    c.paint()
    c.set_line_width(w * 0.03)
    c.arc(w / 2, h * 0.32, w * 0.3, 0, 2 * math.pi)
    c.set_source_rgba(1, 1, 1, 0.6)
    c.stroke()


def screen_description(k):
    lines = ["BANKNIFTY LIVE TRADING", "", ">> Open demat with MY link", "   bit.ly/••••••",
             "Use code: LIVE100", "", "Telegram for calls: t.me/••••"]
    def draw(c, w, h, t):
        c.set_source_rgb(0.97, 0.97, 0.98)
        c.paint()
        S.rrect(c, 0, 0, w, h * 0.28, 0)
        grad(c, [(0, (0.3, 0.1, 0.4)), (1, (0.1, 0.05, 0.2))], 0, 0, 0, h * 0.28)
        c.fill()
        c.move_to(w/2-w*0.04,h*0.16-w*0.05); c.line_to(w/2+w*0.05,h*0.16); c.line_to(w/2-w*0.04,h*0.16+w*0.05); c.close_path(); c.set_source_rgb(1,1,1); c.fill()
        text(c, "Description", w * 0.06, h * 0.34, w * 0.055, fill=(0.1, 0.1, 0.1), stroke=None, anchor="left")
        n = int(len(lines) * clamp(k) + 0.999)
        for i in range(n):
            col = (0.1, 0.1, 0.12)
            if "link" in lines[i] or "bit.ly" in lines[i]:
                S.rrect(c, w * 0.04, h * (0.385 + i * 0.065) - h * 0.04, w * 0.92, h * 0.058, h * 0.01)
                c.set_source_rgba(1.0, 0.85, 0.2, 0.55)
                c.fill()
            text(c, lines[i], w * 0.07, h * (0.39 + i * 0.065), w * 0.045, fill=col, stroke=None, anchor="left")
    return draw


# ---------------- infographic pieces ----------------
def big_number(c, txt, x, y, size, k, col=YEL, sub=None):
    sc = eob(k)
    c.save()
    c.translate(x, y)
    c.scale(sc, sc)
    text(c, txt, 0, 0, size, fill=col, stroke=(0, 0, 0), lw=size * 0.12)
    if sub:
        text(c, sub, 0, size * 0.55, size * 0.28, fill=(1, 1, 1), stroke=(0, 0, 0), lw=8)
    c.restore()


def people_grid(c, x, y, cols, rows, size, lit, k, col_on=RED, col_off=(0.5, 0.52, 0.6)):
    """lit = fraction highlighted (bottom-up order), k = reveal progress."""
    total = cols * rows
    shown = int(total * clamp(k))
    on = int(total * lit)
    i = 0
    for r in range(rows):
        for cc in range(cols):
            if i >= shown:
                return
            px, py = x + cc * size * 1.25, y + r * size * 1.6
            colr = col_on if i < on else col_off
            c.arc(px, py, size * 0.32, 0, 2 * math.pi)
            c.set_source_rgb(*colr)
            c.fill()
            S.rrect(c, px - size * 0.42, py + size * 0.38, size * 0.84, size * 0.6, size * 0.3)
            c.fill()
            i += 1


def coin(c, x, y, r, a=1.0):
    c.arc(x, y, r, 0, 2 * math.pi)
    c.set_source_rgba(1.0, 0.78, 0.18, a)
    c.fill_preserve()
    c.set_source_rgba(0.6, 0.42, 0.05, a)
    c.set_line_width(r * 0.18)
    c.stroke()
    text(c, "₹", x, y + r * 0.38, r * 1.1, fill=(0.6, 0.42, 0.05), stroke=None, alpha=a)


def money_flow(c, t, k, sources, target, n=26, seed=5):
    rnd = random.Random(seed)
    for i in range(n):
        sx, sy = sources[i % len(sources)]
        ph = (k * 1.6 + rnd.random()) % 1.0
        if k < rnd.random() * 0.4:
            continue
        x = sx + (target[0] - sx) * ease(ph)
        y = sy + (target[1] - sy) * ease(ph) - math.sin(ph * math.pi) * 160
        coin(c, x, y, 22, a=1 - ph * 0.3)


def stamp(c, txt, x, y, t0, t, ang=-6, col=RED, size=96):
    if t < t0:
        return
    k = (t - t0) / 0.16
    sc = 1.9 - 0.9 * ease(k) if k < 1 else 1.0
    c.save()
    c.translate(x, y)
    c.rotate(math.radians(ang))
    c.scale(sc, sc)
    c.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    c.set_font_size(size)
    e = c.text_extents(txt)
    w, h = e.x_advance + 70, size * 1.3
    S.rrect(c, -w / 2, -h / 2, w, h, 18)
    c.set_source_rgba(*col, 0.95)
    c.fill_preserve()
    c.set_source_rgb(1, 1, 1)
    c.set_line_width(8)
    c.stroke()
    c.move_to(-e.x_advance / 2, size * 0.36)
    c.text_path(txt)
    c.set_source_rgb(1, 1, 1)
    c.fill()
    c.restore()


def card(c, x, y, w, h, title, value, k, col=YEL):
    sc = eob(k)
    c.save()
    c.translate(x + w / 2, y + h / 2)
    c.scale(sc, sc)
    S.rrect(c, -w / 2, -h / 2, w, h, 28)
    c.set_source_rgba(0.08, 0.09, 0.14, 0.92)
    c.fill_preserve()
    c.set_source_rgba(*col, 0.9)
    c.set_line_width(5)
    c.stroke()
    text(c, title, 0, -h * 0.12, min(h * 0.2, w * 1.5 / max(1, len(title))), fill=(0.8, 0.82, 0.9), stroke=None, weight=cairo.FONT_WEIGHT_NORMAL)
    text(c, value, 0, h * 0.3, min(h * 0.34, w * 1.6 / max(1, len(value))), fill=col, stroke=None)
    c.restore()


def arrow(c, x0, y0, x1, y1, k, col=YEL, lw=14):
    x = x0 + (x1 - x0) * clamp(k)
    y = y0 + (y1 - y0) * clamp(k)
    c.set_line_width(lw)
    c.set_line_cap(cairo.LINE_CAP_ROUND)
    c.set_source_rgb(*col)
    c.move_to(x0, y0)
    c.line_to(x, y)
    c.stroke()
    if k > 0.05:
        ang = math.atan2(y1 - y0, x1 - x0)
        c.move_to(x + math.cos(ang + 2.6) * 40, y + math.sin(ang + 2.6) * 40)
        c.line_to(x, y)
        c.line_to(x + math.cos(ang - 2.6) * 40, y + math.sin(ang - 2.6) * 40)
        c.stroke()


def doc_sebi(c, x, y, w, h, k):
    """Generic report document (factual citation, no logo)."""
    c.save()
    c.translate(x, y)
    c.rotate(math.radians(-4 + 4 * ease(k)))
    S.rrect(c, 0, 0, w, h, 14)
    c.set_source_rgb(0.97, 0.96, 0.92)
    c.fill()
    c.rectangle(0, 0, w, h * 0.12)
    c.set_source_rgb(0.12, 0.2, 0.42)
    c.fill()
    text(c, "SEBI STUDY · F&O · FY25", w / 2, h * 0.08, w * 0.06, fill=(1, 1, 1), stroke=None)
    for i in range(9):
        c.rectangle(w * 0.08, h * (0.2 + i * 0.07), w * (0.84 - 0.2 * (i % 3 == 2)), h * 0.018)
        c.set_source_rgba(0.2, 0.2, 0.25, 0.35)
        c.fill()
    c.restore()
