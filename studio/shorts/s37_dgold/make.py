import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
import fest as F  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s37_dgold"
GOLD = F.GOLD
CAPS = [
    "Dhanteras offer: buy gold in an app for just ₹10! Sid instantly buys 'digital gold'.",
    "But wait. In Nov 2025, SEBI warned: digital gold is NOT regulated by SEBI.",
    "It's not a security. The govt is only DISCUSSING rules (like physical backing). Nothing final yet.",
    "So if the platform runs into trouble, SEBI's investor protection does NOT cover you.",
    "SEBI flagged counterparty + operational risk: you fully trust the seller and its vault.",
    "Regulated routes exist: gold ETFs, electronic gold receipts, exchange-traded gold contracts.",
    "Rule: before buying any 'gold', ask WHO REGULATES IT? No clear answer = no money.",
    "MORAL: Shiny app + unclear rules = real risk.",
    "Send this to the friend buying ₹10 gold this Dhanteras.",
]
HOOK = [("YOUR DIGITAL GOLD", WHITE), ("ISN'T REGULATED", RED), ("SEBI WARNED", YEL)]
SRC = "Source: SEBI press release (8 Nov 2025); Outlook Money"
sh = None


def scene(c, t, lt, **kw):
    F.room(c, t, lt, **kw)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def bar(c, x, y, w, h, a=1.0):
    c.move_to(x + 30, y); c.line_to(x + w - 30, y); c.line_to(x + w, y + h); c.line_to(x, y + h); c.close_path()
    c.set_source_rgba(*GOLD, a); c.fill()
    T(c, "999", x + w / 2, y + h * 0.68, h * 0.42, (0.5, 0.35, 0.05), a, stroke=None)


def o_offer(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 500)
    T(c, "DHANTERAS OFFER", 540, 960, 50, YEL, k(t, st + 0.2, st + 0.5), stroke=None)
    bar(c, 400, 1000, 280, 100, k(t, st + 0.5, st + 0.8))
    K.rows(c, t, st, [("GOLD FOR ₹10", WHITE, 70, 1.2)], y0=1190)
    K.stamp(c, t, st + 3.0, "BOUGHT!", 540, 1300, GRN, 50, -0.05)


def o_sebi(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "SEBI, NOV 2025", 540, 400, 64, GREY, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "DIGITAL GOLD", 540, 560, 104, GOLD, k(t, st + 0.8, st + 1.1), lw=12)
    K.stamp(c, t, st + 1.8, "NOT REGULATED BY SEBI", 540, 740, RED, 58, -0.03)


def o_rules(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "NOT A SECURITY", 540, 420, 80, WHITE, k(t, st + 0.2, st + 0.5), lw=10)
    T(c, "Govt: rules only", 540, 600, 66, YEL, k(t, st + 1.4, st + 1.7), lw=8)
    T(c, "BEING DISCUSSED", 540, 690, 66, YEL, k(t, st + 1.4, st + 1.7), lw=8)
    if t > st + 3.4:
        T(c, "nothing final yet", 540, 860, 60, RED, k(t, st + 3.4, st + 3.7), lw=8)


def o_protect(c, t, lt):
    st = sh.s(4)
    K.panel(c, 870, 500)
    T(c, "PLATFORM IN TROUBLE?", 540, 960, 50, GREY, stroke=None)
    K.rows(c, t, st, [("SEBI investor protection", WHITE, 50, 0.6)], y0=1080)
    K.stamp(c, t, st + 2.0, "DOESN'T COVER YOU", 540, 1230, RED, 56, 0.04)


def o_risk(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "SEBI FLAGGED", 540, 400, 64, GREY, k(t, st + 0.2, st + 0.5), lw=8)
    K.rows(c, t, st, [("COUNTERPARTY RISK", RED, 70, 0.7), ("OPERATIONAL RISK", RED, 70, 1.5)], y0=560, gap=120)
    if t > st + 3.0:
        T(c, "you trust: seller + its vault", 540, 900, 52, YEL, k(t, st + 3.0, st + 3.3), lw=6)


def o_routes(c, t, lt):
    st = sh.s(6)
    U.dim(c, 0.88)
    T(c, "REGULATED ROUTES", 540, 400, 74, GRN, k(t, st + 0.2, st + 0.5), lw=8)
    K.rows(c, t, st, [("Gold ETFs", WHITE, 62, 0.9), ("Electronic Gold Receipts", WHITE, 56, 1.9),
                      ("Exchange-traded gold contracts", WHITE, 46, 2.9)], y0=560, gap=120)
    if t > st + 4.0:
        T(c, "(categories, not advice)", 540, 960, 36, GREY, k(t, st + 4.0, st + 4.3), stroke=None)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "GOLD RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("Ask: WHO REGULATES IT?", WHITE, 50, 0.8), ("Clear answer > consider", GRN, 46, 2.2),
                      ("No answer > NO money", RED, 46, 3.4)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "SHINY APP +", "UNCLEAR RULES = RISK")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "BUYING ₹10 GOLD", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: scene(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), rw(mouth='bigsmile', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_offer, 'warm'),
        (s(2), s(3), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_sebi, 'red'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_rules, 'studio'),
        (s(4), s(5), rw(mouth='frown', squint=0.3, **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_protect, 'warm'),
        (s(5), s(6), sw(), (1.78, 960, 540), (1.85, 960, 520), o_risk, 'studio'),
        (s(6), s(7), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_routes, 'money'),
        (s(7), s(8), rw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw(mouth='bigsmile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
