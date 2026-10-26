import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import body as B  # noqa: E402
import env as V  # noqa: E402
import props as P  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s09_card"
CAPS = [
    "Sid's credit card bill: ₹50,000. And below it: MINIMUM DUE, just ₹2,500.",
    "Sid thought: nice. Pay ₹2,500 now, the rest later.",
    "That's the most EXPENSIVE mistake.",
    "Most Indian cards charge 3.5% a MONTH on the unpaid amount. That's about 42% a YEAR.",
    "Of the first ₹2,500, ₹1,750 went to INTEREST. The loan dropped by just ₹750.",
    "If Sid pays only the minimum every month, and spends nothing new... clearing ₹50,000 takes about 15 YEARS. Total paid: about ₹1.5 LAKH. Plus GST.",
    "The rule: pay the FULL bill every month. If you can't, that spend wasn't in your budget.",
    "Send this to the friend who thinks the minimum due IS the bill.",
]
HOOK = [("CREDIT CARD", WHITE), ("\"MINIMUM DUE\"", YEL), ("TRAP", RED)]
SRC = "Typical card rate 3.5%/month · illustration, not advice"
sh = None


def bill(c, w, h, t):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
    c.rectangle(0, 0, w, 130); c.set_source_rgb(0.1, 0.12, 0.3); c.fill()
    T(c, "Card Statement", w / 2, 85, 40, WHITE, stroke=None)
    T(c, "Total due", 50, 230, 34, (0.4, 0.4, 0.5), stroke=None, anchor="left", bold=False)
    T(c, "₹50,000", 50, 320, 84, (0.1, 0.1, 0.15), stroke=None, anchor="left")
    S.rrect(c, 30, 390, w - 60, 200, 20); c.set_source_rgb(1, 0.95, 0.8); c.fill()
    T(c, "Minimum due", 60, 460, 34, (0.5, 0.35, 0.1), stroke=None, anchor="left", bold=False)
    T(c, "₹2,500", 60, 550, 84, (0.85, 0.45, 0.05), stroke=None, anchor="left")
    S.rrect(c, 30, h - 160, w - 60, 100, 50); c.set_source_rgb(0.15, 0.45, 0.95); c.fill()
    T(c, "Pay ₹2,500", w / 2, h - 95, 40, WHITE, stroke=None)


def w_room(c, t, lt, **kw):
    V.room(c, t, 'night')
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1, mouth='flat')
    d.update(kw)
    B.figure(c, 1000, 330, 0.5, t, **d)


def o_bill(c, t, lt):
    U.phone_frame(c, 240, 300, 600, 1060, bill, t, tilt=-2 + 3 * lt)


def w_relief(c, t, lt):
    w_room(c, t, lt, mouth='bigsmile', blush=0.4, arms=((14, -10), (100, 40)), phone=None)


def o_mistake(c, t, lt):
    U.dim(c, 0.4)
    P.stamp(c, "COSTLIEST", 540, 900, sh.s(3) + 0.2, t, -8, RED, 110)
    P.stamp(c, "MISTAKE", 540, 1060, sh.s(3) + 0.6, t, 6, RED, 110)


def o_rate(c, t, lt):
    U.dim(c, 0.8)
    T(c, "3.5%", 540, 620, 260, YEL, k(t, sh.s(4) + 2.3, sh.s(4) + 2.6), lw=22)
    T(c, "PER MONTH", 540, 720, 64, WHITE, k(t, sh.s(4) + 2.5, sh.s(4) + 2.8))
    if t > sh.s(4) + 4.8:
        T(c, "= ~42%", 540, 1000, 200, RED, k(t, sh.s(4) + 4.8, sh.s(4) + 5.1), lw=20)
        T(c, "PER YEAR", 540, 1100, 64, WHITE, k(t, sh.s(4) + 5.0, sh.s(4) + 5.3))


