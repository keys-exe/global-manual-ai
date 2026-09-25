# EDIT-DFA — edit grammar read off the inspo (§42 Part 3A)

Source: `intake/inspo.mp4` (142s, 40 shots), shot frames `intake/frames/inspo/S01…S40`, per-second sheets `sheet_01…05`.
Style axis: wins over house defaults, never over compliance.

| ID | Device | Reading from the inspo | Our execution | Carried by |
|---|---|---|---|---|
| EG01 | Base track | Doctor talking head, seated/standing in clinic, centred, face at ~1/3 height | TH-BODY / TH-HK1-3 as base, `th_focus_y` 0.33 | assemble.py |
| EG02 | B-roll PiP over TH | B-roll box bottom-right, ~45% width, thin white border (S01, S04) | `pip` over `th`, corner br, scale 0.45, border 6 | assemble.py |
| EG03 | Doctor cutout over B-roll | Cut-out doctor, bottom-left, ~1/3 width, over full-frame B-roll (S08, S14) | `pip` over `broll`, corner bl, scale 0.33, border 0 (box, not a matte cutout) | assemble.py; true cutout = CapCut remove-background on the box (optional) |
| EG04 | Split band | B-roll fills the lower band, doctor above (S28) | `split`, broll bottom, ratio 0.45 (mechanism beats) | assemble.py |
| EG05 | Full-frame product | Product hero full frame (S39) | `full` on BR16, BR18, BR27 | assemble.py |
| EG06 | Captions | One word at a time, black text in a white rounded pill, centred horizontally, mid-frame | Word-by-word auto captions, white pill, black bold sans | CapCut |
| EG07 | List card | Handwritten white card, items struck through with red X (S34) | "Without…" card (HK1), "sleeve / brace / gel" card (body) | CapCut |
| EG08 | Badge | Gold "60 DAYS MONEY BACK GUARANTEE" seal, top-right over product (S39) | 60-day badge on BR27 | CapCut |
| EG09 | Punch-ins | None measured — the inspo holds the TH framing | none | — |
| EG10 | Transitions | Hard cuts only | hard cuts | assemble.py |
