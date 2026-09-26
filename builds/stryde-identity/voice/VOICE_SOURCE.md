# Narrator voice source — §22U steps 1–5 (stryde-identity)

| Take | Kling generation | Line | Speech (s) | After trim → ×1.2 | Pitch median | §22W verdict |
|---|---|---|---|---|---|---|
| G1 | `AbYmZVq-…t5zrAL`… `AbYmZVq-3uWGoxdGGYwytXKefII1i4AWM4NC0ZaOeZKIStq3WTKynyfQgQ7YJpnUtbM5R8MX` | HK1 "Why these knee straps are a must if you've been told you're bone on bone." | 2.84–8.80 | 4.52 → 3.79 | 128.0 Hz | **USE** — every word, identity holds, no frozen/black runs |
| G2 | `AQv15za5WyvcXyFXbvvJdQo6jNyx6xq41DO9r4WzoJSG78G-XpH4issWD59KefiTkZs6U81i` | P-001/002 "Because every step puts seventeen times your bodyweight through one small spot below your kneecap." | 2.12–9.50 | 6.69 → 5.58 | 131.1 Hz (+2.4%) | **USE** |
| G3 | `AYQSzgBulpHzuh-xmJBfuoDWa7d1n_gJwuIhC8icGwzFGQ_v5M8axkohLN_Onx55JvmLLHdY` | P-003/004 "These straps took three years to build with orthopaedic surgeons, to sit right on that spot." | 3.32–9.84 | 5.23 → 4.38 | 134.5 Hz (+5.1%) | **USE** ("orthoparic" is Whisper's mishearing) |

Same-voice gate: all three within ±10% of G1 (max 5.1%), no mismatch. Joined 13.74s, looped ×3 → **`Identity_clone_source.mp3`, 41.27s**, no gap over 0.4s. Step-1 frame: `N_step1_v1.jpg` (job `51db2e7e-77a8-40ab-8c4e-2dbd8caf3d3f`, passed `nano_banana_pro`, logged `nano_banana_2` — §5 routing fault, not model-critical).

**Unverified by ear:** the accent (Tyneside) and texture — the agent measures pitch, the user hears the placement. Media files (`.mp4`, `.mp3`) are git-ignored and delivered in chat.

**Step 6 — HUMAN (the connector has no clone call):** ElevenLabs app → Voices → Instant Voice Clone → upload `Identity_clone_source.mp3` → *Remove background noise* ON → name **Identity** → send the voice ID.
