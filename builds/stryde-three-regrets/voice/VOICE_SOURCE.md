# Narrator voice source — §22U steps 1–5 (stryde-three-regrets)

## Step 1 — talking-head frame
- Prompt `N_step1_image.prompt.txt` (8,881 chars), built by `build_voice.py` from Appendix A by ID (`CAM-LOCK`, `FRAME-SCALE` + `FRAME-PROPPED`,
  `LIGHT-SHOT` from the P2 light plan: east window, screen-left, `SKIN-B1/B3/B4`, `EYES-A`, `HAIR-A`, `NECK-A`, `TEETH-A`, `CAP-A`, `CAP-FILE`,
  negatives incl. `NEG-LIGHT`). Attached: the N sheet (`4bb1467d…`) and the P2 workroom plate (`698faa52…`).
- Render: job `9378efcb-3e27-47ab-99d1-18e9ee05c803`, 1536×2752, `N_step1_v1.png` (board asset `eabcc9f5cc70f78e33a9cbfd63a0fec8`).
  **Routing note:** requested `nano_banana_pro`; the job reports `nano_banana_2`, the same §5 logging mismatch the last STRYDE build saw.
  Recorded, not rerolled. The check is yours.
- This frame is also the HeyGen avatar image (§22U step 11).

## Step 2 — Kling takes (step-1 frame confirmed by the user, 2026-09-28; sent)
| Take | Line (verbatim, HK1) | Words | JSON chars | Preflight |
|---|---|---|---|---|
| G1 | Three things people tell us they wish they had known about their knees. | 13 | 2,476 | PASS except "start image approved" |
| G2 | Not one of them is that they should have gone to the doctor sooner. | 14 | 2,476 | PASS except "start image approved" |

`kling-video-v3_0_omni`, `image_1` = the step-1 frame, 9:16, 1080p, 10s, `enable_audio: true`, `prefer_multi_shots: false`, one generation per call.
§37 TH ladder applied to reach the 2,500 ceiling (was 2,597): step 1, selected negatives (dropped from `NEG-WARP-C`: parts detaching,
duplicate objects, flickering geometry; from `NEG-LIGHT-C`: sun patch moving), and step 4, the framing tightened to "As in the start frame."
`VOICE-NARR` and `AUD-A` are whole.

| Take | Kling generation | Speech after trim → ×1.2 | Pitch median | Whisper |
|---|---|---|---|---|
| G1 | `AU0gnSBASAXOJOROw4Xw1oFfaiNULTSTl75pp2M8QQqunjW6EU5ifbbCrWynnXa494B9u29z` | 3.23 → 2.71s | 179.8 Hz | verbatim |
| G2 | `AfQ5upmgCBYZTIJevOIgWX6RFZu6yoAFUbQmYOL6p8Xw7f-EamuemMQuxuK-KuEymS02DlmJ` | 4.10 → 3.44s | 179.8 Hz (0%) | verbatim |

240 Kling credits (120 each); Kling balance 2,319 → 2,079. G2 (24.5 MB) is on the board as two 15 MB byte pieces.

## Steps 3–5 — `voice_source.py N_G1.mp4 N_G2.mp4 --name Regrets` → PASS
Same-voice gate PASS (0% pitch difference). Joined 6.14s, looped ×5 → **`Regrets_clone_source.mp3`, 30.75s**, no gap over 0.4s.
**Note:** 6.14s of unique speech is thin for a clone (the last build had 13.74s from three takes). §22U allows G3+ (the next lines);
one or two more takes (P-001, P-002) would roughly double the unique speech for 240 more Kling credits. Offered, not sent.
**Unverified by ear:** the accent (West Yorkshire) and texture. The agent measures pitch; you hear the placement.
## Step 6 — HUMAN: you clone `Regrets_clone_source.mp3` in the ElevenLabs app (Instant Voice Clone, Remove background noise ON), name **Regrets**
