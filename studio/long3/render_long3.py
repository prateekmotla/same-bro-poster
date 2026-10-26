"""Same Bro LONG 03 — Salary Aate Hi Khatam: where your money really goes."""
import json
import math
import random
import sys
import wave

import numpy as np
from PIL import Image

sys.path.insert(0, "/home/claude/sid/long1")
import render_long as R  # noqa: E402
import body as B  # noqa: E402
import env as V  # noqa: E402
import props as P  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, YEL, RED, GRN, WHITE  # noqa: E402

D = "/home/claude/sid/long3"
FPS = R.FPS
L = [None] + json.load(open(f"{D}/lines.json"))
R.L = L
with wave.open(f"{D}/vo16.wav") as wv:
    _a = np.frombuffer(wv.readframes(wv.getnframes()), np.int16).astype(np.float32) / 32768
_hop = 16000 // FPS
_e = np.array([np.sqrt((_a[i:i + _hop] ** 2).mean() + 1e-12) for i in range(0, len(_a), _hop)])
R._env = np.convolve(np.clip((20 * np.log10(_e + 1e-9) + 45) / 30, 0, 1), [0.25, 0.5, 0.25], mode="same")
DUR = 168.0


def s(n):
    return L[n][0]


# balance over the story (time -> rupees)
BAL = [(0, 35000), (s(6) + 3.5, 31000), (s(7) + 3.5, 28000), (s(8) + 2.5, 27700), (s(8) + 4.5, 27100), (s(9) + 3, 26900),
       (s(10) + 2, 25400), (s(11) + 4, 20000), (s(12) - 0.5, 800)]


def balance(t):
    if t < s(6):
        return 35000 if t < s(3) else 800
    return int(np.interp(t, [b[0] for b in BAL], [b[1] for b in BAL]))


def meter(c, t, x=1380, y=100):
    v = balance(t)
    S.rrect(c, x, y, 360, 130, 24); c.set_source_rgba(0.04, 0.05, 0.08, 0.88); c.fill()
    T(c, "BALANCE", x + 180, y + 42, 26, (0.75, 0.78, 0.88), stroke=None)
    T(c, f"₹{v:,}", x + 180, y + 105, 56, GRN if v > 15000 else (YEL if v > 5000 else RED), stroke=None)


def minus(c, t, t0, txt, x, y):
    if t0 <= t < t0 + 1.6:
        a = 1 - (t - t0) / 1.6
        T(c, txt, x, y - (t - t0) * 80, 64, RED, a, lw=8)


def sms(amount_txt, title="BANK", body="Salary credited"):
    def f(c, w, h, t):
        U.scr_fill(c, w, h, (0.95, 0.96, 0.98))
        T(c, "Messages", w / 2, 90, 30, (0.1, 0.1, 0.12), stroke=None)
        S.rrect(c, 24, 160, w - 48, 220, 24); c.set_source_rgb(0.88, 0.9, 0.95); c.fill()
        T(c, title, 50, 210, 24, (0.2, 0.3, 0.6), stroke=None, anchor="left")
        T(c, body, 50, 260, 30, (0.1, 0.1, 0.12), stroke=None, anchor="left")
        T(c, amount_txt, 50, 335, 56, (0.1, 0.55, 0.3), stroke=None, anchor="left")
    return f


# ---------------- shots ----------------
def sh_salary(c, t, lt):
    V.room(c, t, 'day')
    B.figure(c, 760, 330, 0.5, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=0.3, mouth='o', eyes=1.2)
    U.phone_frame(c, 1180, 120, 420, 760, sms("₹35,000"), t, tilt=4, glow=0.2)
    T(c, "1st", 380, 260, 120, YEL)
    return 'morning'


def sh_happy(c, t, lt):
    V.room(c, t, 'day')
    B.figure(c, 960, 300, 0.6, t, pose='stand', mouth='bigsmile', arms=((70, 120), (70, 120)), blush=0.5)
    T(c, "\"This month: SAVINGS pakka\"", 960, 160, 64, WHITE, k(t, s(2) + 0.8, s(2) + 1.1))
    meter(c, t)
    return 'morning'


