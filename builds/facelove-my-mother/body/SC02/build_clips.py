"""Scene 2 — THE WALK-OUT (day D1, the hosts' yard at golden hour, straight after the toast). One Seedance 2.5 MULTI-SHOT take via Higgsfield
(omni_reference, 720p, 9:16), ingredients only, no frames (§4, §24K part 5). User go: "CONFIRMED ALL VIDEO. PROCEED" (2026-10-02) — all of SC01 confirmed.
Shared strings come from body/SC01/build_clips.py so the scene keeps SC01's exact look, geography and Susan's seat (@video1 = SC01-T2, the seat
the user named as the reference on SC01's Fixes).
Voice refs hold only the take's own words (L33): Friend A's and Friend B's lines voiced by their own clones (ElevenLabs IVC from their masters,
FaceloveFriendA tUfvpAlFQm6euFy0WBct / FaceloveFriendB 000KR2tcs0eohG8JMMx1), the friends' masters holding none of these words.
Act-map rig for SH03 was F5 walking toward the lens; §24K / the rig table allow F5 only waist-up with the walk not toward the lens, and a take
carries one rig — so the whole take is F2, Susan walking through a locked frame (§27G rule 3)."""
import importlib.util, json
from pathlib import Path
H = Path(__file__).parent; B = H.parents[1]
_s = importlib.util.spec_from_file_location("sc01", B / "body/SC01/build_clips.py"); S1 = importlib.util.module_from_spec(_s); _s.loader.exec_module(S1)
R = S1.R

L006 = "…that was awful of him."
L007 = "…I mean, though. She did kind of stop trying. It's just sad to watch."
VOICE_C5 = ("An American woman of fifty-one, a low, quick, warm voice, plain General American, a little hushed, speaking close to a friend; "
            "genuinely sorry, never theatrical.")
VOICE_C6 = ("An American woman of fifty, a soft, gentle, light voice, careful and kind-sounding, plain General American, never sharp; "
            "the kindness is what makes it cut.")
FA_ID = "Friend A, a woman of fifty-one in a mustard linen wrap dress"
FB_ID = "Friend B, a woman of fifty in a pale pink silk shirt and white wide-leg trousers"
START = R["SC02-SH01"]["start_pos"]
END = R["SC02-SH04"]["end_pos"]

PROMPT = " ".join([
    S1.manifest([("@image1", S1.SHEET("Susan", S1.SUSAN_D1)), ("@image2", S1.SHEET("Friend A", S1.FA_D1)), ("@image3", S1.SHEET("Friend B", S1.FB_D1)),
                 ("@image4", "is Greg: only his navy blazer sleeve and his hand round his drink are ever seen in this take."),
                 ("@image5", S1.YARD), ("@image6", S1.CAKE), ("@video1", S1.SEATV),
                 ("@audio1", S1.VOICE("Friend A")), ("@audio2", S1.VOICE("Friend B"))]),
    S1.SERIES, S1.LOOK, S1.INHERIT, S1.GEO, S1.SEAT,
    "A small drinks table with bottles and glasses stands on the lawn at the garden end of the long table, on Susan's side; the back deck with its three wooden steps "
    "and the glass-paned back door is at the house end of the yard.",
    S1.NOSPK,
    "THE EXCHANGE, word for word and in this order: " + L006 + " " + L007 + " — Friend A says the first line; Friend B, unseen in the last part, says the rest. "
    "Susan says nothing. Nobody else speaks.",
    "One scene covered in 4 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + START + ". "
    "The action carries straight across every cut: each shot picks up the movement exactly where the last one left it, and everyone is where the last shot left them. "
    f"SHOT 1, [0s-3s]: MEDIUM, three-quarter at eye level from Paula's side of the table, Susan, {S1.SUSAN_ID}, in {S1.SUSAN_D1}, in her seat exactly as @video1 shows it, "
    "Greg's navy sleeve and his hand round his drink at the right edge of frame: she stands, folds her napkin once and sets it on the table beside the cake. "
    f"SHOT 2, [3s-6s]: MEDIUM WIDE at eye level, three-quarter, a few metres back from the drinks table, both women seen from the knees up with the drinks table and the party around them: {FA_ID} and {FB_ID} stand side by side about half a metre apart, glasses in hand, turned a little toward each other; Friend A leans in only slightly to keep her voice down; their heads stay well apart at a normal talking distance and never touch; "
    f"Friend A says it low, just to Friend B: {L006} Behind them, soft and out of focus, Susan walks past toward the house, one step a second. "
    "SHOT 3, [6s-11s]: MEDIUM, waist-up, at eye level beside the long table: Susan walks into the locked frame from the right and across it toward the house end of the yard, "
    "one step a second, four steps; Friend B's voice, unseen, carries over her; on 'stop trying' her eyes flick once to the side and she keeps walking, never breaking stride. "
    "SHOT 4, [11s-15s]: WIDE from low on the lawn behind her: Susan climbs the three wooden deck steps, opens the glass-paned back door, goes in and closes it behind her. "
    "Each cut lands on a completed action. Nobody looks into the lens. Last frame: " + END + ".",
    S1.F2, S1.PHYS,
    "LISTENING: Friend B takes Friend A's line with a small wince, eyes down at her glass, and answers it without leaning closer; Susan hears it and does not turn her head; nothing on any face arrives before the word that causes it.",
    S1.state("SUSAN", "the dusty-blue blouse, composed, her face very still after the toast", "standing and walking away"),
    "FOCUS: SHOT 1 her hands and the napkin sharp; SHOT 2 the friends' eyes sharp, Susan soft behind; SHOT 3 Susan's eyes sharp; SHOT 4 deep. The blur is optical: soft and round, never smeared.",
    S1.dialogue("Friend A", L006, VOICE_C5, "Greg has just humiliated his wife in front of everyone. Head close to Friend B, low.",
                "says what everyone is thinking. Opens on a breath; turns on 'awful'; exits flat. Stress on 'awful'.",
                "hushed, quick, low, matching the face in this shot.", "she is embarrassed for Susan, which leaks only through how quietly she says it."),
    S1.dialogue("Friend B (unseen in the last part)", L007, VOICE_C6, "she half agrees with him, and is ashamed to. Close to Friend A, low.",
                "says the unkind thing kindly. Opens hesitant on 'I mean, though'; turns on 'stop trying'; exits on 'sad to watch', soft. Stress on 'stop'.",
                "soft, gentle, hushed, continuing at Friend A's level.", "she believes it, which leaks only through how gentle it sounds."),
    S1.AUD,
    S1.negs(S1.NEG_EQUIP, S1.NEG_MORPH, S1.NEG_CAKE, "no Greg's face in frame, no Susan speaking, no Susan crying, no tears, no running, no one following Susan, no foreheads touching, no heads pressed together, no faces close to the lens, no tight close-up on the friends",
            S1.NEG_SEAT, S1.NEG_FILM, S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND)])

