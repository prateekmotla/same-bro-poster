import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s34_revenge"
CAPS = [
    "Sid loses ₹4,000 in one options trade. 'Abhi wapas nikalta hoon.' He DOUBLES the size.",
    "Trade 2: -₹9,000. Trade 3: even bigger. This is REVENGE TRADING.",
    "After a loss, your brain wants to 'win it back' FAST. So you trade bigger, with no plan.",
    "SEBI's study: over 75% of loss-making F&O traders kept trading anyway.",
    "FY22 to FY24: 1 crore+ traders lost about ₹2 lakh each, on average.",
    "Loss > anger > bigger bet > bigger loss. The cycle feeds itself.",
    "Rule: set a DAILY LOSS LIMIT. Hit it? Close the app. 2 losses in a row = done for the day.",
    "MORAL: The market doesn't owe you your money back.",
    "Send this to the friend who always says 'bas ek last trade'.",
]
HOOK = [("LOST ₹4,000?", WHITE), ("DON'T DOUBLE IT", RED), ("REVENGE TRADING", YEL)]
SRC = "Source: SEBI F&O study (Sep 2024)"
sh = None


def scene(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_loss1(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "TRADE 1", 540, 960, 48, GREY, stroke=None)
    K.rows(c, t, st, [("-₹4,000", RED, 110, 0.4)], y0=1110)
    K.stamp(c, t, st + 3.0, "SIZE x2", 540, 1280, YEL, 60, -0.05)


def o_loss2(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 500)
    K.rows(c, t, st, [("TRADE 2:  -₹9,000", RED, 64, 0.2), ("TRADE 3:  BIGGER...", RED, 64, 1.4)], y0=990, gap=110)
    K.stamp(c, t, st + 2.6, "REVENGE TRADING", 540, 1270, YEL, 56, 0.04)


def o_brain(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "AFTER A LOSS", 540, 420, 70, GREY, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "'WIN IT BACK", 540, 580, 104, RED, k(t, st + 0.8, st + 1.1), lw=12)
    T(c, "RIGHT NOW!'", 540, 710, 104, RED, k(t, st + 0.8, st + 1.1), lw=12)
    if t > st + 2.8:
        T(c, "bigger size + no plan", 540, 900, 60, YEL, k(t, st + 2.8, st + 3.1), lw=8)


def o_sebi(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "SEBI STUDY (FY22-FY24)", 540, 400, 62, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    T(c, "loss-making F&O traders", 540, 480, 44, GREY, k(t, st + 0.3, st + 0.6), lw=6)
    K.hbar(c, t, st + 1.0, 140, 640, 800, 90, 0.76, RED, "Kept trading", "75%+")
    if t > st + 2.6:
        T(c, "LOSS DIDN'T STOP THEM", 540, 900, 72, YEL, k(t, st + 2.6, st + 2.9), lw=9)


def o_avg(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "1 CRORE+ TRADERS", 540, 420, 80, WHITE, k(t, st + 0.3, st + 0.6), lw=10)
    T(c, "lost, on average", 540, 520, 50, GREY, k(t, st + 0.9, st + 1.2), lw=6)
    T(c, "₹2 LAKH", 540, 720, 170, RED, k(t, st + 1.4, st + 1.7), lw=16)
    T(c, "each, over 3 years", 540, 850, 50, WHITE, k(t, st + 2.0, st + 2.3), lw=6)


def o_cycle(c, t, lt):
    st = sh.s(6)
    U.dim(c, 0.88)
    T(c, "THE CYCLE", 540, 380, 70, YEL, k(t, st + 0.1, st + 0.4), lw=8)
    items = [("LOSS", RED), ("ANGER", (1, 0.55, 0.2)), ("BIGGER BET", YEL), ("BIGGER LOSS", RED)]
    cx, cy, r = 540, 760, 260
    for i, (txt, col) in enumerate(items):
        a = k(t, st + 0.5 + i * 0.7, st + 0.8 + i * 0.7)
        ang = -math.pi / 2 + i * math.pi / 2
        x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
        if a > 0:
            S.rrect(c, x - 145, y - 50, 290, 100, 50); c.set_source_rgba(0.08, 0.08, 0.12, 0.95 * a); c.fill()
            T(c, txt, x, y + 16, 42, col, a, stroke=None)
    rot = (t - st) * 1.5
    c.arc(cx, cy, 70, rot, rot + 4.5); c.set_source_rgba(*RED, 0.8 * k(t, st + 3.0, st + 3.3)); c.set_line_width(12); c.stroke()


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Fix a DAILY loss limit", WHITE, 42, 0.8, "left", 130),
                      ("2. Limit hit? CLOSE the app", RED, 42, 2.2, "left", 130),
                      ("3. 2 losses in a row = stop", GRN, 42, 3.6, "left", 130)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "THE MARKET DOESN'T", "OWE YOU ANYTHING")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "'BAS EK LAST TRADE'", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), aw(crash=2, mouth='grit', squint=0.3, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_loss1, 'red'),
        (s(2), s(3), aw(crash=3, mouth='frown', squint=0.5, **ph), (1.9, 1000, 480), (2.0, 1000, 460), o_loss2, 'red'),
        (s(3), s(4), sw(mouth='grit'), (1.78, 960, 540), (1.85, 960, 520), o_brain, 'studio'),
        (s(4), s(5), sw(), (1.78, 960, 540), (1.85, 960, 520), o_sebi, 'studio'),
        (s(5), s(6), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_avg, 'red'),
        (s(6), s(7), aw(crash=2, mouth='frown', squint=0.4), (1.9, 1000, 500), (2.0, 1000, 470), o_cycle, 'red'),
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
