import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s55_monday"
CAPS = [
    "Guess: why does every diet, gym plan and 'new me' start on a MONDAY?",
    "Sunday night, Sid: 'From tomorrow. Gym. Diet. Phone off.'",
    "Wharton researchers call it the 'fresh start effect'. New week = your brain feels like a new you.",
    "Proof: people picked a 'first day of spring' start date 3.5x more often. 26% vs 7%.",
    "The catch: the fresh-start feeling fades. The old habit doesn't. Big plan, zero system.",
    "Same bro? Restarted on 10 different Mondays?",
    "Fix: use the Monday boost, but keep it tiny: 10 pushups, 1 salad. Missed a day? Restart the next day.",
    "MORAL: Monday gives the spark. Tiny habits keep it alive.",
    "Send this to the friend whose diet starts every Monday.",
]
HOOK = [("WHY DOES EVERY", WHITE), ("DIET START", YEL), ("ON MONDAY?", RED)]
SRC = "Source: Dai, Milkman & Riis, Psychological Science (2015) & Mgmt Science (2014)"
sh = None


def room(c, t, lt, mode='night', **kw):
    V.room(c, t, mode, fan=False)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def cal(c, t, st, x0=150, y0=760, crossed=0):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    a = k(t, st + 0.1, st + 0.4)
    S.rrect(c, x0, y0, 780, 300, 22); c.set_source_rgba(0.98, 0.97, 0.94, 0.97 * a); c.fill()
    for i, d in enumerate(days):
        x = x0 + 60 + i * 110
        col = RED if i == 0 else (0.2, 0.2, 0.24)
        T(c, d, x, y0 + 80, 34, col, a, stroke=None)
        if i == 0:
            c.arc(x, y0 + 180, 46, 0, 6.3); c.set_source_rgba(*RED, 0.9 * a); c.set_line_width(6); c.stroke()
            T(c, "NEW ME", x, y0 + 190, 22, RED, a, stroke=None)
        elif i < 1 + crossed:
            c.move_to(x - 30, y0 + 150); c.line_to(x + 30, y0 + 210); c.move_to(x + 30, y0 + 150); c.line_to(x - 30, y0 + 210)
            c.set_source_rgba(0.4, 0.4, 0.45, a); c.set_line_width(6); c.stroke()


def o_guess(c, t, lt):
    st = sh.s(1)
    cal(c, t, st, y0=820)
    K.stamp(c, t, st + 2.6, "ALWAYS MONDAY", 540, 1250, YEL, 58, -0.05)


def o_sunday(c, t, lt):
    st = sh.s(2)
    K.panel(c, 820, 520)
    T(c, "SUNDAY, 11:58 PM", 540, 900, 46, GREY, k(t, st + 0.1, st + 0.4), stroke=None)
    K.rows(c, t, st, [("'From tomorrow...'", YEL, 58, 0.6), ("GYM. DIET. PHONE OFF.", WHITE, 56, 1.4)], y0=1030, gap=110)
    K.stamp(c, t, st + 2.4, "PAKKA.", 540, 1260, GRN, 56, -0.05)


def o_effect(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "WHARTON RESEARCH", 540, 420, 60, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    K.stamp(c, t, st + 1.6, "THE FRESH START EFFECT", 540, 580, YEL, 62, -0.03)
    K.rows(c, t, st, [("New week / month / year", WHITE, 50, 3.6), ("= brain feels like a NEW YOU", GRN, 52, 5.2)], y0=820, gap=105)


def o_proof(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "PICKED A 'FRESH START' DATE", 540, 420, 50, GREY, k(t, st + 0.1, st + 0.4), lw=7)
    K.hbar(c, t, st + 2.4, 140, 640, 800, 100, 0.26 / 0.3, GRN, "'First day of spring'", "26%")
    K.hbar(c, t, st + 3.4, 140, 860, 800, 100, 0.07 / 0.3, RED, "Same day, plain name", "7%")
    T(c, "3.5x MORE", 540, 1080, 90, YEL, k(t, st + 1.2, st + 1.5), lw=10)


def o_catch(c, t, lt):
    st = sh.s(5)
    cal(c, t, st - 0.4, y0=760, crossed=min(6, int(max(0, t - st) * 1.3)))
    K.panel(c, 1100, 230, 140, 800, 0.9)
    T(c, "BIG PLAN, ZERO SYSTEM", 540, 1235, 52, RED, k(t, st + 4.0, st + 4.3), stroke=None)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("RESTARTED ON", WHITE, 60, 0.2), ("10 DIFFERENT MONDAYS?", YEL, 56, 0.8)], y0=1000, gap=110)
    K.stamp(c, t, st + 1.8, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(7)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Use the Monday boost", WHITE, 46, 0.3, "left", 140),
                      ("2. Keep it TINY: 10 pushups", WHITE, 46, 2.4, "left", 140),
                      ("3. Missed? Restart NEXT DAY", GRN, 46, 4.8, "left", 140)], y0=1020, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "MONDAY = THE SPARK", "TINY HABITS = THE FIRE", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHOSE DIET STARTS MONDAY", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    rn = lambda **kw: (lambda c, t, lt: room(c, t, lt, 'night', **kw))
    rd = lambda **kw: (lambda c, t, lt: room(c, t, lt, 'day', **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), rd(mouth='o', eyes=1.2), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'warm'),
        (s(2), s(3), rn(mouth='bigsmile', arms=((60, 120), (14, -10))), (2.0, 1000, 470), (2.15, 1000, 450), o_sunday, 'night'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_effect, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_proof, 'money'),
        (s(5), s(6), rn(mouth='frown', squint=0.3), (1.9, 1000, 480), (2.0, 1000, 460), o_catch, 'night'),
        (s(6), s(7), rd(mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), rd(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rd(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
