"""SCAM OF THE WEEK #10: OLX 'army officer' buyer sends a QR 'to pay you' (engine: vshort.Short).
Facts: Cyberabad Cyber Crimes Wing (Siasat): fake army/paramilitary 'buyer' says he's posted far away, sends a fake
payment screenshot, then a QR code 'to receive money'; seller scans + enters UPI PIN = pays the scammer; then 'mistake,
scan this for double refund' loop. Navi Mumbai Police advisory (Business Insider, 16 Jan 2020): don't trust an army ID
card, "When receiving money, do not scan any QR code", meet at a public place. Receiving UPI money never needs a PIN
(NPCI). Report: 1930 / cybercrime.gov.in. No real marketplace UI or logo shown; OLX named only as where the ad was.
Voice take sped 1.07x."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/c123_olxarmy"
CAPS = [
    "Put my old bike up on OLX. Buyer says: I'm an ARMY officer, posted far away, I'll send the full amount on UPI.",
    "Then he sends a QR code: scan it, enter your PIN, the money comes to you. A: Scan it. B: It's a scam. Comment!",
    "Answer: B. You NEVER scan a QR or enter a PIN to RECEIVE money. Enter the PIN and YOUR money goes out.",
    "Then: 'Oops, mistake! Scan this QR for a double refund.' And the loop goes on.",
    "Army ID card, uniform photo: all can be fake. Deal face to face, in a public place.",
    "Got scammed? Call 1930 right away, or complain on cybercrime.gov.in.",
]
HOOK = [("'ARMY OFFICER' BUYER?", WHITE), ("QR TO PAY YOU = SCAM", RED), ("SCAM OF THE WEEK #10", GREY)]
SRC = "SRC: Cyberabad + Navi Mumbai Police advisories"
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
    U.phone_frame(c, 690, 720, 340, 600, K.sms_screen("BUYER", [("'Army' guy", GRN), ("Posted far,", WHITE),
                                                               ("full amount", WHITE), ("on UPI", YEL)]),
                  t - st, tilt=4)
    if t > st + 3.8:
        K.stamp(c, t, st + 3.8, "SOLD?!", 330, 1200, YEL, 56, -0.05)


def qr(c, x, y, s, a=1.0):
    S.rrect(c, x - s / 2 - 20, y - s / 2 - 20, s + 40, s + 40, 18); c.set_source_rgba(1, 1, 1, a); c.fill()
    n = 9; cell = s / n
    for i in range(n):
        for j in range(n):
            corner = (i < 3 and j < 3) or (i < 3 and j > 5) or (i > 5 and j < 3)
            on = ((i * 7 + j * 5 + i * j) % 3 == 0) if not corner else (i % 2 == 0 or j % 2 == 0) and not (i in (1, 7) and j in (1, 7))
            if on:
                c.rectangle(x - s / 2 + j * cell, y - s / 2 + i * cell, cell, cell)
    c.set_source_rgba(0.06, 0.06, 0.08, a); c.fill()


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "'SCAN + ENTER PIN", 540, 400, 58, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "TO GET YOUR MONEY'", 540, 480, 58, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    a0 = k(t, st + 0.6, st + 1.0)
    if t < st + 4.2:
        qr(c, 540, 820, 380, a0)
    else:
        for i, (lab, txt, d) in enumerate((("A", "SCAN IT", 4.2), ("B", "IT'S A SCAM", 5.0))):
            a = k(t, st + d, st + d + 0.3)
            y = 620 + i * 230
            S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
            c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
            T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
            T(c, txt, 610, y + 118, 60, WHITE, a, stroke=None)
        K.stamp(c, t, st + 6.0, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: IT'S A SCAM", 540, 478, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("TO RECEIVE MONEY", WHITE, 60, 1.0), ("NO QR SCAN", GRN, 76, 2.2), ("NO PIN. EVER.", GRN, 76, 3.4),
                      ("PIN ENTERED =", WHITE, 60, 5.2), ("YOUR MONEY GOES OUT", RED, 62, 6.0)], y0=680, gap=120)


def o_loop(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "'OOPS, MISTAKE!", 540, 440, 66, WHITE, k(t, st, st + 0.3), lw=10)
    T(c, "SCAN FOR DOUBLE REFUND'", 540, 530, 58, YEL, k(t, st + 0.8, st + 1.1), lw=10)
    a = k(t, st + 1.4, st + 1.8)
    qr(c, 380, 840, 220, a)
    qr(c, 700, 840, 220, k(t, st + 2.2, st + 2.6))
    T(c, "x2", 540, 860, 70, RED, k(t, st + 2.4, st + 2.7), lw=10)
    if t > st + 3.6:
        K.stamp(c, t, st + 3.6, "LOOP NEVER ENDS", 540, 1150, RED, 60, -0.04)


def o_tips(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("ARMY ID CARD?", WHITE, 64, 0.1), ("UNIFORM PHOTO?", WHITE, 64, 0.9),
                      ("CAN BE FAKE", RED, 80, 2.0), ("DEAL FACE TO FACE", GRN, 64, 3.2),
                      ("PUBLIC PLACE", YEL, 70, 4.2)], y0=420, gap=165)


def o_end(c, t, lt):
    K.end_card(c, "SCAMMED? CALL", "1930", GRN)
    st = sh.s(6)
    T(c, "cybercrime.gov.in", 540, 1260, 54, YEL, k(t, st + 1.5, st + 1.8), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='smile', eyes=1.1, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3, **ph), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.25), (1.78, 960, 540), (1.85, 960, 520), o_loop, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_tips, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='flat', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 5.5, 9.0] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
