import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
import fest as F  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s33_bonus"
CAPS = [
    "October salary + DIWALI BONUS! Sid is already planning a new phone. But why does a bonus even exist?",
    "The popular story: under the British, workers were paid WEEKLY. 52 weeks a year.",
    "Then pay went MONTHLY. 12 months = only 48 weeks of pay. 4 weeks LOST.",
    "Protests followed. In 1940, the British gave a '13th month' pay around Diwali.",
    "1965: India made it law, the Payment of Bonus Act. Today it's part of the Code on Wages.",
    "For eligible employees: minimum bonus 8.33% of yearly pay. That's 1 month out of 12. Max: 20%.",
    "Rule: split it BEFORE it lands. Clear card dues first, some for Diwali, the rest to savings.",
    "MORAL: A bonus is a reward, not a reason to go broke.",
    "Send this to the friend whose bonus is gone before Bhai Dooj.",
]
HOOK = [("WHY DOES A", WHITE), ("DIWALI BONUS", YEL), ("EVEN EXIST?", RED)]
SRC = "Source: Payment of Bonus Act 1965; DailyO"
sh = None


def scene(c, t, lt, **kw):
    F.room(c, t, lt, **kw)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_bonus(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 500)
    F.envelope(c, 540, 1010, 360, 200, "BONUS", k(t, st + 0.3, st + 0.6))
    K.stamp(c, t, st + 1.8, "NEW PHONE?", 540, 1210, GRN, 54, -0.04)
    if t > st + 3.4:
        T(c, "but WHY does it exist?", 540, 1320, 50, YEL, k(t, st + 3.4, st + 3.7), stroke=None)


def o_weekly(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "BRITISH ERA", 540, 400, 70, GREY, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "PAID WEEKLY", 540, 520, 96, WHITE, k(t, st + 0.6, st + 0.9), lw=12)
    for i in range(52):
        r, cc = divmod(i, 13)
        a = k(t, st + 1.2 + i * 0.03, st + 1.35 + i * 0.03)
        if a > 0:
            S.rrect(c, 120 + cc * 66, 640 + r * 90, 52, 70, 10); c.set_source_rgba(*GRN, a); c.fill()
    if t > st + 3.0:
        T(c, "52 PAYDAYS A YEAR", 540, 1080, 70, GRN, k(t, st + 3.0, st + 3.3), lw=8)


def o_monthly(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "THEN: MONTHLY", 540, 400, 80, WHITE, k(t, st + 0.2, st + 0.5), lw=10)
    for i in range(52):
        r, cc = divmod(i, 13)
        lost = cc == 12
        col = RED if (lost and t > st + 1.6) else GRN
        S.rrect(c, 120 + cc * 66, 520 + r * 90, 52, 70, 10)
        c.set_source_rgba(*col, 0.35 if (lost and t > st + 1.6) else 1); c.fill()
    T(c, "12 months x 4 weeks = 48", 540, 960, 56, WHITE, k(t, st + 1.0, st + 1.3), lw=7)
    if t > st + 2.4:
        T(c, "4 WEEKS LOST", 540, 1100, 100, RED, k(t, st + 2.4, st + 2.7), lw=12)


def o_1940(c, t, lt):
    st = sh.s(4)
    K.panel(c, 870, 500)
    T(c, "PROTESTS > 1940", 540, 960, 56, GREY, stroke=None)
    K.rows(c, t, st, [("'13th MONTH' PAY", YEL, 76, 0.8), ("given around DIWALI", WHITE, 50, 2.0)], y0=1090, gap=110)
    F.diya(c, 300, 1320, t, 0.8); F.diya(c, 780, 1320, t, 0.8)


def o_law(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "1965", 540, 460, 150, YEL, k(t, st + 0.2, st + 0.5), lw=14)
    T(c, "PAYMENT OF BONUS ACT", 540, 620, 70, WHITE, k(t, st + 0.8, st + 1.1), lw=8)
    if t > st + 2.6:
        T(c, "today: part of the", 540, 800, 50, GREY, k(t, st + 2.6, st + 2.9), lw=6)
        T(c, "CODE ON WAGES", 540, 890, 80, GRN, k(t, st + 2.6, st + 2.9), lw=10)


def o_pct(c, t, lt):
    st = sh.s(6)
    U.dim(c, 0.88)
    T(c, "MINIMUM BONUS", 540, 400, 64, GREY, k(t, st + 0.3, st + 0.6), lw=8)
    T(c, "8.33%", 540, 590, 170, YEL, k(t, st + 0.8, st + 1.1), lw=16)
    T(c, "= 1 month out of 12", 540, 720, 60, WHITE, k(t, st + 2.0, st + 2.3), lw=8)
    if t > st + 3.6:
        T(c, "MAXIMUM: 20%", 540, 900, 90, GRN, k(t, st + 3.6, st + 3.9), lw=10)
        T(c, "for eligible employees", 540, 990, 40, GREY, k(t, st + 3.6, st + 3.9), lw=5)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "BONUS RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Clear card dues FIRST", RED, 42, 0.8, "left", 140),
                      ("2. A fixed part for Diwali", WHITE, 42, 2.2, "left", 140),
                      ("3. The rest > savings", GRN, 42, 3.6, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "BONUS = REWARD,", "NOT A REASON TO GO BROKE")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "BROKE BEFORE BHAI DOOJ", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), rw(mouth='bigsmile', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_bonus, 'warm'),
        (s(2), s(3), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_weekly, 'studio'),
        (s(3), s(4), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_monthly, 'red'),
        (s(4), s(5), rw(mouth='smile'), (1.9, 1000, 500), (2.0, 1000, 470), o_1940, 'warm'),
        (s(5), s(6), sw(), (1.78, 960, 540), (1.85, 960, 520), o_law, 'studio'),
        (s(6), s(7), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_pct, 'money'),
        (s(7), s(8), rw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw(mouth='bigsmile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
