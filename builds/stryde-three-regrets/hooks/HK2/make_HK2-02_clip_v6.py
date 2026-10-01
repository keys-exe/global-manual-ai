"""HK2-02 clip v6 (user Fix on clip v5 "the screen zoom into the three high bar", 2026-10-01): composited, no model — from the confirmed
v13 frame (HK2-01 frame, bar chart with blurred labels) the camera pushes in on the three tall orange bars, eased, holding on them at the
end; a light breath sway. Built on a 3x canvas (base upscaled, chart page warped at 3x) so the bars stay sharp when close. 3.04 s, 25 fps."""
import os, subprocess, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)) + "/"
FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
K = 3
base = Image.open(D + "HK2-01_v10.png").convert("RGB")
ch = Image.open(D + "ref/HK2-02_chart_v13.png").convert("RGB")
W, H = ch.size; ch3 = ch.resize((W * K, H * K), Image.LANCZOS)
TL, TR, BR, BL = (265, 1014), (1037, 1045), (1003, 1546), (275, 1500)
def coeffs(dst, src):
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float))
C3 = [(x * K, y * K) for x, y in (TL, TR, BR, BL)]
big = base.resize((base.width * K, base.height * K), Image.LANCZOS)
warp = ch3.transform(big.size, Image.PERSPECTIVE, coeffs(C3, [(0, 0), (W * K, 0), (W * K, H * K), (0, H * K)]).tolist(), resample=Image.BICUBIC)
m = Image.new("L", big.size, 0); ImageDraw.Draw(m).polygon(C3, fill=255)
inner = m.filter(ImageFilter.MinFilter(27))
bw = np.asarray(base, float); mi1 = np.asarray(Image.new("L", base.size, 0)); mk = Image.new("L", base.size, 0); ImageDraw.Draw(mk).polygon([TL, TR, BR, BL], fill=255)
white = np.percentile(bw[np.asarray(mk.filter(ImageFilter.MinFilter(9))) > 0], 90, axis=0)
ww = np.asarray(warp, float) / 255.0 * white
big = Image.composite(Image.fromarray(np.clip(ww, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.5)), big, inner.filter(ImageFilter.GaussianBlur(9)))
# target: the middle of the three tall bars on the chart page -> image coords (forward map page -> image)
Minv = coeffs([(0, 0), (W, 0), (W, H), (0, H)], [TL, TR, BR, BL])
def fwd(u, v):
    a, b, c, d, e, f, g, h = Minv; den = g * u + h * v + 1; return ((a * u + b * v + c) / den, (d * u + e * v + f) / den)
slot = (W - 240) / 9; tx, ty = fwd(120 + slot * 1.5, 470)
BW, BH = base.size; Z0, Z1 = 1.03, 4.6
FPS, DUR = 25, 3.04; n = int(round(FPS * DUR)); out = D + "HK2-02_clip_v6.mp4"
p = subprocess.Popen([FF, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1080x1920", "-r", str(FPS), "-i", "-",
                      "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
for i in range(n):
    s = i / FPS; t = min(max((s - 0.25) / 2.35, 0), 1); e = t * t * (3 - 2 * t)
    z = Z0 * (Z1 / Z0) ** e
    cx = BW / 2 + (tx - BW / 2) * e + 3.0 * math.sin(2 * math.pi * 0.31 * s); cy = BH / 2 + (ty - BH / 2) * e + 2.2 * math.sin(2 * math.pi * 0.27 * s + 0.5)
    cw, chh = BW / z, BH / z
    x0 = min(max(cx - cw / 2, 0), BW - cw); y0 = min(max(cy - chh / 2, 0), BH - chh)
    fr = big.crop((round(x0 * K), round(y0 * K), round((x0 + cw) * K), round((y0 + chh) * K))).resize((1080, 1920), Image.LANCZOS)
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait(); print(out, n, round(tx), round(ty))
