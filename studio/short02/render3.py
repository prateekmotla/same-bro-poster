"""Same Bro Short 02 — The Real Income of Live Traders. Shot-based renderer with camera rig + whip transitions."""
import math
import subprocess
import sys
import wave

import cairo
import numpy as np
from PIL import Image

sys.path.insert(0, "/home/claude/sid/v2")
sys.path.insert(0, "/home/claude/sid/v3")
import sid2 as S  # noqa: E402
import fx  # noqa: E402
import props as P  # noqa: E402
import chars as CH  # noqa: E402
from caps3 import CAPS  # noqa: E402

W, H, FPS = 1080, 1920, 30
DUR = 76.0
YEL, RED, GRN = P.YEL, P.RED, P.GRN
fx.GRADES['studio'] = dict(lift=(0.03, 0.0, 0.05), gain=(1.02, 0.95, 1.08), sat=1.05, vig=1.0, bloom=0.4)
fx.GRADES['red'] = dict(lift=(0.05, 0.0, 0.01), gain=(1.08, 0.9, 0.9), sat=0.95, vig=1.1, bloom=0.3)
fx.GRADES['money'] = dict(lift=(0.0, 0.03, 0.02), gain=(0.98, 1.05, 0.98), sat=1.05, vig=0.9, bloom=0.4)

# ---------- lip sync ----------
with wave.open("vo16.wav") as wv:
    _a = np.frombuffer(wv.readframes(wv.getnframes()), np.int16).astype(np.float32) / 32768
_hop = 16000 // FPS
_env = np.array([np.sqrt((_a[i:i + _hop] ** 2).mean() + 1e-12) for i in range(0, len(_a), _hop)])
_env = np.convolve(np.clip((20 * np.log10(_env + 1e-9) + 45) / 30, 0, 1), [0.25, 0.5, 0.25], mode="same")


def talk(t):
    i = int(t * FPS)
    return float(_env[i]) if 0 <= i < len(_env) else 0.0


def blink(t, base=1.0):
    d = (t * 1.0) % 3.4
    return base * abs(d - 0.065) / 0.065 if d < 0.13 else base


def E(t):
    return S.ease(t)


def k(t, a, b):
    return P.clamp((t - a) / (b - a))


