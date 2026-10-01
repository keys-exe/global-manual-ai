#!/usr/bin/env python3
"""§22X — video preflight: lint a video call before any credit is spent.

Usage:
  preflight.py CALL.json [--json]

CALL.json describes one paid video call exactly as it will be sent:
  {
    "beat": "BF-SC02-SH03",
    "connector": "seedance" | "kling",
    "mode": 1-5,                       # §18A mode lock
    "kind": "dialogue" | "listener" | "insert" | "broll" | "multi" | "voice_master",
                                       # voice_master = a §24I part 7 neutral film voice master (Seedance, 10s, the
                                       # face-only sheet crop as the one ingredient, no audio in): the film-shot strings
                                       # (rig, SERIES-LOOK, drama, state, business) do not apply — the §24I recipe does
    "prompt": "<the full prompt text, or a Kling §35/§36 JSON string>",
    "duration": 8,
    "resolution": "720p", "aspect_ratio": "9:16",
    "start_image": "<approved url or path>",
    "start_approved": true,            # Manual: the user's Confirm; Automatic: §22V USE + scene contact sheet
    "pinned": false, "end_image": null, "end_approved": false,
    "files": ["..."],                  # Seedance ingredients (images + videos + audios), each named in the manifest
    "audios": ["..."],                 # voice masters (dialogue) — voice only, never a music track (§24M)
    "generate_audio": true,            # Seedance: false on every clip with no dialogue — no BGM (§24M, V7.73.3)
    "dialogue": "the spoken words, verbatim from the script",
    "script_line": "the same line as script_lines.py extracted it",
    "pace": "unhurried" | "brisk",
    "subject_motion": "still" | "in_place" | "travels",
    "prefer_multi_shots": "false",
    "generation": 1,                   # 1 = first try, 2 = the one fix; 3+ only with user_go (§22X)
    "user_go": null | "the user's words giving the go for a 3rd+ generation, and the date",
    "fix_note": "diagnosed fault → the change made (required on generation 2)",
    "fix_notes_all": ["every Fix note written on this shot so far, one per earlier generation (required on generation 3+, §22X L18)"],
    "rack": null | {"from": "...", "to": "...", "cue": "..."},   # §30J focus change inside the clip
    "risks": [{"risk": "...", "prevented_by": "..."}]   # top three failure modes and the clause that prevents each
  }

Beat images (§6A, V7.70.0; first-render rules V7.74.0) — a B-roll or hook start/end frame — are linted too, with "kind": "image":
  {
    "beat": "B1-02", "kind": "image", "mode": 1,
    "prompt": "<the image prompt exactly as it will be sent>",
    "script_line": "the spoken line this picture shows, verbatim",
    "face": false,                     # a face shows in the frame
    "room": true,                      # the location shows (plate attached)
    "product": false,                  # the product shows (product photo attached first)
    "body": true,                      # a person or body part shows
    "refs": [{"label": "...", "kind": "product|character|location|frame|info"}],   # in attach order — each named in the prompt as "Image n" (§6A Part 2 rule 1)
    "match": null | "plate" | "frame",   # the shot must match a plate / a confirmed earlier beat exactly → an image edit of it (§6A Part 2 rule 3, V7.74.0)
    "edit_of": null | "<asset id or file of the plate / frame being edited>",   # required when match is set; the prompt opens as an edit ("Keep this photo exactly…")
    "taste": ["HT03", "FP02"],         # House Taste / product fix-pattern rules applied (§34A)
    "anatomy": false,                  # an anatomy / mechanism beat (Nano Banana)
    "anat_style": null | "S1".."S7",   # anatomy beats: the act-map row's style (§12A-1, V7.81.0); S5 (physical model) routes as realistic
    "pair": ["gpt_image_2_5", "gpt_image_2_5"]   # the A/B pair's models (§5): realistic = two Sunburst; anatomy / Modes 2, 3, 5 = two NB Pro
    "alt_reason": null | "why nano_banana_2 runs instead of Pro (the alternative, V7.72.1)"
  }

Beat videos (§35A, V7.71.0) — a Kling B-roll or hook clip in Modes 1–3 — add:
    "script_line": "the spoken line", "motion_plan": "the 'Video will show' line the user confirmed on the image card",
    "motion_confirmed": true,          # Manual: the user's pick of the image with that line; Automatic: the §22V USE
    "risk_class": null | "stairs" | "travel" | "hand_product" | "product_angle",
    "pin_waived": null | "the user's words, if a risky shot runs unpinned",
    "pilot": null | "first" | "confirmed"   # risky class: the build's first clip of that class, or after it was confirmed

Every check is PASS or FAIL. Any FAIL → exit 1 and the call is not sent.
"""
import argparse, json, re, sys
from pathlib import Path

