"""Same Bro BRAVE vs NORMAL — WHO'S RIGHT? engine (campaign100, Prateek 9 Nov 2026).

Sid = 'Brave' vs a 'Normal' friend in a survival situation. One voice take (Rinku), line roles:
  intro  : split screen, both choices on screen in the first 3 s
  brave  : full screen, Brave's choice animates (p 0..1 over the line)
  normal : full screen, Normal's choice animates
  ask    : split freeze 'WHO'S RIGHT? COMMENT B or N' + timer ring
  reveal : split freeze, wrong side red 'WRONG', right side green 'RIGHT' (never injury/gore)
  why    : full screen card, expert-backed reason + SRC tag
  end    : split back at p=0 (loops into the first frame) + comment prompt
A topic supplies scene(c, side, t, p) drawn in a VIRTUAL box (x -400..1480, y 0..1000, key content near x 540),
side 'B' (Brave = Sid) or 'N' (Normal = friend). The engine places the box full screen or in a split panel.
Usage: see studio/shorts/s69_lift/make.py."""
import math
import sys

import cairo
import numpy as np

sys.path.insert(0, "/home/claude/sid/shorts")
import vshort as VS  # noqa: E402
import kit as K  # noqa: E402
from vshort import S, U, T, YEL, RED, GRN, WHITE, FXV  # noqa: E402

VW, VH, FPS = VS.VW, VS.VH, VS.FPS
ORNG = (1.0, 0.55, 0.15)
BLUE = (0.3, 0.62, 1.0)
k = U.k if hasattr(U, 'k') else K.k

FULL = (0, 170, 1080, 1520, 1.42)          # x, y, w, h, scale
TOP = (0, 190, 1080, 720, 0.9)
BOT = (0, 950, 1080, 720, 0.9)


