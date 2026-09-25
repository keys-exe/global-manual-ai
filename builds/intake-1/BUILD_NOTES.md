# Build notes — intake-1 (STRYDE · Identity Callout)

Decisions made in session_01BQXq8gzSUiosctGYAGnASj, 2026-09-25. Read this first when resuming.

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1kvwwMSj8YLBtpOl3TAgfjPfDDNha653q
  (parent → STRYDE → "C - VID | AI VO | TOF | Identity Callout | New | A Must For")
- Re-fetch inputs: `python3 .claude/skills/ai-prompt-engineer/scripts/fetch_drive.py intake-1 <link above>`
- Contents: 1 inspo video (46.3s, 9:16, 22 shots, 2.1s mean shot), script `IDENTITY CALLOUT - A MUST FOR.docx`
  (12 spoken lines, 176 words — extracted to `work/script.lines.txt`), product sheet
  `stryde_product_sheet_v7_49_13.py`, 7 product images.
- Drive OUTPUT tree already created — IDs in `drive.json`. Reuse, never duplicate.

## User's answers
| Question | Answer |
|---|---|
| Mode | **Mode 1 Realistic** |
| Format | **Match the inspo** (§42). The inspo is a narrated, all-B-roll product ad with no talking head → expect a voice-only build: every frame B-roll (§30H rule 4) |
| Hooks | Script's Hooks section is empty → **agent writes them**, 3 hooks (§30H), each approved at step 6 |
| Run | **AUTOMATION** |
| Voice / accent | not yet given — ask in the intake message (`VOICE`) or use the §22D derivation |
| Credit cap | not yet given — needed before the first paid call (`CAP`) |

## Balances at 2026-09-25
Higgsfield 23,725 · Kling 13,677 · Kie 153,049 · HeyGen 11,573 premium.

## Open before running
- `ELEVENLABS_API_KEY` was added to the GLOBAL CLOUD environment after this session started; verify in the new
  session, then write + test the clone script and remove the manual clone stop (§22U step 6, E0).
- Nothing generated yet; no credits spent.
