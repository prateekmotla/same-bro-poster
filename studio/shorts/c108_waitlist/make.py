"""RULES YOU DIDN'T KNOW #15: fully waitlisted e-ticket after the chart (engine: vshort.Short).
Fact: Railway Passengers (Cancellation of Ticket and Refund of Fare) Rules 2015, rule 4(a)-style provision for e-tickets:
a fully waitlisted e-ticket whose passengers stay waitlisted after chart preparation is dropped from the chart and
the fare is refunded automatically to the account used for booking, minus clerkage. Waitlisted ticket holders are not
allowed in reserved sleeper/AC coaches (Railways enforcement from 1 May 2025: penalty and shifted to the general coach,
The Week / national media 1 May 2025)."""

import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c108_waitlist"
CAPS = [
    "Online ticket stuck on waitlist, the chart is out. Should I just board the train?",
    "A: board, the TTE will adjust. B: don't board, take the refund. You tell me, A or B? Comment!",
    "B. Don't board. A waitlisted online ticket gets CANCELLED automatically after the chart.",
    "The refund comes on its own to the same account, minus a small clerkage fee. No need to go to a counter.",
    "And if you sit in sleeper or AC on a waitlisted ticket, you'll be fined and sent to the general coach.",
    "Got a friend on the waitlist? Send them this.",
]
HOOK = [("WL TICKET. CHART OUT.", WHITE), ("BOARD OR NOT?", YEL), ("RULES YOU DIDN'T KNOW #15", GREY)]
SRC = "SRC: Indian Railways refund rules 2015"
sh = None

def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "morning")
        d = dict(pose='stand', mouth='flat', look=(0.6, 0)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f



def ticket(title, rows):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.95, 0.95, 0.97); c.fill()
        c.rectangle(0, 0, w, 110); c.set_source_rgb(0.12, 0.25, 0.55); c.fill()
        T(c, title, w / 2, 72, 34, WHITE, stroke=None)
        for i, (ln, col) in enumerate(rows):
            T(c, ln, 30, 200 + i * 80, 34, col, stroke=None, anchor="left")
    return f


def o_hook(c, t, lt):
    U.phone_frame(c, 660, 700, 360, 620, ticket("E-TICKET", [("DELHI > PATNA", (0.1, 0.1, 0.15)), ("SLEEPER (SL)", GREY),
                                                             ("STATUS: WL 14", RED), ("CHART PREPARED", RED),
                                                             ("NOT CONFIRMED", RED)]), t, tilt=4)
    if t > 3.0:
        K.stamp(c, t, 3.0, "BOARD ANYWAY?", 300, 1220, YEL, 60, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "WAITLISTED E-TICKET", 540, 430, 62, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "AFTER THE CHART?", 540, 515, 56, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "BOARD, TTE WILL ADJUST", 0.2), ("B", "DON'T BOARD, GET REFUND", 3.2))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 112, 42, WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.2, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: DON'T BOARD", 540, 478, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 390, GRN, 54, 0.06)
    K.rows(c, t, st, [("Fully waitlisted e-ticket", WHITE, 52, 1.6), ("after the chart =", WHITE, 52, 1.9),
                      ("AUTO-CANCELLED", YEL, 72, 2.6)], y0=700, gap=110)


def o_refund(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("REFUND COMES", WHITE, 70, 0.2), ("AUTOMATICALLY", GRN, 86, 0.6), ("TO THE SAME ACCOUNT", WHITE, 56, 1.8),
                      ("MINUS SMALL CLERKAGE", GREY, 46, 2.8), ("NO COUNTER VISIT", YEL, 60, 4.2)], y0=440, gap=150)


def o_fine(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("WL TICKET IN", WHITE, 64, 0.2), ("SLEEPER / AC?", RED, 90, 0.7), ("= FINE", RED, 110, 2.6),
                      ("+ SENT TO GENERAL COACH", WHITE, 46, 3.6)], y0=480, gap=170)


def o_end(c, t, lt):
    K.end_card(c, "WL AFTER CHART?", "DON'T BOARD. REFUND IS AUTO.", YEL)
    st = sh.s(6)
    T(c, "SEND TO A WL FRIEND", 540, 1260, 56, GRN, k(t, st + 0.8, st + 1.1), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', squint=0.2, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_refund, 'money'),
        (s(5), s(6), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_fine, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
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
