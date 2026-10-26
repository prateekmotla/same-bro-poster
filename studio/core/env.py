"""Themed environments for Same Bro long-form (1920x1080 world units). Delhi feel, warm/cool practical lights."""
import math
import random

import cairo

import sys
sys.path.insert(0, "/home/claude/sid/v2")
import sid2 as S  # noqa: E402

W, H = 1920, 1080


def rgb(c, col, a=1.0):
    c.set_source_rgba(col[0], col[1], col[2], a)


def box(c, x, y, w, h, col, r=0, line=None, lw=4):
    if r:
        S.rrect(c, x, y, w, h, r)
    else:
        c.rectangle(x, y, w, h)
    rgb(c, col)
    if line:
        c.fill_preserve(); rgb(c, line); c.set_line_width(lw); c.stroke()
    else:
        c.fill()


def lingrad(c, x0, y0, x1, y1, stops):
    g = cairo.LinearGradient(x0, y0, x1, y1)
    for p, col in stops:
        g.add_color_stop_rgba(p, *col) if len(col) == 4 else g.add_color_stop_rgb(p, *col)
    return g


def light(c, x, y, r, col, a):
    g = cairo.RadialGradient(x, y, 0, x, y, r)
    g.add_color_stop_rgba(0, col[0], col[1], col[2], a)
    g.add_color_stop_rgba(1, col[0], col[1], col[2], 0)
    c.set_source(g)
    c.arc(x, y, r, 0, 2 * math.pi)
    c.fill()


def shade(c, a, col=(0, 0, 0)):
    c.set_source_rgba(*col, a)
    c.paint()


def text(c, s, x, y, size, col=(1, 1, 1), a=1.0, bold=True, anchor="center"):
    c.select_font_face("Poppins", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)
    c.set_font_size(size)
    e = c.text_extents(s)
    xx = x - e.x_advance / 2 if anchor == "center" else x
    c.move_to(xx, y)
    c.set_source_rgba(*col, a)
    c.show_text(s)


