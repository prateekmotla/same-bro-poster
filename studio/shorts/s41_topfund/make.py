import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s41_topfund"
CAPS = [
    "Guess: today's TOP fund... what are the odds it STAYS on top?",
    "Sid sorts his app by '1Y return'. Picks #1. Easy money, right?",
    "FundsIndia checked equity funds that were in the TOP 25% over 5 years...",
    "...only 21% stayed in the top 25% for the NEXT 5 years.",
    "Last year's winner often just rode ONE hot sector. The wave goes, the returns go.",
    "Same bro? Bought whatever is #1 in the app this month?",
    "Rule: check 5-10 year CONSISTENCY, the expense ratio and YOUR goal. Not the 1-year rank.",
    "MORAL: Yesterday's topper isn't always tomorrow's topper.",
    "Send this to the friend who sorts funds by 1Y return.",
]
HOOK = [("LAST YEAR'S", WHITE), ("TOP FUND?", RED), ("READ THIS FIRST", YEL)]
SRC = "Source: FundsIndia Wealth Conversations (Oct 2026), via 5paisa"
sh = None
FUNDS = [("Fund A", "+58%"), ("Fund B", "+51%"), ("Fund C", "+44%"), ("Fund D", "+39%")]


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
    T(c, "TODAY'S #1 FUND", 540, 990, 50, GREY, stroke=None)
    T(c, "STAYS ON TOP?", 540, 1120, 84, YEL, k(t, st + 0.6, st + 0.9), stroke=None)
    T(c, "?", 540, 1250, 90, WHITE, k(t, st + 1.4, st + 1.7), stroke=None)


def o_sort(c, t, lt):
    st = sh.s(2)
    K.panel(c, 820, 600)
    T(c, "SORT BY: 1Y RETURN", 540, 890, 46, GREY, stroke=None)
    for i, (nm, r) in enumerate(FUNDS):
        a = k(t, st + 0.3 + i * 0.25, st + 0.55 + i * 0.25)
        y = 950 + i * 90
        hi = i == 0 and t > st + 2.0
        S.rrect(c, 150, y, 780, 76, 16); c.set_source_rgba(*(YEL if hi else (0.12, 0.13, 0.2)), a * (0.35 if hi else 0.95)); c.fill()
        T(c, f"#{i + 1}  {nm}", 190, y + 52, 40, WHITE, a, stroke=None, anchor="left")
        T(c, r, 890, y + 52, 44, GRN, a, stroke=None, anchor="right")
    K.stamp(c, t, st + 2.4, "PICKED #1!", 540, 1350, GRN, 48, -0.05)


def o_study(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "FUNDSINDIA STUDY", 540, 400, 62, GREY, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "EQUITY FUNDS IN THE", 540, 540, 62, WHITE, k(t, st + 0.8, st + 1.1), lw=8)
    T(c, "TOP 25%", 540, 690, 140, GRN, k(t, st + 1.4, st + 1.7), lw=14)
    T(c, "over 5 years", 540, 800, 52, WHITE, k(t, st + 2.0, st + 2.3), lw=6)


def o_21(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "STILL TOP 25%, NEXT 5 YEARS", 540, 400, 52, GREY, k(t, st + 0.1, st + 0.4), lw=7)
    T(c, "ONLY", 540, 540, 70, WHITE, k(t, st + 0.4, st + 0.7), lw=8)
    T(c, "21%", 540, 760, 230, RED, k(t, st + 0.8, st + 1.1), lw=18)
    for i in range(10):
        a = k(t, st + 1.6 + i * 0.06, st + 1.8 + i * 0.06)
        on = i < 2
        S.rrect(c, 150 + i * 80, 880, 60, 60, 12); c.set_source_rgba(*(GRN if on else (0.35, 0.37, 0.45)), a); c.fill()
    if t > st + 2.4:
        T(c, "~1 in 5 stayed on top", 540, 1020, 52, YEL, k(t, st + 2.4, st + 2.7), lw=7)


def o_wave(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "ONE HOT SECTOR", 540, 400, 72, YEL, k(t, st + 0.2, st + 0.5), lw=9)
    TR.line(c, t, st + 0.5, 140, 500, 800, 420, [0.2, 0.35, 0.6, 0.9, 0.95, 0.7, 0.45, 0.35], RED, 2.6)
    if t > st + 1.4:
        T(c, "the wave", 400, 520, 44, GRN, k(t, st + 1.4, st + 1.7), lw=5)
    if t > st + 2.6:
        T(c, "...and after", 780, 1000, 44, RED, k(t, st + 2.6, st + 2.9), lw=5)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 900, 420)
    T(c, "#1 THIS MONTH", 540, 1030, 80, WHITE, k(t, st + 0.2, st + 0.4), stroke=None)
    K.stamp(c, t, st + 1.0, "SAME BRO?", 540, 1210, YEL, 64, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "FUND RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. 5-10 year CONSISTENCY", WHITE, 44, 0.6, "left", 140),
                      ("2. Expense ratio (cost)", WHITE, 44, 2.0, "left", 140),
                      ("3. YOUR goal, not 1Y rank", GRN, 44, 3.4, "left", 140)], y0=1070, gap=100)
    if t > st + 4.6:
        T(c, "education only, not advice", 540, 1350, 32, GREY, k(t, st + 4.6, st + 4.9), stroke=None)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "YESTERDAY'S TOPPER", "ISN'T ALWAYS TOMORROW'S")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO SORTS BY 1Y RETURN", YEL)


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
        (s(2), s(3), aw(mouth='bigsmile', eyes=1.2, **ph), (2.0, 1000, 470), (2.15, 1000, 450), o_sort, 'money'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_study, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_21, 'red'),
        (s(5), s(6), aw(crash=3, mouth='frown', squint=0.3, **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_wave, 'red'),
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
