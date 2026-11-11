"""RULES YOU DIDN'T KNOW #27: best before vs expiry/use by (engine: vshort.Short).
Facts (FSSAI Food Safety and Standards (Labelling and Display) Regulations 2020, compendium v2 29.12.2021):
- Reg 2(1)(c) Best before: end of period the food stays fully marketable/retains claimed qualities; 'beyond that date,
  the food may still be perfectly safe to consume, though its quality may have diminished'; not to be sold if unsafe.
- Reg 2(1)(u) Use by/expiry: after it the product may not remain safe and 'shall not be sold or distributed for human
  consumption'.
- Reg 5(10)(a): 'Date of manufacture or packaging' and 'Expiry/Use by' shall be declared; 'Best before' may be used as
  optional or additional information. (Exemptions in 5(10)(d), e.g. whole fresh fruit/veg, salt, sugar - not voiced.)"""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c156_expiry"
CAPS = [
    "Two packets. One is past its BEST BEFORE. The other is past its EXPIRY date. Which one could still be safe?",
    "Question: A: The best before one. B: The expiry one. Comment!",
    "Answer: A. Under FSSAI rules, BEST BEFORE is a QUALITY date. After it the taste may drop, but the food can still be safe, if the pack is fine and stored right.",
    "EXPIRY or USE BY is a SAFETY date. After it the food isn't considered safe, and shops can't even sell it.",
    "And every pack MUST show the manufacture date and expiry. Best before is optional.",
    "When did you last check an expiry date? Comment!",
]
HOOK = [("BEST BEFORE vs EXPIRY", WHITE), ("WHICH ONE IS SAFE?", YEL), ("RULES YOU DIDN'T KNOW #27", GREY)]
SRC = "SRC: FSSAI Labelling & Display Regs 2020"
sh = None
INK = (0.1, 0.1, 0.12)


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


def pack(c, x, y, s, name, col, label, date, a=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.push_group()
    dk = (col[0] * 0.78, col[1] * 0.78, col[2] * 0.78)
    S.rrect(c, -160, -220, 320, 440, 30); c.set_source_rgb(*col); c.fill()
    S.rrect(c, -160, -220, 320, 70, 30); c.set_source_rgb(*dk); c.fill()
    for zx in range(-160, 161, 20):
        c.move_to(zx, -220); c.line_to(zx + 10, -232); c.line_to(zx + 20, -220)
    c.set_source_rgb(*dk); c.fill()
    T(c, name, 0, -70, 50, WHITE, stroke=None)
    S.rrect(c, -130, 20, 260, 160, 18); c.set_source_rgb(1, 1, 1); c.fill()
    T(c, label, 0, 75, 30, INK, stroke=None)
    T(c, date, 0, 140, 46, (0.75, 0.1, 0.1), stroke=None)
    c.pop_group_to_source(); c.paint_with_alpha(a)
    c.restore()


def two_packs(c, t, st, la="BEST BEFORE", lb="EXPIRY", a=1.0, s=1.0):
    pack(c, 290, 900, s, "CHIPS", (0.2, 0.45, 0.8), la, "08/11/26", a * k(t, st, st + 0.3))
    pack(c, 790, 900, s, "BREAD", (0.85, 0.5, 0.15), lb, "08/11/26", a * k(t, st + 0.4, st + 0.7))


def o_hook(c, t, lt):
    st = sh.s(1)
    U.dim(c, 0.55)
    two_packs(c, t, st)
    T(c, "TODAY: 11/11/26", 540, 1290, 52, YEL, k(t, st + 1.0, st + 1.3), lw=8)
    K.stamp(c, t, st + 1.4, "PASSED", 290, 1150, RED, 50, -0.08)
    K.stamp(c, t, st + 2.6, "PASSED", 790, 1150, RED, 50, 0.06)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "WHICH COULD BE SAFE?", 540, 450, 60, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "PAST BEST BEFORE", 0.5), ("B", "PAST EXPIRY", 1.8))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, INK, a, stroke=None)
        T(c, txt, 615, y + 116, 50, WHITE, a, stroke=None)
    K.stamp(c, t, st + 2.8, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 360, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "A: BEST BEFORE", 540, 458, 60, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 370, GRN, 50, 0.06)
    K.rows(c, t, st, [("= QUALITY DATE", YEL, 66, 1.6), ("TASTE MAY DROP", WHITE, 56, 4.0),
                      ("CAN STILL BE SAFE", GRN, 62, 6.0), ("IF PACK IS FINE", WHITE, 50, 8.4),
                      ("+ STORED RIGHT", WHITE, 50, 9.6)], y0=650, gap=120)


def o_expiry(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    S.rrect(c, 110, 360, 860, 150, 40); c.set_source_rgba(0.5, 0.08, 0.08, 0.95); c.fill()
    T(c, "EXPIRY / USE BY", 540, 458, 60, WHITE, stroke=None)
    K.rows(c, t, st, [("= SAFETY DATE", YEL, 66, 1.4), ("AFTER IT: NOT SAFE", RED, 58, 3.0),
                      ("SHOPS CAN'T SELL IT", WHITE, 58, 5.2)], y0=660, gap=140)
    K.stamp(c, t, st + 5.8, "DON'T EAT", 540, 1130, RED, 60, -0.04)


def lbl(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.99, 0.98, 0.95); c.fill()
    T(c, "PACK LABEL", w / 2, 80, 34, GREY, stroke=None)
    rows = (("MFG DATE", "MUST", GRN, 0.3), ("EXPIRY / USE BY", "MUST", GRN, 1.6), ("BEST BEFORE", "OPTIONAL", YEL, 3.6))
    for i, (a_, b_, col, d) in enumerate(rows):
        al = k(tt, d, d + 0.3)
        y = 150 + i * 130
        S.rrect(c, 24, y, w - 48, 110, 16); c.set_source_rgba(0.12, 0.13, 0.2, al); c.fill()
        T(c, a_, w / 2, y + 48, 30, WHITE, al, stroke=None)
        T(c, b_, w / 2, y + 92, 32, col, al, stroke=None)


def o_label(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.7)
    U.phone_frame(c, 350, 560, 380, 620, lbl, t - st, tilt=-2)
    K.stamp(c, t, st + 0.4, "FSSAI RULE", 540, 1300, YEL, 54, -0.03)


def o_end(c, t, lt):
    K.end_card(c, "LAST TIME YOU CHECKED?", "COMMENT", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', eyes=1.1), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_expiry, 'studio'),
        (s(5), s(6), sw(mouth='smile', **ph), (1.78, 960, 540), (1.85, 960, 520), o_label, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', **ph), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
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
