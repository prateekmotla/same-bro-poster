import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import body as B  # noqa: E402
import env as V  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/shorts/s12_reddot"
CAPS = [
    "Sid picks up his phone just to check the time. A RED DOT. Instagram: 3. WhatsApp: 55.",
    "20 minutes later, he doesn't even remember why he picked it up.",
    "That dot isn't red by accident.",
    "Red puts your brain on ALERT. Danger. Urgent. Look NOW.",
    "And the number? It's an UNFINISHED task. Your brain holds on to unfinished things until you clear them.",
    "So your finger moves on its own. Not a willpower problem. It's DESIGN. Apps sell your TIME.",
    "Change one setting: in notification settings, turn OFF badges for everything except essential apps.",
    "In 2 days you'll feel it. You'll pick up the phone less.",
    "Send this to the friend whose WhatsApp always shows 999+.",
]
HOOK = [("WHY APPS USE", WHITE), ("THE RED DOT", RED), ("ON YOU", YEL)]
SRC = None
sh = None
APPS = [("Insta", (0.85, 0.3, 0.55), "3"), ("WhatsApp", (0.15, 0.7, 0.35), "55"), ("YouTube", (0.9, 0.15, 0.15), "9"),
        ("Gmail", (0.9, 0.9, 0.92), "214"), ("Snap", (1, 0.9, 0.1), "12"), ("Shop", (0.2, 0.4, 0.9), "2"),
        ("X", (0.1, 0.1, 0.12), "20+"), ("Games", (0.6, 0.3, 0.9), "1"), ("News", (0.9, 0.5, 0.1), "7")]


def home(badges=1.0, gray=False):
    def f(c, w, h, t):
        g = c.set_source_rgb(0.12, 0.14, 0.25); c.rectangle(0, 0, w, h); c.fill()
        T(c, "9:41", w / 2, 160, 90, WHITE, stroke=None)
        for i, (name, col, n) in enumerate(APPS):
            x = 70 + (i % 3) * 165; y = 300 + (i // 3) * 210
            S.rrect(c, x, y, 120, 120, 30); c.set_source_rgb(*col); c.fill()
            T(c, name, x + 60, y + 160, 24, WHITE, stroke=None, bold=False)
            if badges > 0:
                sc = badges * (1 + 0.15 * math.sin(t * 6 + i))
                c.arc(x + 115, y + 8, 30 * sc, 0, 2 * math.pi); c.set_source_rgb(0.95, 0.15, 0.2); c.fill()
                T(c, n, x + 115, y + 20, 26 * sc, WHITE, stroke=None)
    return f


def room(c, t, lt, **kw):
    V.room(c, t, 'night')
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1, mouth='flat')
    d.update(kw)
    B.figure(c, 1000, 330, 0.5, t, **d)


def o_home(c, t, lt):
    U.phone_frame(c, 240, 300, 600, 1060, home(k(t, 2.0, 2.6)), t, tilt=-2)


def o_20(c, t, lt):
    U.dim(c, 0.6)
    T(c, "20 MIN LATER", 540, 700, 110, YEL, lw=14)
    T(c, "\"why did I pick it up?\"", 540, 860, 56, WHITE, k(t, sh.s(2) + 1.5, sh.s(2) + 1.8))


def o_dot(c, t, lt):
    U.dim(c, 0.85)
    r = 200 + 30 * math.sin(t * 5)
    c.arc(540, 760, r, 0, 2 * math.pi); c.set_source_rgb(0.95, 0.15, 0.2); c.fill()
    T(c, "1", 540, 830, 220, WHITE, stroke=None)


def o_alert(c, t, lt):
    o_dot(c, t, lt)
    for i, (w, t0) in enumerate((("DANGER", sh.s(4) + 1.8), ("URGENT", sh.s(4) + 2.6), ("LOOK NOW", sh.s(4) + 3.4))):
        T(c, w, 540, 380 + i * 0 if i == 0 else (1120 if i == 1 else 1240), 80, YEL if i < 2 else RED, k(t, t0, t0 + 0.2))


