import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s40_decoy"
CAPS = [
    "Guess why the MEDIUM popcorn costs almost the same as the LARGE?",
    "Sid: 'Medium ₹380, Large ₹420? Arre, take the large. VALUE hai!'",
    "That medium is a DECOY. It's not there to sell. It's there to make the large look cheap.",
    "Famous test (Dan Ariely): web only $59. Print $125. Print + web, also $125.",
    "With the useless 'print' option: 84% picked the costly combo. Remove it: only 32%.",
    "Same bro? Cinema, coffee, phone plans... always 'the bigger one'?",
    "Rule: ignore the middle option. Ask: 'If only the small one existed, would I buy it?'",
    "MORAL: The middle option is bait.",
    "Send this to the friend who always says 'large hi le le'.",
]
HOOK = [("THE MEDIUM SIZE", WHITE), ("IS A TRAP", RED), ("DECOY PRICING", YEL)]
SRC = "Source: Dan Ariely, Predictably Irrational (2008), ch. 1"
sh = None
POP = (1.0, 0.93, 0.7)


def scene(c, t, lt, **kw):
    V.canteen(c, t)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def tub(c, x, y, s, a=1.0, hi=False):
    """Popcorn tub, base centre (x,y), height 260*s."""
    c.save(); c.translate(x, y); c.scale(s, s)
    c.push_group()
    for i in range(9):  # popcorn on top
        px, py = -95 + i * 24, -270 + 18 * math.sin(i * 1.7)
        c.arc(px, py, 34, 0, 2 * math.pi); c.set_source_rgb(*POP); c.fill()
    c.move_to(-120, -250); c.line_to(120, -250); c.line_to(90, 0); c.line_to(-90, 0); c.close_path()
    c.set_source_rgb(0.95, 0.95, 0.95); c.fill()
    for i in range(4):
        x0 = -105 + i * 60
        c.move_to(x0, -250); c.line_to(x0 + 30, -250); c.line_to(x0 + 22, 0); c.line_to(x0 - 4, 0); c.close_path()
        c.set_source_rgb(0.85, 0.12, 0.15); c.fill()
    c.pop_group_to_source(); c.paint_with_alpha(a)
    if hi:
        c.set_source_rgba(*YEL, a); c.set_line_width(10)
        c.move_to(-130, -258); c.line_to(130, -258); c.line_to(98, 8); c.line_to(-98, 8); c.close_path(); c.stroke()
    c.restore()


def menu(c, t, st, decoy=True, pick=None):
    K.panel(c, 740, 620)
    T(c, "POPCORN", 540, 815, 52, YEL, stroke=None)
    items = [("SMALL", "₹250", 0.55, 230), ("MEDIUM", "₹380", 0.75, 540), ("LARGE", "₹420", 0.95, 850)]
    for i, (nm, pr, sc, x) in enumerate(items):
        a = k(t, st + 0.2 + i * 0.25, st + 0.45 + i * 0.25)
        if nm == "MEDIUM" and not decoy:
            a *= 0.25
        tub(c, x, 1160, sc, a, hi=(pick == nm))
        T(c, nm, x, 1210, 40, WHITE, a, stroke=None)
        T(c, pr, x, 1280, 54, GRN if nm == "LARGE" else WHITE, a, stroke=None)


def o_menu(c, t, lt):
    st = sh.s(1)
    menu(c, t, st)
    if t > st + 1.6:
        T(c, "M vs L: just ₹40 apart? (example prices)", 540, 1335, 34, GREY, k(t, st + 1.6, st + 1.9), stroke=None)


def o_sid(c, t, lt):
    st = sh.s(2)
    menu(c, t, st - 1, pick="LARGE" if t > st + 2.0 else None)
    K.stamp(c, t, st + 2.4, "'VALUE HAI!'", 540, 1010, GRN, 50, -0.05)


def o_decoy(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    tub(c, 540, 700, 1.0, k(t, st + 0.2, st + 0.5))
    T(c, "MEDIUM", 540, 780, 60, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    K.stamp(c, t, st + 0.9, "DECOY", 540, 560, RED, 96, -0.08)
    if t > st + 2.4:
        T(c, "job: make LARGE look cheap", 540, 920, 56, YEL, k(t, st + 2.4, st + 2.7), lw=7)


def o_test(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "THE ECONOMIST TEST", 540, 400, 62, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    rows = [("Web only", "$59", WHITE), ("Print only", "$125", RED), ("Print + Web", "$125", GRN)]
    for i, (a_, b_, col) in enumerate(rows):
        a = k(t, st + 0.6 + i * 1.0, st + 0.9 + i * 1.0)
        S.rrect(c, 140, 500 + i * 150, 800, 120, 24); c.set_source_rgba(0.1, 0.11, 0.17, 0.95 * a); c.fill()
        T(c, a_, 190, 580 + i * 150, 50, WHITE, a, stroke=None, anchor="left")
        T(c, b_, 890, 580 + i * 150, 60, col, a, stroke=None, anchor="right")
    if t > st + 3.4:
        T(c, "(print only = the decoy)", 540, 1000, 40, YEL, k(t, st + 3.4, st + 3.7), lw=5)


def o_84(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.9)
    T(c, "PICKED THE COMBO", 540, 400, 62, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    K.hbar(c, t, st + 0.5, 140, 520, 800, 110, 0.84, GRN, "with decoy", "84%")
    K.hbar(c, t, st + 2.4, 140, 720, 800, 110, 0.32, RED, "decoy removed", "32%")
    if t > st + 3.6:
        T(c, "SAME PRICES. ONE FAKE OPTION.", 540, 980, 50, YEL, k(t, st + 3.6, st + 3.9), lw=7)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("CINEMA", WHITE, 56, 0.2), ("COFFEE", WHITE, 56, 0.8), ("PHONE PLANS", WHITE, 56, 1.4)], y0=970, gap=95)
    K.stamp(c, t, st + 2.2, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. IGNORE the middle option", WHITE, 44, 0.5, "left", 140),
                      ("2. Ask: if only SMALL existed,", WHITE, 42, 1.8, "left", 140),
                      ("    would I still buy it?", GRN, 42, 2.4, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "THE MIDDLE OPTION", "IS BAIT")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO SAYS 'LARGE HI LE LE'", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    cw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), cw(mouth='o', eyes=1.2), (1.9, 1000, 480), (2.1, 1000, 450), o_menu, 'warm'),
        (s(2), s(3), cw(mouth='bigsmile', eyes=1.2, arms=((60, 120), (14, -10))), (2.0, 1000, 470), (2.15, 1000, 450), o_sid, 'warm'),
        (s(3), s(4), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_decoy, 'red'),
        (s(4), s(5), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_test, 'studio'),
        (s(5), s(6), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_84, 'money'),
        (s(6), s(7), cw(mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), cw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, cw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1))
    else:
        sh.render(f"{D}/short.mp4")
