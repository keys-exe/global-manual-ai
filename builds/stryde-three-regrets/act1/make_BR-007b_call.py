"""BR-007b clip call (§35 JSON on Kie kling-3.0-omni), strings shared with act6/make_act6_calls.py."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
ns = {"__file__": D + "../act6/make_act6_calls.py"}
exec(open(D + "../act6/make_act6_calls.py").read().split("HPC =")[0], ns)
R1C, HOLD_C, HOLD_HC, PHYS, CAP, NEGW = [ns[k] for k in ("R1C", "HOLD_C", "HOLD_HC", "PHYS", "CAP", "NEGW")]
URL = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_121420_9cc099ab-2ae0-425c-87cf-e3c55402cca6.png"
motion = ("CONTINUING: the neighbour's hand holds out the packet, Gail's fingers just closing on it. "
          "COMPLETING: one hand-over, about two seconds — Gail takes the packet, the neighbour's hand lets go and drops out of frame, Gail draws it to her chest with a small polite nod. "
          "UNRESOLVED: she holds it to her chest, doubtful half-smile, eyes on the neighbour.")
prompt = json.dumps({
    "shot": "act1_neighbour_handover",
    "subject": "THE SAME WOMAN, DOORWAY AND NEIGHBOUR as in the start frame; unchanged in every respect.",
    "camera": {"movement": R1C, "framing": "MEDIUM as in the start frame: over the neighbour's shoulder, three-quarter on Gail. FOCUS: Gail's nearest eye and the packet are sharp."},
    "motion": motion + " " + HOLD_C + " " + HOLD_HC + " " + PHYS, "lighting": CAP,
    "style": "Unremarkable phone clip, grey flat overcast late-morning daylight from the street on the left, no grade.",
    "negatives": NEGW + ", no neighbour's face, no neighbour turning round, no door closing, no opening the packet, no printing or brand appearing on the packet, no talking, no glancing at the lens, no music"},
    ensure_ascii=False, separators=(",", ":"))
call = {"beat": "BR-007b", "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt, "duration": 4, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": URL, "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 1,
        "risks": [{"risk": "the neighbour turns and her face is invented", "prevented_by": "back to the lens throughout; no neighbour's face, no neighbour turning round"},
                  {"risk": "the packet gains printing or morphs into our strap", "prevented_by": "HOLD-C; no printing or brand appearing on the packet, no opening the packet"},
                  {"risk": "hands fuse at the hand-over", "prevented_by": "HOLD-HC; the neighbour lets go and her hand drops out of frame"}]}
json.dump(call, open(D + "BR-007b.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-007b.kie_prompt.txt", "w").write(prompt)
print("BR-007b", len(prompt))
