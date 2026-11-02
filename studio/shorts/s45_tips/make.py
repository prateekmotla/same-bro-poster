import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s45_tips"
TG = (0.16, 0.63, 0.89)
CAPS = [
    "Guess: when a Telegram channel shouts 'BUY NOW', who is SELLING to you?",
    "Sid gets a tip: 'Target 2x, jaldi buy karo!' He buys. Next week: -40%.",
    "SEBI caught one such case: Unison Metals. Tips on Telegram channels with lakhs of members. Price shot up.",
    "At the same time, big holders were selling: their stake fell from 17% to under 2% in ONE month.",
    "Your buying was their EXIT. That's a PUMP AND DUMP.",
    "Same bro? 'Bhai, sure-shot tip hai, kisi ko mat batana'?",
    "Rule: free tip = red flag. Check if the adviser is SEBI-registered. Not registered? Leave the group.",
    "MORAL: If the tip is free, YOU are the exit.",
    "Send this to the friend in 10 'sure-shot tips' groups.",
]
HOOK = [("'BUY NOW!'", WHITE), ("WHO'S SELLING?", RED), ("TELEGRAM TIPS", YEL)]
SRC = "Source: SEBI final order, Unison Metals (Feb 2026)"
sh = None


def scene(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def chat(c, t, st, msgs, y0=930):
    """Telegram-style bubbles: (text, delay)."""
    S.rrect(c, 110, y0 - 70, 860, 90, 24); c.set_source_rgba(*TG, 0.95); c.fill()
    T(c, "SURE-SHOT CALLS 🔥".replace("🔥", ""), 540, y0 - 12, 42, WHITE, stroke=None)
    for i, (m, dt) in enumerate(msgs):
        a = k(t, st + dt, st + dt + 0.25)
        if a <= 0:
            continue
        y = y0 + 40 + i * 120
        S.rrect(c, 140, y, 800, 100, 24); c.set_source_rgba(0.12, 0.14, 0.2, 0.96 * a); c.fill()
        T(c, m, 180, y + 66, 44, WHITE, a, stroke=None, anchor="left")


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 820, 560)
    chat(c, t, st, [("BUY NOW!! Target 2x", 0.3), ("Last chance, jaldi!", 0.9)])
    if t > st + 2.4:
        K.stamp(c, t, st + 2.4, "WHO'S SELLING?", 540, 1290, RED, 56, -0.05)


def o_sid(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    T(c, "SID BUYS", 540, 970, 56, GRN, k(t, st + 0.3, st + 0.6), stroke=None)
    T(c, "NEXT WEEK", 540, 1080, 44, GREY, k(t, st + 2.4, st + 2.7), stroke=None)
    T(c, "-40%", 540, 1230, 130, RED, k(t, st + 2.8, st + 3.1), stroke=None)


def o_case(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "SEBI CASE", 540, 400, 70, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    T(c, "UNISON METALS", 540, 520, 84, WHITE, k(t, st + 0.5, st + 0.8), lw=10)
    S.rrect(c, 190, 600, 700, 90, 45); c.set_source_rgba(*TG, 0.95 * k(t, st + 1.4, st + 1.7)); c.fill()
    T(c, "tips to LAKHS of members", 540, 660, 44, WHITE, k(t, st + 1.4, st + 1.7), stroke=None)
    TR.line(c, t, st + 2.4, 200, 760, 680, 260, [0.1, 0.15, 0.2, 0.35, 0.55, 0.8, 0.95], col=GRN, dur=1.6)


def o_stake(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "BIG HOLDERS' STAKE", 540, 400, 66, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    K.hbar(c, t, st + 0.9, 140, 500, 800, 110, 0.85, GRN, "before", "17%")
    K.hbar(c, t, st + 2.4, 140, 680, 800, 110, 0.1, RED, "1 month later", "<2%")
    if t > st + 3.6:
        T(c, "THEY SOLD. INTO THE HYPE.", 540, 940, 54, YEL, k(t, st + 3.6, st + 3.9), lw=7)


def o_exit(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "YOUR BUY", 540, 480, 90, GRN, k(t, st + 0.2, st + 0.5), lw=10)
    T(c, "=", 540, 600, 90, WHITE, k(t, st + 0.6, st + 0.9), lw=10)
    T(c, "THEIR EXIT", 540, 730, 100, RED, k(t, st + 0.9, st + 1.2), lw=12)
    K.stamp(c, t, st + 2.0, "PUMP & DUMP", 540, 900, YEL, 70, -0.05)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("'SURE-SHOT TIP HAI'", WHITE, 56, 0.2), ("'KISI KO MAT BATANA'", YEL, 56, 1.0)], y0=1000, gap=110)
    K.stamp(c, t, st + 2.0, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Free tip = RED FLAG", RED, 44, 0.5, "left", 140),
                      ("2. Check: SEBI-registered?", WHITE, 44, 2.0, "left", 140),
                      ("3. Not registered? LEAVE", GRN, 44, 4.0, "left", 140)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "IF THE TIP IS FREE,", "YOU ARE THE EXIT", RED)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "IN 10 'SURE-SHOT' GROUPS", YEL)


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
        (s(2), s(3), aw(crash=3, mouth='frown', squint=0.4, **ph), (2.0, 1000, 470), (2.15, 1000, 450), o_sid, 'red'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_case, 'studio'),
        (s(4), s(5), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_stake, 'money'),
        (s(5), s(6), sw(mouth='grit'), (1.78, 960, 540), (1.85, 960, 520), o_exit, 'red'),
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
