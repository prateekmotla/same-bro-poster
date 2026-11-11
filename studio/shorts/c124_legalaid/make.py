"""RULES YOU DIDN'T KNOW #19: free legal aid — who gets it (engine: vshort.Short).
Facts (NALSA eligibility page; Legal Services Authorities Act 1987 s.12; SCLSC FAQ): eligible = SC/ST member, victim of
trafficking/begar, a woman or a child, disabled person, person in undeserved want (disaster, ethnic violence, caste
atrocity...), industrial workman, person in custody, or income below the state-prescribed limit (Delhi Rs 3,00,000 per
NALSA list; Rs 5 lakh for Supreme Court cases). Women get aid irrespective of income. Aid = lawyer at state expense,
court fee and incidental expenses paid (Rajasthan SLSA). NALSA helpline 15100 (nalsa.gov.in menu > nalsa15100.in)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/c124_legalaid"
CAPS = [
    "You need to fight a case but can't pay a lawyer. So no justice for you?",
    "Question: who gets a FREE government lawyer? A: Only the poor. B: Every woman and child too, whatever the income. Comment!",
    "Answer: B. Section 12, Legal Services Authorities Act: every woman, every child, SC/ST, disabled, people in custody, and low-income people.",
    "Each state sets its own income limit. Delhi: Rs 3 lakh a year.",
    "And free means FULLY free. Lawyer, court fee, papers: the government pays.",
    "Where to go? The legal services authority office at your district court, or NALSA helpline 15100.",
]
HOOK = [("NO MONEY FOR A LAWYER?", WHITE), ("GET ONE FREE", GRN), ("RULES YOU DIDN'T KNOW #19", GREY)]
SRC = "SRC: NALSA + Legal Services Authorities Act s.12"
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


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 690, 720, 340, 600, K.sms_screen("LAWYER", [("Fees:", WHITE), ("Rs 50,000", RED),
                                                                ("advance", WHITE), ("first", RED)]),
                  t - st, tilt=4)
    if t > st + 3.0:
        K.stamp(c, t, st + 3.0, "NO JUSTICE?!", 330, 1200, RED, 50, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "FREE GOVT LAWYER", 540, 430, 62, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "WHO GETS IT?", 540, 515, 58, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, sz, d) in enumerate((("A", "ONLY THE POOR", 60, 2.6), ("B", "EVERY WOMAN + CHILD TOO", 44, 4.0))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 625, y + 112, sz, WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.6, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: WOMEN + CHILDREN TOO", 540, 474, 56, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("SECTION 12, LSA ACT", YEL, 56, 0.9), ("EVERY WOMAN", WHITE, 60, 2.8), ("EVERY CHILD", WHITE, 60, 3.6),
                      ("SC / ST, DISABLED", WHITE, 60, 4.6), ("PEOPLE IN CUSTODY", WHITE, 60, 6.0),
                      ("LOW INCOME", GRN, 66, 7.4)], y0=650, gap=110)


def o_income(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("INCOME LIMIT", WHITE, 70, 0.1), ("SET BY EACH STATE", YEL, 62, 1.0),
                      ("DELHI:", WHITE, 64, 2.6), ("₹3 LAKH / YEAR", GRN, 90, 3.0)], y0=480, gap=180)


def o_free(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("FULLY FREE", GRN, 90, 0.1), ("LAWYER", WHITE, 66, 1.8), ("COURT FEE", WHITE, 66, 2.5),
                      ("PAPERS", WHITE, 66, 3.2), ("GOVT PAYS", YEL, 80, 4.2)], y0=440, gap=165)


def o_end(c, t, lt):
    K.end_card(c, "DISTRICT COURT LSA", "OR CALL 15100", GRN)
    st = sh.s(6)
    T(c, "NALSA HELPLINE", 540, 1260, 54, YEL, k(t, st + 0.3, st + 0.6), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'warm'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', eyes=1.2, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3, **ph), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.25), (1.78, 960, 540), (1.85, 960, 520), o_income, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_free, 'studio'),
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
