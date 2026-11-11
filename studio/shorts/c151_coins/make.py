"""THEY'RE TRICKING YOU #12: cashback 'coins' are not money (engine: vshort.Short).
Facts: Flipkart SuperCoins Terms & Conditions (flipkart.com/pages/supercoins-tnc, read 11 Nov 2026): SuperCoins
cannot be converted to cash or used as cash equivalents; cannot be gifted or transferred; hold no monetary value;
expire 6 months from the date they are credited; Flipkart may modify, withdraw or terminate the feature at any time
without prior notice. Said in the voice as 'one big shopping app's own T&C' (generic coin art, no brand logo).
Brand-fair: we quote the app's own published terms, nothing more. Education only, not financial advice."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c151_coins"
CAPS = [
    "The order said Rs 100 CASHBACK. You got 100 coins. But are coins money?",
    "Question: A: Coins = cash, move it to the bank. B: Coins are NOT cash. Comment!",
    "Answer: B. One big shopping app's own T&C says: coins can't be turned into cash, can't be transferred, and have NO monetary value.",
    "And they EXPIRE in 6 months. The company can change or end the program without notice.",
    "So don't shop extra just for coins. Real cashback is the one that lands in your BANK account.",
    "How many of YOUR coins expired? Comment!",
]
HOOK = [("RS 100 CASHBACK?", WHITE), ("OR 100 COINS?", YEL), ("THEY'RE TRICKING YOU #12", GREY)]
SRC = "SRC: a major shopping app's coin T&C (Nov 2026)"
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


def coin(c, x, y, r, a=1.0):
    c.arc(x, y, r, 0, 6.283); c.set_source_rgba(0.98, 0.78, 0.15, a); c.fill()
    c.arc(x, y, r * 0.72, 0, 6.283); c.set_source_rgba(0.92, 0.62, 0.05, a); c.fill()
    T(c, "C", x, y + r * 0.35, int(r), (1, 0.92, 0.5), a, stroke=None)


def app_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.96, 0.97, 1.0); c.fill()
    c.rectangle(0, 0, w, 120); c.set_source_rgb(0.2, 0.35, 0.85); c.fill()
    T(c, "ORDER PLACED", w / 2, 85, 40, WHITE, stroke=None)
    T(c, "CASHBACK", w / 2, 220, 44, (0.1, 0.1, 0.12), stroke=None)
    T(c, "Rs 100", w / 2, 320, 96, (0.1, 0.55, 0.25), stroke=None)
    if tt > 2.5:
        S.rrect(c, 30, 380, w - 60, 150, 20); c.set_source_rgb(1, 0.95, 0.8); c.fill()
        coin(c, 100, 455, 46)
        T(c, "+100 COINS", w / 2 + 55, 470, 40, (0.6, 0.4, 0.0), stroke=None)
    T(c, "*credited as coins", w / 2, h - 60, 26, GREY, stroke=None, bold=False)


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 690, 720, 340, 600, app_screen, t - st, tilt=4)
    if t > st + 4.8:
        K.stamp(c, t, st + 4.8, "COINS = MONEY?", 330, 1200, RED, 56, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "100 COINS = RS 100?", 540, 450, 60, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "COINS = CASH", 0.6), ("B", "COINS ARE NOT CASH", 3.3))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 116, 50, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.4, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: NOT CASH", 540, 478, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("THE APP'S OWN T&C:", YEL, 56, 1.4), ("NO CASH CONVERSION", RED, 60, 3.8),
                      ("NO TRANSFER", RED, 60, 5.4), ("NO MONETARY VALUE", RED, 60, 6.6)], y0=700, gap=130)


def o_expire(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.86)
    for j in range(5):
        a = 1 - 0.8 * k(t, st + 1.0 + j * 0.25, st + 1.6 + j * 0.25)
        coin(c, 260 + j * 140, 470, 56, a)
    K.rows(c, t, st, [("EXPIRE IN 6 MONTHS", RED, 70, 0.6), ("PROGRAM CAN CHANGE", WHITE, 56, 2.8),
                      ("OR END WITHOUT NOTICE", WHITE, 56, 3.6)], y0=720, gap=150)


def o_bank(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("DON'T SHOP EXTRA", WHITE, 66, 0.1), ("JUST FOR COINS", YEL, 66, 1.0),
                      ("REAL CASHBACK =", WHITE, 60, 3.0), ("MONEY IN YOUR BANK", GRN, 66, 3.8)], y0=480, gap=160)


def o_end(c, t, lt):
    K.end_card(c, "COINS EXPIRED ON YOU?", "COMMENT", YEL)
    T(c, "HOW MANY?", 540, 1200, 56, WHITE, k(t, sh.s(6) + 0.8, sh.s(6) + 1.1), lw=8)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (40, 110)))
    sh.shots = [
        (0, s(2), w_room(mouth='smile', eyes=1.1, **ph), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3, **ph), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='o', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_expire, 'studio'),
        (s(5), s(6), sw(mouth='smile', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_bank, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', **ph), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
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
