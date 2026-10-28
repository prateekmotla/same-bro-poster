import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, PINK, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s19_dating"
CAPS = [
    "Sid swipes right 100 times on a dating app. Matches? ZERO. Then the app says: buy a Boost, more people will see you. Just a few hundred rupees.",
    "Listen. India's dating apps have a big problem. In a survey by the app Woo, 74% of users were MEN. Women: just 26%.",
    "That's around 3 guys for every girl. Girls' inboxes: FULL. Guys' inboxes: EMPTY.",
    "And THAT's where the money is. The app is free, but to get seen first, or to see who liked you, you PAY.",
    "The more frustrated Sid gets, the more likely he pays. That empty inbox IS their business.",
    "Simple rule: fix your profile before spending money. Good photos, a real bio. And don't make the app your main plan. College, gym, friends, people meet there too.",
    "Send this to the friend who buys dating app premium every month.",
]
HOOK = [("WHY YOU GET", WHITE), ("ZERO MATCHES", RED), ("ON DATING APPS", YEL)]
SRC = "Source: Woo survey of 20,000 users, via Business Insider India"
sh = None


def room(c, t, lt, **kw):
    V.room(c, t, 'night')
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1)
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def canteen(c, t, lt, **kw):
    V.canteen(c, t)
    K.sid(c, t, 1000, 330, 0.5, pose='sit', **kw)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def heart(c, x, y, r, col, a=1.0):
    c.save(); c.translate(x, y); c.scale(r / 50, r / 50)
    c.move_to(0, 35)
    c.curve_to(-70, -10, -40, -70, 0, -35)
    c.curve_to(40, -70, 70, -10, 0, 35)
    c.set_source_rgba(*col, a); c.fill()
    c.restore()


def app_screen(swipes, boost):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.1, 0.06, 0.1); c.fill()
        T(c, "SPARK", w / 2, 90, 46, PINK, stroke=None)
        T(c, "Right swipes", 50, 200, 32, WHITE, stroke=None, anchor="left", bold=False)
        T(c, str(swipes), w - 50, 200, 46, GRN, stroke=None, anchor="right")
        T(c, "Matches", 50, 290, 32, WHITE, stroke=None, anchor="left", bold=False)
        T(c, "0", w - 50, 290, 46, RED, stroke=None, anchor="right")
        if boost:
            S.rrect(c, 30, 340, w - 60, 220, 24); c.set_source_rgb(0.95, 0.35, 0.55); c.fill()
            T(c, "GET A BOOST", w / 2, 420, 46, WHITE, stroke=None)
            T(c, "be seen by more people", w / 2, 480, 28, WHITE, stroke=None, bold=False)
            T(c, "BUY NOW", w / 2, 535, 32, YEL, stroke=None)
    return f


def o_swipe(c, t, lt):
    st = sh.s(1)
    n = int(min(100, max(0, (t - st - 0.3) / 3.0 * 100)))
    U.phone_frame(c, 260, 860, 560, 600, app_screen(n, t > st + 6.0), t, glow=0.25)


def o_ratio(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "DATING APP USERS", 540, 420, 70, WHITE, k(t, st + 2.0, st + 2.3), lw=10)
    T(c, "(Woo survey, India)", 540, 500, 40, GREY, k(t, st + 2.0, st + 2.3), lw=6)
    K.hbar(c, t, st + 4.0, 140, 680, 800, 90, 0.74, BLUE, "MEN", "74%")
    K.hbar(c, t, st + 6.6, 140, 900, 800, 90, 0.26, PINK, "WOMEN", "26%")


def inbox(c, x, y, title, val, col, a):
    S.rrect(c, x - 180, y - 120, 360, 300, 30); c.set_source_rgba(0.12, 0.13, 0.18, a); c.fill()
    T(c, title, x, y - 50, 40, WHITE, a, stroke=None)
    T(c, val, x, y + 90, 110, col, a, stroke=None)


def o_inbox(c, t, lt):
    st = sh.s(3)
    K.panel(c, 850, 560, a=0.85)
    T(c, "~3 GUYS : 1 GIRL", 540, 940, 62, YEL, k(t, st + 0.3, st + 0.6), stroke=None)
    inbox(c, 320, 1140, "HER INBOX", "99+", GRN, k(t, st + 2.4, st + 2.7))
    inbox(c, 760, 1140, "HIS INBOX", "0", RED, k(t, st + 4.0, st + 4.3))


def o_pay(c, t, lt):
    st = sh.s(4)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("APP = FREE", GRN, 56, 1.6),
                      ("Get seen first?", WHITE, 46, 3.4), ("PAY", RED, 60, 3.9),
                      ("See who liked you?  PAY", RED, 46, 5.2)], y0=960, gap=100)


def o_biz(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.86)
    T(c, "MORE FRUSTRATION", 540, 470, 84, RED, k(t, st + 0.3, st + 0.6), lw=12)
    T(c, "=", 540, 590, 90, WHITE, k(t, st + 1.2, st + 1.4), lw=10)
    T(c, "MORE PAYING", 540, 710, 96, YEL, k(t, st + 1.6, st + 1.9), lw=12)
    if t > st + 3.4:
        a = k(t, st + 3.4, st + 3.7)
        heart(c, 540, 930, 90, (0.4, 0.4, 0.45), a)
        T(c, "Empty inbox = THEIR BUSINESS", 540, 1120, 56, WHITE, a, lw=8)


def o_rule(c, t, lt):
    st = sh.s(6)
    K.panel(c, 860, 540)
    T(c, "BEFORE YOU PAY", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Fix photos + real bio", WHITE, 46, 1.8, "left", 160),
                      ("2. App = side plan", GRN, 46, 5.0, "left", 160),
                      ("3. College, gym, friends", WHITE, 46, 7.0, "left", 160)], y0=1070, gap=100)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO BUYS PREMIUM MONTHLY", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: room(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    cw = lambda **kw: (lambda c, t, lt: canteen(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), lambda c, t, lt: room(c, t, lt, mouth='smile' if t < 3.5 else 'frown', eyes=1.0 if t < 3.5 else 0.8),
         (1.9, 1000, 480), (2.1, 1000, 450), o_swipe, 'phone'),
        (s(2), s(3), sw(), (1.78, 960, 540), (1.85, 960, 520), o_ratio, 'studio'),
        (s(3), s(4), cw(mouth='frown'), (1.9, 1000, 500), (2.0, 1000, 470), o_inbox, 'warm'),
        (s(4), s(5), sw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 960, 500), (2.0, 960, 470), o_pay, 'studio'),
        (s(5), s(6), rw(mouth='frown', eyes=0.8, bags=1), (1.78, 960, 540), (1.85, 960, 520), o_biz, 'red'),
        (s(6), s(7), cw(mouth='smile'), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
        (s(7), sh.dur + 1, cw(mouth='smirk', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1, 7.5] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
