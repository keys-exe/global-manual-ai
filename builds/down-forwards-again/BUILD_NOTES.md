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
- **Then:** videos act by act after the user's Confirm; cuts placed by hand from word + loudness timings; finished variants (HKn + the body); CapCut block.
