"""THEY'RE TRICKING YOU #10: 'charge only to 80%' — myth or truth? (engine: vshort.Short).
Facts: Apple 'About charging and maintaining your iPad/iPhone battery' (support.apple.com/118418) + Apple 'Why
lithium-ion': lithium-ion batteries age faster when kept at high charge for long and when hot; Optimized Battery Charging
delays charging past 80%; iPhone 15 and later have an '80% Limit' charging option (Tom's Guide / Cult of Mac). Samsung
Galaxy 'Battery protection' (One UI) can stop charging at 80% (Samsung support / Chargie). Heat is the biggest enemy
(Apple: avoid extreme ambient temperatures; gaming while charging heats the phone). Occasional 100% is fine.
Fair to brands: setting names only, no logos."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c135_battery"
CAPS = [
    "Phone charged to 100% every night. People say: stop at 80, the battery lasts longer. Myth or truth?",
    "Question: A: Myth, charge to 100. B: True, stopping at 80 is better for the battery. Comment!",
    "Answer: B. A lithium battery that sits at full charge for long, and gets HOT, wears out faster.",
    "That's why iPhone has an 80% limit option, and Samsung has Battery protection.",
    "But don't panic. 100% once in a while is fine. The real enemy is HEAT, like heavy gaming while charging.",
    "What's YOUR battery health? Comment!",
]
HOOK = [("CHARGE ONLY TO 80%?", WHITE), ("MYTH or TRUTH?", YEL), ("THEY'RE TRICKING YOU #10", GREY)]
SRC = "SRC: Apple battery support page; Samsung Battery protection"
sh = None


def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "night")
        d = dict(pose='stand', mouth='flat', look=(0.6, 0)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def battery(c, x, y, s, frac, col, label=None, a=1.0, bolt=False):
    c.save(); c.translate(x, y); c.scale(s, s)
    S.rrect(c, -150, -80, 300, 160, 22); c.set_source_rgba(1, 1, 1, a); c.set_line_width(12); c.stroke()
    S.rrect(c, 152, -30, 26, 60, 8); c.set_source_rgba(1, 1, 1, a); c.fill()
    S.rrect(c, -134, -64, 268 * max(0.04, frac), 128, 12); c.set_source_rgba(*col, a); c.fill()
    if bolt:
        c.move_to(15, -55); c.line_to(-30, 8); c.line_to(0, 8); c.line_to(-15, 55); c.line_to(35, -10); c.line_to(5, -10)
        c.close_path(); c.set_source_rgba(1, 1, 1, a); c.fill()
    c.restore()
    if label:
        T(c, label, x, y + 150 * s, 64 * s, WHITE, a, lw=8)


def toggle_screen(rows):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
        T(c, "Battery", 40, 100, 44, (0.1, 0.1, 0.15), stroke=None, anchor="left")
        for i, (lab, on) in enumerate(rows):
            y = 210 + i * 120
            S.rrect(c, 24, y - 50, w - 48, 100, 18); c.set_source_rgb(1, 1, 1); c.fill()
            T(c, lab, 50, y + 12, 30, (0.1, 0.1, 0.15), stroke=None, anchor="left", bold=False)
            S.rrect(c, w - 130, y - 22, 84, 46, 23); c.set_source_rgb(*(GRN if on else (0.75, 0.75, 0.78))); c.fill()
            c.arc(w - 69 if on else w - 107, y + 1, 18, 0, 6.283); c.set_source_rgb(1, 1, 1); c.fill()
    return f


def o_hook(c, t, lt):
    st = sh.s(1)
    fr = min(1.0, 0.55 + 0.45 * k(t, 0.3, 2.5))
    battery(c, 280, 980, 0.9, fr, GRN, f"{int(fr * 100)}%", bolt=True)
    if t > st + 3.2:
        S.rrect(c, 120, 1170, 330, 80, 30); c.set_source_rgba(1, 1, 1, 0.95); c.fill()
        T(c, "'STOP AT 80!'", 285, 1224, 38, (0.1, 0.1, 0.15), stroke=None)
    if t > st + 5.6:
        K.stamp(c, t, st + 5.6, "MYTH or TRUTH?", 330, 1360, YEL, 48, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "CHARGE ONLY TO 80%?", 540, 450, 60, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, sz, d) in enumerate((("A", "MYTH: GO TO 100", 54, 0.6), ("B", "TRUE: 80 IS BETTER", 52, 2.6))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 114, sz, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.8, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: MOSTLY TRUE", 540, 476, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("LITHIUM BATTERY WEARS FASTER", YEL, 50, 0.9)], y0=640)
    battery(c, 330, 850, 0.7, 1.0, (1, 0.6, 0.2), "FULL FOR HOURS", a=k(t, st + 1.8, st + 2.1))
    if t > st + 3.4:
        a = k(t, st + 3.4, st + 3.7)
        T(c, "+", 540, 880, 90, WHITE, a, lw=8)
        c.save(); c.translate(760, 850)
        for j in range(3):
            c.move_to(-60 + j * 60, 70)
            c.curve_to(-90 + j * 60, 20, -30 + j * 60, -20, -60 + j * 60, -70)
        c.set_source_rgba(*RED, a); c.set_line_width(16); c.stroke(); c.restore()
        T(c, "HEAT", 760, 990, 50, RED, a, lw=8)
    if t > st + 4.6:
        K.stamp(c, t, st + 4.6, "= FASTER WEAR", 540, 1190, RED, 52, -0.03)


def o_settings(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.85)
    U.phone_frame(c, 320, 820, 440, 520, toggle_screen([("Limit to 80%", t > st + 1.3), ("Optimised", True)]),
                  t - st, tilt=-3)
    T(c, "iPHONE: 80% LIMIT", 540, 430, 56, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    T(c, "SAMSUNG:", 540, 540, 56, WHITE, k(t, st + 2.4, st + 2.7), lw=8)
    T(c, "BATTERY PROTECTION", 540, 620, 56, GRN, k(t, st + 2.8, st + 3.1), lw=8)


def o_heat(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("DON'T PANIC", WHITE, 72, 0.1), ("100% SOMETIMES = OK", GRN, 62, 1.4), ("REAL ENEMY: HEAT", RED, 72, 3.2),
                      ("GAMING WHILE CHARGING", YEL, 56, 4.4)], y0=500, gap=180)


def o_end(c, t, lt):
    st = sh.s(6)
    K.end_card(c, "SETTINGS > BATTERY", "CHECK YOUR HEALTH %", GRN)
    T(c, "COMMENT YOURS", 540, 1260, 54, YEL, k(t, st + 1.0, st + 1.3), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='flat', **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='flat', **ph), (1.78, 960, 540), (1.85, 960, 520), o_settings, 'studio'),
        (s(5), s(6), sw(mouth='o', eyes=1.2, arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_heat, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', **ph), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 2.5, 6.0] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
