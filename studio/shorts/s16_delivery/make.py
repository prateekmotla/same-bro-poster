import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s16_delivery"
CAPS = [
    "Sid orders butter chicken on the app. ₹340. Next day he visits the same restaurant. The menu says ₹300.",
    "NOT a coincidence. Jefferies checked 80 restaurants. 80% charged MORE on the app.",
    "Median? 10-11% more. And 1 in 5 restaurants charged 30% MORE or even higher.",
    "Why? The app takes a COMMISSION on every order. The restaurant puts that cost straight into the menu price.",
    "Plus delivery fee, platform fee, packing charge. Sid thinks he's only paying for delivery. He's paying EXTRA for the food too.",
    "Simple rule: restaurant nearby? Check their direct number or dine-in price. Or just go pick it up.",
    "Send this to the friend who orders on the app even from the dhaba 2 km away.",
]
HOOK = [("SAME FOOD,", WHITE), ("HIGHER PRICE", RED), ("ON THE APP?", YEL)]
SRC = "Source: Jefferies report via Inc42, Aug 2022"
sh = None


def room(c, t, lt, **kw):
    V.room(c, t, 'night')
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1)
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def street(c, t, lt, **kw):
    V.street(c, t, off=t * 40, night=False)
    K.sid(c, t, 960, 330, 0.5, pose='walk', ph=t * 0.9, **kw)


def o_order(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 440)
    T(c, "BUTTER CHICKEN", 540, 960, 54, WHITE, stroke=None)
    K.rows(c, t, st, [("ON APP", GREY, 40, 0.8, "left", 200), ("IN MENU", GREY, 40, 4.5, "left", 200)], y0=1080, gap=150)
    if t > st + 1.2:
        T(c, "₹340", 880, 1095, 90, RED, k(t, st + 1.2, st + 1.5), stroke=None, anchor="right")
    if t > st + 4.8:
        T(c, "₹300", 880, 1245, 90, GRN, k(t, st + 4.8, st + 5.1), stroke=None, anchor="right")


def o_80(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "80 RESTAURANTS CHECKED", 540, 380, 62, WHITE, k(t, st + 0.8, st + 1.1), lw=8)
    for i in range(80):
        x = 180 + (i % 10) * 80; y = 520 + (i // 10) * 80
        a = k(t, st + 1.2 + i * 0.015, st + 1.4 + i * 0.015)
        red = i < 64 and t > st + 3.2
        c.arc(x, y, 28, 0, 2 * math.pi); c.set_source_rgba(*(RED if red else (0.5, 0.52, 0.6)), a); c.fill()
    if t > st + 3.2:
        T(c, "80% = PRICIER ON APP", 540, 1250, 70, RED, k(t, st + 3.2, st + 3.5), lw=10)


def o_median(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "HOW MUCH MORE?", 540, 420, 72, WHITE, lw=10)
    K.hbar(c, t, st + 0.6, 140, 640, 800, 70, 0.27, YEL, "Typical (median)", "10-11%")
    K.hbar(c, t, st + 2.8, 140, 860, 800, 70, 0.75, RED, "1 in 5 restaurants", "30%+")
    if t > st + 4.0:
        T(c, "some went above 60%", 540, 1080, 52, GREY, k(t, st + 4.0, st + 4.3), lw=6)


def o_comm(c, t, lt):
    st = sh.s(4)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("APP takes COMMISSION", YEL, 50, 0.8),
                      ("on every order", WHITE, 42, 1.3),
                      ("Restaurant adds it", WHITE, 48, 3.6),
                      ("to YOUR menu price", RED, 52, 4.2)], y0=960, gap=105)


FEES = [("Butter chicken", "₹340"), ("Delivery fee", "₹35"), ("Platform fee", "₹10"), ("Packing charge", "₹20")]


def o_fees(c, t, lt):
    st = sh.s(5)
    show = 1 + int(min(3, max(0, (t - st - 0.4) / 0.9)))
    hi = [0] if t > st + 6.0 else None
    U.phone_frame(c, 240, 830, 600, 600, K.bill_screen("CHECKOUT", FEES, "₹405", show=show, hi=hi), t, glow=0.2)


def o_rule(c, t, lt):
    st = sh.s(6)
    K.panel(c, 860, 520)
    T(c, "RESTAURANT NEARBY?", 540, 950, 58, YEL, stroke=None)
    K.rows(c, t, st, [("1. Call them directly", WHITE, 46, 1.6, "left", 170),
                      ("2. Compare dine-in price", GRN, 46, 3.0, "left", 170),
                      ("3. Or just pick it up", WHITE, 46, 4.6, "left", 170)], y0=1070, gap=100)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO ORDERS FROM 2 KM AWAY", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: room(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    stw = lambda **kw: (lambda c, t, lt: street(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), rw(mouth='smile'), (1.9, 1000, 480), (2.1, 1000, 450), o_order, 'phone'),
        (s(2), s(3), sw(), (1.78, 960, 540), (1.85, 960, 520), o_80, 'studio'),
        (s(3), s(4), sw(), (1.78, 960, 540), (1.85, 960, 520), o_median, 'studio'),
        (s(4), s(5), sw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 960, 500), (2.0, 960, 470), o_comm, 'studio'),
        (s(5), s(6), rw(mouth='o', eyes=1.2, sweat=1), (1.9, 1000, 480), (2.0, 1000, 460), o_fees, 'phone'),
        (s(6), s(7), stw(mouth='smile'), (1.9, 960, 500), (2.0, 960, 480), o_rule, 'morning'),
        (s(7), sh.dur + 1, stw(mouth='smirk'), (1.9, 960, 500), (2.1, 960, 470), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1, 5.5] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
