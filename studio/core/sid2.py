"""Sid v2 — polished flat-illustration character (pycairo). Head-centric: most shots are close/medium."""
import math
import cairo


def C(h, a=1.0):
    h = h.lstrip('#')
    return (int(h[0:2], 16) / 255, int(h[2:4], 16) / 255, int(h[4:6], 16) / 255, a)


SKIN, SKIN_SH, SKIN_HI, SKIN_LN = C('C98C5F'), C('A06540'), C('E3A97C'), C('5B3322')
HAIR, HAIR_HI, HAIR_LN = C('1B1517'), C('3E3236'), C('0E0A0B')
HOOD, HOOD_SH, HOOD_HI, HOOD_LN = C('4A5262'), C('363C4A'), C('5E6779'), C('1E222C')
EYE_W, IRIS, PUPIL = C('F7F2EA'), C('4A2C18'), C('0C0705')
MOUTH_IN, TEETH, TONGUE = C('5A1E22'), C('F4EFE8'), C('B5525A')


def src(ctx, col):
    ctx.set_source_rgba(*col)


def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def ease_out_back(t, s=1.7):
    t = max(0.0, min(1.0, t)) - 1
    return t * t * ((s + 1) * t + s) + 1


def rrect(ctx, x, y, w, h, r):
    r = min(r, w / 2, h / 2)
    ctx.new_sub_path()
    ctx.arc(x + w - r, y + r, r, -math.pi / 2, 0)
    ctx.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    ctx.arc(x + r, y + h - r, r, math.pi / 2, math.pi)
    ctx.arc(x + r, y + r, r, math.pi, 3 * math.pi / 2)
    ctx.close_path()


def face_path(ctx):
    ctx.new_path()
    ctx.move_to(-116, -20)
    ctx.curve_to(-118, -110, -60, -138, 0, -138)
    ctx.curve_to(60, -138, 118, -110, 116, -20)
    ctx.curve_to(114, 40, 96, 92, 58, 120)
    ctx.curve_to(34, 138, -34, 138, -58, 120)
    ctx.curve_to(-96, 92, -114, 40, -116, -20)
    ctx.close_path()


def shade_inside(ctx, path_fn, shadow_col, dx, dy, blur_steps=4):
    """Soft inner shadow: clip to shape, draw offset shape inverted with soft edge."""
    ctx.save()
    path_fn(ctx)
    ctx.clip()
    for i in range(blur_steps):
        k = (i + 1) / blur_steps
        ctx.save()
        ctx.translate(dx * (1 + 0.15 * i), dy * (1 + 0.15 * i))
        ctx.rectangle(-2000, -2000, 4000, 4000)
        path_fn(ctx)
        ctx.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
        r, g, b, a = shadow_col
        ctx.set_source_rgba(r, g, b, a / blur_steps * (1.3 - 0.3 * k))
        ctx.fill()
        ctx.restore()
    ctx.restore()


