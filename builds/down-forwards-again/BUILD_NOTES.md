# Build notes — down-forwards-again (STRYDE · Down Forwards Again, Doctor VSL · Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1m1H8YO6MEVQBnoD2gkWPfn-y__PW0Bbk
- User message: the Drive link + "RUN MANUAL". MODE blank → Mode 1; HOOKS → 3 in script (A/B/C) → 3 finished videos; VOICE derived (the script's "his" → male doctor, British).
- Script is a native Google Doc: `fetch_drive.py` exported it as .docx → `intake/script.txt`; spoken lines `work/script.lines.txt`, split into `work/HK1–HK3.lines.txt` and `work/BODY.lines.txt` (576 words). Hook labels / "(the reference's construction, exactly)" are authoring notes (VN01–VN03), not voiced.
- Inspo = a doctor-authority menopause supplement ad (the script's "Reference" link), 142.1s, 40 shots, 360×640 download, renamed `intake/inspo.mp4`; transcript `intake/inspo_transcript.txt`; measurements `intake/inspo_report.json`.
- Product Sheet V7.49.32 → `products/stryde/` (was V7.49.31 on this branch).
- **Boards:** Current https://claude.ai/artifact/UqVKJB21YyfBZTjxh5dNNT · Old https://claude.ai/artifact/8eXUW9NwJq49zRfPHtgC5Y · Final https://claude.ai/artifact/W11NPXayafpTXoY4FqMccb · Plan https://claude.ai/artifact/5Wzyk63o5viz5t4wLVZUu7
- **Hourly Fix check:** `trig_01XNVEi8936asCGsYpstFCaw` (:41 UTC, bound to session_01YaVWUyhH3VYNdrBjxmx6TC).

## Sessions
- session_01YaVWUyhH3VYNdrBjxmx6TC (2026-09-28 19:05–19:25 UTC): steps 1–3. Absorption, ledger, phrase inventory, claims,
  Mode & Model Lock; 2 avatar sheets (D-DOC, P-PATIENT) on Higgsfield (Sunburst, high, 2k, one each) → board To check;
  `docs/absorption` on Plan + Current. Higgsfield 17,998.5 credits before the cast.

- Same session 19:48 UTC: user "USE BRITISH ETNICITY" → D-DOC recast white British (v2 `71b20c5a`), v1 moved to Old; VOICE-DOC → light Yorkshire. Hourly check 19:41 found no Fixes.

- Same session ~20:00 UTC: user "go ahead with steps 4–5" → STEP4_5.md: PROP-P (Victorian terrace, stairs on the left wall),
  plates P0 hall/stairs, P1 front room, P2 kitchen (both with P0 attached), P3 consulting room; LEFT-knee worn refs W-L-FRONT/REAR/BENT
  (sent as nano_banana_pro, Higgsfield job record says nano_banana_2 — flagged on the cards); act map 44 rows (8 TH, 4 MECH),
  angles.py PASS; wardrobe map; 51 cards on Current; docs locations/actmap/wardrobe on Plan + Current. Higgsfield 17,894 after.
- Same session ~20:10 UTC: user "THE HOUSE LOOKS SMALL AND COMPRESSED" → cause: v1 prompts asked for a narrow Victorian terrace hall + galley
  kitchen, framed through doorways. Rebuilt as a large Edwardian semi (wide hall/stairs, ~3 m ceilings, shot from inside each room, no-cramped
  negative): P0 v2 `176c5c39`, P1 v2 `d0eeaf2a`, P2 v2 `abc2c220` (both against P0 v2); v1s on the Old board. Layout unchanged, angles PASS. Higgsfield 17,879.75.

- Same session ~20:20 UTC: user "go ahead with the voice stage" (every avatar/plate/ref was Confirmed on the board). Step 1 frame D-VOICE-IMG
  (job edd8434b, reported nano_banana_2) → board To check. G1–G3 Kling calls written + preflighted (PASS but 'start image approved'). Enhanced VO text
  locked (verbatim PASS, 3,180 chars). **STOP: Kling 3.0 credits** (§5 CREDIT_CAP, no reroute). See voice/VOICE_SOURCE.md.

- ~20:30 UTC: user "USE KEI AI AS SUBSTITUTE FOR NOW" → ADJUST recorded in BUILD_SHEET (Mode & Model Lock): every Kling call routes through
  Kie `kling-3.0-omni/image-to-video` (same Kling 3.0 Omni, prompt ≤3,072) via `voice/kie_kling.py` (refuses without preflight PASS), until Kling
  is topped up. Kie 186,607.8 credits. G1–G3 preflight: only 'start image approved' left (D-VOICE-IMG still To check).

- ~20:52 UTC: user "USE A DOCTOR CLOTHES" → D-VOICE-IMG v2 (job b17f293d): white coat + stethoscope locked in the prompt; v1 to Old; G1–G3 point at v2.

- ~21:00–21:40 UTC: user "go ahead with the voice stage" (taken as approval of D-VOICE-IMG v2). G1–G3 via Kie (690 credits; first send
  rejected free: Kie needs aspect_ratio auto). voice_source PASS → clone **Down** `lLQRuUpi2CbzE9mw4WRD` → eleven_v4 ×4 → split → house cut (16 parts +
  whole T1 one pass 135.83s PASS) → HeyGen photo avatar `bd3f0bac…` → Avatar V one-go render `c48a6bc2…` (motionPrompt rejected: no digital twin).
  Applied the user's 2026-09-28 corrections from the stryde-thirty-years branch (Avatar V only, one go) — that branch's §22U is not merged here yet.
  See vo/VO.md.

- ~22:00 UTC: user "the vo feels so fast the trims i dont like that" + "its trimmed even though she is not done talking".
  Measured: raw takes speak ~235 wpm speech-only (clone learned from the §22U ×1.2 source); the house cut left parts ending at −29…−38 dB
  (last word clipped); the HK3/body split clipped HK3 too. eleven_v4 ignores voice_settings.speed (0.85 and 0.7 both 12.32s on HK1).
  Fix in progress: re-cloned from the SAME takes at ×1.0 → **Down-Doctor** `a0lv6tcMVlFOFYq3VUob` (HK1 167 wpm vs 181); 4 new takes `vo/full2/`
  (T1, T4 verbatim by transcript; T2, T3 contractions); split with cuts snapped to the quietest point in each gap (`split_vo2.py`, `split2.json`).
  Planned cut: `trim.py` natural pace (0.35s sentence / 0.2s comma kept) with `--post 0.4` so every part ends in silence (test: −87 dB), not the house cut.
  **PAUSED on the user's word: "ill make a pr wait for it".** The HeyGen render `c48a6bc2…` (fast T1.ALL audio) is superseded once the new VO is cut.

- 2026-09-29 ~05:30 UTC: user "Ive added the new trim. Proceed with the vo again". Merged the default branch (V7.66.0, PR #36: no tight cuts —
  vo_trim −50 dB + 80 ms release, 60 ms fade, natural pauses 0.45/0.20s kept, pace gate ≤210 wpm). §22U step 4 still says ×1.2, so the ×1.0
  re-clone is NOT standard → the user picks. Re-cut all 8 whole takes (vo/cut766/): Down T1–T4 = 201/204/200/206 wpm (T4 FAIL: a breath left),
  Down-Doctor T1–T4 = 190/192/192/192 wpm, all others PASS, every tail −54…−59 dB. Board: VO-T1…T4-ALL (Down), VO-T5…T8-ALL (Down-Doctor), To check;
  the 16 old house-cut part cards + old T1.ALL moved to the Old board.

- 2026-09-29 ~08:05 UTC: user "CONFIRMED VO" — confirmed **VO-T7 (Down-Doctor take 3, ×1.0 clone, V7.66.0 cut, 192 wpm)** on the board → VO locked
  (the ×1.0 source is the user's call, off §22U step 4). Audio → HeyGen asset `bace0e73…` → Avatar V one go (photo avatar `bd3f0bac…`, 9:16 1080p, no
  motionPrompt) → video `f3fed9116b971e93d10e105279df52ae` (179.5 s). `vo/cut_points.py` now cuts at every hook AND act (A1–A5 lines from the act map;
  A1..A5 = BODY verified) → `th/TH-<k>.cut.mp4` → trim.py V7.66.0 → all 8 PASS (0.11–0.65 s removed each) → board TH-HK1/2/3 + TH-A1…A5 To check.
  Flag: at 69.2 s (TH-A2 ~7.8 s) both transcribers hear "the good **me**" for "the good knee" — told the user.

- 2026-09-29 ~08:40 UTC: user "CONFIRM PROCEEDS" → TH-HK1/2/3 + TH-A1…A5 set `use`. Step 6 hooks: `hooks/build_hooks.py` writes the four hook
  frames (§22T order + ANGLE-LINE / FOCUS-LINE / LIGHT-SHOT, start frame caught in the action, HK1-01a CONCEALED + NEG-CONCEAL, HK3-01a SKIN-T + CAP-SHARP),
  refs by Higgsfield job id → nano_banana_2 9:16 2k, one each (jobs 11d544d2, e46ab752, 82a43e53, b38467ec; Higgsfield reports `nano_banana_flash`)
  → board HK1-01a, HK1-02a, HK2-02a, HK3-01a images To check. Higgsfield 17,584 credits.
  Note: the act map's hook layouts (HK1-01a pip then HK1-02a cutout) predate the V7.65.0 layout limit (≤1 boxed in 5, never two in a row) —
  settle at assembly (`assemble.py` LAYOUT_MIX); frames are composed full-frame so either layout crops.

- 2026-09-29 ~09:15 UTC: user "I WANT A HOOK THAT WILL SELL I DONT WANT THIS NORMAL LOOKING HOOKS" → §34 correction on all four hook pictures
  (spoken lines unchanged, verbatim): HK1-01a → home-camera footage (§22E CCTV-FULL, hall corner), P-D1, coming down BACKWARDS with both hands on the
  banister, layout full; HK1-02a → the overfull drawer spilling onto the tiles; HK2-02a → tears the blank top sheet off the prescription pad (F12);
  HK3-01a → overhead, desk buried under knee scans, one more dropped on the heap, layout full. `work/actmap.py` rows + STEP4_5 + docs/actmap (Plan + Current)
  updated; angles.py PASS. `hooks/build_hooks_v2.py` → nano_banana_2 v2 renders (jobs 49b86e44, fd67eaff, 00f46dd9, f282b14c) → board To check;
  v1 frames moved to the Old board (copies confirmed, then deleted from Current). CapCut: HK1-01a gets a home-camera timestamp overlay in post (§22E, §17).

- 2026-09-29 ~10:15 UTC: user "FIX THOSE" → the board Fix notes (§34): HK1-01a "…RUNNING DOWN THE STAIRS AT THE SUBWAY STATION, NOT JUST AT HOME" →
  v3: she runs down Underground entrance stairs, forwards, P-D2, CONCEALED (new INCIDENTAL location L-TUBE); HK1-02a "SHOW ALL OF THOSE" → split into
  HK1-02a the operation (pre-op marker arrow on her left knee, L-HOSP) · HK1-02b the physio (resistance band, front-room floor, overhead) · HK1-02c the
  drawer (the v2 spill render carried over, no new call); HK2-02a "TEN SECONDS TO PUT ON THE STRYDE STRAP" → seating beat (§9B, SEAT_LOCK start frame:
  closed strap at mid-shin, both hands on the shell; NEG_SEAT kept for the clip, pin_end yes) — the product now first appears in Hook 2 (was PR-12).
  HK3-01a confirmed by the user. `hooks/build_hooks_v3.py`; jobs dc061b02, 21b325d8, caaf587d, dd2add6c (HK2-02a: nano_banana_pro requested,
  Higgsfield reports nano_banana_2). Replaced v2s (HK1-01a, HK2-02a) moved to the Old board. Act map rows + STEP4_5 + docs/actmap updated; angles.py PASS.
  Note: three B-rolls on the HK1-02 line (~6 s) sit near the 2.0 s minimum hold (§30H) — checked at assembly. Higgsfield 17,548.

- 2026-09-29 ~12:25 UTC: user "fix those" → board Fix notes (§34): HK1-01a "her hands should never hold the hand rail" → v4 both hands free, rail far off;
  HK1-02a "the operation is a knee replacement" → v4 a surgeon holds a total knee replacement implant above her bare left knee; HK1-02b "should be a COURSE
  not at home" → v2 NHS physio class (new INCIDENTAL L-PHYSIO), step-down with the physio watching; HK1-02c "holding the stryde strap … braces at the back,
  focus only on the stryde" → v2 held beat (§9A, HELD_GRIPS fingertips behind, nano_banana_pro requested / Higgsfield reports nano_banana_2), the overflowing
  drawer soft behind. HK2-02a (strap put on) and HK3-01a confirmed by the user. `hooks/build_hooks_v4.py`; jobs 76034f69, b03e5124, 96983a1e, 183c767a.
  Replaced versions moved to the Old board. Act map + STEP4_5 + docs/actmap updated; angles.py PASS. Higgsfield 17,445.25.

- 2026-09-29 ~12:35 UTC: user "fiix those" → board Fix notes (§34); HK1-01a v4 confirmed. HK1-02a "not an operation immediately — the doctor proposing a knee
  replacement" → v5 consultation (L-ORTHO): over the surgeon's shoulder, implant held out across the desk, her worried face (SKIN-T); HK1-02b "too simple,
  camera angle" → v3 busy NHS physio class, ground level through the parallel bars, straining step-up, physio spotting; HK1-02c "create a new one" → v3 from
  inside the drawer past the old braces, her hand lifts the STRYDE strap out (HELD_GRIPS bottom-edge pinch, focus on the strap). `hooks/build_hooks_v5.py`;
  jobs b6817ac4, cac8d27e, 11e82707. Replaced versions to the Old board. Act map + STEP4_5 + docs/actmap updated; angles.py PASS. Higgsfield 17,398.25.

- 2026-09-29 ~12:50 UTC: user "fix those" → HK1-02a v5 and HK1-02b v3 confirmed; HK1-02c "she should never put that strap on that drawer" → v4: the strap lies
  apart on the kitchen table, sharp in the foreground (§15A object beat); behind, soft, she tips the whole drawer of old braces into a black bin bag
  (`hooks/build_hooks_v6.py`, job 31dd56c8, nano_banana_pro requested / Higgsfield reports nano_banana_2). v3 to the Old board. Act map updated, angles.py PASS.

- 2026-09-29 ~13:20 UTC: user "that is good but dont make the braces magically going to the trash bag she should be putting them there" → HK1-02c v5:
  same frame as v4, she puts one brace into the bin bag by hand (bag held open with the other hand), the rest still in the drawer, nothing in mid-air
  (`hooks/build_hooks_v7.py`, job 08be9db1). v4 to the Old board.

- 2026-09-29 ~13:25 UTC: user "confirmed all" → all hook images confirmed. Lengths from `assemble.py --lengths` (hooks/plan/*.plan.json, on the trimmed
  TH-HKn audio): HK1-01a/02a/02b 3 s, HK1-02c 4 s, HK2-02a 4 s, HK3-01a 5 s. `hooks/build_hook_videos.py` → §35 JSON (RIG-R1C, one action + pace, HOLD-C,
  PHYS-MOTION-C, NEG-WARP-C + NEG-LIGHT-C, audio off), preflight PASS ×5 → Kie kling-3.0-omni (tasks 4c31f723, 0580e273, 9805c9fe, e3c78916, 885279cc;
  324 Kie credits) → board To check (generation 1 each). HK2-02a is pinned (§27G rule 5): its END frame (strap seated, hands lifting off,
  `hooks/build_hk2_end.py`, job 74bff83d) is on the board as card HK2-02a-END for the user's Confirm before its video. Kie 168,280.8.

- 2026-09-29 ~13:40 UTC: user "hk2 02a should not need an end frame remove it" → ADJUST: HK2-02a not pinned (act map pin_end no). END frame card removed from
  Current (image kept on the Old board as HK2-02a-END, unchosen). `hooks/build_hk2_video.py` → start frame only, SEAT_LOCK slide compressed, preflight PASS
  → Kie task c54cdc14 (72 credits) → board To check.

- 2026-09-29 ~13:45 UTC (hourly check): HK1-01a, HK1-02a, HK1-02b, HK1-02c, HK3-01a videos confirmed (`use`). HK2-02a video Fix "she should just be moving it up
  to fit the patellar tendon" → §22X gen 2: diagnosed from the v1 contact sheet (hands wrapped/pulled the band — the start frame leaves little travel, so the
  model filled 4 s with handling) → motion = ONE straight slide up, hands flat on the shell, then hold still; band-handling negatives; preflight PASS →
  Kie ed8a6e35 (72 credits) → board To check. v1 to the Old board. A third generation of HK2-02a needs the user's go.

- 2026-09-29 ~13:50 UTC: user "confirmed" → HK2-02a v2 use; all six hook videos confirmed. Hook rough cuts `assemble.py hooks/plan/HKn.plan.json`
  (TH-HKn trimmed + the hook clips, full layout) → all PASS (length = master, no black): HK1 12.18 s (cut-ins 3.0/5.0/7.0/9.0–12.0; the 2 s holds put
  'physio' 0.2 s and 'brace' 0.7 s ahead of their pictures; 0.2 s of doctor at the end), HK2 8.6 s, HK3 7.64 s → board HK1-CUT, HK2-CUT, HK3-CUT To check.

- 2026-09-29 ~14:05 UTC: user "the broll are late" → diagnosed: cuts anchored on late key words (stairs, operation, physio, brace, ten, scan) + the 2.0 s minimum
  hold pushed HK1's 'withouts' (lines ~1.7 s apart) after their words. Fix: anchors moved to the line starts (HK1-01a 'woman', 'Without' ×3, HK2 'It',
  HK3 'somebody'); ADJUST (build-local, `hooks/plan/assemble_local.py`): minimum hold 1.5 s instead of 2.0 s for this build — the shared assemble.py is
  unchanged. Re-cut v2: every cut-in 0.1 s before its first word; all PASS. v1 cuts to the Old board.

- 2026-09-29 ~14:25 UTC: user "the broll ends even though the script line hasnt finish yet" → diagnosed: the 0.1 s lead cut each B-roll into the previous
  line's ringing last word, HK3's scans cut back exactly on 'cartilage' (word end 4.9) and HK2 flashed 0.14 s of doctor at the end. Fix (build-local
  ADJUST in `hooks/plan/assemble_local.py`): --lead 0 (cut on the next line's first word) and a longer hold (DFA_HOLD: HK1 3.0, HK2 5, HK3 4.69 → ends
  exactly on 'I have started', 5.48 s). v3 cuts PASS (length = master, no black) → board; v2 to the Old board.

- 2026-09-29 ~14:50 UTC: user notes on the v3 cuts — HK3 open on the B-roll; HK2 B-roll a bit late; HK1 first cut before 'backwards' finished, last cut
  late (cut on 'And'), second B-roll only on 'Without'. → cuts placed BY HAND (`hooks/plan/cut_by_hand.py`, timelines `hooks/plan/HKn.cut.v4.json`) from
  medium.en word times + a 30 ms loudness trace (`hooks/plan/words.py` → words.json): HK1 doctor 0–1.50 | stairs 1.50–4.53 (backwards rings out 4.40) |
  knee replacement 4.53–5.72 (1.2 s) | physio 5.72–7.52 | braces 7.52–9.87 | doctor on 'And' 9.87. HK2 strap from 5.28 (end of 'knee'). HK3 scans 0–5.40
  (0.93×, §30H allows ≥0.8×), doctor on 'I have'. All = master length, no black. v3 cuts to the Old board.

## Where it stands
- Hooks done: images, videos and cuts v4 confirmed by the user (2026-09-29 "all confirmed").
- **Step 7 — all body images on the board, waiting on the user (2026-09-29 ~15:50 UTC).** The user: "generate all the images so i can check all of them",
  then, mid-run: "fix all the images cause the wardrobe map is just the same wardrobe all over even though its a different day/event".
  - **Wardrobe v2** (`work/wardrobe.py`, STEP4_5.md §Wardrobe map, `docs/wardrobe` on Plan + Current): one outfit per story day — 15 body days for P
    (P-B1…P-B9 problem, P-A1…P-A6 after), §14A audits PASS, signature item = her reading glasses on a beaded cord. Hooks keep P-D1/P-D2 (confirmed renders,
    untouched); the doctor keeps D-D1. `act` map `day` = light state only.
  - Every beat that shows her clothes was re-rendered with its day's outfit (one render each, Higgsfield nano_banana_2 / nano_banana_pro, gpt_image_2_5 for PR-22a).
    Act 1 BR-01/04/05a/05b and Acts 2–3 BR-06…BR-17b had an old-wardrobe v1 → moved to the Old board (Act 1 copies server-side then deleted from Current;
    the 13 Acts 2–3 v1s went straight to Old — they were replaced before review). BR-19a/b, PR-22a, BR-23 were first rendered with v2 wardrobe.
    Unchanged beats (no wardrobe): BR-02, MECH-01/03/05, BR-09a, MECH-14, BR-15, BR-16a/b, BR-20, BR-22b.
  - All 32 body images are To check on the Current board (Act 1: 8, Act 2: 7, Act 3: 7, Act 4: 7, Act 5: 3). Jobs, urls and asset ids: `acts/renders.json`,
    `acts/acts2_5_v1_renders.json`, `acts/v2_renders.json`; prompts `acts/<beat>.image[.v2].prompt.txt` from `acts/build_act1.py` / `acts/build_acts2_5.py`.
  - BR-07's first v2 job failed on Higgsfield's side (no render); resent once, same prompt.
- **Script lines (the user, 2026-09-29: "fix the script line cause its not showing the script line for that broll only"):** where B-rolls share
  a phrase, each card now carries only its own verbatim span (`BLINE` in `work/actmap.py`, asserted to rebuild the phrase; full phrase kept as `phraseLine`).
- **Fix round 1 (the user's board notes):** BR-02 v2 (film clipped flat on a wall viewer, not floating), BR-04 v3 (knee bent, fingertip on the tendon under the kneecap),
  BR-05a v3 (glasses on her nose; hauling herself up, struggling), BR-06 v3 (the plate's one straight flight, seen from the hall), BR-09b v3 (one woman only),
  MECH-03 v2 (glow on the tendon below the kneecap, kneecap unlit) — `acts/build_fix_r1.py`, one render each, back on the board as To check; replaced
  versions moved to Old. Confirmed so far: BR-01, BR-05b, BR-07, BR-08, BR-09a, MECH-01, MECH-05.
- **Fix round 2 (board notes ~16:40 UTC + the user's photo of the pad's inside):** BR-04 v4 (lens in front at knee height), BR-06 v4 (no feet at the bottom,
  phone at chest height), BR-11c v3 (her whole seated body side-on, one continuous leg), BR-16a v2 + PR-12 v3 (strap small in frame, ~10 cm, palm-wide),
  BR-17a v3 (sitting on the second tread, stairs under and behind her), MECH-14 v2 (strap in its real shape, shell cut away to show the pad) —
  `acts/build_fix_r2.py`. **Pad inside, from the user's photo (overrides the Product Sheet's INNER_PAD "plain smooth black"):** a mid-grey silicone pad set
  into the black shell back, same outline, fine raised curved parallel ridges over its surface, one smooth raised bar down its centre; chrome slide each end.
  The photo reached the chat only (no file in the container / Drive), so it is described in words; the Product Sheet itself is not changed yet (shared file).
- **Round 3 (2026-09-29 ~17:10 UTC):** the user split two script lines into more B-rolls — B-22's first half is now PR-22a (two straps) + **BR-22a2**
  ("Sixty days, and you keep the straps." — the two straps kept by her armchair, a calendar crossed off; 60-day seal in the edit) + **BR-22a3** ("From the
  Stryde site." — her phone on a shop page, the real site laid over in the edit). B-14: **MECH-14** is no longer anatomy (the user: "no need an anatomy here") —
  it is the strap turned over in her hand showing the grey ridged pad; **BR-14b** carries "The weight gets caught…" (her strapped knee stepping down a stair,
  hands free). Act map + STEP4_5 tables + docs/actmap (Plan + Current) updated; angles.py PASS; wardrobe audits PASS. Fixes: BR-04 v5 (finger on the midline,
  right under the kneecap), BR-16a v3 (strap held low by the knee model, waist-up), BR-19b v2 + BR-23 v2 (at the top of the flight stepping down, hands free),
  BR-22b v2 (undistorted copy). `acts/build_fix_r3.py`. Replaced versions moved to Old.
- **Round 4 (2026-09-29 ~18:10 UTC), all on nano_banana_pro:** BR-04 v6 (head-on close-up, finger straight down onto the tendon midline), BR-14b v2 (slim
  strap, ~3 cm tall), BR-19b v3 (strapped LEFT leg straight on the top step, RIGHT foot stepping down), BR-22b v3 (front view of her legs, the copy on the
  LEFT knee slipped a finger's width), MECH-14 v4 (strap flat in her palm, back up; pad described shape by shape — hourglass/peanut outline with a deep curve
  on one side, contour grooves, dog-bone rib), BR-22a2 v2 (product close-up of the two straps, no clutter). `acts/build_fix_r4.py`. Replaced versions moved
  to Old. **BR-22a3 ("From the Stryde site.") was deleted from the board (by the user) — not recreated; the line has no card until the user says where it goes.**
- **Round 5 (2026-09-29 ~18:25 UTC), nano_banana_pro:** the user sent two photos, now kept as files and uploaded to Higgsfield as references —
  the pad's inside `products/stryde/stryde_refs/inner_pad_user.png` (media `dca6d9b5-4931-4114-b093-f6fd7f8930c8`) and the BR-04 point
  `refs/BR-04_point_ref.png` (media `6a2715d9-de51-420d-844b-99abba716adb`; a pose/spot reference only — the finger points UP from below into the dip
  right under the kneecap, camera a little above the knee in front). MECH-14 v5 and BR-04 v7 attach them. New board Fix notes: BR-22a2 "brolls of showing
  the results of using the strap" → v3 is the result: her, weeks on, stepping down her front step to go out, strapped left leg straight (own story day
  **P-A5b** in `work/wardrobe.py`; act-map row now BR · L-P-DOOR · hip/three-quarter); BR-22b "show the cheap COPIES" → v4 is three stretched near-copies
  tipped out on the kitchen table (row now PRODUCT; CP-01 copy leg retired). STEP4_5 tables + docs/actmap + docs/wardrobe (Plan + Current) synced;
  angles.py PASS; wardrobe audits PASS. `acts/build_fix_r5.py`. Replaced versions moved to Old. The Product Sheet's INNER_PAD ("plain smooth black")
  still disagrees with the user's photo — not edited (shared file); the photo is in stryde_refs for any build to attach.
- **Round 6 (hourly Fix check, 2026-09-29 18:45 UTC):** BR-04 "the patellar tendon is below the center of the knee cap. will never be at the side fix this"
  → v8 is an edit of the user's own pointing photo (its framing and fingertip spot kept, the person/clothes/room swapped). `acts/build_fix_r6.py`.
  v7 moved to Old. Balances: Higgsfield 14,178.65; Kling 3.0.
- **Round 7 (2026-09-29 ~19:05 UTC):** the user sent a second BR-04 photo — "this is the point she should be pressuring her finger": a head-on,
  knee-height close-up, the tip on the front of the knee right under the centre of the kneecap (`refs/BR-04_point_ref2.png`, Higgsfield media
  `8227e906-5c92-428a-b483-c699d956d55f`). v9 edits that photo (framing + tip spot kept; her own right hand, rust jersey, camel corduroy skirt,
  mustard armchair). `acts/build_fix_r7.py`. v8 moved to Old.
- **2026-09-29 ~19:05 UTC: user "all confirmed"** → all 32 body images confirmed. **Act 1 videos:** word times for TH-A1…A5
  (`acts/plan/words.py` → `acts/plan/words.json`, faster-whisper medium.en), lengths `acts/plan/lengths.py` → `lengths.json` (each B-roll from its
  own span's first word to the next B-roll's; Kling = ceil, 3–15 s). `acts/build_act1_videos.py` → §35 JSON (B-roll: RIG-R1C, HOLD-C,
  PHYS-MOTION-C, INHERIT-CAP/ENV, PiP framing; MECH: RIG-RVF entry push, HOLD-C + HOLD-AC, NEG-CAM-RV + selected ANAT-NEG), preflight PASS ×8 →
  Kie kling-3.0-omni (tasks in `acts/video/act1_tasks.txt`; 648 Kie credits) → board To check, generation 1 each: BR-01 4 s, MECH-01 3, BR-02 3,
  MECH-03 10 (split in 2 parts), BR-04 5, BR-05a 5 (2 parts), BR-05b 3, MECH-05 3.
- **2026-09-29 ~19:30 UTC: user "fix those and generate the act 2 videos".** Video Fix notes: BR-05a "this should be 2 brolls", MECH-03 "this
  should be cut into 4 brolls", MECH-05 "new image and mechanism here" (BR-01, MECH-01, BR-02, BR-04, BR-05b confirmed). Act map: B-03 → MECH-03a
  ("Two centimetres below your kneecap", front view, one spot marked) · BR-03b ("there is a band of tendon about as wide as your thumb.", her thumb
  across the band, P-B2) · MECH-03 ("Every step you take lands on it.", keeps its image) · MECH-03d ("Seventeen times your bodyweight.", peak load);
  B-05 → BR-05 NEW ("Coming down is worse than going up.", top of the flight, hesitating, P-B3) · BR-05a (keeps its image, "Going up, your muscles
  lift you."); MECH-05 row = close on the knee at the catch. angles.py PASS, wardrobe PASS, STEP4_5 + docs/actmap + docs/wardrobe synced.
  New images (`acts/build_fix_r8.py`, nano_banana_pro): BR-05, BR-03b (first send blocked by the content filter as nsfw → resent once with the skirt
  resting above the knee, r8b), MECH-03a, MECH-03d, MECH-05 v2 → board To check; MECH-05 image v1 + video v1 to Old. Videos (`acts/build_act2_videos.py`):
  BR-05a v2 + MECH-03 v2 (gen 2, 3 s each for their new spans; v1s to Old) and Act 2 gen 1 — BR-06 5 s, BR-07 3, BR-08 6, BR-09a 5, BR-09b 3, BR-09c 3,
  BR-10 6 (tasks `acts/video/act2_tasks.txt`, 666 Kie credits) → board To check. Next: videos for BR-05, BR-03b, MECH-03a, MECH-03d, MECH-05 once
  their images are confirmed.
- **2026-09-29 ~19:50 UTC: user "fix and generate the act 3 videos".** Board: BR-03b card deleted by the user (not recreated; its span "there is a
  band of tendon about as wide as your thumb." now shows the doctor unless the user says otherwise). Fix notes: BR-06 video "she should be halfway
  down the stairs to show the going backwards", BR-10 video "this should be 3 separate brolls", MECH-03 video "normal walk only".
  B-10 split → BR-10 (keeps its image) · BR-10b ("It was never a weak muscle.", hand on the tightening thigh, P-B9) · BR-10c ("It was where the load
  was landing.", the left foot landing off the bottom stair, P-B9); act map + angles PASS + wardrobe PASS + STEP4_5 + docs synced. New images
  (`acts/build_fix_r9.py`) → board To check. Videos (`acts/build_act3_videos.py`, crop sentence now per layout per §35): Act 3 gen 1 (BR-11a 3 s,
  BR-11b 5, BR-11c 4, PR-12 3, BR-13 6, MECH-14 6, BR-14b 5, BR-15 5), Act 1 new images gen 1 (BR-05, MECH-03a, MECH-03d 3 s each; MECH-05 3 s on
  its new image, video v2), fixes BR-06 v2 (stay mid-flight, facing the steps), BR-10 v2 (3 s, its own span), MECH-03 v3 (one ordinary walking
  step; third generation on the user's go = their "fix and generate" on the card's Fix note). 1,080 Kie credits. Replaced videos to Old.
  **Honest flag:** BR-06 v2's last frame still has her at the bottom of the stairs walking away — the start frame puts her high on the flight and the
  model finishes the descent; a third try should start from a new frame with her halfway down, backwards (needs the user's go).
- **2026-09-29 ~20:10 UTC: user "fix and generate the act 4 videos".** Fix notes: BR-06 image "she should be half way down so we can emphasize the
  going down backwards", BR-15 image "generate a new image for this different concept", PR-12 image "this is too big the product", MECH-03 video
  "make a new image", BR-14b video "dont show any hesitation she should be walking normally no stopping". New images (`acts/build_fix_r10.py`):
  BR-06 v5 (halfway down), BR-15 v2 (NEW CONCEPT: her fingertip on the strap's notch at the kneecap's lower edge — act-map row now P hand ·
  L-P-FRONT · P-D2, wardrobe P-A2), PR-12 v4 (waist-up at the kitchen window so her body sets the strap's scale), MECH-03 v3 (the whole leg, one
  ordinary walking step) → board To check; their old images and the videos made from them moved to Old. **lengths.py fix:** a B-roll followed by
  a talking-head-only stretch (≥5 unmatched words) now ends 0.4 s after its own last word, and up to 3 unmatched numerals just before a span
  ("200 ,000", "34 %") belong to it — Acts 1–3 unchanged; A4 BR-17b 11 s → 3 s (the doctor's "I do not sell these…" stays on the doctor).
  Videos (`acts/build_act4_videos.py`): Act 4 gen 1 (BR-16a 6 s, BR-16b 3, BR-17a 4, BR-17b 3, BR-19a 5, BR-19b 5, BR-20 10), BR-10b + BR-10c 3 s
  each, BR-14b v2 (three even steps, no pause) → board To check; 846 Kie credits. Act map + docs synced.
  **Open for later acts:** A4 aligns poorly (ratio 0.74; BR-17b came out 11 s) — check the A4 act-map lines against the heard words before its
  videos. A5 still has the BR-22a3 row ("From the Stryde site.") with no card.
- **2026-09-30 ~10:45 UTC: user "fix those and generate the next videos".** Board Fix notes: BR-06 image "fix this distorted image"; videos
  BR-10b "this feels lke floating", BR-10c "make this anatomy", BR-14b "use anatomy here", BR-16a "this should be 2 brolls make an over all new ones",
  BR-16b "i need new image here", BR-17b "new image productive broll but with the pants down not showing the strap", BR-19a "should be going down the
  stairs no breathing and she should not touch the hand rail", BR-20 "i want new images here this should be 3 brolls".
  **Act map** (angles PASS, wardrobe PASS, STEP4_5 + docs/actmap, docs/wardrobe, docs/locations synced on Plan + Current): BR-06 now eye/profile from
  across the hall · BR-10b heel on a footstool · BR-10c → MECH (the load running down the leg, landing on the tendon) · BR-14b → MECH + strap (load
  caught by the pad, turned into the shell) · B-16 split: BR-16a "Thirty four percent less strain. Measured." (gait lab, L-LAB) + NEW BR-16a2 "Three
  years with orthopedic surgeons." (surgeon fitting the strap, L-ORTHO) · BR-16b walking group in a park (L-PARK; L-TOWPATH retired) · BR-17b out at
  the greengrocer's, trousers down (L-SHOP, still P-A3) · BR-19a sets off down the stairs, hands free · B-20 split: BR-20 "Not because the arthritis
  has gone." (his finger on the narrowed joint gap) + NEW BR-20b "Her scan looks exactly the same…" (the two films on his desk, overhead) + NEW BR-20c
  "Because the load is not landing on that band any more." (MECH + strap, tendon calm). Lengths re-run (A4: BR-16a 4 s, BR-16a2 3, BR-16b 3,
  BR-17b 3, BR-20 3, BR-20b 4, BR-20c 4).
  **Images** (`acts/build_fix_r11.py`, nano_banana_pro, one each) → board To check: BR-06 v6, BR-10b v2, BR-10c v2, BR-14b v3, BR-16a v4, BR-16a2 v1,
  BR-16b v2, BR-17b v3, BR-20 v2, BR-20b v1, BR-20c v1. Their videos wait for the user's Confirm (cards on Planned); the replaced images and videos
  moved to Old (Current's 1 GB store was full — the move freed it).
  **Videos** (`acts/build_act5_videos.py`, preflight PASS ×8, Kie kling-3.0-omni, tasks `acts/video/act5_tasks.txt`): Act 5 gen 1 PR-22a 4 s,
  BR-22a2 3, BR-22b 4, BR-23 3; BR-15 v2 5 s and PR-12 v2 3 s on their new images; MECH-03 v4 3 s on its new image (4th video of the card —
  user_go = this message); BR-19a v2 5 s (Fix, gen 2).
- **2026-09-30 11:41 UTC hourly Fix check (round 12):** image Fixes on the round-11 renders — BR-10c "i want a new one here" → v3 close on the knee,
  red pulses down the thigh landing on the tendon; BR-16a2 "wrong product" → v2 and BR-16b "wrong product" → v3 (both had drawn padded open-kneecap
  braces: now the strap described by what the knee shows — kneecap bare, a small curved shell under it, a thin band — the worn reference attached first,
  brace/sleeve negatives, the camera closer; BR-16b cut to four walkers); BR-20c "fix this cause its distorted" → v2 one leg only, no crossed legs.
  `acts/build_fix_r12.py` → To check; replaced images to Old. The user had meanwhile confirmed BR-06, BR-10b, BR-14b, BR-16a, BR-17b, BR-20, BR-20b →
  their videos (`acts/build_r11_videos.py`, preflight PASS ×7, tasks `acts/video/r11_tasks.txt`): BR-06 v3 5 s (third video, new frame; user_go = the
  10:45 message), BR-10b v2 3 s, BR-14b v3 5 s (third, new anatomy frame), BR-16a v2 4 s, BR-17b v2 3 s, BR-20 v2 3 s, BR-20b v1 4 s.
  Round-11 videos landed on the board To check: BR-15 v2, PR-12 v2, MECH-03 v4, PR-22a, BR-22a2, BR-22b (540 Kie credits for the eight);
  BR-19a v2 and BR-23 still downloading (Kie's file host drops transfers; `fetch.py`-style resume loop). Kie spend ≈ 3,780 so far.
- **2026-09-30 ~12:30 UTC: user "fix those and generate the new ones" (twice).** Video Fixes: PR-12 v3 "just let move it infront dont turn it" (a
  straight sideways move, front face to the lens), BR-22b v2 "dont make the strap jump" (almost still, one slow sag), BR-14b v4 "it should turn to
  blue" (the red stream turns cool blue where it meets the strap; 4th video, user_go = that message) — `acts/build_r13_videos.py`, preflight PASS.
  BR-16a "show it in a like treadmill" → new frame first (§22X): v5 is an edit of the confirmed v4 with a lab treadmill (`acts/build_fix_r13.py`;
  act-map row updated, angles PASS) → To check; its video waits. Replaced renders moved to Old.
  **All pending clips landed on the board To check:** BR-06 v3, BR-14b v4, BR-10b v2, BR-17b v2, BR-19a v2, BR-20 v2, BR-20b v1, BR-23 v1,
  PR-12 v3, BR-22b v2 (plus BR-15 v2, MECH-03 v4, PR-22a, BR-22a2 earlier).
  **Download fix:** Kie's tempfile host stalls mid-transfer through the proxy; `voice/kie_fetch.py` asks Kie's `common/download-url` for a signed
  R2 link and downloads in one go (sizes checked against Content-Length).
  Waiting on the user's check: images BR-10c v3, BR-16a v5, BR-16a2 v2, BR-16b v3, BR-20c v2 (their videos follow a Confirm).
- **2026-09-30 ~13:00 UTC → 2026-10-01: user "fix those and generate the new ones" / "Try again" (round 14).**
  **Mistake owned:** BR-14b v4 was sent on the OLD live-action start frame (a stale `START` entry carried over from an older builder) instead of the
  confirmed anatomy image — the user: "this is not the right image to genrate the video". v5 (`acts/build_r14_videos.py`) takes its start image from
  the board's confirmed `imageUrl` and asserts it; same for BR-22b v3. Both preflight PASS (user_go = the user's messages), landed To check.
  BR-23 "she should be going up normally she is not touching the hand rail" → new frame first (§22X): v3 she goes UP the stairs, hands free, seen
  high/front from the landing (`acts/build_fix_r14.py`) → To check; its video waits. Act-map rows BR-16a (treadmill), BR-19a, BR-23 synced to
  STEP4_5.md and `docs/actmap` (Plan + Current v14); angles PASS. Hourly check: no `regenerate` cards. Balances 2026-10-01: Higgsfield 11,377.4;
  Kie spend on this build ≈ 5,000.
  Waiting on the user's check: images BR-10c v3, BR-16a v5, BR-16a2 v2, BR-16b v3, BR-20c v2, BR-23 v3; videos BR-14b v5, BR-22b v3 and the
  earlier To-check clips.
- **2026-10-01: user "fix those and generate the next ones".** The board held one Fix: BR-14b video v5 "dont change the product". Diagnosis
  (§22X, motion): the RIG-RVF fast push ran from the whole leg to a tight close-up and, as the strap grew in frame, the model redrew it (a wider
  shell, metal side clips). v6 (`acts/build_r15_videos.py`, preflight PASS, 6th video — user_go = that message): RIG-RVD lateral drift, no push,
  the strap locked at its start-frame size and look, the light round it never on it → To check; v5 moved to Old. No other video could start: the
  remaining new-shot images (BR-10c, BR-16a, BR-16a2, BR-16b, BR-20c, BR-23) still wait for the user's Confirm. Every other B-roll video is confirmed.
- **2026-10-01 (later): user "fix those and generate the next ones".** Board: BR-14b v6 confirmed; BR-16a2, BR-16b, BR-20c images confirmed;
  Fixes BR-16a "remove those silver dots on the body", BR-23 "the product is wrong"; BR-10c still To check.
  Images (`acts/build_fix_r16.py`, edits of the current render attached first): BR-16a v6 markers removed; BR-23 v4 strap redrawn as worn (kneecap
  bare, small shell below, thin band; worn reference; brace negatives) → To check.
  Videos (`acts/build_r16_videos.py`, start images from the board, preflight PASS ×3; tasks `acts/video/r16_tasks.txt`): BR-16a2 v1 3 s,
  BR-16b v2 3 s (new park frame), BR-20c v1 4 s (RIG-RVD drift, not the fast push — BR-14b's lesson). BR-16a2 and BR-20c landed To check.
  **Storage: the Old board's 1 GB store is full, and so is Current's.** The replaced BR-16a v5 and BR-23 v3 images stay on Current (not lost, not
  marked archived). BR-16b v2 (21 MB, split in two) could not be uploaded — it is in `acts/video/clips/` (gitignored) and on Kie for 24 h
  (`clips/BR-16b.v2.result.json`); its card stays Generating. Asked the user whether to open a second Old Versions board.
- **2026-10-01 (later still): user "fix those and generate the next videos ones".** Fix: BR-20c video "dont show that red line i want blue glow
  on the stryde" → v2 (`acts/build_r17_videos.py`, preflight PASS): no red anywhere, the strap itself glows soft cool blue as the step lands, same
  RIG-RVD drift → To check. No new video could start (BR-10c, BR-16a, BR-23 images still To check).
  **Storage fixed: Old Versions 2 board** https://claude.ai/artifact/XPkuXUmrtvRSPgumXHsH9X (the live Old page, title "… Old Versions 2"; the
  first Old board's 1 GB is full). Moved there (copy confirmed, then deleted from Current, entries kept with `archived`, `archiveAsset`,
  `archiveUrl` = Old 2): BR-16a image v5, BR-23 image v3, BR-20c video v1, and the seven VO takes not chosen (T1–T6, T8; T7 is locked).
  BR-16b v2 (split in two parts) landed To check. The page's Old link still opens the first Old board; Old 2 is reached by its own link
  (`boards.old2` on the Current build doc).
- **2026-10-01 ~11:00 UTC: user "USE THE LATEST BGM UPDATE".** Merged the default branch (standards V7.76.0; the merge kept both sides of the
  CLAUDE.md table and .gitignore). Applied **§40A (V7.75.0) — music follows the script**: the Music Register Map (Build Sheet 5c, `docs/music`
  on Plan + Current) — hooks MUS-OPEN; body: The patient OPEN · The band EDU · "That is why" + the failed fixes EXPOSE · "This does." TURN ·
  Proof AFTER · Move the load / the offer (held back under the price) / "Go and do your stairs" OFFER. One family: low bowed cello and string
  drone, sparse felt piano, a slow heartbeat pulse (66 BPM pinned); no cute/cheerful/upbeat anywhere.
  Composing (ElevenLabs Music via `music.py`), what failed and why: v1 — the "ticking" pulse read 170–215 BPM, the 152 s body had a 42 s silent
  hole; v2/v3 — the body's turn section came out as one flat held tone between silences (three times); HK3 v2 refused (a section under 3 s).
  Fix: the body composed in three parts — A (patient → failed fixes, fades on "This does."), B (the release → proof; its first try had 14 s of
  silence from my "starting from near silence" and went silent from 73 s), C (the close, "Two for one" → end, crossfaded under the price).
  Loudness per section, the hook/body hand-over, the turn join and the close are set in the mix (`work/bgm_mix.py`), not regenerated.
  `music.py check` on the variant beds: TEMPO ~65 BPM PASS, VOCALS none, ENERGY in order; the CLICK flags fall on the bar downbeats (every
  ~3.9 s = 4 beats at 65 BPM) and the close's pulse — rhythm, not splices; LENGTH differs only by the plan's 2 s tail. On the board To check:
  MUS-HK1/2/3, MUS-BODY, PREVIEW-HK1 (the HK1 variant with the locked VO on top). The raw compositions are force-added to git (`edit/music/*.mp3`).
  Also landed: BR-16a v3 (treadmill), BR-23 v2 (going up), BR-10c v2 (red on the patellar tendon) — To check.
- **2026-10-01 (new session): user "FIX THOSE".** Merged the default branch (standards V7.77.0). One Fix on the board: BR-10c video v2 "I NEED A
  NEW MOVEMENT BASE ON THE IMAGE". Diagnosis (§22X, motion): v2's "the foot lands, the knee bends" on a frame whose foot is already planted made
  the model invent a step-up (the body, both hands and a second leg came into frame, the knee bent into a squat). v3 is written in the §35A
  short form (`acts/build_r20_videos.py`, 762 chars, the line, the action from this frame, one camera clause, 3 facts, 5 negatives, taste
  HT11/HT12/HT13): the leg stays planted, the knee settles a few degrees, three red pulses land on the patellar tendon. Preflight passes all
  but "motion confirmed" — §22X wants the user's confirm of the "Video will show" line before a video credit; this board's template predates
  the motion-plan display, so the line is asked in chat (also stored as `motionPlan` on the card, status ready). On the confirm: rebuild with
  `--confirmed` and send.
- **2026-10-01: user "ITS TAKING TOO LONG ON THE FIXING USE KLING CONNECTOR".** Merged the default branch again. Kling connector back (Ultra,
  45,091 credits) — video Fixes go through it from here (`kling-video-v3_0`, first frame, silent, 1080p). BR-10c v3 (§35A prompt, the reply
  taken as the motion confirm) was sent on Kling (24 credits) — but the user had meanwhile changed the card's note to "USE NEW IMAGE HERE ALSO
  USE KILNG FIR VIDEO", so that clip (made on the old frame) goes to Old 2 as unused when it lands. New image BR-10c v5 (`acts/build_fix_r21.py`,
  nano_banana_pro per the lock): the knee from the front, close, the tendon facing the lens, the foot planted → To check; its video (Kling)
  follows the Confirm, with the motion plan already on the card. Current's 1 GB store full again: image v4 and video v2 of BR-10c moved to Old 2.
- **2026-10-01 11:41 UTC hourly Fix check.** BR-10c image v5 Fix "MAKE THIS A CLOSE UP SHOT AND PATELLAR TENDON" → v6 (`acts/build_fix_r22.py`,
  an edit of v5): a front close-up of the knee only, the tendon large and the one red spot → To check; v5 to Old 2. The Kling clip made on v4
  (v3, 24 Kling credits) landed and was filed on Old 2 as unused. The card's motion plan updated for the close-up (the knee stays still, the
  pulses land on the tendon). Note: Higgsfield reports `nano_banana_2` as the model on the jobs requested as `nano_banana_pro` (every render
  this build) — logged, not changed. Balances: Higgsfield 10,498.65; Kling 45,027.
- **2026-10-01 ~12:30 UTC: user "i need a new br10c"** (board note on v6: "IT SHOULD BE THE PATELLAR TENDON NOT THE KNEE CAP"). Diagnosis: v4–v6
  all lit the kneecap — their ~5,000-character prompts named the kneecap a dozen times (every "not on the kneecap" line) and the model put the
  glow where the word sat. v7 (`acts/build_fix_r23.py`): a 710-character targeted edit of v6 — the pale cord below the kneecap glows red, the
  kneecap plain ivory, nothing else changed → To check; v6 to Old 2. Lesson for anatomy frames: name the target by what it looks like and
  where it is, keep the prompt short, and don't repeat the wrong structure in negatives.
- **2026-10-01 ~12:35 UTC: user "generate the video".** BR-10c image v7 confirmed → video v4 on the Kling connector (`acts/build_r24_videos.py`,
  §35A, 575 chars, kneecap named once; `kling-video-v3_0`, 3 s, silent, 24 credits) → To check.
- **2026-10-01 ~12:40–13:05 UTC: the edit + music v2.** User "confirm proceed, use the latest bgm update" (BR-10c v4 confirmed; every B-roll
  confirmed). Layouts: the user picked the current rule over the act map's EDIT-DFA — full screen by default, a 60/40 split on five mechanism
  shots (MECH-01/03/05/14, BR-20), never two in a row. Body cut (`work/body_edit.py` → `assemble.py`): no key-word anchors (they cut late);
  four rows merged for FLASH (<2 s lines: BR-05b, BR-09b, BR-10b, BR-16a2 — the doctor on camera there; the clips stay in the B-roll bank);
  PASS, 148.4 s, matches the VO, no black frames (`edit/body/BODY.rough.mp4`, 123 MB, not in git).
  User then: "i want a new one investigation and change when the product shows not a sad" → music v2 (`work/music_v2.py`,
  `work/bgm_mix_v2.py`): an investigation groove (ticking hi-hat, low kick, pizzicato, muted synth arpeggio, ~100 BPM, curious, never sad) up
  to "This does.", then the same groove lifts into a bright major key, confident, to the end. Body in two parts split on the turn word; BODY_A
  recomposed longer (TURN + 12 s) so the HK1/HK3 beds reach the turn with no gap. Check: ~99 BPM, no vocals, the lift 4 dB up. v1 music on Old 2;
  MUS-HK1/2/3 and MUS-BODY v2 To check; PREVIEW-HK1 retired to Old 2 (the finished videos replace it). Finished videos: `work/finish.py`
  (hook cut + body cut, one-word captions EG01, v2 bed ~18 dB under the voice, ducked, −14 LUFS) → `edit/final/FINAL-HK<n>.mp4`.
- **Then:** videos act by act after the user's Confirm; cuts placed by hand from word + loudness timings; finished variants (HKn + the body); CapCut block.

### 2026-10-01 — finished videos, captions reworked
- User: "the caption should not be one word only use the safezone". `work/finish.py` captions are now 2–4 words a card (phrases broken at punctuation / pauses >0.35 s, balanced — 5 words → 3+2; a lone word joins its phrase inside one sentence), white rounded box, black LiberationSans-Bold 64, wrapped to at most two even lines, centred at 58 % height inside the 9:16 safe zone (x 100–940, clear of the top 14 %, the bottom 25 % and the right-side buttons; asserted per card).
- Final board: FINAL-HK1 v2 (160.55 s, 163 cards), FINAL-HK2 v1 (157.01 s), FINAL-HK3 v1 (156.01 s), all `review`. FINAL-HK1 v1 (one-word captions) moved to Old 2 and deleted from Final.
- Next: the user's Confirm / Fix on the three finals; then Drive export.

### 2026-10-01 — Fix on the finals: captions, split screen, missing and late B-roll
- User: "THE CAPTION IS TOO BIG AND TOO HIGH ALSO DONT USE SPLIT SCREEN, SOME OF THE BROLLS ARE MISSING, BROLL PLACEMENT ARE NOT TIMED TO THE SCRIPT LINE".
- Body re-cut (`work/body_edit.py`): no split (all full screen); the four FLASH-dropped rows restored (BR-05b, BR-09b, BR-10b, BR-16a2) → 42 B-rolls; timed with `--model medium.en` (base.en had put BR-19a 1.2 s late and BR-17b / BR-20c 0.4–0.5 s late); every cut lands 0.25 s before its line's first word. Rendered via `hooks/plan/assemble_local.py` with `DFA_MIN_FLASH=1.0` (BR-09b "The garden." is a 1.0 s line) and `--min-th 1.25` (the doctor on "From the Stryde site.", 1.29 s). PASS, 148.38 s, no black frames.
- Hooks unchanged (already full screen, cuts confirmed).
- Captions: 46 px (was 64), centred at 70 % height (was 58 %), still inside the safe zone.
- Final board: FINAL-HK1 v3, FINAL-HK2 v2, FINAL-HK3 v2 — all `review`; the replaced versions on Old 2.

### 2026-10-01 ~15:10 UTC — new B-rolls on doctor-only lines; captions lower
- User: "SOME OF THE BROLLS ARE MISSING ALSO THE CAPTON SHOULD NOT COVER THE STRAP BRAND LOGO MOVE IT A BIT DOWN", then "there is a band of tendon about as wide as your thumb — THIS LINE AND ALSO CHECK THE OTHER SCRIPT LINES IF IT CAN BE ADDED A BROLL".
- Every confirmed B-roll was already in the cut; the doctor-only lines were BR-03b (thumb line, card deleted by the user 09-29), BR-22a3 ("From the Stryde site.", card deleted by the user — left alone), the Act 4 stretch (line 17, 7.9 s) and the Act 5 line ("You cannot strengthen your way out of a load problem. You have to move the load.", 4.6 s).
- New images (`acts/new_r25/build.py`, nano_banana_pro, one render each; Higgsfield reports nano_banana_2): **BR-03b** (edit of BR-04 v9: her thumb flat across the band), **BR-18** ("because it is the cheapest thing on the list and the only one aimed at the band." — edit of BR-11b: sleeve, brace, gel, strap in a row on the kitchen table; the doctor keeps "I do not sell these and I make nothing from saying this. I say it before we talk about anything else,"), **BR-21** ("You cannot strengthen your way out of a load problem." — her seated leg raise against an exercise band in the front room; the doctor keeps "You have to move the load."). Preflight: only the Sunburst rule fails (build lock, §18A) and on BR-18 the product-first rule (Image 1 must be the edited frame). On the Current board To check with motion plans.
- Current board store was full: two unreferenced images (2c6d8c6e…, 6ab8b1c0…) copied to Old 2 and deleted from Current.
- Hooks: their doctor-only openings are the doctor's own intro/close and the hook cuts are confirmed — not changed.
- Captions: centre moved 0.70 → 0.79 of the height (clear of the strap at knee height); re-render after the new B-roll videos land.
- Next: user checks BR-03b / BR-18 / BR-21 images → Kling videos (§35A) → user checks → body re-cut with the new rows → finals re-rendered.
- ~15:25 UTC: user "i want a broll there not th" → BR-03b video v1 made on Kling from the knee-photo image (24 credits); then the user: "i dont want to re use broll … i want anatomy here". BR-03b image v2 = new anatomy (nano_banana_pro, style of MECH-03a, three-quarter front: the tendon band lit, a glass thumb outline laid across it) — To check. Image v1 + the unused Kling clip moved to Old 2.
- ~15:40 UTC: user "confirm" (BR-03b anatomy image) → BR-03b video v2 (Kling, 24 cr); user "confirm all" → BR-18 (4 s, 32 cr) and BR-21 (3 s, 24 cr) videos. The Current board's 1 GB store was full again (everything left on it in use) → **Current 2 overflow board https://claude.ai/artifact/5triLGJUL7zH8wXtgk6Uc8** (template, BOARD_ROLE current, title "Down Forwards Again 2"); BR-03b / BR-18 / BR-21 cards and files moved there and deleted from Current; `boards.current2` on the build doc. All three videos To check on Current 2.
- Next: user checks the three videos → act map rows for BR-18 / BR-21 (BR-03b's row exists) and body re-cut (`work/body_edit.py` must read Current 2 cards too) → finals re-rendered with captions at 0.79.

### 2026-10-01 ~17:00 UTC — anatomy only; talking heads re-cut; B-roll re-timed
- User: "i dont need those 2, i just need the anatomy / some of the vo he didnt finish what he was saying i need you to fix the trimming / and the brolls still late or early…".
- BR-18 and BR-21 moved to Old 2 (not used); BR-03b (anatomy, video v2) set `use` on Current 2.
- Diagnosed the cut-off speech: the old trims (trim.py, base.en word edges + 0.3 s tail cap) ended every part while the last word still sounded (−42…−58 dB in the last 150 ms); TH-HK3's cut from the HeyGen take ended inside "question". **`th/recut_v2.py`**: parts re-cut from the take (`th/TH-ALL.wav.cuts.json`, medium.en) at the middle of the longest quiet run between parts; each part starts 0.12 s before its first voiced frame and ends 0.20 s after the last frame above −60 dB; nothing inside a part is cut; 60 ms fade-out. Every part now ends in digital silence. Old trims kept as `th/TH-*.trim.v1.mp4`.
- Hooks v5: the confirmed hand-placed v4 cuts mapped onto the new trims through the take's timeline (`hooks/plan/HKn.cut.v5.json`; HK1-01a 0.956×, HK2-02a in-point 0.32 to fill the longer spans). HK1 12.59 s, HK2 8.84 s, HK3 7.84 s.
- Body: `"audio": "base"` (V7.79.0 §30H rule 0 — timed on the trimmed take itself), 43 rows incl. BR-03b, `assemble_local.py` with DFA_MIN_FLASH=1.0 and --min-th 1.25, V7.79 LINE check PASS (no word under another line's picture); every cut 0.25 s before its line's first word. TH-BODY rebuilt with a re-encoded concat snapped to 149.75 s. Body 149.75 s, PASS, no black.
- Music v2 re-mixed on the new lengths, the lift on PR-12's first frame (67.375 s into the body).
- Finals re-rendered (captions 46 px at 0.79): FINAL-HK1 v4 (162.33 s), FINAL-HK2 v3 (158.58 s), FINAL-HK3 v3 (157.58 s) on the Final board `review`; replaced versions on Old 2.
- ~17:00 UTC: user "the sixty days i need a new one cause the video shows a buckle at the back of her knees that is not the product". Diagnosis: in the wide doorway shot the strap was under a fifth of the frame (FP11), so Kling redrew it as a bigger brace with a buckle behind the knee as she stepped. New image BR-22a2 v4 (`acts/new_r26/`, nano_banana_pro, edit of the front-room plate + front.webp): the act map's original idea for the line — her two straps kept, resting on her armchair arm, close (FP01/02/05/09/11/12). Card moved to Current 2 (Current is full); image v3 + video v1 moved to Old 2. Motion plan: slow push-in, nothing moves. To check.
