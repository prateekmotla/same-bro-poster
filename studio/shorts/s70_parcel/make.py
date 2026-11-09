"""SCAM OF THE WEEK #2: fake 'your parcel is held by customs' call (engine: vshort.Short, real-time voice lines)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s70_parcel"
CAPS = [
    "A call: 'Your parcel is held at CUSTOMS. Drugs found inside. Pay to clear the case.'",
    "Then the call is 'transferred' to fake POLICE. Fake ID, fake FIR, and so much fear you can't think.",
    "What do you do? A: pay up. B: cut the call. Comment!",
    "B is right. Customs says it clearly: its officers NEVER ask for duty on phone or SMS. Into a personal account? NEVER.",
    "A real Customs notice has a DIN number you can verify on the CBIC website.",
    "Got this call? Cut it. Call 1930 or report at cybercrime.gov.in",
    "Send this to your family, so if they get this call, they pick B too.",
]
HOOK = [("'PARCEL HELD'", WHITE), ("PAY OR CUT?", RED), ("SCAM OF THE WEEK #2", GREY)]
SRC = "SRC: CBIC / Indian Customs advisory (PIB, 16 Jun 2024)"
sh = None
BLUE = (0.26, 0.52, 0.96)


def call_screen(name, sub, lines, n):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.06, 0.08, 0.12); c.fill()
        T(c, name, w / 2, 120, 40, WHITE, stroke=None)
        T(c, sub, w / 2, 170, 26, GREY, stroke=None, bold=False)
        T(c, f"00:{int(tt) % 60:02d}", w / 2, 215, 26, GRN, stroke=None, bold=False)
        for i, (ln, col) in enumerate(lines[:n]):
            S.rrect(c, 24, 260 + i * 92, w - 48, 74, 20); c.set_source_rgb(0.18, 0.2, 0.26); c.fill()
            T(c, ln, w / 2, 308 + i * 92, 30, col, stroke=None)
        c.arc(w / 2, h - 80, 44, 0, 6.283); c.set_source_rgb(0.9, 0.2, 0.2); c.fill()
        T(c, "END", w / 2, h - 70, 24, WHITE, stroke=None)
    return f


def rw(mode='day', **kw):
    def f(c, t, lt):
        V.room(c, t, mode, fan=False)
        d = dict(pose='stand', mouth='flat')
        d.update(kw)
        K.sid(c, t, 1000, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def o_hook(c, t, lt):
    st = sh.s(1)
    n = 1 + int(k(t, st + 1.0, st + 4.6) * 2.99)
    U.phone_frame(c, 290, 560, 500, 640, call_screen("+91 8X4X XXXX07", "'Courier / Customs'",
                                                     [("Parcel SEIZED", RED), ("Drugs found inside", WHITE),
                                                      ("Pay to clear case", YEL)], n), t - st, tilt=-2 + 3 * lt)
    K.stamp(c, t, st + 2.8, "A: PAY   or   B: CUT?", 540, 1330, RED, 50, -0.04)


def o_police(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.86)
    T(c, "TRANSFERRED TO 'POLICE'", 540, 480, 58, WHITE, k(t, st + 0.1, st + 0.4), lw=10)
    a = k(t, st + 1.2, st + 1.5)
    S.rrect(c, 230, 560, 620, 330, 26); c.set_source_rgba(0.85, 0.88, 0.95, a); c.fill()
    c.rectangle(270, 610, 170, 210); c.set_source_rgba(0.55, 0.6, 0.7, a); c.fill()
    T(c, "POLICE ID", 640, 660, 44, (0.1, 0.15, 0.35), a, stroke=None)
    T(c, "Insp. XXXXX", 640, 730, 34, (0.2, 0.2, 0.25), a, stroke=None, bold=False)
    T(c, "FIR No. 2026/XXX", 640, 790, 32, (0.2, 0.2, 0.25), a, stroke=None, bold=False)
    K.stamp(c, t, st + 2.6, "FAKE", 760, 700, RED, 80, -0.12)
    K.rows(c, t, st, [("FEAR = NO TIME TO THINK", YEL, 56, 4.8)], y0=1030)


def o_choice(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "WHAT DO YOU DO?", 540, 470, 72, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt) in enumerate((("A", "PAY TO 'CLEAR' IT"), ("B", "CUT THE CALL"))):
        a = k(t, st + 0.5 + i * 0.9, st + 0.8 + i * 0.9)
        y = 580 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 590, y + 112, 52, WHITE, a, stroke=None)
    K.stamp(c, t, st + 2.6, "COMMENT A or B", 540, 1120, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    S.rrect(c, 110, 430, 860, 190, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: CUT THE CALL", 540, 545, 64, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 450, GRN, 54, 0.06)
    K.rows(c, t, st, [("CUSTOMS NEVER ASKS", WHITE, 58, 2.0), ("FOR DUTY ON CALL / SMS", YEL, 52, 2.8),
                      ("PERSONAL ACCOUNT?", WHITE, 58, 5.2), ("NEVER.", RED, 80, 6.2)], y0=760, gap=110)


def o_din(c, t, lt):
    st = sh.s(5)
    K.panel(c, 820, 470)
    T(c, "REAL NOTICE = DIN", 540, 920, 62, YEL, stroke=None)
    K.rows(c, t, st, [("Document Identification No.", WHITE, 42, 0.6), ("Verify it on the", WHITE, 42, 2.4),
                      ("CBIC website", GRN, 56, 2.9)], y0=1020, gap=80)


def o_help(c, t, lt):
    st = sh.s(6)
    K.full(c, t, st, [("GOT THIS CALL?", WHITE, 70, 0.1), ("CUT. CALL 1930", GRN, 104, 1.2), ("cybercrime.gov.in", YEL, 64, 3.4)],
           y0=560, gap=190)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO FAMILY.", "SO THEY PICK B TOO.", YEL)
    st = sh.s(7)
    T(c, "A or B? COMMENT", 540, 1260, 64, YEL, k(t, st + 1.5, st + 1.8), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (60, 120)))
    sh.shots = [
        (0, s(2), rw('day', mouth='o', eyes=1.3, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), rw('night', mouth='frown', sweat=1, **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_police, 'red'),
        (s(3), s(4), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(4), s(5), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(5), s(6), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_din, 'studio'),
        (s(6), s(7), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_help, 'money'),
        (s(7), sh.dur + 1, rw('day', mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.5, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
