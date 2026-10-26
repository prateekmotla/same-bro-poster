"""Same Bro thumbnails v2 — clean: blurred scene, ONE big face, max 4 words that call the viewer out."""
import math
import sys

import cairo
import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, "/home/claude/sid/v3")
sys.path.insert(0, "/home/claude/sid/v2")
import chars as CH  # noqa: E402
import props as P  # noqa: E402
import sid2 as S  # noqa: E402
from thumbs import words, tag, YEL, RED, GRN  # noqa: E402

WHITE = (1, 1, 1)


def surf(w, h):
    s = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    return s, cairo.Context(s)


def to_pil(s):
    s.flush()
    return Image.frombuffer("RGBA", (s.get_width(), s.get_height()), bytes(s.get_data()), "raw", "BGRa", 0, 1)


def finish(img, path):
    rgb = np.asarray(img.convert("RGB")).astype(np.float32)
    h, w = rgb.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx - w / 2) / (w * 0.75)) ** 2 + ((yy - h / 2) / (h * 0.75)) ** 2)
    rgb *= np.clip(1.1 - 0.5 * r ** 2, 0.4, 1)[..., None]
    rgb = (rgb - 128) * 1.06 + 128  # contrast
    rgb += np.random.default_rng(2).normal(0, 3, rgb.shape)
    Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).save(path, quality=95)


def scene_live(w, h, cx, accent):
    """Blurred background: studio with ring light, LIVE screens, candle charts."""
    s, c = surf(w, h)
    g = cairo.LinearGradient(0, 0, 0, h)
    g.add_color_stop_rgb(0, 0.08, 0.06, 0.16)
    g.add_color_stop_rgb(1, 0.02, 0.02, 0.05)
    c.set_source(g); c.paint()
    P.candles(c, 0, h * 0.15, w, h * 0.55, seed=4, n=26, trend=-0.6, crash=8)
    P.glow(c, cx, h * 0.42, h * 0.75, accent, 0.45)
    c.set_line_width(h * 0.03)
    c.arc(cx, h * 0.42, h * 0.36, 0, 2 * math.pi)
    c.set_source_rgba(1, 0.9, 1, 0.8); c.stroke()
    return to_pil(s).filter(ImageFilter.GaussianBlur(h * 0.018))


def phone_glow_face(c, x, y, s):
    """Cold screen light from below on the face."""
    g = cairo.RadialGradient(x, y + 260 * s, 0, x, y + 260 * s, 380 * s)
    g.add_color_stop_rgba(0, 0.55, 0.75, 1.0, 0.35)
    g.add_color_stop_rgba(1, 0.55, 0.75, 1.0, 0)
    c.set_source(g); c.paint()


def held_phone(c, x, y, s, live=True):
    c.save(); c.translate(x, y); c.rotate(-0.18); c.scale(s, s)
    S.rrect(c, -95, -170, 190, 340, 26); c.set_source_rgb(0.05, 0.05, 0.07); c.fill()
    S.rrect(c, -84, -158, 168, 316, 18)
    g = cairo.LinearGradient(0, -158, 0, 158)
    g.add_color_stop_rgb(0, 0.35, 0.15, 0.55); g.add_color_stop_rgb(1, 0.12, 0.05, 0.2)
    c.set_source(g); c.fill()
    if live:
        S.rrect(c, -70, -140, 74, 34, 8); c.set_source_rgb(*RED); c.fill()
        P.text(c, "LIVE", -33, -114, 22, fill=WHITE, stroke=None)
        P.candles(c, -75, -60, 150, 150, seed=9, n=10, trend=-0.8)
    c.restore()
    # hand
    c.save(); c.translate(x - 10 * s, y + 120 * s); c.scale(s, s)
    S.rrect(c, -70, -30, 140, 120, 50); c.set_source_rgb(*S.SKIN[:3]) if isinstance(S.SKIN, tuple) else None
    c.set_source_rgb(0.72, 0.47, 0.32); c.fill()
    c.restore()


