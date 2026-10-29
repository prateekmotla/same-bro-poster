import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/s21_chips"
CAPS = [
    "Sid opens a ₹20 chips packet. Big packet... HALF of it is air.",
    "Everyone thinks: SCAM. But that \"air\" is mostly NITROGEN gas.",
    "Oxygen makes the oil go stale and moisture makes chips soggy. Nitrogen keeps them CRISPY.",
    "The gas also works as a cushion, so your chips don't reach you as crumbs.",
    "The HIDDEN part: a fat packet LOOKS like more food. Eyes judge size, not grams.",
    "That extra space even has a name: SLACK FILL. Freshness AND marketing, both.",
    "Rule: ignore the packet size. Check the NET WEIGHT, compare price per gram.",
    "Send this to the friend who says chips companies sell air.",
]
HOOK = [("CHIPS PACKET", WHITE), ("HALF AIR?", RED), ("THE REAL REASON", YEL)]
SRC = "Source: Mental Floss, 'Why are chip bags half empty?'"
sh = None


def room(c, t, lt, mode='night', **kw):
    V.room(c, t, mode)
    d = dict(pose='sit', arms=((14, -10), (60, 120)))
    d.update(kw)
    K.sid(c, t, 1000, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def chips_bag(c, x, y, s, fill, a=1.0, gas=None):
    """Chips bag centre (x,y); fill 0..1 = chips level; gas = label for the empty part."""
    c.save(); c.translate(x, y); c.scale(s, s)
    c.push_group()
    c.move_to(-170, -240); c.curve_to(-200, -80, -200, 120, -170, 240); c.line_to(170, 240)
    c.curve_to(200, 120, 200, -80, 170, -240); c.close_path()
    c.set_source_rgb(0.9, 0.2, 0.25); c.fill_preserve(); c.save(); c.clip()
    top = 240 - 480 * fill
    c.rectangle(-220, top, 440, 480); c.set_source_rgba(1, 1, 1, 0.0); c.fill()
    for i in range(18):
        cx = -140 + (i % 6) * 56; cy = 220 - (i // 6) * 50
        if cy > top:
            c.save(); c.translate(cx, cy); c.scale(1, 0.6); c.arc(0, 0, 32, 0, 2 * math.pi); c.restore()
            c.set_source_rgb(0.98, 0.8, 0.3); c.fill()
    if gas:
        c.rectangle(-220, -240, 440, top + 240); c.set_source_rgba(0.6, 0.85, 1, 0.35); c.fill()
        T(c, gas, 0, (top - 240) / 2 + 20, 64, WHITE, stroke=(0.1, 0.2, 0.4), lw=8)
    c.restore()
    c.rectangle(-180, -255, 360, 30); c.set_source_rgb(0.7, 0.12, 0.16); c.fill()
    c.rectangle(-180, 225, 360, 30); c.set_source_rgb(0.7, 0.12, 0.16); c.fill()
    T(c, "CHIPS", 0, -120 if not gas else -300, 60, YEL, stroke=None) if not gas else None
    c.pop_group_to_source(); c.paint_with_alpha(a)
    c.restore()


def o_open(c, t, lt):
    st = sh.s(1)
    chips_bag(c, 540, 1110, 0.62, 1.0 if t < st + 2.2 else max(0.45, 1 - (t - st - 2.2) * 0.6), a=k(t, st, st + 0.3))
    if t > st + 3.2:
        T(c, "50% AIR?!", 540, 860, 80, RED, k(t, st + 3.2, st + 3.4), lw=10)


def o_n2(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.86)
    K.stamp(c, t, st + 0.6, "SCAM?", 540, 420, RED, 90, 0.05)
    if t > st + 2.0:
        chips_bag(c, 540, 860, 0.85, 0.45, a=k(t, st + 2.0, st + 2.3), gas="N2")
    if t > st + 2.6:
        T(c, "NITROGEN", 540, 1210, 96, BLUE, k(t, st + 2.6, st + 2.9), lw=12)


def o_fresh(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.86)
    T(c, "OXYGEN", 300, 420, 80, RED, k(t, st + 0.3, st + 0.6), lw=10)
    T(c, "stale oil", 300, 520, 50, WHITE, k(t, st + 0.8, st + 1.1), lw=6)
    T(c, "MOISTURE", 780, 420, 76, RED, k(t, st + 1.4, st + 1.7), lw=10)
    T(c, "soggy chips", 780, 520, 50, WHITE, k(t, st + 1.8, st + 2.1), lw=6)
    if t > st + 3.0:
        a = k(t, st + 3.0, st + 3.3)
        T(c, "NITROGEN =", 540, 760, 90, BLUE, a, lw=12)
        T(c, "CRISPY", 540, 900, 130, GRN, k(t, st + 3.5, st + 3.8), lw=14)


def o_cushion(c, t, lt):
    st = sh.s(4)
    K.panel(c, 870, 500)
    T(c, "GAS = CUSHION", 540, 950, 60, YEL, stroke=None)
    for i in range(3):
        x = 260 + i * 280
        a = k(t, st + 0.8 + i * 0.5, st + 1.1 + i * 0.5)
        y = 1170 + math.sin(t * 6 + i) * 18
        chips_bag(c, x, y, 0.38, 0.45, a=a)
    T(c, "no crumbs in the truck", 540, 1340, 44, WHITE, k(t, st + 2.4, st + 2.7), stroke=None)


def o_eyes(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.86)
    T(c, "WHICH HAS MORE?", 540, 400, 76, WHITE, k(t, st + 0.3, st + 0.6), lw=10)
    chips_bag(c, 310, 780, 0.75, 0.45, a=k(t, st + 0.8, st + 1.1))
    chips_bag(c, 780, 820, 0.55, 0.8, a=k(t, st + 1.1, st + 1.4))
    if t > st + 3.2:
        T(c, "50g", 310, 1060, 80, YEL, k(t, st + 3.2, st + 3.5), lw=10)
        T(c, "50g", 780, 1060, 80, YEL, k(t, st + 3.2, st + 3.5), lw=10)
        T(c, "SAME!", 540, 1220, 100, RED, k(t, st + 4.0, st + 4.3), lw=12)


def o_slack(c, t, lt):
    st = sh.s(6)
    K.full(c, t, st, [("SLACK FILL", YEL, 140, 0.8), ("freshness", GRN, 70, 2.4), ("+ marketing", RED, 70, 3.2)],
           y0=520, gap=200)


def o_rule(c, t, lt):
    st = sh.s(7)
    K.panel(c, 860, 520)
    T(c, "BEFORE YOU BUY", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Ignore packet size", WHITE, 48, 0.8, "left", 170),
                      ("2. Read NET WEIGHT", GRN, 48, 1.8, "left", 170),
                      ("3. Price per gram", WHITE, 48, 2.8, "left", 170)], y0=1070, gap=100)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHO SAYS \"THEY SELL AIR\"", YEL)


