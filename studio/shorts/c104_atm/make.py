"""RULES YOU DIDN'T KNOW #14: free ATM transactions + the Rs 23 cap (engine: vshort.Short).
Fact: RBI circular RBI/2021-22/52 DPSS.CO.OD.No.S-182/06.07.011/2021-22 (10 Jun 2021, updated 28 Mar 2025):
five free transactions a month (financial + non-financial) at own-bank ATMs; at other banks' ATMs three free in
metro centres and five in non-metro centres; beyond that a customer may be charged max Rs 23 per transaction from
1 May 2025, applicable taxes extra."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c104_atm"
CAPS = [
    "You took cash from the ATM, and ₹23 more quietly got cut from your account. Why?",
    "Question: how many FREE transactions a month at your own bank's ATM? A: unlimited. B: only 5. Comment!",
    "B is right. RBI rule: 5 free a month at your own bank's ATM. At other banks' ATMs: 3 in metros, 5 in other cities.",
    "And a balance check counts too. After that, max ₹23 per transaction, plus tax.",
    "So don't do lots of small withdrawals. Take it out in one go, and check your balance on the app.",
    "Want to dodge ATM charges? Save this.",
]
HOOK = [("WHY DID ₹23 GET CUT?", WHITE), ("ONLY 5 FREE ATM USES", YEL), ("RULES YOU DIDN'T KNOW #14", GREY)]
SRC = "SRC: RBI circular on ATM charges (2025)"
sh = None


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
    U.phone_frame(c, 690, 720, 340, 600, K.sms_screen("BANK ALERT", [("Debited ₹23", RED), ("ATM txn charge", WHITE),
                                                                     ("+ GST", GREY)]), t - st, tilt=4)
    if t > st + 3.6:
        K.stamp(c, t, st + 3.6, "WHY?", 300, 1200, YEL, 70, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "FREE ATM USES", 540, 430, 66, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "PER MONTH (OWN BANK)?", 540, 515, 56, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "UNLIMITED", 5.2), ("B", "ONLY 5", 6.6))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 118, 64, WHITE, a, stroke=None)
    K.stamp(c, t, st + 8.3, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: ONLY 5", 540, 478, 72, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 390, GRN, 54, 0.06)
    T(c, "FREE PER MONTH", 540, 630, 50, GREY, k(t, st + 1.2, st + 1.5), stroke=None)
    for i, (lab, val, d) in enumerate((("OWN BANK ATM", "5", 2.9), ("OTHER BANK: METRO", "3", 6.2),
                                       ("OTHER BANK: NON-METRO", "5", 8.1))):
        a = k(t, st + d, st + d + 0.3)
        y = 680 + i * 170
        S.rrect(c, 110, y, 860, 140, 32); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        T(c, lab, 150, y + 88, 42, WHITE, a, stroke=None, anchor="left")
        T(c, val, 900, y + 98, 80, YEL, a, stroke=None)


def o_fee(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("BALANCE CHECK", WHITE, 70, 0.2), ("COUNTS TOO", YEL, 80, 0.8), ("AFTER THAT", WHITE, 60, 2.8),
                      ("MAX ₹23", RED, 130, 3.4), ("+ TAX, PER TRANSACTION", GREY, 46, 4.4)], y0=470, gap=170)


def o_tips(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("FEWER, BIGGER", WHITE, 72, 0.2), ("WITHDRAWALS", GRN, 90, 0.7), ("CHECK BALANCE", WHITE, 72, 2.6),
                      ("ON THE APP", GRN, 90, 3.1)], y0=500, gap=170)


def o_end(c, t, lt):
    K.end_card(c, "5 FREE. THEN ₹23.", "PLAN YOUR CASH", YEL)
    st = sh.s(6)
    T(c, "SAVE THIS", 540, 1260, 64, GRN, k(t, st + 1.3, st + 1.6), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='frown', angry=0.3, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_fee, 'studio'),
        (s(5), s(6), sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_tips, 'money'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 4.5] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
