"""RULES YOU DIDN'T KNOW #21: phone stolen? Block it all over India on Sanchar Saathi (CEIR) (engine: vshort.Short).
SWAP: row 132's 'hotel must give free drinking water' rests on the Sarais Act 1867, whose application to modern hotels is
disputed (Free Press Journal, Shangri-La washroom row) -> not stated as a rule; the fallback ('no return' defect rights)
was already used by 116. Fresh RULES topic instead.
Facts: DoT / C-DOT Sanchar Saathi portal (sancharsaathi.gov.in, CEIR module; Business Standard 22 May 2023, Business
Insider May 2023, CEIR user manual): file a police complaint first (many states allow it online), then 'Block your lost /
stolen mobile handset' with the IMEI and a copy of the complaint; the IMEI is blocked on all Indian telecom networks so
the phone can't be used with any SIM; once recovered, unblock it on the same portal. *#06# shows the IMEI."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c132_lostphone"
CAPS = [
    "Your phone got STOLEN. Everyone says: it's gone, forget it. But most people don't know this.",
    "Question: A: Nothing can be done. B: You can block the phone all over India on a govt portal. Comment!",
    "Answer: B. First file a police complaint, it can be done online too. Then on the Sanchar Saathi portal: Block lost phone.",
    "Enter the IMEI number and the complaint copy. The phone is blocked on EVERY network. Any SIM: it won't work.",
    "And if you get the phone back, unblock it on the same portal.",
    "Do you know your phone's IMEI? Dial *#06# and note it down. Comment!",
]
HOOK = [("PHONE STOLEN?", WHITE), ("GONE FOREVER?", YEL), ("RULES YOU DIDN'T KNOW #21", GREY)]
SRC = "SRC: DoT Sanchar Saathi (CEIR) portal"
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


def handset(c, x, y, s, a=1.0, blocked=False):
    c.save(); c.translate(x, y); c.scale(s, s)
    S.rrect(c, -110, -200, 220, 400, 34); c.set_source_rgba(0.12, 0.12, 0.15, a); c.fill()
    S.rrect(c, -96, -180, 192, 360, 24); c.set_source_rgba(*((0.35, 0.05, 0.08) if blocked else (0.2, 0.45, 0.85)), a); c.fill()
    if blocked:
        T(c, "BLOCKED", 0, 10, 40, WHITE, a, stroke=None)
        T(c, "NO NETWORK", 0, 70, 26, (1, 0.7, 0.7), a, stroke=None)
    c.restore()


def portal_screen(step):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
        c.rectangle(0, 0, w, 120); c.set_source_rgb(0.1, 0.3, 0.6); c.fill()
        T(c, "SANCHAR SAATHI", w / 2, 80, 34, WHITE, stroke=None)
        T(c, "Block lost / stolen", 40, 190, 30, (0.1, 0.1, 0.15), stroke=None, anchor="left")
        T(c, "mobile", 40, 230, 30, (0.1, 0.1, 0.15), stroke=None, anchor="left")
        for i, (lab, val) in enumerate((("IMEI", "35xxxxxxxxxxxx1"), ("POLICE COMPLAINT", "copy.pdf"), ("MOBILE NO.", "98xxxxxx12"))):
            y = 300 + i * 110
            T(c, lab, 40, y, 24, GREY, stroke=None, anchor="left")
            S.rrect(c, 30, y + 14, w - 60, 56, 10); c.set_source_rgb(1, 1, 1); c.fill_preserve()
            c.set_source_rgb(0.75, 0.75, 0.8); c.set_line_width(2); c.stroke()
            if step > i:
                T(c, val, 50, y + 54, 28, (0.1, 0.1, 0.15), stroke=None, anchor="left", bold=False)
        S.rrect(c, 40, h - 110, w - 80, 80, 40); c.set_source_rgb(*(RED if step >= 3 else (0.6, 0.6, 0.65))); c.fill()
        T(c, "BLOCK", w / 2, h - 57, 36, WHITE, stroke=None)
    return f


def o_hook(c, t, lt):
    st = sh.s(1)
    handset(c, 270, 1010, 0.9, a=max(0, 1 - max(0, t - 2.2) / 0.6))
    if t > 0.6:
        K.stamp(c, t, 0.6, "STOLEN", 270, 1010, RED, 56, -0.1)
    if t > st + 2.4:
        S.rrect(c, 520, 860, 470, 90, 40); c.set_source_rgba(1, 1, 1, 0.95); c.fill()
        T(c, "'FORGET IT, BRO'", 755, 920, 40, (0.1, 0.1, 0.15), stroke=None)
    if t > st + 4.2:
        K.stamp(c, t, st + 4.2, "OR IS IT?", 760, 1180, YEL, 52, 0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "PHONE STOLEN", 540, 430, 60, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "WHAT CAN YOU DO?", 540, 510, 52, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, sz, d) in enumerate((("A", "NOTHING", 64, 0.8), ("B", "BLOCK IT ALL OVER INDIA", 44, 2.4))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 112, sz, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.4, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: BLOCK IT", 540, 476, 70, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("STEP 1", YEL, 50, 0.9), ("POLICE COMPLAINT", WHITE, 60, 1.2), ("(ONLINE TOO)", GREY, 44, 2.6),
                      ("STEP 2", YEL, 50, 3.8), ("SANCHAR SAATHI PORTAL", WHITE, 56, 4.2),
                      ("'BLOCK LOST MOBILE'", GRN, 56, 5.8)], y0=640, gap=105)


def o_form(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.6)
    step = min(3, int((t - st) / 1.0))
    U.phone_frame(c, 250, 800, 360, 620, portal_screen(step), t - st, tilt=-3)
    if t > st + 3.6:
        handset(c, 850, 1000, 0.7, blocked=True)
        T(c, "EVERY NETWORK", 830, 820, 44, WHITE, k(t, st + 3.8, st + 4.0), lw=8)
        K.stamp(c, t, st + 4.8, "ANY SIM: DEAD", 830, 1260, RED, 44, 0.04)


def o_unblock(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("GOT IT BACK?", WHITE, 72, 0.1), ("UNBLOCK", GRN, 100, 1.0), ("ON THE SAME PORTAL", YEL, 56, 1.6)],
           y0=560, gap=180)


def o_end(c, t, lt):
    st = sh.s(6)
    K.end_card(c, "DIAL  *#06#", "NOTE YOUR IMEI NOW", GRN)
    T(c, "KNOW YOURS?", 540, 1260, 54, YEL, k(t, st + 3.0, st + 3.3), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', eyes=1.2), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk', **ph), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='flat', **ph), (1.78, 960, 540), (1.85, 960, 520), o_form, 'studio'),
        (s(5), s(6), sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_unblock, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', **ph), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.5, 5.0] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
