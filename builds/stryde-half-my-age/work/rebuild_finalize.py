"""Second pass of the account move: version lists from the Kie logs, current version per beat, statuses from BUILD_NOTES
(2026-10-01 19:10 UTC), old board asset ids dropped (the files of replaced versions stay on the other account's Old board).
Writes <out>/final/<docid>.json and <out>/media.json (current file per card: url or local path)."""
import json, re, sys, glob, pathlib
OUT = pathlib.Path(sys.argv[1]); G = OUT/"gen"; F = OUT/"final"; F.mkdir(exist_ok=True)
B = "stryde-half-my-age"
def kie(path):
    t = open(path).read(); i = t.find("{\n")
    d = json.loads(t[i:]) if i >= 0 else {}
    return d if d.get("state") == "success" else None
def logs_for(beat):
    if beat.startswith("HK"):
        out = []
        for p in glob.glob(f"hooks/{beat[:3]}/{beat}*.kie.log"):
            m = re.search(r"\.v(\d+)\.kie\.log$", p); n = int(m.group(1)) if m else 1
            if re.search(r"\.(402|402b)\.log$", p): continue
            d = kie(p)
            if d: out.append((n, d))
        return sorted(out, key=lambda x: x[0])
    if beat.startswith("SC02"):
        out = []
        for p in glob.glob(f"body/SC02/{beat}.sd*.kie.log"):
            d = kie(p)
            if d: out.append((int(re.search(r"\.sd(\d+)\.", p).group(1)), d))
        return sorted(out, key=lambda x: x[0])
    return []
CONFIRM_EXCEPT = {"INFO-DRAWER", "OUT-C3-B3", "EDIT-HKA", "EDIT-HKB", "EDIT-HKC", "EDIT-HKE"}
media = {}
for f in sorted(G.glob("*.json")):
    d = json.load(open(f)); beat = d["beat"]; did = f"{B}__{beat}"
    for k in ("videoVersions", "imageVersions"):
        for x in d.get(k, []) or []:
            for z in ("asset", "archiveAsset", "parts", "archiveParts"): x.pop(z, None)
    for z in ("videoAsset", "imageAsset", "videoParts", "imageParts", "fault", "imageFault", "waiting"): d.pop(z, None)
    vids = logs_for(beat)
    if vids:
        old = {x.get("url"): x for x in d.get("videoVersions", []) or []}
        keep = [x for x in d.get("videoVersions", []) or [] if "seedance" not in (x.get("url") or "")]  # Wan pilots (SC02)
        base = len(keep); vv = list(keep)
        for i, (n, k) in enumerate(vids):
            u = k["urls"][0]; prev = old.get(u, {})
            vv.append({"v": base + (n if beat.startswith("HK") else i + 1), "type": "video/mp4", "url": u, "model": "bytedance/seedance-2-5",
                       "connector": "Kie AI", "credits": k.get("credits"), "job": k.get("taskId"), "at": prev.get("at") or int(re.search(r"/(\d{13})-", u).group(1)),
                       "note": prev.get("note", "")})
        d["videoVersions"] = vv
    for p in glob.glob(f"body/SC0*/ingredients/{beat}.v*.kie.log"):   # Fix renders made after the last saved board write
        n = int(re.search(r"\.v(\d+)\.kie", p).group(1)); k = kie(p)
        if k and all(x["v"] != n for x in d.get("imageVersions", [])):
            note = {"INFO-DRAWER": "THE DRAWER IS BIGGER AS WHERE IT CAME FROM", "OUT-C3-B3": "I WANT A DIFFERENT OUTFIT NOT THE SAME AS THE SCENE 2"}.get(beat, "")
            d["imageVersions"].append({"v": n, "type": "image/png", "url": k["urls"][0], "model": "gpt-image-2 image-to-image", "connector": "Kie AI",
                                       "credits": k.get("credits"), "job": k.get("taskId"), "at": int(re.search(r"(\d{13})", k["urls"][0]).group(1)), "note": note})
            d["imageCredits"] = k.get("credits")
    for k, step in (("videoVersions", "video"), ("imageVersions", "image")):
        vv = d.get(k)
        if not vv: continue
        cur = max(vv, key=lambda x: x["v"])
        for x in vv: x["archived"] = x is not cur
        if step == "video":
            d.update(videoUrl=cur.get("url", ""), videoType=cur.get("type", "video/mp4"), videoAt=cur.get("at"), credits=cur.get("credits", d.get("credits")))
            if cur.get("job"): d["videoJob"] = cur["job"]
        else:
            d.update(imageUrl=cur.get("url", ""), imageType=cur.get("type", "image/png"), imageAt=cur.get("at"))
        src = cur.get("url") or ""
        if beat.startswith("VOICE-"): src = f"voice/{beat[6:]}_voice_master.m4a"
        elif beat.startswith("VO-"): src = "eleven:" + d.get("prompt", "")
        elif beat.startswith("EDIT-"): src = f"recut:{beat[5:]}"
        else:
            loc = glob.glob(f"body/SC0*/ingredients/{beat}_v{cur['v']}.png")
            if loc: src = loc[0]
        media[did] = {"step": step, "v": cur["v"], "src": src, "type": cur.get("type") or ("audio/mp4" if step == "video" and d.get("kind") == "audio" else "")}
    # statuses (BUILD_NOTES 2026-10-01: everything confirmed except the two SC03 v2 cards and the hook edits v3)
    if beat not in CONFIRM_EXCEPT:
        if d.get("imageVersions"): d["imageStatus"] = "confirmed"
        d["status"] = "use"
    else:
        d["status"] = "review"
        if d.get("imageVersions"): d["imageStatus"] = "review"
    d = {k: v for k, v in d.items() if v != {"__delete__": True}}   # replayed delete markers
    d["movedFrom"] = "iamnotkeysi@gmail.com boards (2026-10-01); replaced versions' files stay on that account's Old board"
    json.dump(d, open(F/f"{did}.json", "w"), ensure_ascii=False, indent=1)
json.dump(media, open(OUT/"media.json", "w"), indent=1)
print(len(media), "cards with a current file")
