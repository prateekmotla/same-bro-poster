"""Usage: python3 timings.py <dir>  -> writes lines.json & wclean.json using vo.txt (tags stripped) + words.json"""
import json, re, sys
d = sys.argv[1]
w = json.load(open(f"{d}/words.json")); w = w['words'] if isinstance(w, dict) else w
w = [x for x in w if x.get('type', 'word') == 'word']
# drop tag tokens: any token sequence from '[...' to '...]'
clean, intag = [], False
for x in w:
    t = x['text']
    if t.startswith('['):
        intag = True
    if not intag:
        clean.append(x)
    if t.endswith(']'):
        intag = False
lines = [re.sub(r'\[[^\]]*\]\s*', '', l).strip() for l in open(f"{d}/vo.txt").read().split('\n') if l.strip()]
out, i = [], 0
for l in lines:
    n = len(l.split()); seg = clean[i:i + n]; i += n
    out.append([round(seg[0]['start'], 2), round(seg[-1]['end'], 2)])
print(i, len(clean))
json.dump(out, open(f"{d}/lines.json", "w"))
json.dump([[x['text'], x['start'], x['end']] for x in clean], open(f"{d}/wclean.json", "w"))
for k, o in enumerate(out): print(k + 1, o, lines[k][:50])
