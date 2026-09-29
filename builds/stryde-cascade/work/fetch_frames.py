import json, sys, subprocess
from PIL import Image
U = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"
urls = json.load(open("work/frame_urls.json")) if __import__("os").path.exists("work/frame_urls.json") else {}
for a in sys.argv[1:]:
    beat, name = a.split("=")
    urls[beat] = U + name
    subprocess.run(["curl", "-sSL", "--retry", "5", "--retry-all-errors", "-o", f"renders/{beat}_f.png", U + name], check=True)
json.dump(urls, open("work/frame_urls.json", "w"), indent=1)
beats = [a.split("=")[0] for a in sys.argv[1:]]
ims = [Image.open(f"renders/{b}_f.png").convert("RGB") for b in beats]
W = 400; H = int(W * 16 / 9)
for i in range(0, len(ims), 3):
    c = Image.new("RGB", (W * 3, H), "white")
    for j, im in enumerate(ims[i:i+3]): c.paste(im.resize((W, H)), (j * W, 0))
    c.save(f"renders/rv_{beats[i]}.jpg", quality=85); print(f"renders/rv_{beats[i]}.jpg", beats[i:i+3])
