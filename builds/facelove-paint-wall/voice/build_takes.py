#!/usr/bin/env python3
"""§22U step 2 — Kling voice-source takes G1, G2 (kling3_0 via Higgsfield, rung 3; pro 1080p, 10 s, sound on), §36 JSON.
Start frame: N-VOICE-SHELF-B (bare face, at the shelves, phone on a tripod). G1 = the script's opening line, G2 = the next line that fits 10 s (≤ 20 words)."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
VOICE_N = ("An American woman of fifty-seven: a warm low-middle voice, clear and unhurried, bold and knowing with a dry streak of humour — "
           "a woman who has finally worked something out and is about to show you. General American, no regional accent put on. "
           "Statements fall at the end; stress comes by slowing a word, never by shouting.")
AUD = ("Not a narrator, not an advert. Audio must sound like a phone microphone on a tripod two metres away in a bright, quiet dressing room, not a studio voice track: "
       "audible breath before the first word and between phrases, mouth and lip noise, sibilance present and un-de-essed, plosives on hard consonants, a little room in the sound off the plaster walls. "
       "No studio compression, no noise gate, no reverb plate, no post EQ.")
NEGS = ("no morphing, no warping, no melting, no shape shifting, no merging, no splitting, no parts detaching, no proportions changing, no duplicate objects, no background bending, "
        "no texture swimming, no smearing, no flickering geometry, no camera coming to rest, no music, no second voice")
TAKES = {
 "G1": dict(line="You could throw out every expensive foundation on your shelf right now, and you would not lose a thing.",
            mood="bold and knowing, a little dry; stress on 'every' and 'not lose a thing'", nod="a small sideways tilt of the head toward the shelves on 'shelf'; arms stay relaxed at her sides", close="thing"),
 "G2": dict(line="I am fifty seven. And for years I felt like my own face had quietly turned on me.",
            mood="honest and a little tired, plain and unhurried; stress on 'fifty seven' and 'quietly'", nod="a slow small nod on 'fifty seven', eyes stay on the lens; arms stay at her sides", close="me"),
}
for g, t in TAKES.items():
    j = {"shot": f"Voice take {g}.", "dialogue": t["line"], "delivery": VOICE_N + " " + t["mood"] + ". " + AUD,
         "subject": "As in the start frame.",
         "camera": {"movement": "On a tripod at chest height, locked; only the faint micro-shake of a phone on a tripod, no travel, no zoom.",
                    "framing": "TRIPOD, waist-up, as in the start frame."},
         "motion": ("Take one small quick inhale and begin speaking as it finishes — the first word lands within the first half second of the clip, no settle, no glance, no held beat before speech. "
                    + t["nod"] + "; eyes on lens. Jaw-carried speech, visibly dropping on open vowels, lips shaping over it. Lips fully close on the exact word '" + t["close"] + "'. "
                    "After the final word the lips close and the jaw settles. Everything in frame keeps the exact form, proportion and count it has in the start frame, first frame to last — "
                    "nothing melts, merges, splits, grows or becomes something else. Subject fully in frame throughout."),
         "lighting": "Capture characteristics exactly as in the start frame — same tone-mapping, same noise, same colour temperature. No grading change across the clip.",
         "style": "As in the start frame.", "negatives": NEGS}
    prompt = json.dumps(j, ensure_ascii=False, separators=(",", ":"))
    call = {"beat": f"N-VOICE-{g}", "connector": "kling", "mode": 1, "kind": "dialogue", "duration": 10, "resolution": "1080p", "aspect_ratio": "9:16",
            "start_image": "N-VOICE-SHELF-B v1 (Higgsfield job e5dbc0bc)", "start_approved": False, "pinned": False, "end_image": None, "end_approved": False,
            "dialogue": t["line"], "script_line": t["line"], "pace": "brisk", "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 1,
            "risks": [{"risk": "hands distort when they come up into frame", "prevented_by": "arms stay relaxed at her sides, hands out of frame; a head movement carries the stress"},
                      {"risk": "late first word / dead air eats the 10s budget", "prevented_by": "first word lands within the first half second of the clip, no settle"},
                      {"risk": "studio-clean or second voice / music in the take (bad clone source)", "prevented_by": "phone microphone room audio clause + negatives no music, no second voice"}],
            "prompt": prompt}
    (HERE / f"N_{g}.prompt.txt").write_text(prompt); json.dump(call, open(HERE / f"N_{g}.call.json", "w"), indent=1, ensure_ascii=False)
    print(g, len(prompt), len(t["line"].split()), "words")
