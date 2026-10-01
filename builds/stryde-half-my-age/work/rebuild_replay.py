"""Rebuild the board state from the repo's saved board writes (board/json) — used to move the build to a new account's boards.
Replays every Current-board write in commit order; Old-board writes are skipped. Output: <out>/gen/<BEAT>.json, docs, build."""
import json, re, subprocess, sys, pathlib, copy
OUT = pathlib.Path(sys.argv[1]); (OUT/"gen").mkdir(parents=True, exist_ok=True)
J = pathlib.Path("board/json")
log = subprocess.run(["git", "log", "--reverse", "--format=@%H", "--name-only", "--", "board/json"], capture_output=True, text=True).stdout
commits, seen = [], set()
for line in log.splitlines():
    line = line.strip()
    if line.startswith("@"): commits.append([]); continue
    if not line.startswith("builds/"): continue
    p = pathlib.Path(line).relative_to("builds/stryde-half-my-age/board/json")
    if p not in seen and (J/p).exists(): seen.add(p); commits[-1].append(p)
def rank(p):
    n = p.stem; m = re.match(r"([a-z]+?)(\d*)_", n)
    if not m or n.startswith(("gen_",)): return (0, 0)
    pre, num = m.group(1), int(m.group(2) or 1)
    return ({"clip": 0, "edit": 0}.get(pre, 1), num)
OLD = ("old", "oldv1", "sdold", "unusedold", "editold", "retire")
def beat_of(p):
    n, d = p.stem, p.parent.name
    m = re.match(r"^[a-z]+\d*_(.+)$", n); core = m.group(1) if m else n
    if n.startswith("edit"): return "EDIT-" + core
    core = re.sub(r"_v\d+$", "", core)
    if re.fullmatch(r"SH\d\d", core): return {"hka": "HKA", "hkb": "HKB", "hkc": "HKC", "hke": "HKE", "sc02": "SC02"}[d] + "-" + core
    return core
order = [p for c in commits for p in sorted(c, key=lambda p: (rank(p), str(p)))]
docs = {}
# stable sort: commit order, then rank inside a commit (approximated by rank among same-commit neighbours)
for p in order:
    if p.suffix != ".json": continue
    pre = re.match(r"^([a-z]+\d*)_", p.stem)
    if pre and pre.group(1).rstrip("0123456789") in OLD or p.stem.startswith(("editold", "sdold", "unusedold", "oldv1")): continue
    data = json.load(open(J/p))
    if isinstance(data, list):
        for w in data:
            if "data" in w and w.get("collection") == "generations":
                b = w["doc_id"].split("__", 1)[1]
                docs.setdefault(b, {}).update(copy.deepcopy(w["data"])) if w["op"] == "update" else docs.__setitem__(b, copy.deepcopy(w["data"]))
        continue
    if p.name in ("build.json", "absorption.json") or p.stem.startswith("doc_"): continue
    b = beat_of(p)
    if "build" in data and "beat" in data: docs[b] = copy.deepcopy(data)
    else: docs.setdefault(b, {}).update(copy.deepcopy(data))
for f in sorted(pathlib.Path("body").glob("SC0*/ingredients/*.board.json")):
    d = json.load(open(f)); docs[d.get("beat") or f.name.split(".")[0]] = d
for b, d in docs.items():
    if "beat" not in d: print("NO BASE", b, list(d)[:6])
    json.dump(d, open(OUT/"gen"/f"{b}.json", "w"), ensure_ascii=False, indent=1)
print(len(docs), "docs:", " ".join(sorted(docs)))
