"""BODY FIX series template (Prateek 25 Nov 2026): health / body-signal shorts, fully animated with Sid on screen.
Structure (7 voice lines): 1 hook (symptom scene) / 2 quiz A-B-C / 3 reveal + why / 4 mechanism or extra fact
/ 5 the fix (steps) / 6 red flags (see a doctor) / 7 share CTA.
A topic is a dict (see topics/*.py). Engine: vshort.Short (Sid world + overlays + captions + music2 bed)."""
import math
import sys

import cairo
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from kit import T, k, U, V, S, B, YEL, RED, GRN, WHITE, GREY  # noqa: E402

EMOJI_FONT = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
_EM = {}


def _emoji_surface(ch):
    ch = ch.replace('\ufe0f', '').replace('\U0001F62E\u200d\U0001F4A8', '\U0001F624')
    if ch not in _EM:
        f = ImageFont.truetype(EMOJI_FONT, 109)
        im = Image.new("RGBA", (180, 180), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((90, 90), ch, font=f, embedded_color=True, anchor="mm")
        im = im.crop(im.getbbox() or (0, 0, 180, 180))
        a = np.array(im).astype(np.float32)
        al = a[..., 3:4] / 255.0
        bgra = np.concatenate([a[..., [2, 1, 0]] * al, a[..., 3:4]], axis=2).astype(np.uint8)
        bgra = np.ascontiguousarray(bgra)
        sf = cairo.ImageSurface.create_for_data(bytearray(bgra.tobytes()), cairo.FORMAT_ARGB32, im.width, im.height,
                                                cairo.ImageSurface.format_stride_for_width(cairo.FORMAT_ARGB32, im.width))
        _EM[ch] = sf
    return _EM[ch]


def emoji(c, ch, x, y, size, a=1.0, rot=0.0):
    if a <= 0.01:
        return
    sf = _emoji_surface(ch)
    sc = size / max(sf.get_width(), sf.get_height())
    c.save()
    c.translate(x, y); c.rotate(rot); c.scale(sc, sc)
    c.set_source_surface(sf, -sf.get_width() / 2, -sf.get_height() / 2)
    c.paint_with_alpha(min(1, a))
    c.restore()


# ---------- Sid poses ----------
POSES = {
    'stand': dict(),
    'belly': dict(arms=((-50, 120), (-50, 120))),           # both hands on stomach
    'think': dict(arms=((14, -10), (-40, 160))),          # hand to chin
    'point': dict(arms=((14, -10), (100, 40))),           # explaining / pointing up-right
    'wave': dict(arms=((14, -10), (140, 30))),
    'shrug': dict(arms=((60, 60), (60, 60))),
    'yes': dict(arms=((14, -10), (120, -20))),            # fist up
    'phone': dict(phone=1, arms=((14, -10), (40, 110))),
    'head': dict(arms=((14, -10), (-60, 170))),           # hand on head (headache / facepalm)
}


def sid_kw(pose='stand', **e):
    d = dict(POSES.get(pose, {}))
    d.update(e)
    return d


ENVS = {
    'night': lambda c, t: V.room(c, t, 'night'),
    'morning': lambda c, t: V.room(c, t, 'morning'),
    'canteen': V.canteen,
    'street': lambda c, t: V.street(c, t, off=t * 40, night=False),
    'streetnight': lambda c, t: V.street(c, t, off=t * 40, night=True),
    'studio': V.studio,
    'metro': V.metro,
}

SID_X, SID_Y, SID_S = 960, 640, 0.40   # Sid lower in the world so overlays sit above his head


def world(env, sid=None, fx=None, walk=False, x=SID_X):
    def f(c, t, lt):
        ENVS[env](c, t)
        if sid is not None:
            kw = dict(sid)
            if walk:
                kw.update(pose='walk', ph=t * 0.9)
            else:
                kw.setdefault('pose', 'stand')
            B.figure(c, x, SID_Y, SID_S, t, **kw)
        if fx:
            fx(c, t, lt)
    return f


# ---------- symptom FX (drawn in world coords around Sid) ----------
def fx_bubble(ch, t0=0.4):
    """thought bubble with an emoji above-left of Sid"""
    def f(c, t, lt):
        a = U.eob(k(t, t0, t0 + 0.4))
        bx, by = SID_X - 230, SID_Y - 190
        for i, (dx, dy, r) in enumerate(((150, 120, 12), (110, 80, 18))):
            c.arc(bx + dx, by + dy, r * a, 0, 6.283); c.set_source_rgba(1, 1, 1, 0.92 * a); c.fill()
        c.save(); c.translate(bx, by); c.scale(a, a)
        c.arc(0, 0, 95, 0, 6.283); c.set_source_rgba(1, 1, 1, 0.95); c.fill()
        c.restore()
        emoji(c, ch, bx, by + 4 * math.sin(t * 3), 120 * a, a)
    return f


def fx_marks(sym='!', col=RED, t0=0.6):
    def f(c, t, lt):
        for i, (dx, dy, r) in enumerate(((150, -110, 0.25), (190, -40, 0.1), (-170, -90, -0.2))):
            a = k(t, t0 + i * 0.25, t0 + i * 0.25 + 0.2)
            c.save(); c.translate(SID_X + dx, SID_Y + dy + 6 * math.sin(t * 5 + i)); c.rotate(r)
            T(c, sym, 0, 0, 70, col, a, lw=8)
            c.restore()
    return f


def fx_belly(t0=0.3):
    """pulsing 'bloat' rings on Sid's stomach"""
    def f(c, t, lt):
        if t < t0:
            return
        for i in range(3):
            p = ((t - t0) * 0.9 + i / 3) % 1
            c.arc(SID_X, SID_Y + 330, 60 + 120 * p, 0, 6.283)
            c.set_source_rgba(1, 0.35, 0.3, 0.5 * (1 - p)); c.set_line_width(8); c.stroke()
    return f


def fx_float(chars, t0=0.3):
    """emoji floating around Sid"""
    def f(c, t, lt):
        pos = ((-280, -40), (280, 20), (-240, 260), (260, 300))
        for i, ch in enumerate(list(chars) if isinstance(chars, (list, tuple)) else [chars]):
            a = U.eob(k(t, t0 + i * 0.2, t0 + i * 0.2 + 0.35))
            dx, dy = pos[i % 4]
            emoji(c, ch, SID_X + dx, SID_Y + dy + 8 * math.sin(t * 2.4 + i), 110 * a, a, 0.15 * math.sin(t + i))
    return f


def fx_zzz(t0=0.2):
    def f(c, t, lt):
        for i in range(3):
            p = ((t - t0) * 0.5 + i / 3) % 1
            T(c, "Z", SID_X + 120 + 80 * p, SID_Y - 120 - 160 * p, 40 + 30 * p, WHITE, (1 - p) * k(t, t0, t0 + 0.2), lw=6)
    return f


def combine(*fs):
    def f(c, t, lt):
        for g in fs:
            if g:
                g(c, t, lt)
    return f


FX = {'bubble': fx_bubble, 'marks': fx_marks, 'belly': fx_belly, 'float': fx_float, 'zzz': fx_zzz}


def make_fx(spec):
    """spec: list like [('bubble','🥟'), ('belly',), ('marks','?', YEL)]"""
    if not spec:
        return None
    return combine(*[FX[s[0]](*s[1:]) for s in spec])


# ---------- overlays (screen coords 1080x1920; Sid's head sits ~y 1150) ----------
def card_bg(c, x, y, w, h, a, col=(0.1, 0.11, 0.18), r=34):
    S.rrect(c, x, y, w, h, r); c.set_source_rgba(*col, 0.94 * a); c.fill()


class BodyFix:
    def __init__(self, topic, d):
        self.tp, self.d = topic, d

    # -- line 1: hook. Title box from vshort for 2.6 s, then a stamp
    def o_hook(self, c, t, lt):
        tp = self.tp
        if tp.get('hook_stamp') and t > 2.7:
            K.stamp(c, t, 2.7, tp['hook_stamp'], 540, 520, YEL, 66, -0.05)

    # -- line 2: quiz
    def o_quiz(self, c, t, lt):
        tp, st = self.tp, self.sh.s(2)
        en = self.sh.L[1][1]
        U.dim(c, 0.55)
        card_bg(c, 70, 170, 940, 190, k(t, st, st + 0.2), (0.05, 0.05, 0.08))
        T(c, tp['q1'], 540, 245, 54, WHITE, k(t, st, st + 0.2), lw=8)
        T(c, tp['q2'], 540, 320, 58, YEL, k(t, st + 0.15, st + 0.35), lw=8)
        for i, txt in enumerate(tp['opts']):
            a = k(t, st + 0.3 + i * 0.25, st + 0.6 + i * 0.25)
            y = 380 + i * 160
            xo = (1 - S.ease(a)) * 300
            card_bg(c, 80 + xo, y, 920, 140, a)
            c.arc(165 + xo, y + 70, 48, 0, 6.283); c.set_source_rgba(*YEL, a); c.fill()
            T(c, "ABC"[i], 165 + xo, y + 92, 62, (0.08, 0.08, 0.1), a, stroke=None)
            T(c, txt, 580 + xo, y + 87, 46 if len(txt) < 22 else 40 if len(txt) < 26 else 35, WHITE, a, stroke=None)
        # countdown
        p = max(0, min(1, (t - st) / max(0.6, en - st)))
        S.rrect(c, 200, 862, 680, 20, 10); c.set_source_rgba(1, 1, 1, 0.2); c.fill()
        S.rrect(c, 200, 862, max(20, 680 * (1 - p)), 20, 10); c.set_source_rgb(*YEL); c.fill()
        K.stamp(c, t, st + 1.2, "GUESS FIRST", 540, 930, YEL, 46, -0.03)

    # -- line 3: reveal
    def o_reveal(self, c, t, lt):
        tp, st = self.tp, self.sh.s(3)
        U.dim(c, 0.5)
        ans = tp['answer']
        for i, txt in enumerate(tp['opts']):
            ok = i == ans
            y = 190 + i * 130
            a = 1.0 if ok else 1 - 0.6 * k(t, st, st + 0.4)
            card_bg(c, 80, y, 920, 115, a, (0.07, 0.36, 0.2) if ok else (0.32, 0.1, 0.13))
            c.arc(160, y + 57, 40, 0, 6.283); c.set_source_rgba(*(GRN if ok else RED), a); c.fill()
            T(c, "ABC"[i], 160, y + 77, 52, (0.08, 0.08, 0.1), a, stroke=None)
            T(c, txt, 580, y + 72, 42 if len(txt) < 22 else 37 if len(txt) < 26 else 33, WHITE, a, stroke=None)
        y_ok = 190 + ans * 130
        K.stamp(c, t, st + 0.3, "RIGHT", 900, y_ok + 10, GRN, 48, 0.08)
        card_bg(c, 70, 600, 940, 90 + 85 * len(tp['why']), k(t, st + 0.6, st + 0.9), (0.04, 0.04, 0.07))
        for j, (txt, col, size) in enumerate(tp['why']):
            T(c, txt, 540, 670 + j * 85, size, col, k(t, st + 0.8 + j * 0.5, st + 1.1 + j * 0.5), lw=8)

    # -- line 4: mechanism / extra fact (big text, emoji)
    def o_fact(self, c, t, lt):
        tp, st = self.tp, self.sh.s(4)
        card_bg(c, 60, 150, 960, 120 + 105 * len(tp['fact']), k(t, st, st + 0.25), (0.04, 0.04, 0.07))
        for j, (txt, col, size) in enumerate(tp['fact']):
            a = k(t, st + 0.2 + j * 0.6, st + 0.5 + j * 0.6)
            c.save(); c.translate(540, 250 + j * 105); s_ = 1 + 0.25 * (1 - U.eob(a)) if a < 1 else 1
            c.scale(s_, s_); T(c, txt, 0, 0, size, col, a, lw=8); c.restore()

    # -- line 5: the fix
    def o_fix(self, c, t, lt):
        tp, st = self.tp, self.sh.s(5)
        en = self.sh.L[4][1]
        U.dim(c, 0.45)
        T(c, "THE FIX", 540, 250, 84, GRN, k(t, st, st + 0.2), lw=10)
        n = len(tp['fix'])
        for i, (ch, txt) in enumerate(tp['fix']):
            t0 = st + 0.3 + i * min(1.6, (en - st - 0.6) / n)
            a = k(t, t0, t0 + 0.3)
            y = 310 + i * 140
            card_bg(c, 70, y, 940, 125, a)
            emoji(c, ch, 160, y + 62, 80 * U.eob(a), a)
            lines = txt.split('|')
            for m, ln in enumerate(lines):
                T(c, ln, 600, y + 62 + 16 + (m - (len(lines) - 1) / 2) * 46, 44 if len(ln) < 24 else 38 if len(ln) < 28 else 34, WHITE, a,
                  stroke=None)

    # -- line 6: red flags
    def o_flag(self, c, t, lt):
        tp, st = self.tp, self.sh.s(6)
        a = k(t, st, st + 0.25)
        U.dim(c, 0.5)
        S.rrect(c, 60, 160, 960, 200 + 105 * len(tp['flags']), 40)
        c.set_source_rgba(0.28, 0.06, 0.1, 0.95 * a); c.fill_preserve()
        c.set_source_rgba(*RED, a); c.set_line_width(6); c.stroke()
        emoji(c, "🚩", 200, 255, 100 * U.eob(a), a)
        T(c, "SEE A DOCTOR IF", 600, 282, 64, RED, a, lw=8)
        for j, txt in enumerate(tp['flags']):
            T(c, "• " + txt, 540, 400 + j * 105, 50 if len(txt) < 22 else 42 if len(txt) < 28 else 35, WHITE,
              k(t, st + 0.4 + j * 0.45, st + 0.7 + j * 0.45), stroke=None)

    # -- line 7: share CTA
    def o_cta(self, c, t, lt):
        tp, st = self.tp, self.sh.s(7)
        a = k(t, st, st + 0.25)
        card_bg(c, 60, 170, 960, 380, a, (0.04, 0.04, 0.07))
        emoji(c, "📲", 540, 255, 110 * U.eob(a), a)
        T(c, "SEND THIS TO", 540, 375, 50, GREY, a, stroke=None)
        for j, ln in enumerate(tp['cta']):
            T(c, ln, 540, 450 + j * 75, 58, YEL if j == len(tp['cta']) - 1 else WHITE, k(t, st + 0.2, st + 0.5), lw=8)
        K.stamp(c, t, st + 1.2, "FOLLOW FOR BODY FIX #" + str(tp['no'] + 1), 540, 640, GRN, 42, -0.03)

    def build(self):
        tp, d = self.tp, self.d
        sh = VS.Short(d, tp['caps'], tp['hook'], [], tp['src'])
        assert len(sh.txt) == 7 == len(tp['caps']), (len(sh.txt), len(tp['caps']))
        sh.mood = tp.get('mood', 'chill')
        self.sh = sh
        s = sh.s
        sc = tp['scenes']   # 7 dicts: env, sid(kw), fx(list), walk
        overs = [self.o_hook, self.o_quiz, self.o_reveal, self.o_fact, self.o_fix, self.o_flag, self.o_cta]
        grades = ['warm', 'studio', 'money', 'studio', 'money', 'red', 'warm']
        # camera: Sid's head lands ~y 1150 on screen; z 1.55-1.75 gentle push-ins, alternating sides for energy
        cams = [((1.55, 960, 560), (1.72, 960, 600)), ((1.62, 930, 580), (1.68, 960, 580)),
                ((1.68, 990, 580), (1.62, 960, 580)), ((1.55, 960, 570), (1.66, 940, 590)),
                ((1.62, 960, 580), (1.56, 990, 580)), ((1.66, 960, 580), (1.74, 960, 600)),
                ((1.55, 960, 570), (1.66, 960, 600))]
        shots = []
        for i in range(7):
            a = 0 if i == 0 else s(i + 1)
            b = s(i + 2) if i < 6 else sh.dur + 1
            sd = sc[i]
            w = world(sd.get('env', 'studio'), sid_kw(**sd.get('sid', {})), make_fx(sd.get('fx')), sd.get('walk', False))
            shots.append((a, b, w, cams[i][0], cams[i][1], overs[i], sd.get('grade', grades[i])))
        sh.shots = shots
        return sh


def run(topic, d, mode):
    bf = BodyFix(topic, d)
    sh = bf.build()
    if mode == "preview":
        L = sh.L
        sh.preview([0.4, 2.0, 3.5] + [a + (b - a) * 0.9 for a, b in L[1:]], f"{d}/prev.png")
        print("dur", round(sh.dur, 1), [round(a, 1) for a, b in L])
    else:
        sh.render(f"{d}/short.mp4")
