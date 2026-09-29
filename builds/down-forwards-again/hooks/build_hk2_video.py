#!/usr/bin/env python3
"""HK2-02a video — the user, 2026-09-29: "hk2 02a should not need an end frame remove it" → NOT pinned (ADJUST over §27G rule 5):
Kling 3.0 Omni I2V from the confirmed start frame (v3) alone; motion = the Product Sheet SEAT_LOCK slide, compressed to the ≤2,500 budget (§37)."""
import re, json, pathlib
here = pathlib.Path(__file__).parent; ROOT = here.parents[2]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i): return re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
motion = ("Both hands, flat on the two sides of the matte shell, slide the closed strap UP the front of her left shin in one unhurried movement over about "
          "two seconds, the strap travelling as one piece, and seat it on the tendon just below the kneecap: the notch cups the kneecap's lower border, "
          "the peaks stop at the base of its sides, it never climbs the kneecap. Her fingers begin to lift away, the movement unfinished at the cut. "
          "The band stays closed and is never pulled or adjusted; the strap keeps its exact shape, size and wordmark in every frame. " + S("HOLD-C"))
j = {"shot": "hk2_02a", "subject": S("INHERIT-SUBJ"), "camera": {"movement": S("RIG-R1C"), "framing": "CLOSE, as in the start frame: her left leg and the strap, her face soft at the top."},
     "motion": motion, "lighting": S("INHERIT-CAP"), "style": "As in the start frame.",
     "negatives": ", ".join([S("NEG-WARP-C"), "no flickering light, no exposure pumping",
       "no band being opened, no band being pulled tight, no fingers on the chrome slides, no strap changing shape or size, no second strap, "
       "no strap travelling past or onto the kneecap, no strap coming to rest low on the shin, no strap moving downward, no hands passing through the strap, "
       "no bending, no curling, no folding, no melting, no flipping of the product, no speaking, no music, no text appearing"])}
p = json.dumps(j, ensure_ascii=False, separators=(",", ":"))
c = {"beat": "HK2-02a", "connector": "kling", "mode": 1, "kind": "broll", "prompt": p, "duration": 4, "resolution": "1080p", "aspect_ratio": "9:16",
     "start_image": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_101530_dd2add6c-2681-4176-8877-4d9cbd5eb04c.png",
     "start_approved": True, "pinned": False, "end_image": None, "end_approved": False,
     "script_line": "It takes ten seconds and it is not a prescription.", "pace": "unhurried", "subject_motion": "in_place", "prefer_multi_shots": "false",
     "generation": 1, "rack": None, "audio": False, "route": "kie", "kie_model": "kling-3.0-omni/image-to-video",
     "adjust": "user 2026-09-29: no end frame on HK2-02a (not pinned)",
     "risks": [{"risk": "the strap climbs onto the kneecap or stops low", "prevented_by": "seat point named (notch cups the lower border), no travelling past/onto the kneecap, no resting low"},
               {"risk": "the strap deforms or the band opens while sliding", "prevented_by": "travels as one piece, band closed; product negatives + NEG-WARP-C"},
               {"risk": "hands fuse with or pass through the strap", "prevented_by": "hands flat on the shell's sides; no hands passing through the strap"}]}
(here / "video" / "HK2-02a.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(len(p))
