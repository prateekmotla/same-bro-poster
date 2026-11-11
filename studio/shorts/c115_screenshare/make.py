"""SCAM OF THE WEEK #9: 'install this app + share screen for your refund' call (engine: vshort.Short).
Facts: RBI Alert 1/2019 (14 Feb 2019) and NPCI advisory (Feb 2019) warned against remote screen-access apps like
AnyDesk: the fraudster gets the victim to install the app and share its code, gains access to the phone and its
payment/banking apps and steals credentials (Outlook Business, 19 Feb 2019). RBI BE(A)WARE booklet: refund/cashback
frauds, never share screen, OTP, PIN; UPI PIN is only for paying, never for receiving. Report: 1930 /
cybercrime.gov.in. No real brand or company named; AnyDesk named only as the app type RBI/NPCI flagged."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/c115_screenshare"
CAPS = [
    "Your order refund was stuck. Then a call: 'Sir, for the refund just install this app and share your screen.'",
    "What do you do? A: install the app and get the refund. B: cut the call. Comment!",
    "B is right. RBI and NPCI both warned: frauds happen through screen-sharing apps like AnyDesk.",
    "Share your screen and they see your OTP, PIN, banking app, everything LIVE. Then the account is EMPTY.",
    "No real refund needs you to install an app, and you NEVER need a PIN to receive money. Scammed? Call 1930.",
    "Want a refund? Only from the official app or website, yourself. Send this to everyone at home.",
]
HOOK = [("'REFUND' CALL?", WHITE), ("SHARE SCREEN = SCAM", RED), ("SCAM OF THE WEEK #9", GREY)]
SRC = "SRC: RBI Alert 1/2019 + NPCI advisory"
sh = None


def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "evening")
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
    U.phone_frame(c, 690, 720, 340, 600, K.sms_screen("INCOMING CALL", [("Refund desk", GRN), ("Install this", WHITE),
                                                                       ("app & share", WHITE), ("your screen", RED)]),
                  t - st, tilt=4)
    if t > st + 4.6:
        K.stamp(c, t, st + 4.6, "SHARE SCREEN?!", 330, 1200, RED, 50, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "'REFUND' CALL", 540, 430, 66, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "WHAT DO YOU DO?", 540, 515, 58, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "INSTALL THE APP", 1.0), ("B", "CUT THE CALL", 2.9))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 610, y + 118, 60, WHITE, a, stroke=None)
    K.stamp(c, t, st + 4.3, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: CUT THE CALL", 540, 478, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("RBI + NPCI WARNING", YEL, 60, 1.2), ("SCREEN-SHARING", RED, 80, 3.4), ("APPS LIKE ANYDESK", WHITE, 64, 4.4),
                      ("USED FOR FRAUD", GREY, 50, 6.0)], y0=690, gap=125)


def o_steal(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("SCREEN SHARED", WHITE, 66, 0.2), ("OTP, PIN, BANK APP", YEL, 72, 1.2),
                      ("ALL SEEN LIVE", RED, 90, 2.6)], y0=500, gap=180)
    if t > st + 3.9:
        K.stamp(c, t, st + 3.9, "ACCOUNT: ₹0", 540, 1180, RED, 72, -0.04)


def o_tips(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("REAL REFUND =", WHITE, 64, 0.1), ("NO APP INSTALL", GRN, 76, 0.8),
                      ("RECEIVING MONEY = NO PIN", YEL, 54, 3.2), ("SCAMMED? CALL", WHITE, 60, 6.4), ("1930", GRN, 130, 7.0),
                      ("cybercrime.gov.in", GREY, 44, 7.4)], y0=400, gap=150)


def o_end(c, t, lt):
    K.end_card(c, "'REFUND' CALL?", "CUT IT", YEL)
    st = sh.s(6)
    T(c, "REFUND ONLY IN THE OFFICIAL APP", 540, 1260, 44, YEL, k(t, st + 0.3, st + 0.6), lw=8)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', eyes=1.2, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3, **ph), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.25), (1.78, 960, 540), (1.85, 960, 520), o_steal, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_tips, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 5.5] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
