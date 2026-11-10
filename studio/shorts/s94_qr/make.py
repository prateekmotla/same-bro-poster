"""SCAM OF THE WEEK #5: fake QR sticker pasted over the real one at a petrol pump / shop (engine: vshort.Short).
Facts: Khajuraho & Chhatarpur, Madhya Pradesh (Jan 2025, India Today via Curly Tales 12 Jan 2025): QR codes at six
shops incl. petrol pumps were swapped overnight / pasted over; a customer noticed the payee name was not the shop's.
NPCI safety tips (Business Standard, 10 Jul 2025): 'Always check the recipient's name on your screen before
transferring money.' Report fraud: 1930 / cybercrime.gov.in."""
import math
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s94_qr"
CAPS = [
    "Filled petrol, scanned the QR at the counter, money gone. But the owner says: 'payment never came.'",
    "Someone stuck THEIR QR over the real one at night. It actually happened at petrol pumps and shops in Madhya Pradesh.",
    "After scanning, before you pay, what do you check? A: the amount. B: the NAME of who gets the money. Comment!",
    "B is right. NPCI says: check the receiver's name on screen before sending money. Not the shop's name? STOP.",
    "QR looks pasted on top? Ask. And if you get scammed, call 1930 right away.",
    "Next time you scan, READ THE NAME. Send this to your family.",
]
HOOK = [("SCANNED. PAID.", WHITE), ("PUMP GOT ₹0", RED), ("SCAM OF THE WEEK #5", GREY)]
SRC = "SRC: NPCI safety tips; MP QR swap case, Jan 2025"
sh = None


def qr(c, x, y, s, seed=1, a=1.0):
    c.save(); c.translate(x, y)
    c.rectangle(0, 0, s, s); c.set_source_rgba(1, 1, 1, a); c.fill()
    n = 15
    cs = s * 0.86 / n
    o = s * 0.07
    st = seed * 7 + 3
    for i in range(n):
        for j in range(n):
            st = (st * 1103515245 + 12345) & 0x7fffffff
            if (i < 5 and j < 5) or (i < 5 and j > n - 6) or (i > n - 6 and j < 5):
                continue
            if (st >> 8) % 2 == 0:
                c.rectangle(o + j * cs, o + i * cs, cs, cs); c.set_source_rgba(0.05, 0.05, 0.08, a); c.fill()
    for (i, j) in ((0, 0), (0, n - 5), (n - 5, 0)):
        for m, col in ((0, 0.05), (1, 1.0), (2, 0.05)):
            c.rectangle(o + (j + m * 0.8) * cs, o + (i + m * 0.8) * cs, (5 - 1.6 * m) * cs, (5 - 1.6 * m) * cs)
            c.set_source_rgba(col, col, col + 0.03, a); c.fill()
    c.restore()


def pump(c, t, fake_a=1.0):
    g = (0.82, 0.86, 0.9)
    c.rectangle(0, 0, 1920, 1080); c.set_source_rgb(*g); c.fill()
    c.rectangle(0, 0, 1920, 140); c.set_source_rgb(0.85, 0.2, 0.15); c.fill()
    T(c, "FUEL STATION", 1350, 100, 70, WHITE, stroke=None)
    c.rectangle(0, 860, 1920, 220); c.set_source_rgb(0.45, 0.45, 0.48); c.fill()
    # dispenser
    S.rrect(c, 300, 300, 260, 560, 20); c.set_source_rgb(0.95, 0.95, 0.95); c.fill()
    c.rectangle(330, 340, 200, 110); c.set_source_rgb(0.1, 0.12, 0.1); c.fill()
    T(c, "₹500.00", 430, 410, 44, (0.3, 1, 0.4), stroke=None)
    c.move_to(560, 520); c.curve_to(640, 560, 640, 760, 600, 820); c.set_source_rgb(0.1, 0.1, 0.1); c.set_line_width(16); c.stroke()
    # counter with QR stand
    c.rectangle(1250, 620, 520, 260); c.set_source_rgb(0.5, 0.33, 0.2); c.fill()
    S.rrect(c, 1400, 360, 240, 280, 14); c.set_source_rgb(0.2, 0.35, 0.75); c.fill()
    T(c, "SCAN & PAY", 1520, 400, 30, WHITE, stroke=None)
    qr(c, 1430, 420, 180, 1)
    if fake_a > 0:   # sticker pasted on top, slightly crooked
        c.save(); c.translate(1520, 510); c.rotate(0.06); c.translate(-90, -90)
        qr(c, 0, 0, 180, 9, fake_a)
        c.rectangle(-4, -4, 188, 188); c.set_source_rgba(0.9, 0.9, 0.8, 0.6 * fake_a); c.set_line_width(4); c.stroke()
        c.restore()


