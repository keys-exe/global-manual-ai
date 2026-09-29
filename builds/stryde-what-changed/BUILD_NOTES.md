# Build notes — stryde-what-changed (STRYDE · What Changed, podcast, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1zFGMzZ-olam9tpD63hM5MvHlUMkUVHKW
- User message: "RUN MANUAL. BRITISH" → RUN: MANUAL, VOICE: British. MODE blank → Mode 1. HOOKS → 3 in script (A/B/C) + one shared body → 3 videos.
- Script file had no extension (Word 2007+) → `intake/script.docx`; spoken lines `work/script_lines.txt`, per part `work/script_{HK1,HK2,HK3,BODY}.txt`
  (the "A —" / "B —" labels and the hook quotation marks removed by hand; no spoken word touched).
- Product Sheet in the folder is V7.49.29; the repo's V7.49.37 is used.
- **Boards (account iamnotkeysi@gmail.com):** Current https://claude.ai/artifact/3uy6935ZTAivEZgysENYvq · Old https://claude.ai/artifact/T3RZo3ak1QfC2ue6yaV9LD · Final https://claude.ai/artifact/6aiYxibqFq5F9R8tMiqp2z · Plan https://claude.ai/artifact/SGxFerhs4WKGiy3uV5bh8R

## Sessions
- session_01F5f9WBysAi6Tgspjop271s (2026-09-29 11:20 UTC): steps 1–3. Inspo measured (195.5s, 115 shots, 176 wpm, host ~55% on camera,
  cut-out PiP on most B-roll), absorption, ledger (VN01 = hook line 1 as VO over B-roll), phrase inventory, claims (F2–F11), Mode & Model Lock.
  Cast: H-HOST, R1-MAUREEN, R2-DESMOND (landed 11:50, board To check) on Higgsfield (Sunburst, 2k, one each; R2's first call returned 503 before starting, sent once more).
  Higgsfield 17,537 credits before the cast. Four boards made; docs/absorption on Plan + Current.

- 12:08 UTC hourly Fix check: H-HOST Fix "change host avatar to more attractive or have pleasing personality" → v2 (job b9242d45…, Sunburst):
  attractive/warm face fill, 44, `NEG-DEFAULT-FACE` without "catalogue-model bone structure" and its last two clauses, "unflattering" dropped
  from `SKIN-T` (H only; §34 correction for this sheet, `cast/build_sheets.py` `host=True`). v1 moved to Old (asset 10c81baa…), deleted from Current.

- 12:25 UTC user "fix": H-HOST Fix "change the host, i want different person have pleasing personlaity" → v3 (job e6a49b97…): a new person —
  white British woman, 41, honey-blonde, freckles, beauty mark, cream cable-knit; same warm face register as v2. v2 moved to Old (asset 700dc380…).

- 12:45 UTC user "I'VE CONFIRM PROCEED": H-HOST v3, R1, R2 confirmed (flags unanswered → voiced as written, open).
  Steps 4–5: plates P0-STUDIO, P1-PROP-M, P2-PROP-D, P3-STREET, P4-KITCHEN, P5-CONSULT (Sunburst 16:9) + S1-SURGEON sheet (§19B)
  + H-VOICE-IMG (§22U step 1, nano_banana_pro requested, logged nano_banana_2) → board To check. Act map `work/actmap.py`
  (61 rows: 44 B-roll + 17 TH; pip on B06, B12, B20; `angles.py` PASS HK1–HK3), wardrobe map, `STEP4_5.md`; docs/locations,
  docs/actmap, docs/wardrobe on Plan + Current; 44 planned beat cards. Kling takes G1/G2 built (`voice/H_G*.kling.json`, 2,441 / 2,417).

- 13:00 UTC user "fix those": board → all 6 plates + S1-SURGEON confirmed; H-VOICE-IMG Fix "medium shot only, not too wide" →
  v2 (job bccb1cd0…, waist-up, face ~¼ frame height, no knees/legs; nano_banana_pro requested, logged nano_banana_2). v1 to Old (asset 0b58b0a8…).

- 13:08 hourly check: H-VOICE-IMG v2 confirmed → §22U straight through. Kling at 3 credits → Kie `kling-3.0/video` (pro, sound, 10s):
  G1 057fb576… (15 words, cut from HK1's first clause to pass the 20-word 10s budget), G2 c252fcb9… (19 words); preflight PASS both.
  `voice_source.py` PASS (190.5 / 188.2 Hz, 31.9 s) → ElevenLabs IVC **`Changed` = YlKDROvtue2RvBG9MAKL**. Enhance run by hand on
  HK1+HK2+HK3+BODY (`vo/enhanced.fitted.txt`, 5,025 chars, `[slowly]`/`[pause]`, verbatim PASS) → 4 eleven_v4 takes at speed 0.9
  (T1 174, T2 177, T3 174, T4 172 wpm). Take check `work/take_check.py` (cut_points.py's number map lacks 5,000 / 70 million):
  T1 PASS (small.en missed "your"; medium.en hears it) = **working take**; T3 "that is" → "that's". Cuts T1: 10.34 / 25.91 / 41.82 s.
  User (mid-run) "CONFIRM ALL LOCATION. PROCEED"; "VOICE ID: PROCEED" → asked: keep `Changed` (answer: keep).
  HeyGen photo avatar 1f288b8b… (H-VOICE-IMG v2); Avatar V rejected motionPrompt (no digital twin) → Avatar V without it (§22U (c)),
  video 20d477e9…, 254.06 s → cut HK1/HK2/HK3 + BODY → `trim.py` natural PASS: HK1 213.2 s 182 wpm, HK2 217.8 s 185, HK3 218.8 s 181.
  Board: user chose the 4 Mbps re-encode (trim.py output ~320 MB each); TH-ALL-T1 untrimmed (133 MB, parts) + TH-HK1…3 (~112 MB).
  Hook 1 images HK1-a (Maureen's legs on her stairs, NB2 → logged nano_banana_flash) + HK1-b (ANAT-A hot spot) → To check.

- 15:07 hourly check: user confirmed VO parts on the board — **HK1 + HK2 = T4, HK3 + BODY = T2** (VO locked, `voLocked`).
  §22U step 10 → talking heads regenerated: `vo/VO_LOCK.mp3` (T4 HK1 + T4 HK2 + T2 HK3 + T2 BODY, untrimmed, cuts 10.44 / 25.76 / 41.39 s)
  → HeyGen Avatar V in one go (video 2de76968…, 249.4 s, no motionPrompt) → cut + `trim.py` natural: HK1 3:30 185 wpm, HK2 3:34 188,
  HK3 3:36 183, all PASS → 4 Mbps board encode (`vo/th/lock/`). T1 talking heads (4 cards) + the 12 unchosen VO parts moved to the
  Old board, their files deleted from Current. One upload part began with '<' and was refused as markup → boundary moved one byte
  (TH-ALL-LOCK parts: 14,999,999 + 7,500,001 + 7,500,000 + …; the join is byte-exact).

- 16:40 user "confirm": board shows HK1-a + HK1-b images confirmed; talking heads (TH-ALL-T1, TH-HK1…3) set to `use` on that word.
  Hook 1 clips (`work/clips.py`, §27G, locked-off tripod, `preflight.py` PASS): E6 from the trimmed HK1 variant's word timings
  (HK1-a 0–4.28 s → 6 s; HK1-b 4.28–7.64 s → 5 s). Kling at 3 credits → Kie kling-3.0: HK1-a 7bbb2401… (108 cr), HK1-b 6b510627… (90 cr) → To check.

## Where it stands
- **Waiting on the user:** Confirm/Fix Hook 1's clips HK1-a, HK1-b (step 6 gate), then Hook 2's images. Their clips (Kie Kling 3.0 while Kling is short) follow each image's Confirm; E6 lengths from the T1 cuts.
- Board storage: Current ≈ 0.65 GB used of 1 GB after the talking heads — B-roll clips will need the Final/Old split or a second store.
- Open flags: F2, F3, F5, F6, F8, F9, F11 (claims).

### 2026-09-29 — Hook 2 images
- Hook 1 images and clips confirmed (board `use`). Hook 2 start images generated (`work/beats.py HK2-a HK2-b`, nano_banana_2 2k 9:16, one render each; HK2-b refs R2 sheet + P2 plate; new light `D-GREY-L`, colour `D-STAIRS-AM` 6500K). Jobs e16327a8 (HK2-a), a7ba052b (HK2-b); on the board as To check (`hooks/HK2-*_v1.png`).
- HK2-a shows no thumb against the tendon (F2 unanswered).
- Video connector: Kie AI `kling-3.0/video` (Kling account 3 credits) — told the user.
- User "CONFIRM": HK2-a / HK2-b images confirmed. Hook 2 clips (`work/clips.py`, §27G locked-off, `preflight.py` PASS), E6 from the trimmed HK2
  variant (HK2-a 0–3.36 s → 5 s; HK2-b 3.36–6.80 s → 5 s). Kie kling-3.0: HK2-a 1cbc2673… (90 cr), HK2-b f2445f70… (90 cr) → To check.
- User Fix on HK2-a image: "GIVE ME DIFFERENT BROLL" → HK2-a re-planned (act map + `beats.py`): no longer ANAT-A (too close to HK1-b) —
  MCU Desmond seated on his bottom stair tying his right trainer, bent bare knee nearest the lens, high three-quarter (angles.py PASS).
  v2 job f20c462e (refs R2 + P2) → To check. v1 image + v1 clip moved to the Old board, deleted from Current. HK2-a clip in
  `clips.py` still describes the anatomy swell — rewrite it (one lace tug) once v2 is confirmed. HK2-b clip still waiting on the user's check.
- User Fixes: HK2-a "I WANT ANATOMY B ROLL HERE" → anatomy again but an ECU of the tendon as a band, high three-quarter
  (ANAT_A_POINT_TIGHT kept), v3 job 512cb5a0. HK2-b "GIVE ME DIFFERENT BROLL HERE" → Desmond rising out of a deep squat with a heavy
  box of old football kit in his hall, low front, v2 job fd0fae7c (refs R2 + P2). Act map rows updated, angles.py PASS. Replaced
  versions (HK2-a v2 image; HK2-b v1 image + v1 clip) moved to the Old board, deleted from Current. Both clips in `clips.py` need
  rewriting to the new shots once the images are confirmed (HK2-a: the band draws taut once; HK2-b: one lift out of the squat).
- HK2-a v3 image confirmed on the board → clip rewritten to the band shot (`clips.py`: the band draws taut once, spot brightens once;
  preflight PASS), Kie kling-3.0 497adfd7… (90 cr), 5 s → To check (video v2; v1 was the old front-view shot, already on Old).
- HK2-b Fix "FIX THIS" (no detail) → read off v2: face partly in frame, Nike logos on the trainers, "OLD KIT" on the box, shallow squat with
  the box in front of the knees. v3 prompt fixes all four (top edge across the chest, plain unbranded trainers, unmarked box, deep squat with
  the box between the knees), job ec0b55bb → To check. v2 image moved to Old, deleted from Current.
- **Where it stands:** waiting on the user's check of the HK2-a clip and the HK2-b v3 image; then the HK2-b clip (one lift out of the squat),
  then Hook 3 images.
