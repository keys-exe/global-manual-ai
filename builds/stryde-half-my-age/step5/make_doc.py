import json, pathlib
H = pathlib.Path(__file__).parent
rows = json.load(open(H/"act_map.json"))
lines = {f"L{r['n']:03d}": r for r in json.load(open(H.parent/"work/lines.json"))["lines"]}
out = []
W = out.append
W("""# Steps 4–5 — stryde-half-my-age (Mode 4 film, Manual)

Built against the confirmed avatars and absorption (user 2026-09-30: "CONFIRMED ALL PROCEED"). Plates are on the Current board as To check. Flags from steps 1–3 run on my recommendations until you say otherwise (right knee; Hook E = she gets up off the floor; "Three weeks" voiced as written; the café trouser-leg reveal kept, strap shown in its own insert).

## 4. Property and location maps (§30G, §30C)

### Property Sheet — P-HOUSE (her house)

| # | Field | Value |
|---|---|---|
| 1 | Type and era | 1930s red-brick semi-detached in a northern English town; the same couple forty years |
| 2 | Shell | magnolia emulsion over uneven old plaster (dado rail in the hall) · tall moulded skirting, white gloss gone yellow · moulded white architraves · white three-panel 1930s doors, worn brass levers · white ceilings, small plaster roses · worn oatmeal wool carpet through hall, stairs (brass stair rods), landing, bedrooms, living room → brown-and-cream patterned vinyl at the kitchen threshold · white steel panel radiators under windows · white plastic rocker switches, yellowed |
| 3 | Floor map | front door (north) → hall; stairs rise along the hall's left wall, 13 steps, banister on the open right side, to a small landing; living room front right off the hall; kitchen at the back (end of the hall); upstairs the back bedroom opens off the landing on the right |
| 4 | Orientation | front (hall door glass, living-room bay) faces **north** — cool soft daylight; kitchen and back bedroom face **south-west** — warm afternoon sun; landing lit by a frosted side window |
| 5 | Carried elements | the dark-varnished banister and newel post · brass stair rods · the framed family photographs up the stair wall · the telephone table and brass barometer at the foot of the stairs · the oatmeal carpet |
| 6 | Exterior | red-brick semi with a bay, privet hedge and low brick wall to the street, identical semis opposite; back garden lawn, washing line, brown fence, shed |
| 7 | Standing negatives | (none observed yet) |

### Location Sheets

| ID | Tier | Beats | Owner | Anchors (restated in every shot) | Light profile | Plate |
|---|---|---|---|---|---|---|
| P-HOUSE (hall) | PLATED (property plate) | SC13 door, SC02/SC07 foot of stairs | HER | stairs up the left wall, banister right, photos up the wall, telephone table + barometer, living-room doorway right | north door glass, cool 6500K day; hall pendant 2800K at night | v1 To check |
| L-STAIRS | PLATED | SC02, SC03, SC07, SC13 (13 shots) | HER | banister + top newel post, brass stair rods, photos up the left wall, frosted landing window | frosted landing window (east), soft; landing lamp 2800K at night | v1 To check |
| L-KITCHEN | PLATED | SC03, SC05, SC06, SC08, SC10, SC13 (17 shots) | HER | pine table + four ladder-back chairs by the left window, sage-green cupboards, white sink under the back window with the spider plant, cream fridge | SW windows, warm afternoon sun; soft cool morning | v1 To check |
| L-BEDROOM | PLATED | SC02, SC03, SC10 (7 shots) | HER | dark-wood chest of drawers under the window (bottom drawer not quite shut), green candlewick bedspread, walnut wardrobe, pleated bedside lamp | SW window through nets; bedside lamp 2800K at night | v1 To check |
| L-LIVING | PLATED | HKE, SC11 (7 shots) | HER | brown leather armchair by the fire, tiled 1930s fireplace + mantel, floral sofa, bay with green velvet curtains | north bay, cool soft day | v1 To check |
| L-STATION | PLATED | HKA (3) | GENERIC | sandstone steps + black iron centre rail, green-and-cream columns, glass canopy, train with doors open | overcast canopy 6500K | v1 To check |
| L-CARRIAGE | PLATED | HKA (2) | GENERIC | blue moquette facing seats, grey tables, yellow grab poles | windows, overcast | v1 To check |
| L-ESCALATOR | PLATED | HKC (5) | GENERIC | stopped escalator with yellow barrier, fixed stairs beside with steel rails, glass roof | glass roof 6000K | v1 To check |
| L-SHOPCENTRE | PLATED | HKB (5) | GENERIC | glass lift left, wide tiled stairs with chrome rails, gallery rail, skylight | skylight 5600K | v1 To check |
| L-WEDDING | PLATED | SC04 (5) | GENERIC | parquet dance floor, looped fairy lights, white round tables with candle jars, stage at the back | practicals 2700K, 4:1 | v1 To check |
| L-SHOP | PLATED | SC10 (3) | GENERIC | conveyor checkout + till, chrome queue rail, rack by the lane | shop light + glass front 4500K | v1 To check |
| L-CAFE | PLATED | SC12 (9) | GENERIC | round window table + bentwood chairs, counter with glass cake display, exposed brick wall, warm pendants | front window 4800K | v1 To check |
| L-HIGHST | TRAVERSED | SC10 (2) | GENERIC | landmark carried: the red post box and the row of shopfronts; `GEO-LINE` left→right | late-morning sun | no plate (§30C 1a) |
| L-PHYSIO | INCIDENTAL | SC03 (2) | GENERIC | — | clinic blinds 5600K | info card at step 7 |
| L-CLINIC / L-GOLF / L-TENNIS | INCIDENTAL | SC09 (1 each) | one-offs | — | daylight | info cards at step 7 |

**Set checks:** S1 tiers above · S2 daylight except SC02 night, SC03 evening (lamp in frame) and the wedding · S3 profiles follow the orientation (north front cool, south-west back warm) · S4 consecutive scenes change room except SC05→SC06→SC07→SC08 (one continuous morning — declared CONTINUOUS joins, not act boundaries). **The set closes here.**

## 5. Act map, Scene Bibles and wardrobe map

**`angles.py` PASS** — 89 shots (`step5/act_map.json`): setups eye/¾ ×19, eye/OTS ×11, low/¾ ×10, eye/profile ×9…; no signature shots; one mirror pair (SC02-SH03 → SC07-SH02, same high angle behind her: backwards then forwards).

### Story spine (§24I part 9)
Want: her life back (stairs, town, Sundays not planned around one level) · Stakes: the family waiting for her; staying upstairs · Obstacle: the knee · Failed fixes: brace, physio, pills, injections, the drawer · Turn: Barbara (bone on bone, dancing) → the strap → the first step forwards · Payoff: town, queue, bags, "I know", the café, the sister on the stairs · Plants: the drawer (SC03 → gone in SC10), the sister's one-level Sundays (SC03 → SC13), backwards (SC02) → forwards (SC07).

### Scene Bibles
""")
SCN = [
 ("HKA","Hook A — station stairs","HA (After)","L-STATION → L-CARRIAGE","late morning, overcast 6500K","HER (forest-green coat), Daughter (olive parka)","top of the stairs → platform, daughter above/behind, HER below; carriage: facing seats across the table","her shopping bag: in her right hand → on her lap","cold open: the result, witnessed","Daughter: rushing → winded, amazed · HER: brisk → settled, private smile (subtext: I know)","MUS-HK (sparse pulse, drops for 'When did that happen?')","station hubbub, train doors; carriage hum","SFX-TRAIN-DOORS"),
 ("HKB","Hook B — the lift queue","HB (After)","L-SHOPCENTRE","afternoon, skylight 5600K","HER (navy quilted jacket), Daughter (charcoal coat)","lift left, stairs right; HER climbing, daughter at the lift then the top","bags: two in HER hands throughout; daughter's bags sag","cold open","Daughter: reasonable → out of breath · HER: amused → unbothered","MUS-HK","atrium murmur","—"),
 ("HKC","Hook C — the dead escalator","HC (After)","L-ESCALATOR","morning rush, glass roof 6000K","HER (burgundy raincoat), Daughter (black puffer + coffee), Commuter (one-off)","foot of the stairs; HER passes the commuter frame left→right and climbs","daughter's coffee cup: in hand throughout","cold open","Commuter: fed up · HER: breezy → at the top, looking back · Daughter: stunned","MUS-HK","concourse ambience","SFX-TANNOY (voice, off)"),
 ("HKE","Hook E — the floor","HE (After)","L-LIVING","afternoon, bay 5600K","HER (oatmeal cardigan, grey trousers), Daughter (denim jacket, grey hoodie)","HER kneeling mid-room on the rug, daughter enters from the hall doorway (frame right)","jigsaw box: on the floor → in HER hands → on the mantel","cold open (VO variant)","Daughter: reflex care → hand frozen mid-air · HER: busy → a small look","MUS-HK","living-room quiet, clock","—"),
 ("SC02","Rock bottom","B1 evening → B2 morning → B2 afternoon","L-STAIRS · L-BEDROOM","night: hall pendant + landing lamp 2800K; morning: frosted window 6500K","HER (B1: green jumper, charcoal skirt; B2: blue quilted dressing gown, slippers), Husband (brown cardigan, checked shirt)","landing above, hall below: HER stays up, he stays down (the axis is the stairs)","shopping bags: by the bottom step → in his hands; mug of tea: his hand → hers","Before — the low point","HER: covering → alone · Husband: helping too quickly (subtext: he's scared for her)","MUS-SC02 (sparse, single piano notes)","house at night; morning quiet","SFX-BAGS-LIFT"),
 ("SC03","Tried everything + the Sunday plant","B3 (montage days) → B3d evening","L-STAIRS · L-PHYSIO · L-KITCHEN · L-BEDROOM","landing lamp 2800K; clinic 5600K; kitchen cold morning 6500K; bedside lamp 2800K","HER (B3: slate cardigan, cream blouse, navy knee skirt; B3d: same), Husband, Sister (voice only)","HER at the chest of drawers, back to the door; husband in the doorway","brace: on her shin → round the ankle → into the drawer; drawer: open → pushed shut, still proud; phone: rings → in her lap","Problem — the failed fixes; the plant (one-level Sundays)","HER: tired → resigned · Husband: soft worry","MUS-SC02 continues sparser","bedroom tone","SFX-DRAWER-SHUT, SFX-PHONE-RING"),
 ("SC04","The wedding","B4 June evening","L-WEDDING","fairy lights and candles 2700K, 4:1","HER (dusty-rose dress, cream jacket), Husband (navy suit, blue shirt, tie), Barbara (royal-blue dress, silver cardigan), bride (one-off)","dance floor centre, their table at the edge; HER faces the floor, he is at her left","his pint: in hand","Turn begins — Barbara seen","HER: watchful → quietly shaken · Husband: distracted","MUS-SC04 (the room's party music is not generated — our cue is warm, low)","reception murmur","—"),
 ("SC05","Barbara comes to stay","B5 morning","L-KITCHEN","soft morning 5600K from the left windows","HER (sage cardigan, charcoal skirt above the knee), Barbara (sheet outfit: cobalt gilet, white top, navy knee-length shorts)","facing each other across the pine table, window on frame left","routine (pills, gel, brace, ice pack on right knee) on the table; strap: on Barbara's knee; box: laid on the table","Turn — the reveal","HER: routine → sceptical · Barbara: watching → decided (subtext: I've been you)","MUS-SC05 (theme's first notes)","kitchen, radio off","SFX-BOX-ON-TABLE"),
 ("SC06","The sceptic","B5 (continuous)","L-KITCHEN","same","same","same","strap: in HER palm","Turn — objection","HER: disbelief · Barbara: certain","MUS-SC05","same","—"),
 ("SC07","The test","B5 (continuous)","L-STAIRS","frosted landing window, morning 5600K — the light opens","HER (same), Barbara (same)","top of the stairs → foot; Barbara in the hall below; mirror of SC02-SH03","strap: in hand → seated below the right kneecap; banister: untouched","Turn — the first step forwards (the film's pivot)","HER: braced → released, breath caught · Barbara: quiet pride","MUS-SC07 (the full theme)","hall quiet","—"),
 ("SC08","The mechanism, from Barbara","B5 (continuous)","L-KITCHEN","same morning","same","back at the table","box: beside Barbara's hand","Turn — why it works (claims F2 voiced as written)","HER: taking it in · Barbara: teaching","MUS-SC05 low","kitchen","—"),
 ("SC09","Proof in the family","A1 (one-offs)","L-CLINIC · L-GOLF · L-TENNIS","clear daylight","one-offs: sports-medicine doctor + patient, Barbara's husband (76), niece (22)","—","strap worn in each","After — proof","—","MUS-AF (theme, fuller)","location beds","—"),
 ("SC10","Six weeks","A2","L-BEDROOM · L-KITCHEN · L-HIGHST · L-SHOP","warm morning 5000K; town midday 5600K; shop 4500K","HER (camel trench, cream jumper, navy trousers, white trainers), Cashier (one-off)","high street left→right (GEO-LINE); shop queue facing the till","strap: on → under the trouser leg; table: just a mug (mirror of the pills); two bags: from the cashier → in her hands → up her street","After — the life back","HER: easy, brisk → proud","MUS-AF","high street, shop","—"),
 ("SC11","The husband","A2 afternoon","L-LIVING","bay 5000K","HER (same), Husband (brown cardigan, plain grey shirt)","he in the armchair by the fire, she in the doorway","two bags: at her feet; his newspaper","After — the loop with him","Husband: noticing · HER: 'I know' (subtext: yes, I was gone — and I'm back)","MUS-AF drops out","living-room quiet","—"),
 ("SC12","The café + reveal","A3","L-CAFE","front window, honeyed 4800K","HER (terracotta jumper, navy wide-leg trousers, tan loafers), Friend 1 (sheet), Friend 2 (sheet)","window table; HER crosses from the door frame right→left to the table","cups; strap: under the trouser hem → on the table (insert)","After — the reveal + the name","Friends: curious → teasing → won over · HER: relaxed","MUS-AF","café murmur, cups","—"),
 ("SC13","The offer, planted in the story","A4 Sunday","L-KITCHEN · P-HOUSE (hall) · L-STAIRS","warm afternoon 5000K","HER (cream cardigan, coral blouse, oatmeal trousers), Sister (sheet: lilac fleece)","kitchen table → front door (north, cool daylight behind the sister) → foot of the stairs","box with two straps; the banister","Close — the plant paid","Sister: hopeful, nervous → first step · HER: sure","MUS-OC (theme resolves)","hall","SFX-DOORBELL (VN23)"),
]
W("| Scene | Title | Story day | Location | Time · light (K) | Cast · wardrobe | Blocking / axis | Props (start → end) | Spine beat | Emotion map (entry → exit · subtext) | Music | Room tone | SFX |")
W("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for s in SCN: W("| " + " | ".join(s) + " |")
W("""
**Transitions:** hooks → SC02 on a CUT with the VO time jump ("Six weeks ago"); SC02→SC03 TIME CUT (same house, later days); SC04→SC05 CUT ("the week after"); SC05→SC06→SC07→SC08 CONTINUOUS (one morning, one outfit); SC08→SC09 CUT (VO proof); SC09→SC10 TIME CUT (six weeks); SC10→SC11 CONTINUOUS (she walks in with the bags); SC11→SC12 CUT; SC12→SC13 CUT, then the doorbell (VN23, no card).

### Wardrobe map (§14A, §21) — one outfit per story day

| Day | HER | Daughter | Husband | Barbara | Others |
|---|---|---|---|---|---|
| HA | forest-green wool coat, grey trousers, black ankle boots, tan shoulder bag | olive parka, cream jumper, jeans (sheet) | — | — | — |
| HB | navy quilted jacket, cream jumper, dark jeans, white trainers | charcoal wool coat, jeans, ankle boots | — | — | — |
| HC | burgundy raincoat, black trousers, black trainers | black puffer jacket, jeans | — | — | Commuter: grey hoodie, black backpack |
| HE | oatmeal cardigan over a teal top, grey trousers | denim jacket over a grey hoodie, jeans | — | — | — |
| B1 | heather-green jumper, charcoal A-line skirt (sheet) | — | brown cardigan, checked shirt (sheet) | — | — |
| B2 | pale-blue quilted dressing gown, grey nightdress, slippers | — | same as B1 | — | — |
| B3 | slate-grey cardigan, cream blouse, navy knee-length skirt | — | bottle-green crew-neck jumper, pale-blue oxford shirt, charcoal cords (user Fix 2026-10-01: not the Scene 2 outfit) | — | Sister: voice only |
| B4 | dusty-rose dress, cream jacket | — | navy suit, pale-blue shirt, tie | royal-blue dress, silver cardigan | bride in white |
| B5 | sage-green button cardigan, white blouse, charcoal skirt above the knee | — | — | cobalt gilet, white top, navy knee-length shorts (sheet) | — |
| A2 | camel trench, cream jumper, navy trousers, white trainers | — | brown cardigan, plain grey shirt | — | Cashier: supermarket polo |
| A3 | terracotta jumper, navy wide-leg trousers, tan loafers | — | — | — | Friends 1 and 2: sheet outfits |
| A4 | cream cardigan, coral blouse, oatmeal trousers | — | — | — | Sister: lilac fleece, floral blouse (sheet) |

Outfits that differ from a character's sheet go into the scene's ingredients as an **outfit info card** (one per character per day, `kind: info`), made with the scene's other ingredients at step 6/7.

### Visual Instruction Ledger — assigned

| VN | Carried by | Status |
|---|---|---|
| VN01 | HKA-SH01 | assigned |
| VN02 | HKA-SH01, HKA-SH02 | assigned |
| VN03 | HKA-SH04 | assigned |
| VN04 | HKB-SH01 | assigned |
| VN05 | HKB-SH02 | assigned |
| VN06 | HKB-SH04 | assigned |
| VN07 | HKC-SH01 — tannoy voice off-screen (VOICE-X1), not a picture | assigned |
| VN08 | HKC-SH01 (one-off commuter) | assigned |
| VN09 | HKC-SH02 | assigned |
| VN10 | HKC-SH04 | assigned |
| VN11 | HKE-SH02 | assigned (F8 read) |
| VN12 | HKE-SH05 (VO variant) | assigned |
| VN13 | SC02-SH01 | assigned |
| VN14 | SC02-SH02 | assigned |
| VN15 | SC03-SH06 (VO lands on the drawer closing) | assigned |
| VN16 | SC03-SH07 | assigned |
| VN17 | SC03-SH09 (sister's voice through the phone) | assigned |
| VN18 | SC04-SH03, SC04-SH05 | assigned |
| VN19 | SC05-SH06 | assigned |
| VN20 | SC08-SH02 | assigned |
| VN21 | SC10-SH05 | assigned |
| VN22 | SC12-SH05 | assigned (F10) |
| VN23 | SC13-SH02 → SC13-SH03 cut on the doorbell SFX, no card | assigned |
| VN24 | SC13-SH03 | assigned |
| VN25 | SC13-SH05 | assigned |
| VN26 | HKB (up the stairs, with shopping) | assigned |

### Ingredient ledger — made before the scene's clips (Seedance, no frames — V7.68.0)

| ID | Kind | Fact / content | Scenes |
|---|---|---|---|
| N, C1–C6 | character | the confirmed sheets | all |
| VOICE-N, -C1…-C6, -X1…-X3 | voice | §24I voice masters (next stage) | every speaking shot |
| P-HOUSE, L-* | location | the plates above | per scene |
| PROD-FRONT | product | `stryde_refs/front.webp` (+ `product_tq_left.jpg` at ¾) | every product beat |
| PROD-BOX | product | `stryde_refs/package_open.jpg` — two straps in the open box | SC05-SH06, SC13-SH01 |
| INFO-PLACEMENT | info | the strap sits on the patellar tendon, just below the kneecap, centred, right knee (FP03) | SC05, SC07, SC08, SC09, SC10, SC12 |
| INFO-BRACE | info | a bulky black hinged knee brace with metal side hinges (generic, no brand) | SC03 |
| INFO-DRAWER | info | the bottom drawer crammed with braces, sleeves and supports | SC03 |
| INFO-PHYSIO | info | a physiotherapy room: couch, blinds, a gloved clinician | SC03 |
| INFO-WEDDING | info | the bride in a simple ivory dress, 20s (one-off) | SC04 |
| INFO-HIGHST | info | a northern high street: stone shopfronts, red post box | SC10 |
| P-HOUSE-EXT | location | her street and front door (red-brick semis, privet hedge) | SC10-SH07 |
| OUT-<CHAR>-<DAY> | info | outfit cards per the wardrobe map | per scene |

### Act map (E4) — 89 shots
""")
W("| Beat | Scene | Line | Shot · angle · scale | Action (one, at a pace) | Rig | Focus | Light (K) | Day | Cut cue | Ingredients |")
W("|---|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    shot = r["shot"] if isinstance(r["shot"], str) else " + ".join(r["shot"])
    W(f"| {r['beat']} | {r['group']} | {r['lines'] or '—'} | {shot} · {r['height']}/{r['side']} · {r['scale']} | {r['action']} ({r['pace']}) | {r['rig']} | {r['focus']['plane']}, {r['focus']['dof']} | {r['light']['source']} {r['light']['kelvin']}K | {r['story_day']} | {r['cut']} | {', '.join(r['ingredients'])} |")
W("""
**Durations** are set after the voice masters (E6: each shot as long as its lines at the master's pace); film clips are never trimmed (§24L).
""")
(H.parent/"STEP4_5.md").write_text("\n".join(out))
print(len("\n".join(out)))