def o_split(c, t, lt):
    U.dim(c, 0.8)
    T(c, "YOUR ₹2,500", 540, 400, 80, WHITE)
    fr = k(t, sh.s(5) + 1.0, sh.s(5) + 2.5)
    c.save(); c.translate(540, 760)
    c.arc(0, 0, 260, 0, 2 * math.pi); c.set_source_rgb(*GRN); c.fill()
    c.move_to(0, 0); c.arc(0, 0, 260, -math.pi / 2, -math.pi / 2 + 2 * math.pi * 0.7 * fr); c.close_path()
    c.set_source_rgb(*RED); c.fill()
    c.restore()
    if fr > 0.9:
        T(c, "₹1,750 INTEREST", 540, 1120, 70, RED)
    if t > sh.s(5) + 4.2:
        T(c, "₹750 loan paid", 540, 1210, 56, GRN, k(t, sh.s(5) + 4.2, sh.s(5) + 4.5))


def o_years(c, t, lt):
    U.dim(c, 0.82)
    yrs = int(15 * k(t, sh.s(6) + 4.5, sh.s(6) + 7.0))
    T(c, f"{yrs} YEARS", 540, 520, 170, YEL, lw=18)
    T(c, "to clear ₹50,000", 540, 610, 54, WHITE, stroke=None)
    for i in range(15):
        a = 1.0 if i < yrs else 0.15
        S.rrect(c, 110 + (i % 5) * 175, 690 + (i // 5) * 90, 150, 70, 12); c.set_source_rgba(*YEL, a); c.fill()
        T(c, str(2026 + i), 185 + (i % 5) * 175, 738 + (i // 5) * 90, 30, (0.1, 0.1, 0.1), a, stroke=None)
    if t > sh.s(6) + 8.0:
        T(c, "TOTAL PAID: ~₹1.5 LAKH", 540, 1100, 66, RED, k(t, sh.s(6) + 8.0, sh.s(6) + 8.3))
        T(c, "+ GST on interest", 540, 1180, 44, WHITE, k(t, sh.s(6) + 9.8, sh.s(6) + 10.1), stroke=None)


def w_rule(c, t, lt):
    V.room(c, t, 'day')
    B.figure(c, 900, 330, 0.55, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=0.3, mouth='smile')


def o_rule(c, t, lt):
    S.rrect(c, 90, 860, 900, 420, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
    T(c, "PAY THE FULL BILL", 540, 960, 66, GRN, stroke=None)
    T(c, "every month", 540, 1030, 44, WHITE, stroke=None)
    T(c, "Can't? It wasn't in", 540, 1150, 46, (0.85, 0.85, 0.9), k(t, sh.s(7) + 3.5, sh.s(7) + 3.8), stroke=None)
    T(c, "your budget.", 540, 1215, 46, YEL, k(t, sh.s(7) + 3.8, sh.s(7) + 4.1), stroke=None)


def o_end(c, t, lt):
    S.rrect(c, 140, 260, 800, 230, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    T(c, "SEND TO THE", 540, 360, 64, WHITE, stroke=None)
    T(c, "\"MINIMUM DUE\" GUY", 540, 445, 64, YEL, stroke=None)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    sh.shots = [
        (0, s(2), w_room, (1.9, 1000, 480), (2.1, 1000, 450), o_bill, 'phone'),
        (s(2), s(3), w_relief, (2.0, 1000, 470), (2.2, 1000, 440), None, 'warm'),
        (s(3), s(4), w_relief, (2.4, 1000, 420), (2.2, 1000, 450), o_mistake, 'red'),
        (s(4), s(5), w_room, (1.78, 960, 540), (1.85, 1000, 540), o_rate, 'night'),
        (s(5), s(6), w_room, (1.78, 960, 540), (1.85, 920, 540), o_split, 'red'),
        (s(6), s(7), w_room, (1.78, 960, 540), (1.9, 1000, 520), o_years, 'night'),
        (s(7), s(8), w_rule, (1.9, 900, 480), (2.0, 900, 460), o_rule, 'morning'),
        (s(8), sh.dur + 1, w_rule, (1.9, 900, 480), (2.1, 900, 440), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview([1, 4, 7, 11, 15, 18, 22, 25, 29, 33, 36, 40, 44, 48], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
