# fetch completed Higgsfield results: args = BEAT=url ...
import sys, subprocess
from PIL import Image
for a in sys.argv[1:]:
    b, u = a.split("=", 1)
    p = f"renders/{b}.png"; subprocess.run(["curl", "-sSL", "-o", p, u], check=True)
    im = Image.open(p).convert("RGB"); im.resize((im.width * 900 // im.height, 900)).save(f"renders/{b}.view.jpg", quality=85)
    print(b, im.size)
