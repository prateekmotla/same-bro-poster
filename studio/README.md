# Same Bro studio (animation pipeline)

Code that makes the Same Bro videos (pycairo vector animation → ffmpeg). Saved here so it survives between sessions.

- `core/` — characters (sid2, chars, body: full-body Sid / Live Bhai / Rohan), environments (env: room, canteen, metro, street, studio), UI widgets, colour grade (fx = 9:16, fxw = 16:9), thumbnail system.
- `long1/` — long video "How Live Traders REALLY Make Money" (script, timings, renderer, sound, mix).
- `short02/` — short "Live Traders Are Fooling You".

Setup in a fresh machine: copy `core/*` next to the renderer (scripts expect `/home/claude/sid/{v2,v3,long1}` on sys.path), `pip install pycairo numpy scipy pillow`, fonts Poppins + Inter Display, ffmpeg.
Voice (since 5 Nov 2026): ElevenLabs eleven_v4, "Rinku – Deep, Casual and Cool" (voice_id HOHisvZQEvTy8Ddc7Z83) on the new ElevenLabs account; Prateek no longer wants his cloned voice. Line timing: silence gaps (vshort.line_times) unless words.json exists. Hindi words in Devanagari, English in Latin in vo.txt. Word timings: ElevenLabs Scribe (creative_transcribe_audio) saved as words.json next to vo.mp3 — shorts/vshort.py reads it.
Music (since 2 Nov 2026): core/music2.py — code-generated dark half-time trap/lo-fi bed, unique key/tempo/motif per video (seed = folder name), mood tense/chill/warm, ~14 dB under the voice and ducked on words. Used by shorts/vshort.py render (set sh.mood) and long1/mix_generic.sh. The old bed.wav / audio_generic bed is retired for voiced videos.
