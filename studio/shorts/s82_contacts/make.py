"""THEY'RE TRICKING YOU #2: why every app wants your contacts.
Sources: Google Play Personal Loans policy update (Apr 2023, effective 31 May 2023): personal loan apps may not access
contacts or photos; widespread reports (RBI working group on digital lending, police advisories) of illegal loan apps
harassing borrowers' contacts. Growth: 'find friends / invite' contact upload."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s82_contacts"
CAPS = [
    "Every new app asks for this first: allow contacts. But WHY?",
    "Reason 1: growth. They use your contacts to send invites to your friends and grow their user list.",
    "Think: you tapped allow, so your friends' numbers are with the company too, without asking them.",
    "And the most dangerous: some fake loan apps took contacts and made threat calls to people's family and friends.",
    "That's why from 2023 Google blocked personal loan apps from accessing contacts and photos.",
    "Fix: think before you tap. A chat app needs contacts, a torch app doesn't. Go to Settings and remove useless permissions.",
    "Same bro? Check today how many apps have your contacts. Comment.",
]
HOOK = [("EVERY APP WANTS", WHITE), ("YOUR CONTACTS. WHY?", YEL), ("THEY'RE TRICKING YOU #2", GREY)]
SRC = "SRC: Google Play loan-app policy (2023)"
sh = None


def perm_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.12, 0.13, 0.17); c.fill()
    S.rrect(c, 30, 140, w - 60, 330, 26); c.set_source_rgb(0.95, 0.95, 0.97); c.fill()
    c.arc(w / 2, 200, 30, 0, 6.283); c.set_source_rgb(0.25, 0.5, 0.95); c.fill()
    T(c, "Allow FreeApp to access", w / 2, 285, 28, (0.15, 0.15, 0.18), stroke=None)
    T(c, "your contacts?", w / 2, 325, 28, (0.15, 0.15, 0.18), stroke=None)
    T(c, "DON'T ALLOW", w / 2 - 95, 420, 26, (0.4, 0.4, 0.45), stroke=None)
    S.rrect(c, w / 2 + 20, 385, 150, 56, 28); c.set_source_rgb(0.25, 0.5, 0.95); c.fill()
    T(c, "ALLOW", w / 2 + 95, 422, 26, WHITE, stroke=None)


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
    U.phone_frame(c, 290, 640, 500, 560, perm_screen, t - st, tilt=-2 + 3 * lt)


def o_growth(c, t, lt):
    st = sh.s(2)
    K.panel(c, 860, 480)
    T(c, "REASON 1: GROWTH", 540, 950, 60, YEL, k(t, st, st + 0.3), stroke=None)
    K.rows(c, t, st, [("Invites go to your friends", WHITE, 52, 1.5), ("Their user list grows", GRN, 54, 4.0)], y0=1080, gap=120)


def o_friends(c, t, lt):
    st = sh.s(3)
    K.full(c, t, st, [("YOU TAPPED ALLOW", WHITE, 70, 0.1), ("YOUR FRIENDS' NUMBERS", YEL, 64, 1.3), ("SHARED TOO", RED, 90, 2.6),
                      ("WITHOUT ASKING THEM", GREY, 56, 3.4)], y0=520, gap=170)


def o_loan(c, t, lt):
    st = sh.s(4)
    K.panel(c, 860, 520)
    K.stamp(c, t, st + 0.2, "FAKE LOAN APPS", 540, 960, RED, 56, -0.03)
    K.rows(c, t, st, [("Took your contacts", WHITE, 52, 2.2), ("Threat calls to family", WHITE, 52, 3.6),
                      ("and friends", WHITE, 52, 3.6)], y0=1110, gap=90)


def o_google(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("GOOGLE PLAY, 2023:", GREY, 60, 0.1), ("LOAN APPS CAN'T", WHITE, 74, 1.4), ("ACCESS CONTACTS", YEL, 74, 2.4),
                      ("OR PHOTOS", YEL, 74, 2.8)], y0=520, gap=170)


def o_fix(c, t, lt):
    st = sh.s(6)
    K.panel(c, 820, 560)
    T(c, "THE FIX", 540, 900, 60, YEL, stroke=None)
    K.rows(c, t, st, [("Think before ALLOW", WHITE, 50, 0.4, "left", 140), ("Chat app: contacts OK", GRN, 50, 1.6, "left", 140),
                      ("Torch app: NO", RED, 50, 2.8, "left", 140), ("Settings: remove extra", WHITE, 50, 4.2, "left", 140),
                      ("permissions", WHITE, 50, 4.2, "left", 140)], y0=990, gap=82)


def o_end(c, t, lt):
    K.end_card(c, "CHECK YOUR APPS TODAY", "COMMENT HOW MANY", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (60, 120)))
    sh.shots = [
        (0, s(2), rw('day', mouth='flat', squint=0.3, **ph), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_growth, 'studio'),
        (s(3), s(4), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_friends, 'money'),
        (s(4), s(5), rw('night', mouth='frown', angry=0.4, **ph), (1.9, 1000, 480), (2.05, 1000, 455), o_loan, 'red'),
        (s(5), s(6), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_google, 'studio'),
        (s(6), s(7), rw('day', mouth='smile', **ph), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(7), sh.dur + 1, rw('day', mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.5, 3.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
