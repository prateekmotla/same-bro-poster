"""RULES YOU DIDN'T KNOW #24: check your PF balance with one missed call (engine: vshort.Short).
Facts: EPFO member passbook portal (passbook.epfindia.gov.in) banner: 'For EPF Balance Enquiry: 1. Give a Missed
call to 9966044425 or 2. SMS EPFOHO UAN <LAN> to 7738299899'. The missed call must come from the mobile number
registered with your UAN, and the UAN must be seeded with KYC (bank account / Aadhaar / PAN); the call disconnects
by itself, no charge; an SMS returns the PF balance and last contribution (EPFO guidance as reported by ClearTax,
Moneyview, TaxGuru). No login, no internet needed."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c144_pfcall"
CAPS = [
    "Want to check your PF balance? App, password, OTP, all that drama? Or just ONE missed call?",
    "Question: A: Can't do it without login. B: One missed call is enough. Comment!",
    "Answer: B. From your UAN-registered mobile, give a missed call to 99660 44425. The call cuts itself, it's free.",
    "A little later an SMS comes with your PF balance and last contribution.",
    "Just one condition: your UAN must have KYC linked, like Aadhaar, bank or PAN.",
    "SMS works too: type EPFOHO UAN and send it to 77382 99899. When did YOU last check your PF? Comment!",
]
HOOK = [("PF BALANCE?", WHITE), ("JUST 1 MISSED CALL", YEL), ("RULES YOU DIDN'T KNOW #24", GREY)]
SRC = "SRC: EPFO member passbook portal"
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


def login_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
    c.rectangle(0, 0, w, 120); c.set_source_rgb(0.15, 0.35, 0.7); c.fill()
    T(c, "PF LOGIN", w / 2, 85, 44, WHITE, stroke=None)
    for i, lab in enumerate(("UAN", "PASSWORD", "CAPTCHA", "OTP")):
        y = 200 + i * 105
        T(c, lab, 40, y, 28, GREY, stroke=None, anchor="left")
        S.rrect(c, 40, y + 14, w - 80, 56, 12); c.set_source_rgb(0.88, 0.89, 0.93); c.fill()
    S.rrect(c, 40, h - 110, w - 80, 80, 40); c.set_source_rgb(0.15, 0.35, 0.7); c.fill()
    T(c, "LOGIN", w / 2, h - 57, 36, WHITE, stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 690, 720, 340, 600, login_screen, t - st, tilt=4)
    if t > st + 2.4:
        K.stamp(c, t, st + 2.4, "SO MUCH DRAMA?", 330, 1180, RED, 50, -0.05)
    if t > st + 4.0:
        K.stamp(c, t, st + 4.0, "1 MISSED CALL?", 690, 1320, YEL, 54, 0.04)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "CHECK PF BALANCE", 540, 450, 64, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "NEED LOGIN + OTP", 0.8), ("B", "1 MISSED CALL", 2.9))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 116, 56, WHITE, a, stroke=None)
    K.stamp(c, t, st + 4.9, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_call(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 300, 860, 130, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: 1 MISSED CALL", 540, 385, 60, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 310, GRN, 50, 0.06)
    rows = [("FROM YOUR UAN-REGISTERED MOBILE", WHITE, 40, 1.4), ("CALL", GREY, 50, 2.4), ("99660 44425", YEL, 104, 2.6),
            ("CUTS BY ITSELF", WHITE, 56, 7.4), ("FREE", GRN, 90, 8.6)]
    for i, (txt, col, sz, d) in enumerate(rows):
        T(c, txt, 540, 560 + i * 150, sz, col, k(t, st + d, st + d + 0.3), lw=10)


def o_sms(c, t, lt):
    st = sh.s(4)
    U.phone_frame(c, 540, 760, 380, 640, K.sms_screen("EPFOHO", [("PF BALANCE", GRN), ("Rs ••,•••", WHITE),
                                                                 ("Last contribution", GREY), ("•• / ••", WHITE)]), t - st, tilt=-3)
    if t > st + 1.0:
        K.stamp(c, t, st + 1.0, "SMS COMES BACK", 540, 330, GRN, 54, -0.03)


def o_kyc(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("ONE CONDITION", WHITE, 64, 0.1), ("UAN + KYC LINKED", YEL, 74, 1.2),
                      ("AADHAAR", GRN, 64, 2.6), ("BANK", GRN, 64, 3.1), ("PAN", GRN, 64, 3.6)], y0=430, gap=170)


def o_end(c, t, lt):
    st = sh.s(6)
    K.panel(c, 380, 380, 140, 800, 0.9)
    T(c, "OR SMS", 540, 470, 56, WHITE, k(t, st, st + 0.3), stroke=None)
    T(c, "EPFOHO UAN", 540, 580, 76, YEL, k(t, st + 0.8, st + 1.1), stroke=None)
    T(c, "TO 77382 99899", 540, 690, 64, GRN, k(t, st + 2.0, st + 2.3), stroke=None)
    T(c, "LAST PF CHECK? COMMENT", 540, 1260, 50, YEL, k(t, st + 5.6, st + 5.9), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='flat', squint=0.3, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk', **ph), (1.78, 960, 540), (1.85, 960, 520), o_call, 'studio'),
        (s(4), s(5), w_room(mouth='smile', **ph), (1.6, 960, 560), (1.7, 960, 540), o_sms, 'warm'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_kyc, 'studio'),
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
