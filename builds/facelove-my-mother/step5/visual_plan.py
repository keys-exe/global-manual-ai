"""§30M Visual Pitch for facelove-my-mother — picks match act_map.json; alternates kept as 'also considered'."""
import json, pathlib
H = pathlib.Path(__file__).parent
R = {r["beat"]: r for r in json.load(open(H / "act_map.json"))}
LINES = {l[0]: l[5] for l in json.load(open(H.parent / "work/lines.json"))}
def sc(s): return dict(zip(("stop", "line", "feel", "specific", "fresh", "makeable"), s))
def row(beat, pick, a1, a2, hero=False):
    r = R[beat]; ln = " / ".join(LINES[x][:70] for x in r["lines"].split(",")) if r["lines"] else "(no line — " + r["action"][:60] + ")"
    c = [dict(route=x[0], picture=x[1], score=sc(x[2])) for x in (pick, a1, a2)]
    return {"beat": beat, "line": ln, "candidates": c, "pick": 0, "hero": hero}
G = []
def group(g, role, idea, rows): G.append({"group": g, "role": role, "idea": idea, "rows": rows})

group("SC01", "problem", "the toast turns: warm and loud, then a quiet verdict landing on her still face in front of thirty friends", [
 row("SC01-SH01", ("WORLD", "the whole long table under the bulbs, thirty friends mid-laugh, Greg pushing up from his chair tapping his glass", (2,2,1,2,2,2)),
     ("LITERAL", "a fork tapping a wine glass, close", (1,1,1,1,1,2)), ("DETAIL", "the uncut white anniversary cake among the candles", (1,1,1,2,2,2))),
 row("SC01-SH02", ("REACTION", "Greg standing low over the table, glass up, grin wide, the room laughing back at him", (2,2,2,2,1,2)),
     ("LITERAL", "Greg raising his glass", (1,2,1,1,0,2)), ("WORLD", "the guests' raised glasses filling the frame", (1,1,1,1,2,2))),
 row("SC01-SH03", ("REACTION", "Susan seated beside him, almost letting herself enjoy it, her glass lifting an inch", (1,1,2,2,2,2)),
     ("DETAIL", "her hand round the stem of her glass", (1,0,1,2,2,2)), ("WORLD", "a wide of glasses going up all down the table", (1,1,1,1,1,2))),
 row("SC01-SH04", ("STAKES", "close on Susan through the soft white cake, pushing in as his words land — her face the only thing that moves, and it doesn't", (2,2,2,2,2,2)),
     ("REACTION", "Greg's face as he says it", (2,2,1,1,1,2)), ("WORLD", "the table hearing it, forks stopping", (1,1,2,1,2,1)), hero=True),
 row("SC01-SH05", ("REACTION", "her profile, turned up to him, two words low: 'Greg. Sit down.'", (1,2,2,2,2,2)),
     ("LITERAL", "her hand on his sleeve", (1,1,1,1,1,1)), ("DETAIL", "her jaw tightening, extreme close", (1,1,1,2,2,1))),
 row("SC01-SH06", ("STAKES", "Paula from above, staring at her plate as his hand points across at her — named in front of everyone", (2,2,2,2,2,2)),
     ("REACTION", "the guests turning to look at Paula", (1,1,1,1,1,1)), ("LITERAL", "Greg pointing at Paula", (1,2,1,1,1,2))),
 row("SC01-SH07", ("REACTION", "back on Susan, held too long, one breath, eyes level", (2,2,2,2,1,2)),
     ("SYMBOL", "her napkin crumpling in her lap", (1,1,1,2,2,2)), ("WORLD", "the table frozen around her", (1,1,2,1,1,1))),
 row("SC01-SH08", ("WORLD", "high behind her: Greg drops into his chair, reaches past the cake for his drink, thirty people not moving", (2,1,2,2,2,2)),
     ("LITERAL", "Greg sitting down", (1,1,1,1,1,2)), ("DETAIL", "his hand around the drink", (1,0,1,2,1,2))),
 row("SC01-SH09", ("SYMBOL", "the untouched anniversary cake, a fork resting beside it, the title landing", (2,1,2,2,2,2)),
     ("WORLD", "the whole silent table", (1,1,1,1,0,2)), ("DETAIL", "a candle guttering", (1,0,1,1,2,2)))])
