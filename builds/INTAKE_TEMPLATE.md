# Intake (§18B)

## Default — Drive folder + short message

**1. Make one Google Drive folder** and share it as *Anyone with the link — Viewer*. Put in it:

| File | Name it | Formats |
|---|---|---|
| Inspo video(s) | include `inspo` in the main one's name (e.g. `inspo.mp4`) | .mp4 .mov .webm .m4v |
| Script | include `script` in the name; **title on the first line** | .docx .pdf .txt |
| Product Sheet | include `product` or `sheet` in the name | .docx .pdf .txt |
| Product images | any name | .jpg .png .webp .heic |

Save the script and product sheet as .docx or .pdf (native Google Docs are not tested yet). Don't use a scanned PDF, because the text can't be read from it.

**2. Send this message:**

```
DRIVE: 
LOOM: (optional — your Loom walkthrough for this script)
BUILD: 
MODE: 1 Realistic | 2 3D Pixar | 3 Claymation | 4 Realistic Film | 5 Pixar Film
RUN: MANUAL | AUTOMATION
VOICE: e.g. British, female, 50s, warm and plain-spoken
HOOKS: 3 | in script
CAP: e.g. 3000 Higgsfield, 2000 Kling, 20000 Kie
ADJUST:
- 
- 
FORMAT: 
TOOLS: 
CAST NOTES: 
NOTES: 
```

DRIVE, BUILD and MODE are required. LOOM is optional: set the Loom to "anyone with the link" (a private one can't be downloaded — put its MP4 in the Drive folder with `loom` in the name instead). Everything the Loom asks for, and every visual note written on the script, is followed (§27F, §18C). Leave the rest blank to use the defaults (RUN blank = Manual, HOOKS blank = 3). With RUN: MANUAL the agent still downloads and absorbs everything itself, sends you the absorption (steps 1–2) and waits for your go; then you get the prompts and generate as usual. With CAP filled in, the run never asks about credits. Each ADJUST line is applied and recorded. One that conflicts with the product sheet or product images is flagged, not applied.

---

## Alternative — everything in one message

```
BUILD: 
MODE: 1 Realistic | 2 3D Pixar | 3 Claymation | 4 Realistic Film | 5 Pixar Film
FORMAT: UGC Ad | Short VSL | Long VSL | Narrated B-roll | AI Drama VSL
RUN: MANUAL | AUTOMATION
TOOLS: 
LOOM: (optional)

INSPO:
- 

SCRIPT:
<title on this first line>
<full script>

PRODUCT:
Name: 
What it is: 
Reference images:
- 
(or) SHEET: products/<name>

CAST NOTES: 
NOTES: 
```
