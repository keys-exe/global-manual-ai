# OUTPUT — Down Forwards Again (automatic run)

Build `down-forwards-again` · Mode 1 · Short VSL, Doctor Authority · standards V7.63.0 · branch `claude/ecstatic-volta-lut52w`, folder `builds/down-forwards-again/`.

## 08_EDIT — finished videos

| File | Hook | Length |
|---|---|---|
| down-forwards-again_HK1.mp4 | Door A — "In six weeks, this woman stopped coming down her own stairs backwards." | 135.43s |
| down-forwards-again_HK2.mp4 | Door B — "I am a doctor, and I am going to tell you to do something…" | 132.96s |
| down-forwards-again_HK3.mp4 | Door C — "Every week somebody brings me a scan of a knee…" | 132.07s |

Rough cuts from `assemble.py`/`variants.py` (layouts, cuts, master audio). CapCut finish: `capcut_block.md`. Set report: `edit/variants_report.json`.

## 04_VOICE
- Clone "Forwards", ElevenLabs voice ID `7Jh1KORnOEknCS0IfC6z` (eleven_v3), cloned from the Seedance source clip.
- Masters: `voice/Forwards_master.mp3` (body 123.8s), `Forwards_HK1/HK2/HK3_master.mp3`.
- Voice roster: voice_roster.md (this folder).

## 06_TALKING_HEADS (HeyGen Avatar V, no motion prompt — per user instruction)
| Beat | HeyGen | Verdict |
|---|---|---|
| TH-BODY | see run_ledger.json | USE |
| TH-HK1 | https://app.heygen.com/videos/31faf590bd08ac0c885fc92999a79e24 | USE — Avatar V, same doctor/room as body, lip-sync on HK1 master, 11.65s |
| TH-HK2 | https://app.heygen.com/videos/d7778161f7dc229eb1f6e7c31419caf4 | USE — Avatar V, 9.18s |
| TH-HK3 | https://app.heygen.com/videos/230a4ef342c4a0ee35ae335e9528b798 | USE — Avatar V, 8.29s; brief smile near the end (register, minor) |

## 05_HOOKS + 07_BROLL — beats
Start frames: Higgsfield (nano_banana_pro route). Clips: Kling 3.0 Omni 1080p 9:16. Prompts: `beats/<ID>*.t2i.txt` / `*.i2v.json` (highest version = used).

