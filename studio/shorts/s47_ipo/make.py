import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s47_ipo"
CAPS = [
    "Guess: of 2025's hot IPOs, how many were BELOW their issue price by December?",
    "Sid applies to EVERY IPO. 'Listing gain pakka, sab kar rahe hain!'",
    "Grey market buzz. '100x oversubscribed!' Every WhatsApp group talking about it.",
    "2025: 103 IPOs listed. By year-end, 47 were BELOW the issue price. Nearly HALF.",
    "The hype is already in the price. And in many IPOs, old owners are selling THEIR shares to you.",
    "Same bro? 'Allotment mila toh lottery lag gayi'?",
    "Rule: read what the company does and why it's raising money. Can't explain it in 2 lines? Skip it.",
    "MORAL: Hype is not a business plan.",
    "Send this to the friend who applies to EVERY IPO.",
]
HOOK = [("HOT IPO?", WHITE), ("NEARLY HALF", RED), ("WENT BELOW PRICE", YEL)]
SRC = "Source: IANS data on 2025 listings (30 Dec 2025)"
sh = None


def scene(c, t, lt, crash=None, **kw):
    TR.desk(c, t, crash, mode="night", ticker="IPO WATCH")
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    TR.sid(c, t, 1000, 330, 0.5, **d)


def canteen(c, t, lt, **kw):
    V.canteen(c, t)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "2025 IPOs", 540, 980, 60, WHITE, k(t, st + 0.2, st + 0.5), stroke=None)
    T(c, "BELOW ISSUE PRICE?", 540, 1100, 64, RED, k(t, st + 1.4, st + 1.7), stroke=None)
    T(c, "?? / 103", 540, 1240, 90, YEL, k(t, st + 2.4, st + 2.7), stroke=None)


def o_sid(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    K.rows(c, t, st, [("APPLY", GRN, 56, 0.2), ("APPLY", GRN, 56, 0.5), ("APPLY", GRN, 56, 0.8)], y0=980, gap=80)
    K.stamp(c, t, st + 1.8, "'LISTING GAIN PAKKA!'", 540, 1280, YEL, 52, -0.05)


def o_buzz(c, t, lt):
    st = sh.s(3)
    K.panel(c, 820, 560)
    msgs = [("GMP +₹120 🚀".replace("🚀", ""), 0.2), ("100x SUBSCRIBED!!", 1.4), ("Sab apply karo", 2.6)]
    for i, (m, dt) in enumerate(msgs):
        a = k(t, st + dt, st + dt + 0.25)
        if a > 0:
            S.rrect(c, 160, 880 + i * 150, 760, 110, 26); c.set_source_rgba(0.1, 0.45, 0.25, 0.95 * a); c.fill()
            T(c, m, 540, 952 + i * 150, 50, WHITE, a, stroke=None)


def o_data(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "2025: 103 IPOs LISTED", 540, 400, 66, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    for i in range(103):
        col, row = i % 13, i // 13
        x, y = 170 + col * 57, 480 + row * 57
        below = i >= 56
        a = k(t, st + 1.0 + i * 0.012, st + 1.2 + i * 0.012)
        c.arc(x, y, 22, 0, 2 * math.pi)
        c.set_source_rgba(*(RED if (below and t > st + 3.0) else GREY), a); c.fill()
    if t > st + 3.2:
        T(c, "47 BELOW ISSUE PRICE", 540, 1000, 66, RED, k(t, st + 3.2, st + 3.5), lw=8)
        T(c, "nearly HALF", 540, 1080, 52, YEL, k(t, st + 3.8, st + 4.1), lw=7)


def o_hype(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "HYPE = ALREADY", 540, 440, 76, WHITE, k(t, st + 0.2, st + 0.5), lw=9)
    T(c, "IN THE PRICE", 540, 540, 76, YEL, k(t, st + 0.5, st + 0.8), lw=9)
    T(c, "OLD OWNERS", 540, 740, 80, RED, k(t, st + 2.4, st + 2.7), lw=10)
    T(c, "> selling to YOU", 540, 850, 60, WHITE, k(t, st + 3.0, st + 3.3), lw=8)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("ALLOTMENT MILA", GRN, 60, 0.2), ("= LOTTERY?", YEL, 70, 0.9)], y0=1000, gap=110)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. What does it DO?", WHITE, 44, 0.5, "left", 140),
                      ("2. WHY raise money?", WHITE, 44, 1.8, "left", 140),
                      ("3. Can't say it in 2 lines?", RED, 44, 3.4, "left", 140),
                      ("    SKIP IT", GRN, 44, 4.2, "left", 140)], y0=1060, gap=82)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "HYPE IS NOT", "A BUSINESS PLAN")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO APPLIES TO EVERY IPO", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'tense'
    s = sh.s
    aw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    cw = lambda **kw: (lambda c, t, lt: canteen(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), aw(mouth='o', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'night'),
        (s(2), s(3), aw(mouth='bigsmile', **ph), (2.0, 1000, 470), (2.15, 1000, 450), o_sid, 'night'),
        (s(3), s(4), cw(mouth='smile', **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_buzz, 'warm'),
        (s(4), s(5), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_data, 'red'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_hype, 'studio'),
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