def eye(ctx, sx, open_, look, bags, squint):
    ex, ey = sx * 46, 4
    w, h = 36, 22 * max(0.0, open_)
    ctx.save()
    ctx.translate(ex, ey)
    # eye bags
    if bags > 0:
        ctx.new_path()
        ctx.move_to(-30, 18)
        ctx.curve_to(-14, 34, 14, 34, 30, 18)
        ctx.set_source_rgba(0.35, 0.2, 0.3, 0.28 * bags)
        ctx.set_line_width(9)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.stroke()
    if open_ > 0.08:
        top = -h - squint * 4
        bot = h * 0.75 - squint * 6

        def almond(c):
            c.new_path()
            c.move_to(-w, 2)
            c.curve_to(-w * 0.5, top * 1.25, w * 0.5, top * 1.25, w, -1)
            c.curve_to(w * 0.5, bot * 1.2, -w * 0.5, bot * 1.2, -w, 2)
            c.close_path()
        almond(ctx)
        src(ctx, EYE_W)
        ctx.fill()
        ctx.save()
        almond(ctx)
        ctx.clip()
        ix, iy = look[0] * 13, look[1] * 8 + 1
        g = cairo.RadialGradient(ix - 4, iy - 5, 2, ix, iy, 17)
        g.add_color_stop_rgb(0, 0.48, 0.30, 0.17)
        g.add_color_stop_rgb(1, 0.22, 0.12, 0.06)
        ctx.arc(ix, iy, 16, 0, 2 * math.pi)
        ctx.set_source(g)
        ctx.fill()
        ctx.arc(ix, iy, 8, 0, 2 * math.pi)
        src(ctx, PUPIL)
        ctx.fill()
        ctx.arc(ix + 5, iy - 6, 4.5, 0, 2 * math.pi)
        ctx.set_source_rgba(1, 1, 1, 0.95)
        ctx.fill()
        ctx.arc(ix - 5, iy + 5, 2, 0, 2 * math.pi)
        ctx.fill()
        # lid shadow on eyeball
        ctx.rectangle(-w, top * 1.3 - 10, 2 * w, 14)
        ctx.set_source_rgba(0.3, 0.18, 0.12, 0.25)
        ctx.fill()
        ctx.restore()
        # upper lash line
        ctx.new_path()
        ctx.move_to(-w - 3, 3)
        ctx.curve_to(-w * 0.5, top * 1.3, w * 0.5, top * 1.3, w + 4, -2)
        src(ctx, HAIR_LN)
        ctx.set_line_width(6.5)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.stroke()
        # lower lid
        ctx.move_to(-w * 0.7, bot * 0.9)
        ctx.curve_to(-w * 0.3, bot * 1.25, w * 0.3, bot * 1.25, w * 0.7, bot * 0.9)
        ctx.set_source_rgba(*SKIN_LN[:3], 0.6)
        ctx.set_line_width(3)
        ctx.stroke()
    else:
        ctx.new_path()
        ctx.move_to(-w, 2)
        ctx.curve_to(-w * 0.4, 13, w * 0.4, 13, w, 0)
        src(ctx, HAIR_LN)
        ctx.set_line_width(6)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.stroke()
    ctx.restore()


def brow(ctx, sx, raise_, sad, angry):
    bx, by = sx * 46, -44 - raise_ * 16
    inner_dy = -sad * 14 + angry * 14
    outer_dy = sad * 6 - angry * 4
    ctx.save()
    ctx.translate(bx, by)
    ix, ox = -sx * 34, sx * 34
    ctx.new_path()
    ctx.move_to(ix, inner_dy + 4)
    ctx.curve_to(ix * 0.3, inner_dy * 0.6 - 9, ox * 0.4, outer_dy * 0.5 - 10, ox, outer_dy + 2)
    ctx.curve_to(ox * 0.4, outer_dy * 0.5 - 1, ix * 0.3, inner_dy * 0.6 + 5, ix, inner_dy + 12)
    ctx.close_path()
    src(ctx, HAIR)
    ctx.fill()
    ctx.restore()


