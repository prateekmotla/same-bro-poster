"""RULES YOU DIDN'T KNOW #17: wrong / defective item but seller says 'no return' (engine: vshort.Short).
Facts: Consumer Protection (E-Commerce) Rules 2020, rule 6: no seller on an e-commerce entity shall refuse to take back
goods or refuse to refund if the goods are defective, deficient, spurious or not of the characteristics/features as
advertised or agreed (LiveLaw, 19 Mar 2026). A 'no return' policy can cover a change of mind, not defective/misdescribed
goods. Every e-commerce entity must have a grievance officer: acknowledge within 48 h, redress within one month.
Consumer Protection Act 2019 s.2(47): refusing to take back defective goods = unfair trade practice. National Consumer
Helpline 1915; e-filing at the consumer commission, no fee for claims up to Rs 5 lakh. Voice take sped 1.1x."""
import sys

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY, BLUE  # noqa: E402

D = "/home/claude/sid/shorts/c116_wrongitem"
CAPS = [
    "Opened your online order and it's the WRONG item. Seller says: 'Sorry, this is a no return product.'",
    "Question: do you get a refund now? A: No, it said no return. B: Yes, you do. Comment!",
    "Answer: B. The E-Commerce Rules 2020 say if the item is defective, wrong or not as advertised, the seller can't refuse to take it back and refund.",
    "'No return' only covers changing your mind, not a broken or wrong item. Every site must have a grievance officer who has to solve complaints within a month.",
    "Still ignored? National Consumer Helpline 1915. Then an online complaint at the consumer commission, free up to Rs 5 lakh.",
    "Next time, film the unboxing. That proof helps.",
]
HOOK = [("WRONG ITEM, 'NO RETURN'?", WHITE), ("YOU STILL GET A REFUND", GRN), ("RULES YOU DIDN'T KNOW #17", GREY)]
SRC = "SRC: Consumer Protection (E-Commerce) Rules 2020"
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


def o_hook(c, t, lt):
    st = sh.s(1)
    U.phone_frame(c, 690, 720, 340, 600, K.sms_screen("ORDER UPDATE", [("Wrong item", RED), ("Seller says:", WHITE),
                                                                      ("'No return", WHITE), ("product'", RED)]),
                  t - st, tilt=4)
    if t > st + 3.6:
        K.stamp(c, t, st + 3.6, "NO REFUND?!", 330, 1200, RED, 50, -0.05)


def o_choice(c, t, lt):
    st = sh.s(2)
    U.dim(c, 0.88)
    T(c, "WRONG ITEM, 'NO RETURN'", 540, 430, 58, WHITE, k(t, st, st + 0.2), lw=10)
    T(c, "REFUND OR NOT?", 540, 515, 58, YEL, k(t, st + 0.3, st + 0.5), lw=10)
    for i, (lab, txt, d) in enumerate((("A", "NO REFUND", 1.4), ("B", "YES, REFUND", 3.2))):
        a = k(t, st + d, st + d + 0.3)
        y = 620 + i * 230
        S.rrect(c, 110, y, 860, 190, 40); c.set_source_rgba(0.12, 0.13, 0.2, 0.95 * a); c.fill()
        c.arc(220, y + 95, 62, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
        T(c, lab, 220, y + 122, 80, (0.08, 0.08, 0.1), a, stroke=None)
        T(c, txt, 610, y + 118, 60, WHITE, a, stroke=None)
    K.stamp(c, t, st + 4.2, "COMMENT A or B", 540, 1160, YEL, 54, -0.03)


def o_reveal(c, t, lt):
    st = sh.s(3)
    U.dim(c, 0.88)
    S.rrect(c, 110, 380, 860, 150, 40); c.set_source_rgba(0.08, 0.35, 0.16, 0.95); c.fill()
    T(c, "B: YES, REFUND", 540, 478, 66, WHITE, stroke=None)
    K.stamp(c, t, st + 0.3, "RIGHT", 880, 390, GRN, 50, 0.06)
    K.rows(c, t, st, [("E-COMMERCE RULES 2020", YEL, 56, 0.9), ("DEFECTIVE / WRONG /", WHITE, 62, 2.6),
                      ("NOT AS ADVERTISED", WHITE, 62, 3.6), ("SELLER CAN'T REFUSE", RED, 70, 5.2), ("RETURN + REFUND", GRN, 70, 6.6)],
           y0=660, gap=115)


def o_policy(c, t, lt):
    st = sh.s(4)
    K.full(c, t, st, [("'NO RETURN' =", WHITE, 64, 0.1), ("ONLY CHANGE OF MIND", YEL, 64, 0.9),
                      ("NOT BROKEN / WRONG ITEM", RED, 58, 2.4), ("GRIEVANCE OFFICER", WHITE, 64, 4.6),
                      ("SOLVE IN 1 MONTH", GRN, 74, 6.6)], y0=420, gap=170)


def o_tips(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("STILL IGNORED?", WHITE, 64, 0.1), ("CONSUMER HELPLINE", YEL, 60, 1.6), ("1915", GRN, 130, 2.6),
                      ("THEN ONLINE COMPLAINT", WHITE, 56, 4.8), ("FREE UP TO ₹5 LAKH", GRN, 64, 7.0)], y0=400, gap=165)


def o_end(c, t, lt):
    K.end_card(c, "WRONG ITEM?", "REFUND IS YOUR RIGHT", YEL)
    st = sh.s(6)
    T(c, "TIP: FILM THE UNBOXING", 540, 1260, 54, YEL, k(t, st + 0.3, st + 0.6), lw=10)


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
        (s(3), s(4), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_reveal, 'studio'),
        (s(4), s(5), sw(mouth='o', eyes=1.25), (1.78, 960, 540), (1.85, 960, 520), o_policy, 'studio'),
        (s(5), s(6), sw(mouth='flat', arms=((14, -10), (100, 40))), (1.78, 960, 540), (1.85, 960, 520), o_tips, 'studio'),
        (s(6), sh.dur + 1, w_room(mouth='smile', arms=((14, -10), (100, 40))), (1.6, 960, 560), (1.7, 960, 540), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 5.5] + [a + (b - a) * 0.95 for a, b in L[1:]], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
