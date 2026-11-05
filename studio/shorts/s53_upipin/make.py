import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s53_upipin"
CAPS = [
    "Guess: if someone is SENDING you money... why do they need your UPI PIN?",
    "Sid sells his old cycle online. 'Buyer': 'Sent ₹5,000! Just scan this QR and enter PIN to receive.'",
    "Truth: you NEVER need a PIN to receive money. PIN = money going OUT.",
    "That QR wasn't 'receive'. It was a payment. One PIN, and ₹5,000 left Sid's account.",
    "Govt data: 13.42 lakh UPI fraud cases in FY 2023-24 alone.",
    "Same bro? Almost tapped 'Pay' on a request like this?",
    "Fix: PIN only when YOU are paying. Decline unknown requests. Scammed? Call 1930 fast.",
    "MORAL: PIN means payment. Always.",
    "Send this to the friend who sells old stuff online.",
]
HOOK = [("SENDING YOU MONEY?", WHITE), ("THEN WHY", YEL), ("YOUR PIN?", RED)]
SRC = "Source: MoS Finance, Parliament, Dec 2025 (FY24 UPI frauds); 1930 = Cyber Crime Helpline"
sh = None
DK = (0.12, 0.12, 0.14)


def room(c, t, lt, **kw):
    V.room(c, t, 'night', fan=False)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def chat_scr(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.93, 0.95, 0.93); c.fill()
    c.rectangle(0, 0, w, 120); c.set_source_rgb(0.1, 0.4, 0.33); c.fill()
    T(c, "Buyer (cycle)", w / 2, 82, 40, WHITE, stroke=None)
    msgs = [("Bhai cycle final. ₹5,000", 0.0), ("Sent ₹5,000! Scan this QR", 1.4), ("and enter PIN to RECEIVE", 1.4)]
    y = 200
    for i, (m, d) in enumerate(msgs):
        a = k(tt, d, d + 0.3)
        S.rrect(c, 30, y - 50, w - 120, 76, 18); c.set_source_rgba(1, 1, 1, a); c.fill()
        T(c, m, 55, y + 2, 32, DK, a, stroke=None, anchor="left")
        y += 95
    a = k(tt, 2.6, 2.9)
    S.rrect(c, 150, 520, 300, 300, 16); c.set_source_rgba(1, 1, 1, a); c.fill()
    for i in range(7):
        for j in range(7):
            if (i * 3 + j * 5 + i * j) % 3 != 0 or (i in (0, 6) and j in (0, 6)):
                c.rectangle(175 + i * 36, 545 + j * 36, 32, 32); c.set_source_rgba(*DK, a); c.fill()
    T(c, "'RECEIVE ₹5,000'", w / 2, 880, 36, (0.1, 0.4, 0.33), a, stroke=None)


def pin_scr(paid):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
        c.rectangle(0, 0, w, 120); c.set_source_rgb(0.2, 0.25, 0.6); c.fill()
        T(c, "UPI", w / 2, 82, 44, WHITE, stroke=None)
        if not paid:
            T(c, "PAYING TO: buyer@upi", w / 2, 230, 34, DK, stroke=None)
            T(c, "₹5,000", w / 2, 330, 80, RED, stroke=None)
            T(c, "ENTER UPI PIN", w / 2, 440, 38, DK, stroke=None)
            n = min(6, int(tt * 2.5))
            for i in range(6):
                c.arc(w / 2 - 125 + i * 50, 520, 14, 0, 6.3)
                c.set_source_rgb(*(DK if i < n else (0.8, 0.8, 0.84))); c.fill()
        else:
            c.arc(w / 2, 330, 90, 0, 6.3); c.set_source_rgb(*RED); c.fill()
            T(c, "!", w / 2, 370, 110, WHITE, stroke=None)
            T(c, "₹5,000 DEBITED", w / 2, 520, 50, RED, stroke=None)
            T(c, "A/c balance: ₹312", w / 2, 600, 36, DK, stroke=None, bold=False)
    return f


def o_guess(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 240, 420, 600, 930, pin_scr(False), t - st, tilt=-2 + 3 * lt)
    K.stamp(c, t, st + 2.6, "TO RECEIVE??", 540, 1380, YEL, 58, -0.05)


def o_chat(c, t, lt):
    st = sh.s(2)
    U.phone_frame(c, 240, 420, 600, 930, lambda c_, w, h, tt: chat_scr(c_, w, h, t - st), t, tilt=-2 + 3 * lt)


def o_truth(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "TO RECEIVE MONEY:", 540, 520, 62, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    K.stamp(c, t, st + 1.4, "PIN NEEDED = NEVER", 540, 660, GRN, 64, -0.03)
    T(c, "PIN =", 540, 900, 72, WHITE, k(t, st + 3.3, st + 3.6), lw=8)
    T(c, "MONEY GOING OUT", 540, 1010, 78, RED, k(t, st + 3.7, st + 4.0), lw=10)


def o_debit(c, t, lt):
    st = sh.s(4)
    paid = t > st + 3.4
    U.phone_frame(c, 240, 420, 600, 930, pin_scr(paid), t - st, tilt=2 - 3 * lt)
    if paid:
        K.stamp(c, t, st + 3.6, "GONE", 540, 1380, RED, 70, -0.06)


def o_data(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.9)
    T(c, "UPI FRAUD CASES, FY 2023-24", 540, 470, 50, GREY, k(t, st + 0.1, st + 0.4), lw=7)
    a = k(t, st + 1.2, st + 1.8)
    T(c, f"{13.42 * U.eob(a):.2f} LAKH", 540, 680, 120, RED, a, lw=12)
    T(c, "(Govt data in Parliament)", 540, 820, 42, WHITE, k(t, st + 3.0, st + 3.3), lw=6)
    T(c, "That's ~3,700 cases a DAY", 540, 960, 52, YEL, k(t, st + 4.6, st + 4.9), lw=7)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("ALMOST TAPPED 'PAY'", WHITE, 58, 0.2), ("ON A REQUEST LIKE THIS?", YEL, 50, 0.8)], y0=1000, gap=110)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(7)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. PIN only when YOU pay", WHITE, 46, 0.4, "left", 140),
                      ("2. Unknown request? DECLINE", WHITE, 46, 2.6, "left", 140),
                      ("3. Scammed? Call 1930 FAST", GRN, 48, 4.6, "left", 140)], y0=1020, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "PIN MEANS PAYMENT.", "ALWAYS.", RED)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO SELLS OLD STUFF ONLINE", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'tense'
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: room(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), rw(mouth='o', eyes=1.2, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'night'),
        (s(2), s(3), rw(mouth='bigsmile', **ph), (2.0, 1000, 470), (2.15, 1000, 450), o_chat, 'night'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_truth, 'studio'),
        (s(4), s(5), rw(mouth='o', eyes=1.4, **ph), (1.9, 1000, 480), (2.2, 1000, 450), o_debit, 'night'),
        (s(5), s(6), sw(mouth='frown'), (1.78, 960, 540), (1.85, 960, 520), o_data, 'studio'),
        (s(6), s(7), rw(mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'night'),
        (s(7), s(8), rw(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'night'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'night'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1))
    else:
        sh.render(f"{D}/short.mp4")