def mouth(ctx, shape, open_):
    my = 82
    ctx.save()
    ctx.translate(0, my)
    curve = {'smile': 10, 'bigsmile': 14, 'frown': -9, 'flat': 0, 'smirk': 4, 'o': 0, 'sleep': 3, 'grit': -2}.get(shape, 0)
    wid = {'smile': 30, 'bigsmile': 38, 'frown': 24, 'flat': 24, 'smirk': 26, 'o': 14, 'sleep': 12, 'grit': 30}.get(shape, 24)
    op = max(open_, 0.55 if shape in ('o', 'bigsmile') else 0)
    if shape == 'grit':
        rrect(ctx, -wid, -9, 2 * wid, 18, 8)
        src(ctx, TEETH); ctx.fill_preserve()
        src(ctx, SKIN_LN); ctx.set_line_width(4); ctx.stroke()
        for x in (-12, 0, 12):
            ctx.move_to(x, -9); ctx.line_to(x, 9)
        ctx.set_source_rgba(*SKIN_LN[:3], 0.5); ctx.set_line_width(2); ctx.stroke()
        ctx.restore()
        return
    if op > 0.08:
        hgt = 6 + op * 30
        lw = wid * (0.85 + 0.15 * op) if shape != 'o' else wid
        ctx.new_path()
        ctx.move_to(-lw, -curve * 0.6)
        ctx.curve_to(-lw * 0.5, -4 - curve * 0.2, lw * 0.5, -4 - curve * 0.2, lw, -curve * 0.6 - (6 if shape == 'smirk' else 0))
        ctx.curve_to(lw * 0.6, hgt + curve * 0.4, -lw * 0.6, hgt + curve * 0.4, -lw, -curve * 0.6)
        ctx.close_path()
        src(ctx, MOUTH_IN)
        ctx.fill_preserve()
        ctx.save()
        ctx.clip()
        rrect(ctx, -lw, -12, 2 * lw, 9 + op * 3, 4)
        src(ctx, TEETH)
        ctx.fill()
        ctx.arc(0, hgt + 6, lw * 0.6, 0, 2 * math.pi)
        src(ctx, TONGUE)
        ctx.fill()
        ctx.restore()
        ctx.new_path()
        ctx.move_to(-lw, -curve * 0.6)
        ctx.curve_to(-lw * 0.6, hgt + curve * 0.4, lw * 0.6, hgt + curve * 0.4, lw, -curve * 0.6)
        src(ctx, SKIN_LN)
        ctx.set_line_width(3.5)
        ctx.stroke()
    else:
        ctx.new_path()
        ctx.move_to(-wid, -curve)
        ctx.curve_to(-wid * 0.4, curve * 0.9, wid * 0.4, curve * 0.9, wid, -curve - (8 if shape == 'smirk' else 0))
        src(ctx, SKIN_LN)
        ctx.set_line_width(5)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.stroke()
        # lower lip hint
        ctx.move_to(-10, 12 + curve * 0.3)
        ctx.curve_to(-4, 15 + curve * 0.3, 4, 15 + curve * 0.3, 10, 12 + curve * 0.3)
        ctx.set_source_rgba(*SKIN_SH[:3], 0.7)
        ctx.set_line_width(3)
        ctx.stroke()
    ctx.restore()


def hair_back(ctx):
    ctx.new_path()
    ctx.move_to(-124, 10)
    ctx.curve_to(-140, -90, -90, -168, -10, -170)
    ctx.curve_to(80, -172, 140, -110, 126, 6)
    ctx.curve_to(118, -40, 110, -60, 100, -70)
    ctx.line_to(-100, -70)
    ctx.curve_to(-112, -50, -120, -20, -124, 10)
    ctx.close_path()
    src(ctx, HAIR)
    ctx.fill()


def hair_front(ctx, t):
    sway = math.sin(t * 1.7) * 2
    ctx.new_path()
    ctx.move_to(-122, -12)
    ctx.curve_to(-126, -110, -70, -160, 0, -158)
    ctx.curve_to(70, -160, 126, -112, 122, -16)
    ctx.curve_to(112, -58, 96, -78, 70, -84)
    ctx.curve_to(58, -64, 36, -52, 8 + sway, -50)            # fringe swoop
    ctx.curve_to(24, -66, 26, -78, 20, -86)
    ctx.curve_to(-6, -62, -40, -56, -66 + sway, -60)
    ctx.curve_to(-52, -72, -48, -82, -50, -90)
    ctx.curve_to(-80, -80, -108, -56, -122, -12)
    ctx.close_path()
    g = cairo.LinearGradient(-60, -160, 60, -40)
    g.add_color_stop_rgba(0, *HAIR_HI)
    g.add_color_stop_rgba(0.5, *HAIR)
    g.add_color_stop_rgba(1, *HAIR)
    ctx.set_source(g)
    ctx.fill_preserve()
    src(ctx, HAIR_LN)
    ctx.set_line_width(3)
    ctx.stroke()
    # strands / highlights
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    for (x0, y0, x1, y1, x2, y2) in ((-70, -140, -40, -120, -20, -96), (-10, -150, 20, -128, 30, -100),
                                     (40, -146, 70, -124, 86, -96), (-100, -110, -96, -90, -90, -70)):
        ctx.move_to(x0, y0)
        ctx.curve_to(x1, y1, x1, y1, x2, y2)
        ctx.set_source_rgba(*HAIR_HI[:3], 0.9)
        ctx.set_line_width(5)
        ctx.stroke()
    # messy spikes on top
    for (x, y, dx, dy) in ((-46, -150, -26, -34), (8, -158, 10, -40), (58, -146, 30, -30)):
        ctx.move_to(x - 18, y + 12)
        ctx.curve_to(x - 8, y - 4, x + dx * 0.6, y + dy * 0.6, x + dx, y + dy)
        ctx.curve_to(x + 6, y - 6, x + 14, y, x + 18, y + 10)
        ctx.close_path()
        src(ctx, HAIR)
        ctx.fill()


