import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s65_challan"
CAPS = [
    "Papa got an SMS: 'Challan pending, pay via link.' STOP. That link is a SCAM.",
    "The site looks exactly like the RTO's. Enter your vehicle number... then it says: install this app.",
    "That app is an .APK file. Once installed, it can read your SMS and OTPs.",
    "Then money can go from UPI, bank, wallet. PIB and police have both warned about this.",
    "Same bro? Someone at home said 'there's a challan, just pay it fast'?",
    "Fix: check challans ONLY on the official Parivahan e-Challan site or app. Never the SMS link. NEVER install an APK.",
    "Money gone? Call 1930 right away. Or complain online: cybercrime.gov.in",
    "MORAL: A real challan never sends you an APK.",
    "Send this to your mummy-papa. Today.",
]
HOOK = [("CHALLAN SMS?", WHITE), ("DON'T TAP IT", RED), ("SCAM OF THE WEEK #1", GREY)]
SRC = "Source: PIB Fact Check advisory (Jul 2026); Kerala Police (Sep 2026)"
sh = None
BLUE = (0.26, 0.52, 0.96)


def fake_site(stage):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
        c.rectangle(0, 0, w, 120); c.set_source_rgb(0.1, 0.25, 0.55); c.fill()
        T(c, "e-Challan", w / 2, 82, 40, WHITE, stroke=None)
        S.rrect(c, 40, 170, w - 80, 70, 10); c.set_source_rgb(0.9, 0.9, 0.93); c.fill()
        T(c, "DL 3C AB 1234", w / 2, 218, 34, (0.2, 0.2, 0.25), stroke=None)
        T(c, "Fine due: ₹500", w / 2, 320, 38, RED, stroke=None)
        if stage:
            S.rrect(c, 30, 400, w - 60, 320, 20); c.set_source_rgb(1, 1, 1); c.fill_preserve()
            c.set_source_rgb(0.8, 0.8, 0.85); c.set_line_width(3); c.stroke()
            T(c, "Internal Security", w / 2, 470, 32, (0.15, 0.15, 0.2), stroke=None)
            T(c, "Review", w / 2, 515, 32, (0.15, 0.15, 0.2), stroke=None)
            T(c, "Install app to pay?", w / 2, 580, 28, (0.35, 0.35, 0.4), stroke=None, bold=False)
            S.rrect(c, 70, 630, w - 140, 70, 35); c.set_source_rgb(0.15, 0.6, 0.3); c.fill()
            T(c, "YES", w / 2, 677, 32, WHITE, stroke=None)
    return f


def rw(mode='night', **kw):
    def f(c, t, lt):
        V.room(c, t, mode, fan=False)
        d = dict(pose='stand', mouth='flat')
        d.update(kw)
        K.sid(c, t, 1000, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 290, 610, 500, 560, K.sms_screen("VM-ECHLN", [("Challan pending!", RED), ("Pay now to avoid", WHITE),
                                                                    ("court: bit.ly/ech..", BLUE)]), t - st, tilt=-2 + 3 * lt)
    K.stamp(c, t, st + 3.2, "THIS LINK = SCAM", 540, 1290, RED, 56, -0.05)


def o_site(c, t, lt):
    st = sh.s(2)
    U.phone_frame(c, 290, 470, 500, 820, fake_site(t > st + 3.5), t - st, tilt=2 - 3 * lt)
    K.stamp(c, t, st + 1.3, "LOOKS LIKE RTO", 540, 1370, YEL, 48, 0.04)


def o_apk(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    a = k(t, st + 0.2, st + 0.5)
    S.rrect(c, 340, 470, 400, 300, 30); c.set_source_rgba(0.2, 0.22, 0.3, a); c.fill()
    T(c, ".APK", 540, 650, 110, RED, a, lw=10)
    K.rows(c, t, st, [("CAN READ YOUR", WHITE, 60, 2.0), ("SMS + OTPs", YEL, 90, 2.8)], y0=930, gap=130)


def o_drain(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    for i, lab in enumerate(["UPI", "BANK", "WALLET"]):
        a = k(t, st + 0.3 + i * 0.5, st + 0.6 + i * 0.5)
        if a > 0:
            S.rrect(c, 160, 480 + i * 150, 760, 120, 24); c.set_source_rgba(0.35, 0.08, 0.1, a); c.fill()
            T(c, lab, 210, 560 + i * 150, 56, WHITE, a, stroke=None, anchor="left")
            T(c, "-₹₹₹", 870, 560 + i * 150, 56, RED, a, stroke=None, anchor="right")
    K.stamp(c, t, st + 3.0, "PIB + POLICE WARNING", 540, 1080, YEL, 48, -0.03)


def o_same(c, t, lt):
    st = sh.s(5)
    K.panel(c, 900, 420)
    K.rows(c, t, st, [("'CHALLAN HAI,", WHITE, 60, 0.3), ("JALDI PAY KAR DO'?", YEL, 58, 1.2)], y0=1010, gap=110)
    K.stamp(c, t, st + 2.4, "SAME BRO?", 540, 1250, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(6)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Check ONLY on official", WHITE, 46, 0.3, "left", 140),
                      ("    Parivahan e-Challan site/app", WHITE, 40, 0.3, "left", 140),
                      ("2. Never tap the SMS link", WHITE, 46, 3.6, "left", 140),
                      ("3. NEVER install an APK", RED, 48, 5.2, "left", 140)], y0=1000, gap=90)


def o_help(c, t, lt):
    st = sh.s(7)
    K.full(c, t, st, [("MONEY GONE?", WHITE, 70, 0.1), ("CALL 1930", GRN, 140, 0.9), ("cybercrime.gov.in", YEL, 64, 2.6)],
           y0=560, gap=190)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "A REAL CHALLAN", "NEVER SENDS AN APK.", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND THIS TO", "MUMMY-PAPA. TODAY.", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (60, 120)))
    sh.shots = [
        (0, s(2), rw('day', mouth='o', eyes=1.3, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), rw('day', mouth='flat', squint=0.3, **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_site, 'warm'),
        (s(3), s(4), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_apk, 'red'),
        (s(4), s(5), sw(mouth='frown', angry=0.6), (1.78, 960, 540), (1.85, 960, 520), o_drain, 'red'),
        (s(5), s(6), rw(mouth='frown', sweat=1, **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'night'),
        (s(6), s(7), rw('day', mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(7), s(8), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_help, 'money'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw('day', mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
