import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import body as B  # noqa: E402
import env as V  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s10_mf"
CAPS = [
    "Sid started an SIP. The bank guy said: best fund, fill the form, I'll handle the rest.",
    "Nobody told Sid this: every mutual fund has TWO versions. REGULAR and DIRECT.",
    "Same fund. Same manager. Same portfolio. One difference: REGULAR plans hide the seller's COMMISSION.",
    "Every year, a little gets cut from your money. You won't even see it separately on your statement.",
    "The gap looks tiny, around 1%. But compounding makes it HUGE.",
    "₹5,000 SIP for 20 years. 12% in direct vs 11% in regular... that's a gap of about ₹6 LAKH.",
    "Check your fund's name. Does it say \"DIRECT\" or \"REGULAR\"? That's all you need to check.",
    "Send this to the friend whose SIP was opened by the bank guy.",
]
HOOK = [("YOUR SIP HAS A", WHITE), ("HIDDEN", RED), ("COMMISSION", YEL)]
SRC = "Illustration: assumed returns · not financial advice"
sh = None


def w_bank(c, t, lt):
    V.canteen(c, t)
    B.figure(c, 700, 330, 0.55, t, pose='sit', mouth='smile', look=(0.7, 0))
    B.figure(c, 1250, 330, 0.55, t, who='bhai', glasses=False, pose='sit', mouth='bigsmile', arms=((14, -10), (100, 40)))


def o_bank(c, t, lt):
    S.rrect(c, 120, 880, 840, 220, 30); c.set_source_rgba(0.97, 0.97, 0.99, 0.95); c.fill()
    T(c, "\"Best fund hai, sign karo\"", 540, 1010, 52, (0.1, 0.1, 0.15), stroke=None)


def o_two(c, t, lt):
    U.dim(c, 0.82)
    for i, (lab, col) in enumerate((("REGULAR", RED), ("DIRECT", GRN))):
        a = k(t, sh.s(2) + 2.5 + i * 0.8, sh.s(2) + 2.8 + i * 0.8)
        x = 90 + i * 470
        S.rrect(c, x, 420, 430, 560, 30); c.set_source_rgba(0.08, 0.09, 0.13, 0.95 * a); c.fill()
        c.set_source_rgba(*col, a); c.set_line_width(6); S.rrect(c, x, 420, 430, 560, 30); c.stroke()
        T(c, lab, x + 215, 520, 56, col, a, stroke=None)
        for j, row in enumerate(("Same fund", "Same manager", "Same portfolio")):
            T(c, row, x + 215, 640 + j * 80, 38, WHITE, a, stroke=None)
        if i == 0 and t > sh.s(3) + 3.0:
            S.rrect(c, x + 30, 880, 370, 70, 14); c.set_source_rgb(*RED); c.fill()
            T(c, "+ COMMISSION", x + 215, 928, 38, WHITE, stroke=None)


def o_leak(c, t, lt):
    U.dim(c, 0.8)
    T(c, "EVERY YEAR", 540, 400, 70, WHITE)
    c.save(); c.translate(540, 760)
    S.rrect(c, -200, -230, 400, 460, 40); c.set_source_rgb(0.2, 0.5, 0.35); c.fill()
    T(c, "₹", 0, 60, 220, (0.1, 0.3, 0.2), stroke=None)
    c.restore()
    for i in range(6):
        ph = (t * 0.7 + i / 6) % 1
        c.arc(540 + math.sin(i) * 60, 1000 + ph * 260, 14, 0, 2 * math.pi); c.set_source_rgba(*RED, 1 - ph); c.fill()


def o_tiny(c, t, lt):
    U.dim(c, 0.8)
    T(c, "~1%", 540, 700, 280, YEL, lw=24)
    T(c, "a year", 540, 800, 60, WHITE, stroke=None)
    T(c, "+ COMPOUNDING", 540, 1050, 70, RED, k(t, sh.s(5) + 2.0, sh.s(5) + 2.3))


def o_chart(c, t, lt):
    U.dim(c, 0.85)
    T(c, "₹5,000/month · 20 years", 540, 330, 50, WHITE, stroke=None)
    p = k(t, sh.s(6) + 1.0, sh.s(6) + 6.0)
    import math as m
    def fv(r, n):
        r = r / 12
        return 5000 * ((1 + r) ** n - 1) / r * (1 + r)
    x0, y0, w, h = 120, 1150, 840, 650
    for rate, col in ((0.12, GRN), (0.11, RED)):
        c.move_to(x0, y0)
        for i in range(1, int(240 * p) + 1):
            c.line_to(x0 + w * i / 240, y0 - h * fv(rate, i) / 5.2e6)
        c.set_source_rgb(*col); c.set_line_width(10); c.stroke()
    if p > 0.95:
        T(c, "DIRECT ₹50 L", 760, 470, 46, GRN, stroke=None)
        T(c, "REGULAR ₹44 L", 760, 600, 46, RED, stroke=None)
        T(c, "GAP ≈ ₹6 LAKH", 540, 1260, 80, YEL)


def w_check(c, t, lt):
    V.room(c, t, 'day')
    B.figure(c, 900, 330, 0.55, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=0.3, mouth='o', **{'raise': 0.6})


def o_check(c, t, lt):
    S.rrect(c, 80, 860, 920, 440, 30); c.set_source_rgba(0.97, 0.97, 0.99, 0.95); c.fill()
    T(c, "XYZ Flexicap Fund", 540, 960, 50, (0.1, 0.1, 0.15), stroke=None)
    T(c, "- Regular Plan - Growth", 540, 1040, 46, RED, stroke=None)
    T(c, "or", 540, 1120, 36, (0.4, 0.4, 0.5), stroke=None)
    T(c, "- Direct Plan - Growth", 540, 1200, 46, (0.1, 0.55, 0.3), stroke=None)


def o_end(c, t, lt):
    S.rrect(c, 140, 260, 800, 230, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    T(c, "SEND TO THE", 540, 360, 64, WHITE, stroke=None)
    T(c, "SIP FRIEND", 540, 445, 76, YEL, stroke=None)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    room = lambda c, t, lt: (V.room(c, t, 'night'), B.figure(c, 1000, 330, 0.5, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1, mouth='flat'))
    sh.shots = [
        (0, s(2), w_bank, (1.78, 960, 520), (1.95, 1000, 480), o_bank, 'warm'),
        (s(2), s(4), room, (1.78, 960, 540), (1.85, 960, 520), o_two, 'night'),
        (s(4), s(5), room, (1.78, 960, 540), (1.85, 1000, 540), o_leak, 'red'),
        (s(5), s(6), room, (1.78, 960, 540), (1.85, 920, 540), o_tiny, 'night'),
        (s(6), s(7), room, (1.78, 960, 540), (1.82, 960, 540), o_chart, 'money'),
        (s(7), s(8), w_check, (1.9, 900, 480), (2.0, 900, 460), o_check, 'morning'),
        (s(8), sh.dur + 1, w_check, (1.9, 900, 480), (2.1, 900, 440), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview([1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 47.5], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