group("SC02", "agitate", "the deeper cut: her friends' quiet verdict, said behind her back as she keeps walking", [
 row("SC02-SH01", ("DETAIL", "her hands folding the napkin once and laying it beside the cake", (2,1,2,2,2,2)),
     ("LITERAL", "Susan standing up", (1,1,1,1,1,2)), ("WORLD", "the table watching her stand", (1,1,2,1,1,1))),
 row("SC02-SH02", ("STAKES", "two friends in profile at the drinks table, heads together, Susan passing soft behind them mid-step", (2,2,2,2,2,2)),
     ("LITERAL", "two women whispering", (1,2,1,1,1,2)), ("REACTION", "Susan's ear catching it", (1,1,2,1,2,1)), hero=True),
 row("SC02-SH03", ("REACTION", "her face walking toward us, eyes flicking once, never breaking stride", (2,2,2,2,1,2)),
     ("STAKES", "her feet not slowing on the grass", (1,1,1,2,2,2)), ("WORLD", "the party going on behind her", (1,0,1,1,1,2))),
 row("SC02-SH04", ("WORLD", "low from the lawn: she climbs the three deck steps and the door clicks shut on the party", (2,1,2,2,2,2)),
     ("SYMBOL", "the door closing, the glass showing the lights", (1,1,2,2,1,2)), ("LITERAL", "Susan walking inside", (1,1,1,1,0,2)))])
group("SC03", "scene", "alone against the shut door, the party glowing behind the glass", [
 row("SC03-SH01", ("SYMBOL", "her back to the lit glass, the party glowing behind her head, her in the dark hall", (2,2,2,2,2,2)),
     ("LITERAL", "Susan alone in a hallway", (1,1,1,1,1,2)), ("WORLD", "the party through the window", (1,1,1,1,1,2)), hero=True),
 row("SC03-SH02", ("REACTION", "half her face in shadow, eyes opening on nothing — they'd already decided", (2,2,2,2,1,2)),
     ("DETAIL", "her fingers pressed flat against the door", (1,1,2,2,2,2)), ("STAKES", "the party laughter faintly through the glass", (1,1,1,1,1,1)))])
group("SC04", "problem", "the disappearing: she makes it true — the invite down, the photo she's not in, the mirror that agrees", [
 row("SC04-SH01", ("SYMBOL", "her hand turning the party invite face-down on the granite and laying her phone on top", (2,2,2,2,2,2)),
     ("LITERAL", "a phone muting a chat", (1,2,1,1,1,1)), ("DETAIL", "an invite in a bin", (1,1,1,1,1,2))),
 row("SC04-SH02", ("STAKES", "behind her: the family on the sofa round the cake in her phone screen, and her one step outside the picture", (2,2,2,2,2,2)),
     ("LITERAL", "an empty chair at a party", (1,1,2,1,1,2)), ("WORLD", "a birthday going on without her", (1,1,1,1,1,2)), hero=True),
 row("SC04-SH03", ("REACTION", "in the mirror: the morning ritual, foundation dabbed on, eyes flat", (2,2,2,2,1,2)),
     ("LITERAL", "a foundation bottle", (1,1,0,1,1,2)), ("WORLD", "her bathroom", (0,1,1,1,1,2))),
 row("SC04-SH04", ("DETAIL", "macro: the old foundation sitting grey and dry in the line beside her mouth, flaking", (2,2,2,2,2,2)),
     ("MECHANISM", "a cutaway of skin with product in the crease", (1,2,1,2,2,1)), ("LITERAL", "her face in the mirror", (1,1,1,1,0,2))),
 row("SC04-SH05", ("REACTION", "the sponge stopping halfway; she lowers it and just looks", (2,2,2,2,2,2)),
     ("SYMBOL", "the sponge dropped on the dressing table", (1,1,1,2,1,2)), ("LITERAL", "a woman sad at a mirror", (1,1,1,0,0,2)))])
