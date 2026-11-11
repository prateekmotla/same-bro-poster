"""RULES YOU DIDN'T KNOW #23: train alarm chain — only for a real emergency (engine: vshort.Short).
Facts: Railways Act 1989, Section 141 (bare act, AdvocateKhoj): interfering with the means of communication 'without
reasonable and sufficient cause' = imprisonment up to one year, or fine up to Rs 1,000, or both; proviso for the
alarm chain: not less than Rs 500 fine on first conviction, not less than 3 months' imprisonment on a second or later
conviction. Valid reasons (Curly Tales explainer, Sep 2026, citing Railways): serious medical emergency, a passenger
falling from the train, fire, a serious criminal / security incident; missing your station or boarding the wrong train
is NOT a valid reason. Rail helpline 139 / Rail Madad."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c140_chain"
CAPS = [
    "Pulling the train chain. Missed your station, so pull it? Or only in an emergency?",
    "Question: A: Missed station? That's fine. B: Only a real emergency. Comment!",
    "Answer: B. Railways Act, Section 141. Pull the chain without a proper reason: up to 1 year jail, or up to Rs 1,000 fine, or both.",
    "And even on a first conviction, a fine of at least Rs 500.",
    "Valid reasons? A medical emergency, someone fell off the train, a fire, or a safety threat.",
    "Missed station or wrong train is NOT a reason. Need help? Call 139. Ever seen someone pull the chain? Comment!",
]
HOOK = [("MISSED YOUR STATION?", WHITE), ("PULL THE CHAIN?", YEL), ("RULES YOU DIDN'T KNOW #23", GREY)]
SRC = "SRC: Railways Act 1989, Section 141"
sh = None


def train_bg(c, t):
    c.rectangle(0, 0, 1920, 1080); c.set_source_rgb(0.55, 0.62, 0.6); c.fill()
    for j in range(4):   # windows with passing scenery
        x = 140 + j * 460
        S.rrect(c, x, 160, 300, 260, 30); c.set_source_rgb(0.6, 0.8, 0.95); c.fill()
        c.save(); S.rrect(c, x, 160, 300, 260, 30); c.clip()
        for q in range(4):
            px = x + ((q * 160 - t * 500) % 460) - 80
            c.rectangle(px, 300, 20, 120); c.set_source_rgb(0.3, 0.55, 0.3); c.fill()
            c.arc(px + 10, 290, 50, 0, 2 * math.pi); c.fill()
        c.restore()
        S.rrect(c, x, 160, 300, 260, 30); c.set_source_rgb(0.35, 0.38, 0.4); c.set_line_width(12); c.stroke()
    c.rectangle(0, 700, 1920, 380); c.set_source_rgb(0.3, 0.42, 0.55); c.fill()   # berths
    for j in range(5):
        c.rectangle(j * 420, 680, 380, 40); c.set_source_rgb(0.25, 0.35, 0.48); c.fill()
    c.rectangle(0, 120, 1920, 14); c.set_source_rgb(0.75, 0.75, 0.7); c.fill()


def w_train(**kw):
    def f(c, t, lt):
        train_bg(c, t)
        d = dict(pose='stand', mouth='flat', look=(0.4, -0.4)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def chain(c, x, y, s, pull=0.0, a=1.0):
    c.save(); c.translate(x, y); c.scale(s, s)
    S.rrect(c, -110, -60, 220, 120, 20); c.set_source_rgba(0.85, 0.15, 0.15, a); c.fill()
    T(c, "ALARM", 0, 15, 40, WHITE, a, stroke=None)
    for j in range(7):
        cy = 75 + j * 34 + pull * 60 * j / 6
        c.save(); c.translate(0, cy); c.scale(0.6, 1); c.arc(0, 0, 18, 0, 2 * math.pi); c.restore()
        c.set_source_rgba(0.25, 0.25, 0.3, a); c.set_line_width(9); c.stroke()
    S.rrect(c, -40, 320 + pull * 60, 80, 50, 14); c.set_source_rgba(0.85, 0.15, 0.15, a); c.fill()
    c.restore()


def o_hook(c, t, lt):
    st = sh.s(1)
    p = 0.5 + 0.5 * math.sin((t - st) * 4) if t > st + 2.5 else 0
    chain(c, 820, 420, 1.0, p)
    if t > st + 3.3:
        K.stamp(c, t, st + 3.3, "STATION MISSED!", 360, 1180, YEL, 50, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "PULL THE CHAIN WHEN?", 540, 450, 60, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, sz, d) in enumerate((("A", "MISSED STATION: FINE", 48, 1.0), ("B", "REAL EMERGENCY ONLY", 48, 3.0))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 114, sz, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.2, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_law(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 300, 860, 130, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: EMERGENCY ONLY", 540, 385, 58, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 310, GRN, 50, 0.06)
    rows = [("RAILWAYS ACT, SEC 141", YEL, 54, 1.5), ("NO PROPER REASON =", WHITE, 54, 3.4),
            ("UP TO 1 YEAR JAIL", RED, 62, 4.6), ("OR UP TO Rs 1,000 FINE", RED, 56, 5.6), ("OR BOTH", WHITE, 62, 6.6)]
    for i, (txt, col, sz, d) in enumerate(rows):
        T(c, txt, 540, 560 + i * 140, sz, col, k(t, st + d, st + d + 0.3), lw=10)


def o_min(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("1st CONVICTION:", WHITE, 64, 0.1), ("MIN Rs 500 FINE", RED, 76, 1.0),
                      ("REPEAT:", WHITE, 56, 2.2), ("MIN 3 MONTHS JAIL", RED, 60, 2.6)], y0=480, gap=190)


def o_valid(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.88)
    T(c, "VALID REASONS", 540, 420, 70, GRN, k(t, st, st + 0.3), lw=10)
    for i, (txt, d) in enumerate((("MEDICAL EMERGENCY", 1.2), ("SOMEONE FELL OFF", 2.4), ("FIRE", 3.6), ("SAFETY THREAT", 4.3))):
        a = k(t, st + d, st + d + 0.3)
        y = 540 + i * 150
        S.rrect(c, 160, y, 760, 120, 30); c.set_source_rgba(0.08, 0.35, 0.16, 0.95 * a); c.fill()
        T(c, "OK", 250, y + 80, 44, YEL, a, stroke=None)
        T(c, txt, 590, y + 80, 50, WHITE, a, stroke=None)


def o_end(c, t, lt):
    K.end_card(c, "NEED HELP? CALL", "139", GRN)
    st = sh.s(6)
    T(c, "MISSED STATION = NOT A REASON", 540, 1260, 44, RED, k(t, st + 0.3, st + 0.6), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    sh.shots = [
        (0, s(2), w_train(mouth='o', eyes=1.2, arms=((14, -10), (100, -40))), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_law, 'studio'),
        (s(4), s(5), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_min, 'studio'),
        (s(5), s(6), sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_valid, 'studio'),
        (s(6), sh.dur + 1, w_train(mouth='flat', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
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
