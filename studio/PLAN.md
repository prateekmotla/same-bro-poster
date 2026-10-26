# Same Bro — batch plan (week of Mon 26 Oct 2026)
Last producer run: Tue 27 Oct, ~1:30 AM IST.

Slots (IST): shorts 9 AM / 1 PM / 7 PM daily; long 6 PM Mon/Wed/Fri. Poster posts the next approved queue item (folder-name order) per type.
RULES (from Prateek): every short = its OWN topic (no re-cuts of longs). Shorts = "hidden truth / exposé" + "this is me" angle, English captions, fact-checked with source tag.
Re-cut shorts only as emergency backup if ElevenLabs credits run out.
Helper: studio/queue_short.py (copy to /home/claude/sid/). Shorts need studio/shorts/bed.wav at /home/claude/sid/shorts/bed.wav.
TODO: repo history grows ~1 GB/week of video; move videos to GitHub Release assets before it nears 5 GB.
Render tip: max ~4 render processes at once (8 GB RAM, OOM otherwise). Use run_in_background Bash, not nohup.

## Queue / status
- [x] 002 short Live traders (posted Mon 1 PM) · [~] 003 short 91% lose (Mon 7 PM: YouTube OK, Instagram FAILED 'API access blocked'. Health check (Actions → 'Instagram health check') shows even /me is blocked = Meta has blocked the app/token; Prateek must fix in Meta App Dashboard. Poster now advances each platform separately, so YouTube keeps posting; IG catches up from 003 once unblocked)
- TODO Prateek: add a GH_PAT secret (fine-grained PAT, Secrets: read/write on this repo) or the weekly IG token refresh fails and the token expires ~late Dec
- [x] 100 long Live traders (Mon 6 PM) — swap in same_bro_long_01_fixed.mp4 (caption fix) if ready
- [ ] 004 short gym business (Tue 9 AM)  · [ ] 005 credit card minimum due (Tue 1 PM) · [ ] 006 sale trick (Tue 7 PM)
- [ ] 007 no-cost EMI (Wed 9 AM) · [ ] 008 regular vs direct MF (Wed 1 PM) · [ ] 009 task-job scam (Wed 7 PM)
- [ ] 101 long Why you can't stop scrolling at 2 AM (Wed 6 PM)
- [ ] 010 red notification dot (Thu 9 AM) · [ ] 011 coaching topper ads (Thu 1 PM, studio/shorts/s13_topper) · [ ] 012 'only 2 left' false urgency (Thu 7 PM, s14_scarcity)
- Next needed: Fri 9 AM / 1 PM / 7 PM shorts; long for Mon 2 Nov 6 PM
- [ ] 102 long Salary aate hi khatam (Fri 6 PM)
- Backups (voiced, generic): s04 "kal se pakka", s05 Instagram comparison
- Topics used: coaching topper ads (011), fake scarcity/false urgency (012)
- Topic ideas next: dating apps business model, fantasy/betting apps & 2025 law, protein/"healthy" snack labels, insurance-investment plans commission, cash-on-delivery 'handling fee' (govt called it a dark pattern 2025), drip pricing at checkout (platform/convenience fee), food-delivery app prices vs restaurant menu, 'free' trial subscription traps (auto-pay mandates), shrinkflation (same price, smaller packet), BNPL/'pay later' late fees
- Long idea for Mon 2 Nov: "Dark patterns: 5 tricks shopping apps use on you" (CCPA 13-pattern list + fixes)
- Render note: Bash run_in_background was unavailable this run; used setsid nohup. 2 shorts in parallel took ~11 min.
