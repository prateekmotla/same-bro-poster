import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s59_trainlate"
CAPS = [
    "Guess: your train is 3+ hours late and your plan is dead. Is your ticket money gone?",
    "Sid at the station. Board: 'RUNNING LATE'. Plan over. He thinks: cancel = cancellation charges.",
    "Rule: train late by MORE than 3 hours + you don't travel = FULL fare refund.",
    "The catch: e-ticket? File a TDR on IRCTC BEFORE the train actually departs. Counter ticket? Surrender it at the counter.",
    "This money doesn't come on its own. No TDR = no refund.",
    "Same bro? Train was late and you just let the ticket go waste?",
    "Fix: check live status. 3+ hrs late and not going? IRCTC > File TDR > 'Train late more than 3 hours'. Done.",
    "MORAL: A late train isn't your fault. Don't pay for it.",
    "Send this to the friend who always takes the train home.",
]
HOOK = [("TRAIN 3 HRS LATE?", WHITE), ("GET A FULL", YEL), ("REFUND", GRN)]
SRC = "Source: Indian Railways refund rules (TDR: train late > 3 hrs, passenger not travelled)"
sh = None


def station(c, t, night=False):
    box, text, light, lg = V.box, V.text, V.light, V.lingrad
    c.set_source(lg(c, 0, 0, 0, 800, [(0, (0.55, 0.6, 0.66) if not night else (0.08, 0.09, 0.14)), (1, (0.75, 0.72, 0.66) if not night else (0.18, 0.16, 0.2))]))
    c.rectangle(0, 0, V.W, V.H); c.fill()
    # roof trusses
    box(c, 0, 0, V.W, 60, (0.35, 0.33, 0.3))
    for i in range(12):
        c.move_to(i * 170, 60); c.line_to(i * 170 + 85, 140); c.line_to(i * 170 + 170, 60)
        c.set_source_rgb(0.3, 0.28, 0.26); c.set_line_width(8); c.stroke()
    # pillars
    for x in (560, 1440):
        box(c, x, 60, 40, 720, (0.45, 0.22, 0.18))
    # departure board
    box(c, 650, 50, 720, 190, (0.05, 0.05, 0.06), 10, (0.4, 0.4, 0.42), 6)
    text(c, "TRAIN      TO        EXP. TIME", 1010, 92, 24, (1, 0.7, 0.2))
    text(c, "12xxx      DELHI     RUNNING LATE", 1010, 145, 26, (1, 0.7, 0.2))
    blink = int(t * 2) % 2 == 0
    text(c, "DELAYED 3:30 HRS", 1010, 210, 32, (1, 0.25, 0.2) if blink else (0.6, 0.15, 0.1))
    # platform + yellow edge + track
    box(c, 0, 760, V.W, 160, (0.6, 0.58, 0.55) if not night else (0.3, 0.3, 0.32))
    box(c, 0, 900, V.W, 20, (0.95, 0.8, 0.15))
    box(c, 0, 920, V.W, 160, (0.25, 0.22, 0.2))
    for i in range(30):
        box(c, i * 70, 960, 40, 100, (0.4, 0.3, 0.2))
    box(c, 0, 980, V.W, 10, (0.6, 0.6, 0.65)); box(c, 0, 1040, V.W, 10, (0.6, 0.6, 0.65))
    # bench
    box(c, 1180, 640, 260, 24, (0.3, 0.45, 0.6)); box(c, 1200, 664, 16, 100, (0.2, 0.2, 0.22)); box(c, 1400, 664, 16, 100, (0.2, 0.2, 0.22))
    if night:
        light(c, 1010, 270, 420, (1, 0.7, 0.3), 0.15)


def stw(night=False, **kw):
    def f(c, t, lt):
        station(c, t, night)
        d = dict(pose='stand', mouth='flat')
        d.update(kw)
        K.sid(c, t, 1000, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 900, 420)
    K.rows(c, t, st, [("3+ HOURS LATE...", WHITE, 62, 0.4), ("MONEY GONE?", RED, 66, 3.4)], y0=1030, gap=120)


def o_board(c, t, lt):
    st = sh.s(2)
    K.panel(c, 900, 420)
    T(c, "PLAN: CANCELLED", 540, 1020, 56, WHITE, k(t, st + 2.0, st + 2.3), stroke=None)
    T(c, "'CANCEL = CHARGES?'", 540, 1130, 54, YEL, k(t, st + 4.0, st + 4.3), stroke=None)


