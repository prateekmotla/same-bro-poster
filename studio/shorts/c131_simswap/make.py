"""SCAM OF THE WEEK #11: phone suddenly shows NO NETWORK for hours = possible SIM swap (engine: vshort.Short).
Facts: SIM swap = fraudster gets a duplicate SIM issued on the victim's number (fake ID / social engineering); when the
duplicate is activated the original SIM stops working and OTPs go to the fraudster (Quick Heal advisory 2026). DoT
instructions (Nov 2022, TelecomTalk 15 Nov 2022 / Digit 17 Nov 2022): after a SIM swap / replacement, incoming AND
outgoing SMS on the new SIM are barred for 24 hours; the operator must notify the subscriber and confirm via IVRS, and
stop the swap if the subscriber rejects it. Advice: treat a sudden long loss of network as an emergency, call the
operator, ask the bank to block UPI / net banking, report at 1930 / cybercrime.gov.in. Voice take sped 1.1x."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c131_simswap"
CAPS = [
    "Since afternoon: NO NETWORK. Restarted the phone, still nothing. Must be a tower problem.",
    "Question: A: Wait till tomorrow. B: Get alert NOW, this could be a scam. Comment!",
    "Answer: B. This could be a SIM SWAP. A fraudster used a fake ID to get a duplicate of your SIM. Duplicate ON, your SIM OFF.",
    "Now your bank OTPs go to HIM. That's why a new SIM gets 24 hours of no SMS: a DoT rule.",
    "So if there's no network for long: call your operator NOW, and get the bank to block UPI and net banking.",
    "Got scammed? Call 1930. And if a SIM change call comes that you never asked for, say NO. Ever happened to you? Comment!",
]
HOOK = [("NO NETWORK FOR HOURS?", WHITE), ("WAIT IT OUT or ACT NOW?", YEL), ("SCAM OF THE WEEK #11", GREY)]
SRC = "SRC: DoT SIM swap rules (Nov 2022) + Quick Heal advisory"
sh = None


def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "evening")
        d = dict(pose='stand', mouth='flat', look=(0.6, 0)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def nonet_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.08, 0.09, 0.12); c.fill()
    for j in range(4):    # empty signal bars + cross
        c.rectangle(30 + j * 22, 60 - j * 10, 14, 14 + j * 10); c.set_source_rgba(1, 1, 1, 0.25); c.fill()
    T(c, "x", 135, 66, 36, RED, stroke=None)
    T(c, "NO SERVICE", w / 2, 200, 44, RED, stroke=None)
    T(c, "Emergency", w / 2, 270, 32, (0.7, 0.7, 0.75), stroke=None)
    T(c, "calls only", w / 2, 315, 32, (0.7, 0.7, 0.75), stroke=None)
    T(c, "since 2:14 PM", w / 2, 420, 34, WHITE, stroke=None)


def sim(c, x, y, s, label, col, a=1.0, off=False):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.move_to(-90, -120); c.line_to(50, -120); c.line_to(90, -80); c.line_to(90, 120); c.line_to(-90, 120); c.close_path()
    c.set_source_rgba(*col, a); c.fill()
    S.rrect(c, -50, -40, 100, 80, 12); c.set_source_rgba(0.95, 0.8, 0.3, a); c.fill()
    T(c, label, 0, 95, 30, WHITE, a, stroke=None)
    if off:
        c.move_to(-100, -130); c.line_to(100, 130); c.set_source_rgba(*RED, a); c.set_line_width(14); c.stroke()
    c.restore()


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 690, 740, 340, 560, nonet_screen, t - st, tilt=4)
    if t > st + 3.2:
        K.stamp(c, t, st + 3.2, "TOWER PROBLEM?", 320, 1200, YEL, 50, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "NO NETWORK FOR HOURS", 540, 450, 60, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, sz, d) in enumerate((("A", "WAIT TILL TOMORROW", 50, 1.0), ("B", "ACT NOW: MAYBE A SCAM", 46, 2.6))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 114, sz, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.0, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_swap(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 360, 860, 140, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: COULD BE SIM SWAP", 540, 450, 58, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 370, GRN, 50, 0.06)
    a1 = k(t, st + 2.4, st + 2.8)
    T(c, "FAKE ID > DUPLICATE SIM", 540, 600, 50, YEL, a1, lw=10)
    a2 = k(t, st + 5.2, st + 5.6)
    sim(c, 330, 850, 1.0, "YOURS", (0.2, 0.4, 0.8), a2, off=t > st + 6.4)
    sim(c, 750, 850, 1.0, "FRAUDSTER", (0.75, 0.2, 0.2), a2)
    if t > st + 6.4:
        K.stamp(c, t, st + 6.4, "YOUR SIM: DEAD", 540, 1160, RED, 56, -0.03)


def o_otp(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("YOUR BANK OTPs", WHITE, 66, 0.1), ("GO TO HIM", RED, 84, 1.0),
                      ("DoT RULE:", YEL, 60, 2.8), ("NEW SIM = NO SMS", WHITE, 62, 3.4), ("FOR 24 HOURS", GRN, 70, 4.2)],
           y0=440, gap=170)


def o_act(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("NO NETWORK FOR LONG?", WHITE, 60, 0.1), ("1. CALL YOUR OPERATOR", YEL, 58, 1.4),
                      ("2. CALL YOUR BANK", YEL, 58, 3.0), ("BLOCK UPI + NET BANKING", GRN, 54, 3.6)], y0=480, gap=180)


def o_end(c, t, lt):
    K.end_card(c, "SCAMMED? CALL", "1930", GRN)
    st = sh.s(6)
    T(c, "UNASKED SIM CHANGE CALL? SAY NO", 540, 1260, 44, YEL, k(t, st + 2.0, st + 2.3), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', eyes=1.2, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3, **ph), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='o', eyes=1.25), (1.78, 960, 540), (1.85, 960, 520), o_swap, 'studio'),
        (s(4), s(5), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_otp, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_act, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='flat', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
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
