"""THEY'RE TRICKING YOU #4: IPL teams earn even when they lose (engine: vshort.Short).
Fact: BCCI sold IPL media rights for 2023-2027 for Rs 48,390 crore (BCCI announcement, June 2022; ESPNcricinfo,
afaqs). Franchises get a share of the BCCI central pool (media rights + central sponsorship) every season, whatever
their result (Business Insider India: media rights reportedly 60-70% of a team's revenue, sponsorship 20-30%, tickets
~10%; part of the pool share is weighted by league position). Prize money is small next to that. No team named."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c087_ipl"
CAPS = [
    "Your team lost, you're sad. But the team's owner? He's STILL earning. How?",
    "Question. Does the team that finishes LAST go into loss? A: yes. B: no, it still earns. Comment!",
    "The answer is B. IPL's TV and digital rights deal for 2023 to 2027 is worth ₹48,390 crore.",
    "Every team gets a share of this central pool, win or lose. On top: jersey sponsors and ticket money.",
    "The trophy prize money? Just a small slice of all this.",
    "So next time your team loses, remember: YOUR heart broke, not the owner's wallet. Send this to your cricket friend.",
]
HOOK = [("YOUR TEAM LOST.", WHITE), ("OWNER STILL EARNS", GRN), ("THEY'RE TRICKING YOU #4", GREY)]
SRC = "SRC: BCCI media rights 2023-27 announcement"
sh = None


def score_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.05, 0.08, 0.16); c.fill()
    T(c, "T20 LEAGUE · LIVE", w / 2, 70, 26, GREY, stroke=None, bold=False)
    T(c, "YOUR TEAM", w / 2, 160, 34, WHITE, stroke=None)
    T(c, "142/9", w / 2, 230, 56, WHITE, stroke=None)
    T(c, "OTHER TEAM", w / 2, 320, 34, WHITE, stroke=None)
    T(c, "146/4", w / 2, 390, 56, WHITE, stroke=None)
    S.rrect(c, 30, h - 120, w - 60, 70, 20); c.set_source_rgb(0.75, 0.15, 0.15); c.fill()
    T(c, "LOST BY 6 WICKETS", w / 2, h - 72, 28, WHITE, stroke=None)


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


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 700, 720, 330, 520, score_screen, t - st, tilt=4)
    if t > st + 2.6:
        K.stamp(c, t, st + 2.6, "OWNER: +₹ CRORES", 330, 1250, GRN, 50, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "LAST-PLACE TEAM =", 540, 430, 62, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "LOSS?", 540, 510, 72, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "YES, IN LOSS", 2.6), ("B", "NO, STILL EARNS", 3.8))):
        a = k(t, st + d, st + d + 0.3)
        y = 600 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 112, 50, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.4, "COMMENT A or B", 540, 1140, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: STILL EARNS", 540, 475, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 390, GRN, 54, 0.06)
    K.rows(c, t, st, [("IPL TV + DIGITAL RIGHTS", WHITE, 56, 1.4), ("2023-2027", YEL, 60, 2.6),
                      ("₹48,390 CR", GRN, 120, 4.4)], y0=700, gap=150)


def o_pool(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.9)
    a = k(t, st, st + 0.3)
    c.arc(540, 560, 150, 0, 2 * math.pi); c.set_source_rgba(0.1, 0.4, 0.2, a); c.fill()
    T(c, "CENTRAL", 540, 545, 44, WHITE, a, stroke=None)
    T(c, "POOL", 540, 600, 44, WHITE, a, stroke=None)
    for j in range(10):
        dt = 0.6 + j * 0.18
        b = k(t, st + dt, st + dt + 0.2)
        if b <= 0:
            continue
        x = 120 + (j % 5) * 210
        y = 820 + (j // 5) * 140
        c.move_to(540, 710); c.line_to(x, y - 40); c.set_source_rgba(*GRN, 0.4 * b); c.set_line_width(4); c.stroke()
        S.rrect(c, x - 80, y - 40, 160, 100, 22); c.set_source_rgba(0.14, 0.16, 0.26, b); c.fill()
        T(c, f"TEAM {j + 1}", x, y, 30, WHITE, b, stroke=None)
        T(c, "+₹", x, y + 42, 32, GRN, b, stroke=None)
    T(c, "WIN OR LOSE", 540, 1130, 66, YEL, k(t, st + 2.6, st + 2.9), lw=10)
    T(c, "+ JERSEY SPONSORS", 540, 1235, 52, WHITE, k(t, st + 4.0, st + 4.3), lw=8)
    T(c, "+ TICKETS", 540, 1315, 52, WHITE, k(t, st + 4.8, st + 5.1), lw=8)


def o_prize(c, t, lt):
    st = sh.s(5)
    U.dim(c, 0.9)
    T(c, "TROPHY PRIZE MONEY?", 540, 470, 62, WHITE, k(t, st, st + 0.2), lw=10)
    a = k(t, st + 0.5, st + 0.9)
    cx, cy, r = 540, 820, 230
    c.move_to(cx, cy); c.arc(cx, cy, r, -math.pi / 2 + 0.35, -math.pi / 2 + 2 * math.pi * a)
    c.close_path(); c.set_source_rgba(0.12, 0.45, 0.25, 1); c.fill()
    if a > 0.5:
        c.move_to(cx, cy); c.arc(cx, cy, r + 14, -math.pi / 2, -math.pi / 2 + 0.35); c.close_path()
        c.set_source_rgb(*YEL); c.fill()
        T(c, "PRIZE", cx + 150, cy - 260, 44, YEL, stroke=None)
        T(c, "TV RIGHTS + SPONSORS + TICKETS", 540, 1120, 42, WHITE, stroke=None)
    T(c, "JUST A SMALL SLICE", 540, 1250, 64, YEL, k(t, st + 1.8, st + 2.1), lw=10)
    T(c, "(illustration, not to scale)", 540, 1330, 30, GREY, k(t, st + 1.8, st + 2.1), stroke=None, bold=False)


def o_end(c, t, lt):
    K.end_card(c, "YOUR HEART BROKE.", "NOT THE OWNER'S WALLET", YEL)
    st = sh.s(6)
    T(c, "SEND TO YOUR CRICKET FRIEND", 540, 1260, 50, GRN, k(t, st + 2.0, st + 2.3), lw=8)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='frown', **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(4), s(5), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_pool, 'money'),
        (s(5), s(6), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_prize, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 3.5, 5.5] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[3][0] + 3.0], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
