"""SCAM OF THE WEEK #3: 'your electricity will be cut tonight' SMS.
Sources: PIB Fact Check (23 Feb 2023): Ministry of Power has not issued such notices, it's a scam; messages say power
will be disconnected tonight ~9-9:30 PM because last bill 'not updated', call 'electricity officer' at a number.
Bank advisories (Kotak safe-banking): callers ask for bank details / make you install a remote-access app, then debit.
National cyber-fraud helpline 1930."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s78_power"
CAPS = [
    "SMS: 'Your electricity will be cut tonight at 9 PM. Last bill not updated. Call the officer on this number.' WAIT.",
    "It's a SCAM. PIB Fact Check said it clearly: the Power Ministry sent no such notice.",
    "The moment you call, the 'officer' asks for bank details, or makes you install an app that lets him control your phone.",
    "And then, your account is wiped clean.",
    "Simple rule: check your bill ONLY on your power company's official app or website. No calls to unknown numbers, no app installs.",
    "Got scammed? Call 1930 immediately.",
    "Same bro? Send this to mummy-papa. Comment: have you ever got this message?",
]
HOOK = [("'POWER CUT TONIGHT'", WHITE), ("SMS = SCAM", RED), ("SCAM OF THE WEEK #3", GREY)]
SRC = "SRC: PIB Fact Check (Feb 2023)"
sh = None


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
    U.phone_frame(c, 290, 600, 500, 640, K.sms_screen("+91 98XXX XX761", [("Dear consumer,", WHITE), ("Power cut TONIGHT", RED),
                                                                            ("9 PM. Bill not updated.", WHITE),
                                                                            ("Call officer: 98XXX..", BLUE)]), t - st, tilt=-2 + 3 * lt)
    K.stamp(c, t, st + 6.7, "WAIT.", 540, 1330, RED, 64, -0.05)


def o_pib(c, t, lt):
    st = sh.s(2)
    K.full(c, t, st, [("IT'S A SCAM", RED, 100, 0.1), ("PIB FACT CHECK:", GREY, 56, 1.0), ("POWER MINISTRY SENT", WHITE, 60, 1.4),
                      ("NO SUCH NOTICE", YEL, 74, 2.6)], y0=520, gap=170)


def o_call(c, t, lt):
    st = sh.s(3)
    K.panel(c, 820, 560)
    T(c, "ON THE CALL, 'OFFICER' ASKS:", 540, 900, 44, YEL, k(t, st, st + 0.3), stroke=None)
    K.rows(c, t, st, [("1. Your bank details", WHITE, 54, 1.5), ("2. Install this app", WHITE, 54, 3.0),
                      ("= HE CONTROLS YOUR PHONE", RED, 50, 4.4)], y0=1020, gap=110)


def o_drain(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "BALANCE", 540, 640, 56, GREY, k(t, st, st + 0.2), stroke=None)
    bal = max(0, int(48250 * (1 - min(1, (t - st) / 1.6))))
    T(c, f"₹{bal:,}", 540, 800, 130, RED if bal < 48250 else WHITE, lw=12)
    K.stamp(c, t, st + 1.7, "ACCOUNT WIPED", 540, 1000, RED, 60, -0.04)


def o_fix(c, t, lt):
    st = sh.s(5)
    K.panel(c, 820, 560)
    T(c, "THE RULE", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("Check bill ONLY on the", WHITE, 48, 0.4, "left", 140), ("official app / website", GRN, 50, 1.2, "left", 140),
                      ("No calls to unknown numbers", WHITE, 46, 4.6, "left", 140), ("No app installs", WHITE, 46, 6.0, "left", 140)],
           y0=1000, gap=90)


def o_help(c, t, lt):
    st = sh.s(6)
    K.full(c, t, st, [("GOT SCAMMED?", WHITE, 70, 0.1), ("CALL 1930", GRN, 140, 0.8), ("cybercrime.gov.in", YEL, 60, 1.6)],
           y0=560, gap=190)


def o_end(c, t, lt):
    K.end_card(c, "SEND THIS TO", "MUMMY-PAPA. TODAY.", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (60, 120)))
    sh.shots = [
        (0, s(2), rw('night', mouth='o', eyes=1.3, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'night'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_pib, 'studio'),
        (s(3), s(4), rw('night', mouth='frown', **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_call, 'night'),
        (s(4), s(5), sw(mouth='o', eyes=1.3, sweat=1), (1.78, 960, 540), (1.85, 960, 520), o_drain, 'red'),
        (s(5), s(6), rw('day', mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(6), s(7), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_help, 'money'),
        (s(7), sh.dur + 1, rw('day', mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.5, 6.0] + [a + (b - a) * 0.85 for a, b in L[1:]] + [L[4][0] + 6.5], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
