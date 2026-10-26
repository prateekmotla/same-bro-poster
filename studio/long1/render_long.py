"""Same Bro LONG 01 — How Live Traders Really Make Money. 1920x1080 @24fps, themed environments + full-body chars."""
import json
import math
import subprocess
import sys
import wave

import cairo
import numpy as np
from PIL import Image

sys.path.insert(0, "/home/claude/sid/long1")
sys.path.insert(0, "/home/claude/sid/v2")
sys.path.insert(0, "/home/claude/sid/v3")
import body as B  # noqa: E402
import env as V  # noqa: E402
import fxw as FX  # noqa: E402
import props as P  # noqa: E402
import sid2 as S  # noqa: E402
import ui as U  # noqa: E402
from ui import T, k, eob, YEL, RED, GRN, WHITE  # noqa: E402

W, H, FPS = 1920, 1080, 24
DUR = 235.0
L = [None] + json.load(open("/home/claude/sid/long1/lines.json"))  # L[n] = [start, end]
FX.GRADES['studio'] = dict(lift=(0.03, 0.0, 0.05), gain=(1.02, 0.95, 1.08), sat=1.05, vig=0.9, bloom=0.4)
FX.GRADES['red'] = dict(lift=(0.05, 0.0, 0.01), gain=(1.08, 0.9, 0.9), sat=0.95, vig=1.0, bloom=0.3)
FX.GRADES['money'] = dict(lift=(0.0, 0.03, 0.02), gain=(0.98, 1.05, 0.98), sat=1.05, vig=0.8, bloom=0.4)
FX.GRADES['street'] = dict(lift=(0.03, 0.01, 0.05), gain=(1.05, 0.95, 0.95), sat=1.0, vig=0.9, bloom=0.45)

with wave.open("/home/claude/sid/long1/vo16.wav") as wv:
    _a = np.frombuffer(wv.readframes(wv.getnframes()), np.int16).astype(np.float32) / 32768
_hop = 16000 // FPS
_env = np.array([np.sqrt((_a[i:i + _hop] ** 2).mean() + 1e-12) for i in range(0, len(_a), _hop)])
_env = np.convolve(np.clip((20 * np.log10(_env + 1e-9) + 45) / 30, 0, 1), [0.25, 0.5, 0.25], mode="same")


def talk(t):
    i = int(t * FPS)
    return float(_env[i]) if 0 <= i < len(_env) else 0.0


def s(n):
    return L[n][0]


def e(n):
    return L[n][1]


def grade_dim(c, a=0.55):
    U.dim(c, a)


# ======================= SHOTS =======================
def room_sid(c, t, mode='night', **kw):
    V.room(c, t, mode)
    d = dict(pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1.0 if mode == 'night' else 0.2, mouth='flat',
             look=(0.5, 0.3))
    d.update(kw)
    B.figure(c, 1000, 330, 0.5, t, **d)


def sh_room_wide(c, t, lt):
    room_sid(c, t)
    return 'night'


def sh_room_close(c, t, lt):
    room_sid(c, t, squint=0.2, eyes=0.8, bags=0.6)
    return 'phone'


def sh_live_phone(c, t, lt):
    V.room(c, t, 'night')
    U.dim(c, 0.7)
    chat = ["Sir entry?", "Bought 2 lots", "BN to the moon", "Link se khola"]
    U.phone_frame(c, 660, 40, 600, 1000, U.scr_live(chat[:1 + int(lt * 4)], talk=talk(t), t=t), t, tilt=-2 + 3 * lt)
    if t > 7.5:
        S.rrect(c, 1300, 760, 520, 90, 45)
        c.set_source_rgb(*YEL)
        c.fill()
        T(c, "LINK IN DESCRIPTION", 1560, 820, 36, (0.1, 0.1, 0.1), stroke=None)
    return 'studio'


def sh_sid_think(c, t, lt):
    room_sid(c, t, look=(0.2, -0.6), **{'raise': 0.4})
    # thought bubble
    a = k(t, 10.4, 10.8)
    for i, (x, y, r) in enumerate(((1180, 330, 14), (1230, 280, 22))):
        c.arc(x, y, r, 0, 2 * math.pi)
        c.set_source_rgba(1, 1, 1, a)
        c.fill()
    S.rrect(c, 1240, 130, 520, 130, 60)
    c.set_source_rgba(1, 1, 1, a)
    c.fill()
    T(c, "He wins DAILY...", 1500, 190, 40, (0.1, 0.1, 0.15), a, stroke=None)
    T(c, "why not me?", 1500, 238, 36, (0.6, 0.1, 0.15), a * k(t, 12.4, 12.7), stroke=None)
    return 'phone'


def sh_bhai_cash(c, t, lt):
    V.studio(c, t)
    B.figure(c, 960, 360, 0.6, t, who='bhai', pose='stand', mouth='smirk', arms=((70, 120), (70, 120)))
    for i in range(18):
        ph = (t * 0.5 + i / 18) % 1
        P.coin(c, 300 + (i * 97) % 1320, -40 + ph * 1100, 26, 1 - ph * 0.6)
    return 'studio'


def sh_title(c, t, lt):
    V.studio(c, t)
    U.dim(c, 0.72)
    T(c, "HOW LIVE TRADERS", 960, 450, 110, WHITE, k(t, 17.3, 17.6))
    T(c, "REALLY MAKE MONEY", 960, 590, 110, YEL, k(t, 17.6, 17.9))
    return 'studio'


def sh_from_you(c, t, lt):
    V.room(c, t, 'night')
    U.dim(c, 0.45)
    B.figure(c, 960, 360, 0.75, t, pose='stand', mouth='o', eyes=1.2, **{'raise': 0.9})
    sc = 1 + 0.08 * max(0, 1 - (t - 21.2) / 0.3)
    c.save(); c.translate(960, 230); c.scale(sc, sc)
    T(c, "FROM YOU.", 0, 0, 150, YEL, k(t, 21.1, 21.3), lw=18)
    c.restore()
    return 'warm'


