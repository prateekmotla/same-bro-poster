import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s63_upifail"
CAPS = [
    "UPI failed but money got debited? If the bank is late, it owes YOU ₹100 a day.",
    "Sid paid the chai guy. 'FAILED'. But the money left his account.",
    "RBI rule: failed UPI money must come back by the NEXT working day.",
    "After that, ₹100 compensation for EVERY day of delay. Automatic. For ATMs, the limit is 5 days.",
    "Same bro? On hold with customer care for 3 days?",
    "Fix: complain in the app with the transaction ID. No reply from the bank in 30 days? RBI Ombudsman: cms.rbi.org.in",
    "MORAL: Your time is money too. It's written in the rules.",
    "Send this to the friend whose money always gets stuck.",
]
HOOK = [("UPI FAILED,", WHITE), ("MONEY CUT?", YEL), ("RULES #1", GREY)]
SRC = "Source: RBI circular on TAT for failed transactions, 20 Sep 2019"
sh = None
BLUE = (0.26, 0.52, 0.96)


def fail_scr(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
    c.arc(w / 2, 260, 90, 0, 2 * math.pi); c.set_source_rgb(*RED); c.fill()
    T(c, "X", w / 2, 290, 90, WHITE, stroke=None)
    T(c, "Payment FAILED", w / 2, 440, 44, RED, stroke=None)
    T(c, "₹20 to Chai Stall", w / 2, 510, 32, (0.3, 0.3, 0.35), stroke=None, bold=False)
    S.rrect(c, 30, 600, w - 60, 150, 20); c.set_source_rgb(1, 0.93, 0.92); c.fill()
    T(c, "A/c debited ₹20", w / 2, 665, 34, (0.6, 0.1, 0.1), stroke=None)
    T(c, "Bal: ₹1,480", w / 2, 720, 30, (0.4, 0.3, 0.3), stroke=None, bold=False)


def stw(night=False, **kw):
    def f(c, t, lt):
        V.street(c, t, off=t * 20, night=night)
        d = dict(pose='stand', mouth='flat')
        d.update(kw)
        K.sid(c, t, 1000, 330, 0.5, **d)
    return f


def rw(mode='day', **kw):
    def f(c, t, lt):
        V.room(c, t, mode, fan=False)
        d = dict(pose='stand', mouth='flat')
        d.update(kw)
        K.sid(c, t, 1000, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def o_hook(c, t, lt):
    st = sh.s(1)
    K.panel(c, 1010, 340)
    K.rows(c, t, st, [("BANK LATE?", WHITE, 60, 0.2), ("IT OWES YOU ₹100/DAY", YEL, 62, 2.6)], y0=1120, gap=120)


def o_fail(c, t, lt):
    st = sh.s(2)
    U.phone_frame(c, 290, 470, 500, 800, fail_scr, t - st, tilt=-2 + 3 * lt)
    K.stamp(c, t, st + 2.6, "MONEY GONE?!", 540, 1350, RED, 54, -0.05)


def o_rule(c, t, lt):
    st = sh.s(3)
    K.full(c, t, st, [("RBI RULE", GREY, 60, 0.1), ("FAILED UPI REFUND", WHITE, 64, 1.0), ("BY NEXT", YEL, 120, 2.2),
                      ("WORKING DAY", YEL, 100, 2.6)], y0=520, gap=170)


def o_comp(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "LATE AFTER THAT?", 540, 470, 60, WHITE, k(t, st + 0.1, st + 0.4), lw=8)
    for i in range(4):
        a = k(t, st + 0.8 + i * 0.6, st + 1.1 + i * 0.6)
        if a > 0:
            S.rrect(c, 150, 560 + i * 120, 780, 96, 20); c.set_source_rgba(0.12, 0.3, 0.18, a); c.fill()
            T(c, f"DAY {i + 1} LATE", 190, 625 + i * 120, 44, WHITE, a, stroke=None, anchor="left")
            T(c, "+₹100", 890, 625 + i * 120, 50, GRN, a, stroke=None, anchor="right")
    K.stamp(c, t, st + 4.4, "ATM: LIMIT 5 DAYS", 540, 1150, BLUE, 50, -0.03)


def o_same(c, t, lt):
    st = sh.s(5)
    K.panel(c, 900, 420)
    K.rows(c, t, st, [("3 DAYS ON HOLD", WHITE, 60, 0.3), ("WITH CUSTOMER CARE?", YEL, 56, 1.0)], y0=1010, gap=110)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1250, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(6)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Complain in the app", WHITE, 48, 0.3, "left", 140),
                      ("    with the transaction ID", WHITE, 44, 0.3, "left", 140),
                      ("2. No reply in 30 days?", WHITE, 48, 3.0, "left", 140),
                      ("3. RBI Ombudsman:", GRN, 48, 4.6, "left", 140),
                      ("    cms.rbi.org.in", GRN, 48, 4.6, "left", 140)], y0=1000, gap=76)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(7), "YOUR TIME = MONEY.", "IT'S IN THE RULES.", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WITH STUCK UPI MONEY", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (60, 120)))
    sh.shots = [
        (0, s(2), stw(mouth='o', eyes=1.3, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), stw(mouth='frown', angry=0.6, **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_fail, 'red'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_rule, 'studio'),
        (s(4), s(5), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_comp, 'money'),
        (s(5), s(6), rw(mouth='frown', sweat=1, **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(6), s(7), rw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(7), s(8), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(8), sh.dur + 1, stw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