# A signature sentence from each normative string (Appendix A), so a pasted string can be verified present.
SIG = {
    "INHERIT-FILM": "Nothing about the look changes across the clip",
    "INHERIT-ANIM": "Every character stays exactly on model",
    "STATE-CARRY": "None of it resets",
    "DRAMA-DELIVERY": "UNDER THE LINE",
    "VOICE NOW": "VOICE NOW",
    "PLAYING": "PLAYING:",
    "LISTEN-LINE": "The reaction arrives a beat after the words that cause it",
    "BUSINESS-LINE": "the hands never stop to gesture",
    "AUD-FILM": "clean, close production dialogue sound",
    "AUD-ANIM": "clean studio voice performance recorded for animation",
    "NEG-SCENECUT": "no light direction changing within the scene",
    "NEG-DRAMA": "no theatrical acting",
    "NEG-FILM": "no phone camera look",
    "NEG-ANIMFILM": "no concept art",
    "MULTI-FILM": "within a single take",
    "NEG-SOUND": "no music, no score, no sound effects",
    "SERIES-LOOK": "The look of a high-end live-action drama series",
}
MIC_WORDS = re.compile(r"\b(?:boom|windshield|dead[- ]cat|(?<!phone-)(?<!phone )microphones?|mics?)\b", re.I)
RIGS = {  # rig signature → F-rig (F6–F10: the Seedance move library, §24N)
    "F1": "steady push toward the subject", "F2": "Camera on a tripod", "F3": "Camera on an operator's shoulder",
    "F4": "Camera on a slider", "F5": "Camera on a stabiliser",
    "F6": "Camera pulling back on a dolly", "F7": "Camera arcing", "F8": "Camera on a crane",
    "F9": "Camera tracking alongside", "F10": "Camera performing a slow dolly zoom",
}
TRAVEL_RIGS = {"F1", "F4", "F5", "F6", "F7", "F8", "F9", "F10"}   # the camera moves through space
NOT_IN_PLACE = {"F1", "F4", "F5", "F6", "F7", "F9", "F10"}         # subject sits, stands, turns, reaches (§24K/§24N)
NOT_TRAVELS = {"F1", "F3", "F4", "F6", "F7", "F8", "F10"}          # subject walks: only F2, F5, F9
MUSIC = re.compile(r"\b(?:music(?:al)?|score|soundtrack|bgm|background music|song|melody|instrumental|orchestra(?:l)?|underscore|theme tune)\b", re.I)
NEG_CLAUSE = re.compile(r"\b(?:no|never|without)\b[^,.;:\n]*", re.I)   # negative clauses may name music ("no music, no score")
MUSIC_FILE = re.compile(r"(?:music|bgm|score|soundtrack|MUS-SC)", re.I)
SEEDANCE_ONLY = {"F6", "F7", "F8", "F9", "F10"}
STREAMERS = re.compile(r"\b(netflix|hbo|max original|prime video|amazon original|apple tv|disney\+?|hulu|paramount\+?|peacock)\b", re.I)
WALK = re.compile(r"\b(walks?|walking|steps? (?:toward|into|across|down|up)|crosses|climbs?|stairs|runs?|running)\b", re.I)
PLACEHOLDER = re.compile(r"\[(?:[A-Z][A-Z0-9 ,:/'’\-]{2,}|NAME|WHO|WORD|STATE|PACE|SIDE|FOCAL)[^\]]*\]")
BANNED = re.compile(r"\bcinematic\b", re.I)


def words(t):
    return len(re.findall(r"[A-Za-z0-9’']+", t or ""))


def word_budget(d, pace):
    # §28H: 5s → 9 brisk / 8 unhurried; 10s → 20 / 18 (linear through both points)
    return int(2.2 * d - 2) if pace == "brisk" else int(2 * d - 2)


