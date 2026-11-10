"""RULES YOU DIDN'T KNOW #12: insurance free-look period, 30 days (engine: vshort.Short).
Facts: IRDAI (Insurance Products) Regulations 2024 / Master Circulars on life (12 Jun 2024) and health (29 May 2024)
insurance: free-look period of 30 days from the date of receipt of the policy document (earlier 15 days) for life and
health policies. The policyholder can return the policy without giving reasons; refund of premium subject to deduction
of proportionate risk premium for the period on cover, medical examination expenses and stamp duty."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c096_freelook"
CAPS = [
    "The agent sold you a policy. At home you read it, and realise you never needed it. Is the money gone now?",
    "Can you return the policy? A: no, the money's gone. B: yes, in the free-look period. Comment!",
    "B is right. IRDAI rule: for life and health insurance, you get a 30-day free-look period after you receive the policy document.",
    "Cancel in these days without giving any reason, premium comes back. Only a small cut: days covered, medical test, stamp duty.",
    "Give the cancel request in writing, and keep proof of the date.",
    "Don't like the policy? You have 30 days. Save this, it'll help someone.",
]
HOOK = [("SOLD A POLICY YOU DON'T NEED?", WHITE), ("30 DAYS TO RETURN IT", GRN), ("RULES YOU DIDN'T KNOW #12", GREY)]
SRC = "SRC: IRDAI regulations & master circulars, 2024"
sh = None


def doc(c, x, y, w, h, a=1.0):
    S.rrect(c, x, y, w, h, 16); c.set_source_rgba(0.97, 0.97, 0.95, a); c.fill()
    S.rrect(c, x, y, w, 80, 16); c.set_source_rgba(0.15, 0.3, 0.6, a); c.fill()
    T(c, "POLICY DOCUMENT", x + w / 2, y + 54, 32, WHITE, a, stroke=None)
    for j in range(int((h - 130) / 26)):
        c.rectangle(x + 30, y + 110 + j * 26, w - 60 - (j % 3) * 40, 10); c.set_source_rgba(0.7, 0.72, 0.76, a); c.fill()


def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "morning")
        d = dict(pose='stand', mouth='flat', look=(0.6, 0.2)); d.update(kw)
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
    doc(c, 600, 760, 380, 500, k(t, st + 0.3, st + 0.6))
    a = k(t, st + 2.6, st + 2.9)
    if a > 0:
        bubble(c, 540, 480, "'WHY DID I BUY THIS?'", a)
    if t > st + 4.6:
        K.stamp(c, t, st + 4.6, "MONEY GONE?", 330, 1250, RED, 56, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "CAN YOU RETURN IT?", 540, 470, 66, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "NO, MONEY'S GONE", 1.8), ("B", "YES, FREE-LOOK PERIOD", 3.8))):
        a = k(t, st + d, st + d + 0.3)
        y = 580 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 610, y + 112, 44, WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.4, "COMMENT A or B", 540, 1120, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 400, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: YES, YOU CAN", 540, 495, 64, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 410, GRN, 54, 0.06)
    K.rows(c, t, st, [("IRDAI RULE", YEL, 58, 1.2), ("LIFE + HEALTH POLICIES", WHITE, 56, 2.8),
                      ("30 DAYS", GRN, 110, 4.6), ("FROM GETTING THE DOCUMENT", WHITE, 44, 6.0)], y0=700, gap=145)


def o_refund(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("CANCEL, NO REASON NEEDED", WHITE, 54, 0.1), ("PREMIUM BACK", GRN, 96, 1.8),
                      ("SMALL CUT ONLY:", WHITE, 54, 4.0), ("DAYS COVERED", YEL, 54, 4.8), ("MEDICAL TEST", YEL, 54, 5.6),
                      ("STAMP DUTY", YEL, 54, 6.4)], y0=440, gap=135)


def o_how(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.86)
    doc(c, 290, 450, 500, 420)
    K.stamp(c, t, st + 0.4, "CANCEL IN WRITING", 540, 960, YEL, 58, -0.04)
    K.stamp(c, t, st + 1.6, "KEEP DATE PROOF", 540, 1100, GRN, 58, 0.03)


def o_end(c, t, lt):
    K.end_card(c, "DON'T LIKE THE POLICY?", "30 DAYS. SAVE THIS.", YEL)
    st = sh.s(6)
    T(c, "A or B? COMMENT", 540, 1260, 64, YEL, k(t, st + 1.2, st + 1.5), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'warm'
    s = sh.s
    rd = dict(arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='frown', **rd), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_refund, 'money'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_how, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 3.5, 5.5] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[2][0] + 5.0], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
