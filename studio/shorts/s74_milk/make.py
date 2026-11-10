"""THEY'RE TRICKING YOU #1: why milk is always at the back of the store.
Sources: NPR Planet Money (2014) — cold-chain / delivery-dock logistics AND 'building the basket' (BJ's dairy buyer:
'we want members or customers to get to the back ... and see the wide array of items'); experts split, NPR: both."""
import math
import sys

import cairo

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

D = "/home/claude/sid/shorts/s74_milk"
CAPS = [
    "Went in just for milk, and the bill came to ₹500? Why is milk ALWAYS at the very back of the store?",
    "Reason 1: LOGISTICS. Trucks unload at the back, and the big cold room is right there. Milk stays cold.",
    "Reason 2: you cross the WHOLE store. Chips, biscuits, offers, all in your face. The industry calls it 'building the basket'.",
    "A big US store chain's dairy buyer said it himself on NPR: we want customers to come to the back and see everything.",
    "So the right answer? BOTH. Even experts are split. But the profit on the extra stuff goes to the store.",
    "The fix is simple. Make a list, go straight to the back, grab the milk, and get out.",
    "Same bro? Next time, can you come back with ONLY milk? Comment.",
]
HOOK = [("WENT FOR MILK.", WHITE), ("BILL = ₹500?", YEL), ("THEY'RE TRICKING YOU #1", GREY)]
SRC = "SRC: NPR Planet Money, 2014"
sh = None

PROD = [(0.9, 0.3, 0.25), (0.95, 0.75, 0.2), (0.3, 0.6, 0.9), (0.35, 0.75, 0.4), (0.9, 0.5, 0.2), (0.7, 0.4, 0.8)]


def store(c, t):
    # back wall
    c.rectangle(0, 0, 1920, 1080); c.set_source_rgb(0.86, 0.87, 0.84); c.fill()
    # dairy fridge wall at the back (glowing)
    c.rectangle(560, 120, 880, 420); c.set_source_rgb(0.75, 0.88, 0.95); c.fill()
    for j in range(5):
        x = 580 + j * 172
        c.rectangle(x, 140, 160, 380); c.set_source_rgba(0.9, 0.97, 1, 0.8); c.fill()
        for r in range(3):
            for q in range(3):
                S.rrect(c, x + 14 + q * 48, 180 + r * 118, 40, 80, 8); c.set_source_rgb(0.97, 0.97, 0.98); c.fill()
                c.rectangle(x + 14 + q * 48, 210 + r * 118, 40, 18); c.set_source_rgb(0.2, 0.45, 0.85); c.fill()
    S.rrect(c, 820, 60, 360, 70, 16); c.set_source_rgb(0.15, 0.4, 0.8); c.fill()
    T(c, "DAIRY", 1000, 112, 48, WHITE, stroke=None)
    # side shelves (perspective-ish)
    for side in (-1, 1):
        for lvl in range(5):
            y = 260 + lvl * 120
            x0 = 1000 + side * 470
            x1 = 1000 + side * 960
            c.move_to(x0, y); c.line_to(x1, y - 40); c.line_to(x1, y + 60); c.line_to(x0, y + 80); c.close_path()
            c.set_source_rgb(0.55, 0.5, 0.45); c.fill()
            for j in range(8):
                f = j / 8
                xx = x0 + (x1 - x0) * f
                h = 70 + 30 * f
                c.rectangle(xx, y - 30 * f - h + 10, side * (40 + 20 * f), h); c.set_source_rgb(*PROD[(j + lvl) % 6]); c.fill()
    # floor
    c.move_to(0, 760); c.line_to(1920, 760); c.line_to(1920, 1080); c.line_to(0, 1080); c.close_path()
    c.set_source_rgb(0.72, 0.72, 0.7); c.fill()
    for x in range(-400, 2400, 160):
        c.move_to(1000 + (x - 1000) * 0.4, 760); c.line_to(x, 1080); c.set_source_rgba(0, 0, 0, 0.08); c.set_line_width(3); c.stroke()


def st_(**kw):
    def f(c, t, lt):
        store(c, t)
        d = dict(pose='stand', mouth='flat')
        d.update(kw)
        K.sid(c, t, 1000, 330, 0.5, **d)
    return f


def sw(**kw):
    def f(c, t, lt):
        V.studio(c, t)
        K.sid(c, t, 960, 330, 0.5, **kw)
    return f


def store_map(c, t, st, prog_t0, prog_dur, items=False, y0=820):
    """floor plan: entry bottom-left, milk at the back, path snakes through aisles."""
    K.panel(c, y0, 560, 90, 900)
    x0, x1, ya, yb = 150, 930, y0 + 130, y0 + 500
    S.rrect(c, x0, ya - 70, x1 - x0, 60, 12); c.set_source_rgb(0.2, 0.45, 0.85); c.fill()
    T(c, "MILK", (x0 + x1) / 2, ya - 26, 40, WHITE, stroke=None)
    for j in range(4):
        ax = 250 + j * 180
        S.rrect(c, ax, ya + 30, 60, 300, 10); c.set_source_rgb(0.35, 0.37, 0.45); c.fill()
    S.rrect(c, x0, yb + 6, 170, 46, 12); c.set_source_rgb(*GRN); c.fill()
    T(c, "ENTRY", x0 + 85, yb + 40, 30, (0.05, 0.08, 0.05), stroke=None)
    pts = [(200, yb), (200, ya + 10), (370, ya + 10), (370, yb - 10), (550, yb - 10), (550, ya + 10),
           (730, ya + 10), (730, yb - 10), (900, yb - 10), (900, ya - 20)]
    fr = max(0.0, min(1.0, (t - prog_t0) / prog_dur))
    segs = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    tot = sum(segs) * fr
    c.move_to(*pts[0])
    cur = pts[0]
    for i, L in enumerate(segs):
        if tot <= 0:
            break
        q = min(1, tot / L)
        cur = (pts[i][0] + (pts[i + 1][0] - pts[i][0]) * q, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * q)
        c.line_to(*cur)
        tot -= L
    c.set_source_rgba(*YEL, 0.95); c.set_line_width(10); c.set_dash([22, 14]); c.stroke(); c.set_dash([])
    c.arc(cur[0], cur[1], 18, 0, 2 * math.pi); c.set_source_rgb(*YEL); c.fill()
    if items:
        for j, (txt, at) in enumerate((("CHIPS", 0.2), ("BISCUITS", 0.45), ("OFFERS!", 0.7))):
            if fr > at:
                a = min(1, (fr - at) * 8)
                x = 310 + j * 180
                S.rrect(c, x - 70, ya + 160 - j * 0, 200, 56, 14); c.set_source_rgba(*RED, a); c.fill()
                T(c, txt, x + 30, ya + 200, 32, WHITE, a, stroke=None)