IMG_MAX = 1200          # §6A: a beat image prompt is ≤ 1,200 characters
IMG_NEG_MAX = 5         # §6A: at most five "no …" / "never …" items
NEG_WORD = re.compile(r"\b(?:no|never|without|avoid)\b", re.I)
SIZE_ANCHOR = re.compile(r"\d+(?:\.\d+)?\s*(?:×|x|by)?\s*\d*\s*(?:cm|mm|centimet|millimet)|\bthe size of\b|\bas (?:small|big|large) as\b", re.I)
NANO = {"nano_banana_pro", "nano_banana_2", "nano-banana-pro", "nano-banana-2"}
PRO = {"nano_banana_pro", "nano-banana-pro"}
SUNBURST = {"gpt_image_2_5", "gpt_image_2_5_sunburst", "gpt-image-2-5-sunburst-image-to-image", "gpt-image-2-5-sunburst-text-to-image"}
# §6A Part 2 — right on the first render (V7.74.0)
FRACTION = re.compile(r"\b(?:a |one |two |three |about a |about two |about three |roughly a |at least a |over a |nearly a )?(?:half|third|quarter|fifth|thirds|quarters|fifths|\d{2}\s?(?:%|percent))\s+(?:of\s+)?(?:the\s+)?frame(?:'s)?\b|\bfills?\s+(?:most of\s+)?the\s+frame\b|\bframe[- ]filling\b", re.I)
FIDELITY = re.compile(r"\b(?:copied|reproduced|matched|exactly as|identical to|the same as)\b[^.]{0,80}\bexactly\b|\bexactly\b[^.]{0,40}\b(?:as|in|from)\s+Image\s*\d|\bcopied exactly\b|\bnothing redesigned\b", re.I)
EDIT_OPEN = re.compile(r"^\s*(?:For the line \"[^\"]*\":\s*)?(?:keep|edit|using|take|leave|start from|starting from)\b[^.]{0,120}\b(?:this photo|this picture|this image|this frame|the plate|image\s*1)\b", re.I)
HANDS = re.compile(r"\b(?:hands?|palms?|fingers?|fingertips?|thumbs?|wrists?|arms? (?:at|by|folded|crossed))\b", re.I)
GAZE = re.compile(r"\b(?:both eyes|eyes (?:on|to|toward|down|up|closed|fixed|level)|looking (?:at|down|up|ahead|away|into|toward|straight)|gaze|square to the lens|to the lens|into the lens|at the camera|to camera|face (?:to|turned|toward|square))\b", re.I)
SURFACE = re.compile(r"\b(?:table|desk|counter|worktop|countertop|shelf|shelves|bench|dresser|sideboard|nightstand|floor)\b", re.I)
BARE = re.compile(r"\b(?:bare|empty|clear(?:ed)?|nothing (?:else|on)|only (?:the|one|two|a)|every other surface|no other objects?)\b", re.I)
PLAIN = re.compile(r"\b(?:no|without|free of)\s+(?:readable\s+|visible\s+)?(?:lettering|logos?|text|labels?|writing|branding|print)\b|\bplain(?:,| and| —| -)?\s+(?:un(?:branded|marked|lettered)|no\b)|\bunbranded\b|\bno lettering\b", re.I)
DEVICE = re.compile(r"\b(?:(?:a|an|her|his|their|one|my)\s+(?:i?phone|smartphone|mobile|tripod|camera|ring light|selfie stick|gimbal|laptop|webcam)|the\s+(?:i?phone|smartphone|mobile|tripod|ring light|selfie stick|gimbal|laptop|webcam))\b(?![^.]{0,40}\b(?:photo|shot|frame|lens|register|look|style)\b)", re.I)   # "the camera" is the viewpoint (gaze, edit openings) and is not flagged
BODY_PART = r"(?:legs?|feet|foot|arms?|hands?|heads?|shoulders?|knees?|body|torso|elbows?|hips?|calf|calves|shins?|thighs?|fingers?)"
OUT_OF_FRAME = re.compile(r"(\b\w+\b)\s+(?:is |are |kept |cut |partly |just |half )?(?:out of|outside|off|beyond)\s+(?:the\s+)?(?:frame|shot|picture|screen)\b|\boff[- ]screen\b|\bnot in (?:the )?(?:frame|shot|picture)\b|\bunseen\b", re.I)


