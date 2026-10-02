import json
K = ["stop", "line", "feel", "specific", "fresh", "makeable"]
def sc(s): return dict(zip(K, map(int, s)))
def row(beat, line, cands, hero=False):
    return {"beat": beat, "line": line, "candidates": [{"route": r, "picture": p, "score": sc(s)} for r, p, s in cands], "pick": 0, "hero": hero}
plan = {"build": "stryde-her-dad",
 "hooks": [{"hook": 1, "line": "Sue! SUE!", "pick": "A", "concepts": [
   {"id": "A", "frame1": "high wide: Sue lifting a plant into the boot, the van's reversing lights coming on behind her, Tony ten feet off with a pot in his hands", "stakes": "she can't see it; he can — and can't reach her", "where": "a garden-centre car park on a grey Saturday", "turn": "his shout, then his knee goes on the first step", "score": sc("222222")},
   {"id": "B", "frame1": "Tony's face, mid-shout, the pot already falling from his hands", "stakes": "something terrible behind the camera", "where": "the car park, tight on him", "turn": "cut wide: the van, the lad running", "score": sc("221221")},
   {"id": "C", "frame1": "the van's back doors filling the frame, rolling toward the lens, a woman's legs at the boot beyond", "stakes": "a body about to be hit", "where": "the car park at bumper height", "turn": "the shout off-screen", "score": sc("212121")},
   {"id": "D", "frame1": "the cracked pot on the wet tarmac, soil spilling, a man's knee coming down beside it", "stakes": "a fall — whose?", "where": "the car park at ground level", "turn": "the lad's 'You're alright' over it", "score": sc("122222")},
   {"id": "E", "frame1": "the lad's face, close, asking 'Is your dad alright?'", "stakes": "the humiliation first, the accident after", "where": "the car park, after the near miss", "turn": "rewind to the van", "score": sc("122211")}]}],
 "groups": [
  {"group": "SC01", "role": "problem", "idea": "the one moment his body fails her, in front of a younger man", "rows": [
    row("SC01-SH01", "(the van starts back)", [("STAKES", "high wide: Sue at the boot, the van rolling back at her, Tony ten feet off", "222222"),
        ("WORLD", "the busy car park, trolleys and shoppers, the van among them", "121121"), ("POV", "Tony's eyes: the van and Sue lining up", "211121")], hero=True),
    row("SC01-SH03", "(his knee goes)", [("STAKES", "low profile: his first step, the knee buckles, the pot cracks", "222212"),
        ("DETAIL", "macro on the knee hitting wet tarmac", "212211"), ("LITERAL", "Tony falling over, wide", "111111")]),
    row("SC01-SH04", "(the lad gets there)", [("CONTRAST", "the lad sprints past the man on the ground and pulls her clear", "222212"),
        ("WORLD", "shoppers turning at the sound", "111121"), ("REACTION", "Sue's face as she's pulled", "112121")]),
    row("SC01-SH06b", "He looked like he was going to go over.", [("STAKES", "past the lad's shoulder: Tony still down on one knee, ten feet away", "222222"),
        ("REACTION", "Sue glancing at Tony", "112121"), ("LITERAL", "the lad pointing", "111111")]),
    row("SC01-SH08", "I'm her husband. And I couldn't get ten feet to my own wife.", [("REACTION", "low close on Tony on one knee, watching them; his inner voice over his face", "222222"),
        ("SYMBOL", "the cracked pot beside his hand", "122221"), ("CONTRAST", "the ten feet of tarmac between them, wide", "211221")])]},
  {"group": "SC02", "role": "scene", "idea": "two people side by side who can't look at each other", "rows": [
    row("SC02-SH01", "He has no idea what I saw from behind that van.", [("REACTION", "profile: Sue at the wheel, key not turned, staring ahead", "222222"),
        ("SYMBOL", "her hand frozen on the key", "112221"), ("POV", "the windscreen view of the garden centre", "111121")], hero=True),
    row("SC02-SH11", "(the silence after)", [("WORLD", "from the back seat: two heads, the windscreen, the garden centre", "222122"),
        ("DETAIL", "his dirty trouser knee", "112121"), ("REACTION", "Tony's jaw", "111121")])]},
  {"group": "SC03", "role": "problem", "idea": "the life he's been reduced to, room by room", "rows": [
    row("SC03-SH01", "Sixty-four. Thirty years laying patios.", [("SYMBOL", "the drawer packed with knee supports that won't shut, his palm forcing it", "222222"),
        ("LITERAL", "Tony getting dressed", "111111"), ("DETAIL", "a sleeve's frayed edge", "112121")]),
    row("SC03-SH02", "I've knelt on every drive in this street.", [("STAKES", "high behind: down his own stairs sideways, both hands on the rail", "222222"),
        ("CONTRAST", "a photo of him laying a drive young", "212210"), ("LITERAL", "a driveway", "011111")], hero=True),
    row("SC03-SH03", "Now I can't get across a car park to my own wife.", [("REACTION", "low from the hall: his face tight on each step", "212222"),
        ("DETAIL", "his feet meeting on each step", "112221"), ("WORLD", "the street outside through the door glass", "011121")]),
    row("SC03-SH04", "Now I wait in the car while she loads the boot.", [("CONTRAST", "Tony in the passenger seat; behind him through the rear window Sue lifting the bags alone", "222222"),
        ("LITERAL", "shopping bags", "011111"), ("REACTION", "Sue's look at him", "112121")])]},
  {"group": "SC04", "role": "problem", "idea": "told it's normal", "rows": [
    row("SC04-SH06", "(after 'That works for most people.')", [("STAKES", "high wide: Tony small in the patient chair, alone with his knee, the GP typing", "222222"),
        ("SYMBOL", "the leaflet rack", "011111"), ("DETAIL", "his hand on his knee", "112121")], hero=True)]},
  {"group": "SC05", "role": "mechanism", "idea": "the one spot, found under his own fingers, and the strap that sits on it", "rows": [
    row("SC05-SH01", "(Gary carries a slab alone)", [("PROOF", "low wide: a man of 70 carrying a paving slab on his own", "222222"),
        ("WORLD", "the busy yard", "111121"), ("LITERAL", "Gary's face", "111121")]),
    row("SC05-SH12", "There.", [("DETAIL", "straight down onto the knee: his two fingers pressing the spot just under the kneecap", "222222"),
        ("REACTION", "Tony's wince", "112121"), ("MECHANISM", "an anatomy cut-away", "212201")]),
    row("SC05-SH15b", "A spot the size of a coin.", [("DETAIL", "his forefinger resting on the spot, the coin-sized patch under it", "212222"),
        ("SYMBOL", "a coin in Gary's fingers", "212211"), ("MECHANISM", "the tendon under load", "212201")]),
    row("SC05-SH22", "Sits right on that spot, two centimetres under the kneecap.", [("PRODUCT", "front-on at knee height: the strap on Gary's knee, the notch at the kneecap's edge, his fingers tapping it", "222222"),
        ("PROOF", "Gary squatting with it on", "211211"), ("LITERAL", "the strap in its box", "111121")], hero=True),
    row("SC05-SH27", "(after 'You'll know in a minute.')", [("CONTRAST", "high wide: Gary back to work with a slab, Tony alone on the pallet looking at his knee", "222222"),
        ("REACTION", "Tony's face", "112121"), ("WORLD", "the yard going on around them", "111121")])]},
  {"group": "SC06", "role": "scene", "idea": "the doubt — 'you've said that before'", "rows": [
    row("SC06-SH01", "What's that?", [("PRODUCT", "Sue at the table with the strap flat in her palm, looking up at him", "222222"),
        ("SYMBOL", "the strap on the pile of post", "112121"), ("REACTION", "Tony caught in the doorway", "112121")], hero=True)]},
  {"group": "SC07", "role": "after", "idea": "the change others see before she does", "rows": [
    row("SC07-SH01", "First time in two years, I came down my own stairs forwards.", [("CONTRAST", "the same high angle as SC03: forwards, hands off the rail", "222222"),
        ("PROOF", "his feet one per step", "212221"), ("LITERAL", "the staircase", "011111")], hero=True),
    row("SC07-SH02", "I didn't tell her.", [("PROOF", "low from the hall: coming down into the light, the strap on his knee", "212222"),
        ("REACTION", "his private look", "112221"), ("SYMBOL", "the kitchen door shut", "111111")]),
    row("SC07-SH03", "You're quick today, Tone.", [("PROOF", "Tony striding across the yard with a slab, the labourer calling after him", "222222"),
        ("WORLD", "the yard at work", "111121"), ("REACTION", "the labourer grinning", "112121")]),
    row("SC07-SH04", "Didn't recognise you from the back.", [("WORLD", "tracking beside him down his street, a neighbour turning at her gate", "222222"),
        ("PROOF", "his stride from behind", "212221"), ("LITERAL", "the neighbour", "111121")]),
    row("SC07-SH05", "That was the first time I felt it.", [("REACTION", "close on Tony walking, the corner of his mouth lifting, a look he keeps to himself", "222222"),
        ("SYMBOL", "the post box he passes", "011111"), ("DETAIL", "his boots on the pavement", "112121")])]},
  {"group": "SC08", "role": "after", "idea": "the man she married, back on his knees in his trade", "rows": [
    row("SC08-SH01", "Tony…", [("PROOF", "high past Sue in the doorway: Tony kneeling on the patio he's laying, tapping a flag level", "222222"),
        ("DETAIL", "the mallet on the flag", "112121"), ("LITERAL", "the garden", "011111")]),
    row("SC08-SH02", "(Sue watching)", [("REACTION", "Sue in the doorway, her eyes filling", "222222"),
        ("SYMBOL", "her hand on the door frame", "111121"), ("POV", "her view of him", "112121")]),
    row("SC08-SH03", "The man on his knees in that garden was someone I used to know.", [("WORLD", "low wide pulling back: him kneeling, her in the doorway, the whole patio", "222222"),
        ("PRODUCT", "the strap on the kneeling knee", "212211"), ("CONTRAST", "the empty half of the patio", "112121")], hero=True)]},
  {"group": "SC09", "role": "after", "idea": "the same car park, the opposite outcome", "rows": [
    row("SC09-SH03", "(a car backs out at her)", [("CONTRAST", "the same high wide as the hook: Sue at the boot, a car reversing, Tony ten feet off", "222222"),
        ("STAKES", "the car's lights", "112121"), ("WORLD", "the busy car park", "111121")]),
    row("SC09-SH04", "(three strides)", [("PROOF", "the same low profile as the hook: three strides, his arm round her, no fall", "222222"),
        ("DETAIL", "his boots on the tarmac", "112221"), ("REACTION", "Sue looking up at him", "112121")], hero=True),
    row("SC09-SH07", "(25 kilos into the boot)", [("PROOF", "low: he swings the compost bag into the boot in one move", "222222"),
        ("DETAIL", "the bag landing", "111221"), ("LITERAL", "a garden centre trolley", "011111")]),
    row("SC09-SH08", "(the kiss)", [("REACTION", "in the car: she leans over and kisses his cheek, he keeps his eyes on the windscreen, pleased", "222222"),
        ("SYMBOL", "Tony at the wheel now", "112221"), ("WORLD", "the car pulling out", "111121")])]},
  {"group": "SC10", "role": "offer", "idea": "it's not your age — it's one spot, and this sits on it", "rows": [
    row("SC10-SH01", "If your knees won't come right… It's not your age.", [("PRODUCT", "front-on at knee height in the garden: the strap on his kneeling knee, the sun on the shell", "222222"),
        ("PROOF", "him standing up off the patio", "212211"), ("LITERAL", "a knee", "111121")], hero=True),
    row("SC10-SH02", "It goes on under your trousers and nobody knows it's there.", [("WORLD", "from behind: Tony in jeans walking up his street, just a man", "222222"),
        ("DETAIL", "a jeans leg", "111121"), ("PRODUCT", "the strap under rolled jeans", "211211")]),
    row("SC10-SH03", "Buy one, get one free right now. One for each knee.", [("PRODUCT", "the open box on the kitchen table: two straps side by side", "222222"),
        ("LITERAL", "a price tag", "011111"), ("SYMBOL", "two knees", "111121")])]},
 ]}
json.dump(plan, open("visual_plan.json", "w"), indent=1, ensure_ascii=False)