def o_hook(c, t, lt):
    st = sh.s(1)
    store_map(c, t, st, st + 0.5, 4.5)


def o_logi(c, t, lt):
    st = sh.s(2)
    K.panel(c, 860, 520)
    T(c, "REASON 1: LOGISTICS", 540, 950, 58, YEL, k(t, st, st + 0.3), stroke=None)
    K.rows(c, t, st, [("Trucks unload at the back", WHITE, 50, 0.6), ("Big cold room is right there", WHITE, 50, 2.6),
                      ("Milk stays cold", GRN, 56, 4.8)], y0=1080, gap=110)


def o_basket(c, t, lt):
    st = sh.s(3)
    store_map(c, t, st, st + 0.3, 5.0, items=True)
    T(c, "REASON 2", 540, 790, 54, YEL, k(t, st, st + 0.3))
    K.stamp(c, t, st + 5.8, "BUILDING THE BASKET", 540, 1130, RED, 52, -0.04)


def o_npr(c, t, lt):
    st = sh.s(4)
    U.dim(c, 0.86)
    T(c, "A US STORE CHAIN'S", 540, 560, 54, GREY, k(t, st, st + 0.3), stroke=None)
    T(c, "DAIRY BUYER ON NPR:", 540, 630, 54, GREY, k(t, st, st + 0.3), stroke=None)
    K.panel(c, 700, 380, 90, 900)
    T(c, "\"...we want customers", 540, 800, 60, WHITE, k(t, st + 2.0, st + 2.3), stroke=None)
    T(c, "to get to the back", 540, 880, 60, WHITE, k(t, st + 2.0, st + 2.3), stroke=None)
    T(c, "and see the wide array\"", 540, 990, 60, YEL, k(t, st + 4.2, st + 4.5), stroke=None)


def o_both(c, t, lt):
    st = sh.s(5)
    K.full(c, t, st, [("RIGHT ANSWER?", WHITE, 70, 0.1), ("BOTH", GRN, 140, 1.0), ("EXTRA ITEMS =", WHITE, 62, 3.2),
                      ("THE STORE'S PROFIT", YEL, 66, 3.6)], y0=520, gap=170)


def o_fix(c, t, lt):
    st = sh.s(6)
    K.panel(c, 860, 470)
    T(c, "THE FIX", 540, 950, 60, YEL, stroke=None)
    K.rows(c, t, st, [("1. Make a list", WHITE, 52, 0.4, "left", 170), ("2. Straight to the back", WHITE, 52, 1.4, "left", 170),
                      ("3. Milk. Exit.", GRN, 56, 2.6, "left", 170)], y0=1060, gap=100)


def o_end(c, t, lt):
    K.end_card(c, "ONLY MILK NEXT TIME?", "COMMENT YES or NO", YEL)


def build():
    global sh
    sh = VS.Short(D, CAPS, HOOK, [], SRC)
    assert len(sh.txt) == len(CAPS)
    sh.mood = 'chill'
    s = sh.s
    sh.shots = [
        (0, s(2), st_(mouth='o', eyes=1.3, arms=((60, 120), (14, -10))), (1.9, 1000, 480), (2.1, 1000, 450), o_hook, 'warm'),
        (s(2), s(3), st_(mouth='flat', look=(-0.4, -0.5)), (1.6, 1000, 420), (1.75, 1000, 400), o_logi, 'studio'),
        (s(3), s(4), st_(mouth='frown', angry=0.3), (1.9, 1000, 480), (2.0, 1000, 460), o_basket, 'warm'),
        (s(4), s(5), sw(mouth='o', eyes=1.3), (1.78, 960, 540), (1.85, 960, 520), o_npr, 'money'),
        (s(5), s(6), sw(mouth='smirk'), (1.78, 960, 540), (1.85, 960, 520), o_both, 'money'),
        (s(6), s(7), st_(mouth='smile'), (1.9, 1000, 480), (2.0, 1000, 460), o_fix, 'warm'),
        (s(7), sh.dur + 1, st_(mouth='smile', arms=((14, -10), (100, 40))), (1.9, 1000, 480), (2.1, 1000, 450), o_end, 'warm'),
    ]
    return sh


if __name__ == "__main__":
    sh = build()
    if sys.argv[1] == "preview":
        L = sh.L
        sh.preview([0.5, 1.5, 4.0] + [a + (b - a) * 0.85 for a, b in L[1:]] + [L[2][0] + 3], f"{D}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{D}/short.mp4")
