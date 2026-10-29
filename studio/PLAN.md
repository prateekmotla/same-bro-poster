# Same Bro — batch plan (week of Mon 26 Oct 2026)
Last producer run: Thu 29 Oct, ~1:30–2:30 AM IST.

Slots (IST): shorts 9 AM / 1 PM / 7 PM daily; long 6 PM Mon/Wed/Fri. Poster posts the next approved queue item (folder-name order) per type.
RULES (from Prateek): every short = its OWN topic (no re-cuts of longs). Shorts = "hidden truth / exposé" + "this is me" angle, English captions, fact-checked with source tag.
**ELEVENLABS OFF (Prateek, 29 Oct 2026): do NOT use ElevenLabs at all — no new voiceovers, no Scribe transcription.** Only queue videos whose voice audio already exists; otherwise leave the slot empty and tell Prateek.
Re-cut shorts only as emergency backup if ElevenLabs credits run out.
Helper: studio/queue_short.py (copy to /home/claude/sid/). Shorts need studio/shorts/bed.wav at /home/claude/sid/shorts/bed.wav.
New shorts (s15+) use studio/shorts/kit.py (panels, rows, full cards, stamps, bars, checkout/SMS phone screens, generic packet). Copy it with the rest of studio/shorts/*.
TODO: repo history grows ~1 GB/week of video; move videos to GitHub Release assets before it nears 5 GB (.git was ~565 MB on 29 Oct).
Render tip: max 2 renders at once (8 GB RAM). Bash run_in_background was unavailable again; `setsid nohup ... &` works. 2 shorts in parallel ≈ 12–13 min.
Glyph tip: Poppins has no arrow glyphs (→ ↑ ↓ show as boxes). Use ">" or words.

## Queue / status
- [x] 002 Live traders · [~] 003 91% lose (YouTube OK; Instagram FAILED 'API access blocked' — still failing every slot as of 28 Oct 7 PM. Meta has blocked the app/token; Prateek must fix in Meta App Dashboard. Poster advances each platform separately; IG catches up from 003 once unblocked)
- TODO Prateek: add a GH_PAT secret (fine-grained PAT, Secrets: read/write on this repo) or the weekly IG token refresh fails and the token expires ~late Dec
- [x] 100 long Live traders (Mon 6 PM)
- [x] 004 gym business · [x] 005 credit card minimum due · [x] 006 sale trick (Tue) — YouTube only
- [x] 007 no-cost EMI · [x] 008 regular vs direct MF · [x] 009 task-job scam (Wed) — YouTube only
- [x] 101 long Why you can't stop scrolling at 2 AM (Wed 6 PM)
- [ ] 010 red notification dot (Thu 9 AM) · [ ] 011 coaching topper ads (Thu 1 PM) · [ ] 012 'only 2 left' (Thu 7 PM)
- [ ] 102 long Salary aate hi khatam (Fri 6 PM)
- [ ] 013 shrinkflation (Fri 9 AM, s15_shrink) · [ ] 014 delivery app markup (Fri 1 PM, s16_delivery) · [ ] 015 COD handling fee / drip pricing (Fri 7 PM, s17_cod)
- [ ] 016 free-trial AutoPay trap (Sat 9 AM, s18_trial) · [ ] 017 dating apps business (Sat 1 PM, s19_dating) · [ ] 018 insurance agent commission (Sat 7 PM, s20_policy)
- Next needed: Sun 1 Nov 9 AM / 1 PM / 7 PM shorts; long for Mon 2 Nov 6 PM (not made this run — Fri slot is filled and Mon was >3 days out; next run should make it)
- Backups (voiced, generic): s04 "kal se pakka", s05 Instagram comparison
- Topics used: coaching topper ads (011), false urgency (012), shrinkflation (013), delivery-app menu markup (014), COD fee/drip pricing (015), free-trial subscription trap (016), dating-app gender ratio/boosts (017), endowment vs term commission (018)
- Topic ideas next: fantasy/betting apps & the 2025 online gaming law, protein/"healthy" snack labels (FSSAI), BNPL/'pay later' late fees, chips packet "half air" (nitrogen + slack fill), airport/multiplex ₹250 chai (concession rent), 'MRP ₹99' charm pricing, cashback that's really coins/points, phone 'storage full' → cloud upsell, festive-sale 'bank offer' fine print, loan apps' 'zero interest' processing fee, refurbished/'open box' tricks, PG/hostel brokerage, gold 'making charges'
- Long idea for Mon 2 Nov: "Dark patterns: 5 tricks shopping apps use on you" (CCPA 13-pattern list + fixes) — can reuse facts from 012/015/016 (false urgency, drip pricing, subscription trap)
- ElevenLabs: 6 voiceovers on 29 Oct ≈ 5,000 credits. Now switched OFF by Prateek. Backups s04/s05 have no vo.mp3 in the repo, so nothing voiced is left to fill Sun 1 Nov onward.
