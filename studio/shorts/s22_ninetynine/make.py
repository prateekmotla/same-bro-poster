import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s22_ninetynine"
CAPS = [
    "Sid sees two shirts. One is ₹1,000. The other is ₹999.",
    "His brain says: the ₹999 one is WAY cheaper. Bro, it's ₹1 less.",
    "This is the LEFT-DIGIT EFFECT. Your brain reads the first digit and moves on.",
    "₹999 feels like \"9 hundred something\". ₹1,000 feels like \"a THOUSAND\".",
    "NYU researchers showed it in 2005: the effect is strongest when the FIRST digit changes.",
    "That's why everything ends in 99. ₹499. ₹1,999. ₹99,999 phones.",
    "Rule: round UP in your head. ₹999 = ₹1,000. ₹1,999 = ₹2,000. Then decide.",
    "Send this to the friend who buys anything that ends in 99.",
]
HOOK = [("WHY EVERYTHING", WHITE), ("ENDS IN 99", RED), ("THE BRAIN TRICK", YEL)]
SRC = "Source: Thomas & Morwitz, Journal of Consumer Research, 2005"
sh = None


def street(c, t, lt, **kw):
    V.street(c, t, off=0, night=False)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 960, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def tag(c, x, y, s, price, col=(0.98, 0.95, 0.85), a=1.0, txtcol=(0.1, 0.1, 0.12)):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.push_group()
    c.move_to(-170, -90); c.line_to(130, -90); c.line_to(190, 0); c.line_to(130, 90); c.line_to(-170, 90); c.close_path()
    c.set_source_rgb(*col); c.fill()
    c.arc(130, 0, 14, 0, 6.3); c.set_source_rgb(0.3, 0.3, 0.3); c.fill()
    T(c, price, -20, 24, 74 if len(price) < 7 else 58, txtcol, stroke=None)
    c.pop_group_to_source(); c.paint_with_alpha(a)
    c.restore()


def o_two(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 470, a=0.8)
    tag(c, 300, 1100, 1.0, "₹1,000", a=k(t, st + 0.8, st + 1.1))
    tag(c, 780, 1100, 1.0, "₹999", a=k(t, st + 1.8, st + 2.1))


def o_brain(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 470, a=0.8)
    tag(c, 300, 1050, 0.8, "₹1,000", a=0.5)
    sc = 1 + 0.3 * U.eob(k(t, st + 0.4, st + 0.9))
    tag(c, 780, 1050, 0.8 * sc, "₹999", col=(0.2, 0.8, 0.45), txtcol=(1, 1, 1))
    if t > st + 2.6:
        T(c, "DIFFERENCE: ₹1", 540, 1270, 64, RED, k(t, st + 2.6, st + 2.9), stroke=None)


def o_left(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "LEFT-DIGIT", 540, 420, 130, YEL, k(t, st + 0.5, st + 0.8), lw=14)
    T(c, "EFFECT", 540, 560, 130, YEL, k(t, st + 0.8, st + 1.1), lw=14)
    if t > st + 2.0:
        a = k(t, st + 2.0, st + 2.3)
        T(c, "9", 400, 860, 220, RED, a, lw=16)
        T(c, "99", 620, 860, 220, (0.35, 0.36, 0.42), a, lw=16)
        T(c, "brain reads THIS", 400, 1010, 46, WHITE, k(t, st + 2.8, st + 3.1), lw=6)
        T(c, "skips this", 660, 1080, 40, GREY, k(t, st + 3.4, st + 3.7), lw=6)


def o_feel(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "₹999", 540, 450, 130, GRN, k(t, st + 0.4, st + 0.7), lw=14)
    T(c, "\"9 hundred something\"", 540, 560, 58, WHITE, k(t, st + 1.0, st + 1.3), lw=8)
    T(c, "₹1,000", 540, 800, 130, RED, k(t, st + 2.4, st + 2.7), lw=14)
    T(c, "\"a THOUSAND\"", 540, 910, 66, WHITE, k(t, st + 3.0, st + 3.3), lw=8)


def o_nyu(c, t, lt):
    st = sh.s(5)
    K.panel(c, 870, 470)
    K.rows(c, t, st, [("2005 · NYU STUDY", GREY, 44, 0.5), ("Journal of Consumer Research", WHITE, 40, 1.0),
                      ("strongest when the", WHITE, 46, 2.6), ("FIRST DIGIT CHANGES", YEL, 56, 3.1)], y0=960, gap=100)


def o_all(c, t, lt):
    st = sh.s(6)
    U.dim(c, 0.86)
    for i, p in enumerate(["₹99", "₹499", "₹1,999", "₹99,999"]):
        tag(c, 520 + (i % 2) * 40 - 20, 430 + i * 230, 1.0, p, a=k(t, st + 0.6 + i * 0.6, st + 0.9 + i * 0.6))


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "ROUND IT UP", 540, 950, 62, YEL, stroke=None)
    K.rows(c, t, st, [("₹999  =  ₹1,000", WHITE, 56, 1.4), ("₹1,999  =  ₹2,000", WHITE, 56, 2.6),
                      ("THEN decide", GRN, 56, 3.8)], y0=1080, gap=105)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO FALLS FOR EVERY 99", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    stw = lambda **kw: (lambda c, t, lt: street(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), stw(mouth='flat', look=(0.4, 0)), (1.9, 960, 480), (2.1, 960, 450), o_two, 'day'),
        (s(2), s(3), stw(mouth='bigsmile', eyes=1.2), (1.9, 960, 480), (2.0, 960, 460), o_brain, 'day'),
        (s(3), s(4), sw(), (1.78, 960, 540), (1.85, 960, 520), o_left, 'studio'),
        (s(4), s(5), sw(), (1.78, 960, 540), (1.85, 960, 520), o_feel, 'studio'),
        (s(5), s(6), sw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 960, 500), (2.0, 960, 470), o_nyu, 'studio'),
        (s(6), s(7), sw(), (1.78, 960, 540), (1.85, 960, 520), o_all, 'studio'),
        (s(7), s(8), stw(mouth='smirk', squint=0.4), (1.9, 960, 500), (2.0, 960, 480), o_rule, 'morning'),
        (s(8), sh.dur + 1, stw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 960, 500), (2.1, 960, 470), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1.2, 3.5] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
