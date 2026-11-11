"""RULES YOU DIDN'T KNOW #22: LPG cylinder accident — oil companies' insurance covers registered customers
(engine: vshort.Short).
Facts: Lok Sabha Unstarred Q 2730 (16 Mar 2023, MoPNG reply): OMCs take a comprehensive insurance policy covering all
LPG consumers registered with OMCs: personal accident cover Rs 6 lakh per person (death), medical expenses Rs 30 lakh per
event with max Rs 2 lakh per person, property damage max Rs 2 lakh per event at the customer's registered premises.
Same figures in the 2024-25 OMC policy schedule (PMUY site, immediate relief up to Rs 25,000 per person). Claim: inform
the distributor in writing immediately; the distributor informs the oil company + insurer and helps with formalities
(Moneylife / Citizen's Charter). ROW EDIT: the viral 'Rs 50 lakh' figure is an older per-event liability limit, not what
a family gets, so it is NOT used; the short uses the per-person figures. Policy terms can change year to year."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c136_lpg"
CAPS = [
    "An accident with the gas cylinder. Damage at home, a hospital bill. All from your own pocket?",
    "Question: A: Yes, you pay for everything. B: The oil companies' insurance covers it. Comment!",
    "Answer: B. Every registered LPG customer is covered under the oil companies' insurance policy.",
    "Death: up to ₹6 lakh per person. Treatment: up to ₹2 lakh per person. Damage to the home: up to ₹2 lakh.",
    "To claim, inform your gas distributor in WRITING right away. He takes it to the company and the insurer.",
    "Did you know this? Send it to your family, and comment!",
]
HOOK = [("GAS CYLINDER ACCIDENT", WHITE), ("WHO PAYS?", YEL), ("RULES YOU DIDN'T KNOW #22", GREY)]
SRC = "SRC: MoPNG reply, Lok Sabha (Mar 2023); OMC LPG policy"
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


def cylinder(c, x, y, s, a=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    S.rrect(c, -110, -170, 220, 360, 90); c.set_source_rgba(0.82, 0.15, 0.15, a); c.fill()
    S.rrect(c, -60, -230, 120, 70, 20); c.set_source_rgba(0.75, 0.75, 0.78, a); c.fill()
    c.rectangle(-110, -40, 220, 22); c.set_source_rgba(0.65, 0.1, 0.1, a); c.fill()
    T(c, "LPG", 0, 70, 56, WHITE, a, stroke=None)
    c.restore()


def o_hook(c, t, lt):
    st = sh.s(1)
    cylinder(c, 260, 1000, 0.85)
    if t > 0.5:
        K.stamp(c, t, 0.5, "ACCIDENT!", 260, 1240, RED, 50, -0.06)
    if t > st + 2.4:
        U.phone_frame(c, 560, 780, 380, 520, K.bill_screen("HOSPITAL", [("Treatment", "₹₹₹"), ("Room", "₹₹"),
                                                                       ("Home repair", "₹₹₹")], "???", btn="PAY"), t - 2.4, tilt=4)
    if t > st + 4.4:
        K.stamp(c, t, st + 4.4, "ALL FROM YOUR POCKET?", 560, 1400, YEL, 42, 0.03)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "LPG CYLINDER ACCIDENT", 540, 430, 56, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "WHO PAYS?", 540, 510, 56, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, sz, d) in enumerate((("A", "YOU PAY EVERYTHING", 50, 0.6), ("B", "OIL COMPANIES' INSURANCE", 42, 2.4))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 112, sz, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.6, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: INSURANCE COVERS IT", 540, 476, 54, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("EVERY REGISTERED", WHITE, 60, 1.0), ("LPG CUSTOMER", WHITE, 60, 1.4),
                      ("IS COVERED", GRN, 72, 2.4), ("BY OIL COMPANIES' POLICY", YEL, 50, 3.4)], y0=680, gap=120)


def o_money(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "COVER (PER POLICY)", 540, 430, 50, YEL, k(t, st, st + 0.2), lw=8)
    for i, (lab, val, d) in enumerate((("DEATH", "₹6 LAKH / PERSON", 0.2), ("TREATMENT", "₹2 LAKH / PERSON", 2.6),
                                       ("HOME DAMAGE", "₹2 LAKH", 4.6))):
        a = k(t, st + d, st + d + 0.3)
        y = 520 + i * 200
        S.rrect(c, 110, y, 860, 170, 36); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        T(c, lab, 540, y + 62, 40, GREY, a, stroke=None)
        T(c, "UP TO " + val, 540, y + 132, 54, GRN, a, stroke=None)


def o_claim(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("TO CLAIM", YEL, 64, 0.1), ("TELL YOUR DISTRIBUTOR", WHITE, 56, 0.9), ("IN WRITING", RED, 80, 2.2),
                      ("RIGHT AWAY", WHITE, 64, 3.0), ("> COMPANY > INSURER", GRN, 52, 4.4)], y0=460, gap=165)


def o_end(c, t, lt):
    st = sh.s(6)
    K.end_card(c, "SEND THIS TO", "YOUR FAMILY", GRN)
    T(c, "DID YOU KNOW?", 540, 1260, 54, YEL, k(t, st + 0.3, st + 0.6), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'warm'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', eyes=1.2), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_money, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_claim, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', **ph), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 2.0, 5.0] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