def sh_metro(c, t, lt):
    V.metro(c, t)
    B.figure(c, 760, 330, 0.55, t, pose='stand', phone=1, arms=((14, -10), (30, 150)), glow=0.5, mouth='smile',
             look=(0.5, 0.4))
    U.phone_frame(c, 1180, 160, 420, 760, U.scr_sms(k(t, 24.0, 24.6)), t, tilt=4)
    return 'day'


def sh_canteen(c, t, lt):
    V.canteen(c, t)
    B.figure(c, 640, 330, 0.55, t, pose='sit', mouth='o' if t > 28.6 else 'flat', eyes=1.1, look=(0.6, 0.2))
    B.figure(c, 1240, 330, 0.55, t, who='friend', pose='sit', mouth='bigsmile', arms=((14, -10), (100, 60)),
             talk=talk(t) if t > 28.3 else 0)
    # friend's phone shown to Sid
    U.phone_frame(c, 1000, 380, 170, 300, U.scr_pnl(8000, seed=4), t, tilt=-12, glow=0.4)
    if t > 28.6:
        T(c, "+₹8,000 TODAY", 1090, 330, 46, GRN, k(t, 28.6, 28.9))
    return 'warm'


def sh_signup(c, t, lt):
    V.room(c, t, 'night')
    U.dim(c, 0.6)
    U.phone_frame(c, 690, 40, 540, 1000, U.scr_signup(k(t, 32.4, 33.0)), t, tilt=-1)
    return 'phone'


def sh_bhai_smirk(c, t, lt):
    V.studio(c, t)
    B.figure(c, 960, 380, 0.75, t, who='bhai', pose='stand', mouth='smirk', **{'raise': 0.5})
    P.stamp(c, "+1 REFERRAL", 1450, 300, 33.8, t, 8, GRN, 70)
    return 'studio'


def sh_win_week(c, t, lt):
    V.room(c, t, 'night')
    B.figure(c, 760, 330, 0.55, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=0.8, mouth='bigsmile',
             blush=0.5)
    msgs = [("+₹1,240", True, 'pnl+'), ("bro you're a GENIUS", False, 'txt'), ("+₹2,180", True, 'pnl+'),
            ("teach me too!!", False, 'txt')]
    U.phone_frame(c, 1180, 80, 480, 900, U.scr_chat("College Gang", msgs, k(t, 36.2, 39.6)), t, tilt=3)
    return 'warm'


def sh_crash(c, t, lt):
    V.room(c, t, 'night')
    c.set_source_rgba(0.5, 0, 0, 0.15 * k(t, 40.5, 41.5))
    c.paint()
    B.figure(c, 700, 330, 0.55, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=0.8, mouth='grit',
             sweat=k(t, 41, 42), angry=0.4, squint=0.4)
    U.phone_frame(c, 1150, 80, 480, 900, U.scr_pnl(2180 - 6200 * k(t, 40.5, 43.5), crash=6, seed=9), t,
                  tilt=-3 + math.sin(t * 20) * 1.2 * k(t, 41, 42))
    P.stamp(c, "LOT × 2", 700, 200, 45.0, t, -8, RED, 90)
    return 'red'


def sh_borrow(c, t, lt):
    V.room(c, t, 'night')
    U.dim(c, 0.5)
    msgs = [("−₹9,800", True, 'pnl-'), ("bro lend me 5k?", True, 'txt'), ("will return tmrw", True, 'txt'),
            ("ok sent", False, 'txt')]
    U.phone_frame(c, 700, 40, 520, 1000, U.scr_chat("Rohan", msgs, k(t, 46.2, 48.8)), t, tilt=-2)
    return 'red'


def sh_walk_home(c, t, lt):
    off = (t - s(11)) * 120
    V.street(c, t, off, night=True)
    B.figure(c, 900, 330, 0.55, t, pose='walk', ph=(t - s(11)) * 0.9, mouth='frown', sad=1, eyes=0.6,
             look=(0, 0.7), bags=1)
    if t > 50.2:
        T(c, "₹15,000 → ₹0", 960, 180, 96, WHITE, k(t, 50.2, 50.5))
    if t > 52.0:
        T(c, "nobody at home knows", 960, 280, 46, (0.85, 0.85, 0.9), k(t, 52.0, 52.4), lw=6)
    return 'street'


def sh_noob(c, t, lt):
    V.room(c, t, 'night')
    B.figure(c, 960, 330, 0.62, t, pose='sit', mouth='frown', sad=0.6, look=(-0.5, 0.3), blush=0.3)
    if t > 54.6:
        P.stamp(c, "NOOB?", 1400, 300, 54.6, t, 8, (0.3, 0.3, 0.35), 90)
    if t > 56.2:
        T(c, "Let's check the DATA.", 960, 150, 54, YEL, k(t, 56.2, 56.5))
    return 'night'


def sh_data91(c, t, lt):
    V.studio(c, t)
    U.dim(c, 0.82)
    T(c, "SEBI STUDY · FY25", 960, 120, 44, (0.8, 0.82, 0.9), stroke=None)
    lit = 0.91 * k(t, 61.1, 62.3)
    n = 0
    for r in range(5):
        for cc in range(20):
            idx = r * 20 + cc
            on = idx < int(100 * lit)
            U.ppl(c, 300 + cc * 66, 250 + r * 105, 70, RED if on else (0.45, 0.47, 0.55), k(t, 57.4 + idx * 0.012, 58.0 + idx * 0.012))
            n += 1
    if t > 61.2:
        T(c, "91% LOST MONEY", 960, 890, 84, RED, k(t, 61.2, 61.5))
    if t > 63.3:
        v = int(110069 * k(t, 64.3, 65.6))
        S.rrect(c, 1400, 780, 460, 150, 20)
        c.set_source_rgba(0.1, 0.02, 0.03, 0.9)
        c.fill()
        T(c, "AVG LOSS", 1630, 830, 30, (0.85, 0.8, 0.8), stroke=None)
        T(c, f"₹{v:,}", 1630, 905, 64, RED, stroke=None)
    return 'red'


