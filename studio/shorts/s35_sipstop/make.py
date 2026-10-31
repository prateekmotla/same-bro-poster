import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s35_sipstop"
CAPS = [
    "Market falls 20%. Sid's SIP is red. He taps STOP SIP. 'Pehle market theek ho jaaye.'",
    "Wrong move. In a fall, the same ₹5,000 SIP buys MORE units.",
    "Remember COVID 2020: Nifty fell about 38%, from ~12,360 in January to ~7,610 on 23 March.",
    "By November 2020 it was back above the old high. By end-2021, above 17,000.",
    "SIPs that kept running bought cheap units all through the fall. Those who stopped, missed them.",
    "Stopping in a fall = skipping the sale, then buying back at full price later.",
    "Rule: SIP is for 5+ years. Don't stop it in a fall. Stop only if YOUR goal or income changes. Past isn't a guarantee.",
    "MORAL: A market fall is your SIP's discount season.",
    "Send this to the friend who paused his SIP the last time markets fell.",
]
HOOK = [("STOPPED YOUR SIP", WHITE), ("IN A FALL?", RED), ("BIG MISTAKE", YEL)]
SRC = "Source: NSE Nifty 50 closing data (2020-21)"
sh = None


def scene(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_stop(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "MY SIP", 540, 960, 48, GREY, stroke=None)
    K.rows(c, t, st, [("-20%", RED, 110, 0.3)], y0=1110)
    if t > st + 1.8:
        a = k(t, st + 1.8, st + 2.0)
        S.rrect(c, 340, 1190, 400, 100, 50); c.set_source_rgba(*RED, a); c.fill()
        T(c, "STOP SIP", 540, 1258, 52, WHITE, a, stroke=None)


def o_units(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "SAME ₹5,000 SIP", 540, 400, 72, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "NAV ₹100", 300, 560, 54, GREY, k(t, st + 0.8, st + 1.1), lw=6)
    T(c, "50 units", 300, 660, 70, WHITE, k(t, st + 0.8, st + 1.1), lw=8)
    T(c, "NAV ₹80", 780, 560, 54, GREY, k(t, st + 1.6, st + 1.9), lw=6)
    T(c, "62.5 units", 780, 660, 70, GRN, k(t, st + 1.6, st + 1.9), lw=8)
    if t > st + 2.6:
        T(c, "FALL = MORE UNITS", 540, 860, 84, YEL, k(t, st + 2.6, st + 2.9), lw=10)
        T(c, "(example numbers)", 540, 940, 36, GREY, k(t, st + 2.6, st + 2.9), lw=5)


PTS = [0.86, 0.84, 0.62, 0.30, 0.18, 0.40, 0.55, 0.70, 0.88, 0.95]


def o_covid(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "NIFTY 50, 2020", 540, 400, 70, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    TR.line(c, t, st + 0.6, 140, 520, 800, 420, PTS[:5], RED, 2.0)
    if t > st + 1.0:
        T(c, "~12,360 (Jan)", 260, 500, 40, WHITE, k(t, st + 1.0, st + 1.3), lw=5)
    if t > st + 2.8:
        T(c, "~7,610 (23 Mar)", 820, 1000, 44, RED, k(t, st + 2.8, st + 3.1), lw=5)
        T(c, "-38%", 540, 1110, 120, RED, k(t, st + 3.2, st + 3.5), lw=12)


def o_back(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "THEN...", 540, 400, 70, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    TR.line(c, t, st + 0.2, 140, 520, 800, 420, PTS, GRN, 3.0)
    if t > st + 1.6:
        T(c, "Nov 2020: above old high", 540, 1040, 50, GRN, k(t, st + 1.6, st + 1.9), lw=6)
    if t > st + 3.0:
        T(c, "End-2021: 17,000+", 540, 1130, 70, YEL, k(t, st + 3.0, st + 3.3), lw=8)


def o_cheap(c, t, lt):
    st = sh.s(5)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("KEPT SIP:", WHITE, 50, 0.3), ("cheap units all through the fall", GRN, 42, 0.9),
                      ("STOPPED:", WHITE, 50, 2.6), ("missed the cheapest months", RED, 42, 3.2)], y0=990, gap=90)


def o_sale(c, t, lt):
    st = sh.s(6)
    U.dim(c, 0.88)
    T(c, "STOPPING IN A FALL =", 540, 460, 70, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    K.stamp(c, t, st + 1.0, "SKIPPING THE SALE", 540, 640, RED, 64, -0.04)
    if t > st + 2.6:
        T(c, "then paying FULL price later", 540, 860, 56, YEL, k(t, st + 2.6, st + 2.9), lw=7)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "SIP RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. SIP = 5+ year money", WHITE, 42, 0.8, "left", 140),
                      ("2. Market fall? Keep going", GRN, 42, 2.2, "left", 140),
                      ("3. Stop only if goal/income changes", WHITE, 38, 3.6, "left", 140)], y0=1070, gap=100)
    if t > st + 5.6:
        T(c, "past returns are not a guarantee", 540, 1350, 34, GREY, k(t, st + 5.6, st + 5.9), stroke=None)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "A MARKET FALL =", "SIP DISCOUNT SEASON")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO PAUSED HIS SIP", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), aw(crash=3, mouth='grit', squint=0.3, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_stop, 'red'),
        (s(2), s(3), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_units, 'studio'),
        (s(3), s(4), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_covid, 'red'),
        (s(4), s(5), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_back, 'money'),
        (s(5), s(6), aw(mouth='frown', squint=0.3), (1.9, 1000, 500), (2.0, 1000, 470), o_cheap, 'night'),
        (s(6), s(7), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_sale, 'studio'),
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
