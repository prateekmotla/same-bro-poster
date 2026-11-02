import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
import fest as F  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s43_cards"
GOLD = F.GOLD
CAPS = [
    "Guess: what does a Diwali card party have in common with F&O?",
    "Sid at the Diwali taash party: lost ₹2,000. 'Bas ek aur round, sab wapas!'",
    "Same brain on the trading app. Loss on an option? 'One more trade, I'll recover it.'",
    "SEBI: in FY25, F&O traders lost ₹1.1 LAKH each, on average.",
    "Cards or options: small bet, FAST result, 'next round' feeling. Your brain loves it.",
    "Same bro? Taash at Diwali, options all year?",
    "Rule: play cards for fun with a FIXED limit. Limit gone = game over. Money you need? Never in lottery trades.",
    "MORAL: Gambling with a chart is still gambling.",
    "Send this to the friend who always says 'bas ek last round'.",
]
HOOK = [("DIWALI CARD PARTY", WHITE), ("= F&O BRAIN?", GOLD), ("SAME TRAP", RED)]
SRC = "Source: SEBI F&O study, FY25 (Jul 2025)"
sh = None


def scene(c, t, lt, **kw):
    F.room(c, t, lt, **kw)


def desk(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash)
    F.lights(c, t, 60)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def card(c, x, y, s, txt, col=RED, a=1.0, rot=0.0, back=False):
    """Playing card centred at (x,y), 160x230 * s."""
    c.save(); c.translate(x, y); c.rotate(rot); c.scale(s, s)
    S.rrect(c, -80, -115, 160, 230, 14)
    if back:
        c.set_source_rgba(0.6, 0.1, 0.15, a); c.fill()
        S.rrect(c, -66, -101, 132, 202, 10); c.set_source_rgba(*GOLD, a); c.set_line_width(5); c.stroke()
    else:
        c.set_source_rgba(0.98, 0.97, 0.94, a); c.fill()
        T(c, txt, 0, 30, 96, col, a, stroke=None)
    c.restore()


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    for i, (tx, col) in enumerate([("A", RED), ("K", (0.1, 0.1, 0.12)), ("7", RED)]):
        card(c, 330 + i * 110, 1110, 1.0, tx, col, k(t, st + 0.2 + i * 0.2, st + 0.4 + i * 0.2), -0.25 + i * 0.25)
    T(c, "=", 650, 1140, 110, YEL, k(t, st + 1.0, st + 1.3), stroke=None)
    T(c, "F&O?", 830, 1150, 100, RED, k(t, st + 1.4, st + 1.7), stroke=None)


def o_party(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    for i in range(3):
        card(c, 300 + i * 120, 1080, 0.9, "", a=k(t, st + 0.2 + i * 0.15, st + 0.4 + i * 0.15), rot=-0.2 + i * 0.2, back=True)
    T(c, "-₹2,000", 790, 1110, 96, RED, k(t, st + 0.9, st + 1.2), stroke=None)
    K.stamp(c, t, st + 2.4, "'EK AUR ROUND!'", 540, 1290, YEL, 54, -0.05)


def o_app(c, t, lt):
    st = sh.s(3)
    K.panel(c, 880, 480)
    T(c, "NIFTY 24000 CE", 540, 970, 48, GREY, k(t, st + 0.2, st + 0.5), stroke=None)
    T(c, "-₹3,500", 540, 1110, 110, RED, k(t, st + 0.6, st + 0.9), stroke=None)
    K.stamp(c, t, st + 2.0, "'ONE MORE TRADE!'", 540, 1290, YEL, 54, 0.04)


def o_sebi(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "SEBI STUDY, FY25", 540, 420, 70, WHITE, k(t, st + 0.2, st + 0.5), lw=9)
    T(c, "avg loss per F&O trader", 540, 520, 48, GREY, k(t, st + 0.7, st + 1.0), lw=6)
    T(c, "₹1.1 LAKH", 540, 730, 170, RED, k(t, st + 1.3, st + 1.6), lw=16)
    T(c, "in ONE year", 540, 870, 56, YEL, k(t, st + 2.2, st + 2.5), lw=7)


def o_same(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.86)
    T(c, "CARDS", 300, 440, 76, GOLD, k(t, st + 0.1, st + 0.4), lw=9)
    T(c, "OPTIONS", 780, 440, 76, BLUE, k(t, st + 0.1, st + 0.4), lw=9)
    rows = ["small bet", "FAST result", "'next round'"]
    for i, r in enumerate(rows):
        a = k(t, st + 0.7 + i * 0.7, st + 1.0 + i * 0.7)
        S.rrect(c, 140, 520 + i * 140, 800, 110, 26); c.set_source_rgba(0.1, 0.11, 0.17, 0.95 * a); c.fill()
        T(c, r, 540, 595 + i * 140, 56, WHITE, a, stroke=None)
    if t > st + 3.0:
        T(c, "SAME BRAIN", 540, 1000, 80, RED, k(t, st + 3.0, st + 3.3), lw=9)


def o_samebro(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("DIWALI: TAASH", GOLD, 60, 0.2), ("ALL YEAR: OPTIONS", BLUE, 60, 0.9)], y0=1000, gap=110)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Cards for fun, FIXED limit", WHITE, 42, 0.5, "left", 130),
                      ("2. Limit gone = game over", RED, 42, 2.0, "left", 130),
                      ("3. Needed money? NOT in", GRN, 42, 3.4, "left", 130),
                      ("    lottery trades", GRN, 42, 3.4, "left", 130)], y0=1060, gap=82)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "GAMBLING WITH A CHART", "IS STILL GAMBLING")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "'BAS EK LAST ROUND'", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'warm'
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    dw = lambda **kw: (lambda c, t, lt: desk(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), rw(mouth='smirk', eyes=1.1), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'warm'),
        (s(2), s(3), rw(mouth='grit', squint=0.3, arms=((60, 120), (14, -10))), (2.0, 1000, 470), (2.15, 1000, 450), o_party, 'warm'),
        (s(3), s(4), dw(crash=2, mouth='frown', squint=0.4, **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_app, 'red'),
        (s(4), s(5), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_sebi, 'red'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_same, 'studio'),
        (s(6), s(7), rw(mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_samebro, 'warm'),
        (s(7), s(8), rw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
