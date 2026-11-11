"""SCAM OF THE WEEK #8: 'KYC pending, account will be blocked' SMS (engine: vshort.Short).
Fact: RBI press release 2023-2024/1794 (2 Feb 2024) 'RBI cautions against frauds in the name of KYC updation'
(repeats 13 Sep 2021): fraudsters send unsolicited calls/SMS/emails with links, create false urgency and threaten
account freezing/blocking/closure, get customers to install unverified apps and share login/card/PIN/OTP. RBI:
contact your bank directly for any KYC request; take the bank's number only from its official website; never share
OTP/PIN/passwords; don't click unverified links; report at cybercrime.gov.in or helpline 1930."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/c107_kyc"
CAPS = [
    "SMS: 'Dear customer, your KYC is pending, your account will be BLOCKED tonight. Click the link.'",
    "What do you do? A: open the link and update KYC. B: ignore the link, ask your bank yourself. Comment!",
    "B is right. RBI itself warned: fake SMS and calls in the name of KYC, with a threat to block your account.",
    "They make you install an app from the link, then your login, OTP, PIN, all theirs. Account EMPTY.",
    "Got a KYC message? Confirm with your bank directly, number only from the official website. Scammed? Call 1930.",
    "Send this to your mummy-papa. They get these SMS the most.",
]
HOOK = [("'KYC PENDING' SMS?", WHITE), ("IT'S A SCAM", RED), ("SCAM OF THE WEEK #8", GREY)]
SRC = "SRC: RBI press release (Feb 2024)"
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
    U.phone_frame(c, 690, 720, 340, 600, K.sms_screen("AX-KYCUPD", [("KYC DUE!", RED), ("A/c BLOCKED", WHITE),
                                                                    ("tonight. Update:", WHITE), ("kyc-upd8.xyz", BLUE)]),
                  t - st, tilt=4)
    if t > st + 3.9:
        K.stamp(c, t, st + 3.9, "BLOCKED TONIGHT?!", 330, 1200, RED, 50, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "'KYC PENDING' SMS", 540, 430, 66, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "WHAT DO YOU DO?", 540, 515, 58, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "OPEN THE LINK", 1.3), ("B", "ASK YOUR BANK", 3.9))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 610, y + 118, 60, WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.4, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: ASK YOUR BANK", 540, 478, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("RBI WARNING", YEL, 64, 1.4), ("FAKE KYC", RED, 84, 3.2), ("SMS & CALLS", WHITE, 70, 3.8),
                      ("'ACCOUNT WILL BE BLOCKED'", GREY, 44, 6.0)], y0=690, gap=125)


def o_steal(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("LINK > INSTALL APP", WHITE, 66, 0.3), ("LOGIN, OTP, PIN", YEL, 80, 2.0),
                      ("ALL THEIRS", RED, 90, 3.2)], y0=500, gap=180)
    if t > st + 4.6:
        K.stamp(c, t, st + 4.6, "ACCOUNT: ₹0", 540, 1180, RED, 72, -0.04)


def o_tips(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("KYC MESSAGE?", WHITE, 64, 0.1), ("CALL YOUR BANK", GRN, 80, 1.3),
                      ("NUMBER: OFFICIAL SITE ONLY", YEL, 54, 3.2), ("SCAMMED? CALL", WHITE, 60, 5.3), ("1930", GRN, 130, 6.0),
                      ("cybercrime.gov.in", GREY, 44, 6.4)], y0=400, gap=150)


def o_end(c, t, lt):
    K.end_card(c, "'KYC PENDING' SMS?", "ASK YOUR BANK", YEL)
    st = sh.s(6)
    T(c, "SEND TO MUMMY-PAPA", 540, 1260, 60, YEL, k(t, st + 0.3, st + 0.6), lw=10)


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
        sh.preview([0.5, 5.0] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
