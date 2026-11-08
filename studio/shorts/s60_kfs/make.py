import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s60_kfs"
CAPS = [
    "Guess: a loan app says '0% INTEREST'. So the loan is free?",
    "Sid buys a phone on a '0% EMI' loan through an app. Then the bill: processing fee, convenience fee, GST...",
    "Rule: since 1 Oct 2024, RBI makes every bank / NBFC give a KEY FACT STATEMENT (KFS) with every retail loan.",
    "It must show the APR (Annual Percentage Rate): the loan's REAL cost, all fees included.",
    "And a fee NOT written in the KFS can't be charged without your explicit consent.",
    "Same bro? Saw '0%' and hit 'I agree' without reading?",
    "Fix: ask for the KFS before you sign. Ignore '0%', look at the APR. Compare loans by APR.",
    "MORAL: 0% interest is not 0% cost.",
    "Send this to the friend who buys everything on EMI.",
]
HOOK = [("'0% INTEREST'", WHITE), ("SO IT'S", YEL), ("FREE?", RED)]
SRC = "Source: RBI circular on Key Facts Statement (15 Apr 2024), effective 1 Oct 2024"
sh = None


def emi_scr(show):
    items = [("Phone", "0% EMI", (0.1, 0.55, 0.25)), ("Processing fee", "+ ₹₹₹", (0.8, 0.2, 0.2)),
             ("Convenience fee", "+ ₹₹", (0.8, 0.2, 0.2)), ("GST on fees", "+ ₹", (0.8, 0.2, 0.2))]

    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.98); c.fill()
        c.rectangle(0, 0, w, 120); c.set_source_rgb(0.35, 0.2, 0.7); c.fill()
        T(c, "EMI SUMMARY", w / 2, 80, 38, WHITE, stroke=None)
        for i, (a, b, col) in enumerate(items[:show]):
            y = 210 + i * 110
            T(c, a, 40, y, 32, (0.15, 0.15, 0.2), stroke=None, anchor="left")
            T(c, b, w - 40, y, 32, col, stroke=None, anchor="right")
            c.rectangle(30, y + 40, w - 60, 2); c.set_source_rgb(0.85, 0.85, 0.88); c.fill()
        S.rrect(c, 60, h - 150, w - 120, 90, 20); c.set_source_rgb(0.35, 0.2, 0.7); c.fill()
        T(c, "I AGREE", w / 2, h - 92, 36, WHITE, stroke=None)
    return f


def kfs_scr(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.98, 0.97, 0.94); c.fill()
    T(c, "KEY FACT STATEMENT", w / 2, 80, 34, (0.1, 0.1, 0.15), stroke=None)
    rows = ["Loan amount", "Interest rate", "Processing fee", "Other charges", "Cooling-off period"]
    for i, r in enumerate(rows):
        y = 160 + i * 75
        T(c, r, 40, y, 26, (0.3, 0.3, 0.35), stroke=None, anchor="left")
        S.rrect(c, w - 200, y - 22, 160, 30, 6); c.set_source_rgb(0.85, 0.85, 0.85); c.fill()
    S.rrect(c, 25, 560, w - 50, 130, 16); c.set_source_rgb(1, 0.9, 0.3); c.fill()
    T(c, "APR (all-in cost)", w / 2, 610, 34, (0.1, 0.1, 0.15), stroke=None)
    T(c, "= the REAL number", w / 2, 665, 30, (0.6, 0.1, 0.1), stroke=None)


def rw(mode='night', **kw):
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


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 900, 420)
    a = k(t, st + 0.6, st + 1.0)
    T(c, "0% INTEREST", 540, 1050, 90, GRN, a, lw=10)
    T(c, "= FREE LOAN?", 540, 1180, 62, YEL, k(t, st + 2.6, st + 2.9), stroke=None)


def o_bill(c, t, lt):
    st = sh.s(2)
    show = 1 + int(max(0, t - st - 3.0) / 1.0)
    U.phone_frame(c, 290, 520, 500, 860, emi_scr(min(4, show)), t - st, tilt=-2 + 3 * lt)


def o_rule(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "RBI RULE, SINCE 1 OCT 2024", 540, 420, 52, GREY, k(t, st + 0.1, st + 0.4), lw=7)
    K.rows(c, t, st, [("Every retail loan", WHITE, 60, 3.0), ("from a bank / NBFC", WHITE, 56, 4.0)], y0=580, gap=110)
    K.stamp(c, t, st + 6.0, "KEY FACT STATEMENT", 540, 900, YEL, 66, -0.03)


def o_apr(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    U.phone_frame(c, 290, 480, 500, 760, kfs_scr, t - st, tilt=0)
    K.stamp(c, t, st + 2.0, "LOOK HERE", 540, 1330, RED, 56, -0.05)


def o_consent(c, t, lt):
    st = sh.s(5)
    K.panel(c, 880, 480)
    K.rows(c, t, st, [("FEE NOT IN THE KFS?", WHITE, 56, 0.3), ("CAN'T BE CHARGED", YEL, 60, 2.0),
                      ("without your OK", GRN, 50, 3.4)], y0=990, gap=110)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("SAW '0%' AND HIT", WHITE, 58, 0.4), ("'I AGREE' UNREAD?", YEL, 58, 1.8)], y0=1000, gap=110)
    K.stamp(c, t, st + 2.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(7)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Ask for the KFS first", WHITE, 48, 0.3, "left", 140),
                      ("2. Ignore '0%', read APR", WHITE, 48, 2.6, "left", 140),
                      ("3. Compare loans by APR", GRN, 48, 4.8, "left", 140)], y0=1020, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "0% INTEREST", "IS NOT 0% COST.", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO BUYS EVERYTHING ON EMI", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'tense'
    s = sh.s
    sh.shots = [
        (0, s(2), rw(mouth='o', eyes=1.3), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'night'),
        (s(2), s(3), rw(mouth='frown', squint=0.3, phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 480), (2.05, 1000, 455), o_bill, 'night'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_rule, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_apr, 'money'),
        (s(5), s(6), rw('day', mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_consent, 'warm'),
        (s(6), s(7), rw(mouth='frown', phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'night'),
        (s(7), s(8), rw('day', mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw('day', mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
