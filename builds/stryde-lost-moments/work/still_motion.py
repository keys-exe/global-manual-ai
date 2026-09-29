"""Still-motion clip from a confirmed frame: the anatomy never moves.

Kling kept redrawing the anatomy on MECH-01 / MECH-02 (walking figure, cuts,
tendon sliding into the shin). Here the confirmed frame itself is the clip:
a slow push-in toward the tendon point plus a warm glow composited at one
fixed spot, so the point cannot drift.

python3 still_motion.py FRAME OUT.mp4 --point X Y --dur S --mode pulse|fade
"""
import argparse, math, subprocess
import numpy as np
from PIL import Image
import imageio_ffmpeg

W, H, FPS = 1080, 1920, 24

ap = argparse.ArgumentParser()
ap.add_argument("frame"); ap.add_argument("out")
ap.add_argument("--point", nargs=2, type=float, required=True)  # px in the frame
ap.add_argument("--dur", type=float, required=True)
ap.add_argument("--mode", choices=["pulse", "fade"], required=True)
ap.add_argument("--zoom", type=float, default=1.06)
ap.add_argument("--radius", type=float, default=38)  # glow sigma, frame px
a = ap.parse_args()

src = Image.open(a.frame).convert("RGB")
sw, sh = src.size
px, py = a.point
base = np.asarray(src).astype(np.float32)
yy, xx = np.mgrid[0:sh, 0:sw]
g = np.exp(-(((xx - px) ** 2 + (yy - py) ** 2) / (2 * a.radius ** 2)))
core = np.exp(-(((xx - px) ** 2 + (yy - py) ** 2) / (2 * (a.radius * 0.35) ** 2)))
warm = np.array([255, 170, 90], np.float32)
hot = np.array([255, 240, 215], np.float32)

n = int(round(a.dur * FPS))
cmd = [imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-loglevel", "error",
       "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
       "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "14", "-preset", "slow",
       "-movflags", "+faststart", a.out]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
for i in range(n):
    t = i / FPS
    e = 0.5 - 0.5 * math.cos(math.pi * i / max(n - 1, 1))  # ease in-out
    if a.mode == "pulse":  # one compression per second: sharp rise, slower fall
        ph = t % 1.0
        amp = 0.25 + 0.75 * (math.sin(math.pi * ph / 0.35) if ph < 0.35 else math.exp(-(ph - 0.35) * 4))
        amp *= 0.9
    else:  # the strap takes the load: the warmth settles and dims
        amp = 0.55 * (1 - e) + 0.08 * (0.5 + 0.5 * math.sin(2 * math.pi * t * 0.5))
    img = base + (g[..., None] * warm * 0.55 + core[..., None] * hot * 0.6) * amp
    img = np.clip(img, 0, 255).astype(np.uint8)
    # push-in toward the point, ease in-out
    z = 1 + (a.zoom - 1) * e
    cw, ch = sw / z, sw / z * H / W
    if ch > sh / z * 1.0001 or ch > sh:
        ch = sh / z; cw = ch * W / H
    cx = sw / 2 + (px - sw / 2) * 0.5 * e
    cy = sh / 2 + (py - sh / 2) * 0.5 * e
    x0 = min(max(cx - cw / 2, 0), sw - cw); y0 = min(max(cy - ch / 2, 0), sh - ch)
    fr = Image.fromarray(img).resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait()
print(a.out, n, "frames")
