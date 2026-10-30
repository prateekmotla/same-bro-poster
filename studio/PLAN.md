# Same Bro — batch plan (week of Mon 26 Oct 2026)
Last producer run: Thu 29 Oct, ~1:30–2:30 AM IST.

Slots (IST): shorts 9 AM / 1 PM / 7 PM / 9 PM daily (9 PM added 31 Oct); long 6 PM Mon/Wed/Fri. Poster posts the next approved queue item (folder-name order) per type.
RULES (from Prateek): every short = its OWN topic (no re-cuts of longs). Shorts = "hidden truth / exposé" + "this is me" angle, English captions, fact-checked with source tag.
**ELEVENLABS OFF (Prateek, 29 Oct 2026): do NOT use ElevenLabs at all — no voiceovers, no Scribe transcription.**
**NEW FORMAT: TEXT-ONLY shorts** (Prateek's idea) — story told in on-screen text + music bed + pop/whoosh SFX; works muted and with sound. Engine studio/shorts/tshort.py (TextShort). Templates: s21_chips, s22_ninetynine, s23_airport. Lines ≤ ~18 words (story card fits 3 rows, keep overlays above y 1400).
Re-cut shorts only as emergency backup if ElevenLabs credits run out.
Helper: studio/queue_short.py (copy to /home/claude/sid/). Shorts need studio/shorts/bed.wav at /home/claude/sid/shorts/bed.wav.
New shorts (s15+) use studio/shorts/kit.py (panels, rows, full cards, stamps, bars, checkout/SMS phone screens, generic packet). Copy it with the rest of studio/shorts/*.
TODO: repo history grows ~1 GB/week of video; move videos to GitHub Release assets before it nears 5 GB (.git was ~565 MB on 29 Oct).
Render tip: max 2 renders at once (8 GB RAM). Bash run_in_background was unavailable again; `setsid nohup ... &` works. 2 shorts in parallel ≈ 12–13 min.
Glyph tip: Poppins has no arrow glyphs (→ ↑ ↓ show as boxes). Use ">" or words.

## CONTENT DIRECTION (Prateek, 31 Oct 2026) — overrides older topic ideas
- Daily mix: 2 of 3 shorts = MISTAKES of young traders / new SIP investors (checking portfolio daily, stopping SIP in falls, F&O lottery mindset, tips, averaging down, IPO FOMO...). 1 of 3 = TRENDING money/tech news of the week (gold & silver price moves and WHY, hot IPOs, big tech news) — research it the same day, latest numbers only.
- PROVEN WINNER (Prateek, 31 Oct): 013 "Same ₹10, LESS Biscuit" (shrinkflation) did well on YouTube — people love learning interesting hidden truths about daily-life things they never noticed. So: the 3rd daily slot ALTERNATES between trending money/tech news and an everyday hidden-truth topic (like shrinkflation). Apply the same "you see it daily but never knew why" feel to the trader/SIP mistake shorts too.
- Every short ENDS with a clear solution/rule + a one-line MORAL card. Most important/interesting thing first, solution last.
- Education only: never recommend a specific stock/fund/IPO or give buy/sell calls (SEBI finfluencer rules). Fact-check every number with a source.
- NEXT 4 SHORTS, make in THIS order (Prateek picked, 31 Oct): 
  1. Expiry-day option buying: dream of turning ₹5k into ₹50k on expiry, ends losing it all (theta decay, lottery mindset; SEBI F&O study numbers; angle must differ from 003 "91% lose") — moral: don't trade expiry like a lottery.
  2. "Buy every dip" — a dip can be the start of a big fall; lump sums into every dip with no plan. Moral: invest wisely, with a plan/SIP, not FOMO.
  3. Averaging down a falling stock (catching a falling knife) — moral: average a good business, not a falling price.
  4. Booking profits early but holding losers forever (disposition effect) — moral: cut losers, let winners run.
- 3rd-SLOT EVERYDAY HIDDEN-TRUTH topics (Prateek picked, 31 Oct) — use these in this order when the 3rd slot is an everyday topic (alternate with trending money/tech news; Dhanteras/gold news is timely in the first week of Nov):
  1. Free Wi-Fi isn't free — cafés/airports trade it for your data.
  2. "Multigrain" = mostly maida — how ingredient order / labels fool you (FSSAI rules).
  3. Phone storage always full — why "storage full" pushes you to paid cloud.
  4. Water ₹20 outside, ₹100 at the airport — is MRP really fixed? (legal metrology rules, airport/multiplex cases).
  5. Service charge? Don't pay — restaurants can't force it (CCPA guidelines, Delhi HC).
- DIWALI SERIES (Prateek, 31 Oct): ONE Diwali reel EVERY day Mon 2 Nov – Sun 8 Nov (Diwali), as an EXTRA 4th short (9 PM slot is new). Queue order must put exactly one Diwali short per day among the 4. Sun 8 Nov = MUHURAT TRADING: explain what it is and WHY it happens (Samvat new year, tradition), whether beginners should trade it or not (honest, education only), end with advice + moral. Other Diwali topics: pending Prateek's pick — see chat; if not set, use Diwali-money angles that fit the channel (gold buying on Dhanteras, Diwali bonus, Samvat returns).
- Mistake topic bank: SIP checked daily (loss aversion), stopping SIP when market falls, 8 funds = same stocks (over-diversification), picking fund by last year's return, weekly-expiry option buying, Telegram tip / pump & dump, averaging down a falling stock, selling winners early & holding losers, revenge trading after a loss, margin/MTF leverage, investing with no emergency fund, applying to every IPO for listing gains, jewellery as "investment" vs gold ETF/digital options, panic when gold/silver falls.

## Queue / status
- [x] 002 Live traders · [~] 003 91% lose (YouTube OK; Instagram FAILED 'API access blocked' — still failing every slot as of 28 Oct 7 PM. Meta has blocked the app/token; Prateek must fix in Meta App Dashboard. Poster advances each platform separately; IG catches up from 003 once unblocked)
- [x] Instagram token refresh no longer needs GH_PAT: weekly workflow stores the refreshed token encrypted in ig_token.enc (key = YT_CLIENT_SECRET+IG_USER_ID secrets); scripts/ig_token.sh loads it for post/ig-check
- [x] 100 long Live traders (Mon 6 PM)
- [x] 004 gym business · [x] 005 credit card minimum due · [x] 006 sale trick (Tue) — YouTube only
- [x] 007 no-cost EMI · [x] 008 regular vs direct MF · [x] 009 task-job scam (Wed) — YouTube only
- [x] 101 long Why you can't stop scrolling at 2 AM (Wed 6 PM)
- [ ] 010 red notification dot (Thu 9 AM) · [ ] 011 coaching topper ads (Thu 1 PM) · [ ] 012 'only 2 left' (Thu 7 PM)
- [ ] 102 long Salary aate hi khatam (Fri 6 PM)
- [ ] 013 shrinkflation (Fri 9 AM, s15_shrink) · [ ] 014 delivery app markup (Fri 1 PM, s16_delivery) · [ ] 015 COD handling fee / drip pricing (Fri 7 PM, s17_cod)
- [ ] 016 free-trial AutoPay trap (Sat 9 AM, s18_trial) · [ ] 017 dating apps business (Sat 1 PM, s19_dating) · [ ] 018 insurance agent commission (Sat 7 PM, s20_policy)
- [ ] 019 chips packet half air (Sun 9 AM, text-only, s21_chips) · [ ] 020 why prices end in 99 (Sun 1 PM, s22_ninetynine) · [ ] 021 airport chai price (Sun 7 PM, s23_airport)
- Next needed: Mon 2 Nov 9 AM / 1 PM / 7 PM shorts (text-only). Long slots Mon 2 Nov, Wed 4 Nov, Fri 6 Nov 6 PM are EMPTY: longs need a voiceover and ElevenLabs is off — Prateek to decide (own voice recording, or a text-only long format)
- Backups (voiced, generic): s04 "kal se pakka", s05 Instagram comparison
- Topics used: coaching topper ads (011), false urgency (012), shrinkflation (013), delivery-app menu markup (014), COD fee/drip pricing (015), free-trial subscription trap (016), dating-app gender ratio/boosts (017), endowment vs term commission (018), chips packet air/slack fill (019), ₹99 left-digit pricing (020), airport food prices (021)
- Topic ideas next: fantasy/betting apps & the 2025 online gaming law, protein/"healthy" snack labels (FSSAI), BNPL/'pay later' late fees, multiplex popcorn price (why cinemas earn from F&B), cashback that's really coins/points, phone 'storage full' → cloud upsell, festive-sale 'bank offer' fine print, loan apps' 'zero interest' processing fee, refurbished/'open box' tricks, PG/hostel brokerage, gold 'making charges'
- Long idea for Mon 2 Nov: "Dark patterns: 5 tricks shopping apps use on you" (CCPA 13-pattern list + fixes) — can reuse facts from 012/015/016 (false urgency, drip pricing, subscription trap)
- ElevenLabs: 6 voiceovers on 29 Oct ≈ 5,000 credits. Now switched OFF by Prateek. Backups s04/s05 have no vo.mp3 in the repo. Text-only format fills the gap.
