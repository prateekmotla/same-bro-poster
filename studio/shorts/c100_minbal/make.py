"""RULES YOU DIDN'T KNOW #13: minimum-balance penalty can't push your savings balance negative (engine: vshort.Short).
Fact: RBI circular DBR.Dir.BC.No.47/13.03.00/2014-15 (RBI/2014-15/308), 20 Nov 2014, 'Levy of penal charges on
non-maintenance of minimum balances in savings bank accounts' (effective 1 Apr 2015): bank must notify the customer by
SMS/email/letter of the shortfall; at least one month from the notice to restore the balance before penal charges;
charges directly proportionate to the shortfall; 'the balance in the savings account does not turn into negative
balance solely on account of levy of charges for non-maintenance of minimum balance'. Unresolved: RBI Ombudsman."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c100_minbal"
CAPS = [
    "Only ₹200 in the account, the minimum balance charge got cut, and now the balance is in MINUS?",
    "Can the bank make your balance negative with a minimum balance charge? A: yes. B: NO WAY. Comment!",
    "B is right. RBI's 2014 rule: your balance can't go negative only because of a minimum balance charge.",
    "And before charging, the bank must tell you by SMS or email, and give you at least ONE MONTH to top up.",
    "The charge must match the shortfall. Bank won't fix it? Complain to the RBI Ombudsman.",
    "Balance showing minus? Now you know the rule. Save this.",
]
HOOK = [("₹200 IN THE ACCOUNT", WHITE), ("NOW IT'S MINUS?", RED), ("RULES YOU DIDN'T KNOW #13", GREY)]
SRC = "SRC: RBI circular on minimum balance charges, 20 Nov 2014"
sh = None


def bank_screen(bal, col, cut=False):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.95, 0.96, 0.98); c.fill()
        c.rectangle(0, 0, w, 150); c.set_source_rgb(0.15, 0.3, 0.6); c.fill()
        T(c, "MY BANK", w / 2, 100, 40, WHITE, stroke=None)
        T(c, "SAVINGS A/C BALANCE", w / 2, 240, 24, (0.4, 0.4, 0.45), stroke=None, bold=False)
        T(c, bal, w / 2, 340, 80, col, stroke=None)
        if cut:
            S.rrect(c, 30, 410, w - 60, 120, 20); c.set_source_rgb(1, 0.9, 0.9); c.fill()
            T(c, "MIN BAL CHARGE", w / 2, 460, 30, (0.6, 0.1, 0.1), stroke=None)
            T(c, "- ₹500", w / 2, 510, 40, (0.8, 0.1, 0.1), stroke=None)
    return f


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


def o_hook(c, t, lt):
    st = sh.s(1)
    cut = t > st + 2.0
    neg = t > st + 3.6
    bal = "- ₹300" if neg else "₹200"
    U.phone_frame(c, 700, 720, 330, 560, bank_screen(bal, (0.8, 0.1, 0.1) if neg else (0.1, 0.5, 0.2), cut), t - st, tilt=4)
    if neg:
        K.stamp(c, t, st + 3.6, "MINUS?!", 330, 1250, RED, 70, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "CAN THE CHARGE MAKE", 540, 420, 62, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "YOUR BALANCE NEGATIVE?", 540, 500, 62, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "YES", 3.6), ("B", "NO WAY", 4.6))):
        a = k(t, st + d, st + d + 0.3)
        y = 600 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 118, 60, WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.3, "COMMENT A or B", 540, 1140, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 400, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: NO WAY", 540, 495, 70, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 410, GRN, 54, 0.06)
    K.rows(c, t, st, [("RBI RULE, 2014", YEL, 58, 1.2), ("MIN BALANCE CHARGE", WHITE, 58, 3.0),
                      ("CAN'T MAKE YOUR BALANCE", WHITE, 56, 4.4), ("NEGATIVE", GRN, 96, 5.4)], y0=700, gap=135)


def o_notice(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.86)
    T(c, "BEFORE ANY CHARGE:", 540, 470, 64, WHITE, k(t, st, st + 0.2), lw=10)
    K.rows(c, t, st, [("1. BANK MUST TELL YOU", WHITE, 60, 1.0), ("SMS / EMAIL / LETTER", YEL, 54, 2.2),
                      ("2. AT LEAST", WHITE, 60, 3.8), ("1 MONTH", GRN, 120, 4.4), ("TO TOP UP", WHITE, 60, 5.0)],
           y0=620, gap=130)


def o_how(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("CHARGE MUST MATCH", WHITE, 62, 0.1), ("THE SHORTFALL", YEL, 70, 0.8),
                      ("BANK WON'T FIX IT?", WHITE, 60, 2.6), ("RBI OMBUDSMAN", GRN, 92, 3.4),
                      ("cms.rbi.org.in", GREY, 44, 3.8)], y0=440, gap=160)


def o_end(c, t, lt):
    K.end_card(c, "MIN BALANCE CHARGE", "CAN'T PUSH YOU TO MINUS", YEL)
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
        (0, s(2), w_room(mouth='o', eyes=1.25, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_notice, 'money'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_how, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 3.0, 5.0] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[1][0] + 6.8], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
