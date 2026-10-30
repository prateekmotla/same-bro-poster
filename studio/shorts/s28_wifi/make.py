import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s28_wifi"
CAPS = [
    "Café board: FREE WI-FI. Sid types his phone number and OTP. Connected in 10 seconds.",
    "But nothing online is truly free, bro. If you don't pay with money, you pay another way.",
    "Free services often earn from ads or data sharing. And you just handed over your number.",
    "Hidden risk: CERT-In warns criminals can easily intercept unprotected connections on public Wi-Fi.",
    "That can mean data theft, financial loss, even identity fraud.",
    "So CERT-In's advice: no banking, no shopping, no personal info on public Wi-Fi.",
    "Rule: pay on mobile data, turn OFF auto-connect, use a trusted VPN if you must connect.",
    "MORAL: If it's free, YOU might be the price.",
    "Send this to the friend who joins every free Wi-Fi in the mall.",
]
HOOK = [("FREE WI-FI", WHITE), ("ISN'T FREE", RED), ("HERE'S THE PRICE", YEL)]
SRC = "Source: CERT-In advisory (Apr 2025); Moneylife"
sh = None


def wifi_icon(c, x, y, s, col, a=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    for i, r in enumerate((90, 60, 30)):
        c.arc(0, 0, r, math.radians(225), math.radians(315))
        c.set_source_rgba(*col, a); c.set_line_width(14); c.stroke()
    c.arc(0, 0, 9, 0, 2 * math.pi); c.set_source_rgba(*col, a); c.fill()
    c.restore()


def cafe(c, t, lt, **kw):
    V.canteen(c, t)
    V.box(c, 1100, 40, 180, 150, (0.1, 0.1, 0.12), 14, (0.9, 0.7, 0.3), 5)
    wifi_icon(c, 1190, 165, 0.5, YEL)
    T(c, "FREE WI-FI", 1190, 88, 28, WHITE, stroke=None)
    d = dict(pose='stand', mouth='flat')
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_login(c, t, lt):
    st = sh.s(1)
    K.panel(c, 880, 500)
    wifi_icon(c, 540, 1010, 0.6, BLUE, k(t, st, st + 0.3))
    K.rows(c, t, st, [("Mobile: 98XXXXXX21", WHITE, 46, 1.2), ("OTP: 4 8 1 7", WHITE, 46, 2.6)], y0=1100, gap=80)
    K.stamp(c, t, st + 4.2, "CONNECTED", 540, 1310, GRN, 46, 0.0)


def o_free(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "NOTHING ONLINE", 540, 480, 90, WHITE, k(t, st + 0.3, st + 0.6), lw=10)
    T(c, "IS TRULY FREE", 540, 600, 90, RED, k(t, st + 0.9, st + 1.2), lw=10)
    if t > st + 2.8:
        T(c, "no money? you pay", 540, 820, 60, GREY, k(t, st + 2.8, st + 3.1), lw=8)
        T(c, "ANOTHER WAY", 540, 920, 80, YEL, k(t, st + 3.4, st + 3.7), lw=10)


def o_pay(c, t, lt):
    st = sh.s(3)
    K.panel(c, 870, 500)
    T(c, "FREE IS PAID BY:", 540, 950, 48, GREY, stroke=None)
    K.rows(c, t, st, [("ADS", YEL, 64, 0.8), ("DATA SHARING", RED, 64, 1.8)], y0=1070, gap=105)
    K.stamp(c, t, st + 3.6, "+ YOUR NUMBER", 540, 1300, BLUE, 42, 0.03)


def o_risk(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "CERT-In WARNING", 540, 400, 74, YEL, k(t, st + 0.2, st + 0.5), lw=8)
    T(c, "India's cyber-security agency", 540, 465, 36, GREY, k(t, st + 0.2, st + 0.5), lw=5)
    T(c, "YOU", 200, 720, 56, WHITE, k(t, st + 0.8, st + 1.1), lw=8)
    wifi_icon(c, 540, 760, 0.8, BLUE, k(t, st + 0.8, st + 1.1))
    T(c, "WEBSITE", 880, 720, 56, WHITE, k(t, st + 0.8, st + 1.1), lw=8)
    if t > st + 1.4:
        for j in range(3):
            f = ((t - st - 1.4) * 0.6 + j / 3) % 1
            T(c, "*", 280 + 520 * f, 740, 60, GRN, 1, lw=4)
    if t > st + 3.0:
        a = k(t, st + 3.0, st + 3.3)
        T(c, "?", 540, 1000, 140, RED, a, lw=12)
        T(c, "someone in the middle", 540, 1120, 52, RED, a, lw=8)
    if t > st + 4.6:
        T(c, "unprotected = easy to intercept", 540, 1230, 44, WHITE, k(t, st + 4.6, st + 4.9), lw=6)


def o_loss(c, t, lt):
    st = sh.s(5)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("DATA THEFT", RED, 64, 0.4), ("FINANCIAL LOSS", RED, 64, 1.4), ("IDENTITY FRAUD", RED, 64, 2.4)],
           y0=1000, gap=125)


def o_no(c, t, lt):
    st = sh.s(6)
    U.dim(c, 0.88)
    T(c, "CERT-In ADVICE", 540, 420, 74, WHITE, k(t, st + 0.2, st + 0.5), lw=8)
    for i, w in enumerate(("NO BANKING", "NO SHOPPING", "NO PERSONAL INFO")):
        dt = 1.0 + i * 0.9
        a = k(t, st + dt, st + dt + 0.25)
        if a > 0:
            T(c, w, 540, 620 + i * 150, 78, RED if i < 2 else YEL, a, lw=10)
    if t > st + 4.0:
        T(c, "on public Wi-Fi", 540, 1080, 56, GREY, k(t, st + 4.0, st + 4.3), lw=8)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "THE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Pay on MOBILE DATA", WHITE, 44, 0.8, "left", 150),
                      ("2. Auto-connect: OFF", GRN, 44, 2.0, "left", 150),
                      ("3. Must connect? Trusted VPN", WHITE, 44, 3.2, "left", 150)], y0=1070, gap=100)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "IF IT'S FREE,", "YOU MIGHT BE THE PRICE")


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO JOINS EVERY FREE WI-FI", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    cw = lambda **kw: (lambda c, t, lt: cafe(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    ph = dict(phone=1, arms=((14, -10), (30, 150)), glow=1)
    sh.shots = [
        (0, s(2), cw(mouth='bigsmile', **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_login, 'warm'),
        (s(2), s(3), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_free, 'studio'),
        (s(3), s(4), cw(mouth='o', eyes=1.25, **ph), (1.9, 1000, 480), (2.0, 1000, 460), o_pay, 'warm'),
        (s(4), s(5), sw(), (1.78, 960, 540), (1.85, 960, 520), o_risk, 'studio'),
        (s(5), s(6), cw(mouth='frown', squint=0.4, **ph), (1.9, 1000, 500), (2.0, 1000, 470), o_loss, 'red'),
        (s(6), s(7), sw(), (1.78, 960, 540), (1.85, 960, 520), o_no, 'studio'),
        (s(7), s(8), cw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, cw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
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