# ---------------------------------------------------------------- Sid's room
def room(c, t, mode="night", fan=True):
    night = mode == "night"
    # wall
    wall = (0.16, 0.19, 0.27) if night else (0.80, 0.74, 0.62)
    wall2 = (0.10, 0.12, 0.18) if night else (0.66, 0.60, 0.50)
    c.set_source(lingrad(c, 0, 0, 0, 760, [(0, wall2), (1, wall)]))
    c.rectangle(0, 0, W, 780); c.fill()
    # damp patch + switchboard (very Indian)
    light(c, 1500, 160, 140, (0, 0, 0), 0.10)
    box(c, 1180, 470, 120, 80, (0.88, 0.87, 0.82) if not night else (0.5, 0.5, 0.52), 8, (0.3, 0.3, 0.3), 3)
    for i in range(3):
        box(c, 1195 + i * 34, 488, 22, 34, (0.95, 0.95, 0.92) if not night else (0.6, 0.6, 0.62), 4)
    # skirting + floor
    box(c, 0, 760, W, 22, (0.08, 0.08, 0.1) if night else (0.45, 0.38, 0.3))
    c.set_source(lingrad(c, 0, 780, 0, H, [(0, (0.22, 0.2, 0.22) if night else (0.72, 0.62, 0.5)),
                                          (1, (0.10, 0.09, 0.1) if night else (0.55, 0.46, 0.36))]))
    c.rectangle(0, 780, W, 300); c.fill()
    for i in range(9):  # floor tiles
        c.move_to(i * 240 - 200, H); c.line_to(i * 200 + 60, 782)
        c.set_source_rgba(0, 0, 0, 0.12); c.set_line_width(3); c.stroke()
    # window with grill + city
    wx, wy, ww, wh = 140, 150, 420, 380
    box(c, wx - 16, wy - 16, ww + 32, wh + 32, (0.35, 0.3, 0.26) if not night else (0.2, 0.18, 0.18))
    if night:
        c.set_source(lingrad(c, 0, wy, 0, wy + wh, [(0, (0.04, 0.05, 0.14)), (1, (0.16, 0.1, 0.22))]))
    else:
        c.set_source(lingrad(c, 0, wy, 0, wy + wh, [(0, (0.55, 0.75, 0.95)), (1, (0.95, 0.85, 0.7))]))
    c.rectangle(wx, wy, ww, wh); c.fill()
    rnd = random.Random(3)
    for i in range(9):  # buildings
        bx = wx + i * 50 - 10
        bh = rnd.uniform(90, 230)
        box(c, bx, wy + wh - bh, 46, bh, (0.06, 0.06, 0.1) if night else (0.62, 0.58, 0.55))
        for j in range(int(bh // 30)):
            for k in range(2):
                if rnd.random() < (0.45 if night else 0.0):
                    box(c, bx + 8 + k * 18, wy + wh - bh + 12 + j * 30, 10, 14, (1, 0.8, 0.45))
    if not night:
        light(c, wx + 330, wy + 80, 120, (1, 0.95, 0.7), 0.7)
    for i in range(1, 6):  # grill
        c.move_to(wx + i * ww / 6, wy); c.line_to(wx + i * ww / 6, wy + wh)
    c.move_to(wx, wy + wh / 2); c.line_to(wx + ww, wy + wh / 2)
    c.set_source_rgba(0.1, 0.1, 0.1, 0.9); c.set_line_width(6); c.stroke()
    # curtain
    for side in (0, 1):
        x0 = wx - 60 if side == 0 else wx + ww - 30
        c.move_to(x0, wy - 40)
        for k in range(6):
            c.line_to(x0 + (k % 2) * 30 + 10 * math.sin(t + k), wy - 40 + k * 90)
        c.line_to(x0 + 90, wy + wh + 60); c.line_to(x0 + 90, wy - 40); c.close_path()
        rgb(c, (0.55, 0.16, 0.18) if not night else (0.3, 0.08, 0.12)); c.fill()
    # posters
    box(c, 700, 140, 200, 280, (0.95, 0.75, 0.2) if not night else (0.45, 0.35, 0.12), 6)
    text(c, "GRIND", 800, 230, 48, (0.1, 0.1, 0.1), 0.9)
    text(c, "NEVER", 800, 290, 40, (0.1, 0.1, 0.1), 0.9)
    text(c, "STOP", 800, 345, 52, (0.1, 0.1, 0.1), 0.9)
    box(c, 930, 180, 170, 230, (0.25, 0.55, 0.85) if not night else (0.12, 0.25, 0.4), 6)
    c.arc(1015, 270, 50, 0, 2 * math.pi); rgb(c, (0.98, 0.9, 0.7) if not night else (0.5, 0.45, 0.35)); c.fill()
    # tube light
    box(c, 1350, 70, 380, 26, (0.95, 0.97, 1.0) if not night else (0.35, 0.36, 0.4), 12)
    if not night:
        light(c, 1540, 80, 500, (1, 1, 1), 0.25)
    # shelf + books
    box(c, 1420, 260, 400, 18, (0.35, 0.24, 0.16))
    rnd = random.Random(7)
    x = 1435
    while x < 1800:
        w = rnd.uniform(22, 40)
        h = rnd.uniform(90, 140)
        box(c, x, 260 - h, w, h, rnd.choice([(0.7, 0.2, 0.2), (0.2, 0.4, 0.6), (0.85, 0.7, 0.3), (0.3, 0.5, 0.35)]))
        x += w + 4
    # desk with laptop + chai cup
    box(c, 1300, 640, 560, 30, (0.42, 0.29, 0.19))
    box(c, 1320, 670, 30, 200, (0.3, 0.2, 0.13)); box(c, 1810, 670, 30, 200, (0.3, 0.2, 0.13))
    c.save(); c.translate(1560, 640)
    box(c, -150, -10, 300, 14, (0.6, 0.62, 0.66), 4)
    c.move_to(-130, -10); c.line_to(-110, -190); c.line_to(110, -190); c.line_to(130, -10); c.close_path()
    rgb(c, (0.15, 0.16, 0.2)); c.fill()
    c.move_to(-115, -20); c.line_to(-98, -178); c.line_to(98, -178); c.line_to(115, -20); c.close_path()
    rgb(c, (0.2, 0.55, 0.4) if night else (0.25, 0.3, 0.4)); c.fill()
    c.restore()
    box(c, 1750, 600, 44, 40, (0.95, 0.95, 0.92), 6)
    c.arc(1798, 618, 12, -1.5, 1.5); c.set_line_width(5); rgb(c, (0.95, 0.95, 0.92)); c.stroke()
    # bed (left-centre)
    box(c, 520, 600, 900, 70, (0.36, 0.24, 0.17), 10)  # frame
    box(c, 520, 520, 40, 260, (0.3, 0.2, 0.14), 6)  # headboard post
    box(c, 540, 560, 860, 70, (0.88, 0.88, 0.92) if not night else (0.45, 0.46, 0.55), 20)  # mattress
    c.move_to(760, 575); c.curve_to(900, 540, 1200, 600, 1410, 560); c.line_to(1410, 660); c.line_to(760, 660)
    c.close_path(); rgb(c, (0.25, 0.42, 0.62) if not night else (0.15, 0.22, 0.36)); c.fill()  # blanket
    box(c, 560, 520, 190, 70, (0.97, 0.97, 0.98) if not night else (0.55, 0.56, 0.62), 30)  # pillow
    box(c, 560, 670, 860, 110, (0.3, 0.2, 0.14), 4)
    # ceiling fan (shadowed blades rotate)
    if fan:
        c.save(); c.translate(960, 40)
        box(c, -8, -60, 16, 60, (0.2, 0.2, 0.22))
        c.scale(1, 0.18)
        for i in range(3):
            a = t * 9 + i * 2 * math.pi / 3
            c.save(); c.rotate(a)
            S.rrect(c, 20, -24, 300, 48, 20)
            rgb(c, (0.55, 0.56, 0.6) if not night else (0.25, 0.25, 0.28)); c.fill(); c.restore()
        c.arc(0, 0, 40, 0, 2 * math.pi); rgb(c, (0.4, 0.4, 0.45)); c.fill()
        c.restore()
    if night:
        shade(c, 0.25, (0.02, 0.02, 0.08))


# ---------------------------------------------------------------- college canteen
def canteen(c, t):
    c.set_source(lingrad(c, 0, 0, 0, 700, [(0, (0.95, 0.88, 0.72)), (1, (0.86, 0.76, 0.58))]))
    c.rectangle(0, 0, W, 720); c.fill()
    box(c, 0, 700, W, 380, (0.55, 0.5, 0.45))
    for i in range(12):
        box(c, i * 170, 700, 4, 380, (0.48, 0.43, 0.39))
    # counter + menu board
    box(c, 1150, 120, 650, 300, (0.12, 0.2, 0.15), 8, (0.4, 0.3, 0.2), 10)
    text(c, "CANTEEN", 1475, 185, 54, (1, 0.85, 0.3))
    for i, (it, pr) in enumerate([("Chai", "₹10"), ("Samosa", "₹15"), ("Maggi", "₹40"), ("Cold coffee", "₹50")]):
        text(c, it, 1240, 250 + i * 44, 32, (0.95, 0.95, 0.9), anchor="left")
        text(c, pr, 1700, 250 + i * 44, 32, (0.95, 0.95, 0.9))
    box(c, 1100, 460, 750, 260, (0.62, 0.38, 0.22), 6)
    box(c, 1100, 450, 750, 26, (0.75, 0.75, 0.75), 4)
    for i in range(5):  # glass jars
        box(c, 1150 + i * 120, 380, 80, 80, (0.9, 0.95, 1.0), 14)
        c.arc(1190 + i * 120, 430, 22, 0, 2 * math.pi); rgb(c, (0.9, 0.6, 0.2) if i % 2 else (0.85, 0.75, 0.4)); c.fill()
    # notice board
    box(c, 120, 120, 420, 300, (0.62, 0.45, 0.28), 6, (0.4, 0.28, 0.15), 8)
    for i, col in enumerate([(1, 1, 0.7), (0.8, 0.9, 1), (1, 0.85, 0.85), (0.85, 1, 0.85)]):
        c.save(); c.translate(180 + (i % 2) * 190, 170 + (i // 2) * 120); c.rotate(0.05 * (i - 1.5))
        box(c, 0, 0, 150, 100, col); c.restore()
    text(c, "PLACEMENT DRIVE", 330, 400, 26, (0.15, 0.1, 0.05))
    # background students (silhouettes)
    for i, x in enumerate((640, 760, 900)):
        c.arc(x, 470 + (i % 2) * 10, 34, 0, 2 * math.pi); rgb(c, (0.55, 0.45, 0.4)); c.fill()
        S.rrect(c, x - 55, 505 + (i % 2) * 10, 110, 200, 40); rgb(c, [(0.6, 0.3, 0.3), (0.3, 0.4, 0.6), (0.4, 0.55, 0.4)][i]); c.fill()
    # table in foreground
    box(c, 260, 760, 1400, 46, (0.8, 0.82, 0.85), 10)
    box(c, 300, 806, 30, 260, (0.5, 0.5, 0.55)); box(c, 1590, 806, 30, 260, (0.5, 0.5, 0.55))
    for x in (520, 1300):
        box(c, x, 720, 46, 46, (0.95, 0.95, 0.92), 6)
        box(c, x + 6, 726, 34, 12, (0.7, 0.45, 0.25), 3)
    light(c, 600, 0, 900, (1, 0.95, 0.8), 0.2)


# ---------------------------------------------------------------- Delhi street at night (scrollable)
def street(c, t, off=0.0, night=True):
    sky = [(0, (0.05, 0.05, 0.14)), (1, (0.25, 0.12, 0.25))] if night else [(0, (0.6, 0.78, 0.95)), (1, (0.95, 0.85, 0.7))]
    c.set_source(lingrad(c, 0, 0, 0, 700, sky)); c.rectangle(0, 0, W, 760); c.fill()
    rnd = random.Random(11)
    # far buildings (parallax 0.3)
    c.save(); c.translate(-(off * 0.3) % 600, 0)
    for rep in range(5):
        for i in range(6):
            bx = rep * 600 + i * 100 - 600
            bh = 200 + (i * 53 % 160)
            box(c, bx, 640 - bh, 96, bh + 40, (0.1, 0.09, 0.16) if night else (0.7, 0.66, 0.62))
            for j in range(int(bh // 40)):
                if (i + j + rep) % 3 == 0 and night:
                    box(c, bx + 20, 660 - bh + j * 40, 18, 18, (1, 0.75, 0.4))
    c.restore()
    # near buildings with shop shutters (parallax 0.7)
    c.save(); c.translate(-(off * 0.7) % 900, 0)
    signs = ["MOBILE REPAIR", "SHARMA STORE", "CHAI POINT", "XEROX", "ATM"]
    for rep in range(4):
        x0 = rep * 900 - 900
        for i in range(3):
            bx = x0 + i * 300
            box(c, bx, 260, 296, 520, [(0.5, 0.36, 0.3), (0.42, 0.42, 0.5), (0.55, 0.48, 0.32)][i])
            box(c, bx + 30, 330, 70, 90, (0.15, 0.15, 0.2)); box(c, bx + 190, 330, 70, 90, (0.15, 0.15, 0.2))
            if night and (i + rep) % 2 == 0:
                box(c, bx + 34, 334, 62, 82, (1, 0.8, 0.45))
            sg = signs[(i + rep * 3) % len(signs)]
            box(c, bx + 20, 470, 256, 60, (0.95, 0.85, 0.2) if i % 2 == 0 else (0.85, 0.2, 0.25), 4)
            text(c, sg, bx + 148, 512, 28, (0.1, 0.1, 0.1) if i % 2 == 0 else (1, 1, 1))
            box(c, bx + 20, 540, 256, 220, (0.55, 0.55, 0.6))
            for k in range(10):
                box(c, bx + 20, 548 + k * 21, 256, 4, (0.45, 0.45, 0.5))
            if night and i == 1:
                light(c, bx + 148, 640, 200, (1, 0.8, 0.5), 0.35)
                box(c, bx + 20, 540, 256, 220, (0.95, 0.8, 0.55))
                box(c, bx + 60, 600, 170, 120, (0.6, 0.4, 0.25), 6)
        # tangled wires
        for k in range(4):
            c.move_to(x0 - 50, 200 + k * 18)
            c.curve_to(x0 + 300, 270 + k * 25, x0 + 600, 230 + k * 10, x0 + 950, 210 + k * 20)
            c.set_source_rgba(0.02, 0.02, 0.02, 0.9); c.set_line_width(3); c.stroke()
        # lamp post
        box(c, x0 + 860, 160, 16, 620, (0.2, 0.2, 0.22))
        box(c, x0 + 820, 150, 90, 22, (0.25, 0.25, 0.28), 6)
        if night:
            light(c, x0 + 865, 180, 380, (1, 0.8, 0.45), 0.45)
    c.restore()
    # road + footpath
    box(c, 0, 780, W, 60, (0.55, 0.52, 0.5) if not night else (0.3, 0.29, 0.3))
    for i in range(-1, 14):
        x = i * 160 - (off % 160)
        box(c, x, 780, 156, 8, (0.85, 0.75, 0.2) if i % 2 else (0.2, 0.2, 0.2))
    box(c, 0, 840, W, 240, (0.2, 0.2, 0.23) if night else (0.38, 0.38, 0.4))
    for i in range(-1, 10):
        x = i * 260 - (off * 1.0 % 260)
        box(c, x, 950, 140, 12, (0.9, 0.9, 0.85))
    if night:
        shade(c, 0.12, (0.05, 0.0, 0.1))


def auto_rickshaw(c, x, y, s=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.move_to(-160, 0); c.line_to(-160, -150); c.curve_to(-150, -230, 60, -240, 120, -200); c.line_to(170, -60)
    c.line_to(170, 0); c.close_path(); rgb(c, (0.15, 0.55, 0.3)); c.fill()
    box(c, -160, -60, 330, 60, (0.95, 0.8, 0.15), 8)
    box(c, -60, -170, 140, 100, (0.6, 0.8, 0.9), 10)
    for wx in (-110, 130):
        c.arc(wx, 0, 38, 0, 2 * math.pi); rgb(c, (0.08, 0.08, 0.08)); c.fill()
        c.arc(wx, 0, 16, 0, 2 * math.pi); rgb(c, (0.6, 0.6, 0.6)); c.fill()
    c.restore()


# ---------------------------------------------------------------- live trader studio (wide)
def studio(c, t):
    c.set_source(lingrad(c, 0, 0, 0, H, [(0, (0.12, 0.05, 0.2)), (1, (0.03, 0.02, 0.06))]))
    c.paint()
    # LED strips
    for i, col in enumerate([(0.9, 0.2, 0.8), (0.3, 0.4, 1.0), (0.9, 0.2, 0.8), (0.3, 0.4, 1.0)]):
        x = 180 + i * 520
        box(c, x, 80, 16, 760, col)
        light(c, x + 8, 460, 220, col, 0.25)
    # wall screens with candles
    rnd = random.Random(5)
    for k, sx in enumerate((300, 1320)):
        box(c, sx, 160, 420, 260, (0.02, 0.03, 0.05), 8, (0.25, 0.25, 0.3), 6)
        p = 300
        for i in range(16):
            o = p
            p = max(180, min(400, p + rnd.uniform(-30, 28) + (8 if k == 0 else -6)))
            col = (0.2, 0.85, 0.45) if p < o else (0.95, 0.25, 0.3)
            box(c, sx + 20 + i * 24, min(o, p) - 0, 14, abs(p - o) + 4, col)
    # ring light
    c.arc(960, 430, 300, 0, 2 * math.pi); c.set_source_rgba(1, 0.92, 1, 0.85); c.set_line_width(26); c.stroke()
    light(c, 960, 430, 520, (1, 0.8, 1), 0.18)
    # desk
    box(c, 300, 820, 1320, 260, (0.08, 0.08, 0.1))
    box(c, 300, 810, 1320, 20, (0.3, 0.3, 0.36))
    # mic
    c.move_to(1300, 820); c.line_to(1260, 640); c.set_line_width(10); rgb(c, (0.15, 0.15, 0.17)); c.stroke()
    box(c, 1225, 560, 70, 120, (0.1, 0.1, 0.12), 34)


# ---------------------------------------------------------------- metro coach
def metro(c, t):
    box(c, 0, 0, W, H, (0.82, 0.84, 0.86))
    box(c, 0, 0, W, 80, (0.9, 0.92, 0.95))
    for x in (300, 960, 1620):
        box(c, x - 200, 40, 400, 20, (1, 1, 1), 10)
    # windows with passing lights (tunnel)
    for i in range(3):
        wx = 120 + i * 620
        box(c, wx, 180, 460, 260, (0.06, 0.07, 0.1), 30, (0.6, 0.62, 0.66), 10)
        for k in range(6):
            lx = wx + ((k * 160 - t * 900) % 600) - 70
            if wx < lx < wx + 460:
                box(c, lx, 300, 60, 10, (1, 0.85, 0.5))
    # route map strip
    box(c, 300, 470, 1320, 40, (1, 1, 1), 6)
    c.move_to(330, 490); c.line_to(1590, 490); c.set_line_width(8); rgb(c, (0.8, 0.2, 0.5)); c.stroke()
    for i in range(12):
        c.arc(330 + i * 114, 490, 9, 0, 2 * math.pi); rgb(c, (1, 1, 1)); c.fill_preserve()
        rgb(c, (0.8, 0.2, 0.5)); c.set_line_width(4); c.stroke()
    # seats
    box(c, 0, 640, W, 120, (0.65, 0.68, 0.72), 10)
    box(c, 0, 760, W, 320, (0.5, 0.52, 0.56))
    # poles
    for x in (420, 1500):
        box(c, x, 80, 22, 1000, (0.85, 0.85, 0.9))
        box(c, x + 6, 80, 6, 1000, (1, 1, 1))