def sh_day20(c, t, lt):
    V.room(c, t, 'night')
    B.figure(c, 700, 330, 0.5, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1, mouth='frown', sad=1, sweat=0.6)
    c.save(); c.translate(1500, 450)
    S.rrect(c, -170, -190, 340, 380, 26); c.set_source_rgb(0.97, 0.97, 0.98); c.fill()
    S.rrect(c, -170, -190, 340, 100, 26); c.set_source_rgb(*RED); c.fill()
    T(c, "DATE", 0, -125, 40, WHITE, stroke=None)
    T(c, "20", 0, 110, 200, (0.1, 0.1, 0.12), stroke=None)
    c.restore()
    meter(c, t, 1320, 750)
    if t > s(3) + 3.5:
        S.rrect(c, 120, 160, 760, 150, 26); c.set_source_rgba(0.1, 0.4, 0.3, 0.95); c.fill()
        T(c, "\"bro, 2k milega? salary pe", 500, 225, 40, WHITE, stroke=None)
        T(c, "lauta dunga\"", 500, 280, 40, WHITE, stroke=None)
    return 'night'


def bucket(c, t, x, y, leak=1.0):
    c.save(); c.translate(x, y)
    c.move_to(-220, -200); c.line_to(220, -200); c.line_to(170, 220); c.line_to(-170, 220); c.close_path()
    c.set_source_rgb(0.75, 0.78, 0.85); c.fill()
    lvl = 0.7 - 0.5 * leak
    c.save(); c.move_to(-220, -200); c.line_to(220, -200); c.line_to(170, 220); c.line_to(-170, 220); c.close_path(); c.clip()
    c.rectangle(-240, 220 - 420 * lvl, 480, 420 * lvl); c.set_source_rgb(0.25, 0.75, 0.45); c.fill()
    c.restore()
    T(c, "₹", 0, 80, 160, (0.1, 0.35, 0.2), stroke=None)
    for i, hx in enumerate((-120, -40, 60, 130)):
        for j in range(4):
            ph = (t * 1.2 + j / 4 + i * 0.13) % 1
            c.arc(hx * 0.85, 225 + ph * 260, 12, 0, 2 * math.pi); c.set_source_rgba(0.25, 0.75, 0.45, 1 - ph); c.fill()
    c.restore()


def sh_leaks(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.7)
    bucket(c, t, 960, 500, k(t, s(4), s(5)))
    T(c, "Money doesn't vanish in a day.", 960, 120, 56, WHITE, k(t, s(4) + 2.5, s(4) + 2.8))
    T(c, "It LEAKS.", 960, 950 - 40, 90, YEL, k(t, s(4) + 4.8, s(4) + 5.1))
    return 'night'


def sh_where(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.5)
    c.save(); c.translate(960 + math.sin(t * 2) * 200, 520)
    c.arc(0, 0, 150, 0, 2 * math.pi); c.set_source_rgba(0.8, 0.9, 1, 0.25); c.fill_preserve()
    c.set_source_rgb(0.9, 0.9, 0.95); c.set_line_width(22); c.stroke()
    c.move_to(105, 105); c.line_to(260, 260); c.set_line_width(40); c.stroke()
    c.restore()
    T(c, "WHERE DID IT GO?", 960, 940 - 30, 90, YEL, k(t, s(5), s(5) + 0.3))
    return 'night'


def sh_party(c, t, lt):
    V.canteen(c, t)
    for i, (x, who) in enumerate(((560, 'friend'), (960, 'sid'), (1360, 'friend'))):
        B.figure(c, x, 340, 0.45, t + i, who=who, pose='stand', mouth='bigsmile', arms=((70, 120), (70, 120)))
    T(c, "WEEK 1", 400, 230, 90, YEL)
    minus(c, t, s(6) + 3.5, "−₹4,000", 960, 260)
    meter(c, t)
    return 'warm'


