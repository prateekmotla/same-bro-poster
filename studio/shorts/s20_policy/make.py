import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
import body as B  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s20_policy"
CAPS = [
    "Agent uncle comes to Sid's home. \"Beta, take this policy. Insurance AND investment. Both together!\"",
    "Look at a real example. ₹50 lakh cover. Endowment policy premium: around ₹1.4 LAKH a year.",
    "The same ₹50 lakh cover in a term plan? Only around ₹13,000.",
    "So why does the agent sell endowment? In this example, in year 1 the agent gets 25% of the premium as COMMISSION. That's ₹33,000. On the term plan? Only around ₹3,000.",
    "And the return? In this example, around 7.7% a year. Mix insurance and investment, and both end up half-done.",
    "Simple rule: TERM PLAN for insurance. Invest separately. And before signing, ask straight: what's YOUR commission on this?",
    "Send this to the friend whose dad bought 3 policies in his name.",
]
HOOK = [("WHY AGENTS", WHITE), ("NEVER PUSH", RED), ("TERM PLANS", YEL)]
SRC = "Source: The Federal, May 2022 (₹50L cover example)"
sh = None


def home(c, t, lt, agent=True, sid_kw=None, ag_kw=None):
    V.room(c, t, 'day')
    a = dict(who='bhai', pose='stand', mouth='bigsmile', arms=((70, 120), (14, -10)), glasses=False)
    a.update(ag_kw or {})
    d = dict(pose='stand', mouth='flat', look=(-0.6, 0))
    d.update(sid_kw or {})
    if agent:
        B.figure(c, 760, 320, 0.5, t, **a)
    K.sid(c, t, 1180, 330, 0.5, **d)


def studio(c, t, lt, **kw):
    V.studio(c, t)
    K.sid(c, t, 960, 330, 0.5, **kw)


def o_pitch(c, t, lt):
    st = sh.s(1)
    if t < st + 2.4:
        return
    K.panel(c, 900, 300, 120, 840, a=0.92 * k(t, st + 2.4, st + 2.6))
    K.rows(c, t, st, [("INSURANCE + INVESTMENT", YEL, 50, 2.6), ("\"Both together, beta!\"", WHITE, 46, 4.2)],
           y0=1010, gap=110)


def o_premium(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "SAME ₹50 LAKH COVER", 540, 400, 70, WHITE, k(t, st + 1.0, st + 1.3), lw=10)
    T(c, "yearly premium", 540, 480, 44, GREY, k(t, st + 1.0, st + 1.3), lw=6)
    K.hbar(c, t, st + 2.8, 140, 680, 800, 90, 1.0, RED, "ENDOWMENT", "₹1,40,000")
    if t > sh.s(3):
        K.hbar(c, t, sh.s(3) + 1.6, 140, 900, 800, 90, 0.095, GRN, "TERM PLAN", "₹13,000")
    if t > sh.s(3) + 3.0:
        T(c, "~10x cheaper", 540, 1120, 80, GRN, k(t, sh.s(3) + 3.0, sh.s(3) + 3.3), lw=10)


def o_comm(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "AGENT'S YEAR-1", 540, 390, 70, WHITE, k(t, st + 2.0, st + 2.3), lw=10)
    T(c, "COMMISSION", 540, 480, 70, YEL, k(t, st + 2.0, st + 2.3), lw=10)
    T(c, "ENDOWMENT  (25%)", 540, 650, 52, GREY, k(t, st + 4.0, st + 4.3), lw=6)
    T(c, "₹33,000", 540, 790, 150, RED, k(t, st + 6.0, st + 6.3), lw=14)
    T(c, "TERM PLAN", 540, 960, 52, GREY, k(t, st + 8.0, st + 8.3), lw=6)
    T(c, "~₹3,000", 540, 1090, 120, GRN, k(t, st + 8.4, st + 8.7), lw=12)


def o_return(c, t, lt):
    st = sh.s(5)
    K.panel(c, 870, 500)
    K.rows(c, t, st, [("RETURN in this example", WHITE, 46, 0.6), ("~7.7% a year", YEL, 70, 2.4),
                      ("Insurance + investment", WHITE, 46, 4.0), ("= both HALF-DONE", RED, 56, 5.4)], y0=960, gap=105)


def o_rule(c, t, lt):
    st = sh.s(6)
    K.panel(c, 860, 520)
    T(c, "SIMPLE RULE", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Insurance = TERM PLAN", GRN, 46, 1.2, "left", 150),
                      ("2. Invest separately", WHITE, 46, 2.8, "left", 150),
                      ("3. Ask: \"Your commission?\"", YEL, 46, 4.6, "left", 150)], y0=1070, gap=100)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WITH 3 POLICIES IN HIS NAME", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    sw = lambda **kw: (lambda c, t, lt: studio(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), lambda c, t, lt: home(c, t, lt, sid_kw=dict(mouth='flat', raise_=0.5)), (1.55, 970, 520), (1.65, 970, 500),
         o_pitch, 'morning'),
        (s(2), s(4), sw(), (1.78, 960, 540), (1.85, 960, 520), o_premium, 'studio'),
        (s(4), s(5), lambda c, t, lt: home(c, t, lt, sid_kw=dict(mouth='o', eyes=1.2), ag_kw=dict(mouth='smirk')),
         (1.55, 970, 540), (1.6, 970, 520), o_comm, 'morning'),
        (s(5), s(6), sw(mouth='smirk', arms=((60, 120), (14, -10))), (1.9, 960, 500), (2.0, 960, 470), o_return, 'studio'),
        (s(6), s(7), lambda c, t, lt: home(c, t, lt, agent=False, sid_kw=dict(mouth='smirk', look=(0, 0))),
         (1.9, 1180, 500), (2.0, 1180, 480), o_rule, 'morning'),
        (s(7), sh.dur + 1, lambda c, t, lt: home(c, t, lt, agent=False, sid_kw=dict(mouth='smile', look=(0, 0),
                                                                                     arms=((14, -10), (100, 40)))),
         (1.9, 1180, 500), (2.1, 1180, 470), o_end, 'morning'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1, 6] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