def sh_data43(c, t, lt):
    V.studio(c, t)
    U.dim(c, 0.82)
    T(c, "F&O TRADERS UNDER 30", 960, 160, 60, WHITE)
    U.bar(c, 300, 340, 1200, 90, 0.31 * k(t, 67.6, 68.6) / 0.5, (0.6, 0.62, 0.7), "FY22", "31%")
    U.bar(c, 300, 560, 1200, 90, 0.43 * k(t, 69.6, 70.6) / 0.5, YEL, "FY26", "43%")
    if t > 73.6:
        S.rrect(c, 460, 760, 1000, 180, 30)
        c.set_source_rgba(0.6, 0.05, 0.1, 0.95)
        c.fill()
        T(c, "89% of them LOST money", 960, 870, 64, WHITE, k(t, 73.6, 73.9), stroke=None)
    return 'night'


def sh_nine_of_ten(c, t, lt):
    V.canteen(c, t)
    U.dim(c, 0.6)
    for i in range(10):
        x = 260 + i * 156
        lost = i != 6 and t > 76.4 + i * 0.12
        B.figure(c, x, 380, 0.3, t + i, who='friend' if i % 3 == 1 else 'sid', pose='stand',
                 mouth='frown' if lost else 'flat', sad=1 if lost else 0)
        if lost:
            T(c, "LOST", x, 330 - 80, 34, RED, k(t, 76.4 + i * 0.12, 76.6 + i * 0.12))
    T(c, "9 out of 10", 960, 850, 80, YEL, k(t, 77.0, 77.3))
    return 'warm'


def sh_bhai_wins(c, t, lt):
    V.studio(c, t)
    B.figure(c, 760, 360, 0.6, t, who='bhai', pose='stand', mouth='bigsmile', arms=((70, 120), (60, 130)))
    U.phone_frame(c, 1240, 120, 420, 760, U.scr_pnl(54300, seed=2), t, tilt=6)
    for i in range(3):
        T(c, "?", 300 + i * 110, 300 - i * 50, 160, YEL, k(t, 82.4 + i * 0.3, 82.7 + i * 0.3))
    return 'studio'


CARDS = [("REFERRAL", "brokerage share"), ("PREMIUM GROUP", "₹999 / month"), ("COURSES", "₹15,000 each"),
         ("ADS & SUPERCHATS", "views = money"), ("SCREENSHOTS", "only the wins")]


def sh_five(c, t, lt):
    V.studio(c, t)
    U.dim(c, 0.75)
    T(c, "HIS 5 INCOMES", 960, 200, 90, YEL, k(t, 88.1, 88.4))
    for i, (a, b) in enumerate(CARDS):
        U.icon_card(c, 110 + i * 350, 380, 320, 420, i + 1, a, b, k(t, 89.0 + i * 0.25, 89.4 + i * 0.25))
    return 'studio'


def sh_bhai_link(c, t, lt):
    V.studio(c, t)
    B.figure(c, 960, 380, 0.75, t, who='bhai', pose='stand', mouth='smile', talk=talk(t), arms=((40, 100), (12, -8)))
    U.icon_card(c, 80, 300, 360, 460, 1, "REFERRAL", "brokerage share", 1.0)
    return 'studio'


def sh_funnel(c, t, lt):
    V.studio(c, t)
    U.dim(c, 0.85)
    st = [("1,00,000", "SUBSCRIBERS", 94.6), ("10,000", "OPENED ACCOUNT VIA LINK", 96.4), ("1,000", "TRADE DAILY", 98.5)]
    for i, (v, lab, t0) in enumerate(st):
        w = 1300 - i * 300
        a = k(t, t0, t0 + 0.3)
        S.rrect(c, 960 - w / 2, 180 + i * 230, w, 190, 24)
        c.set_source_rgba(*[(0.25, 0.27, 0.35), (0.85, 0.65, 0.1), (0.15, 0.6, 0.35)][i], 0.95 * a)
        c.fill()
        T(c, v, 960, 280 + i * 230, 76, WHITE, a, stroke=None)
        T(c, lab, 960, 340 + i * 230, 30, WHITE, a, stroke=None, bold=False)
    if t > 100.4:
        T(c, "× 10 orders × ₹20 brokerage", 960, 1000, 54, YEL, k(t, 100.4, 100.7))
    return 'night'


def sh_brokerage(c, t, lt):
    V.studio(c, t)
    U.dim(c, 0.8)
    c.save(); c.translate(-300, -100); c.scale(1.0, 1.0)
    from_render3_broker(c, 700, 640, 1.1)
    c.restore()
    T(c, "₹2,00,000 / day", 400, 860, 60, GRN, k(t, 102.6, 102.9))
    B.figure(c, 1400, 330, 0.55, t, who='bhai', pose='stand', mouth='bigsmile', arms=((70, 120), (70, 120)))
    if t > 104.4:
        P.arrow(c, 620, 560, 1180, 520, k(t, 104.4, 105.2), col=YEL)
        T(c, "10%", 900, 480, 70, YEL, k(t, 105.0, 105.3))
        P.money_flow(c, t, (t - 104.4) / 3.0, [(500, 600)], (1400, 560), n=14, seed=4)
    if t > 106.2:
        T(c, "₹20,000 / DAY", 1400, 180, 80, GRN, k(t, 106.2, 106.5))
    if t > 107.6:
        T(c, "₹4 LAKH / MONTH", 1400, 1010, 70, YEL, k(t, 107.6, 107.9))
    return 'money'


def from_render3_broker(c, x, y, s):
    c.save(); c.translate(x, y); c.scale(s, s)
    c.move_to(-170, -90); c.line_to(0, -190); c.line_to(170, -90); c.close_path()
    c.set_source_rgb(0.85, 0.87, 0.92); c.fill()
    S.rrect(c, -160, -90, 320, 230, 10)
    c.set_source_rgb(0.75, 0.78, 0.85); c.fill()
    for i in range(4):
        S.rrect(c, -130 + i * 70, -60, 40, 150, 6)
        c.set_source_rgb(0.55, 0.58, 0.66); c.fill()
    S.rrect(c, -150, 150, 300, 70, 14)
    c.set_source_rgb(0.08, 0.09, 0.14); c.fill()
    T(c, "BROKER", 0, 200, 46, YEL, stroke=None)
    c.restore()


