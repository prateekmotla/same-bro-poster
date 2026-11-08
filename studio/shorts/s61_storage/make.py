import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import tshort as TS  # noqa: E402,F401
import vtshort as VT  # noqa: E402
import kit as K  # noqa: E402
import trade as TR  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s61_storage"
CAPS = [
    "Guess: Google says 'Storage full. Get a plan.' But where did your free 15 GB go?",
    "Sid's Gmail: 'Storage full. You may stop getting new emails.' Shock. He never even used Drive!",
    "Truth: the free storage is ONE bucket. Gmail, Google Photos and Drive all eat from it.",
    "And since 2024, WhatsApp backups on Android count in it too. Those video-heavy groups? Yeah.",
    "So the bucket fills up... and the 'Upgrade' button shows up.",
    "Same bro? Saw 'storage full' and bought a plan without checking?",
    "Fix: open Google One's storage manager. Delete big files, old attachments, blurry photos. In WhatsApp backup, turn videos off.",
    "MORAL: Clean first. Then decide if you even need to pay.",
    "Send this to the friend whose Gmail is always full.",
]
HOOK = [("STORAGE FULL?", WHITE), ("WHERE DID", YEL), ("15 GB GO?", RED)]
SRC = "Source: Google One Help (15 GB shared); WhatsApp Help (2024)"
sh = None
BLUE = (0.26, 0.52, 0.96)
GPH = (0.98, 0.74, 0.02)
GML = (0.92, 0.26, 0.21)
GDR = (0.2, 0.66, 0.33)


def full_scr(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.98); c.fill()
    T(c, "Gmail", w / 2, 80, 40, (0.2, 0.2, 0.25), stroke=None)
    S.rrect(c, 30, 160, w - 60, 280, 20); c.set_source_rgb(1, 0.93, 0.92); c.fill()
    T(c, "Storage full", w / 2, 230, 42, GML, stroke=None)
    T(c, "You may stop getting", w / 2, 300, 30, (0.25, 0.25, 0.3), stroke=None)
    T(c, "new emails", w / 2, 345, 30, (0.25, 0.25, 0.3), stroke=None)
    S.rrect(c, 60, h - 160, w - 120, 90, 45); c.set_source_rgb(*BLUE); c.fill()
    T(c, "GET MORE STORAGE", w / 2, h - 102, 30, WHITE, stroke=None)


def bucket(c, t, st, show, y0=760):
    # one bar split into Gmail / Photos / Drive / WhatsApp
    x0, w, h = 140, 800, 120
    a = k(t, st + 0.1, st + 0.4)
    S.rrect(c, x0, y0, w, h, 20); c.set_source_rgba(1, 1, 1, 0.15 * a); c.fill()
    parts = [("GMAIL", GML, 0.22), ("PHOTOS", GPH, 0.38), ("DRIVE", GDR, 0.15), ("WHATSAPP", (0.15, 0.75, 0.4), 0.25)]
    x = x0
    for i, (lab, col, fr) in enumerate(parts[:show]):
        b = k(t, st + 0.8 + i * 0.9, st + 1.4 + i * 0.9)
        ww = w * fr * b
        c.rectangle(x, y0, ww, h); c.set_source_rgba(*col, 0.95); c.fill()
        if b > 0.5:
            T(c, lab, x + ww / 2, y0 + h + 60, 32 if lab != "WHATSAPP" else 28, col, b, lw=5)
        x += ww
    T(c, "15 GB", x0 + w / 2, y0 - 40, 56, WHITE, a, lw=8)


def rw(mode='night', **kw):
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


def o_guess(c, t, lt):
    st = sh.s(1)
    K.panel(c, 900, 420)
    K.rows(c, t, st, [("'STORAGE FULL. GET A PLAN.'", WHITE, 50, 0.4), ("WHERE DID 15 GB GO?", YEL, 60, 3.0)], y0=1030, gap=120)


