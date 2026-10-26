"""Post-processing: color grade, bloom, vignette, film grain. Works on cairo ARGB32 surfaces via numpy."""
import numpy as np
from PIL import Image, ImageFilter

W, H = 1920, 1080
_rng = np.random.default_rng(11)
GRAIN = [(_rng.standard_normal((H // 2, W // 2)) * 3).astype(np.float32) for _ in range(8)]
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
_r = np.sqrt(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H / 2) / (H * 0.62)) ** 2)
VIG = np.clip(1.15 - 0.55 * _r ** 2.2, 0.35, 1.0)[..., None].astype(np.float32)

GRADES = {
    # lift (shadows tint), gain (highlights tint), saturation, vignette strength
    'night': dict(lift=(0.02, 0.025, 0.06), gain=(0.92, 0.97, 1.08), sat=0.9, vig=1.0, bloom=0.35),
    'phone': dict(lift=(0.01, 0.02, 0.05), gain=(0.9, 1.0, 1.12), sat=0.95, vig=1.0, bloom=0.45),
    'morning': dict(lift=(0.03, 0.02, 0.0), gain=(1.06, 1.0, 0.9), sat=1.0, vig=0.6, bloom=0.3),
    'void': dict(lift=(0.0, 0.0, 0.02), gain=(0.95, 0.95, 1.0), sat=0.7, vig=1.2, bloom=0.25),
    'warm': dict(lift=(0.03, 0.02, 0.01), gain=(1.05, 0.98, 0.9), sat=1.0, vig=0.8, bloom=0.3),
    'day': dict(lift=(0.03, 0.03, 0.03), gain=(1.0, 1.0, 1.0), sat=0.8, vig=0.6, bloom=0.2),
    'end': dict(lift=(0.02, 0.02, 0.02), gain=(1.02, 1.0, 0.97), sat=1.0, vig=0.5, bloom=0.2),
}


def post(surface, grade, frame_i, flash=0.0):
    g = GRADES[grade]
    buf = np.ndarray((H, W, 4), np.uint8, surface.get_data())
    rgb = buf[..., [2, 1, 0]].astype(np.float32) / 255.0
    # bloom (cheap): downscale, blur, upscale, screen-add bright parts
    if g['bloom'] > 0:
        small = Image.fromarray((rgb * 255).astype(np.uint8)).resize((W // 8, H // 8), Image.BILINEAR)
        small = small.filter(ImageFilter.GaussianBlur(6))
        bl = np.asarray(small.resize((W, H), Image.BILINEAR)).astype(np.float32) / 255.0
        bl = np.clip(bl - 0.45, 0, 1) * 1.8
        rgb = 1 - (1 - rgb) * (1 - bl * g['bloom'])
    # grade
    lift = np.array(g['lift'], np.float32)
    gain = np.array(g['gain'], np.float32)
    rgb = lift + rgb * (gain - lift)
    lum = rgb.mean(axis=2, keepdims=True)
    rgb = lum + (rgb - lum) * g['sat']
    # vignette
    v = 1 - (1 - VIG) * g['vig']
    rgb = rgb * v
    # grain
    gr = GRAIN[frame_i % len(GRAIN)]
    gr = np.repeat(np.repeat(gr, 2, axis=0), 2, axis=1)[..., None] / 255.0
    rgb = rgb + gr
    if flash > 0:
        rgb = rgb + (1 - rgb) * flash
    rgb = np.clip(rgb, 0, 1)
    out = (rgb * 255).astype(np.uint8)
    return out  # HxWx3 RGB
