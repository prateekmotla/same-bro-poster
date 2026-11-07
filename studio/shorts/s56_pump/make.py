import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s56_pump"
CAPS = [
    "Guess: that highway petrol pump toilet. Is it only for the staff?",
    "Long road trip. Sid stops at a pump, asks for the toilet. Staff: 'Bhai, not for public.'",
    "Rule: oil company dealer norms say EVERY petrol pump must give these FREE: air, drinking water, a clean toilet, a phone, a first-aid box.",
    "Not a joke: a Kerala consumer commission made a pump dealer pay ₹1.5 lakh compensation for refusing the toilet.",
    "Toilet locked? Charged for air? That's the dealer's fault, not yours.",
    "Same bro? Filled petrol, then held it till the next dhaba?",
    "Fix: ask politely. Refused? Ask for the complaint book (every pump must keep one). Then complain on the oil company portal or CPGRAMS.",
    "MORAL: You pay for the petrol. Air, water and the toilet are free.",
    "Send this to the friend who's always hunting for a toilet on road trips.",
]
HOOK = [("PETROL PUMP", WHITE), ("TOILET =", YEL), ("STAFF ONLY?", RED)]
SRC = "Source: Lok Sabha USQ 812 (Jul 2025); Pathanamthitta DCDRC (Apr 2025)"
sh = None
DK = (0.12, 0.12, 0.14)


def pump(c, t, lock=False, night=True):
    box, text, light, lg = V.box, V.text, V.light, V.lingrad
    sky = [(0, (0.04, 0.05, 0.12)), (1, (0.2, 0.12, 0.22))] if night else [(0, (0.55, 0.75, 0.95)), (1, (0.95, 0.85, 0.7))]
    c.set_source(lg(c, 0, 0, 0, 800, sky)); c.rectangle(0, 0, V.W, V.H); c.fill()
    # far highway trees / hills
    for i in range(12):
        x = i * 180 - 40
        c.arc(x, 700, 120 + (i * 37 % 60), 3.14, 6.28)
        c.set_source_rgb(*((0.05, 0.08, 0.08) if night else (0.35, 0.5, 0.35))); c.fill()
    # forecourt ground
    box(c, 0, 760, V.W, 320, (0.32, 0.32, 0.34) if night else (0.6, 0.6, 0.62))
    for i in range(8):
        box(c, i * 260, 900, 160, 10, (0.85, 0.75, 0.2))
    # canopy
    box(c, 560, 60, 900, 40, (0.92, 0.92, 0.94))
    box(c, 560, 100, 900, 70, (0.85, 0.15, 0.15))
    box(c, 560, 170, 900, 14, (0.15, 0.25, 0.7))
    text(c, "FUEL  STATION  24x7", 1010, 150, 44, WHITE)
    for x in (640, 860, 1160, 1380):
        box(c, x - 40, 184, 80, 10, (1, 0.98, 0.85))
        if night:
            light(c, x, 260, 260, (1, 0.95, 0.8), 0.22)
    box(c, 600, 184, 26, 600, (0.85, 0.85, 0.88))
    box(c, 1400, 184, 26, 600, (0.85, 0.85, 0.88))
    # dispenser (left of Sid)
    box(c, 690, 420, 170, 380, (0.95, 0.95, 0.96), 10)
    box(c, 690, 420, 170, 60, (0.85, 0.15, 0.15), 10)
    text(c, "PETROL", 775, 462, 26, WHITE)
    box(c, 710, 500, 130, 70, (0.05, 0.08, 0.06), 6)
    text(c, "₹ 1500.00", 775, 545, 24, (0.3, 1, 0.5))
    box(c, 710, 590, 130, 50, (0.05, 0.08, 0.06), 6)
    text(c, "14.58 L", 775, 625, 22, (0.3, 1, 0.5))
    c.move_to(860, 600); c.curve_to(920, 640, 900, 760, 880, 800)
    c.set_source_rgb(0.1, 0.1, 0.1); c.set_line_width(10); c.stroke()
    # toilet block (right of Sid)
    box(c, 1150, 300, 260, 480, (0.78, 0.72, 0.62))
    box(c, 1190, 420, 150, 360, (0.35, 0.45, 0.6), 6)
    box(c, 1165, 330, 230, 60, (0.15, 0.4, 0.75), 6)
    text(c, "TOILET", 1280, 372, 34, WHITE)
    box(c, 1310, 590, 14, 30, (0.85, 0.75, 0.3), 3)
    if lock:
        box(c, 1300, 610, 40, 36, (0.6, 0.6, 0.62), 6)
        c.arc(1320, 610, 14, 3.14, 6.28); c.set_source_rgb(0.6, 0.6, 0.62); c.set_line_width(6); c.stroke()
        box(c, 1205, 470, 120, 50, (0.95, 0.95, 0.9), 4)
        text(c, "STAFF ONLY", 1265, 503, 18, (0.8, 0.1, 0.1))
    # air machine
    box(c, 1440, 560, 70, 220, (0.15, 0.4, 0.75), 8)
    text(c, "AIR", 1475, 600, 22, WHITE)
    if night:
        V.shade(c, 0.1, (0.05, 0.0, 0.1))


