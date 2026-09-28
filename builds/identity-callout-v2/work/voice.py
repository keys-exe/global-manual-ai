from lib import A, BUILD
VOICE_CAROL = ("A sixty-four-year-old White British woman from Nottingham in the East Midlands, a low chest voice with a dry, slightly smoker's rasp, stop-start. "
 "Broad East Midlands accent: short flat 'a' in 'bath' and 'last', 'oo' rounded forward, glottal t's in the middle of words, h dropped at the start of unstressed words, never Received Pronunciation, never Northern-comic, never London. "
 "The voice sits low for a woman her age, in the chest, with breath audible in the tone and a dry scrape on louder words. Quick, with little stops before numbers and before the point of a sentence. "
 "Sentences land falling and flat, the last word clipped rather than lifted. Consonants soft and a bit lazy except on hard claims, where they come out crisp. "
 "Held vowels waver slightly and her breath runs short on long lines, so the last few words of a long sentence rush. "
 "Emphasis is quieter and slower, not louder: she leans on the word and drops her pitch. A short dry exhale through the nose before a claim, and a quick 'mm' of agreement with herself.")
LINE = "Because every step puts seventeen times your bodyweight through one small spot below your kneecap."
def seedance_prompt():
    man = A("ING-MANIFEST")
    man = ("INGREDIENTS. @image1 is the opening composition: the clip opens on exactly this framing, light and camera position, and nothing in it is re-composed. "
           "@image2 is CAROL: face, age, hair and build only, with the wardrobe taken from @image1 and never from this sheet. "
           "@image3 is the room and the house. These references set what things ARE; the prose below sets what HAPPENS, and nothing in them is a shot to cut to.")
    prose = (f"Carol, sitting forward on the edge of the sofa with her forearms on her knees, talks straight to the propped phone and says: \"{LINE}\" "
             f"Her voice: {VOICE_CAROL} "
             "She says it plainly, like telling a friend something she only just found out, a little indignant at the number, eyes on the lens, one hand lifting off her knee on 'seventeen' and tapping just below her own kneecap on 'one small spot'. "
             + A("BREATH-A") + " " + A("PACE-A") + " " + A("AUD-A") + " "
             "Small room, soft furnishings and carpet deadening it, short dull tail, voice about a metre from the phone with a little room in the signal, no boom. "
             "The phone is propped and still apart from the tiniest drift. One continuous shot, no cut. "
             "Negative: " + A("NEG-DEFAULT-VOICE") + ", no music, no second voice, no subtitles, no text on screen, no cut to another shot.")
    return man + " " + prose
if __name__ == "__main__":
    (BUILD/"beats/VO-SRC.seedance.txt").write_text(seedance_prompt()); (BUILD/"voice/VOICE-CAROL.txt").write_text(VOICE_CAROL)
    print(len(seedance_prompt()), len(LINE.split()))
