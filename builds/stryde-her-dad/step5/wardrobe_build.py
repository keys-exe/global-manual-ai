import json, pathlib
rows = json.load(open("act_map.json"))
DAYS = [
 ("D1", "Saturday at the garden centre — the van, then the car", "event: the near miss at the garden centre (L001–L015; story: 'The car park… The car.')",
  {"C1": "a charcoal crew-neck sweatshirt, faded navy work trousers (long — his knees covered), tan leather work boots",
   "C2": "a navy quilted jacket open over a white T-shirt, light-wash straight jeans, white trainers",
   "C4": "garden-centre uniform: plain bottle-green polo shirt and dark-green zip fleece with no logo, black work trousers, black trainers"}),
 ("D2", "a weekday at rock bottom — the drawer, his stairs sideways, waiting in the car", "stated: 'now he comes down his own stairs sideways'; 'Now I wait in the car while she loads the boot' (L016–L017)",
  {"C1": "an olive work sweatshirt, grey work trousers (long), tan work boots",
   "C2": "a burgundy rain jacket, black jeans, grey trainers (seen at the boot through the rear window)"}),
 ("D3", "the GP appointment", "event: 'The GP says it's wear and tear' (L018–L022)",
  {"C1": "a navy zip fleece over a grey T-shirt, dark jeans, brown leather shoes",
   "C5": "her work clothes: a navy fine-knit cardigan over a pale-blue blouse, charcoal trousers, black flat shoes (her sheet's outfit — a doctor's day wear)"}),
 ("D4", "the builders' yard — Gary", "event: 'At the builders' yard, Gary, 70, is lifting slabs on his own' (L023–L043)",
  {"C1": "a grey marl hoodie, khaki canvas work shorts above the knee (both knees bare — he presses the spot), grey socks, tan work boots",
   "C3": "a sand-coloured canvas work jacket open over a faded black T-shirt, navy work shorts above the knee (the strap on his bare right knee), rolled grey socks, brown rigger boots"}),
 ("D5", "the evening the strap arrives — Sue finds it", "event: 'Sue finds the strap' (L044–L047)",
  {"C1": "a navy T-shirt, grey jogging bottoms, socks",
   "C2": "a grey marl lounge jumper, black leggings, sheepskin slippers"}),
 ("D6", "the first day forwards — the stairs, the yard, the street", "stated: 'First time in two years, I came down my own stairs forwards' (L048–L051)",
  {"C1": "a sky-blue T-shirt under an open grey zip fleece, black work shorts above the knee (the strap on his bare right knee), grey socks, tan work boots",
   "X2": "the labourer, 30s: a dusty grey hoodie, black work trousers, rigger boots",
   "X3": "the neighbour, an older woman: a pink fleece, navy trousers, slippers"}),
 ("D7", "laying their new patio", "event: 'Sue finds him on his knees in the garden, laying their new patio' (L052–L053, L058)",
  {"C1": "a white T-shirt, stone-coloured work shorts above the knee (the strap on his bare right knee), tan work boots",
   "C2": "a soft blue linen shirt, white jeans, tan sandals"}),
 ("D8", "the same car park, weeks later", "stated: 'Same car park, weeks later' (L054–L057)",
  {"C1": "a short-sleeved brick-and-cream checked shirt, khaki shorts above the knee (the strap on his bare right knee), tan boots",
   "C2": "a cream knit cardigan over a rust T-shirt, dark jeans, white trainers",
   "C4": "the same garden-centre uniform as D1"}),
 ("D9", "an ordinary day — under his trousers", "contrast: the offer's 'It goes on under your trousers and nobody knows it's there' (L060)",
  {"C1": "dark jeans, a navy canvas jacket, brown boots — the strap hidden under the jeans"}),
]
NAMES = {"C1": "Tony", "C2": "Sue", "C3": "Gary", "C4": "The lad", "C5": "GP", "X2": "Labourer", "X3": "Neighbour"}
days = []
for did, ev, src, outfits in DAYS:
    events, cur = [], None
    for r in rows:
        if r["story_day"] != did: continue
        if not cur or cur["location"] != r["location"]:
            cur = {"id": f"{did}-E{len(events)+1}", "location": r["location"], "visibility": "VISIBLE", "beats": []}; events.append(cur)
        cur["beats"].append(r["beat"])
    days.append({"day": did, "event": ev, "source": src, "outfits": outfits, "events": events})
json.dump({"days": days, "talking_heads": [], "names": NAMES}, open("wardrobe.json", "w"), indent=1, ensure_ascii=False)
print(len(days))
