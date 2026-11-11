"""SCAM OF THE WEEK #13: '0% interest, instant loan, just pay the processing fee first' fake loan app (engine: vshort.Short).
Facts: RBI (Digital Lending) Directions 2025 (8 May 2025): regulated lenders must give a Key Fact Statement (KFS)
with the Annual Percentage Rate (APR) before the loan (para 8); disbursal always straight into the borrower's own
bank account, never via a third-party / LSP account (para 9); RBI publishes a public directory of regulated
entities' Digital Lending Apps on its website (live since 1 Jul 2025, per the Finance Ministry's Rajya Sabha reply,
ANI). Fraud reporting: MHA helpline 1930 / cybercrime.gov.in. The fee-first-then-vanish pattern is dramatised
(generic app, no brand named). Education only, not financial advice."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/c147_loanapp"
CAPS = [
    "An ad on your phone: ZERO percent interest, loan in 5 minutes. Just send the processing fee first. Will you?",
    "Question: A: Pay the fee, the loan will come. B: Wait, check first. Comment!",
    "Answer: B. This is the fake loan app scam. The fee is gone and the loan never comes.",
    "Under RBI rules a real lender gives a Key Fact Statement BEFORE the loan, with the APR, the full yearly cost. And the loan goes straight into YOUR bank account.",
    "Is the app real? Check RBI's list of digital lending apps on its website.",
    "Got trapped? Call 1930 or go to cybercrime.gov.in. Have YOU seen an ad like this? Comment!",
]
HOOK = [("0% INTEREST LOAN?", WHITE), ("PAY A FEE FIRST?", RED), ("SCAM OF THE WEEK #13", GREY)]
SRC = "SRC: RBI Digital Lending Directions 2025"
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


def ad_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.98, 0.96, 0.9); c.fill()
    c.rectangle(0, 0, w, 120); c.set_source_rgb(0.95, 0.45, 0.1); c.fill()
    T(c, "INSTANT LOAN", w / 2, 85, 42, WHITE, stroke=None)
    T(c, "0%", w / 2, 250, 130, (0.1, 0.55, 0.25), stroke=None)
    T(c, "INTEREST", w / 2, 305, 44, (0.1, 0.1, 0.12), stroke=None)
    T(c, "Rs 50,000 in 5 MIN", w / 2, 365, 32, (0.2, 0.2, 0.25), stroke=None)
    S.rrect(c, 30, 395, w - 60, 90, 16); c.set_source_rgb(1, 0.88, 0.88); c.fill()
    T(c, "PROCESSING FEE", w / 2, 432, 26, RED, stroke=None)
    T(c, "Rs 1,999 FIRST", w / 2, 470, 30, RED, stroke=None)
    S.rrect(c, 40, h - 110, w - 80, 80, 40); c.set_source_rgb(0.1, 0.55, 0.25); c.fill()
    T(c, "PAY FEE", w / 2, h - 57, 36, WHITE, stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 690, 720, 340, 600, ad_screen, t - st, tilt=4)
    if t > st + 4.0:
        K.stamp(c, t, st + 4.0, "FEE FIRST?!", 330, 1200, RED, 56, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "'0% LOAN, PAY FEE FIRST'", 540, 450, 56, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "PAY THE FEE", 1.1), ("B", "WAIT, CHECK FIRST", 3.5))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 116, 54, WHITE, a, stroke=None)
    K.stamp(c, t, st + 4.6, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: CHECK FIRST", 540, 478, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("FAKE LOAN APP SCAM", YEL, 62, 1.2), ("FEE: GONE", RED, 84, 2.9), ("LOAN: NEVER COMES", RED, 70, 3.8)],
           y0=700, gap=140)


def o_rbi(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("RBI RULES: REAL LENDER", WHITE, 54, 0.1), ("KEY FACT STATEMENT", YEL, 66, 2.2),
                      ("BEFORE THE LOAN", WHITE, 54, 3.4), ("APR = FULL YEARLY COST", GRN, 56, 5.0),
                      ("LOAN STRAIGHT TO", WHITE, 54, 8.0), ("YOUR BANK ACCOUNT", GRN, 64, 8.6)], y0=420, gap=140)


def o_list(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("IS THE APP REAL?", WHITE, 66, 0.1), ("CHECK RBI'S LIST", YEL, 76, 1.6),
                      ("DIGITAL LENDING APPS", GRN, 58, 2.4), ("ON RBI'S WEBSITE", GREY, 48, 3.2)], y0=470, gap=170)


def o_end(c, t, lt):
    K.end_card(c, "GOT TRAPPED? CALL", "1930", GRN)
    st = sh.s(6)
    T(c, "cybercrime.gov.in", 540, 1200, 50, WHITE, k(t, st + 2.0, st + 2.3), lw=8)
    T(c, "SEEN THIS AD? COMMENT", 540, 1290, 50, YEL, k(t, st + 3.6, st + 3.9), lw=10)


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
        (s(4), s(5), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_rbi, 'studio'),
        (s(5), s(6), sw(mouth='smile', **ph), (1.78, 960, 540), (1.85, 960, 520), o_list, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='flat', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
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