def head(ctx, cx, cy, s=1.0, t=0.0, tilt=0.0, **e):
    """e: eyes(0-1), look(x,y), raise, sad, angry, mouth, talk(0-1), bags, squint, sweat, vein, tear, blush, glow, stubble"""
    eyes = e.get('eyes', 1.0)
    look = e.get('look', (0, 0))
    ctx.save()
    ctx.translate(cx, cy)
    ctx.rotate(math.radians(tilt))
    ctx.scale(s, s)
    # neck
    ctx.new_path()
    ctx.move_to(-38, 100); ctx.line_to(-42, 190); ctx.line_to(42, 190); ctx.line_to(38, 100); ctx.close_path()
    src(ctx, SKIN_SH); ctx.fill()
    hair_back(ctx)
    # ears
    for sx in (-1, 1):
        ctx.save()
        ctx.translate(sx * 114, 14)
        ctx.scale(0.75, 1)
        ctx.arc(0, 0, 28, 0, 2 * math.pi)
        ctx.restore()
        src(ctx, SKIN); ctx.fill_preserve()
        src(ctx, SKIN_LN); ctx.set_line_width(3.5); ctx.stroke()
        ctx.save(); ctx.translate(sx * 116, 16); ctx.scale(0.4, 0.6)
        ctx.arc(0, 0, 22, 0, 2 * math.pi); ctx.restore()
        src(ctx, SKIN_SH); ctx.fill()
    # face base
    face_path(ctx)
    g = cairo.LinearGradient(-120, -130, 100, 140)
    g.add_color_stop_rgba(0, *SKIN_HI)
    g.add_color_stop_rgba(0.45, *SKIN)
    g.add_color_stop_rgba(1, *SKIN_SH)
    ctx.set_source(g)
    ctx.fill_preserve()
    src(ctx, SKIN_LN)
    ctx.set_line_width(4)
    ctx.stroke()
    # stubble
    st = e.get('stubble', 0.55)
    if st > 0:
        ctx.save()
        face_path(ctx)
        ctx.clip()
        ctx.new_path()
        ctx.move_to(-110, 40)
        ctx.curve_to(-80, 70, -50, 60, -30, 66)
        ctx.curve_to(-10, 58, 10, 58, 30, 66)
        ctx.curve_to(50, 60, 80, 70, 110, 40)
        ctx.line_to(110, 160); ctx.line_to(-110, 160); ctx.close_path()
        ctx.set_source_rgba(0.18, 0.12, 0.1, 0.22 * st)
        ctx.fill()
        ctx.restore()
    # side shadow (light from top-left)
    shade_inside(ctx, face_path, (0.38, 0.2, 0.12, 0.55), 26, 10)
    # hair shadow on forehead
    ctx.save()
    face_path(ctx); ctx.clip()
    ctx.new_path(); ctx.move_to(-120, -60); ctx.curve_to(-60, -40, 40, -30, 120, -64); ctx.line_to(120, -140); ctx.line_to(-120, -140); ctx.close_path()
    ctx.set_source_rgba(0.3, 0.16, 0.1, 0.35); ctx.fill()
    ctx.restore()
    # phone glow from below
    glow = e.get('glow', 0)
    if glow > 0:
        ctx.save()
        face_path(ctx); ctx.clip()
        gg = cairo.LinearGradient(0, 160, 0, -140)
        gg.add_color_stop_rgba(0, 0.55, 0.78, 1.0, 0.26 * glow)
        gg.add_color_stop_rgba(1, 0.55, 0.78, 1.0, 0.0)
        ctx.rectangle(-150, -150, 300, 300)
        ctx.set_source(gg); ctx.fill()
        ctx.restore()
    if e.get('blush', 0) > 0:
        for sx in (-1, 1):
            ctx.save(); ctx.translate(sx * 70, 50); ctx.scale(1.7, 1)
            ctx.arc(0, 0, 14, 0, 2 * math.pi); ctx.restore()
            ctx.set_source_rgba(0.85, 0.35, 0.35, 0.28 * e['blush']); ctx.fill()
    # nose
    ctx.new_path()
    ctx.move_to(6, 18)
    ctx.curve_to(16, 40, 12, 52, -2, 52)
    src(ctx, SKIN_LN); ctx.set_line_width(3.5); ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.stroke()
    ctx.save(); ctx.translate(-4, 54); ctx.scale(1.6, 0.6); ctx.arc(0, 0, 10, 0, 2 * math.pi); ctx.restore()
    ctx.set_source_rgba(0.4, 0.22, 0.14, 0.3); ctx.fill()
    for sx in (-1, 1):
        eye(ctx, sx, eyes, look, e.get('bags', 0), e.get('squint', 0))
        brow(ctx, sx, e.get('raise', 0), e.get('sad', 0), e.get('angry', 0))
    mouth(ctx, e.get('mouth', 'flat'), e.get('talk', 0))
    if e.get('vein', 0) > 0:  # anger: red flush + stress lines at temple
        a = e['vein']
        ctx.save()
        face_path(ctx); ctx.clip()
        gr = cairo.LinearGradient(0, -140, 0, 0)
        gr.add_color_stop_rgba(0, 0.85, 0.15, 0.15, 0.35 * a)
        gr.add_color_stop_rgba(1, 0.85, 0.15, 0.15, 0)
        ctx.rectangle(-150, -150, 300, 160); ctx.set_source(gr); ctx.fill()
        ctx.restore()
        ctx.set_source_rgba(0.9, 0.2, 0.2, a); ctx.set_line_width(6); ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        for i in range(3):
            ang = math.radians(-150 + i * 22)
            ctx.move_to(-20 + math.cos(ang) * 150, -40 + math.sin(ang) * 150)
            ctx.line_to(-20 + math.cos(ang) * 185, -40 + math.sin(ang) * 185)
        ctx.stroke()
    hair_front(ctx, t)
    # extras
    if e.get('sweat', 0) > 0:
        a = e['sweat']
        ctx.save(); ctx.translate(98, -60 + (1 - a) * -20)
        ctx.new_path(); ctx.move_to(0, -26); ctx.curve_to(14, -4, 16, 8, 0, 12); ctx.curve_to(-16, 8, -14, -4, 0, -26); ctx.close_path()
        ctx.set_source_rgba(0.7, 0.88, 1, 0.9 * a); ctx.fill_preserve()
        ctx.set_source_rgba(0.2, 0.4, 0.6, a); ctx.set_line_width(3); ctx.stroke()
        ctx.restore()
    if e.get('tear', 0) > 0:
        a = e['tear']
        ctx.save(); ctx.translate(-50, 30 + a * 30)
        ctx.new_path(); ctx.move_to(0, -12); ctx.curve_to(9, 0, 9, 8, 0, 10); ctx.curve_to(-9, 8, -9, 0, 0, -12)
        ctx.set_source_rgba(0.7, 0.88, 1, 0.9); ctx.fill(); ctx.restore()
    ctx.restore()


