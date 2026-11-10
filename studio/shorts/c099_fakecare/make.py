"""SCAM OF THE WEEK #7: fake customer-care number from a web search (engine: vshort.Short).
Facts: Kerala Police via PTI / Outlook India, 3 Oct 2026 — don't blindly trust customer-care numbers found through
internet searches, use only the official websites or apps; never install remote-access / screen-sharing apps or pay at
a stranger's request (fraudsters ask small 'registration/verification' fees like Rs 5); never share OTP/PIN; report to
1930 or cybercrime.gov.in. Cyberabad Cybercrime Police (Telangana Today) also warned of fake numbers posted on Google."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c099_fakecare"
CAPS = [
    "Refund stuck. You searched 'customer care number' on Google and called the TOP result. That's where it went wrong.",
    "On the call: 'Sir, for the refund just download one app and send a ₹5 verification fee.' A: send it. B: hang up. Comment!",
    "B is right. Kerala Police warning: scammers post FAKE customer care numbers on Google.",
    "With a screen-sharing app they see your phone, read your OTP, and the account is EMPTY.",
    "Take the number ONLY from the official app or website. OTP, PIN: to nobody. Scammed? Call 1930 right away.",
    "Send this to your mummy-papa. They also Google helpline numbers.",
]
HOOK = [("GOOGLED A HELPLINE?", WHITE), ("TOP RESULT = SCAMMER", RED), ("SCAM OF THE WEEK #7", GREY)]
SRC = "SRC: Kerala Police advisory (PTI, Oct 2026)"
sh = None


def search_screen(hl=False):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.98); c.fill()
        S.rrect(c, 24, 40, w - 48, 70, 35); c.set_source_rgb(1, 1, 1); c.fill_preserve()
        c.set_source_rgb(0.75, 0.75, 0.8); c.set_line_width(3); c.stroke()
        T(c, "refund customer care no.", w / 2, 85, 24, (0.3, 0.3, 0.35), stroke=None, bold=False)
        for i, (ttl, num) in enumerate((("Refund Helpline 24x7", "98XXX XXXXX"), ("Customer Support", "70XXX XXXXX"),
                                         ("Care Number Free", "88XXX XXXXX"))):
            y = 150 + i * 150
            if i == 0 and hl:
                S.rrect(c, 16, y - 10, w - 32, 135, 16); c.set_source_rgb(1, 0.88, 0.88); c.fill()
            T(c, ttl, 40, y + 40, 28, (0.15, 0.3, 0.75), stroke=None, anchor="left")
            T(c, num, 40, y + 90, 32, (0.15, 0.15, 0.2), stroke=None, anchor="left")
    return f


def call_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.06, 0.07, 0.1); c.fill()
    T(c, "on call  03:12", w / 2, 120, 30, GREY, stroke=None, bold=False)
    c.arc(w / 2, 250, 80, 0, 6.283); c.set_source_rgb(0.3, 0.33, 0.42); c.fill()
    T(c, "'CUSTOMER CARE'", w / 2, 400, 34, WHITE, stroke=None)
    T(c, "98XXX XXXXX", w / 2, 450, 30, GREY, stroke=None, bold=False)
    c.arc(w / 2, h - 70, 40, 0, 6.283); c.set_source_rgb(0.9, 0.2, 0.2); c.fill()


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


def bubble(c, x, y, txt, a=1.0, size=40):
    w = len(txt) * size * 0.6 + 70
    S.rrect(c, x - w / 2, y, w, 92, 40); c.set_source_rgba(1, 1, 1, 0.96 * a); c.fill()
    T(c, txt, x, y + 62, size, (0.1, 0.1, 0.15), a, stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    hl = t > st + 2.4
    U.phone_frame(c, 690, 700, 340, 600, search_screen(hl), t - st, tilt=4)
    if hl:
        K.stamp(c, t, st + 2.4, "TOP RESULT", 300, 1180, YEL, 54, -0.05)
    if t > st + 5.2:
        K.stamp(c, t, st + 5.2, "SCAMMER'S NUMBER", 540, 1320, RED, 58, 0.03)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    a0 = k(t, st, st + 0.3)
    bubble(c, 540, 380, "'DOWNLOAD THIS APP...'", a0)
    bubble(c, 540, 490, "'...AND PAY ₹5 FEE'", k(t, st + 3.0, st + 3.3))
    for i, (lab, txt, d) in enumerate((("A", "SEND ₹5", 5.6), ("B", "HANG UP", 6.9))):
        a = k(t, st + d, st + d + 0.3)
        y = 640 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 118, 60, WHITE, a, stroke=None)
    K.stamp(c, t, st + 8.2, "COMMENT A or B", 540, 1180, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 400, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: HANG UP", 540, 495, 70, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 410, GRN, 54, 0.06)
    K.rows(c, t, st, [("KERALA POLICE WARNING", YEL, 54, 1.0), ("SCAMMERS POST", WHITE, 60, 2.4),
                      ("FAKE CUSTOMER CARE", RED, 66, 3.2), ("NUMBERS ONLINE", WHITE, 60, 4.0)], y0=700, gap=135)


def o_steal(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.8)
    U.phone_frame(c, 540, 760, 300, 520, call_screen, t - st, tilt=0)
    for i, (txt, col, d) in enumerate((("SCREEN-SHARING APP", YEL, 0.2), ("THEY SEE YOUR SCREEN", WHITE, 1.4),
                                       ("THEY READ YOUR OTP", WHITE, 2.4))):
        T(c, txt, 540, 420 + i * 80 - 40, 50, col, k(t, st + d, st + d + 0.25), lw=10)
    if t > st + 3.4:
        K.stamp(c, t, st + 3.4, "ACCOUNT: ₹0", 540, 1300, RED, 72, -0.04)


def o_tips(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("NUMBER ONLY FROM", WHITE, 60, 0.1), ("OFFICIAL APP / WEBSITE", YEL, 64, 0.8),
                      ("OTP, PIN: TO NOBODY", RED, 64, 2.8), ("SCAMMED? CALL", WHITE, 60, 4.6), ("1930", GRN, 130, 5.2),
                      ("cybercrime.gov.in", GREY, 44, 5.8)], y0=400, gap=150)


def o_end(c, t, lt):
    K.end_card(c, "GOOGLED A HELPLINE?", "USE THE OFFICIAL APP", YEL)
    st = sh.s(6)
    T(c, "SEND TO MUMMY-PAPA", 540, 1260, 60, YEL, k(t, st + 0.3, st + 0.6), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='flat', **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3, **ph), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.25), (1.78, 960, 540), (1.85, 960, 520), o_steal, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_tips, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 3.0, 6.0] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[1][0] + 4.0], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
