"""Copy rendered Body Fix shorts into the poster queue, interleaved: Body Fix #k goes right after pending item 096+k
(folder '<NNN>b-body-fix-<kk>-<slug>'), so the queue alternates one existing short / one Body Fix.
Commits each; pushes once at the end. usage: queue_bf.py [--push]"""
import json, os, shutil, subprocess, sys
R = "/home/claude/same-bro-poster"
S = "/home/claude/sid/shorts"
def git(*a, check=True):
    return subprocess.run(["git", "-C", R, *a], check=check, capture_output=True, text=True)
done = []
for d in sorted(x for x in os.listdir(S) if x[:1] == "b" and x[1:3].isdigit() and "_" in x):
    k = int(d[1:3]); slug = d.split("_", 1)[1]
    if not os.path.exists(f"{S}/{d}/short.mp4") or not os.path.exists(f"{S}/{d}/meta.json"):
        continue
    if os.path.exists(f"{S}/{d}/.ok") is False:
        continue  # only frames-checked renders
    q = f"{R}/queue/{96 + k:03d}b-body-fix-{k:02d}-{slug}"
    if os.path.exists(f"{q}/video.mp4") and os.path.getmtime(f"{q}/video.mp4") >= os.path.getmtime(f"{S}/{d}/short.mp4"):
        continue
    os.makedirs(q, exist_ok=True)
    shutil.copy(f"{S}/{d}/short.mp4", f"{q}/video.mp4")
    shutil.copy(f"{S}/{d}/meta.json", f"{q}/meta.json")
    git("add", q)
    git("-c", "user.name=prateekmotla", "-c", "user.email=prateekmotla1199@gmail.com", "commit", "-q", "-m",
        f"Queue Body Fix #{k} ({slug})\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
        "Claude-Session: https://claude.ai/code/session_01JaqxrrZzh68jNEaTpjZrca")
    done.append(k)
print("queued", done)
if "--push" in sys.argv and done:
    git("fetch", "--depth=50", "origin", "main")
    r = git("rebase", "origin/main", check=False)
    print(r.stdout[-300:], r.stderr[-300:])
    r = git("-c", "push.negotiate=true", "push", "origin", "HEAD:main", check=False)
    print("push rc", r.returncode, r.stderr[-400:])
