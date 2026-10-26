import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import envx as X  # noqa: E402
import body as B  # noqa: E402
import env as V  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s14_scarcity"
CAPS = [
    "1 AM. Sid's looking at sneakers. In red: \"ONLY 2 LEFT!\" And a timer: 9 minutes.",
    "PANIC. Sid hits buy without thinking.",
    "Listen. This is called FALSE URGENCY. A dark pattern.",
    "On many sites, refresh the page and the timer starts AGAIN. Same deal, same panic.",
    "Why? When your brain thinks it'll MISS OUT, it stops thinking. It doesn't compare. It just buys.",
    "That's why in 2023 the government listed 13 DARK PATTERNS, and false urgency is one of them. It's NOT allowed.",
    "Simple rule: see a timer? Add to cart and WAIT 24 hours. Check the price history.",
    "If you really need it, you'll still need it tomorrow.",
    "Send this to the friend who pulls out his card at every \"only 2 left\".",
]
HOOK = [("\"ONLY 2 LEFT\"", RED), ("THE TRICK", WHITE), ("BEHIND IT", YEL)]
SRC = "Source: CCPA Dark Patterns Guidelines, 2023"
sh = None
GREY = (0.55, 0.57, 0.65)


def room(c, t, lt, mode='night', **kw):
    V.room(c, t, mode)
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1, mouth='flat')
    d.update(kw)
    B.figure(c, 1000, 330, 0.5, t, **d)


def timer_txt(sec):
    sec = max(0, int(sec))
    return f"Ends in {sec // 60:02d}:{sec % 60:02d}"


def o_shop(c, t, lt):
    tm = timer_txt(9 * 60 - t * 7)
    U.phone_frame(c, 240, 300, 600, 1060, X.shop_phone_screen(3499, 6999, 50, t, stock="Only 2 left!", timer=tm), t,
                  tilt=-2 + math.sin(t * 20) * 0.6 * k(t, 3, 4))


