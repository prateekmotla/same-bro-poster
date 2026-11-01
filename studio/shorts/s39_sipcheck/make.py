import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s39_sipcheck"
CAPS = [
    "Guess why checking your SIP DAILY makes you lose money?",
    "Sid opens his app 10 times a day. -₹800 today. Mood ruined.",
    "Science: a loss hurts about 2X more than the same gain feels good.",
    "Check daily and you see RED on lots of days. Your brain only counts the pain.",
    "So: panic. Pause SIP. Sell at the bottom. It's called myopic loss aversion.",
    "Same bro? First thing at 9:15 AM: open the app?",
    "Rule: check your SIP once a MONTH or once a quarter. Remove the widget. Let time work.",
    "MORAL: Check less, panic less.",
    "Send this to the friend who checks his SIP in class.",
]
HOOK = [("STOP CHECKING", WHITE), ("YOUR SIP DAILY", RED), ("HERE'S WHY", YEL)]
SRC = "Source: Kahneman & Tversky (1992); Benartzi & Thaler (1995)"
sh = None


def scene(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 900, 420)
    T(c, "OPENED TODAY", 540, 990, 48, GREY, stroke=None)
    n = min(10, int(max(0, t - st - 0.3) * 4) + 1)
    T(c, f"{n}x", 540, 1150, 150, YEL, k(t, st + 0.3, st + 0.5), stroke=None)


def o_red(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    T(c, "MY SIP TODAY", 540, 960, 48, GREY, stroke=None)
    K.rows(c, t, st, [("-₹800", RED, 130, 0.5)], y0=1130)
    K.stamp(c, t, st + 1.8, "MOOD: RUINED", 540, 1270, RED, 52, -0.05)


def o_2x(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "HOW IT FEELS", 540, 400, 64, GREY, k(t, st + 0.2, st + 0.5), lw=8)
    K.hbar(c, t, st + 0.8, 140, 520, 800, 90, 0.4, GRN, "gain ₹1,000", "1x")
    K.hbar(c, t, st + 1.6, 140, 700, 800, 90, 0.8, RED, "loss ₹1,000", "~2x")
    if t > st + 2.6:
        T(c, "LOSS HURTS ~2X", 540, 960, 96, YEL, k(t, st + 2.6, st + 2.9), lw=12)


def o_days(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "DAILY VIEW", 540, 400, 66, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    for i in range(20):
        r, cc = divmod(i, 5)
        a = k(t, st + 0.5 + i * 0.07, st + 0.7 + i * 0.07)
        col = RED if (i * 7) % 5 in (0, 3) else GRN
        S.rrect(c, 190 + cc * 140, 480 + r * 120, 120, 100, 14); c.set_source_rgba(*col, a); c.fill()
    if t > st + 2.4:
        T(c, "BRAIN COUNTS ONLY THE RED", 540, 1060, 58, RED, k(t, st + 2.4, st + 2.7), lw=8)


def o_panic(c, t, lt):
    st = sh.s(5)
    K.panel(c, 870, 520)
    K.rows(c, t, st, [("PANIC", RED, 72, 0.2), ("> PAUSE SIP", WHITE, 56, 0.9), ("> SELL AT THE BOTTOM", WHITE, 52, 1.6),
                      ("myopic loss aversion", YEL, 44, 2.8)], y0=980, gap=105)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 900, 420)
    T(c, "9:15 AM", 540, 1040, 110, WHITE, k(t, st + 0.2, st + 0.4), stroke=None)
    K.stamp(c, t, st + 1.0, "SAME BRO?", 540, 1210, YEL, 64, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "SIP RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Check once a MONTH", WHITE, 44, 0.8, "left", 140),
                      ("2. Remove the app widget", WHITE, 44, 2.2, "left", 140),
                      ("3. Let TIME do the work", GRN, 44, 3.6, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "CHECK LESS,", "PANIC LESS")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO CHECKS SIP IN CLASS", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'tense'
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), aw(mouth='o', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'night'),
        (s(2), s(3), aw(crash=3, mouth='grit', squint=0.3, **ph), (2.0, 1000, 470), (2.2, 1000, 440), o_red, 'red'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_2x, 'studio'),
        (s(4), s(5), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_days, 'red'),
        (s(5), s(6), aw(crash=3, mouth='frown', squint=0.4, **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_panic, 'red'),
        (s(6), s(7), aw(mouth='smirk', **ph), (1.9, 1000, 480), (2.05, 1000, 460), o_same, 'night'),
        (s(7), s(8), aw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'night'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, aw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'night'),
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
