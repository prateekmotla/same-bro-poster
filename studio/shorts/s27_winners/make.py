import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s27_winners"
CAPS = [
    "Sid's stock is up 10%. He sells it FAST. 'Profit is profit, bro!'",
    "Another stock is down 30%. He holds it for years. 'Wapas aayega.'",
    "This trap has a name: the DISPOSITION EFFECT. Your brain hates booking a loss.",
    "A study of 10,000 trading accounts: a winner was almost 60% MORE likely to be sold than a loser.",
    "So the winners leave early, and the portfolio slowly fills up with losers.",
    "A study of Finnish investors put the cost at about 3% to 6% of returns.",
    "Rule: write your exit BEFORE you buy. Sell when your reason breaks, not when you feel OK.",
    "MORAL: Cut your losers, let your winners run.",
    "Send this to the friend whose 'long-term' stocks are all red.",
]
HOOK = [("SELL WINNERS,", WHITE), ("KEEP LOSERS?", RED), ("THE BRAIN TRAP", YEL)]
SRC = "Source: Odean (1998); Seru, Shumway & Stoffman"
sh = None


def scene(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)





def o_win(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "STOCK A", 540, 960, 48, GREY, stroke=None)
    K.rows(c, t, st, [("+10%", GRN, 110, 0.4)], y0=1120)
    K.stamp(c, t, st + 2.4, "SOLD!", 540, 1280, GRN, 56)


def o_lose(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    T(c, "STOCK B", 540, 960, 48, GREY, stroke=None)
    K.rows(c, t, st, [("-30%", RED, 110, 0.4)], y0=1120)
    K.stamp(c, t, st + 2.4, "HOLD FOR YEARS", 540, 1280, RED, 48, 0.05)


def o_name(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "IT HAS A NAME", 540, 420, 64, GREY, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "DISPOSITION", 540, 600, 110, YEL, k(t, st + 0.8, st + 1.1), lw=12)
    T(c, "EFFECT", 540, 730, 110, YEL, k(t, st + 0.8, st + 1.1), lw=12)
    if t > st + 2.6:
        T(c, "booking a loss = admitting", 540, 930, 50, WHITE, k(t, st + 2.6, st + 2.9), lw=6)
        T(c, "you were wrong. Brain says NO.", 540, 1000, 50, WHITE, k(t, st + 2.6, st + 2.9), lw=6)


def o_study(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "10,000 ACCOUNTS STUDIED", 540, 400, 62, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    T(c, "Odean, 1998 (US broker data)", 540, 470, 38, GREY, k(t, st + 0.3, st + 0.6), lw=6)
    T(c, "share of gains vs losses sold", 540, 590, 36, GREY, k(t, st + 1.0, st + 1.3), lw=5)
    K.hbar(c, t, st + 1.4, 140, 720, 800, 80, 0.148 / 0.16, GRN, "Winners sold", "14.8%")
    K.hbar(c, t, st + 2.6, 140, 930, 800, 80, 0.098 / 0.16, RED, "Losers sold", "9.8%")
    if t > st + 4.4:
        T(c, "~60% MORE LIKELY", 540, 1170, 84, YEL, k(t, st + 4.4, st + 4.7), lw=10)


def o_fill(c, t, lt):
    st = sh.s(5)
    K.panel(c, 870, 500)
    T(c, "SID'S PORTFOLIO", 540, 950, 48, GREY, stroke=None)
    for i in range(6):
        dt = 0.5 + i * 0.45
        a = k(t, st + dt, st + dt + 0.2)
        red = i >= 1
        col = RED if (red and t > st + 1.0 + i * 0.45) else GRN
        if a > 0:
            S.rrect(c, 150 + i * 135, 1040, 110, 150, 18); c.set_source_rgba(*col, a); c.fill()
            T(c, "-" if col == RED else "+", 205 + i * 135, 1140, 70, WHITE, a, stroke=None)
    if t > st + 3.6:
        T(c, "MOSTLY RED", 540, 1300, 70, RED, k(t, st + 3.6, st + 3.9), stroke=None)


def o_cost(c, t, lt):
    st = sh.s(6)
    U.dim(c, 0.88)
    T(c, "THE COST", 540, 420, 70, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    T(c, "3% to 6%", 540, 640, 150, RED, k(t, st + 1.2, st + 1.5), lw=14)
    T(c, "of your returns", 540, 760, 60, YEL, k(t, st + 1.6, st + 1.9), lw=8)
    T(c, "study of Finnish investors", 540, 860, 38, GREY, k(t, st + 1.6, st + 1.9), lw=5)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Write your exit BEFORE buying", WHITE, 40, 0.8, "left", 130),
                      ("2. Reason broke? Cut the loser", GRN, 40, 2.2, "left", 130),
                      ("3. Reason intact? Let it run", WHITE, 40, 3.6, "left", 130)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "CUT YOUR LOSERS,", "LET WINNERS RUN")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WITH ALL-RED 'LONG TERM'", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), aw(mouth='bigsmile', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_win, 'night'),
        (s(2), s(3), aw(crash=3, mouth='grit', squint=0.3, **ph), (1.9, 1000, 480), (2.0, 1000, 460), o_lose, 'red'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_name, 'studio'),
        (s(4), s(5), sw(), (1.78, 960, 540), (1.85, 960, 520), o_study, 'studio'),
        (s(5), s(6), aw(crash=2, mouth='frown', squint=0.4), (1.9, 1000, 500), (2.0, 1000, 470), o_fill, 'red'),
        (s(6), s(7), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_cost, 'studio'),
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
