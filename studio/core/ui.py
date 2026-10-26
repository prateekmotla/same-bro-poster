"""Screen UIs and info-graphics for the landscape long-form."""
import math
import random
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/v2")
sys.path.insert(0, "/home/claude/sid/v3")
import sid2 as S  # noqa: E402
import props as P  # noqa: E402

YEL, RED, GRN = P.YEL, P.RED, P.GRN
WHITE = (1, 1, 1)
DARK = (0.06, 0.07, 0.1)


def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def k(t, a, b):
    return clamp((t - a) / max(1e-6, b - a))


def eob(x):
    return P.eob(clamp(x))


def T(c, s, x, y, size, col=WHITE, a=1.0, stroke=(0, 0, 0), lw=None, anchor="center", bold=True):
    return P.text(c, s, x, y, size, fill=col, stroke=stroke, lw=lw if lw is not None else max(4, size * 0.14),
                  alpha=a, anchor=anchor, weight=cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)


def dim(c, a=0.6):
    c.set_source_rgba(0.01, 0.01, 0.03, a)
    c.paint()


def phone_frame(c, x, y, w, h, screen, t, tilt=0.0, glow=0.3):
    """screen(c, w, h, t) draws inside the local screen rect (0,0,w,h)."""
    c.save()
    c.translate(x + w / 2, y + h / 2)
    c.rotate(math.radians(tilt))
    c.translate(-w / 2, -h / 2)
    if glow:
        g = cairo.RadialGradient(w / 2, h / 2, 10, w / 2, h / 2, max(w, h))
        g.add_color_stop_rgba(0, 0.6, 0.8, 1, glow * 0.5)
        g.add_color_stop_rgba(1, 0.6, 0.8, 1, 0)
        c.set_source(g)
        c.arc(w / 2, h / 2, max(w, h), 0, 2 * math.pi)
        c.fill()
    S.rrect(c, -14, -14, w + 28, h + 28, 46)
    c.set_source_rgb(0.04, 0.04, 0.05)
    c.fill()
    S.rrect(c, 0, 0, w, h, 34)
    c.save()
    c.clip()
    screen(c, w, h, t)
    c.restore()
    S.rrect(c, w / 2 - 60, 12, 120, 26, 13)
    c.set_source_rgb(0.02, 0.02, 0.02)
    c.fill()
    c.restore()


def laptop(c, x, y, w, h, screen, t):
    c.save()
    c.translate(x, y)
    S.rrect(c, -20, -20, w + 40, h + 40, 20)
    c.set_source_rgb(0.12, 0.13, 0.16)
    c.fill()
    c.rectangle(0, 0, w, h)
    c.save()
    c.clip()
    screen(c, w, h, t)
    c.restore()
    c.move_to(-90, h + 20)
    c.line_to(w + 90, h + 20)
    c.line_to(w + 140, h + 70)
    c.line_to(-140, h + 70)
    c.close_path()
    c.set_source_rgb(0.62, 0.64, 0.68)
    c.fill()
    c.restore()


# ---------------- screens -----------------
def scr_fill(c, w, h, col):
    c.rectangle(0, 0, w, h)
    c.set_source_rgb(*col)
    c.fill()


def scr_live(chat, viewers="48.2K", talk=0.0, t=0.0):
    import body as B
    import env as V

    def f(c, w, h, tt):
        c.save()
        sc = h / 1080
        c.translate(w / 2 - 960 * sc, 0)
        c.scale(sc, sc)
        V.studio(c, tt)
        B.figure(c, 960, 360, 0.62, tt, who='bhai', pose='stand', mouth='bigsmile', talk=talk,
                 arms=((40, 100), (12, -8)))
        c.restore()
        S.rrect(c, 20, 60, 110, 44, 10)
        c.set_source_rgb(*RED)
        c.fill()
        T(c, "LIVE", 75, 92, 28, stroke=None)
        T(c, viewers + " watching", 150, 92, 24, stroke=None, anchor="left")
        for i, m in enumerate(chat):
            yy = h - 60 - i * 54
            S.rrect(c, 16, yy - 34, w - 32, 46, 14)
            c.set_source_rgba(0, 0, 0, 0.55)
            c.fill()
            T(c, m, 34, yy, 22, stroke=None, anchor="left", bold=False)
    return f


