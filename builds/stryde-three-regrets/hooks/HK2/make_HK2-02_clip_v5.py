"""HK2-02 clip v5 (user "make clip for HK2-02", 2026-10-01, frame v13): composited, no model, so the chart stays exact — the v13 frame
(HK2-01 frame + bar chart, blurred labels) held still with a gentle handheld breath sway and a 3% zoom, as the HK2-01/BR-057 clips.
3.04 s, 25 fps, 1080x1920, silent. Motion plan: the chart holds still on the screen, her hands still, a slight breath sway."""
import os, subprocess, math
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)) + "/"
FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
base = Image.open(D + "HK2-02_v13.png").convert("RGB")
FPS, DUR = 25, 3.04
n = int(round(FPS * DUR)); out = D + "HK2-02_clip_v5.mp4"
p = subprocess.Popen([FF, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1080x1920", "-r", str(FPS), "-i", "-",
                      "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
for i in range(n):
    s = i / FPS
    dx = 4.0 * math.sin(2 * math.pi * 0.31 * s) + 1.5 * math.sin(2 * math.pi * 0.83 * s + 1.0)
    dy = 3.0 * math.sin(2 * math.pi * 0.27 * s + 0.5) + 1.2 * math.sin(2 * math.pi * 0.71 * s)
    rot = 0.12 * math.sin(2 * math.pi * 0.23 * s)
    fr = base.rotate(rot, resample=Image.BICUBIC, center=(768, 1376), translate=(dx, dy))
    z = 1.03; cw, ch = 1536 / z, 2752 / z; x0, y0 = (1536 - cw) / 2, (2752 - ch) / 2
    fr = fr.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize((1080, 1920), Image.LANCZOS)
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait(); print(out, n)