def pay_screen(name, ok):
    def f(c, w, h, tt):
        c.rectangle(0, 0, w, h); c.set_source_rgb(0.97, 0.97, 0.99); c.fill()
        c.rectangle(0, 0, w, 120); c.set_source_rgb(0.2, 0.25, 0.55); c.fill()
        T(c, "PAY", w / 2, 82, 40, WHITE, stroke=None)
        T(c, "Paying to", w / 2, 210, 30, (0.4, 0.4, 0.45), stroke=None, bold=False)
        S.rrect(c, 30, 240, w - 60, 100, 18); c.set_source_rgb(*((0.85, 1, 0.88) if ok else (1, 0.86, 0.86))); c.fill()
        T(c, name, w / 2, 305, 38, GRN if ok else RED, stroke=None)
        T(c, "₹500", w / 2, 450, 80, (0.1, 0.1, 0.12), stroke=None)
        S.rrect(c, 40, h - 110, w - 80, 80, 40); c.set_source_rgb(0.2, 0.25, 0.55); c.fill()
        T(c, "ENTER UPI PIN", w / 2, h - 57, 34, WHITE, stroke=None)
    return f


def w_pump(fake_a=1.0, **kw):
    def f(c, t, lt):
        pump(c, t, fake_a)
        d = dict(pose='stand', mouth='flat', look=(0.6, 0))
        d.update(kw)
        K.sid(c, t, 1050, 360, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def o_hook(c, t, lt):
    st = sh.s(1)
    if t > st + 3.4:
        a = k(t, st + 3.4, st + 3.7)
        S.rrect(c, 140, 560, 800, 110, 50); c.set_source_rgba(1, 1, 1, 0.96 * a); c.fill()
        T(c, "OWNER: 'PAYMENT NEVER CAME'", 540, 632, 42, (0.1, 0.1, 0.15), a, stroke=None)


def o_swap(c, t, lt):
    st = sh.s(2)
    K.stamp(c, t, st + 0.8, "FAKE QR PASTED ON TOP", 540, 560, RED, 54, -0.04)
    K.rows(c, t, st, [("REAL CASE:", WHITE, 50, 3.6), ("PUMPS & SHOPS, MP", YEL, 62, 4.4)], y0=1240, gap=95)


def o_choice(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    T(c, "BEFORE YOU PAY, CHECK?", 540, 470, 66, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "THE AMOUNT", 3.0), ("B", "THE PAYEE NAME", 3.9))):
        a = k(t, st + d, st + d + 0.3)
        y = 580 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 600, y + 112, 50, WHITE, a, stroke=None)
    K.stamp(c, t, st + 6.6, "COMMENT A or B", 540, 1120, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.88)
    S.rrect(c, 110, 400, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: THE PAYEE NAME", 540, 495, 60, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 860, 410, GRN, 54, 0.06)
    good = t < st + 4.6
    U.phone_frame(c, 330, 600, 420, 560, pay_screen("CITY FUEL STATION" if good else "Mr. X (personal)", good), t - st, tilt=1)
    if not good:
        K.stamp(c, t, st + 4.6, "NOT THE SHOP? STOP.", 540, 1260, RED, 56, -0.04)
    else:
        T(c, "NPCI: CHECK THE NAME FIRST", 540, 1260, 44, YEL, k(t, st + 1.0, st + 1.3), stroke=None)


def o_tips(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("QR LOOKS PASTED ON?", WHITE, 62, 0.1), ("ASK THE STAFF", YEL, 80, 1.0),
                      ("SCAMMED?", WHITE, 60, 2.4), ("CALL 1930", GRN, 120, 3.2), ("cybercrime.gov.in", GREY, 44, 3.6)],
           y0=470, gap=170)


def o_end(c, t, lt):
    K.end_card(c, "SCAN. THEN READ THE NAME.", "SEND THIS TO FAMILY.", YEL)
    st = sh.s(6)
    T(c, "A or B? COMMENT", 540, 1260, 64, YEL, k(t, st + 1.5, st + 1.8), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    ph = dict(phone=1, arms=((14, -10), (60, 120)))
    sh.shots = [
        (0, s(2), w_pump(1.0, mouth='o', eyes=1.2, **ph), (1.5, 1300, 520), (1.65, 1350, 500), o_hook, 'warm'),
        (s(2), s(3), w_pump(1.0, mouth='frown', angry=0.4), (1.9, 1500, 520), (2.3, 1520, 520), o_swap, 'red'),
        (s(3), s(4), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(4), s(5), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'money'),
        (s(5), s(6), sw(mouth='flat', angry=0.3), (1.78, 960, 540), (1.85, 960, 520), o_tips, 'studio'),
        (s(6), sh.dur + 1, w_pump(0.0, mouth='smile', arms=((14, -10), (100, 40))), (1.5, 1300, 520), (1.6, 1300, 500),
         o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 2.5, 5.0] + [a + (b - a) * 0.9 for a, b in L[1:]] + [L[3][0] + 2.0], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