def sh_sneaker(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.55)

    def scr(c2, w, h, tt):
        U.scr_fill(c2, w, h, (0.97, 0.97, 0.99))
        c2.rectangle(0, 0, w, 120); c2.set_source_rgb(0.15, 0.35, 0.9); c2.fill()
        T(c2, "Checkout", w / 2, 82, 44, WHITE, stroke=None)
        c2.save(); c2.translate(w / 2, 330)
        c2.move_to(-170, 40); c2.curve_to(-150, -60, -40, -80, 20, -40); c2.line_to(170, 10); c2.line_to(170, 70); c2.line_to(-170, 70)
        c2.close_path(); c2.set_source_rgb(0.95, 0.25, 0.3); c2.fill()
        S.rrect(c2, -175, 60, 350, 30, 10); c2.set_source_rgb(1, 1, 1); c2.fill()
        c2.restore()
        T(c2, "₹18,000", w / 2, 520, 64, (0.1, 0.1, 0.12), stroke=None)
        S.rrect(c2, 30, 580, w - 60, 200, 20); c2.set_source_rgb(0.9, 1, 0.92); c2.fill()
        T(c2, "NO COST EMI", w / 2, 650, 48, (0.1, 0.55, 0.3), stroke=None)
        T(c2, "₹3,000 × 6 months", w / 2, 730, 42, (0.1, 0.1, 0.12), stroke=None)
    U.phone_frame(c, 690, 40, 540, 1000, scr, t, tilt=-2 + 2 * lt)
    minus(c, t, s(7) + 3.5, "−₹3,000/mo", 1500, 500)
    meter(c, t)
    return 'phone'


def order_card(c, x, y, title, amt, col):
    S.rrect(c, x, y, 460, 120, 22); c.set_source_rgb(0.97, 0.97, 0.98); c.fill()
    S.rrect(c, x, y, 18, 120, 8); c.set_source_rgb(*col); c.fill()
    T(c, title, x + 40, y + 52, 34, (0.1, 0.1, 0.12), stroke=None, anchor="left")
    T(c, amt, x + 40, y + 98, 30, RED, stroke=None, anchor="left")


def sh_zomato(c, t, lt):
    V.room(c, t, 'night')
    B.figure(c, 700, 330, 0.5, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1, mouth='flat', bags=0.6)
    T(c, "WEEK 2", 400, 230, 90, YEL)
    for i in range(3):
        if t > s(8) + 2.5 + i * 1.4:
            order_card(c, 1250, 300 + i * 150, ["Order delivered", "Order delivered", "Order delivered"][i],
                       ["Biryani  −₹300", "Burger  −₹300", "Pizza  −₹300"][i], (0.9, 0.2, 0.25))
    meter(c, t)
    return 'night'


def sh_blinkit(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.3)
    B.figure(c, 760, 330, 0.5, t, pose='sit', mouth='smile', arms=((40, 100), (40, 100)))
    for i, (lab, col) in enumerate((("CHIPS", (0.95, 0.75, 0.2)), ("COLD DRINK", (0.85, 0.15, 0.2)), ("ICE CREAM", (0.6, 0.85, 1.0)))):
        a = k(t, s(9) + 1.4 + i * 0.6, s(9) + 1.7 + i * 0.6)
        S.rrect(c, 1200, 250 + i * 180, 420, 140, 26); c.set_source_rgba(*col, a); c.fill()
        T(c, lab, 1410, 340 + i * 180, 44, (0.1, 0.1, 0.12), a, stroke=None)
    T(c, "11:47 PM craving", 440, 230, 60, YEL)
    minus(c, t, s(9) + 3.0, "−₹200", 1410, 230)
    meter(c, t)
    return 'night'


def sh_subs(c, t, lt):
    V.room(c, t, 'night'); U.dim(c, 0.6)
    T(c, "WEEK 3", 400, 230, 90, YEL)
    for i, (lab, amt) in enumerate((("Music Premium", "₹119/mo"), ("Video App", "₹499/mo"), ("Cloud Storage", "₹130/mo"))):
        a = k(t, s(10) + 0.8 + i * 0.5, s(10) + 1.1 + i * 0.5)
        S.rrect(c, 560, 280 + i * 180, 800, 140, 24); c.set_source_rgba(0.97, 0.97, 0.98, a); c.fill()
        T(c, lab, 600, 365 + i * 180, 46, (0.1, 0.1, 0.12), a, stroke=None, anchor="left")
        T(c, amt, 1330, 365 + i * 180, 46, RED, a, stroke=None, anchor="right")
        if i > 0 and t > s(10) + 2.4:
            T(c, "?", 1420, 380 + i * 180, 110, YEL)
    meter(c, t)
    return 'night'