def run_image(c):
    res = []

    def check(name, ok, detail=""):
        res.append({"check": name, "result": "PASS" if ok else "FAIL", "detail": detail})

    p = c.get("prompt", "")
    mode = int(c.get("mode", 1))
    norm = lambda t: re.sub(r"[\s“”\"']+", " ", (t or "").strip().lower())
    refs = c.get("refs") or []
    kinds = [str(r.get("kind", "")).lower() for r in refs]

    check("≤ 1,200 characters (§6A)", len(p) <= IMG_MAX, f"{len(p)} chars")
    # L10 (2026-10-01): a Mode 2/3/5 beat prompt carries the mode's render line, or the model returns a photograph of the plate edit
    MODE_LINE = {2: r"3D animated|storybook|pixar", 3: r"claymation|stop-motion|clay", 5: r"3D animated|storybook|pixar"}
    if mode in MODE_LINE:
        check(f"the mode's render line is in the prompt (§12 lock, mode {mode})", bool(re.search(MODE_LINE[mode], p, re.I)), "e.g. 'A final frame from a 3D animated feature film, stylized storybook render'")
    sl = c.get("script_line")
    check("the spoken line is in the prompt (§6A)", bool(sl) and norm(sl) in norm(p), "script_line missing" if not sl else "")
    negs = NEG_WORD.findall(p)
    check(f"≤ {IMG_NEG_MAX} negatives (§6A)", len(negs) <= IMG_NEG_MAX, f"{len(negs)} no/never/without/avoid")
    check("no unfilled slot", not PLACEHOLDER.search(p), (PLACEHOLDER.search(p) or [""])[0])
    check("House Taste read (§34A)", isinstance(c.get("taste"), list), "list the HT / FP rules applied on the call as \"taste\" (may be empty)")
    if c.get("face") is False:
        hit = re.search(r"character sheet|the same (?:woman|man|person|girl|boy)\b", p, re.I)
        check("no face block on a no-face shot (§6A)", not hit and "character" not in kinds, hit.group(0) if hit else ("character ref attached" if "character" in kinds else ""))
    if c.get("room") is False:
        hit = re.search(r"location plate", p, re.I)
        check("no room block on a no-room shot (§6A)", not hit and "location" not in kinds, hit.group(0) if hit else ("location ref attached" if "location" in kinds else ""))
    if c.get("product"):
        check("product photo attached first (§6A)", bool(kinds) and kinds[0] == "product", f"first ref: {kinds[0] if kinds else 'none'}")
        check("true-size anchor for the product (§6A)", bool(SIZE_ANCHOR.search(p)), "e.g. '12 × 5 cm, the size of a matchbox'")
    # §6A Part 2 — right on the first render (V7.74.0)
    if refs:
        missing = [i + 1 for i in range(len(refs)) if not re.search(rf"\b(?:Image|Photo|Picture)\s*{i + 1}\b", p, re.I)]
        check("every reference numbered in the prompt (§6A rule 1)", not missing, f"refs not named as 'Image n': {missing}" if missing else "")
    if c.get("product"):
        check("fidelity clause on the product (§6A rule 1)", bool(FIDELITY.search(p)), "e.g. 'the product in Image 1 copied exactly — same shape, same parts, same markings, nothing redesigned'")
        check("frame fraction beside the size anchor (§6A rule 2)", bool(FRACTION.search(p)), "e.g. 'about a third of the frame wide' — the subject at least a quarter of the frame")
    match = (c.get("match") or "").strip().lower()
    if match:
        check(f"edit_of set for a {match}-matched shot (§6A rule 3)", bool(c.get("edit_of")), "the plate / confirmed frame being edited")
        check("the prompt opens as an edit of that picture (§6A rule 3)", bool(EDIT_OPEN.search(p)), "e.g. 'Keep this photo exactly as it is — the room, the camera, the light. Add …'")
        check("Image 1 is the picture being edited (§6A rule 3)", bool(kinds) and kinds[0] in ("location", "frame"), f"first ref: {kinds[0] if kinds else 'none'}")
    if c.get("body") or c.get("face"):
        check("every visible hand placed (§6A rule 4)", bool(HANDS.search(p)), "say where each hand is and what it does — 'right hand on the rail, left hand loose at her side'")
    if c.get("face"):
        check("gaze stated on a face shot (§6A rule 6)", bool(GAZE.search(p)), "e.g. 'square to the lens, both eyes on it, mouth closed' or 'looking down at the next step'")
    if SURFACE.search(p):
        check("bare surfaces / a closed inventory (§6A rule 4)", bool(BARE.search(p)), f"'{SURFACE.search(p).group(0)}' named — say what is on it and close the list ('every other surface bare')")
    check("plain surfaces — no lettering or logos (§6A rule 5)", bool(PLAIN.search(p)), "e.g. 'clothing, packaging, walls and signs plain — no lettering, logos or labels except the product's own wordmark'")
    dev = DEVICE.search(p)
    check("no device named as an object in the picture (§6A rule 7)", not dev, dev.group(0) if dev else "")
    oof = [m for m in OUT_OF_FRAME.finditer(p) if not re.search(rf"\b{BODY_PART}\b", p[max(0, m.start() - 40):m.end()], re.I)]
    check("nothing named outside the frame but a body part (§6A rule 7)", not oof, oof[0].group(0) if oof else "")
    pair = [str(m).lower() for m in (c.get("pair") or [])]
    anatomy = bool(c.get("anatomy"))
    if anatomy:   # §12A-1 (V7.81.0): a style per anatomy beat, never the glass body by habit
        st = c.get("anat_style")
        check("anatomy style named (S1-S7, §12A-1 V7.81.0)", st in {f"S{n}" for n in range(1, 8)}, f"anat_style {st!r}")
        if st and st != "S1":
            s1 = re.search(r"Premium 3D anatomical visuali[sz]ation|near-black (field|background)|glass-like (body|outer|shell)", p, re.I)
            check(f"no S1 glass-body world on an {st} beat (§12A-1)", not s1, s1.group(0) if s1 else "")
        if st == "S5":
            anatomy = False   # a physical model is a Mode 1 capture: routed like realistic work
    check("A/B pair: two renders (§5)", len(pair) == 2, f"pair {pair}")
    if anatomy or mode in (2, 3, 5):
        why = "anatomy" if anatomy else f"Mode {mode}"
        alt = (c.get("alt_reason") or "").strip()
        ok = all(m in PRO for m in pair) or (alt and all(m in NANO for m in pair))
        check(f"Nano Banana Pro ({why}, §18A V7.72.1)", len(pair) == 2 and ok, f"pair {pair}" + ("" if alt else "; nano_banana_2 only with alt_reason"))
    else:
        check(f"Sunburst on realistic work (Mode {mode}, §18A V7.72.0)", len(pair) == 2 and all(m in SUNBURST for m in pair), f"pair {pair}")
    return res


