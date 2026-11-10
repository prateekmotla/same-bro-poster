"""RULES YOU DIDN'T KNOW #4: paid carry bag with the store's logo.
Sources: Chandigarh consumer commission order (reported by IANS/Business Standard, 18 Apr 2019): ₹3 paper bag, customer
can't be compelled to pay; refund ₹3 + ₹1,000 costs + ₹3,000 compensation + ₹5,000 to legal aid = ₹9,000.
South Delhi district commission, Priti Agarwal v. Bata (LiveLaw, 18 Jul 2026): PLAIN bags may be charged only if sold
as a separate product with a prominent prior notice and a real choice. National Consumer Helpline: 1915."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s75_bag"
CAPS = [
    "Bought shoes, and the bill has ₹3 for a carry bag? A bag with the SAME store's logo? Wait.",
    "In Chandigarh, a store charged ₹3 for a paper bag. The consumer commission said: a customer can't be forced to pay for the bag.",
    "The store had to refund the ₹3, AND pay ₹9,000 more. Compensation, case costs, and a legal aid fund.",
    "And think: the bag has THEIR logo. That's their advertisement, and you're carrying it.",
    "But note: a Delhi commission said in 2026, a PLAIN bag can be charged IF there's a notice beforehand and you get a choice.",
    "So ask before billing. Forced to pay for a logo bag? Complain on the National Consumer Helpline, 1915.",
    "Same bro? Have you ever paid for a bag? Comment.",
]
HOOK = [("PAID ₹3 FOR", WHITE), ("THEIR LOGO BAG?", YEL), ("RULES YOU DIDN'T KNOW #4", GREY)]
SRC = "SRC: Chandigarh consumer commission 2019; Delhi DCDRC 2026"
sh = None
SHOE = [(0.85, 0.25, 0.2), (0.15, 0.15, 0.18), (0.95, 0.95, 0.95), (0.25, 0.45, 0.85), (0.6, 0.4, 0.25)]


def shop(c, t):
    c.rectangle(0, 0, 1920, 1080); c.set_source_rgb(0.92, 0.88, 0.82); c.fill()
    # shoe wall
    for r in range(4):
        y = 120 + r * 150
        c.rectangle(500, y + 70, 1000, 14); c.set_source_rgb(0.55, 0.42, 0.3); c.fill()
        for j in range(7):
            x = 530 + j * 140
            col = SHOE[(r * 3 + j) % 5]
            c.move_to(x, y + 70); c.line_to(x, y + 30); c.curve_to(x + 20, y + 20, x + 50, y + 25, x + 60, y + 40)
            c.curve_to(x + 80, y + 50, x + 100, y + 55, x + 105, y + 70); c.close_path(); c.set_source_rgb(*col); c.fill()
            c.rectangle(x, y + 62, 105, 8); c.set_source_rgb(0.95, 0.95, 0.95); c.fill()
    # counter
    c.rectangle(0, 700, 1920, 380); c.set_source_rgb(0.3, 0.24, 0.2); c.fill()
    c.rectangle(0, 690, 1920, 24); c.set_source_rgb(0.45, 0.36, 0.3); c.fill()
    # POS screen
    S.rrect(c, 1110, 560, 150, 130, 12); c.set_source_rgb(0.1, 0.1, 0.12); c.fill()
    S.rrect(c, 1120, 572, 130, 96, 8); c.set_source_rgb(0.2, 0.6, 0.9); c.fill()
    T(c, "₹1,502", 1185, 632, 28, WHITE, stroke=None)
    # logo bag on the counter
    logo_bag(c, 830, 640, 0.55)


def logo_bag(c, x, y, s, a=1.0, glow=False):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.arc(0, -70, 45, math.pi, 2 * math.pi); c.set_source_rgba(0.5, 0.35, 0.2, a); c.set_line_width(10); c.stroke()
    c.move_to(-110, -70); c.line_to(110, -70); c.line_to(130, 120); c.line_to(-130, 120); c.close_path()
    c.set_source_rgba(0.82, 0.68, 0.48, a); c.fill()
    c.arc(0, 25, 58, 0, 2 * math.pi); c.set_source_rgba(0.85, 0.15, 0.15, a); c.fill()
    T(c, "LOGO", 0, 40, 36, WHITE, a, stroke=None)
    c.restore()


def sh_(**kw):
    def f(c, t, lt):
        shop(c, t)
        d = dict(pose='stand', mouth='flat')
        d.update(kw)
        K.sid(c, t, 1000, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def receipt(c, t, st):
    a = k(t, st, st + 0.3)
    S.rrect(c, 200, 880, 680, 470, 14); c.set_source_rgba(0.98, 0.97, 0.94, a); c.fill()
    T(c, "TAX INVOICE", 540, 950, 40, (0.2, 0.2, 0.22), a, stroke=None)
    rows = [("Shoes", "₹1,499"), ("Carry bag (logo)", "₹3")]
    for j, (l, r) in enumerate(rows):
        b = k(t, st + 0.6 + j * 1.0, st + 0.9 + j * 1.0)
        col = (0.15, 0.15, 0.18) if j == 0 else (0.8, 0.1, 0.1)
        T(c, l, 250, 1050 + j * 80, 42, col, b, stroke=None, anchor="left")
        T(c, r, 830, 1050 + j * 80, 42, col, b, stroke=None, anchor="right")
    c.rectangle(240, 1180, 600, 3); c.set_source_rgba(0.3, 0.3, 0.3, a); c.fill()
    T(c, "TOTAL", 250, 1250, 46, (0.1, 0.1, 0.12), k(t, st + 2.4, st + 2.7), stroke=None, anchor="left")
    T(c, "₹1,502", 830, 1250, 46, (0.1, 0.1, 0.12), k(t, st + 2.4, st + 2.7), stroke=None, anchor="right")
    if t > st + 1.8:
        c.save(); c.arc(820, 1130, 48, 0, 2 * math.pi); c.restore()
        c.set_source_rgba(*RED, k(t, st + 1.8, st + 2.0)); c.set_line_width(7); c.stroke()


def o_hook(c, t, lt):
    st = sh.s(1)
    receipt(c, t, st + 0.2)
    K.stamp(c, t, st + 4.0, "WAIT.", 540, 1420, RED, 64, -0.05)


def o_case(c, t, lt):
    st = sh.s(2)
    K.panel(c, 860, 560)
    T(c, "CHANDIGARH CONSUMER", 540, 950, 50, YEL, k(t, st, st + 0.3), stroke=None)
    T(c, "COMMISSION (2019)", 540, 1012, 50, YEL, k(t, st, st + 0.3), stroke=None)
    K.rows(c, t, st, [("₹3 paper bag charged", WHITE, 50, 1.0), ("Customer CAN'T be forced", GRN, 54, 3.6),
                      ("to pay for the bag", GRN, 54, 3.6)], y0=1120, gap=100)


def o_fine(c, t, lt):
    st = sh.s(3)
    K.full(c, t, st, [("₹3 REFUND", WHITE, 84, 0.2), ("+ ₹9,000", GRN, 150, 1.4), ("compensation + costs", GREY, 52, 3.4),
                      ("+ legal aid fund", GREY, 52, 4.6)], y0=520, gap=170)


def o_logo(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.86)
    logo_bag(c, 540, 820, 2.2, k(t, st, st + 0.3))
    T(c, "THEIR AD", 540, 1180, 84, YEL, k(t, st + 1.2, st + 1.5), lw=10)
    T(c, "YOU CARRY IT", 540, 1290, 70, WHITE, k(t, st + 2.2, st + 2.5), lw=10)


def o_delhi(c, t, lt):
    st = sh.s(5)
    K.panel(c, 820, 600)
    T(c, "BUT: DELHI COMMISSION (2026)", 540, 905, 46, YEL, k(t, st, st + 0.3), stroke=None)
    K.rows(c, t, st, [("A PLAIN bag can be charged", WHITE, 50, 2.0), ("ONLY IF:", GREY, 44, 4.2),
                      ("Notice shown BEFORE billing", GRN, 50, 4.6), ("+ you get a real choice", GRN, 50, 6.2)],
           y0=1010, gap=100)


def o_fix(c, t, lt):
    st = sh.s(6)
    K.full(c, t, st, [("ASK BEFORE BILLING", WHITE, 72, 0.2), ("FORCED LOGO-BAG CHARGE?", YEL, 56, 2.0),
                      ("COMPLAIN: NCH 1915", GRN, 80, 4.0)], y0=560, gap=190)


def o_end(c, t, lt):
    K.end_card(c, "EVER PAID FOR A BAG?", "COMMENT YES or NO", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    sh.shots = [
        (0, s(2), sh_(mouth='o', eyes=1.3, arms=((60, 120), (14, -10))), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_case, 'studio'),
        (s(3), s(4), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_fine, 'money'),
        (s(4), s(5), sh_(mouth='smirk'), (1.9, 1000, 480), (2.0, 1000, 460), o_logo, 'warm'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_delhi, 'studio'),
        (s(6), s(7), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_fix, 'money'),
        (s(7), sh.dur + 1, sh_(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 480), (2.1, 1000, 450), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.5, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]] + [L[4][0] + 7], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
