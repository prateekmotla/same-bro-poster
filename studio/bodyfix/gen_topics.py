"""Create b<NN>_<slug>/ folders (vo.txt + make.py) from topics_all.E."""
import os, sys
sys.path.insert(0, "/home/claude/sid/shorts")
import topics_all as TA
TEMPLATE = '''"""BODY FIX #{no}: {slug}. Source: {src}. Data in topics_all.py (entry no={no})."""
import sys
sys.path.insert(0, "/home/claude/sid/shorts")
import bodyfix as BF
import topics_all as TA
from bodyfix_topic import to_topic

if __name__ == "__main__":
    e = [x for x in TA.E if x["no"] == {no}][0]
    BF.run(to_topic(e), "{d}", sys.argv[1])
'''
for e in TA.E:
    d = f"/home/claude/sid/shorts/b{e['no']:02d}_{e['slug']}"
    os.makedirs(d, exist_ok=True)
    open(f"{d}/vo.txt", "w").write("\n".join(e["vo"]) + "\n")
    open(f"{d}/make.py", "w").write(TEMPLATE.format(no=e["no"], slug=e["slug"], src=e["src"], d=d))
print("ok", len(TA.E))
