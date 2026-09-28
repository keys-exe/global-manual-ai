# A/B test — video prompt length vs distortion (2026-09-28)

Question (user): do longer prompts cause distortion, and what length is the sweet spot?

- **Beat:** BR-25 (stairs payoff): the hardest shot in the build, 10 regenerations.
- **Fixed:** the confirmed BR-25 image (v10), `kling-3.0-omni/image-to-video` on Kie AI (the Kling connector had 3 credits;
  the user approved Kie for this test), 5s, 1080p, `prefer_multi_shots: false`, audio off, one render each.
- **Only variable:** the prompt. Same action and pace (brisk, ~2.5 steps/s, one foot per step), same rigid-strap clause.
- Both passed `preflight.py`.

| Arm | Chars | Kie task | Board card | Credits |
|---|---|---|---|---|
| LEAN | 731 | 11748fd3fc77af7f9a4b620741c24980 | `stryde-identity__AB-25-LEAN` | 90 |
| LONG (the exact BR-25 v7 prompt) | 2467 | c5d3cd8f22809087eca6c61f0174778b | `stryde-identity__AB-25-LONG` | 90 |

BR-25 v7 (already on the board, same image and prompt as LONG) is a free second sample of the long arm.
Verdict (user, 2026-09-28): **"both look the same".** With the image, model and settings fixed, a 731-char prompt and a 2,467-char prompt gave clips of the same quality. At this range, prompt length does not cause the distortion (n=1 per arm, plus v7 as a second long sample).

## LEAN prompt
```
{"subject":"Maureen from the start frame, full body at the top of the stairs, cardigan in both hands, the strap on her right knee.","camera":{"movement":"Locked off, handheld breath sway only; never follows her.","framing":"As in the start frame."},"motion":"She walks down the stairs toward the camera at a brisk real-time pace, about two and a half steps per second, one foot per step, never pausing. Hands stay on the cardigan. One continuous take. The strap is rigid hard plastic: it keeps its exact shape, size and wordmark in every frame and moves only with her knee.","negatives":"no slow motion, no cut, no morphing, no warping, no melting limbs, no extra fingers, no bending or flipping of the strap, no hand on the rail"}
```

## LONG prompt
```
{"shot":"top_to_bottom_fast","subject":"Maureen at the top of the carpeted stairs, full body, blue dress, the strap on her right knee, a cardigan in both hands.","camera":{"movement":"Already drifting on frame one. Low breath sway throughout, vertical with slight roll. Camera lags the subject, never anticipates, never travels with it. Still drifting at the cut.","framing":"Full body from the hall looking up the flight, as in the start frame."},"motion":"She comes down the stairs towards the camera FAST at real-time speed, never slow motion, like someone in a hurry: about two and a half steps per second, one smooth continuous rhythm, never pausing, one foot per step, alternating. Her hands stay on the cardigan, off the rail. One single continuous take from the first frame to the last: no cut, no jump, no skipped moment, no change of angle, nothing appearing or disappearing. Everything keeps the exact form, proportion and count it has in the start frame; nothing melts, merges, splits or grows. Subject fully in frame throughout. Same person every frame: same face, age, hair and wardrobe; five separate fingers on each hand; limbs keep their length and bend only at real joints. The strap keeps the start frame's exact geometry every frame: same two equal peaks, same centred notch, same chrome slides and grey stryde wordmark. The shell is hard moulded plastic and never bends, flexes, wobbles or jiggles. Mass and momentum: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly; fabric and the soft elastic band lag and settle after the body stops.","lighting":"Capture exactly as in the start frame: same tone, noise and colour temperature, no grading change across the clip.","style":"Ordinary everyday footage, natural daylight colour, unretouched.","negatives":"no morphing, no warping, no melting, no shape shifting, no merging, no splitting, no duplicate objects, no background bending, no texture swimming, no flickering geometry, no bending, no curling, no folding, no melting, no flipping of the product, no jelly wobble, no rubbery shell, no slow motion, no pausing, no two feet on one step, no hand on the rail, no going up, no cut, no jump cut, no teleporting, no skipped frames, no scene change, no second shot, no phone, no smartphone, no mobile phone anywhere in the frame, no camera in frame, no AI face, no plastic skin, no extra fingers, no fused fingers, no deformed limbs, no CGI look, no text, no music"}
```