def o_rule(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "THE RULE", 540, 420, 64, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    K.rows(c, t, st, [("Train late > 3 HOURS", WHITE, 62, 1.0), ("+ you DON'T travel", WHITE, 62, 3.0)], y0=600, gap=120)
    K.stamp(c, t, st + 5.0, "= FULL REFUND", 540, 920, GRN, 84, -0.03)


def o_catch(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "THE CATCH", 540, 420, 64, YEL, k(t, st + 0.1, st + 0.4), lw=8)
    K.rows(c, t, st, [("E-TICKET:", GRN, 56, 1.2), ("File TDR on IRCTC", WHITE, 54, 1.8),
                      ("BEFORE the train leaves", WHITE, 54, 3.4),
                      ("COUNTER TICKET:", GRN, 56, 6.4), ("Surrender at the counter", WHITE, 52, 7.2)], y0=580, gap=105)


def o_notdr(c, t, lt):
    st = sh.s(5)
    K.panel(c, 880, 460)
    T(c, "NOT AUTOMATIC", 540, 1010, 62, WHITE, k(t, st + 0.3, st + 0.6), stroke=None)
    K.stamp(c, t, st + 2.0, "NO TDR = NO REFUND", 540, 1180, RED, 60, -0.04)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("TRAIN LATE, TICKET", WHITE, 56, 0.4), ("JUST WASTED?", YEL, 60, 1.6)], y0=1000, gap=110)
    K.stamp(c, t, st + 2.6, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def tdr_scr(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.95, 0.95, 0.97); c.fill()
    c.rectangle(0, 0, w, 120); c.set_source_rgb(0.15, 0.3, 0.6); c.fill()
    T(c, "File TDR", w / 2, 80, 40, WHITE, stroke=None)
    T(c, "Select reason:", 40, 200, 30, (0.3, 0.3, 0.35), stroke=None, anchor="left")
    for i, (r, on) in enumerate([("AC not working", False), ("Train late more than", True), ("Party partially travelled", False)]):
        y = 250 + i * 110
        S.rrect(c, 30, y, w - 60, 90, 14); c.set_source_rgb(*((0.85, 0.95, 0.87) if on else (1, 1, 1))); c.fill()
        c.arc(70, y + 45, 16, 0, 6.3); c.set_source_rgb(*((0.1, 0.6, 0.3) if on else (0.7, 0.7, 0.7))); c.fill()
        T(c, r, 105, y + 45 + (0 if not on else -12), 26, (0.15, 0.15, 0.2), stroke=None, anchor="left")
        if on:
            T(c, "3 hours, not travelled", 105, y + 70, 24, (0.15, 0.15, 0.2), stroke=None, anchor="left")
    S.rrect(c, 60, h - 150, w - 120, 90, 20); c.set_source_rgb(0.95, 0.5, 0.1); c.fill()
    T(c, "SUBMIT", w / 2, h - 92, 36, WHITE, stroke=None)


def o_fix(c, t, lt):
    st = sh.s(7)
    if t < st + 4.0:
        K.panel(c, 820, 560)
        T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
        K.rows(c, t, st, [("1. Check live status", WHITE, 48, 0.2, "left", 140),
                          ("2. 3+ hrs late & not going?", WHITE, 46, 1.8, "left", 140)], y0=1020, gap=100)
    else:
        U.phone_frame(c, 290, 560, 500, 820, tdr_scr, t - st, tilt=-2 + 2 * lt)
        K.stamp(c, t, st + 7.0, "DONE", 540, 1300, GRN, 64, -0.05)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "LATE TRAIN? NOT YOUR FAULT.", "DON'T PAY FOR IT.", GRN)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO TAKES THE TRAIN HOME", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    sh.shots = [
        (0, s(2), stw(mouth='o', eyes=1.3), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'warm'),
        (s(2), s(3), stw(mouth='frown', squint=0.3, arms=((60, 120), (14, -10))), (1.7, 1010, 420), (1.95, 1000, 430), o_board, 'warm'),
        (s(3), s(4), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_rule, 'studio'),
        (s(4), s(5), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_catch, 'money'),
        (s(5), s(6), stw(night=True, mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_notdr, 'night'),
        (s(6), s(7), stw(night=True, mouth='frown'), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'night'),
        (s(7), s(8), stw(mouth='smile', phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, stw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