def scr_sms(amount_k):
    def f(c, w, h, t):
        scr_fill(c, w, h, (0.95, 0.96, 0.98))
        T(c, "Messages", w / 2, 90, 30, (0.1, 0.1, 0.12), stroke=None)
        S.rrect(c, 24, 160, w - 48, 200 * amount_k + 1, 24)
        c.set_source_rgb(0.88, 0.9, 0.95)
        c.fill()
        if amount_k > 0.5:
            T(c, "BANK", 50, 210, 24, (0.2, 0.3, 0.6), stroke=None, anchor="left")
            T(c, "Salary credited", 50, 260, 30, (0.1, 0.1, 0.12), stroke=None, anchor="left")
            T(c, "₹15,000", 50, 320, 52, (0.1, 0.55, 0.3), stroke=None, anchor="left")
    return f


def scr_pnl(pnl, label="NIFTY CE", crash=None, seed=3, k_chart=1.0):
    def f(c, w, h, t):
        scr_fill(c, w, h, (0.06, 0.07, 0.1))
        T(c, label, w / 2, 80, 28, (0.8, 0.82, 0.9), stroke=None)
        P.candles(c, 20, 120, w - 40, h * 0.42, seed=seed, n=16, crash=crash, grow=k_chart)
        col = GRN if pnl >= 0 else RED
        T(c, "P&L", w / 2, h * 0.68, 28, (0.7, 0.72, 0.8), stroke=None)
        T(c, ("+" if pnl >= 0 else "−") + f"₹{abs(int(pnl)):,}", w / 2, h * 0.68 + 80, 64, col, stroke=None)
        for i, (lab, cc) in enumerate((("BUY", GRN), ("SELL", RED))):
            S.rrect(c, 30 + i * (w / 2 - 15), h - 120, w / 2 - 45, 70, 16)
            c.set_source_rgb(*cc)
            c.fill()
            T(c, lab, 30 + i * (w / 2 - 15) + (w / 2 - 45) / 2, h - 72, 30, stroke=None)
    return f


def scr_signup(k_):
    def f(c, w, h, t):
        scr_fill(c, w, h, (0.97, 0.97, 0.99))
        T(c, "Open Demat Account", w / 2, 110, 32, (0.1, 0.1, 0.15), stroke=None)
        for i, lab in enumerate(("Mobile number", "PAN", "Referral code")):
            S.rrect(c, 30, 170 + i * 120, w - 60, 80, 14)
            c.set_source_rgb(0.9, 0.91, 0.95)
            c.fill()
            T(c, lab, 50, 160 + i * 120, 20, (0.4, 0.4, 0.5), stroke=None, anchor="left", bold=False)
        if k_ > 0:
            S.rrect(c, 30, 410, w - 60, 80, 14)
            c.set_source_rgba(1, 0.8, 0.16, 0.5 * k_)
            c.fill()
            T(c, "LIVEBHAI100", 50, 462, 32, (0.1, 0.1, 0.15), stroke=None, anchor="left")
        S.rrect(c, 30, h - 150, w - 60, 90, 45)
        c.set_source_rgb(0.15, 0.45, 0.95)
        c.fill()
        T(c, "Continue", w / 2, h - 92, 34, stroke=None)
    return f


