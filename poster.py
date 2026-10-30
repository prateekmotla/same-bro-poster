"""
Auto-Poster
Posts the next APPROVED reel from queue/ to Instagram (Reels) and YouTube (Shorts).
Runs on GitHub Actions on a schedule. Free.

Queue layout:
  queue/<id>/video.mp4    vertical 9:16, H.264 + AAC (keep a music track), under 3 min
  queue/<id>/meta.json    see queue/001-example/meta.json

Each item's meta.json has "type": "short" (Reel + YouTube Short, under 3 min)
or "long" (regular YouTube video, 8+ min; Instagram optional).
Run:  python poster.py short   or   python poster.py long
Only items with "approved": true are posted. Posted ids are recorded in posted.json.
Set DRY_RUN=1 to test without posting.
"""
import json
import os
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).parent
QUEUE = ROOT / "queue"
POSTED_FILE = ROOT / "posted.json"
DRY_RUN = os.getenv("DRY_RUN") == "1"
IG_API = "https://graph.instagram.com/v25.0"


def log(msg):
    print(f"[poster] {msg}", flush=True)


def load_posted():
    if POSTED_FILE.exists():
        return json.loads(POSTED_FILE.read_text())
    return {}


def save_posted(data):
    POSTED_FILE.write_text(json.dumps(data, indent=2) + "\n")


def next_items(posted, kind):
    """For each platform, the next approved item of this kind not yet posted there.

    Platforms advance independently, so an Instagram outage never blocks YouTube (and vice versa).
    Items with meta "priority": true (e.g. the Diwali series) are time-sensitive: on a platform that
    is behind (Instagram backlog), they jump the line as soon as YouTube posts them (same slot).
    Returns [(folder, meta, video, platform), ...]."""
    default = ["instagram", "youtube"] if kind == "short" else ["youtube"]
    items = []
    for folder in sorted(p for p in QUEUE.iterdir() if p.is_dir()):
        meta_path = folder / "meta.json"
        video = folder / "video.mp4"
        if not meta_path.exists() or not video.exists():
            continue
        meta = json.loads(meta_path.read_text())
        if not meta.get("approved") or meta.get("type", "short") != kind:
            continue
        items.append((folder, meta, video))

    def pending(platform):
        return [it for it in items
                if platform in it[1].get("platforms", default)
                and platform not in posted.get(it[0].name, {})]

    out = []
    yt = pending("youtube")
    yt_now = yt[0] if yt else None
    if yt_now:
        out.append((*yt_now, "youtube"))
    for platform in sorted({p for it in items for p in it[1].get("platforms", default)} - {"youtube"}):
        cand = pending(platform)
        if not cand:
            continue
        def due(it):  # priority item already out on YouTube (or going out now)
            return "youtube" in posted.get(it[0].name, {}) or (yt_now and it[0] == yt_now[0])
        pri = [it for it in cand if it[1].get("priority") and due(it)]
        rest = [it for it in cand if not (it[1].get("priority") and not due(it))]
        pick = pri[0] if pri else (rest[0] if rest else None)
        if pick:
            out.append((*pick, platform))
    return out


# ---------------- Instagram (Instagram API with Instagram Login) ----------------

def public_video_url(folder):
    base = os.getenv("MEDIA_BASE_URL")
    if not base:
        repo = os.environ["GITHUB_REPOSITORY"]
        branch = os.getenv("GITHUB_REF_NAME", "main")
        base = f"https://raw.githubusercontent.com/{repo}/{branch}/queue"
    return f"{base.rstrip('/')}/{folder.name}/video.mp4"


