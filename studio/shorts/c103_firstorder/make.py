"""THEY'RE TRICKING YOU #6: '₹100 off your first order' = what you cost them (engine: vshort.Short).
Fact: first-order discounts are a customer acquisition cost (CAC) - money spent to win a new customer, earned back
over later orders. Harvard Business Review, 'The Value of Keeping the Right Customers' (Amy Gallo, 29 Oct 2014):
'acquiring a new customer is anywhere from five to 25 times more expensive than retaining an existing one'.
No brand named."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c103_firstorder"
CAPS = [
    "New app, ₹100 off your first order. Free money? Or are YOU the product?",
    "Question: is that ₹100 discount a loss for the company? A: yes, a loss. B: no, it's the price of buying YOU. Comment!",
    "B is right. It's called customer acquisition cost: what they spend to get one new customer.",
    "Harvard Business Review: getting a new customer costs 5 to 25 times more than keeping an old one.",
    "So the first order is cheap, so you get hooked. The real money comes from the next orders.",
    "Take the discount, not the habit. Compare prices before you order. Send this to a friend.",
]
HOOK = [("₹100 OFF FIRST ORDER?", WHITE), ("THEY'RE BUYING YOU", RED), ("THEY'RE TRICKING YOU #6", GREY)]
SRC = "SRC: Harvard Business Review (2014)"
sh = None


def coupon_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.96, 0.99); c.fill()
    T(c, "WELCOME!", w / 2, 110, 40, (0.3, 0.2, 0.6), stroke=None)
    S.rrect(c, 30, 170, w - 60, 250, 26); c.set_source_rgb(0.98, 0.84, 0.2); c.fill()
    T(c, "₹100 OFF", w / 2, 290, 74, (0.1, 0.1, 0.12), stroke=None)
    T(c, "on your FIRST order", w / 2, 360, 28, (0.2, 0.2, 0.25), stroke=None, bold=False)
    S.rrect(c, 60, h - 150, w - 120, 90, 45); c.set_source_rgb(0.2, 0.65, 0.35); c.fill()
    T(c, "ORDER NOW", w / 2, h - 92, 36, WHITE, stroke=None)


def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "evening")
        d = dict(pose='stand', mouth='flat', look=(0.6, 0)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 690, 720, 340, 600, coupon_screen, t - st, tilt=4)
    if t > st + 3.0:
        K.stamp(c, t, st + 3.0, "FREE MONEY?", 300, 1200, YEL, 56, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "₹100 DISCOUNT =", 540, 430, 66, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "COMPANY'S LOSS?", 540, 515, 62, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "YES, A LOSS", 4.5), ("B", "NO, IT BUYS YOU", 6.4))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 610, y + 116, 56, WHITE, a, stroke=None)
    K.stamp(c, t, st + 9.2, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: IT BUYS YOU", 540, 478, 68, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("IT'S CALLED", WHITE, 52, 1.2), ("CUSTOMER", YEL, 84, 1.8), ("ACQUISITION COST", YEL, 72, 2.2),
                      ("= price of 1 new customer", GREY, 42, 4.0)], y0=690, gap=120)


def o_hbr(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "HARVARD BUSINESS REVIEW", 540, 430, 50, WHITE, k(t, st, st + 0.2), lw=8)
    for i, (lab, col, d) in enumerate((("NEW CUSTOMER", RED, 1.8), ("OLD CUSTOMER", GRN, 3.4))):
        a = k(t, st + d, st + d + 0.3)
        y = 560 + i * 200
        S.rrect(c, 110, y, 860, 160, 36); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        T(c, lab, 150, y + 96, 42, col, a, stroke=None, anchor="left")
        # cost bar
        w = 360 if i == 0 else 30
        ga = U.eob(k(t, st + d + 0.3, st + d + 1.0))
        S.rrect(c, 570, y + 55, max(8, w * ga), 50, 14); c.set_source_rgba(*col, a); c.fill()
    a = k(t, st + 4.7, st + 5.0)
    T(c, "5 to 25x", 540, 1080, 130, YEL, a, lw=12)
    T(c, "MORE EXPENSIVE", 540, 1170, 56, WHITE, a, lw=8)


def o_habit(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "ORDER #1", 540, 430, 60, WHITE, k(t, st, st + 0.2), lw=10)
    K.stamp(c, t, st + 0.4, "₹100 OFF", 540, 540, GRN, 60, -0.03)
    for j in range(8):
        d = 1.2 + j * 0.25
        a = k(t, st + d, st + d + 0.2)
        x, y = 200 + (j % 4) * 227, 720 + (j // 4) * 200
        S.rrect(c, x - 90, y - 70, 180, 140, 26); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        T(c, f"#{j + 2}", x, y + 18, 54, YEL, a, stroke=None)
    K.stamp(c, t, st + 3.6, "THE REAL MONEY", 540, 1180, RED, 58, 0.03)


def o_end(c, t, lt):
    K.end_card(c, "TAKE THE DISCOUNT", "NOT THE HABIT", YEL)
    st = sh.s(6)
    T(c, "COMPARE PRICES FIRST", 540, 1260, 54, GRN, k(t, st + 1.8, st + 2.1), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='smile', **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_hbr, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_habit, 'money'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 4.5] + [a + (b - a) * 0.95 for a, b in L[1:]] + [L[3][0] + 6.0], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
