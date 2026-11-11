"""THEY'RE TRICKING YOU #8: 'Mango DRINK' is not mango juice (engine: vshort.Short).
Facts: FSSAI directive (3 Jun 2024, Business Standard): remove '100% fruit juice' claims from labels/ads of
reconstituted juices - no provision for a '100%' claim under the Advertising & Claims Regulations 2018; misleading where
water is the main ingredient or the juice is reconstituted from concentrate; reconstituted juice must say so; added
sweeteners above 15 g/kg = 'sweetened juice'. FSSAI 2016 (carbonated): below 10% fruit content cannot be called fruit
juice. Ingredients are listed in descending order of weight. Generic bottle, no brand shown."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/c119_fruitdrink"
CAPS = [
    "Big mango on the bottle, 'MANGO DRINK' on top. So it's juice inside, right?",
    "A: Yes, it's fruit juice. B: No, mostly water and sugar. Comment!",
    "B is right. If it says 'drink' or 'beverage', it's not juice. A little fruit, the rest is water, sugar and flavour.",
    "And in 2024 FSSAI told brands to remove '100% fruit juice' claims from juices made from concentrate.",
    "How to check? Read the ingredients on the back. First word 'Water' = mostly water. Sugar? See the nutrition table.",
    "Next time read the label, not the mango photo.",
]
HOOK = [("'MANGO DRINK'?", WHITE), ("NOT MANGO JUICE", RED), ("THEY'RE TRICKING YOU #8", GREY)]
SRC = "SRC: FSSAI (2024 directive, labelling rules)"
sh = None


def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "evening")
        d = dict(pose='stand', mouth='flat', look=(0.6, 0)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


ORANGE = (1.0, 0.62, 0.1)


def bottle(c, x, y, s=1.0, a=1.0, back=False):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.push_group()
    S.rrect(c, -40, -330, 80, 70, 14); c.set_source_rgb(0.95, 0.5, 0.1); c.fill()          # cap
    c.move_to(-50, -260); c.curve_to(-50, -200, -120, -190, -120, -120); c.line_to(-120, 300)
    c.curve_to(-120, 330, 120, 330, 120, 300); c.line_to(120, -120); c.curve_to(120, -190, 50, -200, 50, -260); c.close_path()
    c.set_source_rgba(1.0, 0.75, 0.2, 0.92); c.fill()
    S.rrect(c, -130, -60, 260, 270, 20); c.set_source_rgb(0.98, 0.97, 0.92); c.fill()          # label
    if not back:
        c.save(); c.translate(0, 30); c.rotate(-0.3); c.scale(1, 0.78)
        c.arc(0, 0, 70, 0, 2 * math.pi); c.restore(); c.set_source_rgb(*ORANGE); c.fill()      # mango
        c.move_to(10, -30); c.curve_to(40, -70, 80, -60, 90, -40); c.curve_to(60, -30, 30, -30, 10, -30)
        c.set_source_rgb(0.2, 0.65, 0.25); c.fill()
        T(c, "MANGO", 0, 150, 52, (0.85, 0.35, 0.05), stroke=None)
        T(c, "DRINK", 0, 192, 30, (0.4, 0.4, 0.42), stroke=None)
    else:
        T(c, "INGREDIENTS:", 0, -18, 26, (0.15, 0.15, 0.18), stroke=None)
        for j, (w, col) in enumerate((("WATER", RED), ("SUGAR", RED), ("Mango pulp", (0.3, 0.3, 0.32)),
                                      ("Acidity regulator", (0.3, 0.3, 0.32)), ("Flavour", (0.3, 0.3, 0.32)))):
            T(c, w, 0, 22 + j * 38, 30 if j < 2 else 22, col, stroke=None)
    c.pop_group_to_source(); c.paint_with_alpha(a)
    c.restore()


def o_hook(c, t, lt):
    st = sh.s(1)
    bottle(c, 330, 860, 1.05, k(t, st, st + 0.3))
    if t > st + 3.3:
        K.stamp(c, t, st + 3.3, "JUICE INSIDE?", 330, 1270, YEL, 50, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "'MANGO DRINK'", 540, 430, 66, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "WHAT'S INSIDE?", 540, 515, 58, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "FRUIT JUICE", 0.4), ("B", "WATER + SUGAR", 2.0))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 610, y + 118, 60, WHITE, a, stroke=None)
    K.stamp(c, t, st + 4.4, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: WATER + SUGAR", 540, 478, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("'DRINK' / 'BEVERAGE'", YEL, 62, 0.9), ("IS NOT JUICE", RED, 80, 2.0), ("LITTLE FRUIT +", WHITE, 62, 3.6),
                      ("WATER, SUGAR, FLAVOUR", WHITE, 58, 4.4)], y0=690, gap=125)


def o_fssai(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("FSSAI, 2024", YEL, 70, 0.3), ("REMOVE '100% FRUIT JUICE'", WHITE, 54, 3.0),
                      ("CLAIMS", RED, 90, 4.6), ("ON JUICE MADE FROM", WHITE, 54, 6.2), ("CONCENTRATE", YEL, 76, 7.0)],
           y0=420, gap=170)


def o_check(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "FLIP IT. READ THIS:", 540, 420, 62, YEL, k(t, st, st + 0.3), lw=10)
    bottle(c, 540, 900, 1.25, k(t, st + 0.3, st + 0.7), back=True)
    if t > st + 2.8:
        K.stamp(c, t, st + 2.8, "1st = WATER? MOSTLY WATER", 540, 1360, RED, 44, -0.03)


def o_end(c, t, lt):
    K.end_card(c, "READ THE LABEL", "NOT THE MANGO PHOTO", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'warm'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', eyes=1.2, arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3, **ph), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.25), (1.78, 960, 540), (1.85, 960, 520), o_fssai, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_check, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 5.5] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
