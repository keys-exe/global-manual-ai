# global-manual-ai

This repo runs under the **AI Prompt Engineer — Global Standards** (currently V7.60.9).

- Master file (the only standard): `standards/AI_Prompt_Engineer_Global_Standards.md`
- Project skill that loads it: `.claude/skills/ai-prompt-engineer/SKILL.md` — the **Manual** run mode, always the default
- Automatic run mode: `.claude/skills/ai-prompt-engineer-auto/SKILL.md` — load **only** when the user explicitly says "we will use automation" (Appendix E0)

**At the start of every task, invoke the `ai-prompt-engineer` skill** and follow it. Before writing any deliverable, pull the relevant sections from the master file by grepping their headings (the file is too large to read whole). If this CLAUDE.md, the skill or anything else disagrees with the master file, the master file wins.

Changes to the standards follow §0 and §34: say what will change and which sections before editing; edit the master file; keep the skill's summary in sync in the same commit; bump the version and changelog on a cut.

Product Sheets and Build Sheets (Appendix B / C schemas) go under `products/` and `builds/` respectively. Nothing product-, brand-, character- or location-specific goes into `standards/`.