def post_instagram(folder, meta):
    caption = meta.get("instagram_caption") or meta.get("caption", "")
    url = public_video_url(folder)
    log(f"Instagram: creating reel container from {url}")
    if DRY_RUN:
        return "dry-run"
    token = os.environ["IG_ACCESS_TOKEN"]
    user_id = os.environ["IG_USER_ID"]

    r = requests.post(f"{IG_API}/{user_id}/media", data={
        "media_type": "REELS",
        "video_url": url,
        "caption": caption,
        "share_to_feed": "true",
        "access_token": token,
    }, timeout=60)
    if not r.ok:
        raise RuntimeError(f"Instagram container failed {r.status_code}: {r.text[:500]}")
    container = r.json()["id"]

    # Wait for Instagram to process the video (up to ~10 min)
    for _ in range(60):
        s = requests.get(f"{IG_API}/{container}", params={
            "fields": "status_code,status", "access_token": token}, timeout=30).json()
        code = s.get("status_code")
        if code == "FINISHED":
            break
        if code in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"Instagram processing failed: {s}")
        time.sleep(10)
    else:
        raise RuntimeError("Instagram processing timed out")

    r = requests.post(f"{IG_API}/{user_id}/media_publish", data={
        "creation_id": container, "access_token": token}, timeout=60)
    if not r.ok:
        raise RuntimeError(f"Instagram publish failed {r.status_code}: {r.text[:500]}")
    media_id = r.json()["id"]
    log(f"Instagram: published {media_id}")
    return media_id


# ---------------- YouTube (Data API v3) ----------------

def post_youtube(folder, meta, video):
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    title = meta.get("youtube_title") or meta.get("title", "New video")
    if meta.get("type", "short") == "short" and "#shorts" not in title.lower():
        title = f"{title} #Shorts"
    body = {
        "snippet": {
            "title": title[:100],
            "description": meta.get("youtube_description") or meta.get("caption", ""),
            "tags": meta.get("tags", []),
            "categoryId": str(meta.get("category_id", 1)),  # 1 = Film & Animation
        },
        "status": {
            "privacyStatus": meta.get("youtube_privacy", "public"),
            "selfDeclaredMadeForKids": bool(meta.get("made_for_kids", False)),
        },
    }
    log(f"YouTube: uploading '{title}'")
    if DRY_RUN:
        return "dry-run"

    creds = Credentials(
        token=None,
        refresh_token=os.environ["YT_REFRESH_TOKEN"],
        client_id=os.environ["YT_CLIENT_ID"],
        client_secret=os.environ["YT_CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token",
        scopes=["https://www.googleapis.com/auth/youtube.upload"],
    )
    yt = build("youtube", "v3", credentials=creds, cache_discovery=False)
    req = yt.videos().insert(part="snippet,status", body=body,
                             media_body=MediaFileUpload(str(video), resumable=True, chunksize=8 * 1024 * 1024))
    resp = None
    while resp is None:
        _, resp = req.next_chunk()
    log(f"YouTube: published https://youtu.be/{resp['id']}")

    thumb = folder / "thumbnail.jpg"
    if thumb.exists():  # needs a phone-verified YouTube channel
        try:
            yt.thumbnails().set(videoId=resp["id"], media_body=MediaFileUpload(str(thumb))).execute()
            log("YouTube: thumbnail set")
        except Exception as e:
            log(f"YouTube: thumbnail skipped ({e})")
    return resp["id"]


def main():
    kind = sys.argv[1] if len(sys.argv) > 1 else "short"
    if kind not in ("short", "long"):
        sys.exit("Usage: python poster.py short|long")
    posted = load_posted()
    items = next_items(posted, kind)
    if not items:
        log(f"No approved '{kind}' videos left in the queue. Skipping.")
        return 0

    failures = 0
    for folder, meta, video, platform in items:
        log(f"Posting {folder.name} to {platform}")
        try:
            if platform == "instagram":
                pid = post_instagram(folder, meta)
            elif platform == "youtube":
                pid = post_youtube(folder, meta, video)
            else:
                log(f"Unknown platform '{platform}', skipping")
                continue
            if not DRY_RUN:
                posted.setdefault(folder.name, {})[platform] = {
                    "id": pid, "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
                save_posted(posted)
        except Exception as e:  # keep going so one platform failing doesn't block the other
            failures += 1
            log(f"{platform} FAILED: {e}")
            with open("errors.log", "a") as fh:
                fh.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {folder.name} {platform}: {str(e)[:600]}\n")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
