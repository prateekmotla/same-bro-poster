import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s62_score"
CAPS = [
    "Does checking your OWN credit score lower it? Nope. That's a myth.",
    "Sid hasn't checked his score in 3 years. Scared it'll drop.",
    "Truth: when YOU check, it's a SOFT inquiry. ZERO effect on your score.",
    "It moves when you APPLY for a loan or card. That's a HARD inquiry. Too many, too fast = damage.",
    "And the rule: 1 FREE full credit report a year, from every credit bureau.",
    "Same bro? Too scared to ever check?",
    "Fix: open your report once a year. Wrong loan or late payment? Raise a dispute with the bureau.",
    "MORAL: The mistake you never check is the one that eats your score.",
    "Send this to the friend who's scared to check his score.",
]
HOOK = [("CHECKING YOUR SCORE", WHITE), ("LOWERS IT?", YEL), ("MYTH.", RED)]
SRC = "Source: RBI (1 free credit report/yr per CIC); TransUnion CIBIL FAQ"
sh = None
BLUE = (0.26, 0.52, 0.96)


def gauge(c, t, st, x=540, y=1000, r=300, val=780, a=1.0, lab="CREDIT SCORE"):
    a *= k(t, st, st + 0.3)
    if a <= 0:
        return
    cols = [RED, (1, 0.6, 0.1), YEL, GRN]
    for i, col in enumerate(cols):
        c.arc(x, y, r, math.pi + i * math.pi / 4 + 0.02, math.pi + (i + 1) * math.pi / 4 - 0.02)
        c.set_source_rgba(*col, a); c.set_line_width(46); c.stroke()
    g = U.eob(k(t, st + 0.3, st + 1.3))
    v = 300 + (val - 300) * g
    ang = math.pi + math.pi * (v - 300) / 600
    c.move_to(x, y); c.line_to(x + (r - 60) * math.cos(ang), y + (r - 60) * math.sin(ang))
    c.set_source_rgba(1, 1, 1, a); c.set_line_width(12); c.set_line_cap(1); c.stroke()
    c.arc(x, y, 22, 0, 2 * math.pi); c.set_source_rgba(1, 1, 1, a); c.fill()
    T(c, str(int(v)), x, y + 110, 96, WHITE, a, lw=10)
    T(c, lab, x, y - r - 50, 44, GREY, a, lw=6)


def score_scr(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
    c.rectangle(0, 0, w, 120); c.set_source_rgb(*BLUE); c.fill()
    T(c, "My Credit", w / 2, 82, 42, WHITE, stroke=None)
    T(c, "Last checked:", w / 2, 260, 34, (0.3, 0.3, 0.35), stroke=None, bold=False)
    T(c, "3 YEARS AGO", w / 2, 330, 50, RED, stroke=None)
    S.rrect(c, 60, h - 170, w - 120, 100, 50); c.set_source_rgb(*BLUE); c.fill()
    T(c, "CHECK SCORE", w / 2, h - 105, 36, WHITE, stroke=None)


def rw(mode='night', **kw):
    def f(c, t, lt):
        V.room(c, t, mode, fan=False)
        d = dict(pose='stand', mouth='flat')
        d.update(kw)
        K.sid(c, t, 1000, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def o_hook(c, t, lt):
    st = sh.s(1)
    K.panel(c, 1020, 330)
    K.rows(c, t, st, [("SELF-CHECK = NO DAMAGE", GRN, 58, 0.2), ("IT'S A MYTH", YEL, 54, 2.8)], y0=1120, gap=110)


def o_scared(c, t, lt):
    st = sh.s(2)
    U.phone_frame(c, 290, 470, 500, 760, score_scr, t - st, tilt=-2 + 3 * lt)
    K.stamp(c, t, st + 2.2, "SCARED TO TAP", 540, 1330, RED, 50, -0.05)


def o_soft(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "YOU CHECK = SOFT INQUIRY", 540, 470, 56, WHITE, k(t, st + 0.1, st + 0.4), lw=8)
    gauge(c, t, st + 0.8, val=782)
    K.stamp(c, t, st + 3.0, "EFFECT: ZERO", 540, 1260, GRN, 60, -0.04)


def o_hard(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "YOU APPLY = HARD INQUIRY", 540, 470, 56, YEL, k(t, st + 0.1, st + 0.4), lw=8)
    for i, lab in enumerate(["LOAN APP", "CARD APP", "LOAN APP", "BNPL APP"]):
        a = k(t, st + 1.0 + i * 0.5, st + 1.3 + i * 0.5)
        if a > 0:
            S.rrect(c, 160 + (i % 2) * 400, 620 + (i // 2) * 150, 360, 110, 20); c.set_source_rgba(0.18, 0.2, 0.28, a); c.fill()
            T(c, lab, 340 + (i % 2) * 400, 690 + (i // 2) * 150, 44, WHITE, a, stroke=None)
    K.stamp(c, t, st + 4.5, "TOO MANY, TOO FAST = DAMAGE", 540, 1100, RED, 44, -0.03)


def o_free(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("RULE:", GREY, 60, 0.1), ("1 FREE", YEL, 150, 1.6), ("FULL REPORT / YEAR", WHITE, 64, 2.4),
                      ("FROM EVERY CREDIT BUREAU", GRN, 48, 3.4)], y0=520, gap=170)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 900, 420)
    K.rows(c, t, st, [("NEVER CHECKED", WHITE, 60, 0.3), ("OUT OF FEAR?", YEL, 60, 1.0)], y0=1010, gap=110)
    K.stamp(c, t, st + 1.6, "SAME BRO?", 540, 1250, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(7)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Open your report", WHITE, 48, 0.3, "left", 140),
                      ("    once a year", WHITE, 48, 0.3, "left", 140),
                      ("2. Wrong loan / late entry?", WHITE, 46, 2.4, "left", 140),
                      ("3. Raise a dispute", GRN, 48, 4.0, "left", 140),
                      ("    with the bureau", GRN, 48, 4.0, "left", 140)], y0=1000, gap=76)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "UNCHECKED MISTAKES", "EAT YOUR SCORE.", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "SCARED TO CHECK HIS SCORE", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (60, 120)))
    sh.shots = [
        (0, s(2), rw(mouth='o', eyes=1.3, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'night'),
        (s(2), s(3), rw(mouth='frown', sweat=1, **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_scared, 'night'),
        (s(3), s(4), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_soft, 'money'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_hard, 'red'),
        (s(5), s(6), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_free, 'studio'),
        (s(6), s(7), rw('day', mouth='frown', **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), rw('day', mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw('day', mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
