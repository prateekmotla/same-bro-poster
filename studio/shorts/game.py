"""Same Bro GAMES engine (Prateek, 8 Nov 2026): watch-till-end challenge shorts. CupGame = ball under 1 of 3 cups,
fair visible swaps that speed up (EASY > HARD > IMPOSSIBLE), freeze 'COMMENT 1, 2 OR 3' + countdown, reveal with Sid.
Voice: one short take with 3 lines (intro / stop+comment / reveal), split by time ranges and placed on the timeline.
Music: music2 bed (seed = folder name) + code SFX (swoosh per swap, tick on countdown, ding on reveal)."""
import json
import math
import random
import subprocess
import sys

import cairo
import numpy as np
from PIL import Image

sys.path.insert(0, "/home/claude/sid/shorts")
sys.path.insert(0, "/home/claude/sid/v2")
import kit as K  # noqa: E402
import music2 as M2  # noqa: E402
import vshort as VS  # noqa: E402
from kit import T, k, U, S, YEL, RED, GRN, WHITE, GREY  # noqa: E402

VW, VH, FPS = 1080, 1920, 30
SLOTX = [250, 540, 830]
TABLE_Y = 1230


def ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


class CupGame:
    def __init__(self, d, segs, caps, title, series, levels=((4, 0.72), (4, 0.5), (4, 0.34)), seed=7,
                 start_cup=1, cup_col=(0.86, 0.16, 0.2), mood='chill'):
        self.d, self.segs, self.caps, self.title, self.series = d, segs, caps, title, series
        self.cup_col, self.mood = cup_col, mood
        rnd = random.Random(seed)
        # timeline
        self.t_show, self.t_down = 0.3, 2.9
        t = 3.6
        self.swaps = []  # (t0, t1, slot_a, slot_b, level)
        last = None
        for li, (n, dur) in enumerate(levels):
            for _ in range(n):
                pairs = [(0, 1), (1, 2), (0, 2)]
                p = rnd.choice([q for q in pairs if q != last])
                last = p
                self.swaps.append((t, t + dur, p[0], p[1], li))
                t += dur + 0.06
            t += 0.25
        self.t_freeze = t + 0.2
        v2 = segs[1][1] - segs[1][0]
        self.t_count = self.t_freeze + v2 + 0.2
        self.t_reveal = self.t_count + 3.0
        self.dur = self.t_reveal + (segs[2][1] - segs[2][0]) + 1.2
        self.voice_at = [0.0, self.t_freeze, self.t_reveal]
        # cup identity per slot; ball under cup id start_cup (which starts in slot start_cup)
        self.ball_cup = start_cup
        slots = [0, 1, 2]  # slots[cup_id] = slot index
        for (_, _, a, b, _) in self.swaps:
            ia, ib = slots.index(a), slots.index(b)
            slots[ia], slots[ib] = b, a
        self.final_slot = slots[self.ball_cup]
        self.levels = ["EASY", "HARD", "IMPOSSIBLE"]
        json.dump(dict(final_answer=self.final_slot + 1, swaps=len(self.swaps), dur=self.dur), open(f"{d}/game.json", "w"))

    def cup_pos(self, t):
        """returns list of (x, y_offset, scale, depth) per cup id."""
        slots = [0, 1, 2]
        pos = [[SLOTX[s], 0.0, 1.0, 0] for s in slots]
        for (t0, t1, a, b, _) in self.swaps:
            ia, ib = slots.index(a), slots.index(b)
            if t >= t1:
                slots[ia], slots[ib] = b, a
                continue
            if t > t0:
                e = ease((t - t0) / (t1 - t0))
                xa = SLOTX[a] + (SLOTX[b] - SLOTX[a]) * e
                xb = SLOTX[b] + (SLOTX[a] - SLOTX[b]) * e
                arc = math.sin(math.pi * e)
                pos = [[SLOTX[s], 0.0, 1.0, 0] for s in slots]
                pos[ia] = [xa, -70 * arc, 1 - 0.08 * arc, -1]
                pos[ib] = [xb, 25 * arc, 1 + 0.06 * arc, 1]
                return pos
            break
        return [[SLOTX[s], 0.0, 1.0, 0] for s in slots]

    def level_at(self, t):
        for (t0, t1, a, b, li) in self.swaps:
            if t < t1 + 0.3:
                return li
        return 2

    def cup(self, c, x, y, s, lift=0.0):
        c.save(); c.translate(x, y - lift * 260); c.scale(s * 1.12, s * 1.12)
        col = self.cup_col
        c.move_to(-120, 0); c.line_to(-78, -300); c.line_to(78, -300); c.line_to(120, 0); c.close_path()
        g = cairo.LinearGradient(-120, 0, 120, 0)
        g.add_color_stop_rgb(0, col[0] * 0.65, col[1] * 0.65, col[2] * 0.65)
        g.add_color_stop_rgb(0.45, min(1, col[0] * 1.15), min(1, col[1] * 1.3 + 0.05), min(1, col[2] * 1.3 + 0.05))
        g.add_color_stop_rgb(1, col[0] * 0.5, col[1] * 0.5, col[2] * 0.5)
        c.set_source(g); c.fill()
        for yy, w in ((-40, 114), (-250, 84)):
            c.rectangle(-w, yy - 8, 2 * w, 16); c.set_source_rgba(1, 1, 1, 0.18); c.fill()
        c.save(); c.translate(0, -300); c.scale(1, 0.22); c.arc(0, 0, 78, 0, 2 * math.pi); c.restore()
        c.set_source_rgb(col[0] * 0.8, col[1] * 0.8, col[2] * 0.8); c.fill()
        c.restore()

    def ball(self, c, x, y, a=1.0):
        c.arc(x, y - 42, 42, 0, 2 * math.pi)
        g = cairo.RadialGradient(x - 14, y - 58, 4, x, y - 42, 44)
        g.add_color_stop_rgba(0, 1, 1, 0.85, a); g.add_color_stop_rgba(1, 0.95, 0.75, 0.05, a)
        c.set_source(g); c.fill()

    def scene(self, c, t):
        g = cairo.LinearGradient(0, 0, 0, VH)
        g.add_color_stop_rgb(0, 0.07, 0.06, 0.13); g.add_color_stop_rgb(0.55, 0.12, 0.08, 0.2); g.add_color_stop_rgb(1, 0.04, 0.03, 0.06)
        c.set_source(g); c.paint()
        for i in range(3):  # spotlights
            r = cairo.RadialGradient(540, 700, 50, 540, 900, 900)
            r.add_color_stop_rgba(0, 1, 0.85, 0.5, 0.18); r.add_color_stop_rgba(1, 1, 0.85, 0.5, 0)
            c.set_source(r); c.paint()
        # Sid host behind the table
        rev = t > self.t_reveal
        if rev:
            kw = dict(mouth='o' if t < self.t_reveal + 1.2 else 'smirk', eyes=1.3 if t < self.t_reveal + 1.2 else 1.0,
                      arms=((14, -10), (100, 40)))
        elif t > self.t_freeze:
            kw = dict(mouth='smirk', arms=((60, 120), (60, 120)))
        else:
            kw = dict(mouth='smile', arms=((14, -10), (14, -10)), look=(0, 0.4))
        K.sid(c, t, 540, 610, 0.42, **kw)
        # table
        c.rectangle(0, TABLE_Y - 40, VW, 560)
        tg = cairo.LinearGradient(0, TABLE_Y - 40, 0, TABLE_Y + 520)
        tg.add_color_stop_rgb(0, 0.45, 0.26, 0.14); tg.add_color_stop_rgb(1, 0.2, 0.11, 0.06)
        c.set_source(tg); c.fill()
        c.rectangle(0, TABLE_Y - 46, VW, 10); c.set_source_rgba(1, 0.8, 0.6, 0.25); c.fill()

    def frame(self, i):
        t = i / FPS
        sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        c = cairo.Context(sf)
        self.scene(c, t)
        pos = self.cup_pos(t)
        # lift amounts
        lift = [0.0, 0.0, 0.0]
        if t < self.t_down:
            up = ease((t - self.t_show) / 0.35) * (1 - ease((t - (self.t_down - 0.4)) / 0.4))
            lift = [up] * 3
        if t > self.t_reveal:
            u = ease((t - self.t_reveal) / 0.35)
            lift = [u * 0.25, u * 0.25, u * 0.25]
            lift[self.ball_cup] = u
        # ball under ball cup (drawn before cups)
        bx = pos[self.ball_cup][0]
        if max(lift) > 0.02:
            self.ball(c, bx, TABLE_Y)
        order = sorted(range(3), key=lambda j: pos[j][3])
        for j in order:
            x, yo, s, _ = pos[j]
            c.save(); c.translate(x, TABLE_Y + 8); c.scale(1, 0.2); c.arc(0, 0, 125 * s, 0, 2 * math.pi); c.restore()
            c.set_source_rgba(0, 0, 0, 0.35); c.fill()
            self.cup(c, x, TABLE_Y + yo, s, lift[j])
        if t > self.t_reveal + 0.3:
            a = k(t, self.t_reveal + 0.3, self.t_reveal + 0.6)
            K.stamp(c, t, self.t_reveal + 0.3, f"CUP {self.final_slot + 1}!", 540, 1600, GRN, 70, -0.04)
        sf.flush()
        rgb = VS.FXV.post(sf, 'studio', i, 0)
        ov = cairo.ImageSurface(cairo.FORMAT_ARGB32, VW, VH)
        o = cairo.Context(ov)
        self.overlay(o, t)
        ov.flush()
        cb = np.ndarray((VH, VW, 4), np.uint8, ov.get_data())
        al = cb[..., 3:4].astype(np.float32) / 255.0
        return np.clip(rgb.astype(np.float32) * (1 - al) + cb[..., [2, 1, 0]], 0, 255).astype(np.uint8)

    def overlay(self, o, t):
        # series tag + title (from second 0)
        S.rrect(o, 300, 70, 480, 60, 30); o.set_source_rgba(*YEL, 0.95); o.fill()
        T(o, self.series, 540, 112, 32, (0.08, 0.08, 0.1), stroke=None)
        if t < self.t_freeze:
            sc = 1 + 0.15 * (1 - U.eob(min(1, t / 0.25)))
            o.save(); o.translate(540, 250); o.scale(sc, sc)
            T(o, self.title[0], 0, 0, 92, WHITE, lw=12)
            T(o, self.title[1], 0, 105, 76, YEL, lw=12)
            o.restore()
        if self.swaps[0][0] - 0.2 < t < self.t_freeze:
            li = self.level_at(t)
            col = [GRN, YEL, RED][li]
            S.rrect(o, 340, 1700, 400, 80, 40); o.set_source_rgba(0.05, 0.05, 0.08, 0.85); o.fill()
            T(o, "LEVEL: " + self.levels[li], 540, 1753, 40, col, stroke=None)
        if self.t_freeze <= t < self.t_reveal:
            a = k(t, self.t_freeze, self.t_freeze + 0.2)
            T(o, "STOP!", 540, 250, 120, RED, a, lw=14)
            T(o, "WHERE'S THE BALL?", 540, 360, 70, WHITE, a, lw=10)
            for n, x in enumerate(SLOTX):
                o.arc(x, 1400, 52, 0, 2 * math.pi); o.set_source_rgba(*YEL, a); o.fill()
                T(o, str(n + 1), x, 1424, 64, (0.08, 0.08, 0.1), a, stroke=None)
            S.rrect(o, 140, 1500, 800, 110, 55); o.set_source_rgba(0.05, 0.05, 0.08, 0.9 * a); o.fill()
            T(o, "COMMENT 1, 2 OR 3", 540, 1575, 58, YEL, a, stroke=None)
            if t > self.t_count:
                n = 3 - int(t - self.t_count)
                f = (t - self.t_count) % 1
                o.save(); o.translate(880, 640); o.scale(1.4 - 0.4 * U.eob(min(1, f / 0.2)), 1.4 - 0.4 * U.eob(min(1, f / 0.2)))
                o.arc(0, 0, 110, 0, 2 * math.pi); o.set_source_rgba(0.05, 0.05, 0.08, 0.85); o.fill()
                T(o, str(max(1, n)), 0, 50, 150, WHITE, lw=10)
                o.restore()
        if t >= self.t_reveal:
            T(o, "DID YOU GET IT?", 540, 260, 84, WHITE, k(t, self.t_reveal + 1.0, self.t_reveal + 1.3), lw=12)
            if t > self.dur - 2.2:
                K.stamp(o, t, self.dur - 2.2, "WATCH AGAIN >", 540, 400, RED, 56, -0.04)
        # captions (one per voice segment)
        for n_, (a0, a1) in enumerate(self.segs):
            st = self.voice_at[n_]
            ln = a1 - a0
            if st <= t < st + ln + 0.2:
                ws = self.caps[n_].split()
                groups, cur = [], []
                for w in ws:
                    cur.append(w)
                    if len(cur) >= 4 or w[-1] in ".,?!:":
                        groups.append(cur); cur = []
                if cur:
                    groups.append(cur)
                tot = sum(len(g) for g in groups)
                tc = st
                for g in groups:
                    dd = ln * len(g) / tot
                    if tc <= t < tc + dd or g is groups[-1]:
                        y = 1770 if not (self.t_freeze <= t < self.t_reveal) else 1680
                        if self.t_freeze > t > self.swaps[0][0] - 0.2:
                            y = 1640
                        T(o, " ".join(g), 540, y, 60, WHITE, lw=12)
                        break
                    tc += dd
        S.rrect(o, 425, 1840, 230, 56, 28); o.set_source_rgb(0.06, 0.06, 0.08); o.fill_preserve()
        o.set_source_rgb(*YEL); o.set_line_width(4); o.stroke()
        T(o, "SAME BRO", 540, 1879, 30, YEL, stroke=None)

    # ---------- audio ----------
    def audio(self):
        SR = M2.SR
        N = int(SR * self.dur)
        v = M2._read_audio(f"{self.d}/vo.mp3")
        voice = np.zeros(N)
        for (a0, a1), at in zip(self.segs, self.voice_at):
            seg = v[int(a0 * SR):int(a1 * SR)]
            fade = np.minimum(1, np.minimum(np.arange(len(seg)), np.arange(len(seg))[::-1]) / (0.01 * SR))
            i0 = int(at * SR)
            voice[i0:i0 + len(seg)] += (seg * fade)[:N - i0]
        sfx = np.zeros(N)
        rnd = np.random.default_rng(3)

        def put(sig, at, g):
            i0 = int(at * SR)
            sfx[i0:i0 + len(sig)] += g * sig[:N - i0]
        for (t0, t1, *_r) in self.swaps:
            n = int((t1 - t0) * SR)
            noise = M2.lp(M2.hp(rnd.standard_normal(n), 900), 5000)
            env = np.sin(np.pi * np.arange(n) / n) ** 2
            put(noise * env, t0, 0.05)
        tt = np.arange(int(0.05 * SR)) / SR
        tick = np.sin(2 * np.pi * 1500 * tt) * np.exp(-tt * 70)
        for j in range(3):
            put(tick, self.t_count + j, 0.25)
        td = np.arange(int(0.9 * SR)) / SR
        ding = (np.sin(2 * np.pi * 1318.5 * td) + 0.6 * np.sin(2 * np.pi * 1975.5 * td)) * np.exp(-td * 5)
        put(ding, self.t_reveal + 0.15, 0.18)
        import os
        seed = os.path.basename(self.d.rstrip('/'))
        info = M2.mix(voice, self.dur, seed, self.mood, f"{self.d}/mix.wav", sfx=sfx)
        json.dump(info, open(f"{self.d}/music.json", "w"))
        return info

    def preview(self, times, out):
        ims = [Image.fromarray(self.frame(int(tt * FPS))).resize((270, 480)) for tt in times]
        sheet = Image.new("RGB", (270 * min(8, len(ims)), 480 * ((len(ims) + 7) // 8)))
        for k_, im in enumerate(ims):
            sheet.paste(im, ((k_ % 8) * 270, (k_ // 8) * 480))
        sheet.save(out)

    def render(self, out):
        print("audio", self.audio())
        n = int(self.dur * FPS)
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{VW}x{VH}",
                              "-r", str(FPS), "-i", "-", "-i", f"{self.d}/mix.wav",
                              "-filter_complex", "[1:a]aresample=44100,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
                              "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-b:v", "4M",
                              "-maxrate", "5M", "-bufsize", "8M", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                              "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        for i in range(n):
            p.stdin.write(self.frame(i).tobytes())
        p.stdin.close()
        p.wait()