group("SC05", "solution", "a friend concedes the truth, then does her face with her own hands — white, then her own skin", [
 row("SC05-SH01", ("WORLD", "Beth walking straight in without knocking, garment bag on her shoulder, Susan on the end of the bed", (2,2,1,2,2,2)),
     ("LITERAL", "a door opening", (1,1,1,1,1,2)), ("REACTION", "Susan looking up", (1,1,1,1,1,2))),
 row("SC05-SH02", ("REACTION", "Susan small on the end of the bed, saying it to her hands", (1,2,2,2,2,2)),
     ("STAKES", "a photo of Paula on her phone", (1,1,1,1,1,1)), ("LITERAL", "Susan sitting", (0,1,1,1,1,2))),
 row("SC05-SH03", ("CONTRAST", "Beth laying the garment bag down while she says it plainly — the honest friend, not a salesperson", (1,2,2,2,2,2)),
     ("LITERAL", "a syringe", (2,2,1,1,1,1)), ("SYMBOL", "a clinic receipt", (1,2,1,2,1,1))),
 row("SC05-SH04", ("REACTION", "Beth pulling the stool out with one hand and nodding her to it", (2,2,2,2,1,2)),
     ("LITERAL", "a stool", (0,1,0,1,1,2)), ("WORLD", "the bedroom", (1,0,1,1,1,2))),
 row("SC05-SH05", ("PRODUCT", "Beth tilting her chin to the window, the violet stick coming out under her palm like a secret, cap off", (2,2,2,2,2,2)),
     ("LITERAL", "the stick on the table", (1,1,1,1,1,2)), ("DETAIL", "the cap coming off", (1,1,1,2,1,2))),
 row("SC05-SH06", ("PRODUCT", "macro in profile: the balm draws one white stripe up her cheekbone", (2,2,2,2,2,2)),
     ("LITERAL", "a white swatch on skin", (1,2,1,1,1,2)), ("REACTION", "Susan flinching at the white", (1,1,2,1,1,2))),
 row("SC05-SH07", ("PROOF", "one continuous take: the brush circles and behind it the white turns to her own skin, every line still there", (2,2,2,2,2,2)),
     ("MECHANISM", "pigment diagram", (1,2,0,1,1,1)), ("CONTRAST", "split screen before/after", (2,2,1,1,0,1)), hero=True),
 row("SC05-SH08", ("CONTRAST", "Beth stepping back behind her, the mirror showing the evened cheek next to the other", (2,2,2,2,1,2)),
     ("LITERAL", "Beth talking", (0,1,1,1,1,2)), ("PROOF", "a magnified wrinkle unchanged", (1,2,1,2,2,1))),
 row("SC05-SH09", ("PROOF", "in the mirror, Susan leaning an inch in, looking at her cheek — evened, real, lines still there", (2,2,2,2,1,2)),
     ("REACTION", "her hand touching her cheek", (1,1,2,1,1,2)), ("LITERAL", "a mirror", (0,1,1,1,1,2))),
 row("SC05-SH10", ("REACTION", "low and close: quiet disbelief turning to Beth", (2,2,2,2,1,2)),
     ("DETAIL", "her eyes in the mirror", (1,1,2,1,1,2)), ("LITERAL", "Susan asking", (0,1,1,1,1,2))),
 row("SC05-SH11", ("REACTION", "Beth's one nod, plain", (1,2,2,2,2,2)),
     ("PRODUCT", "the stick in Beth's hand", (1,1,1,1,1,2)), ("LITERAL", "Beth answering", (0,1,1,1,1,2)))])
