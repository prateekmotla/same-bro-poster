"""Same Bro music bed v2 (Prateek, 2 Nov 2026): code-generated dark half-time trap / lo-fi. No samples, no copyrighted material.

808 kick with sub tail, clap on the half-time backbeat, rolling hi-hats with 32nd rolls, a short minor pluck motif,
soft dark pad, everything (except kick/808) sidechained to the kick. Every video gets its own key, tempo (120-150 bpm)
and motif from a seed (use the video folder name), mood picks the flavour:
  'tense'  trading / losses / scams  -> faster, harmonic minor, busier hats, darker pad
  'chill'  night / life / everyday   -> slower, natural minor, lo-fi (softer clap, vinyl crackle, warmer filter)
  'warm'   Diwali / festive          -> mid tempo, dorian colour, brighter pluck, shimmer

API:
  music2.bed(dur, seed, mood='chill', sr=44100) -> (np.float32 mono array, info dict)
  music2.mix(vo_wav_or_array, dur, seed, mood, out_wav, below_db=14, duck_db=7)  # voice + bed, bed ~14 dB under voice
CLI:  python3 music2.py <out.wav> <dur> <seed> [mood]      (bed only, for previews / long videos)
"""
import hashlib
import subprocess
import sys
import wave

import numpy as np
from scipy.signal import butter, lfilter, sosfilt

SR = 44100
NOTE = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
KEYS = list(NOTE)
SCALES = {'nat': [0, 2, 3, 5, 7, 8, 10], 'harm': [0, 2, 3, 5, 7, 8, 11], 'dor': [0, 2, 3, 5, 7, 9, 10]}
MOODS = {
    'tense': dict(bpm=(138, 150), scale='harm', hat_density=0.9, roll_p=0.45, pad_cut=900, pluck_cut=2600, crackle=0.0, clap=1.0),
    'chill': dict(bpm=(120, 130), scale='nat', hat_density=0.55, roll_p=0.2, pad_cut=1400, pluck_cut=2000, crackle=0.012, clap=0.7),
    'warm': dict(bpm=(126, 138), scale='dor', hat_density=0.7, roll_p=0.3, pad_cut=1800, pluck_cut=3400, crackle=0.006, clap=0.85),
}


def _rng(seed):
    return np.random.default_rng(int(hashlib.md5(str(seed).encode()).hexdigest()[:8], 16))


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def lp(x, fc, order=2):
    return sosfilt(butter(order, min(fc, SR * 0.45) / (SR / 2), output='sos'), x)


def hp(x, fc, order=2):
    return sosfilt(butter(order, fc / (SR / 2), btype='high', output='sos'), x)


def add(buf, sig, at, g=1.0):
    i = int(at * SR)
    if i >= len(buf) or i + len(sig) <= 0:
        return
    s = sig[max(0, -i):]
    i = max(0, i)
    j = min(len(buf), i + len(s))
    buf[i:j] += s[:j - i] * g


def kick808(f0, tail=0.9):
    n = int(SR * tail)
    t = np.arange(n) / SR
    f = f0 + (f0 * 3.5) * np.exp(-t / 0.035)            # pitch drop into the sub
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t / (tail * 0.42))
    click = np.exp(-t / 0.004) * 0.5
    return np.tanh(1.8 * (body + click)) * 0.9


def clap(rng, soft=1.0):
    n = int(SR * 0.35)
    t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    env = np.zeros(n)
    for k, d in enumerate((0.0, 0.011, 0.022)):           # 3 quick bursts = clap
        m = t >= d
        env[m] += np.exp(-(t[m] - d) / (0.012 if k < 2 else 0.12))
    x = lfilter(*butter(2, [900 / (SR / 2), 2600 / (SR / 2)], btype='band'), noise) * env
    return x * 1.6 * soft


def hat(rng, open_=False):
    n = int(SR * (0.18 if open_ else 0.045))
    t = np.arange(n) / SR
    x = hp(rng.standard_normal(n), 7000, 2) * np.exp(-t / (0.06 if open_ else 0.012))
    return x * 0.5


