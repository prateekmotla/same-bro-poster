"""SCAM OF THE WEEK #4: 'I sent money to you by mistake, please return it' (engine: vshort.Short).
Facts: police/bank advisories (e.g. Tripura Police 2023, SBI on 'jumped deposit' scams): a fake 'credited' SMS or a
small real credit is followed by a call/collect request asking you to 'return' money. Check the balance only in your
bank app/passbook; if money really came, tell the sender to raise it with their bank (banks reverse wrong transfers);
never enter your UPI PIN on a collect request or link. Cyber fraud helpline 1930 / cybercrime.gov.in."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s86_mistake"
CAPS = [
    "SMS: '₹10,000 credited to your account.' Then a call: 'Bhai, sent it by MISTAKE, please send it back.'",
    "But the SMS is FAKE. Not one rupee came in. They just want you to pay from YOUR pocket.",
    "What do you do? A: be honest, send it back. B: check the balance in your BANK APP first. Comment!",
    "B is right. Don't trust the SMS. Trust only your bank app or passbook.",
    "Even if money really came, don't send it yourself. Tell them: complain to YOUR bank, the bank will reverse it.",
    "Got a collect request or a link? Never enter your PIN. Smell fraud? Call 1930.",
    "Send this to your mummy-papa, so if they get this call, they pick B too.",
]
HOOK = [("'SENT BY MISTAKE'", WHITE), ("SEND IT BACK?", RED), ("SCAM OF THE WEEK #4", GREY)]
SRC = "SRC: Police & bank fraud advisories, 1930 helpline"
sh = None


def call_screen(name, sub, lines, n):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.06, 0.08, 0.12); c.fill()
        T(c, name, w / 2, 120, 40, WHITE, stroke=None)
        T(c, sub, w / 2, 170, 26, GREY, stroke=None, bold=False)
        T(c, f"00:{int(tt) % 60:02d}", w / 2, 215, 26, GRN, stroke=None, bold=False)
        for i, (ln, col) in enumerate(lines[:n]):
            S.rrect(c, 24, 260 + i * 92, w - 48, 74, 20); c.set_source_rgb(0.18, 0.2, 0.26); c.fill()
            T(c, ln, w / 2, 308 + i * 92, 30, col, stroke=None)
        c.arc(w / 2, h - 80, 44, 0, 6.283); c.set_source_rgb(0.9, 0.2, 0.2); c.fill()
        T(c, "END", w / 2, h - 70, 24, WHITE, stroke=None)
    return f


def bank_screen(bal, note, note_col):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
        c.rectangle(0, 0, w, 120); c.set_source_rgb(0.1, 0.3, 0.6); c.fill()
        T(c, "MY BANK APP", w / 2, 82, 38, WHITE, stroke=None)
        T(c, "Available balance", w / 2, 220, 30, (0.4, 0.4, 0.45), stroke=None, bold=False)
        T(c, bal, w / 2, 300, 66, (0.1, 0.1, 0.12), stroke=None)
        S.rrect(c, 30, 360, w - 60, 80, 20); c.set_source_rgb(*note_col); c.fill()
        T(c, note, w / 2, 412, 30, WHITE, stroke=None)
        T(c, "Last 3 transactions", 40, 500, 26, (0.4, 0.4, 0.45), stroke=None, anchor="left", bold=False)
        for i, (a, b) in enumerate((("Chai stall", "-₹20"), ("Recharge", "-₹299"), ("Salary", "+₹18,000"))):
            T(c, a, 40, 560 + i * 54, 28, (0.15, 0.15, 0.18), stroke=None, anchor="left", bold=False)
            T(c, b, w - 40, 560 + i * 54, 28, (0.15, 0.15, 0.18), stroke=None, anchor="right")
    return f


def rw(mode='day', **kw):
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
    if t < st + 3.3:
        scr = K.sms_screen("AX-BNKUPD", [("₹10,000 CREDITED", GRN), ("to A/c XX4821", WHITE), ("Ref 6627XXXX", GREY)])
    else:
        n = 1 + int(k(t, st + 3.5, st + 5.5) * 1.99)
        scr = call_screen("+91 9XXXX XXX12", "Unknown", [("'Sent by MISTAKE'", WHITE), ("'Please send it back'", YEL)], n)
    U.phone_frame(c, 290, 560, 500, 640, scr, t - st, tilt=-2 + 3 * lt)
    K.stamp(c, t, st + 5.6, "A: RETURN   or   B: CHECK?", 540, 1330, RED, 46, -0.04)


def o_fake(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.86)
    U.phone_frame(c, 290, 520, 500, 640, bank_screen("₹2,340", "NO NEW CREDIT", RED), t - st, tilt=1)
    K.stamp(c, t, st + 0.4, "SMS = FAKE", 540, 470, RED, 64, -0.05)
    K.rows(c, t, st, [("THEY WANT YOUR MONEY", YEL, 56, 3.3)], y0=1290)


def o_choice(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "WHAT DO YOU DO?", 540, 470, 72, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt) in enumerate((("A", "BE HONEST, SEND BACK"), ("B", "CHECK BANK APP FIRST"))):
        a = k(t, st + 1.0 + i * 2.4, st + 1.3 + i * 2.4)
        y = 580 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 112, 44, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.8, "COMMENT A or B", 540, 1120, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    S.rrect(c, 110, 430, 860, 190, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: CHECK BANK APP", 540, 545, 60, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 450, GRN, 54, 0.06)
    K.rows(c, t, st, [("DON'T TRUST THE SMS", RED, 58, 1.2), ("TRUST ONLY:", WHITE, 52, 2.4),
                      ("YOUR BANK APP", GRN, 70, 2.8), ("OR PASSBOOK", GRN, 70, 3.6)], y0=760, gap=120)


def o_real(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("REALLY CREDITED?", WHITE, 64, 0.1), ("DON'T SEND IT YOURSELF", RED, 62, 1.2),
                      ("TELL THEM:", WHITE, 52, 2.8), ("'COMPLAIN TO YOUR BANK'", YEL, 58, 3.3),
                      ("BANK REVERSES IT", GRN, 70, 4.6)], y0=470, gap=150)


def o_pin(c, t, lt):
    st = sh.s(6)
    K.full(c, t, st, [("COLLECT REQUEST / LINK?", WHITE, 60, 0.1), ("NEVER ENTER PIN", RED, 88, 1.2),
                      ("SMELL FRAUD?", WHITE, 60, 2.8), ("CALL 1930", GRN, 110, 3.6)], y0=520, gap=190)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO MUMMY-PAPA.", "SO THEY PICK B TOO.", YEL)
    st = sh.s(7)
    T(c, "A or B? COMMENT", 540, 1260, 64, YEL, k(t, st + 1.5, st + 1.8), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (60, 120)))
    sh.shots = [
        (0, s(2), rw('day', mouth='o', eyes=1.3, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), rw('day', mouth='frown', angry=0.4, **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_fake, 'red'),
        (s(3), s(4), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(4), s(5), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_real, 'studio'),
        (s(6), s(7), sw(mouth='flat', angry=0.3), (1.78, 960, 540), (1.85, 960, 520), o_pin, 'money'),
        (s(7), sh.dur + 1, rw('day', mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 2.8, 6.2] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[2][0] + 5.5], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
