"""THEY'RE TRICKING YOU #7: 'No added sugar' still has sugar (engine: vshort.Short).
Fact: FSSAI Food Safety and Standards (Advertising and Claims) Regulations 2018, nutrition claims schedule:
'no added sugar' only means no sugars were added during processing; foods with naturally occurring sugars (fruit,
dates, milk) still contain sugar; 'sugar free' claim allowed only if the food has not more than 0.5 g sugars per
100 g / 100 ml. Total sugars are declared in the mandatory nutrition table (FSSAI Labelling & Display Regs 2020).
FSSAI has also acted against misleading 'no added sugar' claims (2024-25 media reports). No brand shown."""

import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c111_nosugar"
CAPS = [
    "The packet says it big: NO ADDED SUGAR. So zero sugar, right?",
    "A: yes, it's sugar-free. B: no, there's sugar inside. Comment!",
    "B is right. 'No added sugar' only means they didn't add sugar on top.",
    "But dates, fruit pulp and milk already have sugar. And 'sugar free' is allowed only under 0.5 g per 100 g.",
    "Want the real number? Flip the packet and read 'Total sugars' in the nutrition table.",
    "Next time you pick up a packet, flip it first.",
]
HOOK = [("'NO ADDED SUGAR'", WHITE), ("= ZERO SUGAR?", YEL), ("THEY'RE TRICKING YOU #7", GREY)]
SRC = "SRC: FSSAI claims regulations 2018"
Q1, Q2 = "'NO ADDED SUGAR'", "MEANS ZERO SUGAR?"
OPT_A, OPT_B, OPT_T = "YES, NO SUGAR", "NO, SUGAR INSIDE", (0.1, 1.6, 3.6)
sh = None

def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "morning")
        d = dict(pose='stand', mouth='flat', look=(0.6, 0)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f



def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, Q1, 540, 430, 62, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, Q2, 540, 515, 56, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", OPT_A, OPT_T[0]), ("B", OPT_B, OPT_T[1]))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 114, 50, WHITE, a, stroke=None)
    K.stamp(c, t, st + OPT_T[2], "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_hook(c, t, lt):
    a = U.eob(k(t, 0.2, 0.7))
    c.save(); c.translate(700, 980); c.rotate(0.06); c.scale(a, a)
    S.rrect(c, -170, -260, 340, 520, 34); c.set_source_rgb(0.95, 0.55, 0.25); c.fill()
    S.rrect(c, -170, -260, 340, 80, 34); c.set_source_rgb(0.8, 0.4, 0.15); c.fill()
    T(c, "FRUIT BAR", 0, -110, 50, WHITE, stroke=None)
    c.arc(0, 10, 70, 0, 6.283); c.set_source_rgb(0.85, 0.2, 0.25); c.fill()
    S.rrect(c, -150, 120, 300, 100, 22); c.set_source_rgb(1, 1, 1); c.fill()
    T(c, "NO ADDED", 0, 162, 34, (0.1, 0.5, 0.2), stroke=None)
    T(c, "SUGAR", 0, 204, 40, (0.1, 0.5, 0.2), stroke=None)
    c.restore()
    if t > 3.2:
        K.stamp(c, t, 3.2, "ZERO SUGAR?", 300, 1260, YEL, 60, -0.05)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: SUGAR INSIDE", 540, 478, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 390, GRN, 54, 0.06)
    K.rows(c, t, st, [("'No ADDED sugar' only means", WHITE, 50, 1.0), ("NOTHING ADDED ON TOP", YEL, 64, 2.0)],
           y0=720, gap=120)


def o_four(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("DATES. FRUIT PULP. MILK.", WHITE, 56, 0.2), ("ALREADY HAVE SUGAR", RED, 70, 2.0),
                      ("'SUGAR FREE' =", WHITE, 64, 3.6), ("UNDER 0.5 g / 100 g", GRN, 76, 5.2)], y0=470, gap=170)


def o_five(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "FLIP THE PACKET", 540, 470, 76, YEL, k(t, st, st + 0.3), lw=10)
    a = k(t, st + 1.0, st + 1.4)
    S.rrect(c, 190, 560, 700, 480, 24); c.set_source_rgba(1, 1, 1, 0.96 * a); c.fill()
    T(c, "NUTRITION INFORMATION", 540, 625, 36, (0.1, 0.1, 0.12), a, stroke=None)
    for i, (l, v) in enumerate((("Per 100 g", ""), ("Energy", "410 kcal"), ("Carbohydrate", "62 g"),
                                ("Total sugars", "38 g"), ("Added sugars", "0 g"))):
        y = 700 + i * 70
        hi = l == "Total sugars"
        if hi and t > st + 2.2:
            S.rrect(c, 210, y - 46, 660, 62, 12); c.set_source_rgba(1, 0.85, 0.2, 0.9); c.fill()
        T(c, l, 230, y, 34, (0.1, 0.1, 0.12), a, stroke=None, anchor="left")
        T(c, v, 850, y, 34, (0.1, 0.1, 0.12), a, stroke=None, anchor="right")
    T(c, "Example label", 540, 1080, 30, GREY, a, stroke=None)


def o_end(c, t, lt):
    K.end_card(c, "NO ADDED SUGAR", "IS NOT ZERO SUGAR", YEL)
    st = sh.s(6)
    T(c, "FLIP IT FIRST", 540, 1260, 64, GRN, k(t, st + 0.6, st + 0.9), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', squint=0.2), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_four, 'studio'),
        (s(5), s(6), sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_five, 'money'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 4.5] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
