import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
import fest as F  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s44_muhurat"
GOLD = F.GOLD
CAPS = [
    "Guess: why is the stock market open on a SUNDAY this Diwali?",
    "Sid: 'Muhurat trading hai! Shubh din, aaj toh profit pakka.'",
    "Muhurat trading = a 1-hour special session on Diwali. The new Samvat year starts, people make a small 'shagun' buy.",
    "This year: Sunday, 8 Nov, 2:20 to 3:30 PM. Usually it's in the evening, this time it's the afternoon.",
    "But the market doesn't know it's shubh. One hour: prices can go UP or DOWN.",
    "Same bro? 'Shubh muhurat hai, F&O mein bada daav'?",
    "Rule: joining? Keep it a small token buy, only what was already in your plan. No F&O, no tips.",
    "MORAL: Muhurat is a tradition, not a profit guarantee.",
    "Send this to the friend planning a BIG Muhurat trade.",
]
HOOK = [("MARKET OPEN", WHITE), ("ON A SUNDAY?", GOLD), ("MUHURAT TRADING", YEL)]
SRC = "Source: NSE circular, Muhurat trading 8 Nov 2026"
sh = None


def scene(c, t, lt, **kw):
    F.room(c, t, lt, **kw)


def desk(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash)
    F.lights(c, t, 60)
    for i in range(3):
        F.diya(c, 1340 + i * 90, 668, t, 0.7)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "NSE / BSE", 540, 960, 46, GREY, k(t, st + 0.2, st + 0.5), stroke=None)
    T(c, "SUNDAY", 540, 1100, 120, GOLD, k(t, st + 0.5, st + 0.8), stroke=None)
    K.stamp(c, t, st + 1.3, "OPEN", 540, 1260, GRN, 70, -0.06)


def o_sid(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    T(c, "'SHUBH DIN...'", 540, 1000, 66, GOLD, k(t, st + 0.2, st + 0.5), stroke=None)
    K.stamp(c, t, st + 1.6, "'PROFIT PAKKA!'", 540, 1180, GRN, 64, -0.05)


def o_what(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "MUHURAT TRADING", 540, 400, 76, GOLD, k(t, st + 0.1, st + 0.4), lw=9)
    rows = [("1-hour special session", WHITE), ("New Samvat year begins", YEL), ("Small 'shagun' buy", GRN)]
    for i, (r, col) in enumerate(rows):
        a = k(t, st + 0.8 + i * 1.3, st + 1.1 + i * 1.3)
        S.rrect(c, 120, 490 + i * 150, 840, 120, 26); c.set_source_rgba(0.1, 0.11, 0.17, 0.95 * a); c.fill()
        T(c, r, 540, 568 + i * 150, 54, col, a, stroke=None)


def o_when(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "SUNDAY, 8 NOV", 540, 430, 90, WHITE, k(t, st + 0.2, st + 0.5), lw=10)
    T(c, "2:20 - 3:30 PM", 540, 620, 130, GOLD, k(t, st + 0.9, st + 1.2), lw=14)
    T(c, "usually evening, this year AFTERNOON", 540, 780, 44, YEL, k(t, st + 2.4, st + 2.7), lw=6)


def o_swing(c, t, lt):
    st = sh.s(5)
    K.panel(c, 820, 560)
    T(c, "1 HOUR. EITHER WAY.", 540, 900, 54, WHITE, k(t, st + 0.1, st + 0.4), stroke=None)
    pts = [0.5, 0.62, 0.4, 0.7, 0.35, 0.6, 0.3, 0.55]
    TR.line(c, t, st + 0.5, 150, 950, 780, 330, pts, col=YEL, dur=2.4, lw=10)
    if t > st + 2.9:
        T(c, "UP?", 860, 1010, 50, GRN, k(t, st + 2.9, st + 3.2), stroke=None)
        T(c, "DOWN?", 840, 1270, 50, RED, k(t, st + 3.2, st + 3.5), stroke=None)


def o_samebro(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("'SHUBH HAI...'", GOLD, 60, 0.2), ("BIG F&O BET?", RED, 70, 1.0)], y0=1000, gap=120)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Small TOKEN buy only", WHITE, 44, 0.6, "left", 140),
                      ("2. Only what's in your plan", GRN, 44, 2.0, "left", 140),
                      ("3. NO F&O. NO tips.", RED, 44, 3.6, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "A TRADITION,", "NOT A GUARANTEE", GOLD)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "PLANNING A BIG MUHURAT TRADE", YEL)


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
        (0, s(2), rw(mouth='o', eyes=1.2), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'warm'),
        (s(2), s(3), dw(mouth='bigsmile', eyes=1.2, **ph), (2.0, 1000, 470), (2.15, 1000, 450), o_sid, 'warm'),
        (s(3), s(4), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_what, 'studio'),
        (s(4), s(5), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_when, 'warm'),
        (s(5), s(6), dw(crash=2, mouth='frown', squint=0.3, **ph), (1.9, 1000, 480), (2.0, 1000, 460), o_swing, 'red'),
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
