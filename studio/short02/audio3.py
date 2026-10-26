"""Sound design for Short 02 (live traders): tense pulse bed + whooshes on cuts + coins/stamps/heartbeat. All synthesized."""
import sys
import wave

import numpy as np
from scipy.signal import lfilter

sys.path.insert(0, "/home/claude/sid/v3")
SR = 44100
DUR = 76.0
N = int(SR * DUR)
rng = np.random.default_rng(7)
t = np.arange(N) / SR


def lp(x, k):
    return lfilter([k], [1, -(1 - k)], x)


def env(n, a=0.01, d=0.3):
    tt = np.arange(n) / SR
    return np.minimum(1, tt / max(a, 1e-4)) * np.exp(-tt / d)


def add(buf, sig, at, g=1.0):
    i = int(at * SR)
    j = min(len(buf), i + len(sig))
    if 0 <= i < len(buf):
        buf[i:j] += sig[: j - i] * g


def tone(f, dur, a=0.005, d=0.4):
    n = int(dur * SR)
    tt = np.arange(n) / SR
    return np.sin(2 * np.pi * f * tt) * env(n, a, d)


def noise(dur):
    return rng.standard_normal(int(dur * SR))


# ---- bed: low drone + 8th-note pulse (100 bpm), drops out at key beats ----
bed = np.zeros(N)
for f, g in ((49.0, 0.5), (73.4, 0.3), (98.0, 0.15)):
    bed += np.sin(2 * np.pi * f * t + np.sin(2 * np.pi * 0.05 * t) * 1.5) * g
bed *= 0.07
pulse = np.zeros(N)
step = 60 / 100 / 2
for i in range(int(DUR / step)):
    at = i * step
    if 17.3 < at < 19.1 or 68.3 < at < 71.0:
        continue
    f = 98.0 if (i // 8) % 2 == 0 else 87.3
    if 42.5 < at < 51.3:
        f *= 1.5  # money section lifts
    add(pulse, lp(tone(f, 0.3, 0.003, 0.09) + 0.3 * tone(f * 2, 0.3, 0.003, 0.05), 0.3), at, 0.11)
intensity = np.interp(t, [0, 7, 12.8, 17.3, 19.1, 28, 42.5, 51.3, 57.5, 64.7, 68.3, 71, 76],
                      [0.6, 0.7, 0.9, 1.0, 0.0, 0.7, 1.0, 1.0, 0.7, 0.85, 0.0, 0.5, 0.0])
bed = bed + pulse * intensity
# riser into the brokerage reveal
r0, r1 = 40.5, 42.55
n = int((r1 - r0) * SR)
rz = lp(noise(r1 - r0), 0.05) * np.linspace(0, 1, n) ** 2 * 0.25
add(bed, rz, r0)

# ---- sfx ----
sfx = np.zeros(N)
CUTS = [2.24, 3.6, 6.1, 7.6, 9.06, 10.42, 12.6, 13.9, 16.02, 17.45, 19.0, 20.55, 21.65, 25.55, 28.12, 31.15, 34.05,
        36.12, 38.11, 40.52, 42.52, 44.45, 47.55, 49.45, 51.25, 53.8, 57.46, 60.05, 64.68, 68.42, 71.02]


def whoosh(dur=0.32):
    n = int(dur * SR)
    w = noise(dur)
    sweep = np.linspace(0.02, 0.35, n)
    out = np.zeros(n)
    y = 0.0
    for i in range(0, n, 64):
        k = sweep[i]
        seg = lfilter([k], [1, -(1 - k)], w[i:i + 64], zi=[y])
        out[i:i + 64] = seg[0]
        y = seg[1][0]
    return out * np.sin(np.linspace(0, np.pi, n)) ** 2


for c in CUTS:
    add(sfx, whoosh(), c - 0.16, 0.35)


def impact():
    return lp(tone(55, 0.6, 0.002, 0.25) + 0.4 * noise(0.6) * env(int(0.6 * SR), 0.001, 0.05), 0.15)


for at in (2.24, 6.14, 12.86, 17.5, 22.9, 34.1, 42.6, 46.0, 63.8):
    add(sfx, impact(), at, 0.8)


def coin(f=2400):
    return tone(f, 0.25, 0.001, 0.06) + 0.6 * tone(f * 1.52, 0.25, 0.001, 0.04)


for i in range(28):
    add(sfx, coin(2200 + rng.uniform(-300, 500)), 42.6 + i * 0.24 + rng.uniform(0, 0.08), 0.12)
for i in range(10):
    add(sfx, coin(2600 + rng.uniform(-200, 300)), 45.4 + i * 0.22, 0.14)
# cash register ding at 47.6
add(sfx, tone(1318, 1.0, 0.002, 0.35) + tone(1975, 1.0, 0.002, 0.3), 47.6, 0.2)


def stamp():
    return lp(noise(0.25) * env(int(0.25 * SR), 0.001, 0.04), 0.3) + tone(80, 0.25, 0.001, 0.08)


for at in (14.96, 50.2, 63.8):
    add(sfx, stamp(), at, 0.9)


def heart():
    return lp(tone(48, 0.25, 0.004, 0.07), 0.08) * 3


for i in range(4):
    add(sfx, heart(), 17.45 + i * 0.42, 0.9)
    add(sfx, heart(), 17.45 + i * 0.42 + 0.14, 0.6)
# profit "ting" and loss "buzz"
add(sfx, tone(880, 0.6, 0.002, 0.2) + tone(1320, 0.6, 0.002, 0.15), 9.15, 0.25)
for at in (12.65, 16.05):
    nn = int(0.4 * SR)
    add(sfx, np.sign(np.sin(2 * np.pi * 110 * np.arange(nn) / SR)) * env(nn, 0.005, 0.15) * 0.4, at, 0.25)
# typing ticks under counters
for i in range(40):
    add(sfx, noise(0.012) * 0.5, 34.2 + i * 0.035, 0.15)
    add(sfx, noise(0.012) * 0.5, 26.4 + i * 0.037, 0.12)
# end chord
for f in (220, 277.2, 329.6, 440):
    add(sfx, lp(tone(f, 4.5, 0.4, 2.5), 0.3), 71.05, 0.06)


def save(name, x):
    x = np.clip(x, -1, 1)
    with wave.open(name, "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())


save("bed3.wav", bed / max(1e-6, np.abs(bed).max()) * 0.8)
save("sfx3.wav", sfx / max(1e-6, np.abs(sfx).max()) * 0.9)
print("ok")
