"""RULES YOU DIDN'T KNOW #10: RTI for Rs 10 (engine: vshort.Short).
Fact: Right to Information Act, 2005 (cic.gov.in): s.6 any citizen can ask a public authority for information in
writing/electronically, no reason needed; s.7(1) reply within 30 days, 48 hours where it concerns the life or
liberty of a person; s.7(5) no fee from persons below the poverty line; s.19 first appeal. RTI Rules 2012: Rs 10
application fee for central public authorities (states set their own fee rules, mostly Rs 10). Online filing for
central ministries/departments: rtionline.gov.in."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c088_rti"
CAPS = [
    "Your file is stuck in a government office for months, and every time it's: 'come tomorrow.' Hear this rule.",
    "For just ₹10, can you demand a written answer from a government office? A: fake. B: true. Comment!",
    "B is right. RTI Act, 2005. For central government offices the fee is just ₹10, and you can file it online too.",
    "The officer has to reply in 30 days. If it's about someone's life or liberty, in 48 hours.",
    "BPL applicants pay no fee. No reply? File a first appeal.",
    "File stuck? ₹10, one RTI. Save this.",
]
HOOK = [("FILE STUCK FOR MONTHS?", WHITE), ("₹10 GETS YOU ANSWERS", GRN), ("RULES YOU DIDN'T KNOW #10", GREY)]
SRC = "SRC: RTI Act 2005, RTI Rules 2012"
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


def bubble(c, x, y, txt, a=1.0, size=42):
    w = len(txt) * size * 0.62 + 70
    S.rrect(c, x - w / 2, y, w, 96, 40); c.set_source_rgba(1, 1, 1, 0.96 * a); c.fill()
    T(c, txt, x, y + 64, size, (0.1, 0.1, 0.15), a, stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    # stack of files with a 'PENDING' tag
    for j in range(5):
        S.rrect(c, 560 + j * 6, 1120 - j * 46, 380, 56, 8); c.set_source_rgb(0.85 - j * 0.04, 0.75 - j * 0.03, 0.5); c.fill()
    K.stamp(c, t, st + 0.8, "PENDING: 4 MONTHS", 750, 1240, RED, 44, -0.05)
    a = k(t, st + 3.6, st + 3.9)
    if a > 0:
        bubble(c, 330, 820, "'COME TOMORROW...'", a, 36)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "₹10 = WRITTEN ANSWER", 540, 430, 62, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "FROM A GOVT OFFICE?", 540, 510, 58, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "FAKE", 3.4), ("B", "TRUE", 4.6))):
        a = k(t, st + d, st + d + 0.3)
        y = 600 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 118, 64, WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.6, "COMMENT A or B", 540, 1140, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: TRUE", 540, 478, 70, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 390, GRN, 54, 0.06)
    K.rows(c, t, st, [("RTI ACT, 2005", YEL, 64, 1.0), ("FEE: ₹10", GRN, 110, 3.6),
                      ("(central govt offices)", GREY, 40, 3.8), ("FILE ONLINE TOO", WHITE, 58, 6.2),
                      ("rtionline.gov.in", YEL, 50, 6.6)], y0=680, gap=125)


def o_time(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "REPLY DEADLINE", 540, 470, 66, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (big, small, col, d) in enumerate((("30 DAYS", "normal request", YEL, 0.6),
                                              ("48 HOURS", "life or liberty at stake", GRN, 3.0))):
        a = k(t, st + d, st + d + 0.3)
        y = 580 + i * 300
        S.rrect(c, 140, y, 800, 250, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        T(c, big, 540, y + 130, 100, col, a, stroke=None)
        T(c, small, 540, y + 205, 40, WHITE, a, stroke=None, bold=False)


def o_bpl(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("BPL?", WHITE, 70, 0.1), ("NO FEE", GRN, 110, 0.6), ("NO REPLY?", WHITE, 64, 2.0),
                      ("FIRST APPEAL", YEL, 90, 2.6)], y0=480, gap=170)


def o_end(c, t, lt):
    K.end_card(c, "FILE STUCK?", "₹10. ONE RTI.", YEL)
    st = sh.s(6)
    T(c, "SAVE THIS", 540, 1260, 64, GRN, k(t, st + 2.0, st + 2.3), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    sh.shots = [
        (0, s(2), w_room(mouth='frown', angry=0.4), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_time, 'studio'),
        (s(5), s(6), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_bpl, 'money'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 3.5, 5.5] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[2][0] + 7.5], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
