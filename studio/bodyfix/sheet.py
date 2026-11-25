"""Contact sheet of rendered shorts: one row per video, 8 frames (scene midpoints). usage: sheet.py out.png dir1 dir2 ..."""
import json, subprocess, sys
from PIL import Image, ImageDraw
out, dirs = sys.argv[1], sys.argv[2:]
W, H = 150, 266
sheet = Image.new("RGB", (W * 8 + 120, H * len(dirs)), (20, 20, 20))
for r, d in enumerate(dirs):
    L = json.load(open(f"{d}/lines.json"))
    ts = [0.3, 3.0] + [a + (b - a) * 0.8 for a, b in L[1:]]
    for c, t in enumerate(ts[:8]):
        p = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", f"{d}/short.mp4", "-frames:v", "1",
                            "-vf", f"scale={W}:{H}", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
        import io
        sheet.paste(Image.open(io.BytesIO(p.stdout)), (120 + c * W, r * H))
    ImageDraw.Draw(sheet).text((5, r * H + 120), d[:14], fill=(255, 255, 0))
sheet.save(out)
