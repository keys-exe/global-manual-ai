# global-manual-ai

This repo runs under the **AI Prompt Engineer — Global Standards** (currently V7.63.0).

- Master file (the only standard): `standards/AI_Prompt_Engineer_Global_Standards.md`
- Project skill that loads it: `.claude/skills/ai-prompt-engineer/SKILL.md` — the **Manual** run mode, always the default
- Automatic run mode: `.claude/skills/ai-prompt-engineer-auto/SKILL.md` — load **only** when the user explicitly says "we will use automation" (Appendix E0)

**At the start of every task, invoke the `ai-prompt-engineer` skill** and follow it. Before writing any deliverable, pull the relevant sections from the master file by grepping their headings (the file is too large to read whole). If this CLAUDE.md, the skill or anything else disagrees with the master file, the master file wins.

Changes to the standards follow §0 and §34: say what will change and which sections before editing; edit the master file; keep the skill's summary in sync in the same commit; bump the version and changelog on a cut.

Product Sheets and Build Sheets (Appendix B / C schemas) go under `products/` and `builds/` respectively. Nothing product-, brand-, character- or location-specific goes into `standards/`.

## Generation Board (standing instruction from the user, 2026-09-26)

Every generation goes on the build's **Generation Board**. Both run modes, every build, no need to ask. **One board per build** (the user's team gets only their build's link), all published from the one template `dashboard/generation_board.html`. The page shows the one build its board holds; there is no build picker and no "new generation" button, so cards are only ever added by you.

| Build | Board |
|---|---|
| `intake-1` (STRYDE · Identity Callout) | https://claude.ai/artifact/HVPuUcnNK1MUrCYnou9UnJ |
| `demo-ad` (example only, placeholder media) | https://claude.ai/artifact/YK4ReHoWRnqBuXQvCMdHLT |

New build: copy the template to your scratchpad, set its `<title>` to the build name, publish it as a new artifact with `capabilities: {db: {}, assets: {}, downloads: true}`, seed `builds/<id>` and its `generations`, and add a row above. To change the design, edit the template and republish it to every board with `url` (keep each board's `<title>`).

- One `builds/<build-id>` doc per build (name, product, mode, format, run, aspect, `folders` = Drive OUTPUT folder IDs from `drive.json`, `balances`, `balancesAt`).
- One `generations/<build-id>__<BEAT>` doc per beat: `build`, `act` (`Hook 1`… for hooks, `Act 1`, `Act 2`… for talking heads and B-roll, set from the step-5 act map), `stage` (`absorption` `cast` `locations` `voice` `hooks` `talking` `broll` `edit`), `beat`, `title`, `line` (verbatim script line), `imagePrompt` / `imageModel` (step 1), `prompt` / `model` (step 2 video, or the only prompt), `duration`, `credits`, `status` (`planned` `ready` `generating` `review` `use` `regenerate`), `imageStatus` (`review` `confirmed` `regenerate`), `fault` / `imageFault` (`Q<n>: fault → fix`), `regens` / `imageRegens`, `imageAsset` / `imageType`, `videoAsset` / `videoType`, and per step the connector record: `imageConnector` / `videoConnector` (Higgsfield, Kling, Kie AI…), `imageUrl` / `videoUrl` (the connector's original link), `imageCredits` / `credits`, `imageRes` (e.g. 1080×1920) / `duration` (s), `imageAt` / `videoAt` (ms); `updatedAt` (ms).
- Generations run through the connectors (§5). The page can't show a connector's CDN link directly, so every result is downloaded and uploaded to the board as an asset; the original link goes in `imageUrl` / `videoUrl`.
- Write with the `ArtifactData` tool (batch when more than two docs). When you write a prompt, add or update its doc (`status: ready`). When a render exists, download it locally, upload it with the Artifact tool (`url` = board, `asset: true`) and store the returned id in `imageAsset` / `videoAsset`. Record the §22V / §22W verdict the same turn.
- Manual run view is grouped by act, in order: Cast, Locations, Voice, **Hook 1, Hook 2…, Act 1, Act 2…**, Edit. Each group shows an **Images** box, then a **Videos** box (cast and locations: images only). A video unlocks once its image is `confirmed`. Each card has **Confirm** and **Fix**. Fix opens "What should be fixed?"; pressing **Confirm & regenerate** sets `imageStatus` / `status` to `regenerate` with the note in `imageFault` / `fault`. When you pick up a `regenerate` card, treat that note as the user's fix request: regenerate with it, upload the new render and set the step back to `review`. When the act map is written, set `act` on every beat.