def sh_upi_walk(c, t, lt):
    V.street(c, t, (t - s(11)) * 130, night=False)
    B.figure(c, 760, 330, 0.55, t, pose='walk', ph=(t - s(11)) * 0.9, mouth='flat', phone=1, arms=((14, -10), (30, 150)))
    for i, (lab, t0) in enumerate((("chai −₹20", 1.0), ("auto −₹60", 1.8), ("cold coffee −₹120", 2.6), ("scan −₹50", 4.5),
                                   ("scan −₹100", 5.3))):
        minus(c, t, s(11) + t0, lab, 1200 + (i % 2) * 300, 420 + (i % 3) * 60)
    meter(c, t)
    return 'day'


def sh_cash_vs_upi(c, t, lt):
    V.studio(c, t); U.dim(c, 0.8)
    c.rectangle(955, 0, 10, 1080); c.set_source_rgb(1, 1, 1); c.fill()
    T(c, "CASH", 480, 180, 80, WHITE)
    T(c, "UPI", 1440, 180, 80, WHITE)
    for i in range(4):
        x = 330 + i * 40
        S.rrect(c, x, 420 + i * 8, 260, 130, 10); c.set_source_rgb(0.55, 0.75, 0.55); c.fill()
        T(c, "₹500", x + 130, 505 + i * 8, 44, (0.15, 0.3, 0.15), stroke=None)
    T(c, "you SEE it go", 480, 760, 56, YEL, k(t, s(12) + 2.5, s(12) + 2.8))
    T(c, "it HURTS a little", 480, 840, 50, RED, k(t, s(12) + 4.5, s(12) + 4.8))
    if t > s(13):
        c.arc(1440, 500, 130, 0, 2 * math.pi); c.set_source_rgb(0.2, 0.5, 1); c.fill()
        T(c, "TAP", 1440, 525, 64, WHITE, stroke=None)
        T(c, "no pain. no sight.", 1440, 780, 54, YEL, k(t, s(13) + 0.5, s(13) + 0.8))
    return 'studio'


def sh_upidata(c, t, lt):
    V.studio(c, t); U.dim(c, 0.85)
    T(c, "UPI · H2 2024 vs H2 2023", 960, 140, 50, (0.8, 0.82, 0.9), stroke=None)
    U.bar(c, 300, 330, 1300, 90, 0.6 * k(t, s(14) + 2.5, s(14) + 3.5), (0.5, 0.52, 0.6), "Average UPI payment (H2 2023)", "₹1,515")
    U.bar(c, 300, 560, 1300, 90, 0.553 * k(t, s(14) + 3.5, s(14) + 4.5), YEL, "Average UPI payment (H2 2024)", "₹1,396")
    U.bar(c, 300, 790, 1300, 90, 0.248 * k(t, s(14) + 5.5, s(14) + 6.5), RED, "Average payment at shops (P2M)", "₹627")
    return 'night'


def sh_many_small(c, t, lt):
    V.studio(c, t); U.dim(c, 0.82)
    rnd = random.Random(3)
    n = int(80 * k(t, s(15) + 1.0, s(15) + 3.5))
    for i in range(n):
        P.coin(c, rnd.uniform(200, 1720), rnd.uniform(300, 900), rnd.uniform(14, 30))
    T(c, "FEWER big spends", 960, 160, 70, WHITE)
    T(c, "MANY small ones", 960, 1000 - 40, 80, YEL, k(t, s(15) + 1.5, s(15) + 1.8))
    return 'warm'


def sh_math(c, t, lt):
    V.studio(c, t); U.dim(c, 0.85)
    T(c, "₹250 / day", 960, 300, 130, WHITE, k(t, s(16) + 1.5, s(16) + 1.8))
    if t > s(17):
        T(c, "= ₹7,500 / month", 960, 500, 100, YEL, k(t, s(17), s(17) + 0.3))
    if t > s(17) + 1.6:
        v = int(90000 * k(t, s(17) + 1.6, s(17) + 3.0))
        T(c, f"= ₹{v:,} / year", 960, 720, 130, RED, lw=14)
    if t > s(18) + 1.3:
        T(c, "on chai · snacks · delivery", 960, 900, 56, WHITE, k(t, s(18) + 1.3, s(18) + 1.6), stroke=None)
    return 'red'


