import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import envx as X  # noqa: E402
import body as B  # noqa: E402
import env as V  # noqa: E402
import props as P  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s06_emi"
CAPS = [
    "\"NO COST EMI.\" Sounds like free money. Sid thought so too. New phone, just ₹5,000 a month.",
    "But \"no cost\" doesn't always mean FREE.",
    "Sometimes the cash DISCOUNT is quietly removed. Sometimes there's a PROCESSING FEE. And GST on the interest.",
    "The biggest cost? Your next 6 months of salary, already BOOKED.",
    "One EMI is fine. Three at once, and every month is TIGHT.",
    "Simple rule: if you can't buy it in cash TWICE, don't buy it on EMI even once.",
    "And before buying, check the FINAL total. Fee and GST included.",
    "Send this to the friend whose everything is on EMI.",
]
HOOK = [("\"NO COST EMI\"", YEL), ("IS NOT", WHITE), ("FREE", RED)]
SRC = "General info · not financial advice"
sh = None


def emi_screen(c, w, h, t):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
    c.rectangle(0, 0, w, 120); c.set_source_rgb(0.15, 0.35, 0.9); c.fill()
    T(c, "Checkout", w / 2, 82, 44, WHITE, stroke=None)
    S.rrect(c, w / 2 - 80, 160, 160, 270, 24); c.set_source_rgb(0.1, 0.1, 0.12); c.fill()
    T(c, "₹30,000", w / 2, 520, 64, (0.1, 0.1, 0.12), stroke=None)
    S.rrect(c, 30, 580, w - 60, 200, 20); c.set_source_rgb(0.9, 1, 0.92); c.fill()
    T(c, "NO COST EMI", w / 2, 650, 48, (0.1, 0.55, 0.3), stroke=None)
    T(c, "₹5,000 × 6 months", w / 2, 730, 42, (0.1, 0.1, 0.12), stroke=None)
    S.rrect(c, 30, h - 150, w - 60, 90, 45); c.set_source_rgb(1, 0.6, 0.1); c.fill()
    T(c, "PLACE ORDER", w / 2, h - 90, 40, WHITE, stroke=None)


def w_room(c, t, lt, **kw):
    V.room(c, t, 'night')
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1, mouth='bigsmile')
    d.update(kw)
    B.figure(c, 1000, 330, 0.5, t, **d)


def o_phone(c, t, lt):
    U.phone_frame(c, 240, 300, 600, 1060, emi_screen, t, tilt=-2 + 3 * lt)


def o_notfree(c, t, lt):
    U.dim(c, 0.5)
    T(c, "NO COST", 540, 800, 130, WHITE, lw=14)
    if t > sh.s(2) + 1.2:
        c.set_line_width(22); c.set_source_rgb(*RED)
        c.move_to(170, 760); c.line_to(910, 760); c.stroke()
        T(c, "≠ FREE", 540, 980, 130, RED, k(t, sh.s(2) + 1.2, sh.s(2) + 1.5), lw=14)


def o_hidden(c, t, lt):
    U.dim(c, 0.82)
    T(c, "HIDDEN COSTS", 540, 330, 80, YEL)
    items = [("Cash discount removed", sh.s(3) + 0.3), ("Processing fee", sh.s(3) + 3.0), ("GST on interest", sh.s(3) + 5.0)]
    for i, (lab, t0) in enumerate(items):
        a = k(t, t0, t0 + 0.3)
        S.rrect(c, 110, 430 + i * 200, 860, 160, 26); c.set_source_rgba(0.12, 0.04, 0.06, 0.95 * a); c.fill()
        T(c, f"{i + 1}", 180, 530 + i * 200, 70, RED, a, stroke=None)
        T(c, lab, 250, 530 + i * 200, 52, WHITE, a, stroke=None, anchor="left")


