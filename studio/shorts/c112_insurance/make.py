"""RULES YOU DIDN'T KNOW #16: IRCTC 45-paise travel insurance (engine: vshort.Short).
Fact: IRCTC optional travel insurance for online e-tickets (confirmed/RAC): premium 45 paise per passenger, cover up
to Rs 10 lakh for death or permanent total disability in a train accident (plus partial disability and hospital
expenses per policy); passenger must opt in while booking and should fill nominee details (Business Today 8 Aug 2025,
Free Press Journal; IRCTC booking page)."""

import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c112_insurance"
CAPS = [
    "When you book a train ticket, a small insurance box shows up. Most people skip it.",
    "Question: what does that box cost? A: ₹100. B: just 45 PAISE. Comment!",
    "B. On IRCTC, with an online ticket, travel insurance costs just 45 paise.",
    "Death or full disability in a train accident: cover up to ₹10 LAKH. It's optional, you have to tick it yourself.",
    "And always fill the nominee, or the claim gets messy. It doesn't even cost a rupee, and you still skip it?",
    "Next booking, tick that box.",
]
HOOK = [("THE BOX YOU ALWAYS SKIP", WHITE), ("WORTH ₹10 LAKH", YEL), ("RULES YOU DIDN'T KNOW #16", GREY)]
SRC = "SRC: IRCTC travel insurance (Business Today, Aug 2025)"
Q1, Q2 = "THAT INSURANCE BOX", "COSTS HOW MUCH?"
OPT_A, OPT_B, OPT_T = "₹100", "JUST 45 PAISE", (2.3, 3.6, 5.2)
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



def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, Q1, 540, 430, 62, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, Q2, 540, 515, 56, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", OPT_A, OPT_T[0]), ("B", OPT_B, OPT_T[1]))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 114, 50, WHITE, a, stroke=None)
    K.stamp(c, t, st + OPT_T[2], "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def booking(chk):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.96, 0.96, 0.98); c.fill()
        c.rectangle(0, 0, w, 110); c.set_source_rgb(0.12, 0.25, 0.55); c.fill()
        T(c, "BOOK TICKET", w / 2, 72, 34, WHITE, stroke=None)
        T(c, "Passenger 1", 30, 190, 34, (0.1, 0.1, 0.15), stroke=None, anchor="left")
        T(c, "Berth: Lower", 30, 250, 30, GREY, stroke=None, anchor="left")
        S.rrect(c, 20, 310, w - 40, 150, 18); c.set_source_rgb(1, 0.95, 0.8); c.fill()
        S.rrect(c, 40, 345, 50, 50, 8); c.set_source_rgb(0.2, 0.2, 0.25); c.set_line_width(4); c.stroke()
        if chk(tt):
            c.move_to(50, 370); c.line_to(62, 385); c.line_to(84, 352); c.set_source_rgb(0.1, 0.6, 0.25); c.set_line_width(7); c.stroke()
        T(c, "Travel insurance", 110, 368, 28, (0.1, 0.1, 0.15), stroke=None, anchor="left")
        T(c, "(optional)", 110, 410, 24, GREY, stroke=None, anchor="left")
        S.rrect(c, 40, h - 120, w - 80, 80, 20); c.set_source_rgb(0.95, 0.5, 0.15); c.fill()
        T(c, "PAY NOW", w / 2, h - 68, 34, WHITE, stroke=None)
    return f


def o_hook(c, t, lt):
    U.phone_frame(c, 660, 700, 360, 620, booking(lambda tt: False), t, tilt=4)
    if t > 2.2:
        K.stamp(c, t, 2.2, "SKIP?", 300, 1220, YEL, 70, -0.05)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: 45 PAISE", 540, 478, 72, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 390, GRN, 54, 0.06)
    K.rows(c, t, st, [("IRCTC online e-ticket", WHITE, 52, 1.6), ("+ TRAVEL INSURANCE", YEL, 68, 3.0)], y0=720, gap=120)


def o_four(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("TRAIN ACCIDENT:", WHITE, 64, 0.2), ("DEATH / FULL DISABILITY", WHITE, 52, 0.8),
                      ("UP TO ₹10 LAKH", GRN, 100, 2.4), ("OPTIONAL: TICK IT YOURSELF", YEL, 46, 4.0)], y0=460, gap=170)


def o_five(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("FILL THE", WHITE, 70, 0.2), ("NOMINEE", YEL, 110, 0.5), ("OR THE CLAIM GETS MESSY", WHITE, 46, 1.4),
                      ("LESS THAN ₹1. STILL SKIP?", RED, 52, 2.8)], y0=480, gap=170)


def o_end(c, t, lt):
    U.phone_frame(c, 360, 260, 360, 620, booking(lambda tt: tt > 0.8), t - sh.s(6), tilt=0)
    K.end_card(c, "45 PAISE INSURANCE", "TICK THE BOX", GRN)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'warm'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='flat', phone=1, arms=((14, -10), (40, 110))), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_four, 'studio'),
        (s(5), s(6), sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_five, 'money'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
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
