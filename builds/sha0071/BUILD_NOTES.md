# SHA0071 — "Energy" (CA - CINE-N - ENRGY - PB - SHF-JHB - V1)

- **Drive task folder:** `1Hs37_1PXzkRAxNmmPlCpFr_THeHM6BUi` (script doc + 2 inspo films; cast photos linked from the script)
- **Board:** https://claude.ai/artifact/NzYWYmtn5wKo97V2xfKCm1
- **Run:** Automatic (`RUN AUTOMATION`), **Mode 4 — Realistic Film**, 9:16, Seedance 720p
- **Scope (user):** "MAKE THE FIRST 30 SECONDS OF THE SCRIPT ONLY" → Scene 1, lines 1–8, ending on Paula's "Energy." (nearest clean line to 30s). Delivered cut runs **47.5s** at film pace — see Flags.
- **Product:** KST Collagen Peptide Serum — https://koreanskintherapy.com/products/korean-silk-collagen-ampoule-2 (not on screen in this excerpt; no Product Sheet in Drive)

## Decisions
- **Connectors (user, mid-run):** "use the higgsfield connector only for all the generations dont use the others. for this run only." → images (GPT Image 2.5 Sunburst, Nano Banana Pro→logged nano_banana_2), Seedance 2.5 (omni_reference, 720p) all on Higgsfield. Kie used only as temporary file hosting for uploads (no generation).
- Credit cap set to **Higgsfield 2,000** for this run (600 image default + the video share that would have gone to Kie).
- Cast from the advertiser's talent photos (authority layer 1): §19 sheets generated **with the photo attached** (§19 says prose-only; reference wins). `NEG-SHEET`'s "no makeup / no jewellery" dropped — the photos show both.
- Film Look Sheet written by the agent (Board → Plan → Absorption). Camera package: ARRI Alexa 35 S35 + Cooke S4/i.
- Voice masters: Seedance 10s neutral clips (§24I), stream-copied. Uploaded to Higgsfield as 320k MP3 (Higgsfield stores audio only as MP3) — format conversion only.
- SC-01 sound: dialogue from the clips (FFT denoise + level), **no music** (script: no music intro; Higgsfield has no general music/SFX model), one continuous synthesized corridor room tone.
- Grade in the edit only: per-clip match to master (sat/luma/warmth), one cool-fluorescent look, one grain pass; captions small, lower-centre, one line at a time.

## Flags
1. Length 47.5s vs "first 30 seconds" — the 8 lines at natural film pace; no silences cut (§24L).
2. Kie spent 630 credits on two voice-master tasks submitted before the Higgsfield-only instruction; outputs discarded.
3. `nano_banana_pro` requests logged as `nano_banana_2` by Higgsfield (known §5 alias) — kept, judged on merit.
4. Insert (badge): 3 image attempts (seated read ×2, then three hands) → §24H edit route: 9:16 crop of v3 (768 px wide).
5. SH01 + SH08 gen 1: **boom microphone in frame** — caused by `AUD-FILM`'s "boom microphone just out of frame" wording. Gen 2 kept the string (preflight enforces it) + "microphone stays outside the picture" + equipment negatives → clean. **Proposed amendment:** reword `AUD-FILM` to drop the boom-mic image.
6. SH08 rendered at MCU not CU → 1.25× punch-in in the edit (≤1.3×, §24H).
7. VISITOR badge text slightly garbled in the SH01 wide (unreadable at that size).
8. No Drive OUTPUT video upload: the Drive connector takes file bytes inline only; the final MP4 is on the board and sent in chat.

## Open
- Scenes 1 (lines 9–10) through 12 not built.

## Delivery (2026-09-27 09:10 UTC)
- Final: `edit/SHA0071_SC01_HK1_final.mp4` — 720×1280, 24 fps, 47.8s, 7 Mbps, −14.6 LUFS, TP −0.9 dB, transcript 74/74 words. On the board as card `SC01-EDIT` (3 byte parts).
- Spend: Higgsfield ≈646 of the 2,000 cap (images ≈30, Seedance 616 incl. the two 70-credit voice masters and SH01/SH08 gen 2). Kie 630 (discarded, Flag 2). Kling 0. The Higgsfield account is shared with other work, so its balance (4,795 → 3,480) also reflects other sessions.
- Raw cut (user ask): `edit/SHA0071_SC01_HK1_raw.mp4` via `build_edit_raw.py` — same cuts, SH08 punch-in and captions; no colour match/grade/grain, clip audio untouched (−19 LUFS). Board `SC01-EDIT` v2; the graded cut stays v1.
- Score (user ask "add the music for more emotion"; user OK to use ElevenLabs Music since Higgsfield has no music model): cue `sound/SC01.cue.json` → 2 tracks (max). v1 played through "Energy."; v2 had 7s silence + mid-scene dropouts → v1 kept, faded in 1.2s and cut to silence at 43.75–44.2s. Mixed under the raw cut with `mix_scene.py` (music −15 dB, duck 6 dB, no added room tone) → `edit/SHA0071_SC01_HK1_raw_music.mp4`, −14.8 LUFS, 73/74 words heard (the "seemed/seems" mishearing). Board `SC01-EDIT` v3 + `MUS-SC01` card. Swell is only 1.5 dB over the confide section (check wanted 2 dB).
- INS01 Fix (user: "that is two hands"): frame v5 = nano_banana_pro edit of the crop with the second hand removed (one right hand); video gen 2 (`calls/SC01-INS01.gen2.json`, preflight PASS, 28 cr) — one hand every frame. Same in/out in the plan.
- Film finish (user: grade + fades "like a movie not a grave"): `build_edit_film.py` — warm gentle S-curve, cool-ish shadows, sat 0.96, soft vignette, fine grain, 0.8s fade in, 1.5s fade out, score mixed (−14.8 LUFS, TP −0.7). → `edit/SHA0071_SC01_HK1_film.mp4`, board `SC01-EDIT` v4.
- Film cut v5 (user): captions plain white, no outline/shadow; no fade in (fade out 1.5s kept); grain removed. Board `SC01-EDIT` v5.
- Wide shots Fix (user: "the two parts … the other angles doesnt look like this"): the old master frame had a narrow corridor with a plain white wall, a wooden door and a picture; every coverage angle shows frosted-glass partitions, daylight and the lift. New wide frame F-WIDE v2 (nano_banana_pro from the two OTS frames + both sheets) → v3 (badge text fixed). SH01 gen 3 (user approved the third try; preflight fails only on the generation count) and SH05 gen 2 (preflight PASS) from it, same in/out. Captions re-timed from `renders/` (make_captions.py now reads the renders, not edit/match). Board `SC01-EDIT` v6. The badge lettering in the SH01 wide is not clean at that size (was already so on the old wide; not a flag until now).