FILES = ["cast/N-SUSAN_v1.png", "cast/C5-FRIEND-A_v1.png", "cast/C6-FRIEND-B_v1.png", "cast/C1-GREG_v1.png", "plates/L-YARD_v1.png",
         "body/SC01/ingredients/CAKE-CARD_v1.png", "body/SC01/SC01-T2_v1.mp4"]
JOBS = [S1.JOBS[k] for k in ("N", "C5", "C6", "C1", "L-YARD", "CAKE")]
AUDIO_MEDIA = {"voice/C5_ref_L006.mp3": "10388ea9-b8d1-4dd1-a246-67305f8bae73", "voice/C6_ref_L007.mp3": "cb3fffd0-e4f7-4a31-9d0e-4c7dd3a802da"}

if __name__ == "__main__":
    call = {"beat": "SC02-T1", "build": "facelove-my-mother", "connector": "seedance", "model": "seedance_2_5", "mode": 4, "kind": "multi", "prompt": PROMPT,
            "take": "SC02-T1", "covers": ["SC02-SH01", "SC02-SH02", "SC02-SH03", "SC02-SH04"], "start_pos": START, "end_pos": END, "duration": 15,
            "resolution": "720p", "aspect_ratio": "9:16", "start_image": None, "ingredients_approved": True,
            "files": FILES + list(AUDIO_MEDIA), "audios": list(AUDIO_MEDIA), "generate_audio": True,
            "dialogue": L006 + " " + L007, "script_line": L006 + " " + L007, "pace": "unhurried", "subject_motion": "travels", "prefer_multi_shots": "false",
            "generation": 2, "user_go": "board Fix (user, 2026-10-02): REVISE THE SCENE OF FREIND A AND FRIEND B DONT MAKE  THE FACE TOO CLOSE",
            "fault": "REVISE THE SCENE OF FREIND A AND FRIEND B DONT MAKE  THE FACE TOO CLOSE",
            "fix_note": "prompt fault: SHOT 2 asked for a MEDIUM in profile with the friends standing 'with their heads close together', so the model pressed their foreheads almost together in a tight two-shot → SHOT 2 now a MEDIUM WIDE from a few metres back, knees up, the two side by side half a metre apart, heads well apart at a normal talking distance, Friend A only leaning in slightly; negatives for touching heads and tight close-ups",
            "risks": [{"risk": "Susan's seat drifts from SC01", "prevented_by": "@video1 = SC01-T2, SEAT clause, NEG_SEAT"},
                      {"risk": "the voices swap or Susan speaks", "prevented_by": "Audio1 Friend A's own line, Audio2 Friend B's own line; THE EXCHANGE names who says what; 'no Susan speaking'"},
                      {"risk": "the camera follows her walk", "prevented_by": "F2 locked for the whole take, she walks through the frame"},
                      {"risk": "the friends' faces pressed close together / too close to the lens (v1 fault)", "prevented_by": "SHOT 2 MEDIUM WIDE, half a metre apart, heads never touch, negatives"}],
            "scene": 2, "title": "Scene 2 · T1 — the walk-out: napkin down, the whisper, the deck door (SH01–SH04)",
            "taste": ["HT17", "HT18", "HT22", "HT23", "HT25"], "jobs": JOBS, "video_jobs": [S1.T2_JOB],
            "audio_media": list(AUDIO_MEDIA.values())}
    (H / "SC02-T1.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
    (H / "SC02-T1.prompt.txt").write_text(PROMPT)
    print("SC02-T1", len(PROMPT), "chars")