def sh_emi(c, t, lt):
    V.studio(c, t); U.dim(c, 0.85)
    T(c, "YOUR SALARY", 960, 220, 70, WHITE)
    S.rrect(c, 260, 300, 1400, 150, 24); c.set_source_rgb(*GRN); c.fill()
    T(c, "₹35,000", 960, 400, 70, (0.05, 0.2, 0.1), stroke=None)
    x = 260
    for i, (lab, amt) in enumerate((("Sneakers EMI", 3000), ("Phone EMI", 5000), ("Bike EMI", 6000), ("Laptop EMI", 4000))):
        a = k(t, s(19) + 3.5 + i * 0.6, s(19) + 3.8 + i * 0.6)
        w = 1400 * amt / 35000
        S.rrect(c, x, 300, w * a, 150, 10); c.set_source_rgb(*RED); c.fill()
        T(c, lab, x + w / 2, 520 + (i % 2) * 50, 32, RED, a, stroke=None)
        x += w
    T(c, "half gone BEFORE the month starts", 960, 800, 60, YEL, k(t, s(19) + 6.0, s(19) + 6.3))
    return 'red'


def sh_order(c, t, lt):
    V.studio(c, t); U.dim(c, 0.85)
    T(c, "WHAT WE DO", 960, 160, 64, WHITE)
    for i, (lab, col) in enumerate((("SALARY", GRN), ("SPEND", RED), ("SAVE what's left", (0.5, 0.5, 0.55)))):
        a = k(t, s(20) + 1.0 + i * 1.2, s(20) + 1.3 + i * 1.2)
        S.rrect(c, 560, 240 + i * 200, 800, 150, 26); c.set_source_rgba(*col, a); c.fill()
        T(c, lab, 960, 335 + i * 200, 56, WHITE, a, stroke=None)
    if t > s(20) + 6.5:
        T(c, "= ₹0", 1500, 640, 120, RED, k(t, s(20) + 6.5, s(20) + 6.8))
    return 'night'


RULES = [("PAY YOURSELF FIRST", "save on salary day"), ("2 ACCOUNTS", "spend only the 2nd"), ("24-HOUR RULE", "for every \"want\""),
         ("CHECK UPI STATEMENT", "once a month"), ("EMI = NEEDS ONLY", "never for wants")]


def sh_rules(c, t, lt):
    V.studio(c, t); U.dim(c, 0.8)
    T(c, "5 SIMPLE RULES", 960, 200, 100, YEL, k(t, s(21), s(21) + 0.3))
    for i, (a, b) in enumerate(RULES):
        U.icon_card(c, 110 + i * 350, 380, 320, 420, i + 1, a, b, k(t, s(21) + 0.6 + i * 0.25, s(21) + 1.0 + i * 0.25), col=GRN)
    return 'studio'