def o_loop(c, t, lt):
    U.dim(c, 0.85)
    T(c, "UNFINISHED TASK", 540, 420, 76, YEL)
    p = (t * 0.5) % 1
    c.set_line_width(30); c.set_source_rgb(*RED)
    c.arc(540, 760, 220, -math.pi / 2, -math.pi / 2 + 2 * math.pi * (0.75 + 0.2 * p)); c.stroke()
    T(c, "your brain won't", 540, 1080, 56, WHITE, k(t, sh.s(5) + 3, sh.s(5) + 3.3), stroke=None)
    T(c, "let it go", 540, 1150, 56, WHITE, k(t, sh.s(5) + 3.3, sh.s(5) + 3.6), stroke=None)


def o_design(c, t, lt):
    U.dim(c, 0.8)
    T(c, "NOT WILLPOWER", 540, 620, 86, WHITE, k(t, sh.s(6) + 2.0, sh.s(6) + 2.3))
    T(c, "DESIGN.", 540, 780, 150, RED, k(t, sh.s(6) + 3.5, sh.s(6) + 3.8), lw=16)
    T(c, "Apps sell your TIME", 540, 920, 56, YEL, k(t, sh.s(6) + 5.0, sh.s(6) + 5.3))


def o_setting(c, t, lt):
    def scr(c2, w, h, tt):
        c2.rectangle(0, 0, w, h); c2.set_source_rgb(0.95, 0.95, 0.97); c2.fill()
        T(c2, "Notifications", w / 2, 110, 44, (0.1, 0.1, 0.12), stroke=None)
        for i, (name, col, _) in enumerate(APPS[:7]):
            y = 200 + i * 110
            S.rrect(c2, 40, y, w - 80, 90, 16); c2.set_source_rgb(1, 1, 1); c2.fill()
            T(c2, f"{name} badges", 70, y + 58, 32, (0.1, 0.1, 0.12), stroke=None, anchor="left")
            on = i == 1 or tt < sh.s(7) + 2.0 + i * 0.4
            S.rrect(c2, w - 170, y + 20, 100, 50, 25); c2.set_source_rgb(*(GRN if on else (0.75, 0.75, 0.78))); c2.fill()
            c2.arc(w - 145 + (50 if on else 0), y + 45, 20, 0, 2 * math.pi); c2.set_source_rgb(1, 1, 1); c2.fill()
    U.phone_frame(c, 240, 300, 600, 1060, scr, t, tilt=0, glow=0.2)


def o_calm(c, t, lt):
    U.phone_frame(c, 240, 300, 600, 1060, home(0), t, tilt=2, glow=0.1)


def o_end(c, t, lt):
    S.rrect(c, 140, 260, 800, 230, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    T(c, "SEND TO THE", 540, 360, 64, WHITE, stroke=None)
    T(c, "999+ FRIEND", 540, 445, 76, YEL, stroke=None)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    s = sh.s
    r = lambda **kw: (lambda c, t, lt: room(c, t, lt, **kw))
    sh.shots = [
        (0, s(2), r(), (1.9, 1000, 480), (2.1, 1000, 450), o_home, 'phone'),
        (s(2), s(3), r(eyes=0.6, bags=1), (2.0, 1000, 470), (2.3, 1000, 430), o_20, 'night'),
        (s(3), s(4), r(), (1.78, 960, 540), (1.85, 960, 520), o_dot, 'red'),
        (s(4), s(5), r(), (1.78, 960, 540), (1.85, 960, 520), o_alert, 'red'),
        (s(5), s(6), r(), (1.78, 960, 540), (1.85, 1000, 540), o_loop, 'night'),
        (s(6), s(7), r(), (1.78, 960, 540), (1.85, 960, 540), o_design, 'night'),
        (s(7), s(8), r(), (1.9, 1000, 480), (2.0, 1000, 460), o_setting, 'phone'),
        (s(8), s(9), r(mouth='smile'), (1.9, 1000, 480), (2.0, 1000, 460), o_calm, 'morning'),
        (s(9), sh.dur + 1, r(mouth='smirk', phone=None, arms=((14, -10), (100, 40))), (1.9, 1000, 480), (2.1, 1000, 440), o_end, 'night'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        sh.preview([1, 5, 8, 12, 15, 19, 24, 28, 32, 36, 40, 44], f"{D}/prev.png")
    else:
        sh.render(f"{D}/short.mp4")