def sh_telegram(c, t, lt):
    V.room(c, t, 'night')
    U.dim(c, 0.6)
    mem = int(2000 * k(t, 113.2, 114.6))
    U.phone_frame(c, 260, 40, 540, 1000, U.scr_telegram(mem, k(t, 109.3, 117.5)), t, tilt=-2)
    if t > 110.9:
        T(c, "₹999", 1360, 320, 120, WHITE, k(t, 110.9, 111.2))
        T(c, "/ month", 1360, 400, 46, (0.8, 0.82, 0.9), k(t, 111.2, 111.5), stroke=None)
    if t > 113.2:
        T(c, f"× {mem:,} members", 1360, 520, 56, WHITE, k(t, 113.2, 113.5))
    if t > 115.0:
        T(c, "= ₹20 LAKH / month", 1360, 660, 72, GRN, k(t, 115.0, 115.3))
    if t > 117.6:
        P.stamp(c, "NO REFUND", 1360, 850, 117.7, t, -6, RED, 80)
    return 'phone'


def sh_bhai_risk(c, t, lt):
    V.studio(c, t)
    B.figure(c, 960, 380, 0.75, t, who='bhai', pose='stand', mouth='smirk', talk=talk(t) * 0.8,
             arms=((60, 90), (60, 90)), **{'raise': 0.6})
    T(c, '"Market risk hai bhai"', 960, 980, 64, WHITE, k(t, 119.1, 119.4))
    return 'studio'