def sh_rule(c, t, lt, n):
    V.room(c, t, 'day')
    B.figure(c, 600, 330, 0.5, t, pose='sit', mouth='smile', phone=1, arms=((14, -10), (30, 150)), glow=0.2)
    S.rrect(c, 1000, 160, 820, 640, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.92); c.fill()
    c.arc(1090, 250, 46, 0, 2 * math.pi); c.set_source_rgb(*GRN); c.fill()
    T(c, str(n + 1), 1090, 268, 52, (0.05, 0.05, 0.05), stroke=None)
    T(c, RULES[n][0], 1160, 268, 46, WHITE, stroke=None, anchor="left")
    st = s(22 + n)
    if n == 0:
        S.rrect(c, 1080, 360, 660, 100, 20); c.set_source_rgb(*GRN); c.fill()
        T(c, "Salary ₹35,000", 1410, 425, 44, (0.05, 0.2, 0.1), stroke=None)
        P.arrow(c, 1250, 480, 1250, 620, k(t, st + 1.5, st + 2.2), col=YEL)
        P.arrow(c, 1580, 480, 1580, 620, k(t, st + 2.5, st + 3.2), col=WHITE)
        T(c, "1. SAVE ₹5,000", 1250, 690, 38, YEL, k(t, st + 2.0, st + 2.3), stroke=None)
        T(c, "2. then spend", 1580, 690, 38, WHITE, k(t, st + 3.0, st + 3.3), stroke=None)
    elif n == 1:
        for i, (lab, col) in enumerate((("SAVINGS a/c", GRN), ("SPENDING a/c", YEL))):
            S.rrect(c, 1080 + i * 340, 380, 300, 260, 24); c.set_source_rgb(*col); c.fill()
            T(c, lab, 1230 + i * 340, 520, 36, (0.1, 0.1, 0.1), stroke=None)
        T(c, "card + UPI only on this", 1570, 700, 32, WHITE, k(t, st + 2.0, st + 2.3), stroke=None)
    elif n == 2:
        c.save(); c.translate(1410, 520)
        c.arc(0, 0, 170, 0, 2 * math.pi); c.set_source_rgb(0.97, 0.97, 0.98); c.fill()
        ang = (t - st) * 1.4
        c.move_to(0, 0); c.line_to(math.sin(ang) * 130, -math.cos(ang) * 130); c.set_source_rgb(*RED); c.set_line_width(10); c.stroke()
        c.restore()
        T(c, "WAIT 24 HOURS", 1410, 760, 46, YEL, stroke=None)
    elif n == 3:
        for i, (lab, amt) in enumerate((("Zomato", "₹4,200"), ("Blinkit", "₹2,900"), ("Chai/snacks", "₹3,100"), ("Auto", "₹1,800"))):
            a = k(t, st + 1.0 + i * 0.4, st + 1.3 + i * 0.4)
            T(c, lab, 1100, 420 + i * 90, 40, WHITE, a, stroke=None, anchor="left")
            T(c, amt, 1760, 420 + i * 90, 40, RED, a, stroke=None, anchor="right")
        T(c, "SHOCK!", 1410, 780, 56, YEL, k(t, st + 3.5, st + 3.8), stroke=None)
    else:
        T(c, "Fridge broke  ->  EMI ok", 1100, 450, 40, GRN, stroke=None, anchor="left")
        T(c, "New sneakers  ->  NO", 1100, 560, 40, RED, k(t, st + 1.8, st + 2.1), stroke=None, anchor="left")
    return 'morning'


def R_(n):
    return lambda c, t, lt: sh_rule(c, t, lt, n)


def sh_sip(c, t, lt):
    V.studio(c, t); U.dim(c, 0.88)
    T(c, "₹5,000 / month · 10 years · 12% (assumed)", 960, 120, 44, (0.8, 0.82, 0.9), stroke=None)
    p = k(t, s(27) + 2.0, s(27) + 8.5)
    x0, y0, w, h = 240, 900, 1440, 680

    def fv(n):
        r = 0.01
        return 5000 * ((1 + r) ** n - 1) / r * (1 + r)
    c.move_to(x0, y0)
    for i in range(1, int(120 * p) + 1):
        c.line_to(x0 + w * i / 120, y0 - h * fv(i) / 1.2e6)
    c.set_source_rgb(*GRN); c.set_line_width(12); c.stroke()
    c.move_to(x0, y0)
    c.line_to(x0 + w * p, y0 - h * 5000 * 120 * p / 1.2e6)
    c.set_source_rgb(0.6, 0.62, 0.7); c.set_line_width(8); c.stroke()
    if p > 0.95:
        T(c, "≈ ₹11.5 LAKH", 1500, 260, 80, GRN)
        T(c, "invested ₹6 LAKH", 1500, 560, 44, (0.8, 0.82, 0.9), stroke=None)
    if t > s(28):
        T(c, "the rest = COMPOUNDING", 960, 1000 - 40, 64, YEL, k(t, s(28) + 1.0, s(28) + 1.3))
    return 'money'


def sh_after(c, t, lt):
    V.room(c, t, 'day')
    B.figure(c, 700, 330, 0.5, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=0.2, mouth='bigsmile', blush=0.4)
    c.save(); c.translate(1450, 420)
    S.rrect(c, -170, -190, 340, 380, 26); c.set_source_rgb(0.97, 0.97, 0.98); c.fill()
    S.rrect(c, -170, -190, 340, 100, 26); c.set_source_rgb(*GRN); c.fill()
    T(c, "DATE", 0, -125, 40, WHITE, stroke=None)
    T(c, "20", 0, 110, 200, (0.1, 0.1, 0.12), stroke=None)
    c.restore()
    if t > s(29) + 4.5:
        S.rrect(c, 1270, 680, 360, 130, 24); c.set_source_rgba(0.04, 0.05, 0.08, 0.88); c.fill()
        T(c, "BALANCE", 1450, 722, 26, (0.75, 0.78, 0.88), stroke=None)
        T(c, "₹9,400", 1450, 785, 56, GRN, stroke=None)
    return 'morning'


