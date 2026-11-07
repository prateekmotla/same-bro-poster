import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s57_digiarrest"
CAPS = [
    "Guess: a 'CBI officer' on video call. Uniform, ID card. 'You're under DIGITAL ARREST.' Is that real?",
    "Sid gets a call: 'A parcel in your name had drugs. Don't cut the call. Don't tell anyone.'",
    "Truth: there is NO 'digital arrest' in Indian law. CBI, ED, police never arrest anyone on a video call.",
    "Still, Indians lost ₹1,935 crore to 'digital arrest' scams in 2024 (Govt in Parliament).",
    "The trick: fear + isolation. They keep you on the call so you can't ask anyone. Then: 'transfer money for verification'.",
    "Same bro? Someone at home got a call like this and panicked?",
    "Fix: cut the call. Tell someone you trust. Report on 1930 or cybercrime.gov.in.",
    "MORAL: Real police don't arrest on video calls. Fear is their only weapon.",
    "Send this to the friend whose parents pick up every unknown call.",
]
HOOK = [("'YOU ARE UNDER", WHITE), ("DIGITAL ARREST'", RED), ("REAL OR SCAM?", YEL)]
SRC = "Source: MHA reply, Rajya Sabha (Mar 2025); I4C advisory (Oct 2024)"
sh = None


def call_scr(stage):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.08, 0.1, 0.14); c.fill()
        # fake office backdrop
        c.rectangle(0, 120, w, h * 0.55); c.set_source_rgb(0.2, 0.25, 0.32); c.fill()
        T(c, "VIDEO CALL  02:14", w / 2, 80, 30, GREY, stroke=None)
        # officer silhouette with cap
        cx, cy = w / 2, 420
        c.arc(cx, cy, 90, 0, 6.3); c.set_source_rgb(0.55, 0.42, 0.33); c.fill()
        S.rrect(c, cx - 105, cy - 120, 210, 60, 20); c.set_source_rgb(0.15, 0.2, 0.35); c.fill()
        S.rrect(c, cx - 170, cy + 90, 340, 220, 60); c.set_source_rgb(0.25, 0.32, 0.22); c.fill()
        S.rrect(c, cx - 60, cy + 150, 120, 50, 8); c.set_source_rgb(0.9, 0.8, 0.3); c.fill()
        T(c, "'CBI OFFICER'", w / 2, 760, 40, WHITE, stroke=None)
        if stage >= 1:
            S.rrect(c, 30, 130, w - 60, 90, 18); c.set_source_rgba(0.85, 0.15, 0.15, 0.9); c.fill()
            T(c, "DON'T CUT THE CALL", w / 2, 188, 34, WHITE, stroke=None)
        # end call button
        c.arc(w / 2, h - 80, 46, 0, 6.3); c.set_source_rgb(0.9, 0.2, 0.2); c.fill()
        T(c, "END", w / 2, h - 68, 26, WHITE, stroke=None)
    return f


def rw(mode='night', **kw):
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


def o_guess(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 240, 520, 600, 930, call_scr(0), t - st, tilt=-2 + 3 * lt)
    K.stamp(c, t, st + 4.0, "REAL?", 540, 1290, YEL, 64, -0.05)


def o_call(c, t, lt):
    st = sh.s(2)
    U.phone_frame(c, 240, 520, 600, 930, call_scr(1 if t > st + 3.0 else 0), t - st, tilt=2 - 3 * lt)
    K.stamp(c, t, st + 1.4, "'DRUGS IN YOUR PARCEL'", 540, 1290, RED, 50, -0.04)


def o_truth(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "'DIGITAL ARREST'", 540, 440, 66, WHITE, k(t, st + 0.3, st + 0.6), lw=8)
    K.stamp(c, t, st + 1.4, "DOES NOT EXIST IN LAW", 540, 580, GRN, 60, -0.03)
    K.rows(c, t, st, [("CBI / ED / POLICE", WHITE, 60, 4.0), ("NEVER ARREST", YEL, 72, 5.2),
                      ("ON A VIDEO CALL", YEL, 72, 5.6)], y0=820, gap=120)


def o_data(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    T(c, "LOST TO 'DIGITAL ARREST', 2024", 540, 470, 50, GREY, k(t, st + 0.1, st + 0.4), lw=7)
    a = k(t, st + 2.0, st + 3.0)
    T(c, f"₹{int(1935 * U.eob(a)):,} CR", 540, 700, 130, RED, a, lw=12)
    T(c, "(Govt reply in Parliament)", 540, 850, 44, WHITE, k(t, st + 5.0, st + 5.3), lw=6)


def o_trick(c, t, lt):
    st = sh.s(5)
    K.panel(c, 820, 560)
    T(c, "THEIR TRICK", 540, 900, 58, GREY, stroke=None)
    K.rows(c, t, st, [("FEAR", RED, 70, 0.8), ("+ ISOLATION", YEL, 66, 1.8),
                      ("= 'Transfer for verification'", WHITE, 44, 7.0)], y0=1030, gap=110)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("SOMEONE AT HOME", WHITE, 58, 0.2), ("GOT THIS CALL?", YEL, 58, 1.0)], y0=1000, gap=110)
    K.stamp(c, t, st + 2.0, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(7)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. CUT the call", WHITE, 48, 0.2, "left", 140),
                      ("2. Tell someone you trust", WHITE, 48, 1.2, "left", 140),
                      ("3. Report: 1930 /", GRN, 48, 2.8, "left", 140),
                      ("    cybercrime.gov.in", GRN, 48, 2.8, "left", 140)], y0=1010, gap=90)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "NO VIDEO-CALL ARRESTS.", "FEAR IS THEIR WEAPON.", RED)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHOSE PARENTS PICK UP", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'tense'
    s = sh.s
    sh.shots = [
        (0, s(2), rw(mouth='o', eyes=1.3, phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'night'),
        (s(2), s(3), rw(mouth='frown', squint=0.3, phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 480), (2.05, 1000, 455), o_call, 'night'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_truth, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_data, 'money'),
        (s(5), s(6), rw(mouth='frown'), (1.9, 1000, 500), (2.0, 1000, 470), o_trick, 'night'),
        (s(6), s(7), rw('day', mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), rw('day', mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw('day', mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
