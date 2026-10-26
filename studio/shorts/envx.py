"""Extra environments for shorts (1920x1080 world)."""
import math
import random
import sys

sys.path.insert(0, "/home/claude/sid/long1")
import env as V  # noqa: E402
import sid2 as S  # noqa: E402
from ui import T, YEL, RED, GRN, WHITE  # noqa: E402

box, light, lingrad, rgb = V.box, V.light, V.lingrad, V.rgb


def gym(c, t, crowd=0):
    c.set_source(lingrad(c, 0, 0, 0, 760, [(0, (0.12, 0.13, 0.16)), (1, (0.2, 0.21, 0.25))]))
    c.rectangle(0, 0, 1920, 780); c.fill()
    # mirror wall
    box(c, 120, 160, 1680, 520, (0.42, 0.5, 0.58), 6, (0.6, 0.62, 0.66), 8)
    for i in range(6):
        c.move_to(200 + i * 300, 170); c.line_to(120 + i * 300, 670)
        c.set_source_rgba(1, 1, 1, 0.08); c.set_line_width(40); c.stroke()
    # neon sign
    box(c, 760, 40, 400, 100, (0.05, 0.05, 0.07), 20)
    T(c, "POWER GYM", 960, 112, 60, (1, 0.3, 0.4), stroke=None)
    light(c, 960, 90, 400, (1, 0.3, 0.4), 0.18)
    # floor
    box(c, 0, 780, 1920, 300, (0.1, 0.1, 0.11))
    for i in range(12):
        c.move_to(i * 200 - 300, 1080); c.line_to(i * 170 + 40, 780)
        c.set_source_rgba(1, 1, 1, 0.04); c.set_line_width(3); c.stroke()
    # dumbbell rack
    box(c, 200, 620, 620, 30, (0.25, 0.25, 0.28), 6)
    box(c, 220, 650, 20, 130, (0.25, 0.25, 0.28)); box(c, 780, 650, 20, 130, (0.25, 0.25, 0.28))
    for i in range(9):
        x = 240 + i * 62
        box(c, x, 590, 14, 34, (0.08, 0.08, 0.08), 4); box(c, x + 34, 590, 14, 34, (0.08, 0.08, 0.08), 4)
        box(c, x + 10, 600, 30, 12, (0.6, 0.6, 0.62), 3)
    # treadmills
    for i in range(3):
        x = 1050 + i * 260
        c.move_to(x, 780); c.line_to(x + 200, 780); c.line_to(x + 180, 740); c.line_to(x + 10, 740); c.close_path()
        rgb(c, (0.15, 0.15, 0.17)); c.fill()
        box(c, x + 170, 560, 16, 190, (0.3, 0.3, 0.33))
        box(c, x + 130, 540, 100, 50, (0.1, 0.1, 0.12), 8)
        box(c, x + 145, 550, 70, 30, (0.2, 0.6, 0.9), 4)
    light(c, 960, 0, 1100, (1, 1, 1), 0.12)
    if crowd:
        rnd = random.Random(2)
        for r in range(4):
            for k in range(int(crowd)):
                x = rnd.uniform(60, 1860); y = 640 + r * 110
                col = rnd.choice([(0.6, 0.3, 0.3), (0.3, 0.4, 0.6), (0.4, 0.55, 0.4), (0.6, 0.55, 0.3), (0.35, 0.35, 0.4)])
                s = 0.8 + r * 0.15
                c.arc(x, y - 70 * s, 26 * s, 0, 2 * math.pi); c.set_source_rgb(0.62, 0.45, 0.33); c.fill()
                S.rrect(c, x - 40 * s, y - 45 * s, 80 * s, 130 * s, 30 * s); rgb(c, col); c.fill()


def reception(c, t):
    gym(c, t)
    box(c, 0, 640, 1920, 440, (0.32, 0.22, 0.16))
    box(c, 0, 630, 1920, 30, (0.85, 0.85, 0.88))
    box(c, 1200, 200, 620, 380, (0.05, 0.05, 0.07), 20, (1, 0.3, 0.4), 6)
    T(c, "MEMBERSHIP", 1510, 270, 50, WHITE, stroke=None)
    T(c, "Monthly   ₹2,000", 1510, 380, 46, (0.85, 0.87, 0.95), stroke=None)
    T(c, "Yearly  ₹10,000", 1510, 480, 54, YEL, stroke=None)
    T(c, "BEST DEAL!", 1510, 545, 36, (1, 0.3, 0.4), stroke=None)


def shop_phone_screen(price, mrp, off, t, stock=None, timer=None):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
        c.rectangle(0, 0, w, 120); c.set_source_rgb(0.15, 0.35, 0.9); c.fill()
        T(c, "BIG SALE", w / 2, 85, 50, YEL, stroke=None)
        S.rrect(c, 40, 160, w - 80, 340, 20); c.set_source_rgb(0.88, 0.9, 0.95); c.fill()
        S.rrect(c, w / 2 - 70, 210, 140, 240, 22); c.set_source_rgb(0.1, 0.1, 0.12); c.fill()
        T(c, f"{off}% OFF", w / 2, 580, 70, RED, stroke=None)
        T(c, f"₹{price:,}", w / 2, 670, 60, (0.1, 0.1, 0.12), stroke=None)
        T(c, f"MRP ₹{mrp:,}", w / 2, 730, 34, (0.5, 0.5, 0.55), stroke=None)
        c.move_to(w / 2 - 130, 720); c.line_to(w / 2 + 130, 720); c.set_source_rgb(0.5, 0.5, 0.55); c.set_line_width(3); c.stroke()
        if stock:
            S.rrect(c, 40, 780, w - 80, 70, 14); c.set_source_rgb(1, 0.9, 0.9); c.fill()
            T(c, stock, w / 2, 828, 32, RED, stroke=None)
        if timer:
            T(c, timer, w / 2, 910, 36, (0.1, 0.1, 0.12), stroke=None)
        S.rrect(c, 40, h - 140, w - 80, 90, 45); c.set_source_rgb(1, 0.6, 0.1); c.fill()
        T(c, "BUY NOW", w / 2, h - 80, 40, WHITE, stroke=None)
    return f