def torso(ctx, cx, cy, s=1.0, t=0.0, breathe=1.0, lean=0.0, arms=None, phone_hand=None, glow=0.0):
    """Upper body (hoodie) below a head at (cx, cy). arms: ((a1,a2),(a1,a2)) outward-positive degrees."""
    br = math.sin(t * 2 * math.pi / 3.4) * 3 * breathe
    ctx.save()
    ctx.translate(cx, cy)
    ctx.scale(s, s)
    ctx.rotate(math.radians(lean))

    def body(c):
        c.new_path()
        c.move_to(-150, 560)
        c.curve_to(-160, 380, -170, 250, -120, 190 - br)
        c.curve_to(-60, 160 - br, 60, 160 - br, 120, 190 - br)
        c.curve_to(170, 250, 160, 380, 150, 560)
        c.close_path()
    body(ctx)
    g = cairo.LinearGradient(-160, 160, 160, 520)
    g.add_color_stop_rgba(0, *HOOD_HI)
    g.add_color_stop_rgba(0.5, *HOOD)
    g.add_color_stop_rgba(1, *HOOD_SH)
    ctx.set_source(g)
    ctx.fill_preserve()
    src(ctx, HOOD_LN); ctx.set_line_width(4); ctx.stroke()
    shade_inside(ctx, body, (0.1, 0.11, 0.15, 0.5), 30, 6)
    # hood collar
    ctx.new_path()
    ctx.move_to(-112, 196 - br); ctx.curve_to(-70, 270, 70, 270, 112, 196 - br)
    ctx.curve_to(70, 230, -70, 230, -112, 196 - br); ctx.close_path()
    src(ctx, HOOD_SH); ctx.fill()
    # strings
    for sx in (-1, 1):
        ctx.move_to(sx * 22, 232); ctx.curve_to(sx * 26, 280, sx * 20, 320, sx * 24, 350)
        ctx.set_source_rgba(0.92, 0.92, 0.9, 1); ctx.set_line_width(6); ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.stroke()
        rrect(ctx, sx * 24 - 5, 348, 10, 22, 4); ctx.set_source_rgba(0.7, 0.7, 0.72, 1); ctx.fill()
    # pocket
    rrect(ctx, -90, 430, 180, 90, 26)
    src(ctx, HOOD_SH); ctx.fill_preserve(); src(ctx, HOOD_LN); ctx.set_line_width(3); ctx.stroke()
    hands = []
    if arms:
        for sx, (a1, a2) in zip((-1, 1), arms):
            x0, y0 = sx * 128, 230
            x1 = x0 + math.sin(math.radians(a1 * sx)) * 160
            y1 = y0 + math.cos(math.radians(a1 * sx)) * 160
            x2 = x1 + math.sin(math.radians((a1 + a2) * sx)) * 150
            y2 = y1 + math.cos(math.radians((a1 + a2) * sx)) * 150
            ctx.set_line_cap(cairo.LINE_CAP_ROUND); ctx.set_line_join(cairo.LINE_JOIN_ROUND)
            for lw, col in ((70, HOOD_LN), (62, HOOD), (20, HOOD_HI)):
                ctx.set_line_width(lw)
                src(ctx, col)
                off = -10 if lw == 20 else 0
                ctx.move_to(x0 + off, y0); ctx.line_to(x1 + off, y1); ctx.line_to(x2 + off * 0.5, y2)
                ctx.stroke()
            hand(ctx, x2, y2, (a1 + a2) * sx)
            hands.append((x2, y2))
    if phone_hand is not None and hands:
        hx, hy = hands[phone_hand]
        phone_small(ctx, hx - 45, hy - 150, 90, 160, glow)
    ctx.restore()