def sh_course(c, t, lt):
    V.room(c, t, 'night')
    U.dim(c, 0.55)
    U.laptop(c, 460, 120, 1000, 620, U.scr_course(1), t)
    if t > 125.8:
        U.dim(c, 0.4 * k(t, 125.8, 126.1))
        n = int(500 * k(t, 125.9, 127.3))
        for i in range(min(n, 200)):
            U.ppl(c, 200 + (i % 25) * 62, 170 + (i // 25) * 66, 40, GRN)
        T(c, f"{n} students", 960, 760, 60, WHITE)
    if t > 127.5:
        T(c, "× ₹15,000 = ₹75 LAKH", 960, 870, 80, YEL, k(t, 127.5, 127.8))
    return 'night'


def sh_youtube(c, t, lt):
    V.studio(c, t)
    U.dim(c, 0.7)
    views = int(250000 * k(t, 131.5, 134.5))
    U.laptop(c, 360, 90, 1200, 680, U.scr_youtube(views, k(t, 130.4, 132.6)), t)
    return 'studio'


def sh_hope(c, t, lt):
    V.room(c, t, 'night')
    B.figure(c, 960, 360, 0.85, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1.0, mouth='flat',
             look=(0.5, 0.2), eyes=1.1)
    T(c, "YOUR HOPE", 960, 220, 110, YEL, k(t, 136.0, 136.3))
    return 'phone'


def sh_story(c, t, lt):
    V.room(c, t, 'night')
    U.dim(c, 0.65)
    T(c, "#5 SCREENSHOTS", 960, 150, 70, YEL, k(t, 137.4, 137.7))
    U.phone_frame(c, 330, 200, 460, 780, U.scr_story('+'), t, tilt=-4)
    if t > 142.1:
        U.phone_frame(c, 1110, 200, 460, 780, U.scr_story('-'), t, tilt=4)
        if t > 142.6:
            c.set_line_width(26)
            c.set_source_rgb(*RED)
            c.move_to(1110, 200); c.line_to(1590, 1000); c.stroke()
            c.move_to(1590, 200); c.line_to(1110, 1000); c.stroke()
            T(c, "NEVER POSTED", 1350, 620, 64, WHITE, k(t, 142.6, 142.9))
    return 'phone'


def sh_accounts(c, t, lt):
    V.studio(c, t)
    U.dim(c, 0.7)
    for i in range(4):
        pnl = [-42000, -18500, 61200, -27300][i]
        x = 140 + i * 430
        a = 1.0 if (t < 146.8 or i == 2) else 0.25
        c.push_group()
        U.phone_frame(c, x, 180, 360, 680, U.scr_pnl(pnl, seed=20 + i, label=f"ACCOUNT {i + 1}"), t, tilt=0, glow=0)
        c.pop_group_to_source()
        c.paint_with_alpha(a)
    if t > 146.8:
        T(c, "only this one gets posted", 1210, 130, 50, GRN, k(t, 146.8, 147.1))
    return 'night'


def sh_twist(c, t, lt):
    V.studio(c, t)
    U.dim(c, 0.82)
    for i, (a, b) in enumerate(CARDS):
        U.icon_card(c, 110 + i * 350, 330, 320, 420, i + 1, a, b, 1.0, stamp=k(t, 151.5 + i * 0.3, 151.7 + i * 0.3))
    T(c, "Not ONE needs him to win a trade", 960, 900, 62, WHITE, k(t, 150.0, 150.3))
    return 'studio'


def sh_you_daily(c, t, lt):
    V.room(c, t, 'night')
    B.figure(c, 960, 340, 0.7, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=1.2, mouth='flat',
             eyes=0.7, bags=1, look=(0.5, 0.3))
    for i, (w, t0) in enumerate((("YOU.", 158.6), ("DAILY.", 159.5), ("TRADING.", 160.0))):
        T(c, w, 420 + i * 540, 250, 100, YEL if i == 0 else WHITE, k(t, t0, t0 + 0.2))
    return 'phone'


def sh_sebi_rule(c, t, lt):
    V.studio(c, t)
    U.dim(c, 0.85)
    P.doc_sebi(c, 120, 160, 560, 760, 1.0)
    T(c, "2024 · SEBI", 1250, 220, 80, YEL, k(t, 163.1, 163.4))
    from_render3_broker(c, 1000, 560, 0.8)
    B.figure(c, 1560, 380, 0.42, t, who='bhai', pose='stand', mouth='o' if t > 168.3 else 'smirk')
    cut = t > 168.3
    for i in range(7):
        x = 1150 + i * 45
        if cut and i == 3:
            continue
        c.save(); c.translate(x, 560); c.scale(1, 0.6)
        c.arc(0, 0, 24, 0, 2 * math.pi); c.restore()
        c.set_source_rgb(0.95, 0.75, 0.22); c.set_line_width(12); c.stroke()
    if cut:
        c.set_line_width(22); c.set_source_rgb(*RED)
        for d in (-1, 1):
            c.move_to(1240, 560 + d * 60); c.line_to(1340, 560 - d * 60); c.stroke()
        T(c, "NO MORE PAYMENTS", 1250, 900, 64, RED, k(t, 168.3, 168.6))
    return 'night'


def sh_ban(c, t, lt, when, amt, label):
    V.studio(c, t)
    U.dim(c, 0.85)
    T(c, when, 960, 200, 70, (0.85, 0.87, 0.95))
    T(c, label, 960, 300, 50, WHITE, stroke=None)
    v = int(amt * k(t, s_(when) + 1.2, s_(when) + 3.4))
    T(c, f"₹{v:,} CRORE", 960, 560, 150, RED)
    T(c, "IMPOUNDED", 960, 700, 70, WHITE, k(t, s_(when) + 3.4, s_(when) + 3.7))
    # gavel
    ang = -0.6 + 0.6 * min(1, max(0, (t - s_(when) - 3.3) / 0.15))
    c.save(); c.translate(1550, 860); c.rotate(ang)
    S.rrect(c, -20, -200, 40, 220, 12); c.set_source_rgb(0.45, 0.28, 0.15); c.fill()
    S.rrect(c, -90, -260, 180, 80, 20); c.set_source_rgb(0.55, 0.34, 0.18); c.fill()
    c.restore()
    return 'red'


def s_(when):
    return s(34) if when.startswith("FEB") else s(35)


def sh_ban1(c, t, lt):
    return sh_ban(c, t, lt, "FEB 2025", 53, "SEBI banned a finfluencer + 5 others")


def sh_ban2(c, t, lt):
    return sh_ban(c, t, lt, "DEC 2025", 546, "A trading academy · unregistered advice")


QS = ["Is he SEBI REGISTERED?", "Does he show his FULL P&L?", "Does he push you to trade DAILY?"]


def sh_walk_qs(c, t, lt):
    off = (t - s(36)) * 140
    V.street(c, t, off, night=False)
    B.figure(c, 640, 330, 0.55, t, pose='walk', ph=(t - s(36)) * 0.9, mouth='flat', look=(0.3, 0), **{'raise': 0.2})
    S.rrect(c, 1000, 140, 840, 470, 30)
    c.set_source_rgba(0.05, 0.06, 0.1, 0.88)
    c.fill()
    T(c, "ASK 3 QUESTIONS", 1420, 220, 54, YEL, stroke=None)
    for i, (q, t0) in enumerate(zip(QS, (s(37), s(38), s(39)))):
        a = k(t, t0, t0 + 0.3)
        c.arc(1070, 310 + i * 100, 28, 0, 2 * math.pi)
        c.set_source_rgba(*YEL, a); c.fill()
        T(c, str(i + 1), 1070, 322 + i * 100, 32, (0.1, 0.1, 0.1), a, stroke=None)
        T(c, q, 1120, 322 + i * 100, 38, WHITE, a, stroke=None, anchor="left")
    return 'day'


def sh_q1(c, t, lt):
    V.room(c, t, 'day')
    U.dim(c, 0.5)

    def scr(c2, w, h, tt):
        U.scr_fill(c2, w, h, (0.97, 0.97, 0.99))
        c2.rectangle(0, 0, w, 90); c2.set_source_rgb(0.12, 0.2, 0.45); c2.fill()
        T(c2, "SEBI · Registered Intermediaries", 30, 58, 30, WHITE, stroke=None, anchor="left")
        S.rrect(c2, 40, 140, w - 80, 70, 10); c2.set_source_rgb(0.9, 0.91, 0.95); c2.fill()
        T(c2, "Search: name / registration no.", 60, 185, 26, (0.4, 0.4, 0.5), stroke=None, anchor="left", bold=False)
        if tt > s(37) + 2.4:
            S.rrect(c2, 40, 250, w - 80, 160, 12); c2.set_source_rgb(1, 0.92, 0.92); c2.fill()
            T(c2, "No registered adviser found", w / 2, 345, 40, RED, stroke=None)
    U.laptop(c, 460, 140, 1000, 600, scr, t)
    T(c, "1. Is he SEBI registered?", 960, 90, 60, YEL)
    return 'day'


def sh_q2(c, t, lt):
    V.room(c, t, 'day')
    U.dim(c, 0.5)
    pts = [0.5, 0.55, 0.48, 0.62, 0.4, 0.35, 0.5, 0.3, 0.25, 0.32, 0.2, 0.15]

    def scr(c2, w, h, tt):
        U.scr_fill(c2, w, h, (0.06, 0.07, 0.1))
        T(c2, "FULL YEAR P&L", w / 2, 70, 40, WHITE, stroke=None)
        n = int(len(pts) * k(tt, s(38) + 0.5, s(38) + 3.5)) + 1
        c2.move_to(60, 120 + pts[0] * (h - 180))
        for i in range(1, min(n, len(pts))):
            c2.line_to(60 + i * (w - 120) / (len(pts) - 1), 120 + (1 - pts[i]) * (h - 180) * 0.9)
        c2.set_source_rgb(*RED); c2.set_line_width(8); c2.stroke()
    U.laptop(c, 460, 140, 1000, 600, scr, t)
    T(c, "2. Full P&L - not just wins", 960, 90, 60, YEL)
    return 'day'


def sh_q3(c, t, lt):
    V.room(c, t, 'day')
    B.figure(c, 760, 330, 0.55, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=0.3, mouth='flat', squint=0.4)
    for i, m in enumerate(("ENTER NOW!", "Don't miss today's move", "Last chance, BN 500 pts", "Trade again tomorrow")):
        a = k(t, s(39) + 0.4 + i * 0.6, s(39) + 0.7 + i * 0.6)
        S.rrect(c, 1180, 160 + i * 150, 620, 120, 24)
        c.set_source_rgba(0.95, 0.95, 0.97, 0.95 * a); c.fill()
        T(c, "LIVE BHAI", 1210, 205 + i * 150, 24, (0.5, 0.1, 0.15), a, stroke=None, anchor="left")
        T(c, m, 1210, 250 + i * 150, 32, (0.1, 0.1, 0.12), a, stroke=None, anchor="left")
    T(c, "3. Pushes you to trade daily?", 960, 90, 60, YEL)
    return 'day'


def sh_morning(c, t, lt):
    V.room(c, t, 'day')
    B.figure(c, 900, 330, 0.55, t, pose='sit', phone=1, arms=((14, -10), (30, 150)), glow=0.2, mouth='smile')

    def scr(c2, w, h, tt):
        U.scr_fill(c2, w, h, (0.96, 0.96, 0.98))
        T(c2, "Notifications", w / 2, 90, 32, (0.1, 0.1, 0.12), stroke=None)
        S.rrect(c2, 30, 150, w - 60, 100, 18); c2.set_source_rgb(0.9, 0.91, 0.95); c2.fill()
        T(c2, "Live alerts", 60, 212, 30, (0.1, 0.1, 0.12), stroke=None, anchor="left")
        on = tt < s(40) + 3.6
        S.rrect(c2, w - 150, 172, 100, 56, 28); c2.set_source_rgb(*(GRN if on else (0.7, 0.7, 0.74))); c2.fill()
        c2.arc(w - 122 + (44 if on else 0), 200, 22, 0, 2 * math.pi); c2.set_source_rgb(1, 1, 1); c2.fill()
    U.phone_frame(c, 1280, 120, 420, 780, scr, t, tilt=3, glow=0)
    return 'morning'


def sh_window(c, t, lt):
    V.room(c, t, 'day')
    B.figure(c, 420, 300, 0.6, t, pose='stand', mouth='smile', look=(-0.6, -0.2))
    if t > s(41) + 3.4:
        T(c, "Blind daily trading is the problem.", 1180, 120, 54, WHITE, k(t, s(41) + 3.4, s(41) + 3.7))
    return 'morning'


def sh_split(c, t, lt):
    V.studio(c, t)
    c.save(); c.rectangle(960, 0, 960, 1080); c.clip()
    V.room(c, t, 'night')
    c.restore()
    c.rectangle(955, 0, 10, 1080); c.set_source_rgb(1, 1, 1); c.fill()
    stop = t > s(42) + 3.6
    B.figure(c, 480, 380, 0.55, t, who='bhai', pose='stand', mouth='o' if stop else 'bigsmile')
    B.figure(c, 1440, 380, 0.55, t, pose='stand', mouth='smile' if stop else 'flat',
             phone=None if stop else 1, arms=((14, -10), (14, -10)) if stop else ((14, -10), (30, 150)), glow=0.5)
    T(c, "HIS INCOME", 480, 160, 60, YEL)
    T(c, "YOUR TRADES", 1440, 160, 60, WHITE)
    if stop:
        P.stamp(c, "STOPPED", 480, 900, s(42) + 3.6, t, -6, RED, 90)
    return 'warm'


def sh_end(c, t, lt):
    V.room(c, t, 'day')
    U.dim(c, 0.35)
    B.figure(c, 960, 380, 0.72, t, pose='stand', mouth='smile', arms=((14, -10), (100, 40)), blush=0.3)
    S.rrect(c, 120, 200, 560, 200, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9 * k(t, 225.5, 225.8)); c.fill()
    T(c, "How much did you lose", 400, 280, 40, WHITE, k(t, 225.5, 225.8), stroke=None)
    T(c, "following live streams?", 400, 340, 40, YEL, k(t, 225.5, 225.8), stroke=None)
    S.rrect(c, 1240, 200, 560, 200, 30); c.set_source_rgba(0.05, 0.06, 0.1, 0.9 * k(t, 227.8, 228.1)); c.fill()
    T(c, "SEND THIS TO", 1520, 280, 46, WHITE, k(t, 227.8, 228.1), stroke=None)
    T(c, "THAT FRIEND", 1520, 345, 52, YEL, k(t, 227.8, 228.1), stroke=None)
    S.rrect(c, 820, 80, 280, 70, 35); c.set_source_rgb(0.06, 0.06, 0.08); c.fill_preserve()
    c.set_source_rgb(*YEL); c.set_line_width(4); c.stroke()
    T(c, "SAME BRO", 960, 128, 40, YEL, stroke=None)
    return 'end'


# (start, end, fn, cam0(z,x,y,rot), cam1, whip)
X = None
SHOTS = [
    (0.0, 2.2, sh_room_wide, (1.0, 960, 540, 0), (1.12, 1000, 560, 0), 0),
    (2.2, 4.7, sh_room_close, (2.4, 1010, 460, -2), (2.7, 1000, 430, 1), 1),
    (4.7, 9.6, sh_live_phone, (1.15, 960, 560, 0), (1.0, 960, 540, 0), -1),
    (9.6, 13.5, sh_sid_think, (1.5, 1150, 400, 2), (1.6, 1200, 380, -1), 1),
    (13.5, 17.3, sh_bhai_cash, (1.0, 960, 540, -2), (1.25, 960, 520, 2), -1),
    (17.3, 21.1, sh_title, (1.08, 960, 540, 0), (1.0, 960, 540, 0), 1),
    (21.1, 22.58, sh_from_you, (1.15, 960, 520, 0), (1.05, 960, 540, 0), 0),
    (22.58, 26.56, sh_metro, (1.1, 820, 560, 0), (1.2, 1150, 540, 0), 1),
    (26.56, 30.48, sh_canteen, (1.0, 960, 560, 0), (1.35, 900, 480, 0), -1),
    (30.48, 33.2, sh_signup, (1.0, 960, 540, 0), (1.2, 960, 600, 0), 1),
    (33.2, 35.17, sh_bhai_smirk, (1.3, 960, 420, 3), (1.15, 960, 450, -2), 0),
    (35.17, 40.0, sh_win_week, (1.1, 860, 540, 0), (1.15, 1200, 520, 0), -1),
    (40.0, 46.16, sh_crash, (1.1, 1000, 540, 0), (1.3, 1000, 520, 4), 1),
    (46.16, 48.96, sh_borrow, (1.0, 960, 540, 0), (1.2, 960, 500, 0), -1),
    (48.96, 53.73, sh_walk_home, (1.25, 900, 600, 0), (1.25, 900, 600, 0), 1),
    (53.73, 57.36, sh_noob, (1.4, 980, 460, -2), (1.2, 960, 520, 2), -1),
    (57.36, 65.84, sh_data91, (1.0, 960, 560, 0), (1.06, 960, 540, 0), 1),
    (65.84, 75.68, sh_data43, (1.0, 960, 540, 0), (1.05, 960, 580, 0), -1),
    (75.68, 79.04, sh_nine_of_ten, (1.05, 960, 560, 0), (1.0, 960, 540, 0), 1),
    (79.04, 85.33, sh_bhai_wins, (1.0, 900, 540, -2), (1.2, 1000, 520, 2), -1),
    (85.33, 91.09, sh_five, (1.0, 960, 560, 0), (1.0, 960, 540, 0), 1),
    (91.09, 94.04, sh_bhai_link, (1.25, 860, 520, 0), (1.35, 900, 500, 0), 0),
    (94.04, 102.56, sh_funnel, (1.0, 960, 500, 0), (1.05, 960, 580, 0), 1),
    (102.56, 109.2, sh_brokerage, (1.0, 960, 540, 0), (1.08, 1000, 520, 0), -1),
    (109.2, 118.9, sh_telegram, (1.05, 800, 540, 0), (1.05, 1100, 560, 0), 1),
    (118.9, 120.72, sh_bhai_risk, (1.35, 960, 450, 2), (1.45, 960, 440, -2), 0),
    (120.72, 129.81, sh_course, (1.0, 960, 480, 0), (1.08, 960, 560, 0), -1),
    (129.81, 135.9, sh_youtube, (1.0, 960, 460, 0), (1.12, 960, 460, 0), 1),
    (135.9, 137.36, sh_hope, (1.2, 960, 480, 0), (1.35, 960, 420, 0), 0),
    (137.36, 144.24, sh_story, (1.0, 960, 560, 0), (1.05, 1150, 560, 0), -1),
    (144.24, 148.69, sh_accounts, (1.0, 960, 540, 0), (1.15, 1200, 540, 0), 1),
    (148.69, 153.96, sh_twist, (1.0, 960, 560, 0), (1.0, 960, 540, 0), -1),
    (153.96, 161.2, sh_you_daily, (1.0, 960, 540, 0), (1.25, 960, 500, 0), 1),
    (161.2, 170.58, sh_sebi_rule, (1.0, 960, 540, 0), (1.05, 1000, 540, 0), -1),
    (170.58, 178.0, sh_ban1, (1.1, 960, 560, -1), (1.0, 960, 540, 1), 1),
    (178.0, 185.24, sh_ban2, (1.1, 960, 560, 1), (1.0, 960, 540, -1), -1),
    (185.24, 189.28, sh_walk_qs, (1.0, 960, 540, 0), (1.08, 1100, 500, 0), 1),
    (189.28, 195.2, sh_q1, (1.0, 960, 560, 0), (1.12, 960, 520, 0), -1),
    (195.2, 200.96, sh_q2, (1.0, 960, 560, 0), (1.12, 960, 520, 0), 1),
    (200.96, 207.76, sh_q3, (1.05, 1000, 560, 0), (1.12, 1300, 520, 0), -1),
    (207.76, 212.76, sh_morning, (1.05, 1000, 540, 0), (1.2, 1150, 520, 0), 1),
    (212.76, 219.0, sh_window, (1.0, 960, 540, 0), (1.15, 700, 500, 0), -1),
    (219.0, 225.48, sh_split, (1.0, 960, 540, 0), (1.06, 960, 540, 0), 1),
    (225.48, 235.0, sh_end, (1.15, 960, 520, 0), (1.0, 960, 540, 0), -1),
]

CAPS_EN = [
    "It's 11:30 PM. Sid's in bed, watching a live stream.",
    "\"Guys, tomorrow's setup is READY. Join the premium group, link in description.\"",
    "Sid thinks... this guy wins every day. Why not me?",
    "Today I'll show you how live traders REALLY make money. They earn way more from YOU than from trading.",
    "Sid's story is simple. First internship money: ₹15,000.",
    "In the canteen, a friend showed his phone: \"₹8,000 profit today.\"",
    "That night Sid opened an account. Whose link? The live guy's link.",
    "First week? Amazing. 2-3 trades in PROFIT. Screenshot straight to the group.",
    "Then the market turned. \"One trade, I'll recover.\" Lot DOUBLED.",
    "That went too. Then borrowed ₹5,000 from a friend.",
    "Three weeks. ₹15,000 → ZERO. Nobody at home knows.",
    "Now you'll say Sid was a noob. Fine. Let's look at the DATA.",
    "SEBI study: in FY25, 91% of F&O traders LOST money. Average loss: ₹1.1 LAKH.",
    "Scarier: in FY26, 43% of F&O traders were UNDER 30. And 89% of them lost.",
    "That's 9 out of 10 young traders LOSING.",
    "So if 9 out of 10 lose... how does the live guy win EVERY day?",
    "Because his real business isn't trading. He has FIVE incomes.",
    "#1: REFERRAL. \"Open an account with my link.\"",
    "Say 1 lakh subscribers. 10,000 open accounts. 1,000 trade daily: 10 orders × ₹20 brokerage.",
    "₹2 LAKH brokerage a day. Even 10% = ₹20,000 a day. ₹4 LAKH a month.",
    "#2: PREMIUM Telegram group. ₹999 a month.",
    "Just 2,000 members = ₹20 LAKH a month.",
    "Calls went wrong? No refund. \"Market risk, bro.\"",
    "#3: COURSES. \"Become a trader like me.\" ₹15,000 per course.",
    "500 students in one batch = ₹75 LAKH. From ONE batch.",
    "#4: ads, sponsors, super chats. More views, more money. And the views come from YOUR hope.",
    "And #5, the smartest: SCREENSHOTS.",
    "Profit screenshot? On the story. Loss screenshot? Ever seen one?",
    "Some run MULTIPLE accounts and show only the green one.",
    "Look closely. NOT ONE of these five incomes needs him to win trades.",
    "Win or lose, his money keeps coming. He needs one thing: YOU, trading DAILY.",
    "And this isn't just my theory.",
    "2024: SEBI barred registered brokers & companies from paying unregistered finfluencers.",
    "Feb 2025: SEBI banned a finfluencer + 5 others, impounded ₹53+ CRORE.",
    "Dec 2025: ₹546 CRORE impounded from a trading academy for unregistered advice.",
    "Next time someone says \"enter now\", ask 3 questions.",
    "1: Is he SEBI REGISTERED? Check on SEBI's website. Takes 2 minutes.",
    "2: Does he show his FULL P&L? Not just wins. The whole year.",
    "3: Does he push you to trade DAILY? Then you know where his money comes from.",
    "Today Sid closed the live. Didn't delete the app, just turned off the alerts.",
    "The market isn't bad. Trading daily on someone else's word, without understanding... THAT is.",
    "He goes live every day because YOU trade every day. The day you stop, his income stops.",
    "Comment: how much did you lose following live streams? Send this to the friend who needs it.",
]


def caption(c, t):
    for n in range(1, len(L)):
        a, b = L[n]
        if a - 0.05 <= t <= b + 0.25:
            txt = CAPS_EN[n - 1]
            c.select_font_face("Poppins", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            size = 40
            c.set_font_size(size)
            words, lines, cur = txt.split(" "), [], []
            for w in words:
                if c.text_extents(" ".join(cur + [w])).x_advance > 1500 and cur:
                    lines.append(cur); cur = [w]
                else:
                    cur.append(w)
            lines.append(cur)
            lh = size * 1.25
            y0 = 1035 - (len(lines) - 1) * lh
            sp = c.text_extents("a a").x_advance - c.text_extents("aa").x_advance
            for i, ln in enumerate(lines):
                wd = [c.text_extents(w).x_advance for w in ln]
                x = 960 - (sum(wd) + sp * (len(ln) - 1)) / 2
                for w, d in zip(ln, wd):
                    core = w.strip('".,:?!\'')
                    hi = (core.isupper() and len(core) > 1) or "₹" in w or "%" in w
                    c.move_to(x, y0 + i * lh)
                    c.text_path(w)
                    c.set_source_rgb(0, 0, 0)
                    c.set_line_width(8)
                    c.set_line_join(cairo.LINE_JOIN_ROUND)
                    c.stroke_preserve()
                    c.set_source_rgb(*(YEL if hi else (1, 1, 1)))
                    c.fill()
                    x += d + sp
            return


def disclaimer(c, t):
    if 94.0 <= t <= 148.7:
        txt = "Example numbers for illustration · not about any specific person"
    elif 57.3 <= t <= 79 or 161 <= t <= 185.3:
        txt = "Source: SEBI studies & orders"
    elif t >= 225.4:
        txt = "Not financial advice"
    else:
        return
    S.rrect(c, 560, 18, 800, 44, 22)
    c.set_source_rgba(0, 0, 0, 0.55)
    c.fill()
    T(c, txt, 960, 48, 22, (0.85, 0.87, 0.95), stroke=None, bold=False)


def hblur(rgb, w):
    if w < 2:
        return rgb
    w = int(w)
    cs = np.cumsum(np.pad(rgb.astype(np.float32), ((0, 0), (w, w), (0, 0)), mode='edge'), axis=1)
    out = (cs[:, 2 * w:] - cs[:, :-2 * w]) / (2 * w)
    return out[:, :rgb.shape[1]].astype(np.uint8)


def render_frame(i):
    t = i / FPS
    idx = next((j for j, sh in enumerate(SHOTS) if sh[0] <= t < sh[1]), len(SHOTS) - 1)
    st, en, fn, c0, c1, wd = SHOTS[idx]
    lt = (t - st) / (en - st)
    tmp = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    c = cairo.Context(tmp)
    grade = fn(c, t, lt)
    ee = S.ease(lt)
    z, fxp, fyp, rot = [a + (b - a) * ee for a, b in zip(c0, c1)]
    fxp += math.sin(t * 1.3) * 5 + math.sin(t * 2.7) * 2
    fyp += math.sin(t * 1.1 + 1) * 4
    rot += math.sin(t * 0.9) * 0.25
    whip = 0.0
    if st > 0 and wd != 0 and t - st < 0.16:
        kk = 1 - (t - st) / 0.16
        fxp -= wd * 500 * kk * kk
        whip = kk
    if idx + 1 < len(SHOTS) and SHOTS[idx + 1][5] != 0 and en - t < 0.09:
        kk = 1 - (en - t) / 0.09
        fxp += SHOTS[idx + 1][5] * 300 * kk * kk
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
    rgb = FX.post(out, grade, i, 0)
    if whip > 0:
        rgb = hblur(rgb, whip * 70)
    if t < 0.4:
        rgb = (rgb.astype(np.float32) * (t / 0.4)).astype(np.uint8)
    ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    oc = cairo.Context(ov)
    disclaimer(oc, t)
    caption(oc, t)
    ov.flush()
    cb = np.ndarray((H, W, 4), np.uint8, ov.get_data())
    a = cb[..., 3:4].astype(np.float32) / 255.0
    return np.clip(rgb.astype(np.float32) * (1 - a) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)


def main():
    if sys.argv[1] != "full":
        for n, tt in enumerate(map(float, sys.argv[1].split(","))):
            Image.fromarray(render_frame(int(tt * FPS))).save(f"p_{n:02d}.png")
        return
    a, b, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                          "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(a, b):
        p.stdin.write(render_frame(i).tobytes())
        if i % 240 == 0:
            print(f"frame {i}/{b}", flush=True)
    p.stdin.close()
    p.wait()


if __name__ == "__main__":
    main()
