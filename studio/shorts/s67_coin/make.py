import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s67_coin"
CAPS = [
    "Shopkeeper says 'this ₹10 coin doesn't work'? Wrong. RBI says all 14 designs are valid.",
    "Sid paid with a ₹10 coin. Uncle: 'This one's fake, won't work.'",
    "Truth: the ₹10 coin has 14 different designs. And RBI has clearly said: ALL are legal tender.",
    "A different design doesn't mean fake. People just stop taking them because of rumours.",
    "And RBI has told banks too: accept coins at every branch, and exchange them.",
    "Same bro? Put the coin back in your pocket without a word?",
    "Fix: say politely, RBI has declared all ₹10 coins valid. Bank refuses? Complain at the branch, then the RBI Ombudsman.",
    "MORAL: RBI's rule is bigger than any rumour.",
    "Send this to the friend whose pocket is full of ₹10 coins.",
]
HOOK = [("SHOP REFUSED", WHITE), ("YOUR ₹10 COIN?", YEL), ("RULES #2", GREY)]
SRC = "Source: RBI press release, 17 Jan 2018"
sh = None
GOLD = (0.85, 0.68, 0.25)
SILV = (0.75, 0.76, 0.8)


def coin(c, x, y, r, a=1.0, var=0, rot=0.0):
    c.save(); c.translate(x, y); c.rotate(rot)
    c.arc(0, 0, r, 0, 2 * math.pi); c.set_source_rgba(*SILV, a); c.fill()
    c.arc(0, 0, r * 0.72, 0, 2 * math.pi); c.set_source_rgba(*GOLD, a); c.fill()
    c.arc(0, 0, r * 0.95, 0, 2 * math.pi); c.set_source_rgba(0.55, 0.55, 0.6, a); c.set_line_width(max(2, r * 0.05)); c.stroke()
    T(c, "₹10", 0, r * 0.18, r * 0.55, (0.35, 0.25, 0.05), a, stroke=None)
    if var % 3 == 1:
        for i in range(10):
            ang = i * math.pi / 5
            c.move_to(r * 0.78 * math.cos(ang), r * 0.78 * math.sin(ang)); c.line_to(r * 0.9 * math.cos(ang), r * 0.9 * math.sin(ang))
        c.set_source_rgba(0.4, 0.4, 0.45, a); c.set_line_width(max(2, r * 0.04)); c.stroke()
    elif var % 3 == 2:
        c.arc(0, -r * 0.45, r * 0.08, 0, 2 * math.pi); c.set_source_rgba(0.4, 0.3, 0.1, a); c.fill()
    c.restore()


def shop(**kw):
    def f(c, t, lt):
        V.canteen(c, t)
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
    K.panel(c, 1000, 380)
    coin(c, 540, 1080, 70, k(t, st, st + 0.3), 0, math.sin(t * 3) * 0.2)
    K.rows(c, t, st, [("ALL 14 DESIGNS VALID", GRN, 58, 0.3), ("SAYS RBI", YEL, 54, 3.8)], y0=1230, gap=90)


def o_refuse(c, t, lt):
    st = sh.s(2)
    K.panel(c, 880, 420)
    coin(c, 540, 1010, 90, k(t, st + 0.2, st + 0.5), 1)
    K.stamp(c, t, st + 2.6, "'FAKE HAI, NAHI CHALEGA'", 540, 1200, RED, 46, -0.04)


def o_designs(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "14 DESIGNS", 540, 470, 90, YEL, k(t, st + 0.1, st + 0.4), lw=10)
    for i in range(14):
        a = k(t, st + 0.6 + i * 0.12, st + 0.9 + i * 0.12)
        if a > 0:
            coin(c, 190 + (i % 5) * 175, 640 + (i // 5) * 175, 70, a, i)
    K.stamp(c, t, st + 4.6, "ALL = LEGAL TENDER", 540, 1200, GRN, 56, -0.03)


def o_rumour(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("DIFFERENT DESIGN", WHITE, 70, 0.2), ("IS NOT FAKE", GRN, 96, 1.4), ("IT'S JUST A RUMOUR", YEL, 60, 3.0)],
           y0=560, gap=180)


def o_bank(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("RBI TO BANKS:", GREY, 60, 0.2), ("ACCEPT COINS", WHITE, 84, 1.4), ("AT EVERY BRANCH", YEL, 70, 2.6)],
           y0=560, gap=180)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 900, 420)
    K.rows(c, t, st, [("COIN BACK IN POCKET,", WHITE, 56, 0.3), ("NO ARGUMENT?", YEL, 60, 1.6)], y0=1010, gap=110)
    K.stamp(c, t, st + 2.4, "SAME BRO?", 540, 1250, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(7)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Politely: 'RBI says all", WHITE, 46, 0.3, "left", 140),
                      ("    ₹10 coins are valid'", WHITE, 46, 0.3, "left", 140),
                      ("2. Bank refuses? Complain", WHITE, 46, 4.0, "left", 140),
                      ("    at the branch", WHITE, 46, 4.0, "left", 140),
                      ("3. Then: RBI Ombudsman", GRN, 48, 6.0, "left", 140)], y0=1000, gap=76)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "RBI'S RULE >", "ANY RUMOUR.", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "FULL OF ₹10 COINS", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    sh.shots = [
        (0, s(2), shop(mouth='o', eyes=1.3, raise_=0) if False else shop(mouth='o', eyes=1.3), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), shop(mouth='frown', angry=0.5), (1.9, 1000, 480), (2.05, 1000, 455), o_refuse, 'warm'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_designs, 'money'),
        (s(4), s(5), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_rumour, 'studio'),
        (s(5), s(6), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_bank, 'money'),
        (s(6), s(7), shop(mouth='frown', sweat=1), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), shop(mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, shop(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
