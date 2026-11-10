"""RULES YOU DIDN'T KNOW #9: DigiLocker / mParivahan licence & RC are valid like the originals (engine: vshort.Short).
Fact: MoRTH advisory to states, Aug 2018 (PTI via The Quint 9-10 Aug 2018): DL, RC etc. in DigiLocker or mParivahan
'are deemed to be legally recognised at par with the original documents' under the IT Act 2000; 'no requirement of
physical seizure' — impounding is recorded electronically (eChallan). Only the app/DigiLocker record counts, not a
photo in the gallery."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402
import body as B  # noqa: E402

D = "/home/claude/sid/shorts/s95_digi"
CAPS = [
    "Checking on the road, and you left your licence at home. Police: 'Show the ORIGINAL, or challan.'",
    "You have DigiLocker on your phone. Will that work? A: no, original needed. B: yes, it works. Comment!",
    "B is right. In 2018 the Transport Ministry said it clearly: a licence and RC in DigiLocker or mParivahan are valid, same as the original.",
    "And your original doesn't even need to be seized. It's all recorded electronically.",
    "Just remember: not a photo from your gallery. Show the verified document in the app.",
    "Put your licence and RC in DigiLocker right now. Save this.",
]
HOOK = [("FORGOT YOUR LICENCE?", WHITE), ("PHONE = VALID?", YEL), ("RULES YOU DIDN'T KNOW #9", GREY)]
SRC = "SRC: MoRTH advisory, Aug 2018 (IT Act 2000)"
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


def doc_screen(verified=True):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.96, 0.97, 1.0); c.fill()
        c.rectangle(0, 0, w, 120); c.set_source_rgb(0.12, 0.3, 0.62); c.fill()
        T(c, "DIGILOCKER" if verified else "GALLERY", w / 2, 82, 38, WHITE, stroke=None)
        S.rrect(c, 30, 160, w - 60, 270, 20); c.set_source_rgb(1, 1, 1); c.fill_preserve()
        c.set_source_rgb(0.75, 0.78, 0.85); c.set_line_width(3); c.stroke()
        T(c, "DRIVING LICENCE", w / 2, 210, 30, (0.15, 0.2, 0.4), stroke=None)
        c.rectangle(60, 240, 110, 140); c.set_source_rgb(0.8, 0.82, 0.88); c.fill()
        for j in range(4):
            c.rectangle(200, 250 + j * 36, w - 260 - j * 30, 16); c.set_source_rgb(0.82, 0.84, 0.9); c.fill()
        if verified:
            S.rrect(c, 30, 460, w - 60, 80, 40); c.set_source_rgb(0.1, 0.6, 0.3); c.fill()
            T(c, "ISSUED / VERIFIED", w / 2, 512, 32, WHITE, stroke=None)
            S.rrect(c, 30, 560, w - 60, 80, 40); c.set_source_rgb(0.85, 0.88, 0.95); c.fill()
            T(c, "VEHICLE RC", w / 2, 612, 32, (0.15, 0.2, 0.4), stroke=None)
        else:
            S.rrect(c, 30, 460, w - 60, 80, 40); c.set_source_rgb(0.85, 0.2, 0.18); c.fill()
            T(c, "JUST A PHOTO", w / 2, 512, 32, WHITE, stroke=None)
    return f


def w_road(sid_kw, off_kw):
    def f(c, t, lt):
        V.street(c, t, 0.0, night=False)
        ok = dict(mouth='flat'); ok.update(off_kw)
        officer(c, t, 1380, 380, 0.5, **ok)
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
    a = k(t, st + 2.6, st + 2.9)
    if a > 0:
        bubble(c, 540, 548, "'ORIGINAL, OR CHALLAN!'", a)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "DIGILOCKER ON PHONE?", 540, 470, 66, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "NO, ORIGINAL NEEDED", 2.6), ("B", "YES, IT'S VALID", 5.0))):
        a = k(t, st + d, st + d + 0.3)
        y = 580 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 112, 46, WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.8, "COMMENT A or B", 540, 1120, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 400, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: YES, IT'S VALID", 540, 495, 62, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 410, GRN, 54, 0.06)
    K.rows(c, t, st, [("TRANSPORT MINISTRY, 2018", YEL, 54, 1.4), ("DIGILOCKER / mPARIVAHAN", WHITE, 56, 4.6),
                      ("LICENCE + RC", WHITE, 64, 5.6), ("= SAME AS ORIGINAL", GRN, 72, 7.2)], y0=700, gap=135)


def o_seize(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("SEIZE YOUR ORIGINAL?", WHITE, 64, 0.1), ("NOT NEEDED", GRN, 96, 1.0),
                      ("RECORDED", WHITE, 62, 2.4), ("ELECTRONICALLY", YEL, 76, 2.8)], y0=520, gap=180)


def o_photo(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    U.phone_frame(c, 120, 520, 400, 620, doc_screen(False), t - st, tilt=-2)
    U.phone_frame(c, 560, 520, 400, 620, doc_screen(True), t - st, tilt=2)
    K.stamp(c, t, st + 0.9, "NOT THIS", 320, 470, RED, 48, -0.05)
    K.stamp(c, t, st + 2.4, "SHOW THIS", 760, 470, GRN, 48, 0.05)


def o_end(c, t, lt):
    K.end_card(c, "ADD LICENCE + RC TO", "DIGILOCKER. NOW.", YEL)
    st = sh.s(6)
    T(c, "A or B? COMMENT", 540, 1260, 64, YEL, k(t, st + 1.2, st + 1.5), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    cam0, cam1 = (1.55, 1150, 520), (1.7, 1150, 500)
    ph = dict(phone=1, arms=((14, -10), (60, 120)))
    sh.shots = [
        (0, s(2), w_road(dict(mouth='o', eyes=1.2, sweat=1), dict(arms=((14, -10), (100, 40)), angry=0.3)),
         cam0, cam1, o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3, **ph), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), w_road(dict(mouth='smile', **ph), dict(mouth='smile')), (1.55, 1150, 520), (1.6, 1150, 510),
         o_seize, 'studio'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_photo, 'studio'),
        (s(6), sh.dur + 1, sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.9, 960, 510), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 3.5] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[2][0] + 6.0, L[4][0] + 3.0], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
