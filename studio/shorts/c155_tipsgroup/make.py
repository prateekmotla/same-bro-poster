"""SCAM OF THE WEEK #14: WhatsApp 'stock tips' group with fake profit screenshots (engine: vshort.Short).
Facts: SEBI press release, 22 Oct 2026 (Business Today, YourStory, Outlook Money): don't join invitation-only
WhatsApp groups run by unknown people / self-styled market experts, esp. overseas numbers; profit claims, praise and
trade confirmations by other members may be deliberately planted ('astroturfing'); don't open accounts on or send
money to apps/platforms recommended in such groups; a new number inviting you to a 'replacement' group after the old
one is shut = red flag; deal only with SEBI-registered intermediaries (check on SEBI's website). Cyber fraud helpline
1930. Not a trading tip short - scam awareness only. Education only, not financial advice."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c155_tipsgroup"
CAPS = [
    "An unknown number added you to a WhatsApp group. Members post PROFIT screenshots every day. Join in?",
    "Question: A: Everyone's earning, I'll put money too. B: It's a TRAP. Comment!",
    "Answer: B. In October 2026 SEBI warned: in such invite-only groups, the profit posts may be deliberately PLANTED.",
    "SEBI says: don't open accounts on the app they push, don't send money. Group shut and a new invite from a new number? Red flag too.",
    "Deal only with SEBI-registered people, check on SEBI's website. Got trapped? Call 1930.",
    "Has anyone added YOU to a group like this? Comment!",
]
HOOK = [("ADDED TO A 'PROFIT' GROUP?", WHITE), ("JOIN OR LEAVE?", YEL), ("SCAM OF THE WEEK #14", GREY)]
SRC = "SRC: SEBI press release, 22 Oct 2026"
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


def chat_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.92, 0.9, 0.85); c.fill()
    c.rectangle(0, 0, w, 120); c.set_source_rgb(0.08, 0.45, 0.38); c.fill()
    T(c, "PROFIT CLUB VIP", w / 2, 70, 32, WHITE, stroke=None)
    T(c, "+91 & overseas numbers", w / 2, 105, 20, (0.85, 0.95, 0.9), stroke=None, bold=False)
    msgs = [("Booked +Rs 48,000 today!", 0.4), ("Thank you sir, +32%!", 1.4), ("Screenshot: +Rs 1.2 lakh", 2.4),
            ("Join our app for VIP tips", 3.4)]
    for j, (m, d) in enumerate(msgs):
        if tt > d:
            y = 150 + j * 110
            S.rrect(c, 24, y, w - 70, 86, 16); c.set_source_rgb(1, 1, 1); c.fill()
            T(c, m, 30 + (w - 70) / 2, y + 54, 24, (0.1, 0.45, 0.2) if j < 3 else (0.8, 0.2, 0.1), stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 690, 720, 340, 600, chat_screen, t - st, tilt=4)
    if t > st + 4.6:
        K.stamp(c, t, st + 4.6, "JOIN IN?", 330, 1200, RED, 56, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "'EVERYONE IS EARNING!'", 540, 450, 56, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "PUT MONEY IN", 0.6), ("B", "IT'S A TRAP", 3.6))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 116, 52, WHITE, a, stroke=None)
    K.stamp(c, t, st + 4.6, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: IT'S A TRAP", 540, 478, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("SEBI WARNING, OCT 2026", YEL, 56, 1.0), ("INVITE-ONLY GROUPS", WHITE, 56, 4.5),
                      ("PROFIT POSTS", RED, 66, 6.5), ("MAY BE PLANTED", RED, 66, 7.6)], y0=700, gap=135)


def o_rules(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("DON'T OPEN THEIR APP", RED, 60, 0.6), ("DON'T SEND MONEY", RED, 60, 2.2),
                      ("NEW NUMBER,", WHITE, 56, 3.6), ("NEW INVITE?", WHITE, 56, 4.4), ("RED FLAG", RED, 76, 6.2)],
           y0=430, gap=150)


def o_check(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("ONLY SEBI-REGISTERED", GRN, 60, 0.3), ("CHECK ON SEBI'S WEBSITE", WHITE, 54, 1.6),
                      ("TRAPPED? CALL", WHITE, 56, 3.4), ("1930", YEL, 110, 4.0)], y0=470, gap=165)


def o_end(c, t, lt):
    K.end_card(c, "ADDED TO ONE TOO?", "COMMENT", YEL)
    T(c, "Education only, not financial advice", 540, 1200, 34, GREY, lw=6)


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
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_rules, 'studio'),
        (s(5), s(6), sw(mouth='smile', **ph), (1.78, 960, 540), (1.85, 960, 520), o_check, 'studio'),
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
