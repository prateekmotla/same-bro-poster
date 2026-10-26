# Same Bro studio (animation pipeline)

Code that makes the Same Bro videos (pycairo vector animation → ffmpeg). Saved here so it survives between sessions.

- `core/` — characters (sid2, chars, body: full-body Sid / Live Bhai / Rohan), environments (env: room, canteen, metro, street, studio), UI widgets, colour grade (fx = 9:16, fxw = 16:9), thumbnail system.
- `long1/` — long video "How Live Traders REALLY Make Money" (script, timings, renderer, sound, mix).
- `short02/` — short "Live Traders Are Fooling You".

Setup in a fresh machine: copy `core/*` next to the renderer (scripts expect `/home/claude/sid/{v2,v3,long1}` on sys.path), `pip install pycairo numpy scipy pillow`, fonts Poppins + Inter Display, ffmpeg.
Voice: ElevenLabs eleven_v4, voice "Rinku – Deep, Casual and Cool". Word timings: ElevenLabs Scribe.
