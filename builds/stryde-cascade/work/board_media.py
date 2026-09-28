"""List board media to upload: every B-roll frame (all versions) and clip (all versions); split files over 15 MB.
Writes work/board/upload_list.json = [{beat, kind, v, file, parts:[paths]}]."""
import json, os, re, subprocess, glob
from pathlib import Path
B = Path(__file__).resolve().parent.parent
os.chdir(B)
SPLIT = B / "renders" / "parts"; SPLIT.mkdir(exist_ok=True)
rows = [r["beat"] for r in json.load(open("actmap.json"))]
out = []
def parts(f):
    if os.path.getsize(f) <= 15_000_000: return [f]
    stem, ext = os.path.splitext(os.path.basename(f))
    pre = SPLIT / f"{stem}.part"
    if not glob.glob(f"{pre}*"):
        subprocess.run(["split", "-b", "15000000", "-d", "-a", "2", f, str(pre)], check=True)
    ps = sorted(glob.glob(f"{pre}[0-9][0-9]"))
    res = []
    for p in ps:
        n = f"{p}{ext}"; os.rename(p, n) if not os.path.exists(n) else None; res.append(n)
    return sorted(glob.glob(f"{pre}[0-9][0-9]{ext}"))
for b in rows:
    fv = sorted(glob.glob(f"renders/{b}_f_v*.png"))
    for i, f in enumerate(fv): out.append({"beat": b, "kind": "image", "v": i + 1, "file": f, "parts": parts(f)})
    if os.path.exists(f"renders/{b}_f.png"): out.append({"beat": b, "kind": "image", "v": len(fv) + 1, "file": f"renders/{b}_f.png", "parts": parts(f"renders/{b}_f.png")})
    cv = sorted(glob.glob(f"renders/{b}_v[0-9].mp4"))
    for i, f in enumerate(cv): out.append({"beat": b, "kind": "video", "v": i + 1, "file": f, "parts": parts(f)})
    if os.path.exists(f"renders/{b}.mp4"): out.append({"beat": b, "kind": "video", "v": len(cv) + 1, "file": f"renders/{b}.mp4", "parts": parts(f"renders/{b}.mp4")})
json.dump(out, open("work/board/upload_list.json", "w"), indent=1)
allp = [p for o in out for p in o["parts"]]
print(len(out), "items", len(allp), "files", round(sum(os.path.getsize(p) for p in allp) / 1e6), "MB")
