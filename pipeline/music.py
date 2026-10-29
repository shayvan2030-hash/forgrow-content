"""Original background music, synthesised from code — no third-party recording, sample or loop is used,
so there is no external licence to clear (organic posts and paid ads alike).

Usage: python3 pipeline/music.py OUT.wav --seconds 36 [--bpm 96] [--seed 7] [--key A]
Style: calm, warm "explainer" bed — soft pad chords, a plucked arpeggio, light kick and shaker.
"""
import argparse, wave
import numpy as np

SR = 44100
NOTE = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    try:
        from scipy.signal import lfilter
        return lfilter([1 - a], [1, -a], x)
    except ImportError:
        y = np.empty_like(x); acc = 0.0
        for i, v in enumerate(x):  # one-pole filter
            acc = (1 - a) * v + a * acc; y[i] = acc
        return y


def env(n, a, d, s, r):
    a, d, r = int(a * SR), int(d * SR), int(r * SR)
    s_len = max(0, n - a - d - r)
    e = np.concatenate([np.linspace(0, 1, a, False), np.linspace(1, s, d, False),
                        np.full(s_len, s), np.linspace(s, 0, r)])
    return np.pad(e, (0, max(0, n - len(e))))[:n]


def saw(f, n, detune=0.0):
    t = np.arange(n) / SR
    out = np.zeros(n)
    for k in range(1, 12):
        out += np.sin(2 * np.pi * f * (1 + detune) * k * t) / k
    return out


def build(seconds, bpm, seed, key):
    rng = np.random.default_rng(seed)
    total = int(seconds * SR)
    mix = np.zeros(total + SR * 2)
    beat = 60 / bpm
    root = 57 + NOTE[key] - 9  # A3 by default
    # i – VI – III – VII  (minor-key progression, hopeful feel)
    prog = [[0, 3, 7], [-4, 0, 3], [3, 7, 10], [-2, 2, 5]]
    bar = beat * 4
    n_bars = int(np.ceil(seconds / bar))
    for b in range(n_bars):
        chord = prog[b % 4]
        start = int(b * bar * SR); n = int(bar * SR)
        # pad
        pad = sum(saw(hz(root + c), n, d) for c in chord for d in (-0.003, 0.003))
        pad = lowpass(pad, 900) * env(n, 0.6, 0.4, 0.8, 0.8) * 0.045
        mix[start:start + n] += pad
        # bass on beats 1 and 3
        for q in (0, 2):
            s = start + int(q * beat * SR); m = int(beat * 1.6 * SR)
            bass = np.sin(2 * np.pi * hz(root + chord[0] - 12) * np.arange(m) / SR)
            mix[s:s + m] += bass * env(m, 0.01, 0.2, 0.5, 0.3) * 0.16
        # plucked arpeggio (8ths), enters after 2 bars
        if b >= 2:
            pattern = [0, 1, 2, 1, 2, 0, 1, 2]
            for e8 in range(8):
                s = start + int(e8 * beat / 2 * SR); m = int(beat * 0.9 * SR)
                note = root + 12 + chord[pattern[e8]] + (12 if e8 == 4 else 0)
                pl = lowpass(saw(hz(note), m), 2400) * env(m, 0.003, 0.18, 0.0, 0.05)
                mix[s:s + m] += pl * (0.05 + 0.01 * rng.random())
        # kick on 1 & 3, shaker on 8ths — from bar 4
        if b >= 4:
            for q in range(4):
                s = start + int(q * beat * SR)
                if q in (0, 2):
                    m = int(0.25 * SR); t = np.arange(m) / SR
                    kick = np.sin(2 * np.pi * (110 * np.exp(-t * 25) + 45) * t) * np.exp(-t * 14)
                    mix[s:s + m] += kick * 0.22
                for h in (0, 0.5):
                    hs = s + int(h * beat * SR); m = int(0.06 * SR)
                    noise = rng.standard_normal(m)
                    noise = lowpass(noise - lowpass(noise, 5000), 9000)
                    mix[hs:hs + m] += noise * np.exp(-np.arange(m) / SR * 60) * (0.016 if h else 0.010)
    mix = mix[:total]
    # fade in/out + normalise
    f = int(1.5 * SR)
    mix[:f] *= np.linspace(0, 1, f); mix[-f:] *= np.linspace(1, 0, f)
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.7
    return mix


def save(path, mono):
    st = np.stack([mono, mono], axis=1)
    data = (st * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(data.tobytes())


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("--seconds", type=float, default=36)
    ap.add_argument("--bpm", type=float, default=96); ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--key", default="A")
    a = ap.parse_args()
    save(a.out, build(a.seconds, a.bpm, a.seed, a.key))
    print("wrote", a.out)
