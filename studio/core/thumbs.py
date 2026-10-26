"""Same Bro thumbnail system.
THEME: deep navy bg + one accent light, yellow #FFCC29 keywords, red for loss/danger, max 4 words,
heavy font (Inter Display Black) with thick black outline, big emotional face, 'SAME BRO' corner tag.
"""
import math
import sys

import cairo
import numpy as np
from PIL import Image

sys.path.insert(0, "/home/claude/sid/v3")
import chars as CH  # noqa: E402
import props as P  # noqa: E402
import sid2 as S  # noqa: E402

YEL = (1.0, 0.80, 0.16)
RED = (0.94, 0.22, 0.25)
GRN = (0.22, 0.85, 0.48)
FONT = "Inter Display Black"


def words(c, parts, x, y, size, anchor="left", lw=None, tilt=0, shadow=True):
    """parts: list of (text, color). Draws on one line with thick black outline + drop shadow."""
    c.save()
    c.translate(x, y)
    c.rotate(math.radians(tilt))
    c.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    c.set_font_size(size)
    sp = size * 0.25
    widths = [c.text_extents(t).x_advance for t, _ in parts]
    total = sum(widths) + sp * (len(parts) - 1)
    xx = -total / 2 if anchor == "center" else (-total if anchor == "right" else 0)
    lw = lw or size * 0.16
    for (t, col), w in zip(parts, widths):
        for dx, dy, a in (((10, 12, 0.55),) if shadow else ()):
            c.move_to(xx + dx, dy)
            c.text_path(t)
            c.set_source_rgba(0, 0, 0, a)
            c.fill()
        c.move_to(xx, 0)
        c.text_path(t)
        c.set_source_rgb(0, 0, 0)
        c.set_line_width(lw)
        c.set_line_join(cairo.LINE_JOIN_ROUND)
        c.stroke_preserve()
        c.set_source_rgb(*col)
        c.fill()
        xx += w + sp
    c.restore()
    return total


def tag(c, x, y, s=1.0):
    c.save()
    c.translate(x, y)
    c.scale(s, s)
    S.rrect(c, 0, 0, 230, 62, 31)
    c.set_source_rgb(0.06, 0.06, 0.08)
    c.fill_preserve()
    c.set_source_rgb(*YEL)
    c.set_line_width(4)
    c.stroke()
    c.select_font_face(FONT, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    c.set_font_size(32)
    c.move_to(30, 43)
    c.text_path("SAME BRO")
    c.set_source_rgb(*YEL)
    c.fill()
    c.restore()


def bg(c, w, h, accent=(1.0, 0.8, 0.16), ax=0.7):
    g = cairo.LinearGradient(0, 0, 0, h)
    g.add_color_stop_rgb(0, 0.07, 0.08, 0.15)
    g.add_color_stop_rgb(1, 0.02, 0.02, 0.05)
    c.set_source(g)
    c.paint()
    P.glow(c, w * ax, h * 0.45, max(w, h) * 0.55, accent, 0.28)
    # subtle rays
    c.save()
    c.translate(w * ax, h * 0.45)
    for i in range(18):
        c.rotate(math.pi * 2 / 18)
        c.move_to(0, 0)
        c.line_to(max(w, h), -60)
        c.line_to(max(w, h), 60)
        c.close_path()
        c.set_source_rgba(*accent, 0.035)
        c.fill()
    c.restore()


def vignette_grain(sf):
    w, h = sf.get_width(), sf.get_height()
    buf = np.ndarray((h, w, 4), np.uint8, sf.get_data())
    rgb = buf[..., [2, 1, 0]].astype(np.float32)
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx - w / 2) / (w * 0.7)) ** 2 + ((yy - h / 2) / (h * 0.7)) ** 2)
    rgb *= np.clip(1.12 - 0.45 * r ** 2, 0.45, 1)[..., None]
    rgb += np.random.default_rng(1).normal(0, 4, rgb.shape)
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))


