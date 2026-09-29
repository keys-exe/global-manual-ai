# Locked compiled strings for build SHA0071 (Mode 4). Verbatim; never paraphrased.
LOOK = ("THE LOOK OF THIS FILM: a restrained American workplace drama about dignity and age, observed quietly and honestly like a prestige feature. "
 "The sets are a corporate office building in cool greys, off-white walls, grey carpet tile, glass partitions and brushed aluminium, with charcoal, navy and ivory wardrobe. "
 "Highlights on fluorescent tubes and windows roll off softly into white, no halation, with the gentle edge softness of Cooke glass. "
 "Captured with natural, neutral colour and a gentle contrast, ungraded — the grade is added later in the edit. Every frame of this film shares exactly this look.")
def CAM(focal, stop, rig):
    return (f"Photographed as a single frame from a US feature film, shot on an ARRI Alexa 35 in Super 35 with Cooke S4/i prime lenses at {focal}mm and {stop}, "
     f"24 frames per second with a 180-degree shutter, in ARRI colour science colour, the camera on {rig} and operated by a feature crew who framed and lit this moment on purpose. "
     "A still lifted from the finished film, not a photograph and not a phone video, composed natively for a vertical 9:16 frame with no letterbox bars.")
CAP = ("This is a frame from a real film shoot, not a render. Real lens optics: focus falls off gradually either side of one chosen plane, and the out-of-focus areas are soft and round rather than smeared. "
 "Highlights behave the way a cinema sensor handles them, rolling off softly into white on the fluorescent tubes and windows with no hard clipped edge. "
 "Shadows hold detail rather than being lifted flat by phone processing. No digital sharpening, no HDR tone-mapping, no phone processing, no beauty retouch, no diffusion glow on skin. "
 "Under the grade, skin, fabric and surfaces keep all of their real texture.")
NEG_FILM = ("no phone camera look, no smartphone processing, no HDR tone-mapping, no flat lifted shadows, no over-sharpening halos, no selfie framing, no front-camera distortion, no handheld phone jitter, "
 "no digital video look, no CGI look, no plastic skin, no beauty retouch, no diffusion filter glow on skin, no soft-focus beauty lighting, no flat frontal key, no unmotivated light, no applied vignette oval, "
 "no letterbox bars, no generated film grain, no slow motion, no speed ramp, no stock footage look, no commercial gloss, no perfect symmetrical face, no actor looking into the lens")
BODY_WHOLE = ("EVERY PERSON IN FRAME IS ANATOMICALLY WHOLE. Each person has exactly one head attached to one neck, two arms and two legs, each joined to the body at the right place and bending only at real joints. "
 "Every visible hand has one thumb and four fingers, separate, correctly sized, gripping or resting the way a real hand does. Any part of a body that is not visible is out of view for a reason you can see — cut by the frame edge or hidden behind a named object — never simply missing inside the frame.")
NEG_BODY = ("no missing head, no head cut off inside the frame, no missing limb, no missing arm, no missing leg, no missing hand, no extra limb, no extra arm, no extra hand, no extra fingers, no missing fingers, "
 "no fused fingers, no six fingers, no three fingers, no malformed hands, no hands merging into objects, no limb ending in mid-air, no limb fading into the background, no body parts detached, no torso without a head, no bent-back joints, no two people sharing a limb")
NEG_SKIN = ("no poreless skin, no smooth skin, no smoothed cheeks, no uniform specular, no beauty-filter smoothing, no airbrushed skin, no perfectly even complexion, no soft-focus glow on the face, no glowing radiant skin, no youthful skin, no glamour portrait")
NEG_TEX = ("no flat skin surface, no texture painted onto a flat face, no uniform pore pattern, no repeating skin texture, no evenly coloured skin, no smooth young neck, no dead eyes, no missing catchlight, no full even lashes, no smooth single-mass hair, no beauty close-up, no studio portrait")
NEG_SCENECUT = ("no light direction changing within the scene, no colour changing between shots, no graded look, no wardrobe changing within the scene, no prop moving between shots unless shown moving, no character changing position between shots, "
 "no camera crossing the action line, no eyeline pointing the wrong way, no time of day changing within the scene, no different room, no extra people, no missing people, no tears, redness or sweat appearing or vanishing between shots, "
 "no hair or clothing state resetting between shots, no prop jumping to the other hand")