VID_MAX = 1000          # §35A: a beat video prompt is ≤ 1,000 characters
RISKY = {"stairs", "travel", "hand_product", "product_angle"}
BOILER = [  # the stacked paragraphs §35A retired: each adds motion or contradicts the one action
    "deliberate reframe", "already drifting", "Mass and momentum in all movement", "One small movement",
    "nothing melts, merges, splits", "Focus soft for a moment at entry", "operator notices",
]
FAST = re.compile(r"\b(?:run(?:s|ning)?|sprint\w*|jog\w*|rac(?:es|ing)|fast|quickly|hurr(?:y|ies|ying))\b", re.I)


NOSPEAK = re.compile(r"\b(?:mouths? (?:closed|shut|still)|never (?:speaks?|sings?|talks?)|nobody (?:speaks?|sings?|talks?)|no one (?:speaks?|sings?)|lips (?:still|closed)|does not (?:speak|sing))\b", re.I)


def run_beat_video(c, p, check):
    norm = lambda t: re.sub(r"[\s“”\"']+", " ", (t or "").strip().lower())
    check("≤ 1,000 characters (§35A)", len(p) <= VID_MAX, f"{len(p)} chars")
    sl = c.get("script_line")
    check("the spoken line is in the prompt (§35A)", bool(sl) and norm(sl) in norm(p), "script_line missing" if not sl else "")
    mp = c.get("motion_plan")
    check("the confirmed motion plan is the prompt's action (§35A)", bool(mp) and norm(mp) in norm(p), "motion_plan missing" if not mp else "")
    check("House Taste read (§34A)", isinstance(c.get("taste"), list), "list the HT / FP rules applied on the call as \"taste\" (may be empty)")
    check("motion confirmed at the image (§22X)", c.get("motion_confirmed") is True, "the user's pick of the image with its 'Video will show' line")
    negs = NEG_WORD.findall(p)
    check(f"≤ {IMG_NEG_MAX} negatives (§35A)", len(negs) <= IMG_NEG_MAX, f"{len(negs)} no/never/without/avoid")
    hits = [b for b in BOILER if b.lower() in p.lower()]
    check("no retired boilerplate (§35A)", not hits, "; ".join(hits))
    # L15 (2026-10-01, user: "you should never talk the lyrics/script in broll") — a B-roll is pictures under the voice; the prompt says so.
    check("nobody mouths the line (§35A rule 6, HT25)", bool(NOSPEAK.search(p)), "e.g. 'mouth closed, she never speaks or sings' or 'nobody speaks'")
    rc = (c.get("risk_class") or "").lower() or None
    if rc in RISKY:
        check(f"{rc}: end frame pinned (§27G)", bool(c.get("pinned")) or bool((c.get("pin_waived") or "").strip()), "first-and-last frame, or the user's words in pin_waived")
        check(f"{rc}: pilot clip first (§22X)", c.get("pilot") in ("first", "confirmed"), "the first clip of this class runs alone; the rest wait for its Confirm")
        if rc in ("stairs", "travel"):
            f = FAST.search(p)
            check("fast comes from the edit, never the legs (§27G)", not f, f.group(0) if f else "")


