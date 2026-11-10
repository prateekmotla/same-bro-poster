"""RULES YOU DIDN'T KNOW #8: traffic cop can't snatch your keys to force pending-challan payment (engine: vshort.Short).
Fact: Telangana High Court, Justice N.V. Shravan Kumar, order 20 Jan 2026 (NewsMeter / Siasat / Telangana Today):
police cannot stop vehicles to force immediate payment of pending challans or snatch/confiscate keys to force payment;
citizens may pay voluntarily; otherwise police must follow due process (court notices). Motorists must still stop when
signalled and produce documents (MV Act s.130)."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402
import body as B  # noqa: E402

D = "/home/claude/sid/shorts/s91_keys"
CAPS = [
    "Stopped at a signal, and the traffic cop pulls the KEY out of your bike: 'Pay old challans NOW, then you get the key.'",
    "Is that allowed? A: yes, he's police. B: no. Comment!",
    "B is right. In January 2026 the Telangana High Court said it clearly: snatching keys to collect pending challans is NOT allowed.",
    "Paying is YOUR choice. Otherwise police must follow proper process, through a court notice.",
    "But yes: you must stop, show your documents, and no attitude. Talk politely.",
    "Save this, it'll help. Has this ever happened to you?",
]
HOOK = [("COP TOOK YOUR KEY", WHITE), ("ALLOWED?", RED), ("RULES YOU DIDN'T KNOW #8", GREY)]
SRC = "SRC: Telangana High Court order, 20 Jan 2026"
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
    c.save(); c.translate(x, y - 58 * s / 0.5)
    S.rrect(c, -62 * s / 0.5, -22 * s / 0.5, 124 * s / 0.5, 34 * s / 0.5, 8); c.set_source_rgb(0.95, 0.95, 0.95); c.fill()
    c.rectangle(-70 * s / 0.5, 6 * s / 0.5, 140 * s / 0.5, 10 * s / 0.5); c.set_source_rgb(0.15, 0.15, 0.2); c.fill()
    c.restore()


def scooter(c, x, y):
    """simple side-view scooter, (x, y) = ground under the seat."""
    for wx in (x - 170, x + 170):
        c.arc(wx, y - 55, 55, 0, 2 * math.pi); c.set_source_rgb(0.12, 0.12, 0.14); c.fill()
        c.arc(wx, y - 55, 24, 0, 2 * math.pi); c.set_source_rgb(0.6, 0.6, 0.62); c.fill()
    c.move_to(x - 230, y - 90); c.curve_to(x - 200, y - 230, x + 60, y - 200, x + 80, y - 110)
    c.line_to(x + 150, y - 110); c.line_to(x + 200, y - 300); c.line_to(x + 240, y - 300); c.line_to(x + 200, y - 90)
    c.close_path(); c.set_source_rgb(0.15, 0.4, 0.7); c.fill()
    S.rrect(c, x - 200, y - 250, 220, 40, 18); c.set_source_rgb(0.1, 0.1, 0.12); c.fill()
    c.move_to(x + 190, y - 330); c.line_to(x + 290, y - 330); c.set_source_rgb(0.2, 0.2, 0.22); c.set_line_width(14); c.stroke()


def keyicon(c, x, y, s=1.0, a=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.arc(0, 0, 30, 0, 2 * math.pi); c.set_source_rgba(0.95, 0.8, 0.25, a); c.fill()
    c.arc(0, 0, 11, 0, 2 * math.pi); c.set_source_rgba(0.2, 0.15, 0.05, a); c.fill()
    c.rectangle(26, -8, 70, 16); c.set_source_rgba(0.95, 0.8, 0.25, a); c.fill()
    for dx in (60, 80):
        c.rectangle(dx, 6, 10, 16); c.fill()
    c.restore()


def w_street(sid_kw, off_kw, key_in_hand=True):
    def f(c, t, lt):
        V.street(c, t, 0.0, night=False)
        scooter(c, 860, 900)
        ok = dict(mouth='flat'); ok.update(off_kw)
        officer(c, t, 1380, 380, 0.5, **ok)
        if key_in_hand:
            keyicon(c, 1250, 600 + 6 * math.sin(t * 3), 1.3)
        d = dict(pose='stand', mouth='flat', look=(0.6, 0))
        d.update(sid_kw)
        K.sid(c, t, 900, 360, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def bubble(c, x, y, txt, a=1.0):
    w = len(txt) * 28 + 70
    S.rrect(c, x - w / 2, y, w, 96, 40); c.set_source_rgba(1, 1, 1, 0.96 * a); c.fill()
    T(c, txt, x, y + 64, 42, (0.1, 0.1, 0.15), a, stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    a = k(t, st + 3.4, st + 3.7)
    if a > 0:
        bubble(c, 540, 548, "'PAY OLD CHALLANS NOW!'", a)
    K.stamp(c, t, st + 5.6, "A: ALLOWED   or   B: NOT?", 540, 1330, RED, 50, -0.04)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "IS THIS ALLOWED?", 540, 470, 72, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt) in enumerate((("A", "YES, HE'S POLICE"), ("B", "NO, NOT ALLOWED"))):
        a = k(t, st + 1.3 + i * 2.0, st + 1.6 + i * 2.0)
        y = 580 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 112, 48, WHITE, a, stroke=None)
    K.stamp(c, t, st + 4.6, "COMMENT A or B", 540, 1120, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 400, 860, 190, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: NOT ALLOWED", 540, 515, 64, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 420, GRN, 54, 0.06)
    K.rows(c, t, st, [("TELANGANA HIGH COURT", YEL, 58, 1.4), ("JAN 2026", WHITE, 50, 2.2),
                      ("NO SNATCHING KEYS", RED, 66, 5.4), ("NO FORCED PAYMENT", RED, 66, 6.6),
                      ("of pending challans", GREY, 44, 7.0)], y0=730, gap=125)


def o_process(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("PAYING ON THE SPOT?", WHITE, 62, 0.1), ("YOUR CHOICE", GRN, 96, 0.9),
                      ("OTHERWISE POLICE MUST", WHITE, 56, 2.0), ("FOLLOW DUE PROCESS", YEL, 70, 2.6),
                      ("court notice", GREY, 48, 4.0)], y0=470, gap=160)


def o_must(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("BUT YOU MUST", RED, 70, 0.1), ("STOP WHEN SIGNALLED", WHITE, 62, 0.6),
                      ("SHOW YOUR DOCUMENTS", WHITE, 62, 1.4), ("STAY POLITE", GRN, 84, 2.6)], y0=520, gap=180)


def o_end(c, t, lt):
    K.end_card(c, "SAVE THIS.", "IT'LL HELP ONE DAY.", YEL)
    st = sh.s(6)
    T(c, "HAPPENED TO YOU? COMMENT", 540, 1260, 54, YEL, k(t, st + 1.2, st + 1.5), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    cam0, cam1 = (1.55, 1150, 520), (1.7, 1150, 500)
    sh.shots = [
        (0, s(2), w_street(dict(mouth='o', eyes=1.2, sweat=1), dict(arms=((14, -10), (100, 40)), angry=0.3)),
         cam0, cam1, o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_process, 'studio'),
        (s(5), s(6), w_street(dict(mouth='smile', arms=((14, -10), (90, 20))), dict(mouth='smile'), key_in_hand=False),
         (1.55, 1150, 520), (1.6, 1150, 510), o_must, 'studio'),
        (s(6), sh.dur + 1, sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.9, 960, 510), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 4.0, 6.5] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[2][0] + 7.5], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
