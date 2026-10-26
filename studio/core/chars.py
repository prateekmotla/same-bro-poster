"""Recurring characters built on sid2: Sid (hero) and 'Live Bhai' (the live-trading finfluencer archetype)."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/v2")
import sid2 as S  # noqa: E402

_SID = dict(HAIR=S.HAIR, HAIR_HI=S.HAIR_HI, HOOD=S.HOOD, HOOD_SH=S.HOOD_SH, HOOD_HI=S.HOOD_HI, HOOD_LN=S.HOOD_LN)
_BHAI = dict(HAIR=S.C('2A1A12'), HAIR_HI=S.C('6B4A30'), HOOD=S.C('1C1C22'), HOOD_SH=S.C('101014'),
             HOOD_HI=S.C('34343E'), HOOD_LN=S.C('050507'))


def _swap(pal):
    for k, v in pal.items():
        setattr(S, k, v)


def sid_head(c, x, y, s, t, **e):
    _swap(_SID)
    S.head(c, x, y, s, t, **e)


def sid_body(c, x, y, s, t, **kw):
    _swap(_SID)
    S.torso(c, x, y, s, t, **kw)


def shades(c, x, y, s, tilt=0.0, shine=0.0):
    c.save()
    c.translate(x, y)
    c.rotate(math.radians(tilt))
    c.scale(s, s)
    for sx in (-1, 1):
        S.rrect(c, sx * 46 - 40, -18, 80, 46, 18)
        g = cairo.LinearGradient(0, -18, 0, 28)
        g.add_color_stop_rgb(0, 0.08, 0.08, 0.1)
        g.add_color_stop_rgb(1, 0.02, 0.02, 0.03)
        c.set_source(g)
        c.fill_preserve()
        c.set_source_rgb(0.75, 0.6, 0.2)
        c.set_line_width(4)
        c.stroke()
        c.move_to(sx * 46 - 24 + shine * 30, -10)
        c.line_to(sx * 46 - 6 + shine * 30, -10)
        c.line_to(sx * 46 - 22 + shine * 30, 18)
        c.close_path()
        c.set_source_rgba(1, 1, 1, 0.25)
        c.fill()
    c.move_to(-8, -4)
    c.line_to(8, -4)
    c.set_source_rgb(0.75, 0.6, 0.2)
    c.set_line_width(5)
    c.stroke()
    c.restore()


def chain(c, x, y, s):
    c.save()
    c.translate(x, y)
    c.scale(s, s)
    for i in range(14):
        a = math.pi * (0.15 + 0.7 * i / 13)
        px, py = math.cos(a) * 95, 200 + math.sin(a) * 120
        c.arc(px, py, 9, 0, 2 * math.pi)
        c.set_source_rgb(0.95, 0.75, 0.22)
        c.fill_preserve()
        c.set_source_rgb(0.55, 0.38, 0.05)
        c.set_line_width(2)
        c.stroke()
    c.restore()


def bhai_head(c, x, y, s, t, tilt=0.0, glasses=True, **e):
    if 'raise_' in e:
        e['raise'] = e.pop('raise_')
    _swap(_BHAI)
    e.setdefault('stubble', 1.0)
    S.head(c, x, y, s, t, tilt=tilt, **e)
    if glasses:
        c.save()
        c.translate(x, y)
        c.rotate(math.radians(tilt))
        shades(c, 0, 4 * s, s, 0, shine=math.sin(t * 1.5) * 0.5 + 0.5)
        c.restore()
    _swap(_SID)


def bhai_body(c, x, y, s, t, **kw):
    _swap(_BHAI)
    S.torso(c, x, y, s, t, **kw)
    chain(c, x, y, s)
    _swap(_SID)