group("SC06", "scene", "the mirror, her enemy all film, gives her back", [
 row("SC06-SH01", ("REACTION", "her eyes holding her own in the mirror, not flinching for the first time", (2,2,2,2,2,2)),
     ("SYMBOL", "the mirror light", (1,1,1,1,1,2)), ("LITERAL", "Susan at the mirror", (1,1,1,1,0,2)), hero=True),
 row("SC06-SH02", ("CONTRAST", "over her shoulder: Beth's hand on her shoulder in the reflection, the two of them in the glass", (2,2,2,2,1,2)),
     ("REACTION", "Beth's face", (1,1,1,1,1,2)), ("LITERAL", "two women in a bedroom", (0,1,1,1,1,2)))])
group("SC07", "after", "the same yard: the group that saw her fall sees her come back, and Paula asks her", [
 row("SC07-SH01", ("WORLD", "across the street: her car at the curb, engine off, white balloons on the mailbox, nobody getting out", (2,2,2,2,2,2)),
     ("LITERAL", "a car parking", (1,1,1,1,1,2)), ("SYMBOL", "the balloons", (1,1,1,1,1,2))),
 row("SC07-SH02", ("REACTION", "through the driver's window: her hands tight on the wheel, Beth's hand on her arm, one breath out", (2,2,2,2,2,2)),
     ("LITERAL", "keys in the ignition", (1,1,1,1,1,2)), ("STAKES", "the party seen through the windshield", (1,1,1,1,1,2))),
 row("SC07-SH03", ("CONTRAST", "the same table, the same lights: heads turning, the talk stopping, then Friend A lighting up", (2,2,2,2,2,2)),
     ("WORLD", "the party in full swing", (1,1,1,1,0,2)), ("LITERAL", "Susan arriving", (1,1,1,1,1,2))),
 row("SC07-SH04", ("PROOF", "Paula crossing the lawn to her first, both hands out", (2,2,2,2,2,2)),
     ("REACTION", "Paula's surprised face", (1,1,1,1,1,2)), ("LITERAL", "two women hugging", (1,1,1,0,1,2))),
 row("SC07-SH05", ("REACTION", "Susan, easy, the corner of her mouth lifting as she says it", (2,2,2,2,2,2)),
     ("CONTRAST", "Greg in the background", (1,1,1,1,1,2)), ("LITERAL", "Susan talking", (0,1,1,1,1,2)), hero=True),
 row("SC07-SH06", ("CONTRAST", "the two women laughing in profile; far behind, Greg small and going still", (2,2,2,2,2,2)),
     ("REACTION", "Greg's face alone", (1,1,2,1,1,2)), ("WORLD", "the party laughing", (1,0,1,1,1,2))),
 row("SC07-SH07", ("SYMBOL", "the same cake shot: now a knife cuts a slice and a hand passes the plate along", (2,1,2,2,2,2)),
     ("WORLD", "people eating cake", (1,0,1,1,1,2)), ("LITERAL", "a slice of cake", (1,0,1,1,1,2)))])
group("SC08", "after", "the redirect: he's sorry, she's kind and done, and the group closes around her", [
 row("SC08-SH01", ("REACTION", "over her shoulder: Greg at her shoulder, quiet, his hand half lifting and dropping", (2,2,2,2,2,2)),
     ("LITERAL", "Greg talking", (0,1,1,1,1,2)), ("SYMBOL", "his wedding ring", (1,1,1,2,1,1))),
 row("SC08-SH02", ("REACTION", "her face, kind and done: 'Go enjoy the party, Greg.'", (2,2,2,2,1,2)),
     ("CONTRAST", "her turning away", (1,1,2,1,1,2)), ("LITERAL", "Susan answering", (0,1,1,1,1,2)), hero=True),
 row("SC08-SH03", ("PROOF", "she turns back to Beth and Paula, laughing before he's finished; Greg left standing", (2,2,2,2,2,2)),
     ("REACTION", "Greg alone", (1,1,2,1,1,2)), ("LITERAL", "women laughing", (0,1,1,0,1,2))),
 row("SC08-SH04", ("CONTRAST", "high wide, the rhyme of the frozen table: Susan in the middle of her friends under the bulbs, Greg alone at the edge", (2,2,2,2,1,2)),
     ("WORLD", "the party at dusk", (1,1,1,1,1,2)), ("LITERAL", "Greg standing", (1,1,1,1,1,2)))])
