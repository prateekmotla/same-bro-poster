import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s51_forex"
ORG = (1.0, 0.6, 0.15)
CAPS = [
    "Guess: F&O didn't work out, so forex or Bitcoin will be EASIER?",
    "Sid lost in Nifty options. Now: 'Forex is stable bhai, Bitcoin runs 24x7!'",
    "Reality: in Europe's forex & CFD data, 74-89% of retail accounts LOSE money.",
    "Bitcoin? Swings even harder. And in India, forex on foreign apps isn't even LEGAL. RBI keeps an alert list.",
    "New market, same mistakes. You didn't fix the skill. You just changed the ground.",
    "Same bro? Lost in one market, jumped to the next?",
    "Rule: master ONE market first: a plan, a stop-loss, one year of records. Then explore others slowly, legally, small.",
    "MORAL: Changing the market won't change the trader.",
    "Send this to the friend who just jumped to forex.",
]
HOOK = [("LOST IN F&O?", WHITE), ("FOREX / BITCOIN", ORG), ("WON'T SAVE YOU", RED)]
SRC = "Source: ESMA retail CFD data; RBI Alert List (Nov 2025)"
sh = None


def scene(c, t, lt, crash=None, ticker="NIFTY 50", **kw):
    TR.desk(c, t, crash, ticker=ticker)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def tile(c, x, y, w, txt, col, a):
    S.rrect(c, x - w / 2, y - 55, w, 110, 26); c.set_source_rgba(0.1, 0.11, 0.17, 0.95 * a); c.fill()
    T(c, txt, x, y + 18, 50, col, a, stroke=None)


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "F&O", 540, 990, 70, RED, k(t, st + 0.2, st + 0.5), stroke=None)
    tile(c, 320, 1130, 340, "FOREX?", BLUE, k(t, st + 1.2, st + 1.5))
    tile(c, 760, 1130, 340, "BITCOIN?", ORG, k(t, st + 1.6, st + 1.9))
    K.stamp(c, t, st + 2.6, "EASIER?", 540, 1290, YEL, 60, -0.05)


def o_sid(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    T(c, "NIFTY OPTIONS: -₹8,000", 540, 990, 54, RED, k(t, st + 0.2, st + 0.5), stroke=None)
    K.stamp(c, t, st + 2.0, "'FOREX IS STABLE!'", 540, 1120, BLUE, 54, -0.04)
    K.stamp(c, t, st + 3.4, "'BTC 24x7!'", 540, 1260, ORG, 54, 0.04)


def o_esma(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.9)
    T(c, "FOREX & CFD, RETAIL", 540, 400, 64, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "accounts that LOSE money", 540, 490, 48, GREY, k(t, st + 0.6, st + 0.9), lw=6)
    T(c, "74-89%", 540, 720, 200, RED, k(t, st + 1.6, st + 1.9), lw=18)
    T(c, "(EU regulator data)", 540, 850, 44, YEL, k(t, st + 2.6, st + 2.9), lw=6)


def o_btc(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "BITCOIN", 540, 390, 70, ORG, k(t, st + 0.1, st + 0.4), lw=9)
    TR.line(c, t, st + 0.4, 150, 430, 780, 260, [0.3, 0.8, 0.2, 0.9, 0.35, 0.75, 0.1, 0.6], col=ORG, dur=1.6)
    T(c, "INDIA: FOREX ON FOREIGN APPS", 540, 800, 50, WHITE, k(t, st + 2.4, st + 2.7), lw=7)
    K.stamp(c, t, st + 3.0, "NOT LEGAL", 540, 920, RED, 76, -0.05)
    if t > st + 4.4:
        T(c, "RBI ALERT LIST", 540, 1040, 52, YEL, k(t, st + 4.4, st + 4.7), lw=7)


def o_ground(c, t, lt):
    st = sh.s(5)
    K.panel(c, 820, 560)
    K.rows(c, t, st, [("NEW MARKET", BLUE, 60, 0.2), ("SAME MISTAKES", RED, 70, 1.0),
                      ("skill not fixed,", WHITE, 46, 2.4), ("just the ground changed", WHITE, 46, 3.0)], y0=920, gap=110)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("F&O > FOREX > BTC > ...", WHITE, 54, 0.2), ("lose, jump, repeat", RED, 54, 1.0)], y0=1000, gap=110)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Master ONE market first", WHITE, 42, 0.5, "left", 130),
                      ("2. Plan + stop-loss + 1 yr record", GRN, 40, 1.8, "left", 130),
                      ("3. Then others: slow, LEGAL,", WHITE, 42, 4.2, "left", 130),
                      ("    and SMALL", WHITE, 42, 4.2, "left", 130)], y0=1060, gap=82)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "NEW MARKET WON'T", "CHANGE THE TRADER")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO JUST JUMPED TO FOREX", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'tense'
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), aw(crash=2, mouth='o', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'night'),
        (s(2), s(3), aw(crash=3, ticker="USD/INR", mouth='bigsmile', **ph), (2.0, 1000, 470), (2.15, 1000, 450), o_sid, 'night'),
        (s(3), s(4), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_esma, 'red'),
        (s(4), s(5), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_btc, 'studio'),
        (s(5), s(6), aw(crash=3, ticker="BTC/USD", mouth='frown', squint=0.4, **ph), (1.9, 1000, 480), (2.0, 1000, 460), o_ground, 'red'),
        (s(6), s(7), aw(mouth='smirk', **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'night'),
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
