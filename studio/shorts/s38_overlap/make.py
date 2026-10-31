import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s38_overlap"
CAPS = [
    "Sid has 8 mutual funds. 'Full diversification, bro!' But open them up...",
    "...the same big companies show up again and again.",
    "Why? SEBI rule: a large-cap fund must put at least 80% in large-cap stocks.",
    "And 'large cap' = only the TOP 100 companies by market value.",
    "So 4 large-cap funds are fishing in the SAME pond of 100 stocks.",
    "8 funds can behave like just 2 or 3. More clutter, same risk.",
    "Rule: check PORTFOLIO OVERLAP first. Fewer funds, each with a DIFFERENT job.",
    "MORAL: More funds isn't more diversification.",
    "Send this to the friend with 12 funds in his app.",
]
HOOK = [("8 FUNDS =", WHITE), ("SAME STOCKS?", RED), ("FAKE DIVERSIFICATION", YEL)]
SRC = "Source: SEBI MF categorisation circular (Oct 2017)"
sh = None
COLS = [BLUE, GRN, YEL, (1, 0.55, 0.2), (0.75, 0.45, 1), (1, 0.4, 0.6), (0.4, 0.9, 0.9), RED]


def scene(c, t, lt, **kw):
    V.room(c, t, 'night', fan=True)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_funds(c, t, lt):
    st = sh.s(1)
    K.panel(c, 870, 500)
    T(c, "SID'S APP: 8 FUNDS", 540, 950, 50, GREY, stroke=None)
    for i in range(8):
        r, cc = divmod(i, 4)
        a = k(t, st + 0.4 + i * 0.2, st + 0.6 + i * 0.2)
        if a > 0:
            S.rrect(c, 150 + cc * 200, 1000 + r * 150, 170, 120, 18); c.set_source_rgba(*COLS[i], a); c.fill()
            T(c, f"FUND {i + 1}", 235 + cc * 200, 1072 + r * 150, 34, (0.05, 0.05, 0.08), a, stroke=None)


def o_same(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "INSIDE EACH FUND", 540, 400, 66, WHITE, k(t, st + 0.1, st + 0.4), lw=8)
    for i in range(8):
        r, cc = divmod(i, 4)
        a = k(t, st + 0.3 + i * 0.1, st + 0.5 + i * 0.1)
        x, y = 150 + cc * 200, 500 + r * 260
        S.rrect(c, x, y, 170, 220, 18); c.set_source_rgba(*COLS[i], 0.25 * a); c.fill()
        for j, lab in enumerate("ABC"):
            T(c, f"Co. {lab}", x + 85, y + 60 + j * 60, 36, WHITE, a, stroke=None)
    if t > st + 2.0:
        T(c, "SAME NAMES EVERYWHERE", 540, 1100, 64, RED, k(t, st + 2.0, st + 2.3), lw=8)


def o_rule80(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "SEBI RULE", 540, 400, 64, GREY, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "LARGE-CAP FUND", 540, 540, 86, WHITE, k(t, st + 0.6, st + 0.9), lw=10)
    K.hbar(c, t, st + 1.4, 140, 680, 800, 90, 0.8, YEL, "in large caps", "80%+")


def o_top100(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "LARGE CAP =", 540, 420, 76, WHITE, k(t, st + 0.2, st + 0.5), lw=10)
    T(c, "TOP 100", 540, 620, 180, GRN, k(t, st + 0.8, st + 1.1), lw=16)
    T(c, "companies by market value", 540, 750, 52, WHITE, k(t, st + 1.6, st + 1.9), lw=6)


def o_pond(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "SAME POND", 540, 400, 90, YEL, k(t, st + 0.2, st + 0.5), lw=10)
    a = k(t, st + 0.5, st + 0.9)
    c.save(); c.translate(540, 760); c.scale(1, 0.5)
    c.arc(0, 0, 380, 0, 2 * math.pi); c.restore()
    c.set_source_rgba(0.15, 0.4, 0.8, 0.6 * a); c.fill()
    T(c, "100 STOCKS", 540, 780, 64, WHITE, a, stroke=None)
    for i in range(4):
        b = k(t, st + 1.2 + i * 0.4, st + 1.4 + i * 0.4)
        ang = math.pi + i * math.pi / 3
        x, y = 540 + 430 * math.cos(ang) * 0.9, 760 + 220 * math.sin(ang) - 40
        if b > 0:
            S.rrect(c, x - 80, y - 40, 160, 70, 18); c.set_source_rgba(*COLS[i], b); c.fill()
            T(c, f"FUND {i + 1}", x, y + 10, 32, (0.05, 0.05, 0.08), b, stroke=None)


def o_like3(c, t, lt):
    st = sh.s(6)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("8 FUNDS", WHITE, 70, 0.3), ("can act like 2 or 3", YEL, 52, 1.3),
                      ("more clutter, SAME risk", RED, 46, 2.6)], y0=1000, gap=115)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Check portfolio OVERLAP", WHITE, 42, 0.8, "left", 140),
                      ("2. Fewer funds", GRN, 42, 2.2, "left", 140),
                      ("3. Each with a DIFFERENT job", WHITE, 42, 3.6, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "MORE FUNDS ISN'T", "MORE DIVERSIFICATION")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WITH 12 FUNDS IN HIS APP", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), rw(mouth='bigsmile', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_funds, 'night'),
        (s(2), s(3), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_same, 'studio'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_rule80, 'studio'),
        (s(4), s(5), sw(), (1.78, 960, 540), (1.85, 960, 520), o_top100, 'money'),
        (s(5), s(6), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_pond, 'studio'),
        (s(6), s(7), rw(mouth='frown', squint=0.3, **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_like3, 'night'),
        (s(7), s(8), rw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'night'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'night'),
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