def sh_end(c, t, lt):
    V.room(c, t, 'day'); U.dim(c, 0.35)
    B.figure(c, 960, 380, 0.72, t, pose='stand', mouth='smile', arms=((14, -10), (100, 40)), blush=0.3)
    S.rrect(c, 100, 200, 620, 200, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9); c.fill()
    T(c, "Your salary lasts", 410, 280, 40, WHITE, stroke=None)
    T(c, "till which DATE?", 410, 340, 44, YEL, stroke=None)
    S.rrect(c, 1200, 200, 620, 200, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9 * k(t, s(30) + 4.0, s(30) + 4.3)); c.fill()
    T(c, "SEND TO THE", 1510, 280, 44, WHITE, k(t, s(30) + 4.0, s(30) + 4.3), stroke=None)
    T(c, "20TH-DATE BORROWER", 1510, 345, 44, YEL, k(t, s(30) + 4.0, s(30) + 4.3), stroke=None)
    S.rrect(c, 820, 80, 280, 70, 35); c.set_source_rgb(0.06, 0.06, 0.08); c.fill_preserve()
    c.set_source_rgb(*YEL); c.set_line_width(4); c.stroke()
    T(c, "SAME BRO", 960, 128, 40, YEL, stroke=None)
    return 'end'


SHOTS = [
    (0.0, s(2), sh_salary, (1.0, 960, 540, 0), (1.15, 1100, 500, 0), 0),
    (s(2), s(3), sh_happy, (1.2, 960, 480, -2), (1.1, 960, 520, 2), 1),
    (s(3), s(4), sh_day20, (1.0, 960, 540, 0), (1.12, 1000, 520, 0), -1),
    (s(4), s(5), sh_leaks, (1.0, 960, 540, 0), (1.1, 960, 520, 0), 1),
    (s(5), s(6), sh_where, (1.1, 960, 540, 0), (1.0, 960, 540, 0), 0),
    (s(6), s(7), sh_party, (1.0, 960, 540, 0), (1.15, 960, 500, 0), 1),
    (s(7), s(8), sh_sneaker, (1.0, 960, 540, 0), (1.08, 1000, 540, 0), -1),
    (s(8), s(9), sh_zomato, (1.0, 960, 540, 0), (1.1, 1100, 520, 0), 1),
    (s(9), s(10), sh_blinkit, (1.05, 960, 540, 0), (1.15, 1100, 520, 0), -1),
    (s(10), s(11), sh_subs, (1.0, 960, 540, 0), (1.08, 960, 520, 0), 1),
    (s(11), s(12), sh_upi_walk, (1.15, 960, 560, 0), (1.15, 960, 560, 0), -1),
    (s(12), s(14), sh_cash_vs_upi, (1.0, 960, 540, 0), (1.05, 1100, 540, 0), 1),
    (s(14), s(15), sh_upidata, (1.0, 960, 540, 0), (1.04, 960, 560, 0), -1),
    (s(15), s(16), sh_many_small, (1.05, 960, 540, 0), (1.0, 960, 540, 0), 1),
    (s(16), s(19), sh_math, (1.0, 960, 540, 0), (1.06, 960, 540, 0), -1),
    (s(19), s(20), sh_emi, (1.0, 960, 540, 0), (1.05, 960, 520, 0), 1),
    (s(20), s(21), sh_order, (1.0, 960, 540, 0), (1.05, 1000, 520, 0), -1),
    (s(21), s(22), sh_rules, (1.0, 960, 560, 0), (1.0, 960, 540, 0), 1),
    (s(22), s(23), R_(0), (1.0, 960, 540, 0), (1.06, 1100, 520, 0), -1),
    (s(23), s(24), R_(1), (1.0, 960, 540, 0), (1.06, 1100, 520, 0), 1),
    (s(24), s(25), R_(2), (1.0, 960, 540, 0), (1.06, 1100, 520, 0), -1),
    (s(25), s(26), R_(3), (1.0, 960, 540, 0), (1.06, 1100, 520, 0), 1),
    (s(26), s(27), R_(4), (1.0, 960, 540, 0), (1.06, 1100, 520, 0), -1),
    (s(27), s(29), sh_sip, (1.0, 960, 540, 0), (1.04, 960, 540, 0), 1),
    (s(29), s(30), sh_after, (1.0, 960, 540, 0), (1.12, 1000, 520, 0), -1),
    (s(30), DUR, sh_end, (1.12, 960, 520, 0), (1.0, 960, 540, 0), 1),
]

