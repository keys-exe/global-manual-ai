#!/usr/bin/env python3
"""§21 / §14A (V7.89.0) — stryde-the-impression wardrobe map: per story day and its events, in story order. Writes wardrobe.json.
Outfits that differ from a person's cast sheet go in by an outfit card (OUT-<ID>-<DAY>) plus a face-and-hair crop (HT26), never the sheet."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
rows = json.load(open(HERE / "act_map.json"))["rows"]
SHEET = "the cast-sheet outfit"
DAYS = [
 ("D1", "Sunday lunch in May, then the hall that night", "stated: 'The lunch. Sunday, the table cleared' + 'That night in the hall'",
  {"N": SHEET + ": oatmeal cable-knit cardigan buttoned over a navy round-neck top, mid-grey wool skirt just above the knee, navy loafers",
   "C1": SHEET + ": navy quilted gilet over a pale blue Oxford shirt, tan chinos, brown suede desert boots",
   "C2": SHEET + ": grey marl sweatshirt, dark straight jeans, white canvas trainers, thin gold chain (a navy wool coat on at night)",
   "C3": SHEET + ": dark green half-zip jumper over a white T-shirt, charcoal chinos, brown trainers",
   "C4": SHEET + ": red-and-navy striped long-sleeve T-shirt, navy shorts, white socks, blue Velcro trainers"}),
 ("D2", "the chemist, a weekday in May — the sleeve she buys on Tuesday", "event: the pharmacy ('as of Tuesday')",
  {"N": "navy quilted jacket over a heather-grey crew-neck jumper, charcoal straight trousers, black flat shoes, a brown leather handbag",
   "X1": SHEET + ": navy short-sleeved pharmacy tunic over a white long-sleeve top, black trousers, black trainers, navy hijab"}),
 ("D3", "Emma finds the drawer, a few days later", "stated: 'Emma finds the drawer: twenty-four, as of Tuesday'",
  {"N": "sage-green cardigan over a cream blouse, grey trousers, navy slippers",
   "C2": "navy zip-up fleece over a white T-shirt, dark jeans, white canvas trainers"}),
 ("D4", "July, 8:40 — she tries the hill alone", "stated: 'July, 8:40, Hazel tries the hill alone'",
  {"N": "stone-coloured lightweight mac over a pale blue blouse, navy trousers over number twenty-four, black flat walking shoes",
   "X2": SHEET + ": faded denim jacket over a white T-shirt, black leggings, grey trainers, cross-body bag; pushing a navy buggy with a toddler"}),
 ("D5", "Roy's plan for the car, and that evening on the stairs", "stated: 'Roy has spoken to Emma' + 'Later, silent: Roy comes down the stairs'",
  {"N": "lilac crew-neck jumper, grey trousers, navy slippers",
   "C1": "grey wool cardigan over a blue checked shirt, tan chinos, brown slippers"}),
 ("D6", "last week of term: pick-up at the gate, Wendy, then the price that night", "stated: 'Last week of term, Hazel in Emma's car at pick-up' + 'Night, the kitchen, the phone'",
  {"N": "soft blue cotton shirt, navy trousers, black flat shoes (reading glasses at night)",
   "C1": "navy V-neck jumper over a white shirt, tan chinos, brown slippers",
   "C5": SHEET + ": cobalt-blue cotton mac open over a navy-and-white spotted shirt dress just below the knee, black walking shoes, a canvas bag",
   "X3": SHEET + ": long fluorescent yellow-green hi-vis coat, white peaked cap, black trousers, black lace-ups, round tortoiseshell glasses",
   "X4": "two grandchildren, a girl of 8 and a boy of 6, in white polo shirts, plain red school sweatshirts with no badge and grey school shorts / a grey pinafore"}),
 ("D7", "the first morning with the strap", "stated: 'The stairs. Morning.'",
  {"N": "a pale cotton nightdress to just above the knee while she puts the strap on (bedroom), then navy cotton trousers and a cream blouse pulled on over it (the stairs)",
   "C1": "brown wool dressing gown over blue striped pyjamas, brown slippers"}),
 ("D8", "August on the hill — past the postbox", "stated: 'August, the hill, the postbox goes by'",
  {"N": "light green linen shirt, cream cotton trousers, white trainers",
   "X2": "white vest top, khaki shorts, grey trainers, sunglasses pushed up on her head; the same navy buggy"}),
 ("D9", "end of August — the second hall film", "stated: 'End of August, the hall: Emma films again'",
  {"N": "honey-yellow cardigan over a white T-shirt, cream trousers, tan flat shoes",
   "C2": "navy-and-white Breton striped top, dark jeans, white canvas trainers"}),
 ("D10", "early September evening — Roy, the hall", "stated: 'Early September, the hall'",
  {"N": "soft green cardigan over a white blouse, navy trousers, tan flat shoes",
   "C1": SHEET + ": navy quilted gilet over a pale blue Oxford shirt, tan chinos, brown suede desert boots"}),
 ("D11", "the first day of school, 8:40 — the hill, the gate, and Hazel to camera", "stated: 'The first day. 8:40, the hill'",
  {"N": "camel wool coat open over a cream crew-neck jumper, navy trousers, black flat shoes",
   "C4": "school uniform: white polo shirt, plain red school jumper with no badge, grey shorts, grey socks, black school shoes, a plain red book bag",
   "C2": "navy wool coat over a grey jumper (seen in the car)",
   "C3": SHEET + ": dark green half-zip jumper over a white T-shirt (seen in the car)"}),
]
days = []
for d, event, source, outfits in DAYS:
    evs = {}
    for r in rows:
        if r["story_day"] == d:
            evs.setdefault(r["scene"], {"id": f"{d}-{r['scene']}", "location": r["location"], "visibility": "CONCEALED", "beats": []})["beats"].append(r["beat"])
            if r.get("product_beat"): evs[r["scene"]]["visibility"] = "REVEAL"
    worn = {c for r in rows if r["story_day"] == d for c in r["cast"]}
    miss = worn - set(outfits)
    assert not miss, (d, miss)
    days.append({"day": d, "event": event, "source": source, "outfits": outfits, "events": list(evs.values())})
names = {"N": "Hazel", "C1": "Roy", "C2": "Emma", "C3": "Dan", "C4": "Oscar", "C5": "Wendy", "X1": "Assistant", "X2": "Mum (buggy)", "X3": "Lollipop lady", "X4": "Wendy's grandchildren"}
json.dump({"days": days, "talking_heads": [], "names": names}, open(HERE / "wardrobe.json", "w"), indent=1, ensure_ascii=False)
cards = [(d, k) for d, _, _, o in DAYS for k, v in o.items() if not v.startswith(SHEET)]
print(len(days), "days ·", len(cards), "outfit cards needed (outfit ≠ sheet):", ", ".join(f"OUT-{k}-{d}" for d, k in cards))
