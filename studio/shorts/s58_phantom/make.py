import sys
import math

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s58_phantom"
CAPS = [
    "Guess: your phone buzzed in your pocket. You check... no notification. Why?",
    "Sid in class. Buzz. Checks the phone. Nothing. 2 minutes later: buzz. Nothing.",
    "It's called 'phantom vibration'. Your brain waits for messages so hard, it reads a shirt rub as a notification.",
    "Not rare: in one study, 89% of college students had it. Almost 9 in 10.",
    "And apps love it: more notifications = more checking = more screen time.",
    "Same bro? Felt a buzz in your pocket while the phone was in your hand?",
    "Fix: turn vibration off. Keep notifications only for apps that matter. Keep the phone in your bag, not your pocket.",
    "MORAL: Not every buzz is real. You run the phone, not the other way round.",
    "Send this to the friend who checks his phone every 2 minutes.",
]
HOOK = [("YOUR PHONE", WHITE), ("BUZZED...", YEL), ("OR DID IT?", RED)]
SRC = "Source: Drouin, Kaiser & Miller, Computers in Human Behavior (2012)"
sh = None


def lock_scr(c, w, h, tt):
    c.set_source(V.lingrad(c, 0, 0, 0, h, [(0, (0.15, 0.12, 0.3)), (1, (0.05, 0.05, 0.12))])); c.rectangle(0, 0, w, h); c.fill()
    T(c, "10:42", w / 2, 220, 120, WHITE, stroke=None)
    T(c, "Monday, 9 November", w / 2, 300, 32, GREY, stroke=None)
    S.rrect(c, 40, 420, w - 80, 120, 24); c.set_source_rgba(1, 1, 1, 0.12); c.fill()
    T(c, "No new notifications", w / 2, 492, 36, WHITE, stroke=None)


def buzz(c, t, x, y, a=1.0):
    ph = (t * 6) % 1
    for i in range(3):
        r = 60 + i * 40 + ph * 30
        c.arc(x, y, r, -0.6, 0.6); c.set_source_rgba(*YEL, a * (1 - ph) * 0.9); c.set_line_width(8); c.stroke()
        c.arc(x, y, r, math.pi - 0.6, math.pi + 0.6); c.stroke()


def cw(**kw):
    def f(c, t, lt):
        V.canteen(c, t)
        d = dict(pose='stand', mouth='flat')
        d.update(kw)
        K.sid(c, t, 1000, 330, 0.5, **d)
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


def o_guess(c, t, lt):
    st = sh.s(1)
    if t < st + 2.5:
        buzz(c, t, 600, 1250)
        K.stamp(c, t, st + 0.5, "BZZZ", 600, 1250, YEL, 70, -0.08)
    else:
        U.phone_frame(c, 290, 560, 500, 800, lock_scr, t - st, tilt=-2 + 3 * lt)
        K.stamp(c, t, st + 3.2, "...NOTHING?", 540, 1300, RED, 60, -0.05)


def o_class(c, t, lt):
    st = sh.s(2)
    K.panel(c, 900, 420)
    on1 = st + 0.8 < t < st + 1.6
    on2 = st + 4.4 < t < st + 5.2
    if on1 or on2:
        buzz(c, t, 540, 760)
    K.rows(c, t, st, [("BUZZ. CHECK. NOTHING.", WHITE, 54, 1.0), ("2 MIN LATER: SAME.", YEL, 54, 4.4)], y0=1030, gap=120)


def o_brain(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "IT HAS A NAME", 540, 420, 56, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    K.stamp(c, t, st + 1.0, "PHANTOM VIBRATION", 540, 560, YEL, 66, -0.03)
    K.rows(c, t, st, [("Brain waits for messages", WHITE, 52, 3.0), ("shirt rub = 'notification'", RED, 54, 6.0)], y0=800, gap=120)


def o_data(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "COLLEGE STUDENTS WHO FELT IT", 540, 450, 50, GREY, k(t, st + 0.3, st + 0.6), lw=7)
    a = k(t, st + 1.6, st + 2.6)
    T(c, f"{int(89 * U.eob(a))}%", 540, 690, 180, YEL, a, lw=14)
    for i in range(10):
        x = 165 + i * 83
        on = i < 9
        c.arc(x, 920, 30, 0, 6.3)
        c.set_source_rgba(*(RED if on else GREY), k(t, st + 4.0 + i * 0.08, st + 4.3 + i * 0.08)); c.fill()
    T(c, "~9 IN 10", 540, 1040, 64, WHITE, k(t, st + 5.0, st + 5.3), lw=8)


def o_apps(c, t, lt):
    st = sh.s(5)
    K.panel(c, 820, 560)
    K.rows(c, t, st, [("MORE NOTIFICATIONS", WHITE, 52, 1.0), ("= MORE CHECKING", YEL, 54, 2.6),
                      ("= MORE SCREEN TIME", RED, 56, 4.0)], y0=980, gap=120)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("PHONE IN YOUR HAND,", WHITE, 56, 0.4), ("BUZZ IN YOUR POCKET?", YEL, 54, 1.6)], y0=1000, gap=110)
    K.stamp(c, t, st + 2.6, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(7)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Vibration OFF", WHITE, 48, 0.3, "left", 140),
                      ("2. Alerts only for", WHITE, 48, 1.8, "left", 140),
                      ("    apps that matter", WHITE, 48, 1.8, "left", 140),
                      ("3. Phone in bag, not pocket", GRN, 46, 5.0, "left", 140)], y0=1010, gap=90)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "NOT EVERY BUZZ IS REAL.", "YOU RUN THE PHONE.", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO CHECKS EVERY 2 MIN", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    sh.shots = [
        (0, s(2), rw(mouth='o', eyes=1.3), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'night'),
        (s(2), s(3), cw(mouth='frown', squint=0.3, phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 480), (2.05, 1000, 455), o_class, 'warm'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_brain, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_data, 'money'),
        (s(5), s(6), rw(mouth='smirk', phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 500), (2.0, 1000, 470), o_apps, 'night'),
        (s(6), s(7), cw(mouth='frown', phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), rw('day', mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw('day', mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
