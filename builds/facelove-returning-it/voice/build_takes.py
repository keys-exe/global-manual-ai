#!/usr/bin/env python3
"""§22U step 2 — Kling voice-source takes G1, G2 (kling3_0 via Higgsfield, rung 3; pro 1080p, 10 s, sound on), §36 JSON.
Start frame: N-VOICE-IMG (finished face). G1 = the script's opening line, G2 = the next line that fits 10 s (≤ 20 words)."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
VOICE_N = ("A Latina American woman of forty-six from San Antonio, Texas: a warm mid-low voice with a little natural rasp, quick and conversational, "
           "a light Texan-Latina lilt on the vowels — never a caricature, never an accent put on. Talks like she's venting to a close friend on a video call: "
           "animated, a little exasperated, a laugh not far under it. Statements fall at the end; stress comes by slowing a word, never by shouting.")
AUD = ("Not a narrator, not an advert. Audio must sound like a phone microphone recording in a bedroom, not a studio voice track: audible breath before the first word and between phrases, "
       "mouth and lip noise, sibilance present and un-de-essed, plosives on hard consonants, level drifting slightly across the take. No studio compression, no noise gate, no reverb plate, no post EQ. Her bedroom, soft carpet, a quiet room.")
NEGS = ("no morphing, no warping, no melting, no shape shifting, no merging, no splitting, no parts detaching, no proportions changing, no duplicate objects, no background bending, "
        "no texture swimming, no smearing, no flickering geometry, no static camera, no camera coming to rest, no music, no second voice")
TAKES = {
 "G1": dict(line="I am so mad, and this is exactly why you read the reviews before you buy another foundation.",
            mood="cross and fed-up; stress on 'so mad' and 'reviews'", nod="small head shake on 'so mad'; one hand lifts off the vanity edge and drops back on 'reviews'", close="reviews"),
 "G2": dict(line="And it is not because it goes on pure white and then turns into my exact shade",
            mood="deadpan, building — the joke is that it's a compliment; stress on 'pure white' and 'exact'", nod="small tilt of the head on 'exact'; hands stay on the vanity edge", close="white"),
}
for g, t in TAKES.items():
    j = {"shot": f"Voice take {g}.", "dialogue": t["line"], "delivery": VOICE_N + " " + t["mood"] + ". " + AUD,
         "subject": "As in the start frame.",
         "camera": {"movement": "Propped on the vanity, not held, not tripod. Small settle at entry, then near-stillness with a slow unresolved drift. Slightly off-level and never corrected.",
                    "framing": "PROPPED as in the start frame."},
         "motion": ("Take one small quick inhale and begin speaking as it finishes — the first word lands within the first half second of the clip, no settle, no glance, no held beat before speech. "
                    + t["nod"] + "; eyes on lens. Jaw-carried speech, visibly dropping on open vowels, lips shaping over it. Lips fully close on the exact word '" + t["close"] + "'. "
                    "After the final word the lips close and the jaw settles. Everything in frame keeps the exact form, proportion and count it has in the start frame, first frame to last — "
                    "nothing melts, merges, splits, grows or becomes something else. Subject fully in frame throughout."),
         "lighting": "Capture characteristics exactly as in the start frame — same tone-mapping, same noise, same colour temperature. No grading change across the clip.",
         "style": "As in the start frame.", "negatives": NEGS}
    prompt = json.dumps(j, ensure_ascii=False, separators=(",", ":"))
    call = {"beat": f"N-VOICE-{g}", "connector": "kling", "mode": 1, "kind": "dialogue", "duration": 10, "resolution": "1080p", "aspect_ratio": "9:16",
            "start_image": "N-VOICE-IMG v1 (Higgsfield job f93cb289)", "start_approved": False, "pinned": False, "end_image": None, "end_approved": False,
            "dialogue": t["line"], "script_line": t["line"], "pace": "brisk", "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 1,
            "risks": [{"risk": "hands distort when lifted at the vanity", "prevented_by": "hands stay on or return to the vanity edge; a head movement carries the stress"},
                      {"risk": "late first word / dead air eats the 10s budget", "prevented_by": "first word lands within the first half second of the clip, no settle"},
                      {"risk": "studio-clean or second voice / music in the take (bad clone source)", "prevented_by": "phone microphone room audio clause + negatives no music, no second voice"}],
            "prompt": prompt}
    (HERE / f"N_{g}.prompt.txt").write_text(prompt); json.dump(call, open(HERE / f"N_{g}.call.json", "w"), indent=1, ensure_ascii=False)
    print(g, len(prompt), len(t["line"].split()), "words")
