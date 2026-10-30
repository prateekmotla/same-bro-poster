import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s24_expiry"
CAPS = [
    "Expiry day. Sid buys ₹5,000 of cheap options. Dream: ₹50,000 by 3:30 PM.",
    "3:30 PM. His ₹5,000 is now ₹0. Same story every week, bro.",
    "Hidden reason: an option MELTS daily. On expiry day, its time value hits ZERO by close.",
    "So the price must move BIG, FAST and TODAY itself. Most days, it just doesn't.",
    "SEBI: 59% of index-option trading in FY26 happened ON expiry day itself.",
    "Result: 88% of individual F&O traders lost money in FY26. Under 30? 89% lost.",
    "Rule: no lottery bets on expiry. Learn first, go small, only money you can lose.",
    "MORAL: Expiry day is not a lottery ticket.",
    "Send this to the friend who says 'bas aaj ka expiry, phir band.'",
]
HOOK = [("₹5K TO ₹50K", WHITE), ("ON EXPIRY DAY?", RED), ("THE REAL MATH", YEL)]
SRC = "Source: SEBI F&O study FY26 (Aug 2026)"
sh = None


def scene(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_dream(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "EXPIRY DAY", 540, 960, 50, GREY, stroke=None)
    K.rows(c, t, st, [("BUY: ₹5,000", WHITE, 64, 0.8), ("DREAM: ₹50,000", GRN, 72, 2.4)], y0=1090, gap=130)
    if t > st + 3.6:
        T(c, "by 3:30 PM", 540, 1320, 46, YEL, k(t, st + 3.6, st + 3.9), stroke=None)


def o_zero(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    T(c, "3:30 PM", 540, 960, 54, GREY, stroke=None)
    v = 5000 * max(0, 1 - (t - st - 0.6) / 1.6) if t > st + 0.6 else 5000
    T(c, f"₹{int(v):,}", 540, 1120, 120, RED if v < 5000 else WHITE, stroke=None)
    K.stamp(c, t, st + 2.4, "EXPIRED WORTHLESS", 540, 1290, RED, 46)


def o_theta(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "OPTION TIME VALUE", 540, 380, 64, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "on expiry day", 540, 450, 42, GREY, k(t, st + 0.2, st + 0.5), lw=6)
    pts = [math.sqrt(max(0, 1 - i / 12)) * 0.9 + 0.02 for i in range(13)]
    TR.line(c, t, st + 0.8, 140, 560, 800, 520, pts, RED, dur=3.0)
    if t > st + 0.8:
        T(c, "9:15 AM", 180, 1140, 36, GREY, stroke=None, anchor="left")
        T(c, "3:30 PM", 900, 1140, 36, GREY, stroke=None, anchor="right")
    if t > st + 4.0:
        T(c, "ZERO", 840, 1010, 80, RED, k(t, st + 4.0, st + 4.3), lw=10)
    if t > st + 4.6:
        T(c, "time decay = THETA", 540, 1260, 54, YEL, k(t, st + 4.6, st + 4.9), lw=8)


def o_move(c, t, lt):
    st = sh.s(4)
    K.panel(c, 870, 500)
    T(c, "TO WIN, PRICE MUST MOVE:", 540, 950, 44, GREY, stroke=None)
    K.rows(c, t, st, [("1. BIG", WHITE, 62, 0.7), ("2. FAST", WHITE, 62, 1.3), ("3. TODAY", YEL, 62, 1.9)], y0=1060, gap=95)
    K.stamp(c, t, st + 3.4, "MOST DAYS: NO", 540, 1330, RED, 40, 0.04)


def o_crowd(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "INDEX-OPTION TRADING", 540, 400, 62, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    T(c, "SEBI study, FY26", 540, 470, 40, GREY, k(t, st + 0.3, st + 0.6), lw=6)
    K.hbar(c, t, st + 1.6, 140, 680, 800, 80, 0.59, RED, "ON expiry day", "59%")
    K.hbar(c, t, st + 2.8, 140, 890, 800, 80, 0.75, YEL, "within 1 day of expiry", "75%")
    if t > st + 4.2:
        T(c, "EVERYONE'S BUYING TICKETS", 540, 1130, 62, YEL, k(t, st + 4.2, st + 4.5), lw=8)


def o_lost(c, t, lt):
    st = sh.s(6)
    U.dim(c, 0.88)
    T(c, "LOST MONEY IN FY26", 540, 400, 70, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    K.hbar(c, t, st + 1.2, 140, 620, 800, 80, 0.88, RED, "All individual F&O traders", "88%")
    K.hbar(c, t, st + 3.0, 140, 830, 800, 80, 0.89, RED, "Traders under 30", "89%")
    if t > st + 4.4:
        T(c, "9 OUT OF 10", 540, 1090, 110, YEL, k(t, st + 4.4, st + 4.7), lw=12)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. No lottery bets on expiry", WHITE, 44, 0.8, "left", 150),
                      ("2. Learn first, go SMALL", GRN, 44, 2.0, "left", 150),
                      ("3. Only money you can lose", WHITE, 44, 3.2, "left", 150)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "EXPIRY DAY IS NOT", "A LOTTERY TICKET")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "'BAS AAJ KA EXPIRY'", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), aw(mouth='bigsmile', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_dream, 'night'),
        (s(2), s(3), aw(crash=6, mouth='o', eyes=1.3, **ph), (1.9, 1000, 480), (2.0, 1000, 460), o_zero, 'red'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_theta, 'studio'),
        (s(4), s(5), aw(crash=6, mouth='frown', squint=0.4), (1.9, 1000, 500), (2.0, 1000, 470), o_move, 'night'),
        (s(5), s(6), sw(), (1.78, 960, 540), (1.85, 960, 520), o_crowd, 'studio'),
        (s(6), s(7), sw(mouth='frown'), (1.78, 960, 540), (1.85, 960, 520), o_lost, 'red'),
        (s(7), s(8), aw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'night'),
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
