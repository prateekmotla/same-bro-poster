import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s52_service"
CAPS = [
    "Guess: that 'service charge' on your restaurant bill... do you HAVE to pay it?",
    "Sid's bill: ₹1,800 food + ₹180 service charge. Paid without even looking.",
    "Rule: CCPA guidelines (July 2022) say no restaurant can force a service charge.",
    "March 2025: Delhi High Court upheld it. Forcing it = unfair trade practice.",
    "It's not a tax. It's a tip. YOU decide whether to pay.",
    "Same bro? Paid it every time thinking it's compulsory?",
    "Fix: politely ask them to remove it. They refuse? Complain to National Consumer Helpline 1915.",
    "MORAL: Read the bill before you pay it.",
    "Send this to the friend who always pays the bill.",
]
HOOK = [("SERVICE CHARGE?", WHITE), ("YOU DON'T", YEL), ("HAVE TO PAY IT", RED)]
SRC = "Source: CCPA guidelines 4 Jul 2022; Delhi HC, 28 Mar 2025 (NRAI/FHRAI v UoI)"
sh = None


def canteen(c, t, lt, **kw):
    V.canteen(c, t)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def bill(c, t, st, x0=150, y0=730, hi=False, cut=False):
    a = k(t, st + 0.1, st + 0.4)
    S.rrect(c, x0, y0, 780, 560, 18); c.set_source_rgba(0.98, 0.97, 0.93, 0.98 * a); c.fill()
    dark = (0.12, 0.12, 0.14)
    T(c, "TABLE 7 - BILL", 540, y0 + 70, 46, dark, a, stroke=None)
    rows = [("Food & drinks", "₹1,800", dark), ("CGST + SGST 5%", "₹90", dark), ("Service charge 10%", "₹180", RED if hi else dark)]
    for i, (l, v, col) in enumerate(rows):
        b = a * k(t, st + 0.4 + i * 0.5, st + 0.7 + i * 0.5)
        y = y0 + 170 + i * 90
        if hi and i == 2:
            S.rrect(c, x0 + 20, y - 50, 740, 72, 10); c.set_source_rgba(1, 0.85, 0.85, b); c.fill()
        T(c, l, x0 + 40, y, 40, col, b, stroke=None, anchor="left", bold=False)
        T(c, v, x0 + 740, y, 42, col, b, stroke=None, anchor="right")
        if cut and i == 2 and t > st + 1.0:
            g = k(t, st + 1.0, st + 1.5)
            c.move_to(x0 + 30, y - 12); c.line_to(x0 + 30 + 720 * g, y - 12)
            c.set_source_rgba(*RED, 1); c.set_line_width(8); c.stroke()
    c.move_to(x0 + 30, y0 + 420); c.line_to(x0 + 750, y0 + 420); c.set_source_rgba(0.7, 0.7, 0.7, a); c.set_line_width(3); c.stroke()
    T(c, "TOTAL", x0 + 40, y0 + 490, 46, dark, a, stroke=None, anchor="left")
    T(c, "₹1,890" if cut else "₹2,070", x0 + 740, y0 + 490, 52, GRN if cut else dark, a, stroke=None, anchor="right")


def o_guess(c, t, lt):
    st = sh.s(1)
    bill(c, t, st, hi=True)
    K.stamp(c, t, st + 2.6, "COMPULSORY?", 540, 1365, YEL, 58, -0.05)


def o_bill(c, t, lt):
    st = sh.s(2)
    bill(c, t, st, hi=True)
    K.stamp(c, t, st + 4.0, "PAID. DIDN'T READ.", 540, 1365, RED, 52, -0.05)


def o_rule(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "CCPA GUIDELINES", 540, 420, 64, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    T(c, "4 JULY 2022", 540, 510, 56, YEL, k(t, st + 0.5, st + 0.8), lw=8)
    K.rows(c, t, st, [("No restaurant can ADD", WHITE, 58, 2.6), ("service charge by default", WHITE, 52, 3.2),
                      ("or FORCE you to pay it", RED, 58, 4.4)], y0=720, gap=110)


def o_court(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "DELHI HIGH COURT", 540, 420, 64, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    T(c, "28 MARCH 2025", 540, 510, 56, YEL, k(t, st + 0.5, st + 0.8), lw=8)
    K.stamp(c, t, st + 2.8, "GUIDELINES UPHELD", 540, 700, GRN, 64, -0.04)
    K.rows(c, t, st, [("Forcing it =", WHITE, 54, 4.2), ("UNFAIR TRADE PRACTICE", RED, 60, 5.0)], y0=900, gap=105)


def o_tip(c, t, lt):
    st = sh.s(5)
    K.panel(c, 860, 480)
    K.rows(c, t, st, [("NOT A TAX.", WHITE, 70, 0.1), ("A TIP.", GRN, 80, 1.3), ("YOU DECIDE.", YEL, 64, 2.4)], y0=960, gap=125)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("PAID IT EVERY TIME,", WHITE, 56, 0.2), ("THOUGHT IT WAS A RULE?", YEL, 54, 0.9)], y0=1000, gap=110)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(7)
    bill(c, t, st - 0.3, y0=420, cut=True)
    K.panel(c, 1020, 400, a=0.94)
    T(c, "THE FIX", 540, 1090, 58, YEL, stroke=None)
    K.rows(c, t, st, [("1. Ask politely: remove it", WHITE, 44, 0.8, "left", 130),
                      ("2. Refused? Call NCH 1915", WHITE, 44, 3.4, "left", 130),
                      ("   or complain on the NCH app", GREY, 38, 4.4, "left", 130)], y0=1190, gap=85)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "READ THE BILL", "BEFORE YOU PAY IT", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO ALWAYS PAYS THE BILL", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    cw = lambda **kw: (lambda c, t, lt: canteen(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), cw(mouth='o', eyes=1.2), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'warm'),
        (s(2), s(3), cw(mouth='smile'), (1.9, 1000, 480), (2.0, 1000, 460), o_bill, 'warm'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_rule, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_court, 'studio'),
        (s(5), s(6), cw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 470), o_tip, 'warm'),
        (s(6), s(7), cw(mouth='frown', squint=0.3), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), cw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, cw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
