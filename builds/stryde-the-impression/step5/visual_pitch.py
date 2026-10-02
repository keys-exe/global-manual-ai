#!/usr/bin/env python3
"""§30M Visual Pitch for stryde-the-impression — the hook's five cold-open concepts and each scene's picture beats
(the silent action, insert and hero shots; dialogue coverage is the act map's). Writes visual_plan.json for visual_plan.py."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
def sc(stop, line, feel, spec, fresh, make): return {"stop": stop, "line": line, "feel": feel, "specific": spec, "fresh": fresh, "makeable": make}
def C(route, picture, s): return {"route": route, "picture": picture, "score": s}
def row(beat, line, cands, hero=False): return {"beat": beat, "line": line, "candidates": cands, "pick": 0, "hero": hero}

hook = {"hook": 1, "line": "Oscar crosses the room the way Nana does. Dan laughs first. Then Emma. Roy looks at his plate.",
 "concepts": [
  {"id": "A", "frame1": "a four-year-old's small hand landing on a chair back as he hitches past the Sunday table, the family behind him laughing",
   "stakes": "a child copying his grandmother's limp in front of everyone", "where": "the dining room after Sunday lunch, the whole family at the table",
   "turn": "the laugh dies on Emma's 'That's enough'", "score": sc(2, 2, 2, 2, 2, 2)},
  {"id": "B", "frame1": "Hazel's face in close-up at the head of the table, laughter all round her, before we see what they are laughing at",
   "stakes": "she is the joke and hasn't been told", "where": "the dining room, Sunday", "turn": "cut wide: it's her walk", "score": sc(2, 1, 2, 2, 1, 2)},
  {"id": "C", "frame1": "Roy alone in frame, eyes down on his plate, pushing a pea, while the room laughs", "stakes": "the one who knows",
   "where": "the dining room, Sunday", "turn": "the reveal of what he won't look at", "score": sc(1, 1, 2, 2, 2, 2)},
  {"id": "D", "frame1": "ground level under the table: small trainers doing the hitch past the chair legs", "stakes": "the walk, copied exactly",
   "where": "under the Sunday table", "turn": "tilt up to the family's faces", "score": sc(2, 1, 1, 2, 2, 1)},
  {"id": "E", "frame1": "the empty chair as Oscar slides off it, Emma reaching too late", "stakes": "something is about to happen in front of everyone",
   "where": "the Sunday table", "turn": "he starts the walk", "score": sc(1, 1, 1, 1, 1, 2)}],
 "pick": "A"}

G = []
def group(g, role, idea, rows): G.append({"group": g, "role": role, "idea": idea, "rows": rows})

group("SC01", "problem", "the walk everyone sees and nobody names, until a child copies it", [
 row("SC01-SH01", "Oscar crosses the room the way Nana does", [
   C("STAKES", "Oscar hitching behind the chairs, a small hand on every chair back, the family laughing behind him", sc(2, 2, 2, 2, 2, 2)),
   C("REACTION", "Hazel's still face at the head of the table while the room laughs", sc(2, 1, 2, 2, 1, 2)),
   C("DETAIL", "Oscar's small hand gripping a ladder-back chair, then the next", sc(1, 1, 1, 2, 2, 2))], hero=True),
 row("SC01-SH02", "Roy looks at his plate", [
   C("REACTION", "Roy, the only one not laughing, eyes down, moving one pea with his fork", sc(2, 2, 2, 2, 2, 2)),
   C("LITERAL", "a plate of Sunday dinner leftovers", sc(0, 1, 0, 1, 0, 2)),
   C("SYMBOL", "Roy's car keys by his plate", sc(1, 0, 1, 2, 2, 2))]),
 row("SC01-SH05", "He does it again. Nobody laughs.", [
   C("CONTRAST", "the same walk in profile, end to end, the table silent now", sc(2, 2, 2, 2, 1, 2)),
   C("REACTION", "Dan's laugh dying on his face", sc(1, 1, 2, 2, 1, 2)),
   C("DETAIL", "Oscar's left shoulder dipping, exactly like hers", sc(1, 2, 1, 2, 2, 1))]),
 row("SC01-SH12", "I'll walk him.", [
   C("REACTION", "Hazel in profile catching the look between Emma and Dan, then saying it", sc(2, 2, 2, 2, 1, 2)),
   C("STAKES", "the steep hill outside the bay window behind her head", sc(1, 1, 2, 2, 2, 1)),
   C("LITERAL", "Hazel saying it to the table", sc(1, 2, 1, 1, 0, 2))])])
group("SC02", "problem", "she sees herself for the first time", [
 row("SC02-SH04", "Film me. From the kitchen to the door.", [
   C("STAKES", "the phone's frame down the hall: Hazel coming toward it, a hand on the wall, the radiator, the newel post", sc(2, 2, 2, 2, 2, 2)),
   C("POV", "over Emma's hands holding the phone, the screen unseen", sc(1, 1, 1, 1, 1, 2)),
   C("DETAIL", "her hand sliding along the dado rail", sc(1, 1, 2, 2, 2, 2))], hero=True),
 row("SC02-SH05", "She watches it once.", [
   C("REACTION", "Hazel's face lit by the phone, watching herself once", sc(2, 2, 2, 2, 1, 2)),
   C("LITERAL", "the phone screen showing the clip", sc(1, 1, 1, 1, 0, 1)),
   C("SYMBOL", "her reflection in the hall mirror behind her", sc(1, 1, 1, 2, 2, 1))])])
group("SC03", "agitate", "every remedy goes round the problem", [
 row("SC03-SH01", "Something for a hill.", [
   C("STAKES", "Hazel steadying herself on the shelf edge at a wall of knee supports", sc(2, 2, 2, 2, 1, 2)),
   C("WORLD", "the high-street chemist from the door, the assistant coming over", sc(1, 1, 1, 2, 1, 2)),
   C("LITERAL", "a rack of knee sleeves", sc(1, 1, 0, 1, 0, 2))], hero=True),
 row("SC03-SH07", "She takes the same beige sleeve off the hook.", [
   C("DETAIL", "her hand taking the same beige sleeve off the hook, the habit of it", sc(2, 2, 2, 2, 2, 2)),
   C("SYMBOL", "the stand of walking sticks beside the till", sc(1, 1, 2, 2, 1, 2)),
   C("LITERAL", "a packet on a hook", sc(0, 1, 0, 1, 0, 2))])])
group("SC04", "agitate", "the count: twenty-four things that go round", [
 row("SC04-SH01", "What is all this?", [
   C("STAKES", "overhead into the stuck drawer: packed with beige sleeves, most still in their packets", sc(2, 2, 2, 2, 2, 2)),
   C("REACTION", "Emma's face as the drawer opens", sc(1, 1, 2, 2, 1, 2)),
   C("LITERAL", "one sleeve on the bed", sc(0, 1, 0, 1, 0, 2))], hero=True),
 row("SC04-SH09", "They all go round.", [
   C("SYMBOL", "Hazel pulling a sleeve over her fist and letting it go slack", sc(2, 2, 2, 2, 2, 2)),
   C("DETAIL", "the sleeve's empty tube in her lap", sc(1, 2, 1, 2, 1, 2)),
   C("LITERAL", "a sleeve on a knee", sc(1, 1, 0, 1, 0, 1))])])
group("SC05", "problem", "the hill wins at the postbox", [
 row("SC05-SH01", "July, 8:40, the hill alone", [
   C("STAKES", "low from the bottom: Hazel small against the whole steep climb, a hand trailing the wall", sc(2, 2, 2, 2, 2, 2)),
   C("WORLD", "the street of terraces waking up, her the only one stopping", sc(1, 1, 1, 2, 1, 2)),
   C("LITERAL", "a steep street", sc(1, 1, 0, 1, 0, 2))], hero=True),
 row("SC05-SH04", "She turns back.", [
   C("STAKES", "from above: she turns round at the red postbox and goes back down", sc(2, 2, 2, 2, 2, 2)),
   C("SYMBOL", "the red postbox alone in the wall after she's gone", sc(1, 1, 2, 2, 2, 2)),
   C("REACTION", "the mum glancing back at her", sc(1, 1, 1, 1, 1, 2))])])
group("SC07", "agitate", "Roy has his own walk", [
 row("SC07-SH01", "Roy comes down the stairs sideways", [
   C("STAKES", "from the kitchen door: Roy coming down sideways, both feet on every step", sc(2, 2, 2, 2, 2, 2)),
   C("REACTION", "Hazel watching from the doorway with the tea towel", sc(1, 1, 2, 2, 1, 2)),
   C("DETAIL", "his slippers turned sideways on one tread", sc(1, 2, 1, 2, 2, 2))], hero=True)])
group("SC09", "mechanism", "one spot under the kneecap, and the thing that takes the weight", [
 row("SC09-SH01", "She gets out of the car", [
   C("CONTRAST", "Hazel's hitch across the pavement toward a woman her age who just walked the hill", sc(2, 2, 2, 2, 1, 2)),
   C("WORLD", "the school gate at pick-up, children everywhere", sc(1, 1, 1, 1, 1, 2)),
   C("LITERAL", "a car door opening", sc(0, 1, 0, 1, 0, 2))]),
 row("SC09-SH09", "One spot. Two centimetres under the kneecap.", [
   C("DETAIL", "Wendy's two fingers touching the spot under her own kneecap through her dress", sc(2, 2, 2, 2, 2, 2)),
   C("MECHANISM", "an anatomy cutaway of the knee", sc(2, 1, 1, 1, 2, 1)),
   C("LITERAL", "Wendy talking", sc(0, 1, 1, 1, 0, 2))]),
 row("SC09-SH13", "This takes the weight before it gets there.", [
   C("PRODUCT", "Wendy lifting her hem: the thin strap with its rigid shell just under her right kneecap on bare skin", sc(2, 2, 2, 2, 2, 2)),
   C("REACTION", "Hazel looking down at it", sc(1, 1, 2, 1, 1, 2)),
   C("MECHANISM", "the load on the tendon lifting", sc(1, 2, 1, 1, 1, 1))], hero=True),
 row("SC09-SH20", "It goes round, it moves nothing.", [
   C("STAKES", "high wide: Wendy off down the steep hill with two children; Hazel left on the bench", sc(2, 1, 2, 2, 2, 2)),
   C("SYMBOL", "Hazel's hand on the bench beside her", sc(1, 1, 1, 1, 1, 2)),
   C("REACTION", "Hazel's face as Wendy goes", sc(1, 1, 2, 1, 1, 2))])])
group("SC11", "proof", "the first morning: the hand comes off on its own", [
 row("SC11-SH01", "The strap goes on, just under the kneecap", [
   C("PRODUCT", "both hands flat on the shell sliding the strap up her bare shin until it seats under the kneecap", sc(2, 2, 2, 2, 2, 2)),
   C("DETAIL", "the strap on the bedspread beside her", sc(1, 1, 1, 2, 1, 2)),
   C("LITERAL", "her knee", sc(0, 1, 0, 1, 0, 2))]),
 row("SC11-SH03", "On the third, my hand came off on its own.", [
   C("PROOF", "low from the hall: on the third step her hand lifts off the banister and she comes on down, hands free", sc(2, 2, 2, 2, 2, 2)),
   C("DETAIL", "her hand hovering above the rail", sc(1, 2, 2, 2, 2, 1)),
   C("REACTION", "her face on the third step", sc(1, 1, 2, 1, 1, 2))], hero=True),
 row("SC11-SH04", "the A/B test on the stairs", [
   C("CONTRAST", "strap off: the hitch is back, the hand is back on the banister", sc(2, 2, 2, 2, 2, 2)),
   C("PROOF", "two descents cut side by side", sc(1, 2, 1, 1, 1, 1)),
   C("LITERAL", "the strap in her hand", sc(0, 1, 0, 1, 0, 2))]),
 row("SC11-SH06", "Roy says nothing.", [
   C("REACTION", "Roy in the kitchen doorway with his mug, watching, saying nothing", sc(2, 2, 2, 2, 1, 2)),
   C("SYMBOL", "his mug going cold", sc(0, 1, 1, 1, 1, 2)),
   C("WORLD", "the hall in morning sun", sc(1, 0, 1, 1, 1, 2))])])
group("SC12", "after", "the hill doesn't win any more", [
 row("SC12-SH01", "the postbox goes by", [
   C("PROOF", "tracking beside her in profile: the red postbox passes behind her and she doesn't slow", sc(2, 2, 2, 2, 2, 2)),
   C("CONTRAST", "the same low wide as July, her higher up the hill", sc(2, 2, 1, 2, 1, 2)),
   C("REACTION", "the mum stopping", sc(1, 1, 1, 1, 1, 2))], hero=True)])
group("SC13", "after", "the second film, the same frame", [
 row("SC13-SH01", "Emma films again", [
   C("PROOF", "the same hall frame as the first film: Hazel coming toward the phone, even, hands free", sc(2, 2, 2, 2, 2, 2)),
   C("CONTRAST", "the two clips side by side (an edit device)", sc(2, 2, 1, 1, 1, 1)),
   C("REACTION", "Emma lowering the phone", sc(1, 1, 2, 1, 1, 2))], hero=True)])
group("SC14", "after", "he knew the day", [
 row("SC14-SH03", "Watch me.", [
   C("PROOF", "the hall frame a third time: she walks to the front door and back past him, even", sc(2, 2, 2, 2, 1, 2)),
   C("REACTION", "Roy's face watching her walk", sc(1, 1, 2, 2, 1, 2)),
   C("SYMBOL", "the car keys in his hand", sc(1, 1, 1, 2, 2, 2))], hero=True)])
group("SC15", "after", "'That's just walking, Nana.'", [
 row("SC15-SH01", "8:40, the hill, hand in hand, his pace", [
   C("PROOF", "beside them in profile: grandmother and boy hand in hand past the red postbox at his pace", sc(2, 2, 2, 2, 2, 2)),
   C("WORLD", "the school run on the hill, other families", sc(1, 1, 1, 1, 1, 2)),
   C("DETAIL", "their two hands", sc(1, 1, 2, 1, 1, 2))]),
 row("SC15-SH04", "He walks. Straight.", [
   C("CONTRAST", "the same child's walk in profile along the railings, straight this time", sc(2, 2, 2, 2, 2, 2)),
   C("REACTION", "Hazel watching him", sc(1, 1, 2, 1, 1, 2)),
   C("LITERAL", "a boy walking", sc(0, 1, 0, 1, 0, 2))], hero=True),
 row("SC15-SH08", "She stands at the gate with nothing in her hands.", [
   C("SYMBOL", "a slow pull-back: Hazel at the open gate, empty hands at her sides", sc(2, 2, 2, 2, 2, 2)),
   C("WORLD", "the playground filling with children", sc(1, 1, 1, 1, 1, 2)),
   C("REACTION", "Emma filming from the car", sc(1, 1, 2, 2, 1, 2))])])
json.dump({"build": "stryde-the-impression", "hooks": [hook], "groups": G}, open(HERE / "visual_plan.json", "w"), indent=1, ensure_ascii=False)
