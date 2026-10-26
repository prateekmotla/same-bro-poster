"""usage: queue_short.py <video> <folder> <yt_title> <yt_desc> <ig_caption> <tags comma>"""
import json, os, shutil, subprocess, sys
v, folder, title, desc, cap, tags = sys.argv[1:7]
repo = "/home/claude/same-bro-poster"
subprocess.run(["git", "-C", repo, "pull", "-q", "origin", "main"], check=True)
d = f"{repo}/queue/{folder}"
os.makedirs(d, exist_ok=True)
shutil.copy(v, f"{d}/video.mp4")
json.dump({"type": "short", "approved": True, "platforms": ["instagram", "youtube"], "youtube_title": title,
           "youtube_description": desc, "instagram_caption": cap, "tags": [t.strip() for t in tags.split(",")],
           "category_id": 27, "youtube_privacy": "public", "made_for_kids": False},
          open(f"{d}/meta.json", "w"), ensure_ascii=False, indent=2)
subprocess.run(["git", "-C", repo, "add", f"queue/{folder}"], check=True)
subprocess.run(["git", "-C", repo, "-c", "user.name=prateekmotla", "-c", "user.email=prateekmotla1199@gmail.com", "commit", "-q", "-m",
                f"Queue short {folder}\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_0139YAN6cWpNdLLsN3YewLcm"], check=True)
subprocess.run(["git", "-C", repo, "push", "-q", "origin", "HEAD:main"], check=True)
print("queued", folder)