def scr_chat(title, msgs, k_=1.0):
    """msgs: list of (text, mine:bool, kind) kind: 'txt' or 'pnl+' or 'pnl-'."""
    def f(c, w, h, t):
        scr_fill(c, w, h, (0.07, 0.1, 0.12))
        c.rectangle(0, 0, w, 120)
        c.set_source_rgb(0.12, 0.2, 0.22)
        c.fill()
        T(c, title, w / 2, 90, 30, stroke=None)
        n = int(len(msgs) * clamp(k_) + 0.999)
        y = 170
        for i, (m, mine, kind) in enumerate(msgs[:n]):
            bh = 150 if kind.startswith('pnl') else 64
            bw = w * 0.72
            x = w - bw - 20 if mine else 20
            S.rrect(c, x, y, bw, bh, 18)
            c.set_source_rgb(*((0.1, 0.4, 0.3) if mine else (0.17, 0.2, 0.24)))
            c.fill()
            if kind.startswith('pnl'):
                S.rrect(c, x + 14, y + 14, bw - 28, bh - 28, 12)
                c.set_source_rgb(0.05, 0.06, 0.08)
                c.fill()
                T(c, m, x + bw / 2, y + bh / 2 + 18, 48, GRN if kind == 'pnl+' else RED, stroke=None)
            else:
                T(c, m, x + 22, y + 42, 26, stroke=None, anchor="left", bold=False)
            y += bh + 18
    return f


def scr_telegram(members, k_):
    def f(c, w, h, t):
        scr_fill(c, w, h, (0.09, 0.12, 0.17))
        c.rectangle(0, 0, w, 150)
        c.set_source_rgb(0.15, 0.32, 0.5)
        c.fill()
        T(c, "PREMIUM CALLS VIP", w / 2, 80, 30, stroke=None)
        T(c, f"{members:,} members", w / 2, 122, 24, (0.8, 0.9, 1), stroke=None, bold=False)
        for i, (m, col) in enumerate((("BN 48000 CE  BUY NOW", GRN), ("Target 200 HIT", GRN), ("SL hit. Market risk.", RED),
                                      ("Join VIP: ₹999/month", YEL))):
            if k_ * 4 > i:
                S.rrect(c, 24, 190 + i * 110, w - 48, 86, 18)
                c.set_source_rgb(0.15, 0.19, 0.25)
                c.fill()
                T(c, m, 44, 245 + i * 110, 28, col, stroke=None, anchor="left")
    return f


def scr_course(k_):
    def f(c, w, h, t):
        scr_fill(c, w, h, (0.07, 0.06, 0.12))
        g = cairo.LinearGradient(0, 0, w, h)
        g.add_color_stop_rgb(0, 0.45, 0.1, 0.6)
        g.add_color_stop_rgb(1, 0.1, 0.1, 0.4)
        c.set_source(g)
        c.rectangle(0, 0, w, h * 0.55)
        c.fill()
        T(c, "BECOME A PRO TRADER", w / 2, h * 0.2, 54, YEL)
        T(c, "in 30 days", w / 2, h * 0.31, 34, stroke=None, bold=False)
        T(c, "₹15,000", w / 2, h * 0.47, 70, WHITE)
        S.rrect(c, w / 2 - 200, h * 0.62, 400, 90, 45)
        c.set_source_rgb(*GRN)
        c.fill()
        T(c, "ENROLL NOW", w / 2, h * 0.62 + 60, 36, stroke=None)
        T(c, "Seats left: 3 (hurry!)", w / 2, h * 0.84, 30, RED, stroke=None)
    return f


def scr_youtube(views, k_):
    def f(c, w, h, t):
        scr_fill(c, w, h, (0.06, 0.06, 0.06))
        c.rectangle(0, 0, w, h * 0.62)
        c.set_source_rgb(0.15, 0.08, 0.2)
        c.fill()
        T(c, "LIVE: BANKNIFTY JACKPOT", w * 0.04, h * 0.72, 40, stroke=None, anchor="left")
        T(c, f"{views:,} views", w * 0.04, h * 0.8, 30, (0.7, 0.7, 0.7), stroke=None, anchor="left", bold=False)
        S.rrect(c, w * 0.6, h * 0.05, w * 0.36, h * 0.12, 12)
        c.set_source_rgb(*YEL)
        c.fill()
        T(c, "SPONSORED", w * 0.78, h * 0.13, 30, (0.1, 0.1, 0.1), stroke=None)
        for i in range(3):
            if k_ * 3 > i:
                S.rrect(c, w * 0.04, h * (0.1 + i * 0.13), w * 0.4, h * 0.1, 14)
                c.set_source_rgb(*[(0.1, 0.6, 0.9), (0.9, 0.5, 0.1), (0.85, 0.15, 0.3)][i])
                c.fill()
                T(c, ["₹100  Sir entry?", "₹500  Love u bhai", "₹2,000  Call pls"][i], w * 0.06, h * (0.165 + i * 0.13), 28,
                  stroke=None, anchor="left")
    return f


