#!/usr/bin/env python3
"""§30M Visual Pitch for facelove-paint-wall — three candidates per B-roll row on three routes, scored /12, the top one picked
(the act map's row). One hero per act. Hooks are pitched at step 6."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
def s(st, li, fe, sp, fr, mk): return dict(stop=st, line=li, feel=fe, specific=sp, fresh=fr, makeable=mk)
def row(beat, line, cands, hero=False):
    c = [dict(route=r, picture=p, score=sc) for r, p, sc in cands]
    tot = [sum(x["score"].values()) for x in c]
    return dict(beat=beat, line=line, candidates=c, pick=tot.index(max(tot)), hero=hero)
G = [
 dict(group="Act 1", role="problem", idea="the years of foundations: her honest bare face, the shelf growing, and every bottle caking in her lines", rows=[
  row("B01", "And for years I felt like my own face", [
   ("WORLD", "from behind her shoulder she runs her eyes along forty unlabelled bottles on her shelf, one hand on the dresser", s(2, 2, 2, 2, 2, 2)),
   ("LITERAL", "her face in close-up, looking down", s(1, 1, 1, 1, 1, 2)),
   ("SYMBOL", "a calendar of years", s(0, 1, 0, 1, 1, 1))]),
  row("B02", "had quietly turned on me.", [
   ("REACTION", "over her shoulder into a round hand mirror: her bare tired face looking back at her", s(2, 2, 2, 2, 2, 2)),
   ("LITERAL", "her face turning away from the lens", s(1, 1, 1, 1, 1, 2)),
   ("CONTRAST", "an old photo of her younger face beside the mirror", s(2, 2, 2, 2, 1, 1))]),
  row("B03", "The dull, tired skin.", [
   ("DETAIL", "in the mirror glass, her bare cheek and eye: dull, sallow, matte skin, one slow blink", s(2, 2, 2, 2, 2, 2)),
   ("LITERAL", "a macro of skin texture alone", s(1, 2, 1, 1, 1, 2)),
   ("STAKES", "her sighing at the mirror", s(1, 1, 2, 1, 1, 2))]),
  row("B04", "The deep lines.", [
   ("DETAIL", "side-on macro: her deep crow's feet hold their shadows as her eyes narrow, then relax", s(2, 2, 2, 2, 2, 2)),
   ("LITERAL", "her forehead lines front-on", s(1, 2, 1, 1, 1, 2)),
   ("SYMBOL", "cracked dry earth", s(1, 1, 1, 0, 1, 2))]),
  row("B05", "The dark circles that made me look worn out", [
   ("STAKES", "from just below, her eyes lift from the mirror to the lens, the dark circles under both eyes plain in the window light", s(2, 2, 2, 2, 2, 2)),
   ("LITERAL", "a macro of one dark circle", s(1, 2, 1, 1, 1, 2)),
   ("REACTION", "her rubbing her eyes", s(1, 1, 1, 1, 1, 2))]),
  row("B06", "I bought the next foundation, then the next,", [
   ("PROOF", "square on the shelf, her hand sets one more unlabelled bottle at the end of a row, then a second beside it", s(2, 2, 1, 2, 2, 2)),
   ("WORLD", "a pile of shopping bags on the floor", s(1, 1, 1, 1, 1, 2)),
   ("LITERAL", "one bottle on a counter", s(1, 1, 0, 1, 1, 2))]),
  row("B07", "then the two hundred dollar one,", [
   ("DETAIL", "from above, her hands lift a heavy faceted glass bottle with a gold cap out of white tissue in a cream box", s(2, 2, 2, 2, 2, 2)),
   ("STAKES", "a receipt with a big total", s(1, 2, 1, 1, 1, 1)),
   ("LITERAL", "the bottle on the shelf", s(1, 1, 0, 1, 1, 2))]),
  row("B08", "always sure the next one would finally fix it.", [
   ("REACTION", "at the hand mirror she dots the new foundation on her cheek with one fingertip and looks, hopeful", s(2, 2, 2, 2, 2, 2)),
   ("SYMBOL", "her fingers crossed", s(1, 1, 1, 0, 1, 2)),
   ("LITERAL", "the new bottle's pump pressed", s(1, 1, 0, 1, 1, 2))]),
  row("B09", "It sat on top, sank into my lines,", [
   ("STAKES", "side-on macro: a flat beige foundation sits cakey on her skin and has settled into every crow's foot, each crease a darker line of product", s(2, 2, 2, 2, 2, 2)),
   ("CONTRAST", "half her cheek bare, half caked", s(2, 2, 1, 2, 1, 1)),
   ("LITERAL", "foundation on a fingertip", s(1, 1, 0, 1, 1, 2))], hero=True),
  row("B10", "oxidized, and left me looking more tired than my bare face.", [
   ("STAKES", "over her shoulder into the hand mirror: her caked face gone patchy and orange along the jaw against a paler neck; she lowers the mirror", s(2, 2, 2, 2, 2, 2)),
   ("DETAIL", "a macro of the orange line at the jaw", s(2, 2, 1, 2, 1, 2)),
   ("LITERAL", "her frowning", s(1, 1, 1, 0, 1, 2))])]),
 dict(group="Act 2", role="mechanism", idea="the paint wall: a factory colour rolled on sits as a coat and sinks into the cracks — exactly as foundation does in her lines", rows=[
  row("B11", "Think of your skin like a wall", [
   ("SYMBOL", "low and wide: she steps beside the bare warm plaster wall, bottle in one hand, and lays her other palm flat on it", s(2, 2, 2, 2, 2, 2)),
   ("LITERAL", "a close-up of a plaster wall", s(1, 2, 0, 1, 1, 2)),
   ("WORLD", "a hardware store paint aisle", s(1, 1, 1, 1, 1, 2))], hero=True),
  row("B12", "Every foundation you have ever bought", [
   ("PRODUCT", "at the wall she raises the beige foundation bottle to shoulder height like an exhibit, eyes on the lens", s(2, 2, 1, 2, 2, 2)),
   ("WORLD", "her shelf of forty bottles again", s(1, 2, 1, 1, 0, 2)),
   ("LITERAL", "a bottle on a white table", s(1, 1, 0, 1, 1, 2))]),
  row("B13", "works exactly like a pre-mixed can of paint from a factory,", [
   ("CONTRAST", "top-down: the open can of flat pinkish-beige paint, and her hand sets the beige foundation bottle right beside it — the same colour", s(2, 2, 1, 2, 2, 2)),
   ("WORLD", "a paint factory line filling cans", s(2, 2, 1, 1, 2, 0)),
   ("LITERAL", "a closed paint can", s(1, 1, 0, 1, 1, 2))]),
  row("B14", "You bring it home, put it on,", [
   ("LITERAL", "from behind her shoulder she rolls the beige paint up the bare wall in one long slow stroke", s(2, 2, 1, 2, 2, 2)),
   ("DETAIL", "the roller's nap pressing into the wall", s(1, 2, 1, 2, 1, 2)),
   ("WORLD", "carrying the can in from the car", s(1, 1, 1, 1, 1, 2))]),
  row("B15", "and it is never quite your color.", [
   ("CONTRAST", "low and square: she steps back and tilts her head at the flat pinkish stripe, plainly wrong against the warm plaster", s(2, 2, 2, 2, 2, 2)),
   ("DETAIL", "the stripe's colour next to the bare wall, close", s(1, 2, 1, 2, 1, 2)),
   ("REACTION", "her wince", s(1, 1, 1, 1, 1, 2))]),
  row("B16", "It sits there as an obvious coat.", [
   ("DETAIL", "macro across the stripe's edge: a flat ridge of beige sitting on top of the plaster with a hard edge", s(2, 2, 1, 2, 2, 2)),
   ("CONTRAST", "the coated and bare wall side by side", s(1, 2, 1, 1, 1, 2)),
   ("LITERAL", "a wet paint sign", s(1, 1, 0, 0, 1, 1))]),
  row("B17", "And on a wall with any texture or fine cracks,", [
   ("MECHANISM", "square macro: the beige coat slides over fine hairline cracks and sinks in, each crack turning to a darker line", s(2, 2, 2, 2, 2, 2)),
   ("LITERAL", "the bare cracks alone", s(1, 2, 1, 1, 1, 2)),
   ("DETAIL", "a fingertip tracing one crack", s(1, 2, 1, 2, 1, 2))]),
  row("B18", "like skin over fifty, it sinks straight into them and makes them worse.", [
   ("CONTRAST", "the same square macro on her cheek: beige foundation sinks into her fine lines in the same pattern as the wall's cracks", s(2, 2, 2, 2, 2, 2)),
   ("STAKES", "her whole caked face in the mirror again", s(1, 2, 2, 1, 0, 2)),
   ("LITERAL", "a macro of fine lines, bare", s(1, 1, 1, 1, 1, 2))])]),
 dict(group="Act 3", role="solution", idea="the opposite: no shade at all — white that becomes her shade on her face, in one unbroken shot", rows=[
  row("B19", "This does the opposite. It does not come in a shade.", [
   ("PRODUCT", "at the wall she sets the beige bottle down by the paint can and holds up the closed violet stick beside her face, wordmark to the lens", s(2, 2, 1, 2, 2, 2)),
   ("CONTRAST", "the paint can and the stick side by side on the drop cloth", s(2, 2, 1, 2, 1, 2)),
   ("LITERAL", "the stick on a white table", s(1, 1, 0, 1, 1, 2))]),
  row("B20", "It comes out pure white. I know what you are thinking. Stay with me.", [
   ("PRODUCT", "a little low: she draws the cap off and turns the white balm to the lens, the corner of her mouth lifting, knowing", s(2, 2, 2, 2, 2, 2)),
   ("DETAIL", "a macro of the white crest", s(1, 2, 1, 2, 1, 2)),
   ("REACTION", "her eyebrow raised to the lens", s(1, 1, 2, 1, 1, 2))]),
  row("B21", "It reads the warmth of your own skin and becomes your exact shade, right there on your face. No shade to pick. No wrong match. It adapts as it goes on.", [
   ("PROOF", "one unbroken side-on macro of her bare cheek: a white stripe goes on, the brush circles through it — white ahead of the crown, her own shade behind — until the cheek is one even tone, every line still there", s(2, 2, 2, 2, 2, 1)),
   ("CONTRAST", "white stripe, then the blended cheek, cut together", s(1, 2, 1, 1, 1, 2)),
   ("LITERAL", "the stick turning on a table", s(1, 1, 0, 1, 0, 2))], hero=True)]),
 dict(group="Act 4", role="proof", idea="the result on the same face: even, matched, every line still hers — and the factory bottle goes back on the shelf", rows=[
  row("B22", "It covers the lines, the dark circles, the tired.", [
   ("PROOF", "she turns her finished face slowly from profile to the lens in the window light: even tone, the circles gone, every line still there", s(2, 2, 2, 2, 2, 2)),
   ("CONTRAST", "her bare face cut to her finished face", s(2, 2, 2, 1, 1, 1)),
   ("LITERAL", "a macro of her finished under-eye", s(1, 2, 1, 1, 1, 2))], hero=True),
  row("B23", "My skin, on its best day. Finally the right match,", [
   ("CONTRAST", "she holds the beige bottle up beside her finished cheek: the flat factory beige next to her even, matched skin", s(2, 2, 2, 2, 2, 2)),
   ("PROOF", "a macro of her cheek, pores and lines, the tone even", s(1, 2, 1, 2, 1, 2)),
   ("REACTION", "her looking at her reflection, pleased", s(1, 1, 2, 1, 1, 2))]),
  row("B24", "instead of a guess from a factory.", [
   ("SYMBOL", "from above her shoulder she sets the beige bottle back on the shelf among the forty others and lets go", s(2, 2, 2, 2, 2, 2)),
   ("PRODUCT", "the stick set down in front of the shelf", s(1, 1, 1, 1, 1, 2)),
   ("LITERAL", "a factory conveyor of bottles", s(1, 2, 0, 1, 1, 0))])]),
 dict(group="Act 5", role="offer", idea="the deal on her dresser, then the stick alone in soft light", rows=[
  row("B25", "two Foundation Sticks for almost the price of one,", [
   ("PRODUCT", "from above the dresser her hand sets a second stick upright beside the first, both wordmarks to the lens", s(2, 2, 1, 2, 2, 2)),
   ("CONTRAST", "one stick, then two", s(1, 2, 1, 1, 1, 2)),
   ("LITERAL", "two sticks on a white background", s(1, 2, 0, 1, 1, 2))]),
  row("B26", "plus a free primer, a mystery gift,", [
   ("PRODUCT", "level with the dresser her hand sets the primer and then the small gift box beside the two sticks", s(2, 2, 1, 1, 1, 2)),
   ("DETAIL", "level with the dresser her hand sets the primer and then the small gift box beside the two sticks, the box lid ajar on a fold of white tissue", s(2, 2, 1, 2, 2, 2)),
   ("LITERAL", "the primer alone", s(1, 1, 0, 1, 1, 2))]),
  row("B27", "Stop paying for a color that was never yours.", [
   ("PRODUCT", "the closed violet stick stands on the white dresser and turns a quarter turn in soft window light, the wordmark coming round, the shelf of bottles soft behind", s(2, 2, 2, 2, 2, 2)),
   ("CONTRAST", "the stick in front, forty bottles behind it in focus", s(2, 2, 1, 2, 1, 2)),
   ("LITERAL", "a price tag", s(1, 1, 0, 0, 1, 2))], hero=True)]),
]
json.dump(dict(build="facelove-paint-wall", hooks=[], groups=G), open(HERE / "visual_plan.json", "w"), indent=1, ensure_ascii=False)
