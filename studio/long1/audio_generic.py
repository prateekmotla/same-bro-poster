"""Generic bed + whooshes for a long video. Usage: python3 audio_generic.py <dir> <duration> <cut1,cut2,...>"""
import sys
import wave

import numpy as np
from scipy.signal import lfilter

d, DUR = sys.argv[1], float(sys.argv[2])
cuts = [float(x) for x in sys.argv[3].split(",") if x]
SR = 44100
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(9)


def lp(x, k):
    return lfilter([k], [1, -(1 - k)], x)


def env(n, a, dd):
    tt = np.arange(n) / SR
    return np.minimum(1, tt / a) * np.exp(-tt / dd)


def add(buf, sig, at, g):
    i = int(at * SR); j = min(len(buf), i + len(sig))
    if 0 <= i < len(buf):
        buf[i:j] += sig[:j - i] * g


bed = sum(np.sin(2 * np.pi * f * t + np.sin(2 * np.pi * 0.05 * t) * 1.5) * g for f, g in ((49, .5), (73.4, .3), (98, .15))) * 0.06
step = 60 / 92 / 2
for i in range(int(DUR / step)):
    f = [98.0, 87.3, 110.0, 82.4][(i // 16) % 4]
    n = int(.3 * SR)
    s = np.sin(2 * np.pi * f * np.arange(n) / SR) * env(n, .003, .09)
    add(bed, lp(s, .3), i * step, .09)
bed *= np.clip(t / 2, 0, 1) * np.clip((DUR - t) / 3, 0, 1)
sfx = np.zeros(N)
for c in cuts:
    n = int(.32 * SR)
    w = lp(rng.standard_normal(n), .15) * np.sin(np.linspace(0, np.pi, n)) ** 2
    add(sfx, w, c - .16, .3)


def save(name, x):
    x = np.clip(x, -1, 1)
    with wave.open(name, 'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype(np.int16).tobytes())


save(f"{d}/bed.wav", bed / np.abs(bed).max() * .8)
save(f"{d}/sfx.wav", sfx / max(1e-6, np.abs(sfx).max()) * .9)
print("ok")