# ---------------- live traders: long-form 16:9 ----------------
def thumb_live_A(path):
    W, H = 1280, 720
    sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    c = cairo.Context(sf)
    bg(c, W, H, accent=(0.9, 0.25, 0.75), ax=0.72)
    # LIVE badge + phone frame behind bhai
    CH.bhai_body(c, 900, 330, 0.95, 0.4, arms=((12, -8), (12, -8)))
    CH.bhai_head(c, 900, 330, 0.95, 0.4, mouth='bigsmile', talk=0.4, **{'raise': 0.3})
    S.rrect(c, 690, 60, 150, 62, 14)
    c.set_source_rgb(*RED); c.fill()
    words(c, [("LIVE", (1, 1, 1))], 765, 106, 44, anchor="center", lw=0.1, shadow=False)
    # coins raining toward him
    for i, (x, y, r) in enumerate(((620, 520, 34), (700, 600, 28), (560, 640, 26), (1150, 560, 30), (1080, 650, 24),
                                   (1200, 300, 22), (640, 380, 20))):
        P.coin(c, x, y, r)
    # text block
    words(c, [("HIS", (1, 1, 1)), ("INCOME", YEL)], 50, 230, 110)
    words(c, [("=", (1, 1, 1)), ("YOU", RED)], 50, 380, 150)
    words(c, [("not his trades", (0.85, 0.87, 0.95))], 56, 470, 52, lw=8)
    tag(c, 50, 620)
    vignette_grain(sf).save(path)


def thumb_live_B(path):
    """A/B variant: big ₹ number + shocked Sid (curiosity gap)."""
    W, H = 1280, 720
    sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    c = cairo.Context(sf)
    bg(c, W, H, accent=(0.2, 0.85, 0.45), ax=0.3)
    CH.sid_body(c, 1010, 360, 1.0, 0.2, arms=((40, 140), (40, 140)))
    CH.sid_head(c, 1010, 360, 1.0, 0.2, eyes=1.25, mouth='o', **{'raise': 1.0}, sweat=1.0, look=(-0.6, 0))
    words(c, [("₹4,00,000", GRN)], 50, 250, 150)
    words(c, [("/MONTH", (1, 1, 1))], 60, 360, 90)
    words(c, [("without", (0.85, 0.87, 0.95)), ("WINNING", YEL)], 56, 480, 72, lw=10)
    words(c, [("a single trade", (0.85, 0.87, 0.95))], 56, 560, 56, lw=8)
    tag(c, 50, 625)
    vignette_grain(sf).save(path)


# ---------------- live traders: short / reel cover 9:16 ----------------
def cover_live(path):
    W, H = 1080, 1920
    sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    c = cairo.Context(sf)
    bg(c, W, H, accent=(0.9, 0.25, 0.75), ax=0.5)
    # middle band (stays visible in the 4:5 / 1:1 grid crop on Instagram)
    CH.bhai_body(c, 540, 820, 1.55, 0.4, arms=((12, -8), (12, -8)))
    CH.bhai_head(c, 540, 820, 1.55, 0.4, mouth='bigsmile', talk=0.4)
    S.rrect(c, 420, 450, 240, 90, 18)
    c.set_source_rgb(*RED); c.fill()
    words(c, [("LIVE", (1, 1, 1))], 540, 520, 70, anchor="center", lw=0.1, shadow=False)
    for x, y, r in ((200, 900, 46), (880, 980, 40), (160, 1180, 34), (930, 760, 30)):
        P.coin(c, x, y, r)
    words(c, [("HIS", (1, 1, 1)), ("INCOME", YEL)], 540, 1330, 120, anchor="center")
    words(c, [("=", (1, 1, 1)), ("YOU", RED)], 540, 1490, 170, anchor="center")
    tag(c, 425, 1580, 1.0)
    vignette_grain(sf).save(path)


if __name__ == "__main__":
    thumb_live_A("thumb_live_A.png")
    thumb_live_B("thumb_live_B.png")
    cover_live("cover_live.png")
    print("ok")