def o_mail(c, t, lt):
    st = sh.s(2)
    U.phone_frame(c, 290, 520, 500, 820, full_scr, t - st, tilt=-2 + 3 * lt)
    K.stamp(c, t, st + 4.6, "NEVER USED DRIVE!", 540, 1300, RED, 52, -0.05)


def o_bucket(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "IT'S ONE BUCKET", 540, 430, 66, YEL, k(t, st + 0.1, st + 0.4), lw=8)
    bucket(c, t, st + 2.0, 3)


def o_wa(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "SINCE 2024 (ANDROID)", 540, 430, 56, GREY, k(t, st + 0.1, st + 0.4), lw=8)
    bucket(c, t, st - 2.0, 4)
    K.stamp(c, t, st + 4.0, "VIDEO GROUPS = GB GONE", 540, 1150, RED, 50, -0.03)


def o_upgrade(c, t, lt):
    st = sh.s(5)
    K.panel(c, 880, 460)
    T(c, "BUCKET FULL...", 540, 1010, 62, WHITE, k(t, st + 0.2, st + 0.5), stroke=None)
    a = k(t, st + 2.0, st + 2.4)
    S.rrect(c, 290, 1100, 500, 110, 55); c.set_source_rgba(*BLUE, a); c.fill()
    T(c, "UPGRADE", 540, 1175, 52, WHITE, a, stroke=None)


def o_same(c, t, lt):
    st = sh.s(6)
    K.panel(c, 880, 460)
    K.rows(c, t, st, [("SAW 'STORAGE FULL'", WHITE, 58, 0.4), ("AND JUST PAID?", YEL, 60, 2.0)], y0=1000, gap=110)
    K.stamp(c, t, st + 3.0, "SAME BRO?", 540, 1270, YEL, 60, -0.05)


def o_fix(c, t, lt):
    st = sh.s(7)
    K.panel(c, 800, 600)
    T(c, "THE FIX", 540, 880, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Google One >", WHITE, 46, 0.3, "left", 130),
                      ("    Storage manager", WHITE, 46, 0.3, "left", 130),
                      ("2. Delete big files, old", WHITE, 46, 3.0, "left", 130),
                      ("    attachments, blurry pics", WHITE, 46, 3.0, "left", 130),
                      ("3. WhatsApp backup: videos OFF", GRN, 42, 5.5, "left", 130)], y0=980, gap=80)


def o_moral(c, t, lt):
    TR.moral(c, t, sh.s(8), "CLEAN FIRST.", "THEN DECIDE TO PAY.", YEL)


def o_end(c, t, lt):
    K.end_card(c, "SEND TO THE FRIEND", "WHOSE GMAIL IS ALWAYS FULL", YEL)


def build():
    global sh
    sh = VT.VoicedText(D, CAPS, HOOK, [], SRC)
    sh.mood = 'chill'
    s = sh.s
    sh.shots = [
        (0, s(2), rw(mouth='o', eyes=1.3, phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 480), (2.1, 1000, 450), o_guess, 'night'),
        (s(2), s(3), rw(mouth='frown', squint=0.3, phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 480), (2.05, 1000, 455), o_mail, 'night'),
        (s(3), s(4), sw(mouth='flat'), (1.78, 960, 540), (1.85, 960, 520), o_bucket, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_wa, 'money'),
        (s(5), s(6), rw(mouth='smirk'), (1.9, 1000, 500), (2.0, 1000, 470), o_upgrade, 'night'),
        (s(6), s(7), rw('day', mouth='frown', phone=1, arms=((14, -10), (60, 120))), (1.9, 1000, 500), (2.0, 1000, 470), o_same, 'warm'),
        (s(7), s(8), rw('day', mouth='smile', arms=((60, 120), (14, -10))), (1.9, 1000, 500), (2.0, 1000, 480), o_fix, 'warm'),
        (s(8), s(9), sw(mouth='smile'), (1.78, 960, 540), (1.85, 960, 520), o_moral, 'studio'),
        (s(9), sh.dur + 1, rw('day', mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 500), (2.1, 1000, 470), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([1.2, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