NEG_LIGHT = ("no rim light without a source behind the subject, no glowing skin, no halo or bloom, no light from nowhere, no shadows falling in two directions, no subject brighter than the room around them, no orange-and-teal grade, no sunbeams or god rays, no haze, no lens flare, no eyes lost in shadow, no blown wordmark")
NEG_LIGHT_C = "no flickering light, no exposure pumping, no light changing across the clip, no shadows sliding, no sun patch moving, no light following the subject"
NEG_DRAMA = ("no theatrical acting, no mugging, no soap-opera reactions, no exaggerated crying, no streaming tears, no glycerin tears, no frozen listener, no blank face while being spoken to, no reaction arriving before the line that causes it, "
 "no emotion resetting between shots, no two characters speaking at once unless the script overlaps them, no speech directed at the camera, no performing to the lens, no expression held for effect, no nodding along while speaking, "
 "no constant half-smile, no eyebrows rising on every stressed word, no hand gesture on every phrase, no head tilt on every line, no voice steadier or brighter than the face, no voice resetting between lines")
NEG_WARP = "no morphing, no warping, no melting, no shape shifting, no merging, no splitting, no parts detaching, no proportions changing, no duplicate objects, no background bending, no texture swimming, no smearing, no flickering geometry"
NEG_SOUND = "no music, no score, no sound effects, no foley, no background ambience events, no singing, no humming"
PROD_DEPTH = lambda fg, who: (f"The set is dressed and layered like a feature production: {fg} soft in the near foreground, {who} in the middle ground, and the room continuing in depth behind them, lived-in, with its own practicals lit. "
 "Real surfaces with age and use, and clothes with weave and wear. Nobody stands against a flat wall.")
PHYS_FRAME = ("Weight and support everywhere: body load visibly on one foot or braced hand, fabric hanging from contact points and creasing at joints, every object resting on something with a tight contact shadow, soft deforming under hard, liquids level with gravity, nothing floating.")
INHERIT = ("The look exactly as in the start frame: same lens, same depth of field, same colours, same light direction and same optical texture. Nothing about the look changes across the clip. "
 "24 frames per second with a 180-degree shutter, so moving hands and objects carry natural motion blur.")
HOLD_C = ("Everything in frame keeps the exact form, proportion and count it has in the start frame, first frame to last — nothing melts, merges, splits, grows or becomes something else. One small movement, completing inside the clip, subject fully in frame throughout, nothing leaving frame and returning.")
HOLD_HC = ("Same person every frame: same face, bone structure, age, hair and wardrobe. Five separate fingers on each hand throughout, never fusing and never passing through anything. Limbs stay attached, keep their length, and bend only the way real joints bend.")
PHYS_MOTION = ("Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide.")
AUD_FILM = ("Audio is clean production sound from a boom microphone just out of frame above the speaker: close, clear and even, with a little of the room's natural tone behind the voice. Breath and mouth detail are present but never exaggerated. "
 "No phone-microphone proximity, no compression pumping, no music and no sound effects anywhere in the clip — dialogue only.")
RIG_F2 = ("Camera on a tripod, framed and locked, with no drift, no sway and no reframe. The only camera life is one small operator pan or tilt of a few degrees to keep the subject in frame as they shift. It arrives a beat late and corrects only part of the way. The subject and the room carry all the other movement.")
RIG_F1 = lambda cm: (f"Camera on a dolly, already moving on the first frame: a slow, steady push toward the subject covering about {cm} centimetres across the whole clip, perfectly level, with no bounce and no sway. As the line lands the move eases and slows but never stops. Still creeping in on the final frame. The subject stays in place — seated, standing or speaking — and never walks while the camera moves.")
VOICE = {
 "PAULA": ("A woman of fifty-eight, Black American from Atlanta, a warm low alto with a soft Southern round to the vowels, dry and level in delivery. "
           "Unhurried, even pace; slightly husky at the bottom of her range; she lands the ends of sentences flat rather than lifting them."),
 "ROBIN": ("A woman of forty-eight, white American from suburban Chicago, a clear bright mid-range voice with flat Midwestern vowels, kind and measured. "
           "Moderate pace that slows and softens when she is being careful; light breath before difficult words."),
}
