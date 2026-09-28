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
**v1 (superseded by v2, kept):** 6.14s of unique speech is thin for a clone (the last build had 13.74s from three takes). §22U allows G3+ (the next lines);
one or two more takes (P-001, P-002) would roughly double the unique speech for 240 more Kling credits. Offered, not sent.
**Unverified by ear:** the accent (West Yorkshire) and texture. The agent measures pitch; you hear the placement.
## Step 6 — HUMAN: you clone `Regrets_clone_source.mp3` in the ElevenLabs app (Instant Voice Clone, Remove background noise ON), name **Regrets**

## Extra takes (user: "proceed" on the recommendation, 2026-09-28)
| Take | Kling generation | Line | Speech after trim | Pitch median | Gate |
|---|---|---|---|---|---|
| G3 | `AfObLPplL4KUADgUYwydzjwwVF6PgSgqHxfICvZ6eLMCqzchszz9oxHs30o0N_2Cbd2ENv_6` | "I read the messages that come in when people buy one of these." | 3.38s | 158.4 Hz (−11.9%) | **FAIL**, left out |
| G4 | `AWSdkjvqUy-CFus6hTAb7G-4AWM_jTDgHzM2bxrUlQThL5VkNHn3oVOGiNMPWRxfJZYmhEQ5` | "Regret number one. Nobody ever told them where it was actually coming from." | 4.03s | 181.8 Hz (+1.1%) | PASS |

G4 was first built as P-002–P-004 (19 words); 2,554 chars went over the ceiling, so it was cut to P-003–P-004 (13 words, 2,492).
240 Kling credits; Kling balance 1,839.

**Clone source v2:** `voice_source.py N_G1.mp4 N_G2.mp4 N_G4.mp4 --name Regrets` → PASS, joined 9.51s, looped ×4 → **38.09s**, no gap over 0.4s.
v1 (G1+G2, 30.72s) was confirmed on the board before v2 existed; it is kept as version 1. The user picks which to clone.
