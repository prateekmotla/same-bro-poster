"""THEY'RE TRICKING YOU #5: incognito mode isn't private (engine: vshort.Short).
Facts: Chrome's own Incognito new-tab page: Chrome won't save browsing history, cookies and site data, or info entered
in forms; 'your activity might still be visible to websites you visit, your employer or school, your internet service
provider'. Google changed the disclaimer in Jan 2024 and in April 2024 settled the US class action Brown v. Google,
agreeing to delete/destroy billions of data records collected from users' private browsing (Reuters / The Verge, Apr 2024)."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c095_incognito"
CAPS = [
    "Opened an incognito tab, and now NOBODY can see? Really?",
    "Incognito only does this: your history and cookies aren't saved on YOUR phone. That's it.",
    "So who can still see you in incognito? A: nobody. B: websites, your office or college wifi, and your internet company. Comment!",
    "B is right. Google's own incognito page says it: websites, your employer or school, and your internet provider may still see your activity.",
    "And in 2024, in a US case, Google agreed to delete data it had collected from incognito browsing.",
    "Incognito hides it from your family, not from the world. Send this to a friend.",
]
HOOK = [("INCOGNITO = PRIVATE?", WHITE), ("NOT FROM THEM", RED), ("THEY'RE TRICKING YOU #5", GREY)]
SRC = "SRC: Chrome Incognito page; Brown v. Google settlement, 2024"
sh = None


def spy(c, x, y, s, col=(0.85, 0.87, 0.95)):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.rectangle(-70, -20, 140, 14); c.set_source_rgb(*col); c.fill()        # hat brim
    S.rrect(c, -40, -70, 80, 54, 14); c.set_source_rgb(*col); c.fill()     # hat
    for gx in (-32, 32):                                                   # glasses
        c.arc(gx, 30, 24, 0, 6.283); c.set_source_rgb(*col); c.set_line_width(9); c.stroke()
    c.move_to(-8, 30); c.line_to(8, 30); c.stroke()
    c.restore()


def inc_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.13, 0.13, 0.15); c.fill()
    S.rrect(c, 20, 30, w - 40, 60, 30); c.set_source_rgb(0.22, 0.22, 0.25); c.fill()
    spy(c, w / 2, 240, 1.2)
    T(c, "You've gone", w / 2, 380, 36, WHITE, stroke=None, bold=False)
    T(c, "INCOGNITO", w / 2, 430, 44, WHITE, stroke=None)
    for j in range(5):
        c.rectangle(50, 490 + j * 34, w - 100 - (j % 2) * 80, 14); c.set_source_rgb(0.3, 0.3, 0.33); c.fill()


def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "night")
        d = dict(pose='stand', mouth='smirk', look=(0.6, 0)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 660, 700, 330, 560, inc_screen, t - st, tilt=4)
    if t > st + 2.6:
        K.stamp(c, t, st + 2.6, "REALLY?", 330, 1250, RED, 70, -0.05)


def o_only(c, t, lt):
    st = sh.s(2)
    K.full(c, t, st, [("INCOGNITO ONLY", WHITE, 64, 0.1), ("DOESN'T SAVE ON", WHITE, 56, 1.0), ("YOUR PHONE:", YEL, 72, 1.6),
                      ("HISTORY + COOKIES", GRN, 66, 3.2), ("THAT'S IT.", RED, 96, 5.6)], y0=450, gap=160)


def o_choice(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "WHO CAN STILL SEE YOU?", 540, 470, 64, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", ("NOBODY", ""), 2.6), ("B", ("WEBSITES, YOUR WIFI", "OWNER, INTERNET CO."), 3.6))):
        a = k(t, st + d, st + d + 0.3)
        y = 580 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        if txt[1]:
            T(c, txt[0], 610, y + 85, 44, WHITE, a, stroke=None)
            T(c, txt[1], 610, y + 145, 44, WHITE, a, stroke=None)
        else:
            T(c, txt[0], 610, y + 112, 52, WHITE, a, stroke=None)
    K.stamp(c, t, st + 8.2, "COMMENT A or B", 540, 1120, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    S.rrect(c, 110, 400, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: THEY CAN SEE", 540, 495, 64, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 410, GRN, 54, 0.06)
    T(c, "GOOGLE'S OWN INCOGNITO PAGE:", 540, 640, 44, YEL, k(t, st + 1.2, st + 1.5), stroke=None)
    for j, (lab, d) in enumerate((("WEBSITES YOU VISIT", 3.4), ("EMPLOYER / SCHOOL", 4.6), ("INTERNET PROVIDER", 6.2))):
        a = k(t, st + d, st + d + 0.3)
        y = 700 + j * 150
        S.rrect(c, 150, y, 780, 120, 30); c.set_source_rgba(0.14, 0.15, 0.22, 0.95 * a); c.fill()
        T(c, lab, 540, y + 78, 50, WHITE, a, stroke=None)
    T(c, "MAY STILL SEE YOUR ACTIVITY", 540, 1200, 48, RED, k(t, st + 7.4, st + 7.7), lw=8)


def o_case(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("2024, US CASE:", WHITE, 64, 0.1), ("GOOGLE AGREED", YEL, 80, 1.6), ("TO DELETE DATA", WHITE, 70, 2.6),
                      ("FROM INCOGNITO", RED, 80, 3.4), ("BROWSING", RED, 80, 3.6)], y0=480, gap=160)


def o_end(c, t, lt):
    K.end_card(c, "HIDDEN FROM FAMILY,", "NOT FROM THE WORLD.", YEL)
    st = sh.s(6)
    T(c, "A or B? COMMENT", 540, 1260, 64, YEL, k(t, st + 1.2, st + 1.5), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(**ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'night'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_only, 'studio'),
        (s(3), s(4), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(4), s(5), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'red'),
        (s(5), s(6), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_case, 'studio'),
        (s(6), sh.dur + 1, w_room(**ph), (1.6, 960, 560), (1.7, 960, 540), o_end, 'night'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 3.5] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[2][0] + 4.0], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
