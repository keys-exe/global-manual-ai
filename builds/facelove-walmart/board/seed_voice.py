"""Voice-stage cards on the Current board: the four §24I film voice masters (audio in an mp4), To check.
Usage: seed_voice.py '<json {KEY: asset_id}>' '<json {KEY: credits}>'"""
import json, time, pathlib, os, sys
os.chdir(pathlib.Path(__file__).resolve().parents[1])
B = "facelove-walmart"; now = int(time.time()*1000)
assets = json.loads(sys.argv[1]); credits = json.loads(sys.argv[2])
M = json.load(open("voice/masters.json")); J = json.load(open("voice/jobs.json"))
NAME = {"N": "Michelle", "C1": "Peter", "C2": "The woman, 41", "C3": "Rosa"}
FACE_REF = {"N": "N-MICHELLE-AFTER", "C1": "C1-PETER", "C2": "C2-YOUNGER", "C3": "C3-ROSA"}
out = pathlib.Path("board/json"); writes = []
for k, a in assets.items():
    c = json.load(open(f"voice/VOICE-{k}.call.json")); m = M[k]
    doc = {"build": B, "act": "Voice", "stage": "voice", "kind": "audio", "beat": f"VOICE-{k}", "title": f"{NAME[k]} — film voice master (§24I, neutral)",
           "line": c["dialogue"], "prompt": c["prompt"], "model": "seedance_2_5 · omni_reference · 720p · 9:16", "duration": m["master_s"], "status": "review", "regens": 0,
           "videoAsset": a, "videoType": "video/mp4", "videoConnector": "Higgsfield", "videoUrl": m["url"], "videoJob": J[k], "credits": credits[k], "videoAt": now, "updatedAt": now,
           "flow": ["video"],
           "note": f"Audio as generated (stream copy); only the idle silence outside the speech cut (0.4 s before / 0.5 s after). Clip {m['clip_s']} s → master {m['master_s']} s. Heard: {m['heard']}",
           "ingredients": [{"label": f"{NAME[k]} — face only (from the confirmed sheet's close-up)", "role": "@image1 · face", "kind": "character", "ref": f"{B}__{FACE_REF[k]}"}],
           "videoVersions": [{"v": 1, "asset": a, "type": "video/mp4", "url": m["url"], "model": "seedance_2_5", "connector": "Higgsfield", "credits": credits[k], "at": now, "note": ""}]}
    json.dump(doc, open(out / f"gen_VOICE-{k}.json", "w"), ensure_ascii=False)
    writes.append({"op": "set", "collection": "generations", "doc_id": f"{B}__VOICE-{k}", "file_path": str((out / f"gen_VOICE-{k}.json").resolve())})
json.dump(writes, open(out / "voice_batch.json", "w")); print(json.dumps(writes))
