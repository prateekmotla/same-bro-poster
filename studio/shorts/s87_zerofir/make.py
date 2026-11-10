"""RULES YOU DIDN'T KNOW #7: Zero FIR — any police station must register your FIR (engine: vshort.Short).
Fact: BNSS 2023 Section 173(1): information of a cognizable offence is recorded 'irrespective of the area where the
offence is committed' (Zero FIR, then transferred); 173(2): copy given to the informant free of cost; 173(4): if the
officer refuses, send the substance in writing to the Superintendent of Police."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402
import body as B  # noqa: E402

D = "/home/claude/sid/shorts/s87_zerofir"
CAPS = [
    "Phone STOLEN. You go to the police station, and hear: 'Not our area. Go there.'",
    "What do you do? A: go to the other station. B: get the FIR written HERE. Comment!",
    "B is right. It's called ZERO FIR. The new law, BNSS Section 173, says: crime anywhere, the FIR must be written.",
    "Police write the FIR here, then TRANSFER it to the right station. You don't have to run around.",
    "Still refused? Send a written complaint to the SP. And don't forget your FREE copy of the FIR.",
    "Save this, it'll help one day. Has this ever happened to you?",
]
HOOK = [("'NOT OUR AREA'", WHITE), ("GO OR STAY?", RED), ("RULES YOU DIDN'T KNOW #7", GREY)]
SRC = "SRC: BNSS 2023, Section 173 (Zero FIR)"
sh = None
KHAKI = dict(HAIR=B.S.C('15110F'), HAIR_HI=B.S.C('3A302A'), HOOD=B.S.C('B49A5E'), HOOD_SH=B.S.C('8C7644'),
             HOOD_HI=B.S.C('CDB57A'), HOOD_LN=B.S.C('4A3D20'))


def officer(c, t, x, y, s, **e):
    def _b(c_, x_, y_, s_, t_, **kw):
        B.CH._swap(KHAKI); B.S.torso(c_, x_, y_, s_, t_, **kw); B.CH._swap(B.CH._SID)

    def _h(c_, x_, y_, s_, t_, **kw):
        B.CH._swap(KHAKI); kw.setdefault('stubble', 0.8); B.S.head(c_, x_, y_, s_, t_, **kw); B.CH._swap(B.CH._SID)
    fb, fh = B.friend_body, B.friend_head
    B.friend_body, B.friend_head = _b, _h
    try:
        B.figure(c, x, y, s, t, who='friend', **e)
    finally:
        B.friend_body, B.friend_head = fb, fh
    # cap
    c.save(); c.translate(x, y - 58 * s / 0.5)
    S.rrect(c, -62 * s / 0.5, -22 * s / 0.5, 124 * s / 0.5, 34 * s / 0.5, 8); c.set_source_rgb(0.62, 0.52, 0.3); c.fill()
    c.rectangle(-70 * s / 0.5, 6 * s / 0.5, 140 * s / 0.5, 10 * s / 0.5); c.set_source_rgb(0.25, 0.2, 0.12); c.fill()
    c.restore()


def station(c, t):
    g = cairo.LinearGradient(0, 0, 0, 900)
    g.add_color_stop_rgb(0, 0.78, 0.8, 0.76); g.add_color_stop_rgb(1, 0.62, 0.64, 0.6)
    c.rectangle(0, 0, 1920, 1080); c.set_source(g); c.fill()
    c.rectangle(0, 620, 1920, 40); c.set_source_rgb(0.35, 0.42, 0.5); c.fill()
    c.rectangle(0, 860, 1920, 220); c.set_source_rgb(0.4, 0.36, 0.32); c.fill()
    S.rrect(c, 980, 30, 520, 100, 12); c.set_source_rgb(0.12, 0.22, 0.45); c.fill()
    T(c, "POLICE STATION", 1240, 100, 52, WHITE, stroke=None)
    # notice board
    c.rectangle(760, 300, 200, 240); c.set_source_rgb(0.55, 0.4, 0.25); c.fill()
    for j in range(3):
        c.rectangle(780 + j * 60, 320 + (j % 2) * 30, 50, 70); c.set_source_rgb(0.95, 0.95, 0.9); c.fill()
    # clock
    c.arc(1600, 300, 50, 0, 2 * math.pi); c.set_source_rgb(0.97, 0.97, 0.95); c.fill()
    c.move_to(1600, 300); c.line_to(1600 + 30 * math.cos(t), 300 + 30 * math.sin(t)); c.set_source_rgb(0.1, 0.1, 0.1)
    c.set_line_width(5); c.stroke()


def desk(c):
    c.rectangle(1180, 640, 420, 240); c.set_source_rgb(0.42, 0.28, 0.17); c.fill()
    c.rectangle(1160, 620, 460, 30); c.set_source_rgb(0.5, 0.34, 0.2); c.fill()
    c.rectangle(1260, 596, 160, 24); c.set_source_rgb(0.9, 0.88, 0.8); c.fill()   # register


def w_station(sid_kw, off_kw):
    def f(c, t, lt):
        station(c, t)
        ok = dict(mouth='flat'); ok.update(off_kw)
        officer(c, t, 1390, 380, 0.5, **ok)
        desk(c)
        d = dict(pose='stand', mouth='flat', look=(0.6, 0))
        d.update(sid_kw)
        K.sid(c, t, 960, 360, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def bubble(c, x, y, txt, a=1.0):
    w = len(txt) * 30 + 70
    S.rrect(c, x - w / 2, y, w, 96, 40); c.set_source_rgba(1, 1, 1, 0.96 * a); c.fill()
    T(c, txt, x, y + 64, 44, (0.1, 0.1, 0.15), a, stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    a = k(t, st + 2.6, st + 2.9)
    if a > 0:
        bubble(c, 640, 548, "'NOT OUR AREA. GO THERE.'", a)
    K.stamp(c, t, st + 3.6, "A: GO   or   B: STAY?", 540, 1330, RED, 50, -0.04)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "WHAT DO YOU DO?", 540, 470, 72, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt) in enumerate((("A", "GO TO 'THAT' STATION"), ("B", "FIR RIGHT HERE"))):
        a = k(t, st + 1.0 + i * 2.3, st + 1.3 + i * 2.3)
        y = 580 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 112, 48, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.0, "COMMENT A or B", 540, 1120, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 400, 860, 190, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: FIR RIGHT HERE", 540, 515, 62, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 420, GRN, 54, 0.06)
    K.rows(c, t, st, [("IT'S CALLED", WHITE, 50, 1.0), ("ZERO FIR", YEL, 110, 1.6), ("BNSS SECTION 173", WHITE, 56, 3.4),
                      ("CRIME ANYWHERE?", WHITE, 56, 6.4), ("FIR MUST BE WRITTEN", GRN, 60, 7.6)], y0=730, gap=125)


def o_transfer(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "HOW ZERO FIR WORKS", 540, 470, 62, YEL, stroke=None)
    boxes = [("FIR WRITTEN", "at ANY station", 0.3), ("TRANSFERRED", "to the right station", 1.9), ("YOU", "don't run around", 3.8)]
    for i, (a1, a2, d) in enumerate(boxes):
        a = k(t, st + d, st + d + 0.3)
        y = 560 + i * 270
        S.rrect(c, 150, y, 780, 190, 34); c.set_source_rgba(0.1, 0.12, 0.2, 0.95 * a)
        c.fill_preserve(); c.set_source_rgba(*(GRN if i == 2 else YEL), a); c.set_line_width(5); c.stroke()
        T(c, a1, 540, y + 85, 60, GRN if i == 2 else WHITE, a, stroke=None)
        T(c, a2, 540, y + 150, 42, GREY, a, stroke=None, bold=False)
        if i < 2:
            T(c, "v", 540, y + 250, 64, YEL, k(t, st + d + 0.4, st + d + 0.7), stroke=None)


def o_refuse(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("STILL REFUSED?", RED, 70, 0.1), ("WRITE TO THE SP", WHITE, 76, 0.9), ("Sec 173(4)", GREY, 44, 1.5),
                      ("FREE COPY OF FIR", GRN, 76, 3.0), ("It's your right. Sec 173(2)", GREY, 44, 3.6)], y0=480, gap=150)


def o_end(c, t, lt):
    K.end_card(c, "SAVE THIS.", "IT'LL HELP ONE DAY.", YEL)
    st = sh.s(6)
    T(c, "HAPPENED TO YOU? COMMENT", 540, 1260, 54, YEL, k(t, st + 1.5, st + 1.8), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    cam0, cam1 = (1.55, 1170, 520), (1.7, 1170, 500)
    sh.shots = [
        (0, s(2), w_station(dict(mouth='o', eyes=1.2, sweat=1), dict(arms=((14, -10), (90, 0)), angry=0.3)),
         cam0, cam1, o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), w_station(dict(mouth='smile'), dict(arms=((14, -10), (14, -10)), mouth='smile')),
         (1.55, 1170, 520), (1.6, 1170, 510), o_transfer, 'studio'),
        (s(5), s(6), sw(mouth='flat', angry=0.3), (1.78, 960, 540), (1.85, 960, 520), o_refuse, 'studio'),
        (s(6), sh.dur + 1, sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.9, 960, 510), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 3.5, 5.0] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[2][0] + 8.5, L[3][0] + 4.5], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