def o_booked(c, t, lt):
    U.dim(c, 0.8)
    T(c, "NEXT 6 SALARIES", 540, 420, 70, WHITE)
    for i in range(6):
        a = k(t, sh.s(4) + 1.0 + i * 0.35, sh.s(4) + 1.2 + i * 0.35)
        x = 150 + (i % 3) * 270; y = 520 + (i // 3) * 270
        S.rrect(c, x, y, 240, 230, 20); c.set_source_rgb(0.15, 0.17, 0.24); c.fill()
        T(c, ["NOV", "DEC", "JAN", "FEB", "MAR", "APR"][i], x + 120, y + 70, 44, WHITE, stroke=None)
        if a > 0:
            c.save(); c.translate(x + 120, y + 150); c.rotate(-0.2); c.scale(0.6 + 0.4 * a, 0.6 + 0.4 * a)
            S.rrect(c, -100, -38, 200, 76, 10); c.set_source_rgba(*RED, a); c.fill()
            T(c, "BOOKED", 0, 18, 42, WHITE, a, stroke=None)
            c.restore()


def o_stack(c, t, lt):
    U.dim(c, 0.82)
    T(c, "YOUR SALARY", 540, 360, 70, WHITE)
    S.rrect(c, 120, 420, 840, 120, 20); c.set_source_rgb(*GRN); c.fill()
    T(c, "₹35,000", 540, 500, 60, (0.05, 0.2, 0.1), stroke=None)
    emis = [("Phone EMI", 5000), ("Bike EMI", 6000), ("Laptop EMI", 4000)]
    x = 120
    for i, (lab, amt) in enumerate(emis):
        a = k(t, sh.s(5) + 0.5 + i * 1.0, sh.s(5) + 0.8 + i * 1.0)
        w = 840 * amt / 35000
        S.rrect(c, x, 420, w * a, 120, 10); c.set_source_rgb(*RED); c.fill()
        T(c, lab, 540, 650 + i * 90, 46, RED, a, stroke=None)
        x += w
    T(c, "TIGHT. EVERY. MONTH.", 540, 1000, 66, YEL, k(t, sh.s(5) + 3.5, sh.s(5) + 3.8))


def w_rule(c, t, lt):
    V.room(c, t, 'day')
    B.figure(c, 900, 330, 0.55, t, pose='sit', mouth='smirk', squint=0.3)


def o_rule(c, t, lt):
    S.rrect(c, 90, 860, 900, 440, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
    T(c, "THE 2X RULE", 540, 960, 70, YEL, stroke=None)
    T(c, "Can't buy it in cash TWICE?", 540, 1070, 46, WHITE, stroke=None)
    T(c, "Don't buy it on EMI ONCE.", 540, 1150, 50, GRN, k(t, sh.s(6) + 2.5, sh.s(6) + 2.8), stroke=None)


def o_total(c, t, lt):
    S.rrect(c, 90, 860, 900, 440, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
    T(c, "CHECK THE FINAL TOTAL", 540, 960, 56, YEL, stroke=None)
    T(c, "price + fee + GST", 540, 1070, 52, WHITE, stroke=None)
    T(c, "= real cost", 540, 1160, 52, GRN, stroke=None)


def o_end(c, t, lt):
    S.rrect(c, 140, 260, 800, 230, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    T(c, "SEND TO THE", 540, 360, 64, WHITE, stroke=None)
    T(c, "EMI KING", 540, 445, 76, YEL, stroke=None)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    sh.shots = [
        (0, s(2), w_room, (1.9, 1000, 480), (2.1, 1000, 450), o_phone, 'phone'),
        (s(2), s(3), w_room, (1.78, 960, 540), (1.85, 960, 520), o_notfree, 'red'),
        (s(3), s(4), lambda c, t, lt: w_room(c, t, lt, mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 1000, 540), o_hidden, 'night'),
        (s(4), s(5), lambda c, t, lt: w_room(c, t, lt, mouth='frown', sad=0.6), (1.78, 960, 540), (1.85, 920, 540), o_booked, 'night'),
        (s(5), s(6), lambda c, t, lt: w_room(c, t, lt, mouth='grit', sweat=1), (1.78, 960, 540), (1.85, 1000, 520), o_stack, 'red'),
        (s(6), s(7), w_rule, (1.9, 900, 480), (2.0, 900, 460), o_rule, 'morning'),
        (s(7), s(8), w_rule, (1.95, 900, 470), (2.05, 900, 450), o_total, 'morning'),
        (s(8), sh.dur + 1, w_rule, (1.9, 900, 480), (2.1, 900, 440), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview([1, 5, 9, 12, 15, 18, 21, 25, 27, 30, 33, 36, 40, 41.5], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
