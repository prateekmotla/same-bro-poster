"""SCAM OF THE WEEK #12: 'You won a car in the online shopping lucky draw!' scratch card / letter (engine: vshort.Short).
Facts: Mumbai Police warning (Outlook, Nov 2021): fraudsters send 'online shopping lucky draw contest' offers, scratch
cards and letters in the name of reputed e-commerce firms, prizes Rs 1-10 lakh, then ask people to deposit an amount to
claim the prize. Telangana Cyber Security Bureau (ETV Bharat, Feb 2024): fake letters sent to home addresses, WhatsApp
'you won a car' messages, QR codes / card details asked; 'If someone asks for a token amount to claim any award then
it should be identified as a fraud'; reputed e-commerce companies never send OTPs or scratch cards or unknown gift
offers; don't click claim links. National cyber-fraud helpline 1930 / cybercrime.gov.in. Generic brand-free card.
Voice take sped 1.07x."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/c139_luckydraw"
CAPS = [
    "A letter came home. Scratched the card: 'Congratulations! You won a CAR in the online shopping lucky draw!'",
    "Question: A: Pay a small fee to claim the prize. B: It's a scam, ignore it. Comment!",
    "Answer: B. First the letter, then a WhatsApp message: 'Want the car? Pay the registration fee or tax first.'",
    "Pay once and they ask for more. The car never comes. Police say: asked to pay for a prize = fraud.",
    "Real companies don't send scratch cards or OTPs like this. Don't click the link, don't scan the QR.",
    "Got scammed? Call 1930. Ever got a letter like this? Comment! Show mummy-papa too.",
]
HOOK = [("YOU WON A CAR?!", WHITE), ("PAY THE FEE or IGNORE?", YEL), ("SCAM OF THE WEEK #12", GREY)]
SRC = "SRC: Mumbai Police + Telangana Cyber Security Bureau"
sh = None


def w_room(**kw):
    def f(c, t, lt):
        V.room(c, t, "day")
        d = dict(pose='stand', mouth='smile', look=(0.6, 0)); d.update(kw)
        K.sid(c, t, 960, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def card(c, x, y, s, scratched, a=1.0):
    c.save(); c.translate(x, y); c.scale(s, s); c.rotate(-0.04)
    S.rrect(c, -330, -220, 660, 440, 36); c.set_source_rgba(0.98, 0.85, 0.3, a); c.fill()
    S.rrect(c, -310, -200, 620, 400, 28); c.set_source_rgba(0.85, 0.2, 0.3, a); c.fill()
    T(c, "LUCKY DRAW", 0, -120, 56, WHITE, a, stroke=None)
    T(c, "SCRATCH & WIN", 0, -60, 34, YEL, a, stroke=None)
    S.rrect(c, -240, -20, 480, 170, 24)
    if scratched < 1:
        c.set_source_rgba(0.75, 0.75, 0.78, a); c.fill()
    S.rrect(c, -240, -20, 480 * scratched, 170, 24); c.set_source_rgba(1, 1, 1, a); c.fill()
    if scratched > 0.6:
        T(c, "YOU WON", 0, 45, 44, (0.1, 0.1, 0.15), a * min(1, (scratched - 0.6) / 0.3), stroke=None)
        T(c, "A CAR!", 0, 115, 64, RED, a * min(1, (scratched - 0.6) / 0.3), stroke=None)
    c.restore()


def wa_screen(c, w, h, tt):
    c.rectangle(0, 0, w, h); c.set_source_rgb(0.92, 0.9, 0.86); c.fill()
    c.rectangle(0, 0, w, 70); c.set_source_rgb(0.1, 0.4, 0.33); c.fill()
    T(c, "Prize Dept", w / 2, 48, 30, WHITE, stroke=None)
    for i, (txt, d) in enumerate((("Congrats! Car is", 0.3), ("ready for you.", 0.3), ("First pay the", 1.2),
                                  ("registration fee + tax", 1.2), ("to release it", 1.2))):
        a = k(tt, d, d + 0.3)
        T(c, txt, w / 2, 160 + i * 60, 27, (0.1, 0.1, 0.12), a, stroke=None)
    S.rrect(c, 40, 470, w - 80, 70, 20); c.set_source_rgba(0.1, 0.55, 0.3, k(tt, 2.2, 2.5)); c.fill()
    T(c, "PAY NOW", w / 2, 517, 32, WHITE, k(tt, 2.2, 2.5), stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    sc = min(1, max(0, (t - st - 1.2) / 1.6))
    card(c, 540, 930, 0.9, sc)
    if t > st + 3.4:
        K.stamp(c, t, st + 3.4, "REAL PRIZE?", 540, 1230, YEL, 54, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "'YOU WON A CAR' LETTER", 540, 450, 56, WHITE, k(t, st, st + 0.2), lw=10)
    for i, (lab, txt, sz, d) in enumerate((("A", "PAY A SMALL FEE", 52, 1.0), ("B", "SCAM. IGNORE IT", 52, 3.0))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 615, y + 114, sz, WHITE, a, stroke=None)
    K.stamp(c, t, st + 5.0, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_fee(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 300, 860, 130, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: IT'S A SCAM", 540, 385, 60, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 310, GRN, 50, 0.06)
    if t > st + 1.6:
        U.phone_frame(c, 380, 700, 320, 560, wa_screen, t - st - 1.6, tilt=-3)


def o_more(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("PAID ONCE?", WHITE, 64, 0.1), ("THEY ASK FOR MORE", RED, 66, 0.9),
                      ("THE CAR NEVER COMES", YEL, 58, 2.2), ("FEE FOR A PRIZE", WHITE, 60, 3.6), ("= FRAUD", RED, 84, 4.3)],
           y0=420, gap=170)


def o_rules(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("REAL COMPANIES DON'T", WHITE, 56, 0.1), ("SEND SCRATCH CARDS", YEL, 58, 0.8),
                      ("OR ASK FOR OTP", YEL, 58, 1.6), ("DON'T CLICK THE LINK", RED, 56, 3.2), ("DON'T SCAN THE QR", RED, 56, 4.2)],
           y0=430, gap=170)


def o_end(c, t, lt):
    K.end_card(c, "SCAMMED? CALL", "1930", GRN)
    st = sh.s(6)
    T(c, "SHOW THIS TO MUMMY-PAPA", 540, 1260, 48, YEL, k(t, st + 2.4, st + 2.7), lw=10)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'tense'
    s = sh.s
    sh.shots = [
        (0, s(2), w_room(mouth='o', eyes=1.25, arms=((100, 20), (100, 20))), (1.6, 960, 560), (1.75, 960, 540), o_hook, 'warm'),
        (s(2), s(3), sw(mouth='flat', squint=0.3), (1.78, 960, 540), (1.85, 960, 520), o_choice, 'studio'),
        (s(3), s(4), sw(mouth='flat', squint=0.4, phone=1, arms=((14, -10), (40, 110))), (1.78, 960, 540), (1.85, 960, 520), o_fee, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.2), (1.78, 960, 540), (1.85, 960, 520), o_more, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_rules, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='flat', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
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
