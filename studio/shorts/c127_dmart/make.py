"""THEY'RE TRICKING YOU #9: 'DMart is cheap so the stuff must be bad' — the real reason it's cheaper (engine: vshort.Short).
Facts: Zerodha Daily Brief 'Here's how DMart works' (14 Jan 2025): "DMart owns most of its stores instead of renting
them", buys in bulk and pays suppliers quickly, follows the EDLC-EDLP (everyday low cost, everyday low price) model,
stocks fast-moving everyday essentials. Kotak Neo 'DMart's 500th store' (May 2026): DMart pays vendors in about 11 days
vs an industry norm of 30-60 days, rarely runs limited-period offers, limited disciplined range of fast-moving products.
Fair to the brand: no claim about product quality either way beyond 'cheap price != low quality'; plain text name, no
logo. Voice take sped 1.05x."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c127_dmart"
CAPS = [
    "Why is everything at DMart so cheap? The stuff must be low quality, right?",
    "Question: A: It's cheap because the quality is low. B: It's cheap because the business model is different. Comment!",
    "Answer: B. DMart doesn't rent most of its stores. It buys the land and builds them. So no huge monthly rent.",
    "It pays suppliers fast, in about 11 days, while the industry takes 30 to 60. In return it gets cheaper stock.",
    "And a limited range: only fast-selling stuff. No flashy sales, just low prices every day.",
    "So the saving is on rent, not on quality. Do YOU find DMart cheaper? Comment!",
]
HOOK = [("DMART SO CHEAP?", WHITE), ("BAD QUALITY or SMART MODEL?", YEL), ("THEY'RE TRICKING YOU #9", GREY)]
SRC = "SRC: Zerodha Daily Brief (Jan 2025), Kotak Neo (May 2026)"
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


def store(c, x, y, s, a=1.0, owned=None):
    c.save(); c.translate(x, y); c.scale(s, s)
    S.rrect(c, -260, -150, 520, 300, 16); c.set_source_rgba(0.92, 0.92, 0.88, a); c.fill()
    c.rectangle(-260, -150, 520, 70); c.set_source_rgba(0.1, 0.45, 0.25, a); c.fill()
    T(c, "SUPERMARKET", 0, -100, 40, WHITE, a, stroke=None)
    for j in range(3):
        c.rectangle(-220 + j * 160, -50, 120, 120); c.set_source_rgba(0.55, 0.75, 0.9, a); c.fill()
    c.restore()
    if owned is not None:
        S.rrect(c, x - 170 * s, y + 170 * s, 340 * s, 70 * s, 20); c.set_source_rgba(*(GRN if owned else RED), 0.95 * a); c.fill()
        T(c, "OWNED: NO RENT" if owned else "RENTED: PAYS RENT", x, y + 218 * s, 30 * s * 1.2, WHITE, a, stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 690, 740, 340, 560, K.bill_screen("BILL", [("Atta 5 kg", "LOW"), ("Oil 1 L", "LOW"),
                                                                ("Soap x4", "LOW")], "LOW!", btn="PAY"),
                  t - st, tilt=4)
    if t > st + 2.6:
        K.stamp(c, t, st + 2.6, "BAD QUALITY?", 330, 1200, RED, 52, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "WHY IS DMART CHEAPER?", 540, 450, 62, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, sz, d) in enumerate((("A", "LOW QUALITY", 60, 1.0), ("B", "DIFFERENT MODEL", 56, 3.4))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 610, y + 116, sz, WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.0, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_rent(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 360, 860, 140, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: DIFFERENT MODEL", 540, 450, 60, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 370, GRN, 50, 0.06)
    a1 = k(t, st + 1.2, st + 1.6)
    store(c, 300, 760, 0.85, a1, owned=False)
    a2 = k(t, st + 3.0, st + 3.4)
    store(c, 780, 760, 0.85, a2, owned=True)
    T(c, "OTHERS", 300, 610, 44, GREY, a1, stroke=None)
    T(c, "DMART", 780, 610, 44, YEL, a2, stroke=None)
    if t > st + 5.0:
        K.stamp(c, t, st + 5.0, "OWNS MOST STORES", 540, 1150, GRN, 56, -0.03)


def o_pay(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    T(c, "PAYS SUPPLIERS IN", 540, 430, 60, WHITE, k(t, st, st + 0.3), lw=10)
    for i, (lab, days, col, d, w) in enumerate((("DMART", "~11 DAYS", GRN, 0.8, 0.2), ("INDUSTRY", "30-60 DAYS", RED, 2.6, 1.0))):
        a = k(t, st + d, st + d + 0.4)
        y = 560 + i * 200
        T(c, lab, 260, y + 60, 46, WHITE, a, stroke=None)
        S.rrect(c, 420, y + 20, 560 * w * a + 1, 60, 20); c.set_source_rgba(*col, 0.95); c.fill()
        T(c, days, 420 + 560 * w * a + 10 if w < 0.5 else 700, y + 66, 40, WHITE if w > 0.5 else col, a, stroke=None,
          anchor="left" if w < 0.5 else "center")
    if t > st + 4.4:
        K.stamp(c, t, st + 4.4, "= CHEAPER STOCK", 540, 1100, YEL, 58, -0.03)


def o_range(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("LIMITED RANGE", WHITE, 70, 0.1), ("FAST-SELLING ONLY", YEL, 60, 1.2),
                      ("NO FLASHY SALES", WHITE, 64, 2.6), ("LOW PRICE EVERY DAY", GRN, 64, 3.6)], y0=480, gap=175)


def o_end(c, t, lt):
    K.end_card(c, "SAVING ON RENT,", "NOT ON QUALITY", GRN)
    st = sh.s(6)
    T(c, "CHEAPER FOR YOU?", 540, 1260, 54, YEL, k(t, st + 2.0, st + 2.3), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='o', eyes=1.2, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3, **ph), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_rent, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.25), (1.78, 960, 540), (1.85, 960, 520), o_pay, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_range, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 3.5] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
