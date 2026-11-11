"""RULES YOU DIDN'T KNOW #18: Lok Adalat — no court fee, fee refunded, award final (engine: vshort.Short).
Facts (NALSA 'Lok Adalats' page, updated Aug 2026; Legal Services Authorities Act 1987 s.21): "There is no court fee
payable when a matter is filed in a Lok Adalat"; if a pending court case is settled there, the court fee originally paid
is refunded (s.21(1), Court-fees Act 1870). Award = deemed decree of a civil court, final and binding, no appeal lies
(s.21(2)). Pending cases AND pre-litigation disputes can go; offences not compoundable by law cannot (s.19(5)).
Voice take sped 1.07x."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/c120_lokadalat"
CAPS = [
    "Case stuck in court for YEARS. Lawyer fees, date after date. Heard there's a place that settles it for free?",
    "Question: do you pay court fee at a Lok Adalat? A: Yes, full fee. B: Not one rupee. Comment!",
    "Answer: B. NO court fee at Lok Adalat. And if your pending court case settles there, the court fee you paid comes BACK.",
    "If both sides agree, the award is as final as a civil court decree. NO appeal against it.",
    "Bank loans, cheque bounce, accident claims, electricity and water bills go there. Serious crimes don't.",
    "Ask your district legal services authority when the next Lok Adalat is.",
]
HOOK = [("COURT CASE FOR FREE?", WHITE), ("LOK ADALAT", GRN), ("RULES YOU DIDN'T KNOW #18", GREY)]
SRC = "SRC: NALSA + Legal Services Authorities Act s.21"
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
    U.phone_frame(c, 690, 720, 340, 600, K.sms_screen("COURT NOTICE", [("Next date:", WHITE), ("adjourned", RED),
                                                                      ("again", WHITE), ("year 4...", RED)]),
                  t - st, tilt=4)
    if t > st + 3.8:
        K.stamp(c, t, st + 3.8, "SETTLE FOR FREE?", 330, 1200, YEL, 48, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "LOK ADALAT", 540, 430, 66, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "COURT FEE?", 540, 515, 58, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "YES, FULL FEE", 2.6), ("B", "NOT ONE RUPEE", 4.0))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 610, y + 118, 60, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.0, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: NOT ONE RUPEE", 540, 478, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("NO COURT FEE", GRN, 80, 0.9), ("PENDING CASE SETTLED?", WHITE, 58, 3.0),
                      ("FEE YOU PAID", WHITE, 62, 4.6), ("COMES BACK", YEL, 80, 5.6)], y0=680, gap=130)


def o_final(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("BOTH SIDES AGREE", WHITE, 64, 0.1), ("AWARD = COURT DECREE", YEL, 62, 1.5),
                      ("FINAL + BINDING", GRN, 74, 3.0), ("NO APPEAL", RED, 90, 4.4)], y0=480, gap=180)


def o_cases(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("BANK LOANS", WHITE, 64, 0.1), ("CHEQUE BOUNCE", WHITE, 64, 0.9),
                      ("ACCIDENT CLAIMS", WHITE, 64, 1.8), ("BILLS: POWER, WATER", WHITE, 58, 2.8),
                      ("SERIOUS CRIMES: NO", RED, 64, 5.4)], y0=420, gap=165)


def o_end(c, t, lt):
    K.end_card(c, "NEXT LOK ADALAT?", "ASK YOUR DISTRICT LSA", YEL)
    st = sh.s(6)
    T(c, "LEGAL SERVICES AUTHORITY", 540, 1260, 50, YEL, k(t, st + 0.3, st + 0.6), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', eyes=1.2, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3, **ph), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.25), (1.78, 960, 540), (1.85, 960, 520), o_final, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_cases, 'studio'),
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