def master_fit(line, pace="unhurried"):
    """§24I (2026-09-30): the shortest Seedance duration (≥ 4s) whose §28H budget holds the line, + 1s of air."""
    d = 4
    while d < 30 and word_budget(d, pace) < words(line):
        d += 1
    return d + 1 if d >= 4 and word_budget(4, pace) < words(line) else max(4, d)


def film_shot(c, p, conn, mode, kind, film, check):
    """§24K/§30J/§24H film-shot checks (sections 5–6), skipped on a §24I voice master."""
    # 5. Motion (§27G / §24K)
    rigs = [r for r, s in RIGS.items() if s in p]
    sm = c.get("subject_motion") or ("travels" if WALK.search(p) else "still")
    series = film and mode == 4 and conn == "seedance"   # ads stay phone style (§24N, V7.69.1)
    if film or series:
        check("one F-rig", len(rigs) == 1, ",".join(rigs) or "none found")
        bad = [r for r in rigs if (sm == "in_place" and r in NOT_IN_PLACE) or (sm == "travels" and r in NOT_TRAVELS)]
        check("camera or subject moves, never both — except F5/F9 on a walk (§24K, §24N)", not bad, f"subject {sm}, rig {','.join(rigs)}")
        if "F5" in rigs:
            check("F5 framed waist-up", "waist" in p.lower())
        if "F9" in rigs:
            check("F9: a walk in profile", sm == "travels" and "profile" in p.lower(), f"subject {sm}")
        if set(rigs) & SEEDANCE_ONLY:
            check("F6–F10 on Seedance only (§24N)", conn == "seedance", conn)
    if series:
        check("SERIES-LOOK (§24N)", SIG["SERIES-LOOK"] in p)
    if not film:
        check("ads stay phone style: no SERIES-LOOK (§24N)", SIG["SERIES-LOOK"] not in p)
        check("ads stay phone style: no F6–F10 (§24N)", not any(sig in p for r, sig in RIGS.items() if r in SEEDANCE_ONLY))
    if kind == "multi":
        check("MULTI-SHOT only when nobody moves", sm == "still", f"subject {sm}")

    # 5b. Focus (§30J)
    rk = c.get("rack")
    if rk:
        check("rack: cue named", bool(rk.get("cue")))
        check("rack: subject still", sm == "still", f"subject {sm}")
        if film:
            check("rack: no travelling rig", not (set(rigs) & TRAVEL_RIGS), ",".join(rigs))
            check("rack: pull written", "focus pulls" in p or "pulls focus" in p)
        else:
            check("rack: Mode 1 tap-to-focus", "tap" in p.lower(), "phones tap to focus — never a clean pull (§30J)")
        check("rack: one focus change", len(re.findall(r"focus (?:pulls|shifts|jumps)", p)) <= 1)
    if film:
        check("FOCUS-LINE", "FOCUS:" in p, "the shot names what is sharp (§30J)")

    # 6. Film strings
    if film:
        check("INHERIT string", SIG["INHERIT-FILM" if mode == 4 else "INHERIT-ANIM"] in p)
        check("NEG-SCENECUT", SIG["NEG-SCENECUT"] in p)
        check("NEG-FILM / NEG-ANIMFILM", SIG["NEG-FILM" if mode == 4 else "NEG-ANIMFILM"] in p)
        check("NEG-SOUND (clips carry dialogue only, §24M)", SIG["NEG-SOUND"] in p)
        if kind in ("dialogue", "listener", "multi", "broll") and kind != "insert":
            check("STATE-CARRY", SIG["STATE-CARRY"] in p)
            check("NEG-DRAMA", SIG["NEG-DRAMA"] in p)
        if kind in ("dialogue", "listener", "multi"):
            check("BUSINESS-LINE", SIG["BUSINESS-LINE"] in p)
        if kind in ("dialogue", "multi"):
            for k in ("DRAMA-DELIVERY", "PLAYING", "VOICE NOW"):
                check(k, SIG[k] in p)
            check("AUD string", SIG["AUD-FILM" if mode == 4 else "AUD-ANIM"] in p)
            check("voice master attached", bool(c.get("audios")), "audios_list empty")
        if kind == "listener":
            check("LISTEN-LINE", SIG["LISTEN-LINE"] in p)
        if kind == "multi":
            check("MULTI-FILM", SIG["MULTI-FILM"] in p)


