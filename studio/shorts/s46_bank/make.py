import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s46_bank"
CAPS = [
    "Guess: your bank pays you about 2.5% on savings. What does it charge your friend for a loan?",
    "Sid has ₹1 lakh in savings. 'Safe hai, bank mein hai.' Interest: about ₹2,500 a year.",
    "Same day, the bank lends that money to Rohan as a personal loan. At 10 to 15%.",
    "Pays you 2.5%. Charges 10%+. That gap, the SPREAD, is how banks earn.",
    "Your idle money isn't sleeping. It's working. For the BANK.",
    "Same bro? All your money sitting in a savings account?",
    "Rule: keep 3 to 6 months of expenses in savings for emergencies. Make a plan for the rest, once you understand it.",
    "MORAL: Idle money works too. Just not for you.",
    "Send this to the friend whose whole salary sleeps in savings.",
]
HOOK = [("YOUR BANK", WHITE), ("PAYS YOU 2.5%", GRN), ("THEN CHARGES 10%+", RED)]
SRC = "Source: SBI savings ~2.5%, personal loan 10-15% (SBI, 2026)"
sh = None


def scene(c, t, lt, **kw):
    V.room(c, t, 'day', fan=True)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def street(c, t, lt, **kw):
    V.street(c, t, 0.0, night=False)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def bank(c, x, y, s, a=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.move_to(-170, -150); c.line_to(0, -240); c.line_to(170, -150); c.close_path()
    c.set_source_rgba(0.85, 0.85, 0.9, a); c.fill()
    for i in range(4):
        S.rrect(c, -140 + i * 80, -140, 40, 150, 6); c.set_source_rgba(0.85, 0.85, 0.9, a); c.fill()
    S.rrect(c, -180, 10, 360, 30, 6); c.set_source_rgba(0.85, 0.85, 0.9, a); c.fill()
    T(c, "BANK", 0, -165, 40, (0.1, 0.1, 0.15), a, stroke=None)
    c.restore()


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 480)
    T(c, "YOU GET", 300, 980, 44, GREY, k(t, st + 0.2, st + 0.5), stroke=None)
    T(c, "2.5%", 300, 1120, 110, GRN, k(t, st + 0.4, st + 0.7), stroke=None)
    T(c, "FRIEND PAYS", 780, 980, 44, GREY, k(t, st + 2.4, st + 2.7), stroke=None)
    T(c, "??%", 780, 1120, 110, RED, k(t, st + 2.6, st + 2.9), stroke=None)
    T(c, "SAVINGS vs LOAN", 540, 1270, 46, YEL, k(t, st + 3.2, st + 3.5), stroke=None)


def o_sid(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 480)
    T(c, "SAVINGS: ₹1,00,000", 540, 990, 60, WHITE, k(t, st + 0.2, st + 0.5), stroke=None)
    T(c, "interest a year", 540, 1090, 44, GREY, k(t, st + 2.6, st + 2.9), stroke=None)
    T(c, "~₹2,500", 540, 1230, 110, GRN, k(t, st + 3.0, st + 3.3), stroke=None)


def o_lend(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    bank(c, 540, 650, 1.2, k(t, st + 0.1, st + 0.4))
    T(c, "> PERSONAL LOAN", 540, 860, 64, WHITE, k(t, st + 0.9, st + 1.2), lw=8)
    T(c, "10 - 15%", 540, 1020, 140, RED, k(t, st + 1.8, st + 2.1), lw=14)


def o_spread(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "THE SPREAD", 540, 400, 72, YEL, k(t, st + 0.1, st + 0.4), lw=9)
    K.hbar(c, t, st + 0.5, 140, 500, 800, 110, 0.2, GRN, "pays you", "2.5%")
    K.hbar(c, t, st + 1.6, 140, 680, 800, 110, 0.8, RED, "charges", "10%+")
    if t > st + 3.0:
        T(c, "THE GAP = BANK'S PROFIT", 540, 940, 56, YEL, k(t, st + 3.0, st + 3.3), lw=7)


def o_idle(c, t, lt):
    st = sh.s(5)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("YOUR IDLE MONEY", WHITE, 56, 0.2), ("IS WORKING...", GRN, 60, 1.6), ("FOR THE BANK", RED, 70, 2.6)], y0=990, gap=110)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("ALL MONEY IN", WHITE, 60, 0.2), ("SAVINGS A/C?", YEL, 70, 0.8)], y0=1000, gap=110)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Savings = 3-6 months", WHITE, 44, 0.5, "left", 140),
                      ("    of expenses (emergency)", GREY, 40, 0.5, "left", 140),
                      ("2. The rest: make a PLAN", GRN, 44, 3.2, "left", 140),
                      ("    you understand", GREY, 40, 3.2, "left", 140)], y0=1060, gap=82)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "IDLE MONEY WORKS TOO.", "JUST NOT FOR YOU", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "SALARY SLEEPS IN SAVINGS", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    stw = lambda **kw: (lambda c, t, lt: street(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), rw(mouth='o', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'warm'),
        (s(2), s(3), rw(mouth='smile', **ph), (2.0, 1000, 470), (2.15, 1000, 450), o_sid, 'warm'),
        (s(3), s(4), sw(mouth='o'), (1.78, 960, 540), (1.85, 960, 520), o_lend, 'red'),
        (s(4), s(5), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_spread, 'money'),
        (s(5), s(6), stw(mouth='frown', squint=0.3), (1.9, 1000, 480), (2.0, 1000, 460), o_idle, 'warm'),
        (s(6), s(7), rw(mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
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
