"""Turn a topics_all entry into a bodyfix TOPIC dict (scenes, colours, sizes)."""
from kit import YEL, RED, GRN, WHITE, GREY


def _sz(txt, big, mid, small):
    return big if len(txt) < 18 else mid if len(txt) < 24 else small


QUIZ = {3, 4, 6, 11, 12, 13, 14, 15, 16, 19, 20, 22, 25, 30, 31, 34, 37, 42, 43, 44}


def to_topic(e):
    h1, h2 = e["hook"]
    hook = [(h1, WHITE)] + ([(h2, YEL)] if h2 else []) + [(f"BODY FIX #{e['no']}", GREY)]
    why = [(e["why"][0], YEL, _sz(e["why"][0], 64, 54, 46)), (e["why"][1], WHITE, _sz(e["why"][1], 54, 48, 42))]
    cols = [WHITE, YEL, YEL, GRN]
    sizes = [(56, 50, 44), (74, 62, 52), (56, 50, 44), (48, 44, 38)]
    fact = [(t, cols[i], _sz(t, *sizes[i])) for i, t in enumerate(e["fact"])]
    sweat = 0.8 if e["mouth1"] in ("grit", "frown") else 0.0
    fx1 = [("bubble", e["bubble"])]
    if e["marks"] == "Z":
        fx1.append(("zzz",))
    elif e["marks"]:
        fx1.append(("marks", e["marks"], YEL if e["marks"] == "?" else RED, 1.0))
    if e["pose1"] == "belly":
        fx1.append(("belly", 0.6))
    scenes = [
        dict(env=e["env1"], sid=dict(pose=e["pose1"], mouth=e["mouth1"], sweat=sweat, squint=0.25), fx=fx1),
        dict(env="studio", sid=dict(pose="think", mouth="flat", squint=0.4, look=(0.5, -0.3))),
        dict(env="studio", sid=dict(pose="point", mouth="smirk", raise_=0.4)),
        dict(env=e["env4"], sid=dict(pose="stand", mouth="o", eyes=1.15), fx=[("float", e["props4"])] if e["props4"] else None),
        dict(env=e["env5"], sid=dict(pose="yes" if not e["walk5"] else "stand", mouth="smile"), walk=e["walk5"],
             fx=[("float", e["props5"])] if e["props5"] else None),
        dict(env="studio", sid=dict(pose="stand", mouth="frown", sad=0.4)),
        dict(env=e["env1"] if e["env1"] != "studio" else "morning", sid=dict(pose="wave", mouth="bigsmile"), fx=[("float", ["📲"])]),
    ]
    q1 = "QUICK QUIZ" if e["no"] in QUIZ else e["q1"]
    return dict(no=e["no"], mood=e["mood"], src=e["src"], hook=hook, hook_stamp=e["stamp"], q1=q1, q2=e["q2"],
                opts=e["opts"], answer=e["ans"], why=why, fact=fact, fix=e["fix"], flags=e["flags"], cta=e["cta"],
                caps=e["caps"], scenes=scenes)