# ---------- captions ----------
def caption(c, t):
    for txt, a, b in CAPS:
        if a - 0.04 <= t <= b + 0.08:
            kk = P.eob((t - a + 0.04) / 0.16)
            c.save()
            c.translate(W / 2, 1520)
            c.scale(0.8 + 0.2 * kk, 0.8 + 0.2 * kk)
            c.select_font_face("Poppins", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            size = 66
            c.set_font_size(size)
            ws = txt.split(" ")
            lines, cur = [], []
            for w in ws:
                if c.text_extents(" ".join(cur + [w])).x_advance > 920 and cur:
                    lines.append(cur); cur = [w]
                else:
                    cur.append(w)
            lines.append(cur)
            lh = size * 1.2
            y0 = -(len(lines) - 1) * lh / 2
            sp = c.text_extents("a a").x_advance - c.text_extents("aa").x_advance
            for i, ln in enumerate(lines):
                wd = [c.text_extents(w).x_advance for w in ln]
                x = -(sum(wd) + sp * (len(ln) - 1)) / 2
                for w, d in zip(ln, wd):
                    core = w.strip('".,:?!\'')
                    hi = (core.isupper() and len(core) > 1) or "₹" in w or "%" in w
                    c.move_to(x, y0 + i * lh)
                    c.text_path(w)
                    c.set_source_rgb(0.02, 0.02, 0.03)
                    c.set_line_width(15)
                    c.set_line_join(cairo.LINE_JOIN_ROUND)
                    c.stroke_preserve()
                    c.set_source_rgb(*(YEL if hi else (1, 1, 1)))
                    c.fill()
                    x += d + sp
            c.restore()
            return


def disclaimer(c, t):
    if 34.0 <= t <= 51.3 or t >= 71.0:
        a = min(1, (t - 34.0) / 0.4) if t < 40 else 1
        txt = "Example numbers for illustration · not about any specific person" if t < 60 else "Not financial advice · Data: SEBI F&O study FY25"
        S.rrect(c, 70, 118, 940, 54, 27)
        c.set_source_rgba(0, 0, 0, 0.55 * a)
        c.fill()
        P.text(c, txt, W / 2, 154, 27, fill=(0.85, 0.87, 0.95), stroke=None, alpha=a)


# ---------- reusable compositions ----------
def bhai_medium(c, t, x=540, y=780, s=1.45, tilt=0, mouth='smile', tk=None, arms=((12, -8), (12, -8)), **e):
    CH.bhai_body(c, x, y, s, t, arms=arms)
    CH.bhai_head(c, x, y + math.sin(t * 1.9) * -3, s, t, tilt=tilt, mouth=mouth,
                 talk=talk(t) if tk is None else tk, **e)


def sid_medium(c, t, x=540, y=780, s=1.45, tilt=0, arms=((14, -10), (14, -10)), phone=None, glow=0, **e):
    CH.sid_body(c, x, y, s, t, arms=arms, phone_hand=phone, glow=glow)
    e.setdefault('eyes', 1.0)
    e['eyes'] = blink(t, e['eyes'])
    if 'raise_' in e:
        e['raise'] = e.pop('raise_')
    CH.sid_head(c, x, y + math.sin(t * 1.8) * -3, s, t, tilt=tilt, glow=glow, **e)


def sid_face(c, t, x, y, s, tilt=0, **e):
    e.setdefault('eyes', 1.0)
    e['eyes'] = blink(t, e['eyes'])
    if 'raise_' in e:
        e['raise'] = e.pop('raise_')
    CH.sid_head(c, x, y, s, t, tilt=tilt, **e)


def burst(c, x, y, r, n, col, rot=0.0, a=1.0):
    c.save()
    c.translate(x, y)
    c.rotate(rot)
    for i in range(n * 2):
        ang = math.pi * i / n
        rr = r if i % 2 == 0 else r * 0.62
        (c.move_to if i == 0 else c.line_to)(math.cos(ang) * rr, math.sin(ang) * rr)
    c.close_path()
    c.set_source_rgba(*col, a)
    c.fill_preserve()
    c.set_source_rgba(0, 0, 0, a)
    c.set_line_width(10)
    c.stroke()
    c.restore()


def broker_box(c, x, y, s=1.0, label="BROKER"):
    c.save()
    c.translate(x, y)
    c.scale(s, s)
    c.move_to(-170, -90); c.line_to(0, -190); c.line_to(170, -90); c.close_path()
    c.set_source_rgb(0.85, 0.87, 0.92); c.fill()
    S.rrect(c, -160, -90, 320, 230, 10)
    c.set_source_rgb(0.75, 0.78, 0.85); c.fill()
    for i in range(4):
        S.rrect(c, -130 + i * 70, -60, 40, 150, 6)
        c.set_source_rgb(0.55, 0.58, 0.66); c.fill()
    S.rrect(c, -150, 150, 300, 70, 14)
    c.set_source_rgb(0.08, 0.09, 0.14); c.fill()
    P.text(c, label, 0, 200, 46, fill=YEL, stroke=None)
    c.restore()


LIVE_CHAT = ["Sir entry?", "Bought 2 lots", "BN to the moon", "Sir SL kya hai?", "Profit booked",
             "Bhai 40k gaye", "Next call kab?", "Link se khola"]


# ---------- shots ----------
def s01(c, t, lt):
    c.save(); c.translate(-40 * lt, 0); P.bg_studio(c, t); c.restore()
    bhai_medium(c, t, 540, 820, 1.5, tilt=-3 + 4 * lt, mouth='smile', arms=((12, -8), (60, 120)))
    S.rrect(c, 70, 230, 170, 66, 14); c.set_source_rgb(*RED); c.fill()
    P.text(c, "LIVE", 155, 280, 46, fill=(1, 1, 1), stroke=None)
    P.text(c, "48.2K watching", 420, 278, 36, fill=(1, 1, 1), stroke=None)
    return 'studio'


def s02(c, t, lt):
    P.bg_studio(c, t)
    burst(c, 540, 470, 330 + 20 * math.sin(t * 20), 14, YEL, rot=t * 0.6)
    P.text(c, "ENTER", 540, 430, 120, fill=RED, stroke=(0, 0, 0), lw=16)
    P.text(c, "NOW!", 540, 560, 150, fill=RED, stroke=(0, 0, 0), lw=18)
    CH.bhai_head(c, 540, 1080, 2.6, t, tilt=-5, mouth='bigsmile', talk=talk(t))
    return 'studio'


def s03(c, t, lt):
    P.bg_void(c, (0.03, 0.02, 0.06))
    P.phone(c, 190, 260, 700, 1300, P.screen_live(3.4, LIVE_CHAT), t, tilt=-3 + 3 * lt, glow_a=0.4)
    # thumb
    c.save(); c.translate(760, 1500); c.rotate(-0.35)
    S.rrect(c, -70, 0, 140, 500, 70); c.set_source_rgba(*S.SKIN[:3], 1); c.fill(); c.restore()
    return 'studio'


def s04(c, t, lt):
    P.bg_void(c, (0.01, 0.01, 0.02))
    P.glow(c, 540, 760, 700, (1.0, 0.85, 0.3), 0.35)
    sc = 1.0 + 0.06 * math.sin(t * 6)
    c.save(); c.translate(540, 820); c.scale(sc, sc)
    P.text(c, "YOU.", 0, 0, 330, fill=YEL, stroke=(0, 0, 0), lw=30)
    c.restore()
    # silhouette Sid from behind holding phone
    c.set_source_rgb(0.05, 0.05, 0.08)
    c.arc(540, 1180, 120, 0, 2 * math.pi); c.fill()
    S.rrect(c, 330, 1270, 420, 600, 160); c.fill()
    return 'void'


def s05(c, t, lt):
    c.save(); c.translate(-60 * lt, 0); P.bg_trading_room(c, t); c.restore()
    sid_medium(c, t, 540, 780, 1.4, tilt=3, arms=((14, -10), (30, 150)), phone=1, glow=0.8,
               mouth='smile', look=(0.5, 0.3))
    # floating "add funds" pill
    kk = P.eob(k(t, 7.9, 8.3))
    c.save(); c.translate(540, 360); c.scale(kk, kk)
    S.rrect(c, -260, -60, 520, 120, 60); c.set_source_rgb(0.1, 0.11, 0.16); c.fill_preserve()
    c.set_source_rgb(*GRN); c.set_line_width(5); c.stroke()
    P.text(c, "+ ₹10,000 added", 0, 20, 52, fill=GRN, stroke=None)
    c.restore()
    return 'night'


def s06(c, t, lt):
    P.bg_grid(c, t, (0.03, 0.05, 0.05))
    pnl = 2340 * E(lt * 1.4)
    P.phone(c, 170, 230, 740, 1340, P.screen_trade_app(pnl, k_chart=0.4 + lt, seed=11), t, tilt=4 - 6 * lt)
    return 'money'


def s07(c, t, lt):
    c.save(); c.translate(-30 * lt, 0); P.bg_trading_room(c, t, 1.3); c.restore()
    for i in range(10):
        ang = t * 1.5 + i * 0.63
        burst(c, 540 + math.cos(ang) * 380, 600 + math.sin(ang) * 260, 22, 4, YEL, a=0.6 + 0.4 * math.sin(t * 5 + i))
    sid_medium(c, t, 540, 820, 1.5, tilt=-4, arms=((70, 120), (70, 120)), mouth='bigsmile', blush=0.6, eyes=0.8)
    # crown
    c.save(); c.translate(540, 440 + math.sin(t * 4) * 8)
    c.move_to(-110, 40); c.line_to(-130, -60); c.line_to(-55, -10); c.line_to(0, -90); c.line_to(55, -10)
    c.line_to(130, -60); c.line_to(110, 40); c.close_path()
    c.set_source_rgb(1, 0.8, 0.2); c.fill_preserve(); c.set_source_rgb(0.5, 0.35, 0); c.set_line_width(6); c.stroke()
    c.restore()
    P.text(c, "GENIUS", 540, 300, 96, fill=YEL, stroke=(0, 0, 0), lw=14, alpha=k(t, 10.6, 10.9))
    return 'warm'


def s08(c, t, lt):
    P.bg_grid(c, t, (0.07, 0.02, 0.03))
    pnl = 2340 - 6440 * E(lt * 1.3)
    P.phone(c, 170, 230, 740, 1340, P.screen_trade_app(pnl, crash=10, seed=11), t, tilt=-5 + 3 * lt)
    return 'red'


def s09(c, t, lt):
    c.save(); c.translate(40 * lt, 0); P.bg_trading_room(c, t, 0.8); c.restore()
    c.set_source_rgba(0.6, 0, 0, 0.18); c.paint()
    sid_medium(c, t, 540, 820, 1.5, tilt=6, mouth='grit', angry=0.8, squint=0.5, sweat=1.0, eyes=0.9,
               arms=((14, -10), (30, 150)), phone=1, glow=0.6)
    P.stamp(c, "LOT × 2", 540, 360, 14.96, t, -7, RED, 110)
    return 'red'


def s10(c, t, lt):
    P.bg_grid(c, t, (0.08, 0.02, 0.03))
    pnl = -4100 - 4800 * E(lt * 1.2)
    P.phone(c, 170, 230, 740, 1340, P.screen_trade_app(pnl, crash=4, seed=5), t, tilt=6 * math.sin(t * 9) * (1 - lt))
    return 'red'


def s11(c, t, lt):
    P.bg_void(c)
    sid_face(c, t, 540, 980, 3.2, tilt=-4, eyes=0.5, look=(0, 0.8), sad=1, bags=1, mouth='frown', tear=lt)
    P.text(c, "₹0", 540, 470, 300, fill=(1, 1, 1), stroke=(0, 0, 0), lw=26, alpha=k(t, 17.5, 17.8))
    return 'void'


def s12(c, t, lt):
    P.bg_grid(c, t, (0.04, 0.05, 0.09))
    P.people_grid(c, 130, 380, 8, 7, 105, 0.0, 1.0, col_off=(0.42, 0.45, 0.55))
    # Sid highlighted in the middle
    c.save(); c.translate(540, 820)
    P.glow(c, 0, 0, 200, YEL, 0.5)
    c.restore()
    sid_face(c, t, 540, 800, 0.62, mouth='frown', sad=0.6)
    return 'night'


def s13(c, t, lt):
    P.bg_grid(c, t, (0.05, 0.06, 0.1))
    P.doc_sebi(c, 160, 360 + 200 * (1 - E(lt * 2)), 760, 1000, lt * 1.5)
    return 'day'


def s14(c, t, lt):
    P.bg_grid(c, t, (0.04, 0.04, 0.07))
    lit = 0.91 * E(k(t, 22.9, 24.0))
    P.people_grid(c, 118, 560, 10, 10, 78, lit, k(t, 21.6, 22.6))
    if t > 22.9:
        P.big_number(c, "91%", 540, 400, 230, k(t, 22.9, 23.25), col=RED, sub="LOST MONEY")
    return 'night'


def s15(c, t, lt):
    P.bg_grid(c, t, (0.07, 0.02, 0.03))
    v = int(110069 * E(k(t, 26.4, 27.9)))
    P.card(c, 120, 520, 840, 360, "AVERAGE LOSS PER TRADER", f"₹{v:,}", k(t, 25.6, 25.95), col=RED)
    for i in range(12):
        ph = (t * 0.6 + i / 12) % 1
        P.coin(c, 150 + i * 70, 960 + ph * 700, 26, a=1 - ph)
    return 'red'


def s16(c, t, lt):
    c.save(); c.translate(50 * lt - 25, 0); P.bg_studio(c, t); c.restore()
    S.rrect(c, 640, 330, 380, 200, 20); c.set_source_rgba(0, 0, 0, 0.7); c.fill()
    P.text(c, "+₹54,000", 830, 455, 64, fill=GRN, stroke=None)
    bhai_medium(c, t, 480, 840, 1.45, tilt=5, mouth='smirk', tk=0)
    for i in range(3):
        a = k(t, 29.2 + i * 0.4, 29.5 + i * 0.4)
        P.text(c, "?", 200 + i * 90, 470 - i * 60, 140, fill=YEL, stroke=(0, 0, 0), lw=12, alpha=a)
    return 'studio'


def s17(c, t, lt):
    P.bg_void(c, (0.03, 0.03, 0.05))
    P.phone(c, 150, 220, 780, 1400, P.screen_description(k(t, 31.3, 32.6)), t, tilt=2 - 2 * lt, glow_a=0.2)
    return 'phone'


def s18(c, t, lt):
    P.bg_grid(c, t)
    v = int(100000 * E(k(t, 34.2, 35.6)))
    P.big_number(c, f"{v:,}".replace(",", ",") if v < 100000 else "1,00,000", 540, 760, 170, k(t, 34.1, 34.4), col=(1, 1, 1),
                 sub="SUBSCRIBERS")
    # bell
    c.save(); c.translate(540, 470); c.rotate(math.sin(t * 12) * 0.2 * (1 - lt))
    c.move_to(-70, 40); c.curve_to(-70, -80, 70, -80, 70, 40); c.line_to(90, 70); c.line_to(-90, 70); c.close_path()
    c.set_source_rgb(*YEL); c.fill(); c.arc(0, 85, 20, 0, 2 * math.pi); c.fill(); c.restore()
    return 'night'


def s19(c, t, lt):
    P.bg_grid(c, t)
    P.card(c, 190, 320, 700, 230, "SUBSCRIBERS", "1,00,000", 1.0, col=(1, 1, 1))
    P.arrow(c, 540, 580, 540, 820, k(t, 36.3, 36.9))
    P.card(c, 190, 850, 700, 230, "OPENED ACCOUNT VIA LINK", "10,000", k(t, 36.8, 37.2), col=YEL)
    return 'night'


def s20(c, t, lt):
    P.bg_grid(c, t)
    P.card(c, 190, 300, 700, 230, "TRADE EVERY DAY", "1,000", k(t, 38.2, 38.55), col=GRN)
    P.people_grid(c, 118, 640, 10, 6, 78, 0.1, k(t, 38.4, 39.4), col_on=GRN)
    return 'money'


def s21(c, t, lt):
    P.bg_grid(c, t)
    P.card(c, 110, 460, 400, 300, "ORDERS / DAY", "10", k(t, 40.6, 40.95), col=(1, 1, 1))
    P.text(c, "×", 540, 650, 140, fill=YEL, stroke=(0, 0, 0), lw=10, alpha=k(t, 41.0, 41.2))
    P.card(c, 570, 460, 400, 300, "BROKERAGE", "₹20", k(t, 41.3, 41.65), col=YEL)
    P.text(c, "× 1,000 traders", 540, 940, 70, fill=(0.85, 0.87, 0.95), stroke=(0, 0, 0), lw=8, alpha=k(t, 41.8, 42.1))
    return 'night'


def s22(c, t, lt):
    P.bg_grid(c, t, (0.03, 0.05, 0.04))
    broker_box(c, 540, 960, 1.4)
    srcs = [(x, 1700) for x in range(100, 1000, 110)]
    P.money_flow(c, t, lt, srcs, (540, 960), n=24)
    P.big_number(c, "₹2,00,000", 540, 420, 150, k(t, 43.2, 43.5), col=GRN, sub="BROKERAGE / DAY")
    return 'money'


def s23(c, t, lt):
    P.bg_grid(c, t, (0.03, 0.05, 0.04))
    broker_box(c, 300, 1120, 0.95)
    bhai_medium(c, t, 800, 820, 0.85, tilt=4, mouth='bigsmile', tk=0)
    P.arrow(c, 420, 1000, 650, 820, k(t, 44.6, 45.3), col=YEL)
    P.text(c, "10%", 520, 880, 80, fill=YEL, stroke=(0, 0, 0), lw=10, alpha=k(t, 45.1, 45.4))
    if t > 45.4:
        P.money_flow(c, t, (t - 45.4) / 2.2, [(300, 1050)], (800, 760), n=10, seed=9)
    if t > 46.0:
        P.big_number(c, "₹20,000", 540, 400, 160, k(t, 46.0, 46.3), col=GRN, sub="EVERY DAY")
    return 'money'


def s24(c, t, lt):
    P.bg_grid(c, t, (0.03, 0.05, 0.04))
    day = 1 + int(21 * E(lt))
    c.save(); c.translate(540, 760)
    S.rrect(c, -240, -260, 480, 520, 30); c.set_source_rgb(0.97, 0.97, 0.98); c.fill()
    S.rrect(c, -240, -260, 480, 120, 30); c.set_source_rgb(*RED); c.fill()
    P.text(c, "TRADING DAY", 0, -180, 50, fill=(1, 1, 1), stroke=None)
    P.text(c, str(day), 0, 120, 250, fill=(0.1, 0.1, 0.12), stroke=None)
    c.restore()
    v = int(20000 * day)
    P.big_number(c, f"₹{v:,}+", 540, 1250, 130, 1.0, col=GRN, sub="PER MONTH")
    return 'money'


def s25(c, t, lt):
    c.save(); c.translate(-30 * lt, 0); P.bg_studio(c, t); c.restore()
    for i in range(14):
        P.coin(c, 300 + (i % 7) * 80, 1260 - (i // 7) * 40, 40)
    bhai_medium(c, t, 540, 800, 1.35, tilt=-4, mouth='smirk', tk=0, arms=((70, 120), (70, 120)))
    P.stamp(c, "0 TRADES WON", 540, 360, 50.2, t, 6, (0.12, 0.12, 0.16), 90)
    return 'studio'


def s26(c, t, lt):
    c.save(); c.translate(-40 * lt, 0); P.bg_night_room(c, t); c.restore()
    sid_medium(c, t, 540, 820, 1.45, tilt=-6, arms=((14, -10), (30, 150)), phone=1, glow=1.0, eyes=0.6, bags=1,
               mouth='flat', look=(0.5, 0.4))
    for i in range(5):
        a = k(t, 51.6 + i * 0.4, 51.8 + i * 0.4)
        S.rrect(c, 120 + (i % 2) * 560, 320 + i * 120, 300, 90, 45)
        c.set_source_rgba(*(GRN if i % 2 == 0 else RED), a); c.fill()
        P.text(c, "BUY" if i % 2 == 0 else "SELL", 270 + (i % 2) * 560, 382 + i * 120, 52, fill=(1, 1, 1), stroke=None,
               alpha=a)
    return 'night'


def s27(c, t, lt):
    P.bg_grid(c, t)
    P.card(c, 140, 360, 800, 300, "YOUR WIN", "doesn't matter", k(t, 53.8, 54.15), col=RED)
    P.card(c, 140, 760, 800, 300, "YOUR TRADE", "is all he needs", k(t, 55.5, 55.85), col=GRN)
    return 'night'


def s28(c, t, lt):
    P.bg_grid(c, t, (0.05, 0.06, 0.1))
    P.doc_sebi(c, 200, 520, 680, 880, 1.0)
    P.big_number(c, "2024", 540, 400, 200, k(t, 59.1, 59.4), col=YEL, sub="SEBI ACTS")
    return 'day'


def s29(c, t, lt):
    P.bg_grid(c, t)
    broker_box(c, 270, 900, 0.85)
    bhai_medium(c, t, 810, 760, 0.75, tilt=0, mouth='o' if t > 63.2 else 'smirk', tk=0)
    cut = t > 62.9
    # chain link
    c.set_line_width(14)
    for i in range(7):
        x = 420 + i * 45
        if cut and 3 <= i <= 3:
            continue
        c.save(); c.translate(x, 820 - i * 8); c.scale(1, 0.6)
        c.arc(0, 0, 26, 0, 2 * math.pi); c.restore()
        c.set_source_rgb(0.95, 0.75, 0.22); c.stroke()
    if not cut:
        P.money_flow(c, t, lt * 2, [(300, 820)], (800, 700), n=6, seed=3)
    else:
        c.set_line_width(26); c.set_source_rgb(*RED); c.set_line_cap(cairo.LINE_CAP_ROUND)
        for d in (-1, 1):
            c.move_to(500, 730 + d * 60); c.line_to(620, 730 - d * 60); c.stroke()
    P.text(c, "Brokers + unregistered finfluencers", 540, 400, 52, fill=(1, 1, 1), stroke=(0, 0, 0), lw=8,
           alpha=k(t, 60.3, 60.7))
    P.stamp(c, "STOPPED", 540, 1150, 63.8, t, -5, RED, 120)
    return 'night'


def s30(c, t, lt):
    c.save(); c.translate(-30 * lt, 0); P.bg_night_room(c, t); c.restore()
    sid_medium(c, t, 540, 840, 1.45, tilt=4, arms=((14, -10), (30, 150)), phone=1, glow=0.9, squint=0.6,
               look=(0.6, 0.4), mouth='flat', angry=0.3)
    # small live phone near
    P.phone(c, 640, 330, 300, 540, P.screen_live(60, LIVE_CHAT, "31K"), t, tilt=8, glow_a=0.3)
    P.text(c, "ENTER NOW!", 790, 300, 52, fill=RED, stroke=(0, 0, 0), lw=8, alpha=k(t, 66.0, 66.2))
    return 'night'


def s31(c, t, lt):
    P.bg_void(c, (0.03, 0.03, 0.05))
    P.glow(c, 540, 900, 700, YEL, 0.2)
    sid_face(c, t, 540, 1000, 3.0, tilt=-3, mouth='smirk', look=(0, 0), **{'raise': 0.8})
    P.text(c, "WHERE DOES", 540, 330, 92, fill=(1, 1, 1), stroke=(0, 0, 0), lw=12, alpha=k(t, 68.5, 68.8))
    P.text(c, "YOUR MONEY", 540, 450, 104, fill=YEL, stroke=(0, 0, 0), lw=14, alpha=k(t, 69.2, 69.5))
    P.text(c, "COME FROM?", 540, 570, 92, fill=(1, 1, 1), stroke=(0, 0, 0), lw=12, alpha=k(t, 69.9, 70.2))
    return 'warm'


def s32(c, t, lt):
    P.bg_grid(c, t)
    P.glow(c, 540, 820, 700, YEL, 0.2)
    sid_medium(c, t, 380, 880, 1.15, tilt=3, arms=((14, -10), (100, 40)), mouth='smile', blush=0.4)
    # share arrow icon
    c.save(); c.translate(780, 600 + math.sin(t * 5) * 14)
    S.rrect(c, -110, -110, 220, 220, 50); c.set_source_rgb(*YEL); c.fill()
    c.set_line_width(22); c.set_source_rgb(0.08, 0.08, 0.1); c.set_line_cap(cairo.LINE_CAP_ROUND)
    c.move_to(-50, 40); c.curve_to(-40, -30, 10, -40, 50, -40); c.stroke()
    c.move_to(20, -75); c.line_to(55, -40); c.line_to(20, -5); c.stroke()
    c.restore()
    P.text(c, "SEND IT TO", 540, 320, 96, fill=(1, 1, 1), stroke=(0, 0, 0), lw=12)
    P.text(c, "THAT FRIEND", 540, 440, 110, fill=YEL, stroke=(0, 0, 0), lw=14)
    S.rrect(c, 395, 1250, 290, 76, 38); c.set_source_rgb(0.06, 0.06, 0.08); c.fill_preserve()
    c.set_source_rgb(*YEL); c.set_line_width(4); c.stroke()
    P.text(c, "SAME BRO", 540, 1302, 44, fill=YEL, stroke=None)
    return 'end'


# (start, end, fn, cam0(z,fx,fy,rot), cam1, whip_dir)
SHOTS = [
    (0.00, 2.24, s01, (1.00, 540, 900, -2), (1.18, 540, 700, 1), 0),
    (2.24, 3.60, s02, (1.10, 540, 800, 3), (1.18, 540, 820, -2), 1),
    (3.60, 6.10, s03, (1.00, 540, 900, 3), (1.22, 540, 1150, -1), -1),
    (6.10, 7.60, s04, (1.35, 540, 820, 0), (1.00, 540, 900, 0), 0),
    (7.60, 9.06, s05, (1.12, 420, 800, -2), (1.12, 660, 820, 2), 1),
    (9.06, 10.42, s06, (1.00, 540, 900, 0), (1.15, 540, 1100, 0), -1),
    (10.42, 12.60, s07, (1.25, 540, 1000, -4), (1.10, 540, 800, 2), 1),
    (12.60, 13.90, s08, (1.15, 540, 1100, 2), (1.05, 540, 950, -2), -1),
    (13.90, 16.02, s09, (1.10, 540, 800, 6), (1.20, 540, 760, 10), 1),
    (16.02, 17.45, s10, (1.05, 540, 950, -3), (1.18, 540, 1150, 2), -1),
    (17.45, 19.00, s11, (1.15, 540, 900, 0), (1.00, 540, 900, 0), 0),
    (19.00, 20.55, s12, (1.80, 540, 820, 0), (1.00, 540, 900, 0), 0),
    (20.55, 21.65, s13, (1.00, 540, 900, -2), (1.12, 540, 850, 1), 1),
    (21.65, 25.55, s14, (1.08, 540, 1000, 0), (1.00, 540, 920, 0), -1),
    (25.55, 28.12, s15, (1.00, 540, 900, -1), (1.12, 540, 760, 1), 1),
    (28.12, 31.15, s16, (1.15, 400, 800, -2), (1.15, 640, 780, 2), -1),
    (31.15, 34.05, s17, (1.00, 540, 900, 0), (1.35, 540, 760, 0), 1),
    (34.05, 36.12, s18, (1.10, 540, 760, 0), (1.00, 540, 900, 0), -1),
    (36.12, 38.11, s19, (1.10, 540, 500, 0), (1.10, 540, 900, 0), 1),
    (38.11, 40.52, s20, (1.00, 540, 900, 0), (1.10, 540, 800, 0), -1),
    (40.52, 42.52, s21, (1.00, 520, 760, -1), (1.06, 560, 700, 1), 1),
    (42.52, 44.45, s22, (1.00, 540, 1000, 0), (1.12, 540, 820, 0), -1),
    (44.45, 47.55, s23, (1.04, 500, 900, 0), (1.06, 580, 820, 0), 1),
    (47.55, 49.45, s24, (1.00, 540, 900, -2), (1.12, 540, 980, 2), -1),
    (49.45, 51.25, s25, (1.10, 540, 800, 3), (1.20, 540, 700, -2), 1),
    (51.25, 53.80, s26, (1.10, 540, 900, 0), (1.15, 540, 820, 5), -1),
    (53.80, 57.46, s27, (1.10, 540, 560, 0), (1.10, 540, 950, 0), 1),
    (57.46, 60.05, s28, (1.00, 540, 900, -2), (1.10, 540, 760, 1), -1),
    (60.05, 64.68, s29, (1.00, 520, 860, 0), (1.06, 560, 860, 0), 1),
    (64.68, 68.42, s30, (1.00, 540, 900, -2), (1.25, 540, 680, 2), 0),
    (68.42, 71.02, s31, (1.20, 540, 900, 0), (1.05, 540, 820, 0), 1),
    (71.02, 76.00, s32, (1.05, 540, 900, 0), (1.00, 540, 900, 0), -1),
]


def hblur(rgb, w):
    if w < 2:
        return rgb
    w = int(w)
    cs = np.cumsum(np.pad(rgb.astype(np.float32), ((0, 0), (w, w), (0, 0)), mode='edge'), axis=1)
    out = (cs[:, 2 * w:] - cs[:, :-2 * w]) / (2 * w)
    return out[:, :rgb.shape[1]].astype(np.uint8)


def render_frame(i):
    t = i / FPS
    idx = next((j for j, s in enumerate(SHOTS) if s[0] <= t < s[1]), len(SHOTS) - 1)
    st, en, fn, c0, c1, wd = SHOTS[idx]
    lt = (t - st) / (en - st)
    tmp = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    c = cairo.Context(tmp)
    grade = fn(c, t, lt)
    e = E(lt)
    z, fxp, fyp, rot = [a + (b - a) * e for a, b in zip(c0, c1)]
    # handheld drift
    fxp += math.sin(t * 1.3) * 6 + math.sin(t * 2.7) * 3
    fyp += math.sin(t * 1.1 + 1) * 5
    rot += math.sin(t * 0.9) * 0.4
    # whip-in offset
    whip = 0.0
    if st > 0 and wd != 0 and t - st < 0.16:
        kk = 1 - (t - st) / 0.16
        fxp -= wd * 420 * kk * kk
        whip = kk
    if idx + 1 < len(SHOTS) and SHOTS[idx + 1][5] != 0 and en - t < 0.08:
        kk = 1 - (en - t) / 0.08
        fxp += SHOTS[idx + 1][5] * 260 * kk * kk
        whip = max(whip, kk)
    punch = 1 + 0.05 * max(0, 1 - (t - st) / 0.12) if st > 0 and wd == 0 else 1
    out = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    o = cairo.Context(out)
    o.set_source_rgb(0, 0, 0)
    o.paint()
    o.translate(W / 2, H / 2)
    o.rotate(math.radians(rot))
    o.scale(z * punch, z * punch)
    o.translate(-fxp, -fyp)
    o.set_source_surface(tmp, 0, 0)
    o.get_source().set_extend(cairo.EXTEND_PAD)
    o.paint()
    out.flush()
    flash = 0.35 * max(0, 1 - (t - 12.6) / 0.15) if 12.6 <= t < 12.75 else 0
    rgb = fx.post(out, grade, i, flash)
    if whip > 0:
        rgb = hblur(rgb, whip * 60)
    ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    oc = cairo.Context(ov)
    disclaimer(oc, t)
    caption(oc, t)
    ov.flush()
    cb = np.ndarray((H, W, 4), np.uint8, ov.get_data())
    a = cb[..., 3:4].astype(np.float32) / 255.0
    return np.clip(rgb.astype(np.float32) * (1 - a) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)


def main():
    if len(sys.argv) > 1 and sys.argv[1] != "full":
        for n, tt in enumerate(map(float, sys.argv[1].split(","))):
            Image.fromarray(render_frame(int(tt * FPS))).save(f"p_{n:02d}.png")
        return
    a, b, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                          "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(a, b):
        p.stdin.write(render_frame(i).tobytes())
        if i % 150 == 0:
            print(f"frame {i}/{b}", flush=True)
    p.stdin.close()
    p.wait()


if __name__ == "__main__":
    main()