def pw(lock=False, night=True, **kw):
    def f(c, t, lt):
        pump(c, t, lock, night)
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
    K.rows(c, t, st, [("PUMP TOILET...", WHITE, 62, 0.6), ("ONLY FOR STAFF?", YEL, 64, 2.0)], y0=1030, gap=120)


def o_trip(c, t, lt):
    st = sh.s(2)
    K.panel(c, 900, 420)
    T(c, "SID: 'TOILET, BHAI?'", 540, 1010, 54, WHITE, k(t, st + 1.2, st + 1.5), stroke=None)
    T(c, "STAFF: 'NOT FOR PUBLIC'", 540, 1120, 52, RED, k(t, st + 3.6, st + 3.9), stroke=None)
    K.stamp(c, t, st + 4.6, "REALLY?", 540, 1250, YEL, 58, -0.05)


def o_rule(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "EVERY PETROL PUMP", 540, 420, 60, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    K.stamp(c, t, st + 2.4, "MUST GIVE FREE", 540, 560, YEL, 70, -0.03)
    K.rows(c, t, st, [("Air", WHITE, 64, 4.4), ("Drinking water", WHITE, 64, 5.2),
                      ("Clean toilet", GRN, 70, 6.0), ("Phone + first-aid box", WHITE, 58, 6.9)], y0=760, gap=125)


def o_case(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "KERALA CONSUMER COMMISSION", 540, 420, 48, GREY, k(t, st + 0.6, st + 0.9), lw=7)
    T(c, "Toilet refused at a pump", 540, 540, 50, WHITE, k(t, st + 2.0, st + 2.3), lw=7)
    a = k(t, st + 4.0, st + 4.4)
    sc = 1 + 0.25 * (1 - U.eob(a))
    c.save(); c.translate(540, 760); c.scale(sc, sc)
    T(c, "₹1.5 LAKH", 0, 0, 150, YEL, a, lw=14)
    c.restore()
    T(c, "COMPENSATION", 540, 900, 62, GRN, k(t, st + 4.6, st + 4.9), lw=8)
    T(c, "(April 2025)", 540, 990, 40, GREY, k(t, st + 4.8, st + 5.1), lw=6)


def o_fault(c, t, lt):
    st = sh.s(5)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("TOILET LOCKED?", WHITE, 56, 0.1), ("PAID FOR AIR?", WHITE, 56, 1.1)], y0=990, gap=100)
    K.stamp(c, t, st + 2.2, "DEALER'S FAULT", 540, 1240, RED, 60, -0.04)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("FILLED PETROL, THEN", WHITE, 54, 0.2), ("HELD IT TILL THE DHABA?", YEL, 50, 1.4)], y0=1000, gap=110)
    K.stamp(c, t, st + 2.6, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(7)
    K.panel(c, 800, 600)
    T(c, "THE FIX", 540, 880, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Ask politely", WHITE, 46, 0.3, "left", 130),
                      ("2. Refused? Ask for the", WHITE, 46, 1.6, "left", 130),
                      ("    complaint book", WHITE, 46, 1.6, "left", 130),
                      ("3. Complain: OMC portal", GRN, 46, 5.4, "left", 130),
                      ("    or CPGRAMS", GRN, 46, 5.4, "left", 130)], y0=980, gap=80)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "PAY FOR PETROL.", "AIR, WATER, TOILET = FREE", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "ALWAYS HUNTING A TOILET", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    sh.shots = [
        (0, s(2), pw(mouth='o', eyes=1.2), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'night'),
        (s(2), s(3), pw(lock=True, mouth='frown', squint=0.3, arms=((60, 120), (14, -10))), (1.75, 1080, 470), (1.95, 1150, 470), o_trip, 'night'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_rule, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_case, 'money'),
        (s(5), s(6), pw(lock=True, mouth='smirk'), (1.8, 1100, 480), (1.95, 1060, 470), o_fault, 'night'),
        (s(6), s(7), pw(night=False, mouth='frown'), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), pw(night=False, mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, pw(night=False, mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