def o_buy(c, t, lt):
    S.rrect(c, 140, 880, 800, 380, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
    a = k(t, sh.s(2) + 1.0, sh.s(2) + 1.2)
    sc = 1 + 0.4 * (1 - U.eob(a))
    c.save(); c.translate(540, 1060); c.scale(sc, sc)
    T(c, "ORDER PLACED", 0, 0, 80, GRN, a, lw=10)
    T(c, "₹3,499", 0, 110, 70, WHITE, a, stroke=None)
    c.restore()


def o_label(c, t, lt):
    U.dim(c, 0.85)
    T(c, "FALSE", 540, 640, 180, RED, k(t, sh.s(3) + 1.0, sh.s(3) + 1.3), lw=18)
    T(c, "URGENCY", 540, 820, 160, RED, k(t, sh.s(3) + 1.3, sh.s(3) + 1.6), lw=18)
    T(c, "a DARK PATTERN", 540, 980, 70, YEL, k(t, sh.s(3) + 2.4, sh.s(3) + 2.7))


def refresh_icon(c, x, y, r, a, rot):
    c.save(); c.translate(x, y); c.rotate(rot)
    c.set_line_width(14); c.set_source_rgba(*YEL, a)
    c.arc(0, 0, r, 0.3, 2 * math.pi - 0.3); c.stroke()
    c.move_to(r * math.cos(-0.3) + 22, r * math.sin(-0.3) - 6); c.line_to(r * math.cos(-0.3) - 4, r * math.sin(-0.3) - 30)
    c.line_to(r * math.cos(-0.3) - 14, r * math.sin(-0.3) + 12); c.close_path(); c.fill()
    c.restore()


def o_refresh(c, t, lt):
    U.dim(c, 0.85)
    st = sh.s(4)
    tr = st + 2.6
    sec = 7 - (t - st) * 2 if t < tr else 9 * 60 + 59 - (t - tr)
    col = RED if t < tr else YEL
    T(c, f"{max(0, int(sec)) // 60:02d}:{max(0, int(sec)) % 60:02d}", 540, 700, 220, col, lw=20)
    T(c, "TIMER", 540, 460, 64, WHITE)
    if t > tr - 0.6:
        a = k(t, tr - 0.6, tr - 0.4)
        refresh_icon(c, 540, 950, 90, a, (t - tr) * 6 if t < tr + 0.5 else 3)
        T(c, "REFRESH", 540, 1130, 70, YEL, a)
    if t > tr + 0.8:
        T(c, "STARTS AGAIN", 540, 1260, 70, RED, k(t, tr + 0.8, tr + 1.1))


def o_brain(c, t, lt):
    U.dim(c, 0.85)
    st = sh.s(5)
    rows = [("\"I'LL MISS OUT!\"", RED, 1.5), ("BRAIN STOPS THINKING", WHITE, 3.5), ("no compare", GREY, 5.0),
            ("JUST BUYS", YEL, 6.0)]
    for i, (txt, col, dt) in enumerate(rows):
        T(c, txt, 540, 500 + i * 190, 84 if i != 2 else 60, col, k(t, st + dt, st + dt + 0.3), lw=12)
    if t > st + 5.0:
        a = k(t, st + 5.0, st + 5.3)
        c.move_to(330, 860); c.line_to(750, 860); c.set_source_rgba(*RED, a); c.set_line_width(8); c.stroke()


PATTERNS = ["False urgency", "Basket sneaking", "Confirm shaming", "Forced action", "Subscription trap",
            "Interface interference", "Bait and switch", "Drip pricing", "Disguised ads", "Nagging",
            "Trick question", "SaaS billing", "Rogue malware"]


def o_law(c, t, lt):
    U.dim(c, 0.88)
    st = sh.s(6)
    T(c, "2023 · GOVT LIST", 540, 330, 56, WHITE)
    T(c, "13 DARK PATTERNS", 540, 430, 84, YEL, lw=12)
    for i, p in enumerate(PATTERNS):
        x = 130 + (i % 2) * 430; y = 560 + (i // 2) * 105
        a = k(t, st + 1.0 + i * 0.12, st + 1.2 + i * 0.12)
        hi = i == 0 and t > st + 4.0
        S.rrect(c, x - 20, y - 55, 410, 85, 18)
        c.set_source_rgba(*((0.5, 0.08, 0.1) if hi else (0.12, 0.13, 0.18)), a); c.fill()
        T(c, p, x + 185, y + 2, 38, RED if hi else WHITE, a, stroke=None)
    if t > st + 6.0:
        a = k(t, st + 6.0, st + 6.2)
        c.save(); c.translate(540, 1320); c.rotate(-0.06)
        S.rrect(c, -170, -55, 340, 110, 18); c.set_source_rgba(*RED, a); c.fill()
        T(c, "NOT ALLOWED", 0, 18, 46, WHITE, a, stroke=None)
        c.restore()


def o_rule(c, t, lt):
    st = sh.s(7)
    S.rrect(c, 90, 860, 900, 500, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
    T(c, "SEE A TIMER?", 540, 950, 62, YEL, stroke=None)
    T(c, "1. Add to cart", 160, 1060, 48, WHITE, k(t, st + 1.2, st + 1.5), stroke=None, anchor="left")
    T(c, "2. WAIT 24 hours", 160, 1160, 48, GRN, k(t, st + 2.4, st + 2.7), stroke=None, anchor="left")
    T(c, "3. Check price history", 160, 1260, 48, WHITE, k(t, st + 4.0, st + 4.3), stroke=None, anchor="left")


def o_calm(c, t, lt):
    S.rrect(c, 90, 900, 900, 360, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
    T(c, "REALLY NEED IT?", 540, 1010, 64, WHITE, stroke=None)
    T(c, "It'll still be there", 540, 1110, 56, GRN, k(t, sh.s(8) + 1.0, sh.s(8) + 1.3), stroke=None)
    T(c, "TOMORROW", 540, 1200, 64, GRN, k(t, sh.s(8) + 1.3, sh.s(8) + 1.6), stroke=None)


def o_end(c, t, lt):
    S.rrect(c, 140, 900, 800, 230, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    T(c, "SEND TO THE", 540, 1000, 60, WHITE, stroke=None)
    T(c, "\"ONLY 2 LEFT\" BUYER", 540, 1085, 62, YEL, stroke=None)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    r = lambda **kw: (lambda c, t, lt: room(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), r(eyes=1.1), (1.9, 1000, 480), (2.1, 1000, 450), o_shop, 'phone'),
        (s(2), s(3), r(mouth='o', eyes=1.2, sweat=1), (2.0, 1000, 500), (2.2, 1000, 470), o_buy, 'red'),
        (s(3), s(4), r(), (1.78, 960, 540), (1.85, 960, 520), o_label, 'red'),
        (s(4), s(5), r(), (1.78, 960, 540), (1.85, 960, 520), o_refresh, 'night'),
        (s(5), s(6), r(), (1.78, 960, 540), (1.85, 1000, 540), o_brain, 'night'),
        (s(6), s(7), r(), (1.78, 960, 540), (1.85, 960, 540), o_law, 'night'),
        (s(7), s(8), r(mode='day', mouth='smirk', squint=0.4, glow=0.3), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'morning'),
        (s(8), s(9), r(mode='day', mouth='smile', glow=0.3), (1.9, 1000, 500), (2.0, 1000, 480), o_calm, 'morning'),
        (s(9), sh.dur + 1, r(mode='day', mouth='smirk', phone=None, arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1, 3.5] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
