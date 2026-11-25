"""Write meta.json (queue format) for each b<NN> folder: YouTube title/description, IG caption, tags."""
import json, os, sys, re
sys.path.insert(0, "/home/claude/sid/shorts")
import topics_all as TA

E = [dict(no=1, slug="constipation", src="SRC: NHS - Constipation self-help",
          hook=("15 MIN IN THE TOILET?", "STILL NOTHING?"), stamp="YOU'RE SITTING WRONG",
          caps=["15 min in the toilet, phone in hand... still NOTHING? Bro, it's how you SIT.", "Guess: what actually helps? A, B or C?",
                "B is right. Feet on a small stool, knees above hips = straighter path, easier exit.",
                "Timing too: go 15-20 min after breakfast or warm water. That's when your gut pushes.",
                "Don't hold the urge. Walk daily, add fibre slowly, with WATER.",
                "Blood, weight loss without trying, or it keeps happening? See a DOCTOR.",
                "Send this to the friend who scrolls reels in the toilet."],
          cta=["THE FRIEND WHO SCROLLS", "REELS IN THE TOILET"])] + TA.E

def clean(s):
    return s.replace("<", "").replace(">", "")

def tc(s):
    return " ".join(w if w.isupper() and len(w) <= 4 else w.capitalize() for w in s.lower().split()).replace("'S", "'s")

for e in E:
    d = [x for x in os.listdir('.') if x.startswith(f"b{e['no']:02d}_")][0]
    h1, h2 = e["hook"]
    hook = (h1 + (" " + h2 if h2 else "")).strip()
    src = e["src"].replace("SRC: ", "")
    caps = e["caps"]
    title = clean(f"{tc(hook)} {tc(e['stamp']).rstrip('.')} | Body Fix #{e['no']} #Shorts")
    if len(title) > 100:
        title = clean(f"{tc(hook)} | Body Fix #{e['no']} #Shorts")
    tag = re.sub(r'[^a-z]', '', e['slug'])
    desc = clean(f"BODY FIX #{e['no']}. {caps[0]}\n{caps[2]}\n{caps[3]}\nFix: {caps[4]}\nRed flags: {caps[5]}\n"
                 f"Not medical advice. See a doctor if it doesn't go away.\nSource: {src}\n#samebro #bodyfix #healthtips #{tag} #shorts")
    cta = " ".join(e["cta"]).lower().replace("the friend", "the friend")
    ig = (f"Body Fix #{e['no']} 🩺 {caps[0]}\n\nGuess A, B or C before the reveal 👀 Comment your answer!\n\n✅ {caps[4]}\n\n"
          f"Send this to {cta} 👇\n\n🚩 {caps[5]}\nNot medical advice.\nSource: {src}\n\n"
          f"#samebro #bodyfix #healthtips #{tag} #health #desi #india")
    meta = {"type": "short", "approved": True, "platforms": ["instagram", "youtube"], "category_id": 27,
            "youtube_privacy": "public", "made_for_kids": False, "youtube_title": title, "youtube_description": desc,
            "instagram_caption": ig, "tags": ["same bro", "body fix", "health tips", tag, "home remedy", "shorts"]}
    json.dump(meta, open(f"{d}/meta.json", "w"), ensure_ascii=False, indent=2)
print("ok", len(E))