def scr_story(kind):
    def f(c, w, h, t):
        scr_fill(c, w, h, (0.1, 0.1, 0.12))
        for i in range(6):
            S.rrect(c, 20 + i * (w - 40) / 6, 30, (w - 40) / 6 - 8, 8, 4)
            c.set_source_rgba(1, 1, 1, 0.9 if i == 0 else 0.35)
            c.fill()
        S.rrect(c, 40, h * 0.2, w - 80, h * 0.5, 24)
        c.set_source_rgb(0.04, 0.05, 0.07)
        c.fill()
        if kind == '+':
            T(c, "+₹54,300", w / 2, h * 0.47, 80, GRN, stroke=None)
            T(c, "Another GREEN day 🟢".replace(" 🟢", ""), w / 2, h * 0.8, 40, stroke=None)
        else:
            T(c, "−₹1,82,000", w / 2, h * 0.47, 80, RED, stroke=None)
    return f


# --------------- info-graphics -----------------
def ppl(c, x, y, s, col, a=1.0):
    c.arc(x, y - s * 0.55, s * 0.28, 0, 2 * math.pi)
    c.set_source_rgba(*col, a)
    c.fill()
    S.rrect(c, x - s * 0.36, y - s * 0.22, s * 0.72, s * 0.62, s * 0.3)
    c.fill()


def bar(c, x, y, w, h, frac, col, label, val):
    S.rrect(c, x, y, w, h, 14)
    c.set_source_rgba(1, 1, 1, 0.08)
    c.fill()
    S.rrect(c, x, y, max(28, w * frac), h, 14)
    c.set_source_rgb(*col)
    c.fill()
    T(c, label, x, y - 20, 34, (0.85, 0.87, 0.95), stroke=None, anchor="left")
    T(c, val, x + max(28, w * frac) + 20, y + h * 0.72, 52, col, stroke=None, anchor="left")


def icon_card(c, x, y, w, h, num, title, sub, k_, col=YEL, stamp=0.0):
    sc = eob(k_)
    if sc <= 0.01:
        return
    c.save()
    c.translate(x + w / 2, y + h / 2)
    c.scale(sc, sc)
    S.rrect(c, -w / 2, -h / 2, w, h, 26)
    c.set_source_rgba(0.07, 0.08, 0.13, 0.95)
    c.fill_preserve()
    c.set_source_rgb(*col)
    c.set_line_width(5)
    c.stroke()
    c.arc(0, -h * 0.25, h * 0.15, 0, 2 * math.pi)
    c.set_source_rgb(*col)
    c.fill()
    T(c, str(num), 0, -h * 0.25 + h * 0.06, h * 0.17, DARK, stroke=None)
    T(c, title, 0, h * 0.08, min(h * 0.13, w * 1.5 / max(1, len(title))), WHITE, stroke=None)
    T(c, sub, 0, h * 0.27, min(h * 0.09, w * 1.6 / max(1, len(sub))), (0.75, 0.78, 0.88), stroke=None, bold=False)
    if stamp > 0:
        c.save()
        c.rotate(-0.2)
        s2 = 1.6 - 0.6 * clamp(stamp)
        c.scale(s2, s2)
        S.rrect(c, -w * 0.45, -h * 0.09, w * 0.9, h * 0.18, 10)
        c.set_source_rgba(*GRN, 0.95)
        c.fill()
        T(c, "NO WIN NEEDED", 0, h * 0.045, h * 0.1, WHITE, stroke=None)
        c.restore()
    c.restore()