def hand(ctx, x, y, ang):
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(-math.radians(ang))
    rrect(ctx, -30, -14, 60, 62, 26)
    src(ctx, SKIN); ctx.fill_preserve(); src(ctx, SKIN_LN); ctx.set_line_width(3.5); ctx.stroke()
    ctx.save(); ctx.translate(30, 10); ctx.rotate(-0.6); ctx.scale(1, 0.55)
    ctx.arc(0, 0, 18, 0, 2 * math.pi); ctx.restore()
    src(ctx, SKIN); ctx.fill_preserve(); src(ctx, SKIN_LN); ctx.set_line_width(3); ctx.stroke()
    ctx.restore()


def phone_small(ctx, x, y, w, h, glow=1.0):
    if glow > 0:
        g = cairo.RadialGradient(x + w / 2, y + h / 2, 10, x + w / 2, y + h / 2, 360)
        g.add_color_stop_rgba(0, 0.55, 0.78, 1, 0.30 * glow)
        g.add_color_stop_rgba(1, 0.55, 0.78, 1, 0)
        ctx.arc(x + w / 2, y + h / 2, 360, 0, 2 * math.pi)
        ctx.set_source(g); ctx.fill()
    rrect(ctx, x, y, w, h, 16)
    ctx.set_source_rgb(0.07, 0.07, 0.09); ctx.fill()
    rrect(ctx, x + 6, y + 8, w - 12, h - 16, 11)
    ctx.set_source_rgba(0.55 + 0.4 * glow, 0.75 + 0.2 * glow, 1, 1); ctx.fill()