CAPS_EN = [
    "1st of the month. Sid's phone: SALARY CREDITED. ₹35,000.",
    "Sid's happy. This month, SAVINGS for sure.",
    "20th of the month. Balance... ₹800. And Sid's texting a friend: \"bro, 2k? I'll return it on salary day.\"",
    "If this sounds familiar, listen. Money doesn't vanish in a day. It goes in small LEAKS.",
    "Let's see where Sid's money went.",
    "Week 1. Salary's in, so celebration. Party with friends: ₹4,000.",
    "Then new sneakers. \"NO COST EMI\", so it felt free. ₹3,000 a month for 6 months.",
    "Week 2. Back late from office, who's cooking? Zomato. ₹300. Next day again. And again.",
    "Late-night craving. Blinkit. Chips, cold drink, ice cream. Another ₹200.",
    "Week 3. Three subscriptions running. He doesn't even remember signing up for two.",
    "Daily chai, auto, cold coffee. Just ₹50, ₹100 each time. Scan on UPI, gone. Didn't even notice.",
    "That's the REAL problem. With cash, you SAW the money leave. It hurt a little.",
    "With UPI there's no pain, nothing to see. Just one TAP.",
    "The data says the same. In H2 2024, the average UPI payment got SMALLER. At shops, just ₹627.",
    "We're making fewer big spends, and MANY more small ones.",
    "Simple math. Just ₹250 a day in small spends.",
    "That's ₹7,500 a month. ₹90,000 a YEAR.",
    "₹90,000. On chai, snacks and delivery. Without even noticing.",
    "And the EMI trap. One EMI feels small. But 3-4 together, and half your salary's gone before it arrives.",
    "The problem isn't income. We put SAVING last. \"I'll save what's left.\" Nothing's ever left.",
    "So what's the fix? Five simple rules.",
    "1: PAY YOURSELF FIRST. On salary day, auto-transfer savings first. Then spend.",
    "2: A separate account for spending. What's in it is all you get that month.",
    "3: Before buying any \"want\", wait 24 HOURS. You'll forget half of them.",
    "4: Check your UPI STATEMENT once a month. Seriously. You'll shock yourself.",
    "5: EMI only for NEEDS. Never for wants.",
    "Example: if Sid invests just ₹5,000 a month for 10 years at an assumed 12%, it could grow to about ₹11.5 LAKH.",
    "He put in ₹6 lakh. COMPOUNDING made the rest.",
    "This month, for the first time, Sid moved ₹5,000 aside on salary day. Even on the 20th, there was money left.",
    "Comment: till which date does your salary last? Send this to the friend who borrows on the 20th every month.",
]
R.SHOTS = SHOTS
R.CAPS_EN = CAPS_EN


def disclaimer(c, t):
    if s(14) <= t <= s(15):
        txt = "Source: Worldline India Digital Payments Report (via Business Standard)"
    elif s(27) <= t <= s(29):
        txt = "Illustration with assumed returns · not financial advice"
    else:
        return
    S.rrect(c, 460, 18, 1000, 44, 22); c.set_source_rgba(0, 0, 0, 0.55); c.fill()
    T(c, txt, 960, 48, 22, (0.85, 0.87, 0.95), stroke=None, bold=False)


R.disclaimer = disclaimer
render_frame = R.render_frame

if __name__ == "__main__":
    import subprocess
    if sys.argv[1] != "full":
        for n, tt in enumerate(map(float, sys.argv[1].split(","))):
            Image.fromarray(render_frame(int(tt * FPS))).save(f"p_{n:02d}.png")
    else:
        a, b, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1920x1080",
                              "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                              "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
        for i in range(a, b):
            p.stdin.write(render_frame(i).tobytes())
        p.stdin.close(); p.wait()
