"""THEY'RE TRICKING YOU #11: 'Buy now, pay later, zero interest' = free money? No, it's a loan (engine: vshort.Short).
Facts: CRIF High Mark (credit bureau, Jan 2025, 'Buy Now, Pay Later: how BNPL influences your credit score'): BNPL loans
are issued by a merchant's partner bank or NBFC, typically interest-free over 2-4 instalments; on-time payments are
reported to credit bureaus, and 'Late or missed payments are reported to credit bureaus, which can harm your
creditworthiness'. Business Today (Jul 2025): missed BNPL payments escalate from fees to big burdens. No fee % shown
(no standard rate). Fair to brands: no app named. Education only, not financial advice."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c143_bnpl"
CAPS = [
    "'Buy now, pay later.' Buy now, pay after. Zero interest! So it's free money, right?",
    "Question: A: It's free, no tension. B: It's actually a loan. Comment!",
    "Answer: B. Pay later is a LOAN from a bank or NBFC. Pay on time and it really costs nothing extra.",
    "But miss the date: late fee. And it goes to the credit bureau. Your CIBIL score can drop.",
    "Score drops, and tomorrow a bike loan or credit card gets harder. Even for small amounts.",
    "So use pay later only when you KNOW you'll pay on the date. How many pay later apps are on your phone? Comment!",
]
HOOK = [("'PAY LATER, 0% INTEREST'", WHITE), ("FREE MONEY or A LOAN?", YEL), ("THEY'RE TRICKING YOU #11", GREY)]
SRC = "SRC: CRIF High Mark credit bureau (Jan 2025)"
sh = None


def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "evening")
        d = dict(pose='stand', mouth='smile', look=(0.6, 0)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def shop_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.98); c.fill()
    S.rrect(c, 40, 50, w - 80, 190, 20); c.set_source_rgb(0.85, 0.88, 0.95); c.fill()
    c.arc(w / 2, 130, 55, 0, 6.283); c.set_source_rgb(0.2, 0.2, 0.25); c.fill()        # headphones icon
    c.arc(w / 2, 130, 35, 0, 6.283); c.set_source_rgb(0.85, 0.88, 0.95); c.fill()
    T(c, "Rs 2,999", w / 2, 300, 40, (0.1, 0.1, 0.15), stroke=None)
    a = k(tt, 0.6, 0.9)
    S.rrect(c, 30, 350, w - 60, 90, 22); c.set_source_rgba(0.55, 0.25, 0.85, a); c.fill()
    T(c, "PAY LATER", w / 2, 395, 34, WHITE, a, stroke=None)
    T(c, "0% interest", w / 2, 428, 24, YEL, a, stroke=None)
    S.rrect(c, 30, 460, w - 60, 70, 22); c.set_source_rgba(0.2, 0.2, 0.25, 0.3); c.fill()
    T(c, "Pay now", w / 2, 505, 28, (0.3, 0.3, 0.35), stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 120, 720, 320, 560, shop_screen, t - st, tilt=4)
    if t > st + 3.2:
        K.stamp(c, t, st + 3.2, "FREE MONEY?", 740, 1230, YEL, 54, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "BUY NOW, PAY LATER IS...", 540, 450, 56, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, sz, d) in enumerate((("A", "FREE. NO TENSION", 52, 1.0), ("B", "ACTUALLY A LOAN", 52, 3.0))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 114, sz, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.0, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_loan(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 300, 860, 130, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: IT'S A LOAN", 540, 385, 60, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 310, GRN, 50, 0.06)
    for i, (txt, col, sz, d) in enumerate((("FROM A BANK / NBFC", YEL, 56, 2.0), ("PAID ON TIME?", WHITE, 56, 4.4),
                                          ("NO EXTRA COST", GRN, 66, 5.4))):
        T(c, txt, 540, 600 + i * 170, sz, col, k(t, st + d, st + d + 0.3), lw=10)


def meter(c, x, y, val, a):
    import math
    for j in range(30):
        f = j / 29
        ang = math.pi + f * math.pi
        col = (1 - f, 0.3 + 0.6 * f, 0.25)
        c.arc(x, y, 210, ang, ang + math.pi / 31); c.set_source_rgba(*col, a); c.set_line_width(40); c.stroke()
    ang = math.pi + val * math.pi
    c.move_to(x, y); c.line_to(x + 170 * math.cos(ang), y + 170 * math.sin(ang))
    c.set_source_rgba(1, 1, 1, a); c.set_line_width(12); c.stroke()
    c.arc(x, y, 20, 0, 2 * math.pi); c.fill()


def o_late(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "MISSED THE DATE?", 540, 430, 66, WHITE, k(t, st, st + 0.3), lw=10)
    T(c, "+ LATE FEE", 540, 560, 76, RED, k(t, st + 1.3, st + 1.6), lw=10)
    T(c, "REPORTED TO CREDIT BUREAU", 540, 690, 48, YEL, k(t, st + 2.6, st + 2.9), lw=10)
    a = k(t, st + 3.6, st + 3.9)
    drop = min(1, max(0, (t - st - 4.0) / 1.2))
    meter(c, 540, 1060, 0.8 - 0.55 * drop, a)
    T(c, "CIBIL SCORE", 540, 1130, 46, WHITE, a, lw=8)


def o_future(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("LOW SCORE =", WHITE, 64, 0.1), ("BIKE LOAN: HARDER", RED, 60, 1.2),
                      ("CREDIT CARD: HARDER", RED, 60, 2.2), ("EVEN FOR SMALL AMOUNTS", YEL, 52, 3.4)], y0=480, gap=190)


def o_end(c, t, lt):
    K.end_card(c, "PAY LATER ONLY IF", "YOU'LL PAY ON TIME", GRN)
    st = sh.s(6)
    T(c, "Education only, not financial advice", 540, 1260, 36, GREY, k(t, st + 1.0, st + 1.3), lw=8)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'warm'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='smile', eyes=1.15, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_loan, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.25), (1.78, 960, 540), (1.85, 960, 520), o_late, 'studio'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_future, 'studio'),
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
