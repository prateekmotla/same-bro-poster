import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s66_easy"
CAPS = [
    "When dopamine is THIS easy, why put in effort? This is my OPINION, science hasn't proven it. But think.",
    "2 AM. Sid alone, phone, adult content. Two minutes, and the brain is happy.",
    "The brain is lazy. It picks the EASIEST reward. Junk food over cooking. Reels over a book.",
    "If it becomes your default escape, the effort real connection needs, talking, confidence, going out, starts getting skipped.",
    "Same bro? Bored, stressed, and straight to that?",
    "Fix: don't make it your default escape. Put that energy into the gym, friends, talking to people.",
    "And if it feels compulsive, out of control, talk to a doctor. Nothing to be ashamed of.",
    "MORAL: Easy dopamine makes you lazy for the real thing.",
    "Send this to the friend who's online till 2 AM every night.",
]
HOOK = [("WHY TRY WHEN", WHITE), ("IT'S THIS EASY?", YEL), ("(AN OPINION)", GREY)]
SRC = "Opinion / habit logic, not medical advice. Compulsive? See a doctor."
sh = None


def tab_scr(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.1, 0.1, 0.13); c.fill()
    T(c, "Private tab", w / 2, 90, 36, GREY, stroke=None)
    for i in range(3):
        S.rrect(c, 40, 170 + i * 200, w - 80, 170, 18); c.set_source_rgb(0.2, 0.2, 0.26); c.fill()
        T(c, "18+", w / 2, 270 + i * 200, 44, (0.45, 0.45, 0.55), stroke=None)
    T(c, "2:04 AM", w / 2, h - 60, 34, GREY, stroke=None)


def rw(mode='night', **kw):
    def f(c, t, lt):
        V.room(c, t, mode, fan=False)
        d = dict(pose='stand', mouth='flat')
        d.update(kw)
        K.sid(c, t, 1000, 330, 0.5, **d)
    return f


def stw(**kw):
    def f(c, t, lt):
        V.street(c, t, off=t * 25, night=False)
        d = dict(pose='stand', mouth='smile')
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
    K.panel(c, 1010, 340)
    K.rows(c, t, st, [("THE LAZIEST", WHITE, 64, 0.2), ("DOPAMINE HIT", YEL, 72, 1.0)], y0=1120, gap=120)
    K.stamp(c, t, st + 4.0, "OPINION, NOT SCIENCE", 540, 1335, GREY, 40, -0.03)


def o_night(c, t, lt):
    st = sh.s(2)
    U.phone_frame(c, 290, 480, 500, 760, tab_scr, t - st, tilt=-2 + 3 * lt)
    K.stamp(c, t, st + 3.8, "2 MIN. ZERO EFFORT.", 540, 1340, RED, 48, -0.05)


def o_lazy(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "BRAIN PICKS THE EASIEST", 540, 470, 56, YEL, k(t, st + 0.1, st + 0.4), lw=8)
    pairs = [("COOKING", "JUNK FOOD", 2.6), ("A BOOK", "REELS", 4.2)]
    for i, (hard, easy, dt) in enumerate(pairs):
        a = k(t, st + dt, st + dt + 0.3)
        if a > 0:
            y = 640 + i * 220
            S.rrect(c, 120, y, 380, 150, 24); c.set_source_rgba(0.2, 0.22, 0.3, a); c.fill()
            T(c, hard, 310, y + 92, 48, GREY, a, stroke=None)
            S.rrect(c, 580, y, 380, 150, 24); c.set_source_rgba(0.45, 0.1, 0.12, a); c.fill()
            T(c, easy, 770, y + 92, 48, WHITE, a, stroke=None)
            T(c, ">", 540, y + 95, 60, YEL, a, stroke=None)


def o_skip(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "DEFAULT ESCAPE =", 540, 470, 60, WHITE, k(t, st + 0.1, st + 0.4), lw=8)
    for i, lab in enumerate(["TALKING", "CONFIDENCE", "GOING OUT"]):
        a = k(t, st + 2.6 + i * 0.8, st + 2.9 + i * 0.8)
        if a > 0:
            y = 620 + i * 150
            S.rrect(c, 200, y, 680, 110, 22); c.set_source_rgba(0.18, 0.2, 0.26, a); c.fill()
            T(c, lab, 540, y + 72, 52, WHITE, a, stroke=None)
            c.move_to(230, y + 56); c.line_to(850, y + 56); c.set_source_rgba(*RED, a); c.set_line_width(8); c.stroke()
    K.stamp(c, t, st + 5.6, "EFFORT SKIPPED", 540, 1140, RED, 52, -0.04)


def o_same(c, t, lt):
    st = sh.s(5)
    K.panel(c, 900, 420)
    K.rows(c, t, st, [("BORED. STRESSED.", WHITE, 60, 0.3), ("STRAIGHT TO THAT?", YEL, 58, 1.3)], y0=1010, gap=110)
    K.stamp(c, t, st + 2.2, "SAME BRO?", 540, 1250, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(6)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Not your default", WHITE, 48, 0.3, "left", 140),
                      ("    stress/boredom escape", WHITE, 44, 0.3, "left", 140),
                      ("2. Spend that energy on:", WHITE, 46, 2.6, "left", 140),
                      ("    GYM. FRIENDS. PEOPLE.", GRN, 48, 3.6, "left", 140)], y0=1000, gap=90)


def o_doc(c, t, lt):
    st = sh.s(7)
    K.full(c, t, st, [("FEELS COMPULSIVE?", WHITE, 70, 0.2), ("TALK TO A DOCTOR", GRN, 80, 2.0), ("NO SHAME IN IT", YEL, 60, 4.4)],
           y0=600, gap=170)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "EASY DOPAMINE MAKES", "YOU LAZY FOR REAL LIFE.", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "ONLINE TILL 2 AM", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (60, 120)))
    sh.shots = [
        (0, s(2), rw(mouth='smirk', **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'night'),
        (s(2), s(3), rw(mouth='flat', eyes=0.8, bags=0.6, glow=0.4, **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_night, 'night'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_lazy, 'studio'),
        (s(4), s(5), sw(mouth='frown'), (1.78, 960, 540), (1.85, 960, 520), o_skip, 'red'),
        (s(5), s(6), rw(mouth='frown', bags=0.6, **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'night'),
        (s(6), s(7), stw(arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(7), s(8), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_doc, 'money'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, stw(arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
