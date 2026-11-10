"""RULES YOU DIDN'T KNOW #6: hospitals can't refuse emergency treatment.
Sources: Supreme Court, Pt. Parmanand Katara v. Union of India (1989): every doctor, at a government hospital or
otherwise, must give immediate medical aid to preserve life; procedural / police formalities can't delay it.
Good Samaritan protection: SC guidelines (2016) + Motor Vehicles Act s.134A (2019): no civil/criminal liability,
can't be forced to disclose identity; hospitals can't demand payment from them. Emergency 112 / ambulance 108."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s83_hospital"
CAPS = [
    "An accident, bleeding, and the hospital says: police case first, treatment later? WRONG.",
    "Supreme Court, 1989, Parmanand Katara case: every doctor has a duty to give immediate treatment to save a life.",
    "Police formalities or paperwork can't be an excuse to stop treatment. Government hospital or private.",
    "And whoever brings the injured person in doesn't need to fear either. The law protects a Good Samaritan: they can't be forced to give their name or pay.",
    "In an emergency, call 112 or 108, and take them to the nearest hospital.",
    "Same bro? How many people know this rule? Comment, and share this.",
]
HOOK = [("'POLICE CASE FIRST'?", WHITE), ("NO. TREAT FIRST.", GRN), ("RULES YOU DIDN'T KNOW #6", GREY)]
SRC = "SRC: Supreme Court, Parmanand Katara (1989)"
sh = None


def hosp(c, t):
    c.rectangle(0, 0, 1920, 1080); c.set_source_rgb(0.86, 0.9, 0.92); c.fill()
    c.rectangle(0, 760, 1920, 320); c.set_source_rgb(0.72, 0.76, 0.78); c.fill()
    S.rrect(c, 560, 90, 760, 110, 18); c.set_source_rgb(0.85, 0.15, 0.15); c.fill()
    T(c, "EMERGENCY", 940, 168, 66, WHITE, stroke=None)
    c.rectangle(1360, 260, 380, 500); c.set_source_rgb(0.7, 0.82, 0.88); c.fill()
    c.rectangle(1545, 260, 10, 500); c.set_source_rgb(0.5, 0.6, 0.65); c.fill()
    # reception desk
    c.rectangle(200, 560, 560, 200); c.set_source_rgb(0.95, 0.95, 0.96); c.fill()
    c.rectangle(200, 545, 560, 22); c.set_source_rgb(0.3, 0.55, 0.75); c.fill()
    # red cross sign
    c.rectangle(380, 300, 40, 120); c.set_source_rgb(0.85, 0.15, 0.15); c.fill()
    c.rectangle(340, 340, 120, 40); c.set_source_rgb(0.85, 0.15, 0.15); c.fill()


def hw(**kw):
    def f(c, t, lt):
        hosp(c, t)
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
    K.panel(c, 900, 360)
    T(c, "'POLICE CASE FIRST,", 540, 1000, 56, WHITE, k(t, st + 0.3, st + 0.6), stroke=None)
    T(c, "TREATMENT LATER'", 540, 1075, 56, WHITE, k(t, st + 0.3, st + 0.6), stroke=None)
    K.stamp(c, t, st + 5.2, "WRONG", 540, 1200, RED, 70, -0.05)


def o_sc(c, t, lt):
    st = sh.s(2)
    K.panel(c, 820, 560)
    T(c, "SUPREME COURT, 1989", 540, 905, 56, YEL, k(t, st, st + 0.3), stroke=None)
    T(c, "Parmanand Katara case", 540, 975, 46, GREY, k(t, st + 1.0, st + 1.3), stroke=None)
    K.rows(c, t, st, [("Every doctor MUST give", WHITE, 52, 3.6), ("immediate treatment", GRN, 56, 4.4),
                      ("to save a life", GRN, 56, 4.4)], y0=1080, gap=95)


def o_paper(c, t, lt):
    st = sh.s(3)
    K.full(c, t, st, [("POLICE FORMALITIES?", WHITE, 70, 0.1), ("PAPERWORK?", WHITE, 70, 0.9), ("NOT AN EXCUSE", RED, 90, 2.2),
                      ("GOVT OR PRIVATE", YEL, 66, 4.0)], y0=520, gap=170)


def o_sam(c, t, lt):
    st = sh.s(4)
    K.panel(c, 820, 600)
    T(c, "GOOD SAMARITAN", 540, 905, 60, YEL, k(t, st, st + 0.3), stroke=None)
    T(c, "(whoever brings them in)", 540, 965, 40, GREY, k(t, st, st + 0.3), stroke=None)
    K.rows(c, t, st, [("Protected by law", GRN, 54, 3.6), ("Can't be forced to", WHITE, 50, 5.8),
                      ("give name or pay", WHITE, 50, 5.8)], y0=1070, gap=100)


def o_call(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("EMERGENCY?", WHITE, 74, 0.1), ("CALL 112 / 108", GRN, 100, 0.8), ("NEAREST HOSPITAL", YEL, 70, 2.6)],
           y0=560, gap=190)


def o_end(c, t, lt):
    K.end_card(c, "WHO KNEW THIS RULE?", "COMMENT + SHARE", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'warm'
    s = sh.s
    sh.shots = [
        (0, s(2), hw(mouth='frown', angry=0.5, arms=((60, 120), (60, 120))), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_sc, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_paper, 'money'),
        (s(4), s(5), hw(mouth='smile'), (1.9, 1000, 480), (2.0, 1000, 460), o_sam, 'warm'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_call, 'money'),
        (s(6), sh.dur + 1, hw(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 480), (2.1, 1000, 450), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.5, 5.6] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
