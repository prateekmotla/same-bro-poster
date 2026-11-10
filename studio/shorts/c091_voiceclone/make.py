"""SCAM OF THE WEEK #6: AI voice-clone 'your son is in trouble' call (engine: vshort.Short).
Facts: Business Standard 15 Jan 2026 'AI-based financial scams: set a family code word for emergency requests';
Tamil Nadu Cyber Crime Police advisory on AI voice cloning (fraudsters clone a relative's voice from social-media
clips and ask for urgent money); UCO Bank security advisory 'Beware of AI voice scam': hang up, call the person back
on the number you have saved, verify before paying. Report fraud: 1930 / cybercrime.gov.in.
Voice take sped 1.05x (41.4 s > 39.4 s)."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c091_voiceclone"
CAPS = [
    "11 PM, mom gets a call. Her son's voice, crying: 'I had an accident, send 50,000 NOW.'",
    "But it was NOT her son. AI copied his voice from his social media videos. A few seconds of audio is enough.",
    "What should mom do? A: send the money fast. B: hang up and call her son back on his SAVED number. Comment!",
    "B is right. Police and bank advisories say the same: call back yourself and verify. Don't trust the voice alone.",
    "Set a family code word that only your family knows. And if you get scammed, call 1930 right away.",
    "Next time a voice cries for money, call back first. Send this to your mummy-papa.",
]
HOOK = [("SON'S VOICE. CRYING.", WHITE), ("IT WASN'T HIM", RED), ("SCAM OF THE WEEK #6", GREY)]
SRC = "SRC: TN Cyber Crime Police & bank advisories on AI voice scams"
sh = None


def wave(c, x, y, w, h, t, col, a=1.0, n=34):
    for j in range(n):
        amp = (0.25 + 0.75 * abs(math.sin(j * 0.7 + t * 7) * math.sin(j * 0.23 + t * 3))) * h
        c.rectangle(x + j * w / n, y - amp / 2, w / n * 0.6, amp); c.set_source_rgba(*col, a); c.fill()


def call_screen(name, sub, col, crying=False):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.06, 0.07, 0.1); c.fill()
        T(c, sub, w / 2, 120, 30, GREY, stroke=None, bold=False)
        c.arc(w / 2, 260, 90, 0, 6.283); c.set_source_rgb(0.3, 0.33, 0.42); c.fill()
        c.arc(w / 2, 235, 34, 0, 6.283); c.set_source_rgb(0.75, 0.78, 0.85); c.fill()
        c.arc(w / 2, 330, 62, 3.4, 6.0); c.set_source_rgb(0.75, 0.78, 0.85); c.fill()
        T(c, name, w / 2, 420, 50, WHITE, stroke=None)
        if crying:
            wave(c, 60, 520, w - 120, 90, tt, (1, 0.45, 0.4))
        for j, (cx, cc) in enumerate(((w * 0.28, (0.9, 0.2, 0.2)), (w * 0.72, col))):
            c.arc(cx, h - 110, 52, 0, 6.283); c.set_source_rgb(*cc); c.fill()
    return f


def w_room(c, t, lt):
    V.room(c, t, "night")


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def o_call(c, t, lt):
    st = sh.s(1)
    U.dim(c, 0.45)
    ring = 6 * math.sin(t * 40) * (1 if (t % 1.2) < 0.6 else 0)
    U.phone_frame(c, 300 + ring, 430, 480, 760, call_screen("BETA", "incoming call  11:04 PM", GRN, crying=t > st + 2.2), t - st, tilt=0)
    if t > st + 2.6:
        a = k(t, st + 2.6, st + 2.9)
        S.rrect(c, 80, 1230, 920, 170, 40); c.set_source_rgba(1, 1, 1, 0.96 * a); c.fill()
        T(c, "'MOM, I HAD AN ACCIDENT!", 540, 1300, 44, (0.1, 0.1, 0.15), a, stroke=None)
        T(c, "SEND ₹50,000 NOW!'", 540, 1365, 50, RED, a, stroke=None)


def o_clone(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.7)
    K.stamp(c, t, st + 0.2, "IT WASN'T HIM", 540, 460, RED, 66, -0.04)
    for j in range(3):   # reel tiles
        a = k(t, st + 1.2 + j * 0.3, st + 1.5 + j * 0.3)
        S.rrect(c, 90 + j * 140, 620 + j * 30, 200, 330, 22); c.set_source_rgba(0.2 + 0.1 * j, 0.22, 0.4, 0.95 * a); c.fill()
        c.move_to(170 + j * 140, 750 + j * 30); c.rel_line_to(0, 70); c.rel_line_to(55, -35); c.close_path()
        c.set_source_rgba(1, 1, 1, 0.9 * a); c.fill()
    a = k(t, st + 2.6, st + 2.9)
    T(c, ">", 560, 830, 110, YEL, a, stroke=None)
    S.rrect(c, 640, 690, 300, 230, 30); c.set_source_rgba(0.1, 0.1, 0.14, 0.95 * a); c.fill()
    T(c, "AI", 790, 800, 90, (0.6, 0.85, 1), a, stroke=None)
    wave(c, 670, 870, 240, 50, t, (0.6, 0.85, 1), a, n=20)
    K.rows(c, t, st, [("HIS VOICE, COPIED", WHITE, 58, 3.6), ("FROM A FEW SECONDS OF VIDEO", YEL, 46, 4.6)], y0=1110, gap=90)


def o_choice(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "WHAT SHOULD MOM DO?", 540, 470, 66, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", ("SEND THE MONEY", "FAST"), 1.6), ("B", ("HANG UP, CALL BACK", "ON HIS SAVED NUMBER"), 3.4))):
        a = k(t, st + d, st + d + 0.3)
        y = 580 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt[0], 610, y + 85, 44, WHITE, a, stroke=None)
        T(c, txt[1], 610, y + 145, 40, YEL if i else WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.0, "COMMENT A or B", 540, 1120, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: CALL BACK & VERIFY", 540, 475, 56, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 870, 390, GRN, 54, 0.06)
    ok = t > st + 3.2
    U.phone_frame(c, 330, 590, 420, 600, call_screen("BETA (saved)", "calling..." if not ok else "connected", GRN), t - st, tilt=1)
    if ok:
        a = k(t, st + 3.2, st + 3.5)
        S.rrect(c, 120, 1230, 840, 100, 40); c.set_source_rgba(1, 1, 1, 0.96 * a); c.fill()
        T(c, "'I'M FINE, MOM. WHAT CALL?'", 540, 1296, 44, (0.1, 0.4, 0.15), a, stroke=None)
    T(c, "DON'T TRUST THE VOICE ALONE", 540, 1400, 44, YEL, k(t, st + 5.0, st + 5.3), stroke=None)


def o_tips(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("SET A FAMILY", WHITE, 62, 0.1), ("CODE WORD", YEL, 96, 0.6), ("ONLY YOUR FAMILY KNOWS IT", GREY, 44, 1.6),
                      ("SCAMMED?", WHITE, 60, 3.6), ("CALL 1930", GRN, 120, 4.2), ("cybercrime.gov.in", GREY, 44, 4.6)],
           y0=430, gap=150)


def o_end(c, t, lt):
    K.end_card(c, "VOICE CRIES FOR MONEY?", "CALL BACK FIRST.", YEL)
    st = sh.s(6)
    T(c, "A or B? COMMENT", 540, 1260, 64, YEL, k(t, st + 1.5, st + 1.8), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    sh.shots = [
        (0, s(2), w_room, (1.0, 960, 540), (1.15, 960, 520), o_call, 'night'),
        (s(2), s(3), sw(phone=1, arms=((14, -10), (60, 120)), mouth='smile'), (1.78, 960, 540), (1.9, 960, 520), o_clone, 'red'),
        (s(3), s(4), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(4), s(5), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(5), s(6), sw(mouth='flat', angry=0.3), (1.78, 960, 540), (1.85, 960, 520), o_tips, 'studio'),
        (s(6), sh.dur + 1, w_room, (1.0, 960, 540), (1.1, 960, 520), o_end, 'night'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 2.0, 4.5] + [a + (b - a) * 0.85 for a, b in L[1:]] + [L[3][0] + 1.5], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
