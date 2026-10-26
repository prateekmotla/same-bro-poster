import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import body as B  # noqa: E402
import env as V  # noqa: E402
import props as P  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s11_task"
CAPS = [
    "WhatsApp message: \"PART TIME JOB. Just like YouTube videos. ₹50 per like.\"",
    "Sid liked 3 videos. And yes, ₹150 actually came in.",
    "That's exactly where the TRAP starts.",
    "Then a Telegram group. Then a \"VIP TASK\". \"Deposit ₹2,000, get ₹3,000 back.\" And he did.",
    "Then bigger tasks. ₹10,000. ₹50,000. Now the money gets \"STUCK\". \"One more task and it's all released.\"",
    "Those small payouts were BAIT. Your own money returned to build TRUST.",
    "The government has blocked 100+ websites running these task scams. New groups pop up every day.",
    "Rule: a job that asks YOU for money is not a job. It's a SCAM. Defrauded? Call 1930 immediately.",
    "Send this to the friend who replies to \"work from home\" messages.",
]
HOOK = [("\"₹50 PER LIKE\"", YEL), ("JOB = SCAM", RED), ("HERE'S HOW", WHITE)]
SRC = "Cyber fraud helpline: 1930 · cybercrime.gov.in"
sh = None


def chat(msgs, title="Unknown +91 9xxxx", tg=False):
    def f(c, w, h, t):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.07, 0.1, 0.12) if not tg else c.set_source_rgb(0.09, 0.12, 0.17); c.fill()
        c.rectangle(0, 0, w, 130); c.set_source_rgb(0.1, 0.33, 0.28) if not tg else c.set_source_rgb(0.15, 0.32, 0.5); c.fill()
        T(c, title, w / 2, 85, 34, WHITE, stroke=None)
        y = 180
        for m, mine, col in msgs:
            bw = w * 0.8
            x = w - bw - 20 if mine else 20
            lines = m.split("|")
            bh = 30 + 50 * len(lines)
            S.rrect(c, x, y, bw, bh, 18); c.set_source_rgb(*((0.1, 0.4, 0.3) if mine else (0.17, 0.2, 0.24))); c.fill()
            for j, ln in enumerate(lines):
                T(c, ln, x + 24, y + 58 + j * 50, 32, col or WHITE, stroke=None, anchor="left")
            y += bh + 20
    return f


def room(c, t, lt, **kw):
    V.room(c, t, 'night')
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1, mouth='flat')
    d.update(kw)
    B.figure(c, 1000, 330, 0.5, t, **d)


def o_msg(c, t, lt):
    U.phone_frame(c, 240, 300, 600, 1060, chat([("Hi! PART TIME JOB|Like YouTube videos|₹50 per like", False, None)]), t, tilt=-2)


def o_paid(c, t, lt):
    U.phone_frame(c, 240, 300, 600, 1060, chat([("Task done: 3 likes", True, None), ("₹150 credited", False, GRN)]), t, tilt=2)


def o_trap(c, t, lt):
    U.dim(c, 0.5)
    P.stamp(c, "THE TRAP", 540, 950, sh.s(3) + 0.1, t, -6, RED, 120)


def o_vip(c, t, lt):
    U.phone_frame(c, 240, 300, 600, 1060, chat([("Welcome to VIP Earning Group", False, YEL),
                                                 ("Prepaid task: deposit ₹2,000|get ₹3,000 back", False, None),
                                                 ("₹3,000 credited", False, GRN)][:1 + int(3 * k(t, sh.s(4), sh.s(4) + 6))],
                                                title="VIP Tasks (Telegram)", tg=True), t, tilt=-2)


def o_stuck(c, t, lt):
    msgs = [("Task: ₹10,000", False, None), ("Task: ₹50,000", False, None), ("Withdrawal BLOCKED|Complete 1 more task", False, RED)]
    U.phone_frame(c, 240, 300, 600, 1060, chat(msgs[:1 + int(3 * k(t, sh.s(5), sh.s(5) + 5))], title="VIP Tasks (Telegram)", tg=True),
                  t, tilt=math.sin(t * 20) * 1.2 * k(t, sh.s(5) + 5, sh.s(5) + 5.5))


def o_bait(c, t, lt):
    U.dim(c, 0.8)
    T(c, "₹150 IN", 540, 560, 120, GRN, lw=14)
    T(c, "₹60,000 OUT", 540, 760, 120, RED, k(t, sh.s(6) + 1.5, sh.s(6) + 1.8), lw=14)
    T(c, "small payout = BAIT", 540, 920, 60, YEL, k(t, sh.s(6) + 3.0, sh.s(6) + 3.3))


def o_gov(c, t, lt):
    U.dim(c, 0.82)
    T(c, "100+", 540, 640, 260, YEL, lw=22)
    T(c, "SCAM SITES BLOCKED", 540, 760, 64, WHITE)
    T(c, "new groups: every day", 540, 900, 50, RED, k(t, sh.s(7) + 4.0, sh.s(7) + 4.3), stroke=None)


def o_rule(c, t, lt):
    U.dim(c, 0.6)
    S.rrect(c, 80, 420, 920, 620, 34); c.set_source_rgba(0.05, 0.06, 0.1, 0.94); c.fill()
    T(c, "JOB ASKS FOR MONEY?", 540, 540, 64, WHITE, stroke=None)
    T(c, "= SCAM", 540, 650, 100, RED, stroke=None)
    T(c, "Call", 540, 820, 56, WHITE, k(t, sh.s(8) + 3.0, sh.s(8) + 3.3), stroke=None)
    T(c, "1930", 540, 960, 140, GRN, k(t, sh.s(8) + 3.2, sh.s(8) + 3.5), stroke=None)


def o_end(c, t, lt):
    S.rrect(c, 140, 260, 800, 230, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    T(c, "SEND TO THE", 540, 360, 64, WHITE, stroke=None)
    T(c, "\"WFH JOB\" FRIEND", 540, 445, 66, YEL, stroke=None)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    r = lambda **kw: (lambda c, t, lt: room(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), r(mouth='o', eyes=1.1), (1.9, 1000, 480), (2.1, 1000, 450), o_msg, 'phone'),
        (s(2), s(3), r(mouth='bigsmile'), (1.9, 1000, 480), (2.0, 1000, 460), o_paid, 'warm'),
        (s(3), s(4), r(mouth='smile'), (2.3, 1000, 430), (2.1, 1000, 450), o_trap, 'red'),
        (s(4), s(5), r(mouth='smile'), (1.9, 1000, 480), (2.0, 1000, 460), o_vip, 'phone'),
        (s(5), s(6), r(mouth='grit', sweat=1, angry=0.4), (1.9, 1000, 480), (2.1, 1000, 440), o_stuck, 'red'),
        (s(6), s(7), r(mouth='frown', sad=1, tear=1), (1.78, 960, 540), (1.85, 960, 520), o_bait, 'night'),
        (s(7), s(8), r(mouth='frown'), (1.78, 960, 540), (1.85, 1000, 540), o_gov, 'night'),
        (s(8), s(9), r(mouth='flat'), (1.78, 960, 540), (1.82, 960, 540), o_rule, 'night'),
        (s(9), sh.dur + 1, r(mouth='smirk', phone=None, arms=((14, -10), (100, 40))), (1.9, 1000, 480), (2.1, 1000, 440), o_end, 'night'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview([1, 5, 9, 14, 18, 23, 27, 32, 36, 40, 44, 48, 50.5], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
