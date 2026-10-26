"""Make a 9:16 short from a segment of the long video: clean re-render (no landscape captions), big word captions, hook title."""
import json
import subprocess
import sys

import cairo
import numpy as np
from PIL import Image

sys.path.insert(0, "/home/claude/sid/long1")
import render_long as R  # noqa: E402
import ui as U  # noqa: E402
from ui import T, YEL, RED, GRN, WHITE  # noqa: E402
import sid2 as S  # noqa: E402

R.caption = lambda c, t: None
VW, VH, FPS = 1080, 1920, 24
WORDS = json.load(open("/home/claude/sid/long1/wclean.json"))
CAPMAP = {}


def chunks(a, b):
    """English captions: each line's English text split into ~4-word chunks spread over the line's duration."""
    out = []
    for n in range(1, len(R.L)):
        s0, s1 = R.L[n]
        if s0 < a - 0.05 or s0 >= b:
            continue
        ws = R.CAPS_EN[n - 1].split()
        groups, cur = [], []
        for w in ws:
            cur.append(w)
            if len(cur) >= 4 or w[-1] in ".,?!:":
                groups.append(cur); cur = []
        if cur:
            groups.append(cur)
        tot = sum(len(g) for g in groups)
        tcur = s0
        for g in groups:
            d = (s1 - s0) * len(g) / tot
            out.append((" ".join(g), tcur, tcur + d - 0.05))
            tcur += d
    return out


def draw_vertical(land, t, a, b, hook, chs, end_txt):
    sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
    c = cairo.Context(sf)
    g = cairo.LinearGradient(0, 0, 0, VH)
    g.add_color_stop_rgb(0, 0.07, 0.08, 0.15)
    g.add_color_stop_rgb(1, 0.02, 0.02, 0.05)
    c.set_source(g)
    c.paint()
    # hook title
    yy = 210
    for i, (txt, col) in enumerate(hook):
        T(c, txt, 540, yy + i * 105, 92 if len(txt) < 14 else 74, col, lw=12)
    # landscape band
    img = Image.fromarray(land).crop((260, 0, 1660, 1080)).resize((1080, 833), Image.BILINEAR).convert("RGBA")
    band = np.array(img)
    out = np.array(Image.frombuffer("RGBA", (VW, VH), bytes(sf.get_data()), "raw", "BGRa", 0, 1).convert("RGB"))
    y0 = 560
    out[y0:y0 + 833] = band[..., :3]
    ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
    o = cairo.Context(ov)
    S.rrect(o, 0, y0 - 6, VW, 6, 0); o.set_source_rgb(*YEL); o.fill()
    S.rrect(o, 0, y0 + 833, VW, 6, 0); o.set_source_rgb(*YEL); o.fill()
    # word captions (Hinglish spoken words, as heard) — big, 3 words
    for txt, s0, s1 in chs:
        if s0 - 0.05 <= t <= s1 + 0.15:
            kk = U.eob((t - s0 + 0.05) / 0.12)
            o.save(); o.translate(540, 1590); o.scale(0.85 + 0.15 * kk, 0.85 + 0.15 * kk)
            words_ = txt.split()
            col = YEL if any((w.strip('".,:?!').isupper() and len(w.strip('".,:?!')) > 1) or '₹' in w or '%' in w for w in words_) else WHITE
            T(o, txt, 0, 0, 72 if len(txt) < 20 else 58, col, lw=14)
            o.restore()
            break
    if t > b - 0.1:
        T(o, end_txt, 540, 1590, 56, YEL, U.k(t, b - 0.1, b + 0.2), lw=10)
    S.rrect(o, 425, 1760, 230, 62, 31); o.set_source_rgb(0.06, 0.06, 0.08); o.fill_preserve()
    o.set_source_rgb(*YEL); o.set_line_width(4); o.stroke()
    T(o, "SAME BRO", 540, 1802, 32, YEL, stroke=None)
    ov.flush()
    cb = np.ndarray((VH, VW, 4), np.uint8, ov.get_data())
    al = cb[..., 3:4].astype(np.float32) / 255.0
    return np.clip(out.astype(np.float32) * (1 - al) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)


def make(a, b, hook, out, end_txt="Full video on the channel"):
    tail = 1.6
    chs = chunks(a, b)
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{VW}x{VH}",
                          "-r", str(FPS), "-i", "-", "-ss", str(a), "-t", str(b - a + tail),
                          "-i", "/home/claude/sid/long1/same_bro_long_01.mp4",
                          "-map", "0:v", "-map", "1:a", "-af", f"afade=t=in:d=0.15,afade=t=out:st={b - a + tail - 0.6}:d=0.6",
                          "-c:v", "libx264", "-preset", "medium", "-b:v", "3M", "-maxrate", "4M", "-bufsize", "8M",
                          "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out],
                         stdin=subprocess.PIPE)
    i0, i1 = int(a * FPS), int((b + tail) * FPS)
    for i in range(i0, i1):
        t = i / FPS
        land = R.render_frame(min(i, int((b - 0.3) * FPS)))
        p.stdin.write(draw_vertical(land, t, a, b, hook, chs, end_txt).tobytes())
    p.stdin.close()
    p.wait()


CUTS = {
    "story": (22.59, 53.56, [("F&O:", WHITE), ("₹15,000 TO ₹0", RED), ("IN 3 WEEKS", YEL)]),
    "data": (53.73, 79.0, [("91% OF F&O", RED), ("TRADERS", WHITE), ("LOSE MONEY", YEL)]),
    "incomes": (79.04, 120.68, [("HOW LIVE TRADERS", WHITE), ("EARN WITHOUT", YEL), ("WINNING", GRN)]),
    "screens": (137.36, 161.12, [("LIVE TRADERS'", WHITE), ("SCREENSHOT", YEL), ("TRICK", RED)]),
    "sebi": (161.2, 185.2, [("SEBI SEIZED", WHITE), ("₹546 CRORE", RED), ("FROM FINFLUENCERS", YEL)]),
    "questions": (185.24, 207.68, [("ASK THIS BEFORE", WHITE), ("FOLLOWING ANY", WHITE), ("LIVE TRADER", YEL)]),
}

if __name__ == "__main__" and False:
    name = sys.argv[1]
    a, b, hook = CUTS[name]
    if len(sys.argv) > 2 and sys.argv[2] == "preview":
        chs = chunks(a, b)
        for n, tt in enumerate((a + 1, (a + b) / 2, b + 0.5)):
            land = R.render_frame(int(min(tt, b) * FPS))
            Image.fromarray(draw_vertical(land, tt, a, b, hook, chs, "Full video on the channel")).save(f"v_{n}.png")
    else:
        make(a, b, hook, f"short_{name}.mp4")
