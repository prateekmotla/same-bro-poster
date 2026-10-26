"""Full-body Sid / Live Bhai: legs, poses (stand, walk, sit, lie) on top of sid2 head+torso.
Local units: head centre (0,0), torso to y=560, hips ~y=540, feet ~y=1010.
"""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/v2")
sys.path.insert(0, "/home/claude/sid/v3")
import sid2 as S  # noqa: E402
import chars as CH  # noqa: E402

JEANS, JEANS_SH, JEANS_LN = (0.20, 0.26, 0.40), (0.14, 0.18, 0.29), (0.07, 0.08, 0.13)
BLACKP = (0.12, 0.12, 0.14), (0.07, 0.07, 0.09), (0.02, 0.02, 0.03)
SHOE, SHOE_SOLE = (0.95, 0.95, 0.96), (0.75, 0.76, 0.8)


def _seg(c, pts, lw, col):
    c.set_line_cap(cairo.LINE_CAP_ROUND)
    c.set_line_join(cairo.LINE_JOIN_ROUND)
    c.set_line_width(lw)
    c.set_source_rgb(*col)
    c.move_to(*pts[0])
    for p in pts[1:]:
        c.line_to(*p)
    c.stroke()


def shoe(c, x, y, ang=0.0, flip=1, s=1.0):
    c.save()
    c.translate(x, y)
    c.rotate(ang)
    c.scale(flip * s, s)
    S.rrect(c, -38, -26, 96, 46, 22)
    c.set_source_rgb(*SHOE); c.fill_preserve()
    c.set_source_rgb(0.2, 0.2, 0.22); c.set_line_width(4); c.stroke()
    S.rrect(c, -40, 10, 100, 14, 7)
    c.set_source_rgb(*SHOE_SOLE); c.fill()
    c.move_to(-5, -20); c.line_to(25, -8)
    c.set_source_rgb(0.85, 0.2, 0.25); c.set_line_width(6); c.stroke()
    c.restore()


def leg(c, hip, knee, ankle, pal=None, front=True):
    col, sh, ln = pal or (JEANS, JEANS_SH, JEANS_LN)
    _seg(c, [hip, knee, ankle], 92, ln)
    _seg(c, [hip, knee, ankle], 82, col if front else sh)
    hx, hy = hip
    kx, ky = knee
    _seg(c, [(hx + 18, hy + 10), (kx + 18, ky)], 14, sh)  # crease shade


def legs_stand(c, t, sway=0.0, pal=None):
    for sx in (-1, 1):
        hip = (sx * 62, 540)
        knee = (sx * 66 + sway * 6, 770)
        ank = (sx * 70, 975)
        leg(c, hip, knee, ank, pal)
        shoe(c, sx * 78, 1000, 0, sx)


def legs_walk(c, ph, pal=None):
    """ph: walk phase in cycles. Front/3-4 view walk toward camera: alternating knee lift + stride."""
    order = sorted((-1, 1), key=lambda sx: math.sin(2 * math.pi * ph + (0 if sx < 0 else math.pi)))
    for sx in order:
        p = 2 * math.pi * ph + (0 if sx < 0 else math.pi)
        lift = max(0.0, math.sin(p))
        fwd = math.cos(p)
        hip = (sx * 60, 540)
        knee = (sx * 66 + fwd * 18, 770 - lift * 70)
        ank = (sx * 70 + fwd * 30, 975 - lift * 110 + max(0, -fwd) * 10)
        leg(c, hip, knee, ank, pal, front=lift < 0.3)
        shoe(c, ank[0] + sx * 8, ank[1] + 25, -0.25 * lift * sx, sx, 1.0 + 0.08 * fwd)


def legs_sit(c, pal=None, spread=1.0):
    """Sitting facing camera on a seat at y~600: thighs foreshortened toward viewer, shins down."""
    for sx in (-1, 1):
        hip = (sx * 62, 560)
        knee = (sx * (95 * spread), 650)
        ank = (sx * (100 * spread), 900)
        leg(c, hip, knee, ank, pal)
        # knee cap highlight
        c.arc(knee[0], knee[1] - 4, 44, 0, 2 * math.pi)
        c.set_source_rgb(*(pal or (JEANS,))[0]); c.fill()
        shoe(c, ank[0] + sx * 10, 925, 0, sx)


def legs_cross(c, pal=None):
    """Sitting cross-legged on bed/floor."""
    col, sh, ln = pal or (JEANS, JEANS_SH, JEANS_LN)
    for sx in (-1, 1):
        _seg(c, [(sx * 60, 560), (sx * 230, 640), (-sx * 40, 700)], 96, ln)
        _seg(c, [(sx * 60, 560), (sx * 230, 640), (-sx * 40, 700)], 86, col if sx < 0 else sh)


def figure(c, x, y, s, t, who='sid', pose='stand', ph=0.0, arms=((14, -10), (14, -10)), phone=None, glow=0.0,
           lean=0.0, tilt=0.0, bob=True, **e):
    """Draw full figure. (x,y) = HEAD centre in canvas units, s = scale (1.0 => ~1200px tall)."""
    pal = BLACKP if who == 'bhai' else None
    yb = 0.0
    if pose == 'walk' and bob:
        yb = -abs(math.sin(2 * math.pi * ph)) * 14
    c.save()
    c.translate(x, y + yb * s)
    c.scale(s, s)
    c.rotate(math.radians(lean))
    if pose == 'stand':
        legs_stand(c, t, math.sin(t * 0.8), pal)
    elif pose == 'walk':
        legs_walk(c, ph, pal)
    elif pose == 'sit':
        legs_sit(c, pal)
    elif pose == 'cross':
        legs_cross(c, pal)
    c.restore()
    if pose == 'walk' and arms == ((14, -10), (14, -10)):
        sw = math.sin(2 * math.pi * ph) * 14
        arms = ((10 + sw, -12), (10 - sw, -12))
    body = CH.bhai_body if who == 'bhai' else CH.sid_body
    head = CH.bhai_head if who == 'bhai' else CH.sid_head
    if who == 'friend':
        body, head = friend_body, friend_head
    body(c, x, y + yb * s, s, t, arms=arms, phone_hand=phone, glow=glow, lean=lean)
    if who == 'sid':
        e.setdefault('eyes', 1.0)
        d = (t * 1.0) % 3.4
        if d < 0.13:
            e['eyes'] = e['eyes'] * abs(d - 0.065) / 0.065
    if 'raise_' in e:
        e['raise'] = e.pop('raise_')
    head(c, x, y + yb * s + math.sin(t * 1.8) * -2 * s, s, t, tilt=tilt, **e)


def lying(c, x, y, s, t, **e):
    """Sid lying on his back on a bed, head at (x,y), body extending to the right, phone above face."""
    c.save()
    c.translate(x, y)
    c.rotate(-math.pi / 2)
    c.translate(-x, -y)
    figure(c, x, y, s, t, pose='stand', arms=((150, 40), (14, -10)), **e)
    c.restore()


_FRIEND = dict(HAIR=S.C('3A2418'), HAIR_HI=S.C('6E4A33'), HOOD=S.C('8C2F39'), HOOD_SH=S.C('64202A'),
               HOOD_HI=S.C('B04652'), HOOD_LN=S.C('2E0E13'))


def friend_body(c, x, y, s, t, **kw):
    CH._swap(_FRIEND)
    S.torso(c, x, y, s, t, **kw)
    CH._swap(CH._SID)


def friend_head(c, x, y, s, t, **e):
    CH._swap(_FRIEND)
    e.setdefault('stubble', 0.6)
    S.head(c, x, y, s, t, **e)
    CH._swap(CH._SID)