class Dilemma(VS.Short):
    def __init__(self, d, caps, roles, scene, cfg, mood='tense'):
        """roles: dict role -> list of 1-based line numbers. cfg: series, question (2 lines), brave, normal (choice text),
        answer 'B'|'N', why_title, why_rows [(text, col)], src, end (2 lines), grade."""
        super().__init__(d, caps, [], [], cfg.get('src'))
        assert len(self.txt) == len(caps), f"vo.txt has {len(self.txt)} lines, CAPS has {len(caps)}"
        self.roles, self.scene, self.cfg, self.mood = roles, scene, cfg, mood
        self.role_of = {}
        for r, ls in roles.items():
            for n in ls:
                self.role_of[n - 1] = r

    def at(self, t):
        """(role, line index, progress within that role's lines 0..1)."""
        idx = next((j for j, (a, b) in enumerate(self.L) if t < b), len(self.L) - 1)
        if t < self.L[0][0]:
            idx = 0
        role = self.role_of.get(idx, 'intro')
        ls = [n - 1 for n in self.roles[role]]
        a0, b1 = self.L[min(ls)][0], self.L[max(ls)][1]
        if role == 'intro':
            a0 = 0.0
        return role, idx, max(0.0, min(1.0, (t - a0) / max(0.01, b1 - a0))), t - a0

    # ---------- drawing ----------
    def panel(self, c, box, side, t, p, tint=None, freeze=False):
        x, y, w, h, sc = box
        c.save()
        c.rectangle(x, y, w, h); c.clip()
        c.translate(x + w / 2, y + h / 2); c.scale(sc, sc); c.translate(-540, -500 if box[1] < 200 and h > 1000 else -530)
        self.scene(c, side, t, p)
        c.restore()
        if tint:
            c.rectangle(x, y, w, h); c.set_source_rgba(*tint); c.fill()

    def tag(self, c, box, side, a=1.0, big=False):
        x, y, w, h, _ = box
        col = ORNG if side == 'B' else BLUE
        name = "BRAVE" if side == 'B' else "NORMAL"
        if y > 900:
            y = y + h - 112
        S.rrect(c, 30, y + 24, 230 if big else 210, 64, 32); c.set_source_rgba(*col, 0.95 * a); c.fill()
        T(c, name, 30 + (115 if big else 105), y + 68, 38, (0.06, 0.06, 0.08), a, stroke=None)
        txt = self.cfg['brave'] if side == 'B' else self.cfg['normal']
        x0 = 280 if not big else 300
        S.rrect(c, x0, y + 20, 1050 - x0, 72, 22); c.set_source_rgba(0.03, 0.03, 0.06, 0.82 * a); c.fill()
        T(c, txt, (x0 + 1050) / 2, y + 70, 40 if len(txt) < 24 else 34, WHITE, a, stroke=None)

    def seam(self, c, t, l1, l2=None, col1=WHITE, col2=YEL, t0=0.0, size=56):
        a = k(t, t0, t0 + 0.2)
        sc = 1 + 0.2 * (1 - U.eob(a))
        h = 150 if l2 else 96
        c.save(); c.translate(540, 930); c.scale(sc, sc)
        S.rrect(c, -500, -h / 2, 1000, h, 34); c.set_source_rgba(0.02, 0.02, 0.05, 0.94 * a); c.fill_preserve()
        c.set_source_rgba(*YEL, a); c.set_line_width(5); c.stroke()
        if l2:
            T(c, l1, 0, -12, size, col1, a, stroke=None)
            T(c, l2, 0, 52, size - 8, col2, a, stroke=None)
        else:
            T(c, l1, 0, 20, size, col1, a, stroke=None)
        c.restore()

    def caption(self, c, t):
        for n, (a, b) in enumerate(self.L):
            if not (a - 0.05 <= t <= b + 0.15):
                continue
            ws = self.caps[n].split()
            groups, cur = [], []
            for w in ws:
                cur.append(w)
                if len(cur) >= 4 or w[-1] in ".,?!:":
                    groups.append(cur); cur = []
            if cur:
                groups.append(cur)
            tot = sum(len(g) for g in groups)
            tc = a
            for g in groups:
                dd = (b - a) * len(g) / tot
                if tc - 0.05 <= t < tc + dd:
                    txt = " ".join(g)
                    kk = U.eob((t - tc + 0.05) / 0.12)
                    hi = any((w.strip('".,:?!').isupper() and len(w.strip('".,:?!')) > 1) or '₹' in w for w in g)
                    c.save(); c.translate(540, 1762); c.scale(0.85 + 0.15 * kk, 0.85 + 0.15 * kk)
                    T(c, txt, 0, 0, 64 if len(txt) < 20 else 54, YEL if hi else WHITE, lw=12)
                    c.restore()
                    return
                tc += dd
            return

    def frame(self, i):
        t = i / FPS
        role, idx, p, lt = self.at(t)
        cf = self.cfg
        ans = cf['answer']
        wrong = 'B' if ans == 'N' else 'N'
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        c = cairo.Context(sf)
        c.set_source_rgb(0.03, 0.03, 0.05); c.paint()
        frz = self.L[self.roles['ask'][0] - 1][0]  # scene clock stops here
        if role in ('intro', 'end'):
            self.panel(c, TOP, 'B', t, 0.0)
            self.panel(c, BOT, 'N', t, 0.0)
        elif role == 'brave':
            punch = 1 + 0.05 * max(0, 1 - lt / 0.15)
            x, y, w, h, s_ = FULL
            self.panel(c, (x, y, w, h, s_ * punch), 'B', t, p)
        elif role == 'normal':
            punch = 1 + 0.05 * max(0, 1 - lt / 0.15)
            x, y, w, h, s_ = FULL
            self.panel(c, (x, y, w, h, s_ * punch), 'N', t, p)
        elif role in ('ask', 'reveal'):
            rv = role == 'reveal'
            for box, side in ((TOP, 'B'), (BOT, 'N')):
                tint = None
                if rv and side == wrong:
                    tint = (0.55, 0.0, 0.02, 0.35 * k(t, self.L[idx][0], self.L[idx][0] + 0.3))
                self.panel(c, box, side, frz, 1.0, tint)
        elif role == 'why':
            self.panel(c, FULL, ans, frz, 1.0)
            U.dim(c, 0.78)
        sf.flush()
        grade = 'red' if (role == 'brave' and p > 0.6) else cf.get('grade', 'studio')
        rgb = FXV.post(sf, grade, i, 0)
        ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        o = cairo.Context(ov)
        st = self.L[idx][0]
        if role in ('intro', 'end'):
            self.tag(o, TOP, 'B'); self.tag(o, BOT, 'N')
            if role == 'intro':
                self.seam(o, t, cf['question'][0], cf['question'][1], t0=0.0, size=58)
            else:
                self.seam(o, t, cf['end'][0], cf['end'][1], t0=st)
        elif role == 'brave':
            self.tag(o, (0, 170, 1080, 1520, 1), 'B', big=True)
        elif role == 'normal':
            self.tag(o, (0, 170, 1080, 1520, 1), 'N', big=True)
        elif role == 'ask':
            self.tag(o, TOP, 'B'); self.tag(o, BOT, 'N')
            o.rectangle(0, 0, VW, VH); o.set_source_rgba(0, 0, 0, 0.25); o.fill()
            self.seam(o, t, "WHO'S RIGHT?", "COMMENT  B  or  N", t0=st, size=74)
            for box, side in ((TOP, 'B'), (BOT, 'N')):
                col = ORNG if side == 'B' else BLUE
                cx, cy = 900, box[1] + 300
                a = k(t, st + 0.2, st + 0.4)
                o.arc(cx, cy, 90, 0, 2 * math.pi); o.set_source_rgba(*col, a); o.fill()
                T(o, side, cx, cy + 40, 120, (0.05, 0.05, 0.08), a, stroke=None)
            b = self.L[idx][1]
            fr = max(0.0, min(1.0, (t - st) / max(0.1, b - st)))
            o.set_line_width(12); o.set_source_rgba(*YEL, 0.95)
            o.arc(110, 930, 34, -math.pi / 2, -math.pi / 2 + 2 * math.pi * (1 - fr)); o.stroke()
        elif role == 'reveal':
            for box, side in ((TOP, 'B'), (BOT, 'N')):
                self.tag(o, box, side)
                if side == wrong:
                    K.stamp(o, t, st + 0.15, "WRONG", 850, box[1] + 330, RED, 84, -0.08)
                else:
                    a = k(t, st + 0.5, st + 0.8)
                    x, y, w, h, _ = box
                    o.rectangle(x + 6, y + 6, w - 12, h - 12); o.set_source_rgba(*GRN, a); o.set_line_width(12); o.stroke()
                    K.stamp(o, t, st + 0.5, "RIGHT", 850, box[1] + 330, GRN, 84, -0.05)
            nm = "BRAVE" if ans == 'B' else "NORMAL"
            self.seam(o, t, f"{nm} IS RIGHT", None, GRN, t0=st + 0.9, size=70)
        elif role == 'why':
            K.panel(o, 470, 120 + 112 * len(cf['why_rows']) + 60, 50, 980, 0.92)
            T(o, cf.get('why_title', 'WHY?'), 540, 575, 66, YEL, stroke=None)
            n = len(cf['why_rows'])
            ls = [q - 1 for q in self.roles['why']]
            a0, b1 = self.L[min(ls)][0], self.L[max(ls)][1]
            for j, (txt, col) in enumerate(cf['why_rows']):
                dt = a0 + (b1 - a0) * 0.8 * j / max(1, n)
                a = k(t, dt, dt + 0.3)
                if a > 0:
                    T(o, txt, 100, 700 + j * 112, 52 if len(txt) < 28 else 46, col, a, stroke=None, anchor="left")
        if self.sources and role in ('reveal', 'why'):
            S.rrect(o, 140, 1640 if role == 'why' else 116, 800, 46, 23); o.set_source_rgba(0, 0, 0, 0.6); o.fill()
            T(o, self.sources, 540, (1640 if role == 'why' else 116) + 32, 24, (0.85, 0.87, 0.95), stroke=None, bold=False)
        # series pill
        S.rrect(o, 270, 60, 540, 56, 28); o.set_source_rgba(*YEL, 0.95); o.fill()
        T(o, cf['series'], 540, 99, 30, (0.08, 0.08, 0.1), stroke=None)
        self.caption(o, t)
        S.rrect(o, 425, 1838, 230, 56, 28); o.set_source_rgb(0.06, 0.06, 0.08); o.fill_preserve()
        o.set_source_rgb(*YEL); o.set_line_width(4); o.stroke()
        T(o, "SAME BRO", 540, 1877, 30, YEL, stroke=None)
        ov.flush()
        cb = np.ndarray((VH, VW, 4), np.uint8, ov.get_data())
        al = cb[..., 3:4].astype(np.float32) / 255.0
        return np.clip(rgb.astype(np.float32) * (1 - al) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)

    def preview_times(self):
        out = [0.3, 2.0]
        for j, (a, b) in enumerate(self.L[1:], 1):
            out += [a + (b - a) * 0.3, a + (b - a) * 0.9]
        return out
