"""RULES YOU DIDN'T KNOW #25: 112 = one number for police, fire and ambulance (engine: vshort.Short).
Facts: 112.gov.in (ERSS, MHA): 112 is the single emergency number; existing numbers 100 (police), 101 (fire) and
108 (ambulance) are to be integrated into 112; the '112 India' app has an SOS button that sends an alert with the
caller's location. Supreme Court, May 2026 (SaveLIFE Foundation petition; India TV 29 May 2026): all states/UTs
directed to make 112 fully operational within three months, integrating 100, 101, 102, 108 etc. Indian Express
(Jun 2026): only a few states/UTs had fully integrated all helplines into 112 -> where not merged yet, 108 still runs.
No claim that 112 already covers everything in every state."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c148_112"
CAPS = [
    "You see an accident on the road. Now which number? Police? Ambulance? Fire?",
    "Question: A: Remember all the different numbers. B: Just 112. Comment!",
    "Answer: B. 112 is India's single emergency number. Police, fire, ambulance, all on ONE call.",
    "In May 2026 the Supreme Court ordered every state: make 112 fully work within 3 months.",
    "100, 101, 108, all are being merged into 112. Where it's not done yet, 108 still works.",
    "And the 112 India app has an SOS button that sends your location. Is 112 saved in YOUR phone? Comment!",
]
HOOK = [("ACCIDENT ON THE ROAD", WHITE), ("WHICH NUMBER?", YEL), ("RULES YOU DIDN'T KNOW #25", GREY)]
SRC = "SRC: 112.gov.in + Supreme Court order (May 2026)"
sh = None


def w_street(**kw):
    def f(c, t, lt):
        V.street(c, t, 0.0, night=False)
        d = dict(pose='stand', mouth='flat', look=(0.6, 0)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def bubble(c, x, y, txt, col, a):
    c.arc(x, y, 95, 0, 6.283); c.set_source_rgba(*col, 0.95 * a); c.fill()
    T(c, txt, x, y + 22, 64, WHITE, a, stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    for i, (txt, col, d) in enumerate((("100", (0.15, 0.35, 0.8), 1.8), ("108", (0.1, 0.55, 0.3), 2.9), ("101", (0.85, 0.25, 0.15), 4.0))):
        a = k(t, st + d, st + d + 0.25)
        bubble(c, 230 + i * 310, 1200, txt, col, a)
        T(c, ("POLICE", "AMBULANCE", "FIRE")[i], 230 + i * 310, 1340, 34, WHITE, a, lw=8)
    if t > st + 4.6:
        K.stamp(c, t, st + 4.6, "WHICH ONE?!", 540, 1030, RED, 54, -0.04)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "EMERGENCY: CALL WHAT?", 540, 450, 62, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "REMEMBER ALL NUMBERS", 0.9), ("B", "JUST 112", 2.4))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 116, 50 if len(txt) > 14 else 64, WHITE, a, stroke=None)
    K.stamp(c, t, st + 3.2, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_one(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 300, 860, 130, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: JUST 112", 540, 385, 64, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 310, GRN, 50, 0.06)
    a = k(t, st + 1.0, st + 1.3)
    sc = 1 + 0.3 * (1 - U.eob(a))
    c.save(); c.translate(540, 660); c.scale(sc, sc); T(c, "112", 0, 0, 200, YEL, a, lw=14); c.restore()
    T(c, "INDIA'S SINGLE", 540, 800, 56, WHITE, k(t, st + 2.0, st + 2.3), lw=10)
    T(c, "EMERGENCY NUMBER", 540, 880, 56, WHITE, k(t, st + 2.4, st + 2.7), lw=10)
    for i, (txt, d) in enumerate((("POLICE", 3.6), ("FIRE", 4.0), ("AMBULANCE", 4.4))):
        T(c, txt, 220 + i * 320, 1010, 50, GRN, k(t, st + d, st + d + 0.25), lw=8)
    T(c, "ONE CALL", 540, 1120, 70, YEL, k(t, st + 5.4, st + 5.7), lw=10)


def o_court(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("MAY 2026", GREY, 56, 0.1), ("SUPREME COURT", YEL, 74, 1.4), ("TO EVERY STATE:", WHITE, 56, 2.8),
                      ("MAKE 112 FULLY WORK", GRN, 64, 3.8), ("IN 3 MONTHS", WHITE, 64, 5.0)], y0=420, gap=160)


def o_merge(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    for i, (txt, col, d) in enumerate((("100", (0.15, 0.35, 0.8), 0.2), ("101", (0.85, 0.25, 0.15), 0.9), ("108", (0.1, 0.55, 0.3), 1.6))):
        m = U.eob(k(t, st + 3.0, st + 4.0))
        x = 230 + i * 310 + (540 - (230 + i * 310)) * m
        y = 520 + 180 * m
        bubble(c, x, y, txt, col, k(t, st + d, st + d + 0.25) * (1 - 0.9 * m))
    a = k(t, st + 3.6, st + 4.0)
    c.arc(540, 700, 130 * (0.6 + 0.4 * U.eob(a)), 0, 6.283); c.set_source_rgba(0.9, 0.7, 0.1, a); c.fill()
    T(c, "112", 540, 735, 100, (0.1, 0.08, 0.05), a, stroke=None)
    T(c, "MERGING INTO 112", 540, 920, 56, WHITE, k(t, st + 4.0, st + 4.3), lw=10)
    T(c, "NOT MERGED YET?", 540, 1060, 50, GREY, k(t, st + 5.5, st + 5.8), lw=8)
    T(c, "108 STILL WORKS", 540, 1140, 62, GRN, k(t, st + 6.6, st + 6.9), lw=10)


def sos_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.96, 0.96, 0.98); c.fill()
    c.rectangle(0, 0, w, 120); c.set_source_rgb(0.12, 0.2, 0.45); c.fill()
    T(c, "112 INDIA", w / 2, 85, 42, WHITE, stroke=None)
    p = 0.5 + 0.5 * __import__('math').sin(tt * 5)
    c.arc(w / 2, 320, 120 + 12 * p, 0, 6.283); c.set_source_rgba(0.9, 0.15, 0.15, 0.3); c.fill()
    c.arc(w / 2, 320, 105, 0, 6.283); c.set_source_rgb(0.85, 0.12, 0.12); c.fill()
    T(c, "SOS", w / 2, 345, 70, WHITE, stroke=None)
    T(c, "Sends your location", w / 2, 500, 28, (0.2, 0.2, 0.25), stroke=None, bold=False)


def o_end(c, t, lt):
    st = sh.s(6)
    U.phone_frame(c, 690, 720, 340, 600, sos_screen, t - st, tilt=4)
    if t > st + 2.5:
        K.stamp(c, t, st + 2.5, "SOS = LOCATION SENT", 360, 1150, GRN, 44, -0.04)
    if t > st + 4.4:
        K.stamp(c, t, st + 4.4, "112 SAVED? COMMENT", 560, 1300, YEL, 50, 0.03)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_street(mouth='o', eyes=1.2, look=(-0.6, 0.1)), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_one, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.15), (1.78, 960, 540), (1.85, 960, 520), o_court, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_merge, 'studio'),
        (s(6), sh.dur + 1, w_street(mouth='smile', **ph), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 4.8] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
