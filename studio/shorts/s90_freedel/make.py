"""THEY'RE TRICKING YOU #3: 'Free delivery above ₹199' = a bigger basket (engine: vshort.Short).
Fact: UPS Pulse of the Online Shopper (UPS/comScore, press release 3 Jun 2015, 5,118 US online shoppers): 60% have
added items to their cart to qualify for free shipping. Free-delivery thresholds are a basket-size lever.
No platform named. Answer: add only what you'd buy anyway, otherwise paying the fee is cheaper."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s90_freedel"
CAPS = [
    "Cart: ₹180. Delivery fee: ₹30. And it says: FREE delivery above ₹199. What do you do?",
    "A: just pay the ₹30. B: add ₹40 of something else. Comment!",
    "That number isn't random. It's set on purpose, so your basket gets BIGGER.",
    "In a UPS study, 60% of shoppers added extra items to their cart just to get free shipping.",
    "So what's right? If you needed that item anyway: B. If not: A, the ₹30 is cheaper.",
    "Free delivery isn't free, your bill just gets bigger. Are you A or B?",
]
HOOK = [("CART ₹180", WHITE), ("FREE ABOVE ₹199", YEL), ("THEY'RE TRICKING YOU #3", GREY)]
SRC = "SRC: UPS Pulse of the Online Shopper, 2015"
sh = None


def cart_screen(added):
    items = [("Bread", "₹45"), ("Milk 1L", "₹68"), ("Eggs x6", "₹67")]
    if added:
        items = items + [("Chips (extra)", "₹40")]
    items = items + [("Delivery fee", "₹0" if added else "₹30")]
    total = "₹220" if added else "₹210"

    def f(c, w, h, tt):
        K.bill_screen("MY CART", items, total, hi=[3] if added else [3], btn="CHECKOUT")(c, w, h, tt)
        if added:
            return
        S.rrect(c, 24, h - 200, w - 48, 70, 18); c.set_source_rgb(0.1, 0.55, 0.25); c.fill()
        T(c, "FREE DELIVERY ABOVE ₹199!", w / 2, h - 153, 30, WHITE, stroke=None)
    return f


def rw(**kw):
    def f(c, t, lt):
        V.room(c, t, 'day', fan=False)
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
    U.phone_frame(c, 290, 480, 500, 780, cart_screen(False), t - st, tilt=-2 + 3 * lt)
    K.stamp(c, t, st + 5.4, "A: PAY ₹30   or   B: ADD ₹40?", 540, 1330, RED, 44, -0.04)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "WHAT DO YOU DO?", 540, 470, 72, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt) in enumerate((("A", "PAY THE ₹30 FEE"), ("B", "ADD ₹40 MORE STUFF"))):
        a = k(t, st + 0.3 + i * 1.6, st + 0.6 + i * 1.6)
        y = 580 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 112, 46, WHITE, a, stroke=None)
    K.stamp(c, t, st + 3.8, "COMMENT A or B", 540, 1120, YEL, 54, -0.03)


def o_random(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.86)
    U.phone_frame(c, 330, 400, 420, 680, cart_screen(True), t - st, tilt=1)
    K.rows(c, t, st, [("₹199 ISN'T RANDOM", YEL, 66, 0.3), ("IT'S SET SO YOUR", WHITE, 52, 2.0),
                      ("BASKET GETS BIGGER", RED, 66, 2.8)], y0=1150, gap=95)


def o_stat(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "UPS SHOPPER STUDY", 540, 520, 56, GREY, k(t, st, st + 0.2), stroke=None)
    a = k(t, st + 0.8, st + 1.2)
    pct = int(60 * U.eob(a))
    T(c, f"{pct}%", 540, 860, 260, YEL, a, lw=16)
    K.rows(c, t, st, [("ADDED EXTRA ITEMS", WHITE, 62, 2.4), ("JUST FOR FREE SHIPPING", GRN, 60, 3.6)], y0=1060, gap=110)


def o_answer(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.9)
    T(c, "SO WHAT'S RIGHT?", 540, 470, 66, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (q, ans, col, d) in enumerate((("NEEDED IT ANYWAY?", "B: ADD IT", GRN, 1.2), ("DON'T NEED IT?", "A: PAY ₹30", YEL, 3.4))):
        a = k(t, st + d, st + d + 0.3)
        y = 580 + i * 280
        S.rrect(c, 110, y, 860, 230, 40); c.set_source_rgba(0.1, 0.12, 0.2, 0.95 * a); c.fill_preserve()
        c.set_source_rgba(*col, a); c.set_line_width(5); c.stroke()
        T(c, q, 540, y + 85, 48, WHITE, a, stroke=None)
        T(c, ans, 540, y + 175, 72, col, a, stroke=None)
    T(c, "₹30 FEE < ₹40 OF STUFF YOU DON'T NEED", 540, 1220, 40, GREY, k(t, st + 4.4, st + 4.7), stroke=None)


def o_end(c, t, lt):
    K.end_card(c, "FREE DELIVERY ISN'T FREE.", "YOUR BILL JUST GROWS.", YEL)
    st = sh.s(6)
    T(c, "A or B? COMMENT", 540, 1260, 64, YEL, k(t, st + 2.4, st + 2.7), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (60, 120)))
    sh.shots = [
        (0, s(2), rw(mouth='flat', squint=0.3, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), rw(mouth='o', eyes=1.2, **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_random, 'red'),
        (s(4), s(5), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_stat, 'money'),
        (s(5), s(6), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_answer, 'studio'),
        (s(6), sh.dur + 1, rw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 3.0, 6.5] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[3][0] + 1.0], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
