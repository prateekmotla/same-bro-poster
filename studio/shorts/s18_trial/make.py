import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s18_trial"
CAPS = [
    "Sid starts a free trial on an app. ₹0. Just had to turn on UPI AutoPay.",
    "Forgot in 3 days. A month later, an SMS: ₹499 DEBITED.",
    "Listen. Free trials are free because the company KNOWS lots of people forget to cancel.",
    "It's called a SUBSCRIPTION TRAP, and it's on the government's list of 13 dark patterns. Join in ONE click, cancel in TEN screens.",
    "Good news? Under RBI rules, you must get an alert at least 24 HOURS before every auto-debit. And you can cancel the mandate ANYTIME.",
    "Simple rule: the day you start a trial, set a reminder. Open your UPI app's AutoPay section. Cancel what you don't need right there.",
    "Send this to the friend whose account gets hit by some subscription every month.",
]
HOOK = [("₹0 FREE TRIAL?", WHITE), ("THE HIDDEN", RED), ("AUTOPAY TRAP", YEL)]
SRC = "Source: CCPA Dark Patterns Guidelines 2023; RBI e-mandate rules"
sh = None


def room(c, t, lt, mode='night', **kw):
    V.room(c, t, mode)
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1 if mode == 'night' else 0.3)
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def metro(c, t, lt, **kw):
    V.metro(c, t)
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=0.6)
    d.update(kw)
    K.sid(c, t, 960, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def trial_screen(on):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.08, 0.06, 0.14); c.fill()
        T(c, "PREMIUM", w / 2, 110, 50, YEL, stroke=None)
        T(c, "FREE TRIAL", w / 2, 220, 64, WHITE, stroke=None)
        T(c, "₹0", w / 2, 340, 110, GRN, stroke=None)
        S.rrect(c, 40, 400, w - 80, 80, 20); c.set_source_rgb(0.16, 0.14, 0.24); c.fill()
        T(c, "UPI AutoPay", 70, 452, 32, WHITE, stroke=None, anchor="left", bold=False)
        S.rrect(c, w - 160, 420, 100, 44, 22); c.set_source_rgb(*(GRN if on else (0.4, 0.4, 0.45))); c.fill()
        c.arc(w - 160 + (78 if on else 22), 442, 18, 0, 6.3); c.set_source_rgb(1, 1, 1); c.fill()
        T(c, "then ₹499/month", w / 2, 520, 22, (0.45, 0.43, 0.5), stroke=None, bold=False)
    return f


def o_trial(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 260, 860, 560, 580, trial_screen(t > st + 3.5), t, glow=0.25)


def o_sms(c, t, lt):
    st = sh.s(2)
    if t < st + 2.6:
        K.panel(c, 900, 200, 190, 700)
        T(c, "3 days later...", 540, 1020, 60, GREY, stroke=None)
        return
    lines = [("Rs.499 DEBITED", RED), ("AutoPay - Premium plan", WHITE)]
    U.phone_frame(c, 260, 880, 560, 460, K.sms_screen("BANK ALERT", lines), t, glow=0.25,
                  tilt=k(t, st + 2.6, st + 2.8) * 0)


def o_why(c, t, lt):
    st = sh.s(3)
    K.panel(c, 880, 400)
    K.rows(c, t, st, [("Why is it FREE?", WHITE, 54, 0.8),
                      ("They KNOW", YEL, 60, 2.6),
                      ("you'll forget to cancel", RED, 52, 3.2)], y0=980, gap=110)


def o_trap(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "SUBSCRIPTION", 540, 400, 104, YEL, k(t, st + 0.8, st + 1.1), lw=12)
    T(c, "TRAP", 540, 530, 130, RED, k(t, st + 1.1, st + 1.4), lw=14)
    T(c, "1 of the govt's 13 dark patterns", 540, 650, 46, WHITE, k(t, st + 2.6, st + 2.9), lw=6)
    a = k(t, st + 5.0, st + 5.3)
    T(c, "JOIN: 1 click", 540, 820, 70, GRN, a, lw=10)
    if t > st + 6.2:
        for i in range(10):
            a2 = k(t, st + 6.2 + i * 0.08, st + 6.3 + i * 0.08)
            S.rrect(c, 330 + i * 16, 900 + i * 22, 300, 180, 18); c.set_source_rgba(0.2, 0.22, 0.3, a2); c.fill_preserve()
            c.set_source_rgba(0.5, 0.52, 0.6, a2); c.set_line_width(3); c.stroke()
        T(c, "CANCEL: 10 screens", 540, 1350, 70, RED, k(t, st + 6.6, st + 6.9), lw=10)


def o_rbi(c, t, lt):
    st = sh.s(5)
    K.panel(c, 860, 520)
    T(c, "RBI RULE", 540, 950, 60, GRN, stroke=None)
    K.rows(c, t, st, [("Alert at least", WHITE, 46, 2.0), ("24 HRS BEFORE", YEL, 66, 2.6),
                      ("every auto-debit", WHITE, 46, 3.2), ("Cancel ANYTIME", GRN, 56, 6.2)], y0=1050, gap=88)


def o_rule(c, t, lt):
    st = sh.s(6)
    K.panel(c, 860, 520)
    T(c, "TOOK A TRIAL?", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Set a reminder TODAY", WHITE, 46, 1.6, "left", 160),
                      ("2. UPI app > AutoPay", GRN, 46, 3.8, "left", 160),
                      ("3. Cancel what you don't use", WHITE, 44, 5.6, "left", 160)], y0=1070, gap=100)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WITH 5 SUBSCRIPTIONS", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: room(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), rw(mouth='smile'), (1.9, 1000, 480), (2.1, 1000, 450), o_trial, 'phone'),
        (s(2), s(3), lambda c, t, lt: metro(c, t, lt, mouth='o' if t > s(2) + 2.6 else 'flat', eyes=1.2 if t > s(2) + 2.6 else 1,
                                            sweat=1 if t > s(2) + 2.6 else 0),
         (1.9, 960, 480), (2.1, 960, 450), o_sms, 'day'),
        (s(3), s(4), sw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 960, 500), (2.0, 960, 470), o_why, 'studio'),
        (s(4), s(5), sw(), (1.78, 960, 540), (1.85, 960, 520), o_trap, 'studio'),
        (s(5), s(6), sw(mouth='smile'), (1.9, 960, 500), (2.0, 960, 470), o_rbi, 'studio'),
        (s(6), s(7), rw(mode='day', mouth='smirk', squint=0.4), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'morning'),
        (s(7), sh.dur + 1, rw(mode='day', mouth='smile', phone=None, arms=((14, -10), (100, 40))), (1.9, 1000, 500),
         (2.1, 1000, 470), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1, 5] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