def pluck(f, dur, cut):
    n = int(SR * dur)
    t = np.arange(n) / SR
    saw = 2 * ((f * t) % 1) - 1
    sq = np.sign(np.sin(2 * np.pi * f * 1.0 * t)) * 0.3
    x = (saw + sq) * np.exp(-t / 0.16)
    x = lp(x, cut * 1.0) * np.minimum(1, t / 0.002)
    return x * 0.5


def pad_chord(freqs, dur, cut, rng):
    n = int(SR * dur)
    t = np.arange(n) / SR
    x = np.zeros(n)
    for f in freqs:
        for det in (-0.12, 0.0, 0.11):
            ff = f * 2 ** (det / 12)
            x += 2 * ((ff * t + rng.random()) % 1) - 1
    x = lp(x / (len(freqs) * 3), cut, 4)
    a = np.minimum(1, t / 0.6) * np.minimum(1, (dur - t) / 0.6)
    return x * np.clip(a, 0, 1)


def bed(dur, seed, mood='chill', sr=SR):
    M = MOODS.get(mood, MOODS['chill'])
    rng = _rng(seed)
    bpm = int(rng.integers(M['bpm'][0], M['bpm'][1] + 1))
    key = KEYS[int(rng.integers(0, 12))]
    sc = SCALES[M['scale']]
    root = 33 + NOTE[key]                                   # A1-ish region for the 808
    if root > 40:
        root -= 12
    beat = 60 / bpm
    bar = beat * 4                                          # half-time feel: clap on beat 3
    N = int(SR * (dur + 1))
    drums, sub, mel = np.zeros(N), np.zeros(N), np.zeros(N)
    kick_times = []
    # progression (scale degrees) and motif (scale steps, 8 x 16th grid over 2 beats) from seed
    progs = [[0, 5, 3, 4], [0, 3, 5, 4], [0, 6, 5, 3], [0, 5, 6, 4], [0, 2, 5, 4]]
    prog = progs[int(rng.integers(0, len(progs)))]
    motif_len = 8
    motif = [int(rng.choice([0, 2, 4, 3, 6, 7, -1, -1])) for _ in range(motif_len)]
    motif[0] = 0
    kick_pats = [[0, 2.5], [0, 1.75, 2.5], [0, 0.75, 2.5, 3.25], [0, 2.75], [0, 1.5, 2.5]]
    kp = kick_pats[int(rng.integers(0, len(kick_pats)))]
    nbars = int(dur / bar) + 2
    for b in range(nbars):
        t0 = b * bar
        deg = prog[(b // 2) % len(prog)]
        dm = lambda d_: root + sc[d_ % 7] + 12 * (d_ // 7)
        r = dm(deg)
        intro = b == 0
        # kick + 808 (808 = kick tuned to chord root, longer tail)
        for kb in (kp if not intro else [0]):
            kt = t0 + kb * beat
            kick_times.append(kt)
            add(sub, kick808(hz(r), tail=0.55 if kb else 1.1), kt, 0.9)
        # clap on beat 3 (half-time backbeat); last bar of 4 gets a ghost
        if not intro:
            add(drums, clap(rng, M['clap']), t0 + 2 * beat, 0.55)
            if b % 4 == 3:
                add(drums, clap(rng, M['clap']) * 0.4, t0 + 3.75 * beat, 0.5)
        # hats: 8ths, sometimes 16ths, 32nd rolls / triplet rolls at bar ends
        steps = 16
        for s in range(steps):
            st = t0 + s * beat / 4
            if s % 2 == 1 and rng.random() > M['hat_density']:
                continue
            add(drums, hat(rng), st, 0.35 if s % 4 == 0 else 0.22)
        if rng.random() < M['roll_p'] and not intro:
            rs = t0 + 3 * beat + (0 if rng.random() < 0.5 else beat / 2)
            n32 = int(rng.choice([4, 6, 8]))
            for q in range(n32):
                add(drums, hat(rng), rs + q * beat / 8, 0.12 + 0.18 * q / n32)
        if b % 2 == 1:
            add(drums, hat(rng, True), t0 + 3.5 * beat, 0.18)
        # pad: minor-ish triad of the chord, 1 bar
        tri = [hz(dm(deg + o) + 24) for o in (0, 2, 4)]
        add(mel, pad_chord(tri, bar + 0.4, M['pad_cut'], rng), t0, 0.32)
        # pluck motif: plays on bars 2 and 4 of each 4-bar phrase (short, leaves room for the voice)
        if b % 4 in (1, 3) and not intro:
            for s, stp in enumerate(motif):
                if stp < 0:
                    continue
                f = hz(dm(deg + stp) + 36)
                add(mel, pluck(f, 0.4, M['pluck_cut'] * 0.6), t0 + s * beat / 4, 0.11)  # softer, duller (no arcade feel)
    # sidechain: duck pad/pluck/drums(not kick) on every kick
    sc_env = np.ones(N)
    rel = int(SR * beat * 0.45)
    curve = 1 - 0.65 * np.exp(-np.arange(rel) / (rel / 3))
    for kt in kick_times:
        i = int(kt * SR)
        j = min(N, i + rel)
        if i < N:
            sc_env[i:j] = np.minimum(sc_env[i:j], curve[:j - i])
    out = sub * 0.8 + (drums * 0.8 + mel) * sc_env
    if M['crackle']:
        cr = (rng.random(N) < 0.0006) * rng.standard_normal(N) * 3 + hp(rng.standard_normal(N), 3000) * 0.15
        out += lp(cr, 6000) * M['crackle']
    out = lp(out, 9000 if mood != 'chill' else 6500)
    out = out[:int(SR * dur)]
    tt = np.arange(len(out)) / SR
    out *= np.clip(tt / 1.2, 0, 1) * np.clip((dur - tt) / 2.0, 0, 1)
    out = np.tanh(out / (np.abs(out).max() + 1e-9) * 1.2)
    return out.astype(np.float32), dict(key=key + ' minor', bpm=bpm, mood=mood, scale=M['scale'], prog=prog, motif=motif)


def _read_audio(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768


def save(path, x, sr=SR):
    x = np.clip(x, -1, 1)
    with wave.open(path, 'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((x * 32767).astype(np.int16).tobytes())


def rms_db(x):
    return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9)


def mix(vo, dur, seed, mood, out_wav, below_db=18.0, duck_db=7.0, sfx=None):
    # 18 dB (was 14): Prateek 10 Nov 2026 wants soft, subtle beds, nothing loud or video-game-like.
    """Voice + new bed. Bed sits `below_db` under the voice's speech level, and dips another `duck_db` while words are spoken."""
    v = _read_audio(vo) if isinstance(vo, str) else vo
    v = hp(v, 70)
    N = int(SR * dur)
    v = np.pad(v, (0, max(0, N - len(v))))[:N]
    m, info = bed(dur, seed, mood)
    m = np.pad(m, (0, max(0, N - len(m))))[:N]
    # speech envelope (20 ms frames) -> smooth duck curve
    fr = int(SR * 0.02)
    nf = N // fr + 1
    e = np.array([np.sqrt(np.mean(v[i * fr:(i + 1) * fr] ** 2) + 1e-12) for i in range(nf)])
    speech = e > (np.max(e) * 0.06)
    spv = v[np.repeat(speech, fr)[:N]] if speech.any() else v
    v_db = rms_db(spv)
    # attack fast, release slow
    g = np.zeros(nf)
    for i in range(nf):
        tgt = 1.0 if speech[i] else 0.0
        g[i] = g[i - 1] + (tgt - g[i - 1]) * (0.5 if tgt > g[i - 1] else 0.06) if i else tgt
    duck = 10 ** (-duck_db * np.repeat(g, fr)[:N] / 20)
    m_db = rms_db(m)
    base = 10 ** ((v_db - below_db - m_db) / 20)
    mm = m * base * duck
    mm *= 10 ** ((v_db - below_db - rms_db(mm)) / 20)   # average bed level (after ducking) = below_db under the voice
    out = v + mm
    if sfx is not None:
        out[:len(sfx)] += sfx[:N]
    out = out / max(1.0, np.abs(out).max() / 0.97)
    save(out_wav, out)
    info.update(voice_db=round(float(v_db), 1), bed_avg_db=round(float(rms_db(mm)), 1),
                bed_under_voice_db=round(float(v_db - rms_db(mm)), 1), duck_db=duck_db)
    return info


if __name__ == "__main__":
    o, d, s = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    md = sys.argv[4] if len(sys.argv) > 4 else 'chill'
    x, inf = bed(d, s, md)
    save(o, x * 0.8)
    print(inf)