group("SC09", "offer", "the life she walked back into, then the stick and the primer", [
 row("SC09-SH01", ("WORLD", "a plate of cake passed to her past a friend's shoulder, Susan laughing at Beth", (2,1,2,2,2,2)),
     ("PRODUCT", "the stick on the party table", (1,2,1,1,1,1)), ("LITERAL", "Susan eating cake", (1,0,1,1,1,2))),
 row("SC09-SH02", ("WORLD", "from the deck down the full table into the dusk, the whole group, Susan in the middle", (2,1,2,2,2,2)),
     ("PROOF", "many women's faces", (1,2,1,1,1,1)), ("LITERAL", "a crowd", (1,1,1,0,1,2))),
 row("SC09-SH03", ("PRODUCT", "two closed violet sticks standing beside the white primer tube on pale stone, slow push-in", (2,2,1,2,2,2)),
     ("LITERAL", "a shipping box", (1,1,0,1,1,2)), ("PROOF", "a guarantee badge", (1,2,0,1,1,1)), hero=True),
 row("SC09-SH04", ("REACTION", "low and close, the bulbs behind her: she glances down at the table, lit up among her friends", (2,2,2,2,1,2)),
     ("PRODUCT", "the stick in her bag", (1,1,1,1,1,1)), ("LITERAL", "Susan at the party", (0,1,1,1,0,2)))])

HOOKS = [{"hook": 1, "line": "Thirty years. Thirty. Somebody get this woman a medal for putting up with me, right?",
  "concepts": [
   {"id": "A", "frame1": "the long table under the bulbs, thirty friends mid-laugh, Greg pushing up from his chair tapping his glass", "stakes": "a toast in front of everyone she knows — it's about to turn", "where": "the hosts' back yard at golden hour", "turn": "his face changes; we stay on hers", "score": sc((2,2,2,2,2,2))},
   {"id": "B", "frame1": "close on Susan's face, the soft white cake between her and the lens, his voice off: 'You look like my mother'", "stakes": "the insult lands before we know who she is", "where": "the same table, tight", "turn": "pull back to reveal thirty silent friends", "score": sc((2,2,2,2,1,2))},
   {"id": "C", "frame1": "two friends at the drinks table whispering 'She did kind of stop trying' as Susan walks past", "stakes": "her friends have written her off", "where": "the drinks table by the deck", "turn": "cut back to the toast that caused it", "score": sc((2,2,2,2,2,1))},
   {"id": "D", "frame1": "Susan at the mirror, the old foundation cracking grey in her smile line, the sponge stopping", "stakes": "the face he named, every morning", "where": "her bedroom dressing table", "turn": "VO: 'until I looked exactly like the word he used'", "score": sc((2,1,2,2,1,2))},
   {"id": "E", "frame1": "Paula crossing a lawn with both hands out: 'You look incredible, what are you doing?'", "stakes": "the woman she was compared to asking her", "where": "the same yard, months later", "turn": "'Funny. Greg told me to come ask you.' — then flash back", "score": sc((2,1,2,2,2,1))}],
  "pick": "A"}]
plan = {"build": "facelove-my-mother", "hooks": HOOKS, "groups": G}
json.dump(plan, open(H / "visual_plan.json", "w"), indent=1, ensure_ascii=False)