def build():
    global sh
    sh = TS.TextShort(D, CAPS, HOOK, [], SRC)
    s = sh.s
    rw = lambda **kw: (lambda c, t, lt: room(c, t, lt, **kw))
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), lambda c, t, lt: room(c, t, lt, mouth='smile' if t < s(1) + 2.6 else 'o', eyes=1.0 if t < s(1) + 2.6 else 1.25),
         (1.9, 1000, 480), (2.1, 1000, 450), o_open, 'night'),
        (s(2), s(3), sw(), (1.78, 960, 540), (1.85, 960, 520), o_n2, 'studio'),
        (s(3), s(4), sw(), (1.78, 960, 540), (1.85, 960, 520), o_fresh, 'studio'),
        (s(4), s(5), sw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 960, 500), (2.0, 960, 470), o_cushion, 'studio'),
        (s(5), s(6), rw(mouth='flat', squint=0.5), (1.78, 960, 540), (1.85, 960, 520), o_eyes, 'night'),
        (s(6), s(7), sw(), (1.78, 960, 540), (1.85, 960, 520), o_slack, 'studio'),
        (s(7), s(8), rw(mode='day', mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 480), o_rule, 'morning'),
        (s(8), sh.dur + 1, rw(mode='day', mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470),
         o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1.2, 4.5] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
