# Narrator voice source — §22U steps 1–7 (stryde-too-bad)

## Step 1 — voice-source frame (N-VOICE-IMG)
- v1 (job 7ae0b05d…): drew a second phone, a pen mug and a newspaper in front of her → user Fix "fix this". v2 (job 055e39b6…): prompt fixed, but ignored the sheet (younger, brown hair) and drew a camera-app screen → user Fix "USE MY AVATAR NARRATOR".
- **v3 (job 847461ac…), confirmed by the user 2026-09-29 ("CONFIRMED PROCEED")**: the sheet's face close-up cropped to `N_face_ref.png` (Higgsfield media 4a0599ba…) and attached as image 2 beside the sheet; identity restated; camera-UI negatives. Requested `nano_banana_pro`; every job reports `nano_banana_2`.

## Step 2 — Kling voice takes (Kie `kling-3.0`, §5 fallback: the Kling connector had 3 credits)
| Take | Line (verbatim) | Kie task | Credits | Notes |
|---|---|---|---|---|
| G1 | Too bad these knee straps look too small to work. | 81c30cb2… | 270 | Kling added a stray "Bad." at the end (clone material only) |
| G2 | Built over three years with orthopaedic surgeons, to do what sleeves and braces never could. | a33afcc7… | 270 | silent lead-in cut at 1.55s (`N_G2.lead.mp4`) — whisper stretched "Built" over 0.7s of air and the medium trim failed its gap check |
| G3 | They're small on purpose. Because the pain comes from one small spot. | 8a22c386… failed ("Internal Error", 0 credits) → resent a7dc8222… | 270 | lead-in cut at 2.2s (`N_G3.lead.mp4`), same reason |

All three: `kling-3.0/video`, pro 1080×1920, 9:16, 10s, sound on, single shot, start image = N-VOICE-IMG v3; JSON 2,441–2,482 chars (§37 TH ladder steps 1 + 4), `preflight.py` PASS.

## Steps 3–5 — `voice_source.py N_G1.mp4 N_G2.lead.mp4 N_G3.lead.mp4 --name TooBad --outdir src` → PASS
Pitch medians 191.6 / 205.1 (+7%) / 210.5 Hz (+9.9%, inside ±10%). Joined 13.57s of speech, looped ×3 → **`src/TooBad_clone_source.mp3`, 40.75s**, no gap over 0.4s.

## Steps 6–7 — clone by API
`elevenlabs_clone.py clone src/TooBad_clone_source.mp3 --name TooBad` → **PASS, voice `TooBad`, id `5Iu9piJEpm2ewCIAa3Wm`** (IVC, background-noise removal on). Account: 513 free voice slots before.
