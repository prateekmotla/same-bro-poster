"""RULES YOU DIDN'T KNOW #11: credit card closure in 7 working days or Rs 500/day to you (engine: vshort.Short).
Fact: RBI Master Direction - Credit Card and Debit Card - Issuance and Conduct Directions, 2022 (21 Apr 2022, in force
1 Jul 2022): a request to close a credit card shall be honoured within seven working days by the card-issuer, subject
to the cardholder paying all dues; failure = penalty of Rs 500 per day of delay payable to the customer till the
account is closed, provided there is no outstanding. Issuers must accept closure requests via helpline, email, IVR,
website, internet banking, mobile app etc. Unresolved: RBI Integrated Ombudsman (cms.rbi.org.in)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c092_cardclose"
CAPS = [
    "You want to close your credit card, and the bank says: 'Sir, just listen to ONE offer.' Weeks later, still not closed?",
    "After your request, how many days does the bank get? A: as long as it wants. B: only 7 working days. Comment!",
    "B is right. RBI's 2022 rule: if all your dues are clear, the bank MUST close the card in 7 working days.",
    "If it's late, the bank pays YOU ₹500 for every day of delay, until the card is closed.",
    "Ask by email, helpline, app, anywhere. Keep proof. Bank ignores you? Complain to the RBI Ombudsman.",
    "Card not getting closed? Now you know the rule. Save this.",
]
HOOK = [("CARD NOT CLOSED?", WHITE), ("BANK PAYS YOU ₹500/DAY", GRN), ("RULES YOU DIDN'T KNOW #11", GREY)]
SRC = "SRC: RBI Master Direction on cards, 2022"
sh = None


def call_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.06, 0.07, 0.1); c.fill()
    T(c, "on call  47:12", w / 2, 120, 30, GREY, stroke=None, bold=False)
    S.rrect(c, w / 2 - 70, 160, 140, 140, 36); c.set_source_rgb(0.2, 0.35, 0.75); c.fill()
    T(c, "BANK", w / 2, 245, 38, WHITE, stroke=None)
    T(c, "CARD HELPLINE", w / 2, 360, 34, WHITE, stroke=None)
    c.arc(w / 2, h - 60, 40, 0, 6.283); c.set_source_rgb(0.9, 0.2, 0.2); c.fill()


def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "morning")
        d = dict(pose='stand', mouth='flat', look=(0.6, 0)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def bubble(c, x, y, txt, a=1.0, size=42):
    w = len(txt) * size * 0.62 + 70
    S.rrect(c, x - w / 2, y, w, 96, 40); c.set_source_rgba(1, 1, 1, 0.96 * a); c.fill()
    T(c, txt, x, y + 64, size, (0.1, 0.1, 0.15), a, stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 700, 720, 330, 520, call_screen, t - st, tilt=4)
    a = k(t, st + 2.6, st + 2.9)
    if a > 0:
        bubble(c, 540, 470, "'SIR, JUST ONE OFFER...'", a)
    if t > st + 4.6:
        K.stamp(c, t, st + 4.6, "REQUEST: DAY 21", 330, 1250, RED, 50, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "BANK GETS HOW LONG?", 540, 470, 66, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "AS LONG AS IT WANTS", 2.0), ("B", "ONLY 7 WORKING DAYS", 4.4))):
        a = k(t, st + d, st + d + 0.3)
        y = 580 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 112, 46, WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.4, "COMMENT A or B", 540, 1120, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 400, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: 7 WORKING DAYS", 540, 495, 62, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 410, GRN, 54, 0.06)
    K.rows(c, t, st, [("RBI RULE, 2022", YEL, 58, 1.4), ("ALL DUES CLEAR?", WHITE, 60, 3.4),
                      ("CARD MUST BE CLOSED", WHITE, 60, 5.0), ("IN 7 WORKING DAYS", GRN, 72, 6.2)], y0=700, gap=135)


def o_fine(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.86)
    T(c, "LATE? BANK PAYS YOU", 540, 520, 66, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "₹500", 540, 760, 200, GRN, k(t, st + 0.8, st + 1.1), lw=14)
    T(c, "PER DAY OF DELAY", 540, 880, 60, YEL, k(t, st + 1.4, st + 1.7), lw=10)
    days = max(0, min(10, int((t - st - 2.0) * 2.5)))
    if t > st + 2.0:
        S.rrect(c, 190, 980, 700, 150, 40); c.set_source_rgba(0.1, 0.12, 0.18, 0.95); c.fill()
        T(c, f"{days} DAYS LATE = ₹{days * 500:,}", 540, 1075, 54, WHITE, stroke=None)


def o_how(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("ASK ANYWHERE:", WHITE, 60, 0.1), ("EMAIL · HELPLINE · APP", YEL, 64, 0.6),
                      ("KEEP PROOF", WHITE, 72, 2.6), ("IGNORED?", WHITE, 60, 3.8), ("RBI OMBUDSMAN", GRN, 92, 4.4),
                      ("cms.rbi.org.in", GREY, 44, 4.8)], y0=420, gap=150)


def o_end(c, t, lt):
    K.end_card(c, "7 WORKING DAYS. OR", "₹500/DAY TO YOU", YEL)
    st = sh.s(6)
    T(c, "A or B? COMMENT", 540, 1260, 64, YEL, k(t, st + 1.0, st + 1.3), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='frown', angry=0.4, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_fine, 'money'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_how, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 3.5, 5.5] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[2][0] + 2.0], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
