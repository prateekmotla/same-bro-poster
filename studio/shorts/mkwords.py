"""mkwords.py <dir> "s1,e1;s2,e2;..." -> words.json with per-line bounds from Scribe (words spread evenly inside each line)."""
import json, sys
d, spec = sys.argv[1], sys.argv[2]
B = [tuple(map(float, p.split(','))) for p in spec.split(';')]
raw = [l for l in open(f"{d}/vo.txt").read().split('\n') if l.strip()]
assert len(raw) == len(B), (len(raw), len(B))
W = []
for l, (a, b) in zip(raw, B):
    toks = l.split()
    tags = [x for x in toks if x.startswith('[') and x.endswith(']')]
    real = [x for x in toks if not (x.startswith('[') and x.endswith(']'))]
    for x in tags:
        W.append({"text": x, "type": "word", "start": max(0, a - 0.06), "end": a - 0.01})
    n = len(real); step = (b - a) / n
    for i, x in enumerate(real):
        W.append({"text": x, "type": "word", "start": round(a + i * step, 3), "end": round(a + (i + 1) * step - 0.02, 3)})
json.dump({"words": W, "note": "line bounds from ElevenLabs Scribe; words spread within lines"}, open(f"{d}/words.json", "w"), ensure_ascii=False)
print(len(W), "words")
