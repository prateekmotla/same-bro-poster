"""RULES YOU DIDN'T KNOW #26: electricity bill wrong? Pay under protest, supply can't be cut (engine: vshort.Short).
Facts: Electricity Act 2003, s.56(1): supply may be cut for non-payment only after not less than 15 clear days'
written notice; proviso: supply shall NOT be cut off if the person deposits, under protest, the amount claimed or the
electricity charges due for each month calculated on the average charge paid during the preceding six months,
whichever is less, pending disposal of the dispute. s.56(2): no sum recoverable after 2 years unless shown
continuously as arrears (not voiced). Grievances: complain to the discom first; s.42(5) every distribution licensee
must set up a Consumer Grievance Redressal Forum (CGRF); s.42(6) unresolved -> Electricity Ombudsman. Same
structure in every state (forum names/portals differ by state). Education only."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c152_bill"
CAPS = [
    "The bill came 5x higher. Plus a notice: pay or your power gets cut. Now what?",
    "Question: A: Pay it all, fight later. B: There's another way. Comment!",
    "Answer: B. Electricity Act Section 56: if you dispute the bill, deposit UNDER PROTEST either the full amount, or a monthly bill at your last 6-month average, whichever is LESS.",
    "Deposit that and they can't cut your connection while the dispute is on. And before any cut: 15 days' WRITTEN notice.",
    "Complain to the discom first. Then the CGRF, the consumer grievance forum. Then the Electricity Ombudsman.",
    "Ever got a wrong bill? Comment!",
]
HOOK = [("BILL 5x HIGHER?", WHITE), ("PAY OR POWER CUT?", RED), ("RULES YOU DIDN'T KNOW #26", GREY)]
SRC = "SRC: Electricity Act 2003, s.56 + s.42"
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


def bill_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.99, 0.98, 0.95); c.fill()
    c.rectangle(0, 0, w, 120); c.set_source_rgb(0.95, 0.65, 0.1); c.fill()
    T(c, "ELECTRICITY BILL", w / 2, 85, 36, WHITE, stroke=None)
    T(c, "LAST MONTH  Rs 1,850", w / 2, 200, 30, GREY, stroke=None)
    T(c, "THIS MONTH", w / 2, 270, 40, (0.1, 0.1, 0.12), stroke=None)
    T(c, "Rs 9,640", w / 2, 360, 66, (0.8, 0.1, 0.1), stroke=None)
    if tt > 1.6:
        S.rrect(c, 30, 400, w - 60, 120, 18); c.set_source_rgb(1, 0.88, 0.88); c.fill()
        T(c, "PAY NOW OR", w / 2, 450, 30, (0.8, 0.1, 0.1), stroke=None)
        T(c, "SUPPLY WILL BE CUT", w / 2, 495, 30, (0.8, 0.1, 0.1), stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 690, 720, 340, 600, bill_screen, t - st, tilt=4)
    if t > st + 3.6:
        K.stamp(c, t, st + 3.6, "NOW WHAT?!", 330, 1200, RED, 56, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "WRONG BILL + CUT NOTICE", 540, 450, 56, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "PAY ALL, FIGHT LATER", 0.6), ("B", "ANOTHER WAY", 3.4))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 116, 48, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.0, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 360, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: PAY UNDER PROTEST", 540, 458, 56, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 370, GRN, 50, 0.06)
    K.rows(c, t, st, [("ELECTRICITY ACT, SEC 56", YEL, 54, 1.0), ("FULL BILL", WHITE, 60, 6.3),
                      ("OR", GREY, 46, 7.4), ("6-MONTH AVG / MONTH", WHITE, 56, 7.8), ("WHICHEVER IS LESS", GRN, 64, 10.0)],
           y0=640, gap=125)


def o_cut(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("DEPOSIT THAT =", WHITE, 60, 0.1), ("NO CUT DURING DISPUTE", GRN, 62, 1.6),
                      ("ANY CUT NEEDS", WHITE, 56, 3.4), ("15 DAYS' WRITTEN", YEL, 66, 4.3), ("NOTICE", YEL, 66, 4.6)],
           y0=430, gap=150)


def o_ladder(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.86)
    T(c, "COMPLAINT LADDER", 540, 430, 64, YEL, k(t, st, st + 0.2), lw=10)
    for i, (txt, d) in enumerate((("1. YOUR DISCOM", 0.3), ("2. CGRF (GRIEVANCE FORUM)", 1.5), ("3. ELECTRICITY OMBUDSMAN", 4.4))):
        a = k(t, st + d, st + d + 0.3)
        y = 560 + i * 210
        S.rrect(c, 110, y, 860, 160, 36); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        T(c, txt, 540, y + 100, 46, (WHITE, YEL, GRN)[i], a, stroke=None)


def o_end(c, t, lt):
    K.end_card(c, "EVER GOT A WRONG BILL?", "COMMENT", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', eyes=1.2, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3, **ph), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_cut, 'studio'),
        (s(5), s(6), sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_ladder, 'studio'),
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
