"""Prepare the SC01 Seedance requests (Higgsfield) and the board's 'generating' updates."""
import json, time
AUDIO_MEDIA = {"voice/C1_ref_L001.mp3": "3378295a-544a-4d72-bbb9-e1936cd0b23b",
               "voice/C1_ref_L005.mp3": "1ca1f2fe-97ff-4c3b-a923-7ae34e552f09",
               "voice/N_ref_L004.mp3": "71387817-a870-4421-af9d-40b02f685bd2"}
CARD = {"cast/C1-GREG_v1.png": ("C1 Greg", "character", "facelove-my-mother__C1-GREG"),
        "cast/N-SUSAN_v1.png": ("N Susan", "character", "facelove-my-mother__N-SUSAN"),
        "cast/C2-PAULA_v1.png": ("C2 Paula", "character", "facelove-my-mother__C2-PAULA"),
        "cast/C5-FRIEND-A_v1.png": ("C5 Friend A", "character", "facelove-my-mother__C5-FRIEND-A"),
        "cast/C6-FRIEND-B_v1.png": ("C6 Friend B", "character", "facelove-my-mother__C6-FRIEND-B"),
        "plates/L-YARD_v1.png": ("L-YARD", "location", "facelove-my-mother__L-YARD"),
        "body/SC01/ingredients/CAKE-CARD_v1.png": ("CAKE-CARD", "info", "facelove-my-mother__CAKE-CARD")}
VOICE = {"voice/C1_ref_L001.mp3": ("Greg · L001", "facelove-my-mother__VOICE-C1"),
         "voice/C1_ref_L005.mp3": ("Greg · L005", "facelove-my-mother__VOICE-C1"),
         "voice/N_ref_L004.mp3": ("Susan · L004", "facelove-my-mother__VOICE-N")}
reqs, now = [], int(time.time() * 1000)
for t in range(1, 5):
    c = json.load(open(f"SC01-T{t}.call.json"))
    medias = [{"role": "image_references", "value": j} for j in c["jobs"]] + \
             [{"role": "audio_references", "value": AUDIO_MEDIA[a]} for a in c["audios"]]
    p = {"model": "seedance_2_5", "prompt": open(f"SC01-T{t}.prompt.txt").read(), "mode": "omni_reference",
         "resolution": "720p", "aspect_ratio": "9:16", "duration": c["duration"], "medias": medias,
         "generate_audio": c["generate_audio"], "count": 1}
    reqs.append({"index": t, "params": p})
    ing = [{"label": CARD[f][0], "role": f"@image{i} · {CARD[f][1]}", "kind": CARD[f][1], "ref": CARD[f][2]}
           for i, f in enumerate(c["files"], 1)]
    ing += [{"label": VOICE[a][0], "role": f"@audio{i} · voice", "kind": "voice", "ref": VOICE[a][1]}
            for i, a in enumerate(c["audios"], 1)]
    json.dump({"status": "generating", "title": c["title"], "covers": c["covers"], "duration": c["duration"],
               "line": c["script_line"] or "(no dialogue — silent clip)", "prompt": p["prompt"],
               "model": "seedance_2_5 · omni_reference · 720p · 9:16", "videoConnector": "Higgsfield",
               "ingredients": ing, "taste": c["taste"], "updatedAt": now},
              open(f"/tmp/claude-0/-home-user-global-manual-ai/9d5b0f1b-2592-580c-a9ad-a857a491cd61/scratchpad/sc01/gen_T{t}.json", "w"))
json.dump(reqs, open("/tmp/claude-0/-home-user-global-manual-ai/9d5b0f1b-2592-580c-a9ad-a857a491cd61/scratchpad/sc01/reqs.json", "w"))
print("ok", [len(r["params"]["medias"]) for r in reqs])