def thumb_A(path):
    """'STILL TAKING HIS ENTRY?' — calls out the viewer. Guilty Sid + phone LIVE."""
    W, H = 1280, 720
    base = scene_live(W, H, 900, (0.85, 0.3, 0.85))
    s, c = surf(W, H)
    P.glow(c, 960, 330, 420, (1.0, 0.8, 0.3), 0.18)
    CH.sid_body(c, 960, 330, 1.55, 0.2, arms=((14, -10), (14, -10)))
    CH.sid_head(c, 960, 330, 1.55, 0.2, tilt=-4, mouth='o', eyes=1.2, sweat=1.0, look=(0.7, 0.5), **{'raise': 0.9})
    phone_glow_face(c, 960, 330, 1.55)
    held_phone(c, 1190, 620, 0.9)
    base.alpha_composite(to_pil(s))
    s, c = surf(W, H)
    words(c, [("LIVE TRADERS", YEL)], 46, 175, 86)
    words(c, [("ARE FOOLING", WHITE)], 46, 290, 86)
    words(c, [("YOU", RED)], 46, 470, 190)
    tag(c, 52, 620)
    base.alpha_composite(to_pil(s))
    finish(base, path)


def thumb_B(path):
    """'YOU LOSE. HE EARNS.' — two-sided: broken Sid sharp, smug Live Bhai behind."""
    W, H = 1280, 720
    base = scene_live(W, H, 1040, (0.25, 0.85, 0.45))
    s, c = surf(W, H)  # bhai layer, soft-blurred to push it back
    CH.bhai_body(c, 1130, 260, 0.95, 0.3, arms=((70, 120), (70, 120)))
    CH.bhai_head(c, 1130, 260, 0.95, 0.3, mouth='smirk', tilt=5)
    for x, y, r in ((960, 520, 28), (1190, 470, 24), (1010, 610, 22), (1220, 610, 26)):
        P.coin(c, x, y, r)
    base.alpha_composite(to_pil(s).filter(ImageFilter.GaussianBlur(2.5)))
    s, c = surf(W, H)
    CH.sid_body(c, 850, 430, 1.4, 0.2, arms=((14, -10), (14, -10)))
    CH.sid_head(c, 850, 430, 1.4, 0.2, tilt=5, mouth='frown', sad=1, bags=1, eyes=0.7, look=(0, 0.6), tear=1)
    base.alpha_composite(to_pil(s))
    s, c = surf(W, H)
    words(c, [("REALITY OF", WHITE)], 46, 220, 90)
    words(c, [("LIVE", YEL)], 46, 360, 130)
    words(c, [("TRADERS", YEL)], 46, 500, 130)
    tag(c, 50, 620)
    base.alpha_composite(to_pil(s))
    finish(base, path)


def cover_short(path):
    W, H = 1080, 1920
    base = scene_live(W, H, 540, (0.85, 0.3, 0.85))
    s, c = surf(W, H)
    CH.sid_body(c, 540, 1050, 2.5, 0.2, arms=((14, -10), (14, -10)))
    CH.sid_head(c, 540, 1050, 2.5, 0.2, tilt=-4, mouth='o', eyes=1.2, sweat=1.0, look=(0.6, 0.5), **{'raise': 0.9})
    phone_glow_face(c, 540, 1050, 2.5)
    held_phone(c, 880, 1520, 1.4)
    base.alpha_composite(to_pil(s))
    s, c = surf(W, H)
    words(c, [("LIVE TRADERS", YEL)], 540, 360, 130, anchor="center")
    words(c, [("ARE FOOLING", WHITE)], 540, 495, 112, anchor="center")
    words(c, [("YOU", RED)], 540, 650, 160, anchor="center")
    tag(c, 425, 1760)
    base.alpha_composite(to_pil(s))
    finish(base, path)


if __name__ == "__main__":
    thumb_A("thumb2_A.jpg")
    thumb_B("thumb2_B.jpg")
    cover_short("cover2_short.jpg")
    print("ok")