| Beat | Phrase | Layout | Start frame | Kling job | Image verdict | Clip verdict |
|---|---|---|---|---|---|---|
| BR01 | A patient of mine. Nine years of knee pain. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195129_8b3d1537-fc59-4b27-aed7-94925d8b3370.png) | AYF7EVAZ7dECfLAU… | USE || USE |
| BR02 | Bone on bone on the left, the right one following it. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_194836_21794a44-a6a4-4975-b258-1c223de55001.png) | Afv3AY5FKZI-VgXb… | USE || USE |
| BR03 | Two centimetres below your kneecap there is a band of tendon about as  | split | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_194656_2af4749a-a104-41ce-8714-1c8e4e7770cc.png) | ASi7MVB2iaauD4Ju… | USE — tendon band the one coloured element, 2 cm below kneecap, no text || USE |
| BR04 | Every step you take lands on it. Seventeen times your bodyweight. | split | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195129_888b25a2-ece3-4f27-8a05-b962e6e1651e.png) | AXZSKxHIH1-QkHB2… | USE (v2) || USE |
| BR05 | Put your finger under your kneecap and press. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195129_6059d735-8cc6-4882-a625-f9b646682c26.png) | AR3VcvvkYn30gyzj… | USE || USE |
| BR06 | Coming down is worse than going up. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195132_21386dce-ff52-4279-a9bb-8d417ed06d44.png) | AVUc2bWJRhUfcSrt… | USE || USE |
| BR07 | Going up, your muscles lift you. Coming down, you are catching yoursel | split | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_194656_0a13e316-74ef-4d90-aae4-8581aee1fc57.png) | AdFiTz31-EsHa4aU… | USE — knee flexing, quads red, tendon orange; orange slightly overlaps kneecap (minor) || USE |
| BR08 | That is why she came down backwards. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195629_7ce781a9-f82c-4298-9dd6-a0403ae6f9ed.png) | AXfoG3_f_NuXJwn1… | USE (v2) — facing up the stairs, descending backwards || USE |
| BR09 | That is why the chair took three tries. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195130_8f631d18-4c3c-4f3c-92a8-ea253169a238.png) | AW_uQDd2wYxc1_8C… | USE || USE |
| BR10 | That is why the good knee started going the same way. She had been lea | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195129_5e1e4f4c-caea-40b7-a4af-32c2b97b307f.png) | AYW9_4haUn4rKdE8… | USE || USE |
| BR11 | The long walk. The garden. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195130_0e5a2d31-d308-48b7-8f2a-19fe5858092f.png) | AQ3SqDQPCUGwxuqZ… | USE || USE |
| BR12 | Her family coming to her instead. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195130_5b02948b-d99f-4b98-bb56-2e28ca910516.png) | AWoV64w_oOl2Wnvd… | USE || USE |
| BR13 | A sleeve squeezes the whole knee. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_194836_e3e8c124-1a32-499e-8999-3dfcc0592dc7.png) | AUJc6RCs7t-hEG8K… | USE || USE |
| BR14 | A hinged brace stops it going sideways, and her knee was never going s | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_194837_b3e4f3e2-1101-40d5-a0e1-0175f984cb36.png) | AepDHYpov0hLutlp… | USE || USE |
| BR15 | A gel sits on the skin. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_194837_3643ed30-631a-407e-b81f-8d5193847d35.png) | AcpGZtYcN7sfoZ6n… | USE || USE |
| BR16 | It is called Stryde. | full | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195130_0066b708-60b7-4d03-905d-8c29f4fceba7.png) | ASWl-Ab7scJ9z-nP… | USE || USE |
| BR17 | It sits two centimetres below the kneecap, on the tendon. It never cro | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195130_793d940b-538b-4597-89e4-cab74f4e210f.png) | AfunYIHau0c8PFyB… | USE || USE |
| BR18 | A silicone pad inside holds pressure on that one band instead of sprea | full | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195629_a0850a66-7541-4441-801a-91785e7d72ac.png) | AYqeV-4AEXtCC-EC… | USE || USE |
| BR19 | The weight gets caught and moved off the worn part before it reaches t | split | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195129_0ccd0ea0-d765-4db8-b15d-9efc65a3729e.png) | Ad3CkBPH0iVQdoSh… | USE (v2) || USE |
| BR20 | The placement is the whole thing. A centimetre too high and it is a sl | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195629_0bc05242-bcf1-4579-8821-e0c722f08d24.png) | AeVIQxcAdwoMwEXb… | USE with motion change — strap already at the tendon (end state), so I2V motion changed fr || USE |
| BR21 | Ten seconds to put on. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195630_1aebc214-4adf-44c2-8129-acf9816843dc.png) | Ad9CIX2a7xbMsQNb… | USE with motion change — strap already at the tendon; I2V motion = fingers settle the notc || USE |
| BR22 | No sores, no rolling down, and nobody can see it. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195629_a8c73048-a3c4-468d-b97d-87df5a2cf419.png) | AWyHCRzi_XM4K2L2… | USE || USE |
| BR23 | You do not have to take my word for it. One knee only. Leave the other | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_200812_d2d9d159-6663-4030-9b76-a56b0fd4127c.png) | AXd4Pl3ycCFyOB8b… | USE (v3) | USE (v3) — standing, strap on her left, right knee bare, shoes on |
| BR24 | Go to your own stairs and come down forwards. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_203007_1c6e72cb-d03b-4781-87c8-04dfd1242641.png) | AfShJAtmgd3OU4Vp… | v1 clip QA caught strap on her right and her climbing -> v3 (side wrong: handrail clause m | USE (v4) — descends forwards towards camera, strap on her left every frame, shoes on |
| BR25 | Her scan looks exactly the same as it did in March. I have both of the | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_194836_968a1a1e-b80a-4a0b-9fb6-9ee0048ffef8.png) | AcS-O0dLwd8gQGor… | USE — two films on a stand lightbox; each film shows one knee (minor, pip-sized) || USE |
| BR26 | Because the load is not landing on that band any more. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195956_8b580cc9-3904-45f7-98e0-173b7504d2ea.png) | ARGnLRWHnfeS11jr… | USE (v2) — strap on her left knee; one foot reads bare (minor continuity, flagged) | USE (flag) — strap on her left, descending into hall; one foot bare mid-clip |
| BR27 | Two for one, so you do both knees, which is what she needed. | full | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195630_60f91068-60d4-4d61-af3b-1bb370de1200.png) | AadraY0pOhF0-Ugy… | USE || USE — in-point 1.2s (skips lid flip) |
| BR28 | The copies stretch, and a stretched strap stops holding the spot. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195631_031b81ca-6bec-4bcf-afea-699a026cafad.png) | AVKuxXVCD5-NIG1G… | USE (v2) — copy keeps peaks/notch, scratched, frayed velcro || USE |
| BR29 | Nothing to lose but the pain. Go and do your stairs. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_203007_340eeb8b-58c6-48c3-b8d9-53da57d9f885.png) | AUjC5lkZ6Gy7NOd4… | BEST-OF-RETRIES v5 — descending, shod; strap on her RIGHT knee (v2 right knee, v3 correct  | USE (best-of-retries, flagged) — descends into hall, shoes on, small smile; strap on her R |
| HK1-01 | In six weeks, this woman stopped coming down her own stairs backwards. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_202715_a51b634f-4992-4873-91a5-aa33f4c3dfd2.png) | AYTzuwByjvvgrgNz… | REGENERATE v1 (Q3 strap on her right) -> v2 (side fixed; Q1 camera at top, climbing, baref | USE (v3) — descends forwards, strap on her left every frame, shoes on |
| HK1-02 | Without one more brace going in the drawer. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_194836_3257a9e5-f630-4c83-9932-9cdfef7b6d07.png) | AcKz-NF9BxtQ_-Xy… | USE | USE — generic brace folded into drawer, drawer closes; no product shown (correct for the l |
| HK2-01 | It takes ten seconds and it is not a prescription. | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_195702_0ca63cee-dac3-4280-b670-33d7decf0005.png) | Acw9NmYe15OY4yPE… | USE with motion change (strap already seated; press-and-lift), barefoot (minor) | USE — seated press-and-lift on the near (left) knee; barefoot at home (continuity flag) |
| HK3-01 | Every week somebody brings me a scan of a knee and asks what can be do | pip | [png](https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_194836_cb17eb2a-f5b5-4c6f-b7bc-89368c528cbf.png) | AQrdyND1cvPCPXYd… | USE | USE — scan slid from envelope across the desk, doctor and patient hands |

## Drive folder IDs
```
{
 "task_folder": "1j0QiaFzwqK1NHlQH3TCZ3Qf5gsPQMZ49",
 "OUTPUT": "1OABbJ8mSJqcXWVJU7jqCcEcwlPyXrZcj",
 "01_ABSORPTION": "1okypXh4fdkzZx1on56ghpXwjXFoIcE8o",
 "02_CAST": "1w0VSVugitN0O2LpKSyMH37K-8MTu8rKp",
 "03_LOCATIONS": "1AnrCVDxQNvBIiZDYce4rN0tngmeXWOGZ",
 "04_VOICE": "1VTTeUA56wWAnkPkCVTHMIImPvFrs0Rpu",
 "05_HOOKS": "1-n9xVAtqPOIscwYyUQyW9loMkpVkffPw",
 "06_TALKING_HEADS": "1F438WprKYXYzmUZGEsolL4FPkDTHua23",
 "07_BROLL": "1HkWd5ZE2YgHLhAAGViAkqfzw0Wn79Pr4",
 "08_EDIT": "1m9EHuBN6jxSJRuYKah5U0b7UZ1LjEKkc"
}
```

Media are indexed by link (the connector cannot take the video bytes); the finished videos are delivered with this run's report.