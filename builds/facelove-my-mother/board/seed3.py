"""Voice stage board writes: 6 voice-master cards (stage voice) + 5 narration takes (stage vo), all To check; build doc voices."""
import json, time, pathlib
B = "facelove-my-mother"; now = int(time.time()*1000); out = pathlib.Path("board/json")
M = json.load(open("voice/masters.json")); jobs = json.load(open("voice/jobs.json"))
asset = {"N": "a18cb8f0efd03c458b9456c06daed590", "C1": "e025c7b46211e6124b710fb5aaa6bb7f", "C2": "f31c6135f59c46fa760f3064f5e20e7a",
         "C3": "1c0f2ee6cc18eae04b169909d6cbf4c3", "C5": "bac64a92a7e62a69e6b930d652555c39", "C6": "837560e98d2377447c9ec23a276eead3"}
face = {"N": "5794978ae475feb9e7398beede4afe76", "C1": "3a09b34ea3808585fceb31dccbb30886", "C2": "f25a86c0620bacff99d1bcd68ca88b54",
        "C3": "7c834cd6985c4b0b4983baf82ca6a538", "C5": "41167b19206c6b5f8883166bb591a8ef", "C6": "afbda13cbd9efd4f31f836a80942f80d"}
names = {"N": "Susan", "C1": "Greg", "C2": "Paula", "C3": "Beth", "C5": "Friend A", "C6": "Friend B"}
sheet = {"N": "N-SUSAN", "C1": "C1-GREG", "C2": "C2-PAULA", "C3": "C3-BETH", "C5": "C5-FRIEND-A", "C6": "C6-FRIEND-B"}
writes = []
for k, m in M.items():
    c = json.load(open(f"voice/VOICE-{k}.call.json")); cr = round(c["duration"] * 6.3, 2)
    doc = {"build": B, "act": "Voice", "stage": "voice", "kind": "audio", "beat": f"VOICE-{k}", "title": f"{names[k]} — film voice master (§24I, neutral)",
           "line": c["dialogue"], "prompt": c["prompt"], "model": "seedance_2_5 · omni_reference · 720p · 9:16", "duration": round(m["master_s"], 2),
           "status": "review", "regens": 0, "videoAsset": asset[k], "videoType": "video/mp4", "videoConnector": "Higgsfield", "videoUrl": m["url"], "videoJob": jobs[k],
           "credits": cr, "videoAt": now, "updatedAt": now, "flow": ["video"],
           "note": f"Audio as generated (stream copy); only the idle silence outside the speech cut (0.4 s before / 0.5 s after). Clip {m['clip_s']} s → master {round(m['master_s'], 2)} s. Heard: {m['heard']}",
           "ingredients": [{"label": f"{names[k]} — face only (from the confirmed sheet's close-up)", "role": "@image1 · face", "kind": "character", "asset": face[k], "type": "image/jpeg", "ref": f"{B}__{sheet[k]}"}],
           "videoVersions": [{"v": 1, "asset": asset[k], "type": "video/mp4", "url": m["url"], "model": "seedance_2_5", "connector": "Higgsfield", "credits": cr, "at": now, "note": ""}]}
    if k == "N": doc["note"] += " · Narrator clone 'Mother' (ElevenLabs, voice_id Keqdw9ZWsMjWZgsJl2h0) built from this master looped to 35.8 s."
    if k == "C1": doc["note"] += " · Listen for 'Paula's' — the transcript heard 'Paul is'."
    json.dump(doc, open(out / f"gen_VOICE-{k}.json", "w"), ensure_ascii=False); writes.append(("generations", f"{B}__VOICE-{k}", f"gen_VOICE-{k}.json"))
vo_asset = {"L008": "e5c1960f26dabc6bf21579fa0777123b", "L009": "2452b559ecf0af9c2d1253de30e5992f", "L021": "c8b98d4a77eb631ad22ca503e6f5da96",
            "L026": "63477d50c6816dee84e826d6857b95a4", "L027": "3b2e9da271cd3b9eac9c3a00f0d43c84"}
dur = {"L008": 16.2, "L009": 14.3, "L021": 6.8, "L026": 8.6, "L027": 18.2}
scene = {"L008": ("SC03", "Inside / the VO"), "L009": ("SC04", "Disappearing"), "L021": ("SC07", "She walks back in"), "L026": ("SC08", "The redirect"), "L027": ("SC09", "CTA + offer")}
for k, a in vo_asset.items():
    doc = {"build": B, "act": "Voice", "stage": "vo", "kind": "audio", "beat": f"VO-T1-{k}", "title": f"Narration {k} — {scene[k][0]} {scene[k][1]} (Susan, take 1)",
           "line": open(f"vo/{k}.lines.txt").read().strip(), "prompt": open(f"vo/{k}.tagged.fitted.txt").read().strip(),
           "model": "eleven_v4 · voice 'Mother' (Keqdw9ZWsMjWZgsJl2h0) · speed 1.0", "duration": dur[k], "status": "review", "regens": 0,
           "videoAsset": a, "videoType": "video/mp4", "videoConnector": "ElevenLabs", "videoAt": now, "updatedAt": now, "flow": ["video"],
           "note": "Verbatim lock PASS (tts_budget.py); every word heard back; used as generated — no trim in a film (§24L).",
           "ingredients": [{"label": "Susan's voice master", "role": "clone source", "kind": "voice", "ref": f"{B}__VOICE-N"}],
           "videoVersions": [{"v": 1, "asset": a, "type": "video/mp4", "model": "eleven_v4", "connector": "ElevenLabs", "at": now, "note": ""}]}
    json.dump(doc, open(out / f"gen_VO-T1-{k}.json", "w"), ensure_ascii=False); writes.append(("generations", f"{B}__VO-T1-{k}", f"gen_VO-T1-{k}.json"))
voices = [{"id": "N", "name": "Susan (narrator)", "needed": True, "status": "cloned", "voice": "American woman, 49, low, warm, slightly smoky, Midwest", "note": "master To check · narrator clone 'Mother' Keqdw9ZWsMjWZgsJl2h0"}] + \
         [{"id": k, "name": names[k], "needed": True, "status": "building", "voice": v, "note": "§24I master To check"} for k, v in
          [("C1", "American man, 52, warm baritone loosened by drink"), ("C2", "American woman, 49, warm, low, a little husky"), ("C3", "American woman, 49, bright, easy, honest"),
           ("C5", "American woman, 51, low and quick"), ("C6", "American woman, 50, soft and gentle")]]
json.dump({"voices": voices, "balances": {"Higgsfield": 7390.52}, "balancesAt": now, "updatedAt": now}, open(out / "build_voices.json", "w"), ensure_ascii=False)
json.dump([{"op": "set", "collection": c, "doc_id": d, "file_path": str((out / f).resolve())} for c, d, f in writes], open(out / "batch3.json", "w"))
print(len(writes))
