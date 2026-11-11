"""RULES YOU DIDN'T KNOW #20: bank locker robbed — bank pays up to 100x the annual rent (engine: vshort.Short).
Facts: RBI revised instructions on safe deposit lockers (circular 18 Aug 2021, in force from 1 Jan 2022; RBI
notification Id 12146): for fire, theft, burglary, dacoity, building collapse, or fraud by the bank's employees, the
bank's liability = up to 100 times the prevailing ANNUAL rent of the locker. Banks are NOT liable for loss from natural
calamities / acts of God (earthquake, flood, lightning...) or the customer's own negligence, but must protect the
premises. The locker agreement is signed in duplicate and a copy is given to the hirer. Example on screen is plain maths:
Rs 4,000/yr x 100 = Rs 4,00,000 (the cap; actual payout up to that amount)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

assert 4000 * 100 == 400000
D = "/home/claude/sid/shorts/c128_locker"
CAPS = [
    "The gold in your bank locker got STOLEN. The bank says: not our responsibility. Really?",
    "Question: A: The bank pays nothing. B: The bank must pay up to 100 times the locker rent. Comment!",
    "Answer: B. RBI locker rules. Fire, theft, dacoity, building collapse, or fraud by bank staff: the bank is liable, up to 100x the yearly rent.",
    "So if the rent is Rs 4,000 a year, up to Rs 4 lakh.",
    "But for natural disasters like an earthquake or flood, the bank is NOT liable.",
    "And you must get a copy of your locker agreement. Checked yours? Comment!",
]
HOOK = [("LOCKER ROBBED?", WHITE), ("BANK PAYS 0 or 100x?", YEL), ("RULES YOU DIDN'T KNOW #20", GREY)]
SRC = "SRC: RBI safe deposit locker rules (2021, from Jan 2022)"
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


def locker(c, x, y, s, open_=0.0, empty=False, a=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    S.rrect(c, -170, -170, 340, 340, 20); c.set_source_rgba(0.55, 0.57, 0.62, a); c.fill()
    S.rrect(c, -150, -150, 300, 300, 14); c.set_source_rgba(0.15, 0.15, 0.18, a); c.fill()
    if not empty:
        for j in range(3):
            S.rrect(c, -110 + j * 75, 60, 60, 40, 6); c.set_source_rgba(1, 0.8, 0.2, a); c.fill()
    else:
        T(c, "EMPTY", 0, 20, 54, RED, a, stroke=None)
    w = 300 * (1 - 0.8 * open_)
    S.rrect(c, -150, -150, w, 300, 14); c.set_source_rgba(0.7, 0.72, 0.78, a); c.fill()
    c.arc(-150 + w * 0.7, 0, 34, 0, 6.283); c.set_source_rgba(0.35, 0.37, 0.42, a); c.fill()
    T(c, "117", -150 + w * 0.5, -90, 40, (0.2, 0.2, 0.25), a, stroke=None)
    c.restore()


def o_hook(c, t, lt):
    st = sh.s(1)
    locker(c, 230, 1000, 0.75, open_=min(1, max(0, (t - 0.6) / 0.6)), empty=True)
    if t > 2.8:
        U.phone_frame(c, 660, 760, 340, 560, K.sms_screen("BANK", [("Not our", WHITE), ("responsibility", RED),
                                                                    ("Sorry.", WHITE)]), t - 2.8, tilt=4)
    if t > st + 4.4:
        K.stamp(c, t, st + 4.4, "REALLY?!", 330, 1260, RED, 56, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "GOLD STOLEN FROM LOCKER", 540, 430, 54, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "WHAT DOES THE BANK PAY?", 540, 510, 52, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, sz, d) in enumerate((("A", "NOTHING", 64, 1.2), ("B", "UP TO 100x THE RENT", 50, 3.0))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 610, y + 114, sz, WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.4, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: UP TO 100x RENT", 540, 476, 62, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("RBI LOCKER RULES", YEL, 56, 0.9), ("FIRE, THEFT, DACOITY", WHITE, 56, 2.0),
                      ("BUILDING COLLAPSE", WHITE, 56, 4.0), ("FRAUD BY BANK STAFF", WHITE, 56, 5.0),
                      ("BANK LIABLE", GRN, 64, 6.4), ("UP TO 100x YEARLY RENT", GRN, 56, 7.6)], y0=650, gap=110)


def o_math(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("RENT: ₹4,000 / YEAR", WHITE, 64, 0.1), ("x 100", YEL, 90, 1.2),
                      ("UP TO ₹4 LAKH", GRN, 90, 2.0)], y0=560, gap=200)


def o_not(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("NOT LIABLE FOR", RED, 70, 0.1), ("EARTHQUAKE", WHITE, 66, 1.0), ("FLOOD", WHITE, 66, 1.6),
                      ("NATURAL DISASTERS", YEL, 62, 2.4)], y0=500, gap=175)


def o_end(c, t, lt):
    K.end_card(c, "GET YOUR COPY OF", "THE LOCKER AGREEMENT", GRN)
    st = sh.s(6)
    T(c, "CHECKED YOURS?", 540, 1260, 54, YEL, k(t, st + 2.0, st + 2.3), lw=10)


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
        (s(4), s(5), sw(mouth='o', eyes=1.25), (1.78, 960, 540), (1.85, 960, 520), o_math, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_not, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.5, 5.5] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
