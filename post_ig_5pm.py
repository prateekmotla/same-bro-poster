"""
Instagram-only 5 PM IST slot for the Same Bro psychology series (queue_ig5pm/).
Each folder is named YYYY-MM-DD-NN and posts on that IST date at 17:00.
YouTube copies of these reels are scheduled separately in YouTube Studio, so this posts Instagram only.
The workflow starts a little early (GitHub cron runs late); this script waits until 17:00 IST.
"""
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import poster

ROOT = Path(__file__).parent
Q = ROOT / "queue_ig5pm"
IST = timezone(timedelta(hours=5, minutes=30))


def main():
    now = datetime.now(IST)
    today = now.strftime("%Y-%m-%d")
    posted = poster.load_posted()
    due = [f for f in sorted(Q.iterdir())
           if f.is_dir() and f.name[:10] <= today
           and "instagram" not in posted.get(f"ig5pm/{f.name}", {})
           and (f / "video.mp4").exists()]
    if not due:
        poster.log("Nothing due for the 5 PM Instagram slot.")
        return 0
    folder = due[0]  # oldest first, one per day
    target = now.replace(hour=17, minute=0, second=0, microsecond=0)
    if os.getenv("WAIT", "1") == "1" and now < target:
        wait = (target - now).total_seconds()
        poster.log(f"Waiting {int(wait)}s until 17:00 IST")
        time.sleep(wait)

    meta = json.loads((folder / "meta.json").read_text())
    repo = os.environ.get("GITHUB_REPOSITORY", "prateekmotla/same-bro-poster")
    os.environ["MEDIA_BASE_URL"] = f"https://raw.githubusercontent.com/{repo}/main/queue_ig5pm"
    try:
        pid = poster.post_instagram(folder, meta)
    except Exception as e:
        poster.log(f"instagram FAILED: {e}")
        with open("errors.log", "a") as fh:
            fh.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} ig5pm/{folder.name} instagram: {str(e)[:600]}\n")
        return 1
    if not poster.DRY_RUN:
        posted = poster.load_posted()
        posted.setdefault(f"ig5pm/{folder.name}", {})["instagram"] = {
            "id": pid, "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        poster.save_posted(posted)
    return 0


if __name__ == "__main__":
    sys.exit(main())
