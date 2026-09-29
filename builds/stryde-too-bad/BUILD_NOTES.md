# stryde-too-bad — BUILD NOTES

- **Task:** A - VID | Short VSL | TOF | Objection First | Iteration | Too Bad
- **Drive:** `1sRxZ8thrNmqmo1hVO3MJxY_-dCHGlsxE`
- **Run:** Manual (user, 2026-09-29: "RUN MANUAL. BRITISH").
- **Mode:** 1 Photorealistic (§44 default; no MODE given). Format: Short VSL (script title).
- **Voice:** British accent (user + script note "keep British Accent on Eleven Labs"), a different voice from the original.
- **Script note (layer 4, whole build):** different voice, B-rolls and editing from the original; about 50% Black people in the B-roll; music.

## Intake (2026-09-29)
- Script `Untitled document.docx` (inferred as script, title on line 1 ✓). **Two ads, each with its own body:**
  HK A "TooSmall" + body A · HK B "Gimmick" + body B. Hook visuals: "Editor's call" (VN01, VN02).
- Product Sheet in the folder is V7.49.29; the repo `products/stryde/` is V7.49.37 → the repo copy stays in use.
- Product images: the standard 10 (`front`, `back`, `product_tq_left/right`, `product_side`, `product_macro`, `worn_front/bent/rear`, `package_open`).
- **Inspo MISSING:** the only reference is `https://www.facebook.com/ads/library/?id=1620934502990537`, which returns HTTP 403 (Facebook's client challenge) from the cloud. Asked the user for the MP4 in the Drive folder (named `inspo`).
- `script_lines.py` misreads this layout: it treats the header note, the `TooSmall`/`Gimmick` labels and the `Body:` prefix as spoken. The voiced text = only the quoted hook lines and the body text after `Body:`, verbatim.

## Open
- Inspo file → then steps 1–3 (absorption, product sheet check, ledger, Mode & Model Lock, avatars) and the four boards.