def run(c):
    if str(c.get("kind", "")).lower() == "image":
        return run_image(c)
    res = []

    def check(name, ok, detail=""):
        res.append({"check": name, "result": "PASS" if ok else "FAIL", "detail": detail})

    p = c.get("prompt", "")
    conn = c.get("connector", "").lower()
    mode = int(c.get("mode", 1))
    kind = c.get("kind", "broll")
    film = mode in (4, 5)
    d = c.get("duration")
    gen = int(c.get("generation", 1))

    # 1. Generation budget
    go = (c.get("user_go") or "").strip()
    check("generation ≤ 2, or the user's go", gen <= 2 or bool(go), f"generation {gen}; a third call on the same shot needs the user (§22X)")
    if gen >= 2:
        fn = c.get("fix_note", "")
        check("gen 2 has a diagnosed fix", "→" in fn or "->" in fn, fn or "missing fix_note")
    if gen >= 3:
        fa = c.get("fix_notes_all") or []
        check("gen 3+ lists every earlier Fix note (fix_notes_all)", isinstance(fa, list) and len(fa) >= gen - 1,
              f"generation {gen} needs {gen - 1} entries in fix_notes_all, one per earlier generation — every note stays in force (§22X, L18); got {len(fa) if isinstance(fa, list) else 'none'}")

    # 2. Frames — on Seedance, ingredients: information, never frames (§4, V7.68.0).
    #    Wan 3.0 in ingredients mode (V7.83.1, user 2026-10-01: "use wan 3.0 prime, the ingredients and not frames") — the same rule.
    if conn in ("seedance", "wan"):
        check("every ingredient approved", c.get("ingredients_approved") is True, "Manual: the user's Confirm on every ingredient card")
        check("no frame in the pack", not c.get("start_image") and not c.get("end_image"), f"a {conn} ingredients call carries no start, end, master or scene frame")
    else:
        check("start image approved", bool(c.get("start_image")) and c.get("start_approved") is True)
    if c.get("pinned"):
        check("pinned: end image approved", bool(c.get("end_image")) and c.get("end_approved") is True)
        check("pinned: runs on Kling first-and-last frame", conn == "kling", "pinned shots never run on Seedance (§24K)")

    # 3. Call parameters
    check("aspect 9:16", c.get("aspect_ratio") == "9:16")
    if conn == "seedance":
        check("Seedance 720p", c.get("resolution") == "720p")
        check("Seedance duration 4–30", isinstance(d, (int, float)) and 4 <= d <= 30, str(d))
        files = c.get("files", [])
        check("ingredients ≤ 30 files", len(files) <= 30, f"{len(files)} files")
        check("ingredient manifest present", "@image1" in p or "ING-MANIFEST" in p or "reference" in p.lower())
    elif conn == "wan":
        check("Wan duration 2–30, stated (never auto)", isinstance(d, (int, float)) and 2 <= d <= 30, str(d))
        imgs = [f for f in c.get("files", []) if not MUSIC_FILE.search(str(f))]
        check("ingredients ≤ 4 images (Appendix D)", len(imgs) <= 4, f"{len(imgs)} images")
        check("ingredient manifest present", "@image1" in p or "Image1" in p or "Image 1" in p or "REF-MANIFEST" in p)
    elif conn == "kling":
        check("Kling duration 3–15", isinstance(d, (int, float)) and 3 <= d <= 15, str(d))
        check("prompt ≤ 2,500 chars", len(p) <= 2500, f"{len(p)} chars")
        check("prefer_multi_shots false", str(c.get("prefer_multi_shots", "")).lower() == "false")
    else:
        check("known connector", False, conn)

    # 3a. No BGM in any Seedance (or Wan) generation — music is laid in the edit (§24M, V7.73.3)
    if conn in ("seedance", "wan"):
        check("NEG-SOUND (no BGM on Seedance, §24M)", SIG["NEG-SOUND"] in p)
        pos = NEG_CLAUSE.sub("", p)
        mus = sorted(set(m.group(0).lower() for m in MUSIC.finditer(pos)))
        check("no music asked for in the prompt (§24M)", not mus, ",".join(mus))
        talk = bool(c.get("dialogue") or c.get("audios"))
        check("no dialogue → generate_audio false (§24M)", talk or c.get("generate_audio") is False,
              "a clip with no dialogue is generated silent (kie.py seedance --no-audio)")
        bad = [a for a in (c.get("audios") or []) if MUSIC_FILE.search(str(a))]
        check("audio references are voice only, never music (§24M)", not bad, ",".join(map(str, bad)))

    # 3b. Beat video prompt (§35A) — Kling B-roll and hook clips in Modes 1–3
    if conn == "kling" and not film and kind in ("broll", "insert"):
        run_beat_video(c, p, check)

    # 4. Prompt hygiene
    ph = PLACEHOLDER.findall(p)
    check("no unfilled [SLOTS]", not ph, ", ".join(sorted(set(ph)))[:300])
    check("no banned word 'cinematic'", not BANNED.search(p))
    if film:  # V7.83.2, LESSONS L13: the video model draws what the prompt names — a boom named "out of frame" lands in frame
        _pos = p.split("NEGATIVES:")[0]
        _mic = MIC_WORDS.findall(_pos)
        check("MIC_PRIME — no microphone, boom or windshield named outside the negatives", not _mic, ",".join(sorted(set(m if isinstance(m, str) else m[0] for m in _mic))))
    check("no streamer, series or studio name (§24N, §10A)", not STREAMERS.search(p), ",".join(sorted(set(m.group(0) for m in STREAMERS.finditer(p)))))

    # 4a. §24I part 7 — a neutral film voice master: its own recipe, not a film shot
    if kind == "voice_master":
        check("voice master on Seedance", conn == "seedance", conn)
        fit = master_fit(c.get("dialogue") or "", c.get("pace", "unhurried"))
        check("voice master duration fits its line — no paid dead space (§24I, 2026-09-30)",
              isinstance(d, (int, float)) and 4 <= d <= fit, f"{d}s for {words(c.get('dialogue') or '')} words; fit ≤ {fit}s")
        imgs = [f for f in c.get("files", []) if not MUSIC_FILE.search(str(f))]
        check("one ingredient: the face-only reference", len(c.get("files", [])) == 1, f"{len(c.get('files', []))} files")
        check("no audio in (it is the master)", not c.get("audios"), ",".join(map(str, c.get("audios") or [])))
        check("dialogue on", c.get("generate_audio") is True and bool(c.get("dialogue")))
        check("neutral delivery (§24I part 7)", "no emotion coloured into the words" in p)
        check("AUD string", SIG["AUD-FILM" if mode == 4 else "AUD-ANIM"] in p)
        check("one speaker only", "one speaker only" in p.lower())
        check("no DRAMA-DELIVERY on a master (who, never how)", SIG["DRAMA-DELIVERY"] not in p)
    else:
        film_shot(c, p, conn, mode, kind, film, check)

    # 7. Dialogue: verbatim and inside the word budget
    dl = c.get("dialogue")
    if dl:
        sl = c.get("script_line")
        norm = lambda t: re.sub(r"\s+", " ", (t or "").strip())
        check("dialogue verbatim from the script", sl is not None and norm(dl) == norm(sl), "script_line missing" if sl is None else "")
        check("dialogue in prompt", norm(dl) in norm(p))
        if isinstance(d, (int, float)):
            b = word_budget(d, c.get("pace", "unhurried"))
            check("§28H word budget", words(dl) <= b, f"{words(dl)} words / {b} for {d}s")

    # 8. Failure-mode review
    risks = c.get("risks") or []
    ok = len(risks) >= 3 and all(r.get("risk") and r.get("prevented_by") for r in risks)
    check("top three risks, each prevented", ok, f"{len(risks)} listed")

    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("call")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    c = json.loads(Path(a.call).read_text())
    res = run(c)
    fails = [r for r in res if r["result"] == "FAIL"]
    if a.json:
        print(json.dumps({"beat": c.get("beat"), "pass": not fails, "checks": res}, indent=1))
    else:
        for r in res:
            print(f"{r['result']:4}  {r['check']}" + (f"  — {r['detail']}" if r["detail"] else ""))
        print(f"\n{c.get('beat', '?')}: {'PREFLIGHT PASS' if not fails else f'PREFLIGHT FAIL ({len(fails)}) — not sent'}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
