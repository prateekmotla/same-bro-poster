# Same Bro — batch plan (week of Mon 26 Oct 2026)
Last producer run: Sat 31 Oct, ~1:25–3:00 AM IST (scheduled run).

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
- NEXT 4 SHORTS, make in THIS order (Prateek picked, 31 Oct): [x] 1 = 022 · [x] 2 = 023 · [x] 3 = 024 queued 31 Oct · [~] 4 = script READY in studio/shorts/s27_winners (render + queue next run)
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
- QUEUE RULE: every Diwali short's meta.json MUST have "priority": true — the poster then posts it on Instagram in the same slot as YouTube, jumping the Instagram backlog (Prateek chose: Diwali first on IG, old backlog fills the other slots).
- DIWALI SERIES (Prateek PICKED each day, 31 Oct 01:28 — final): ALL Diwali shorts go out BEFORE Diwali (8 Nov). One per day as the EXTRA 4th short, in that day's 7 PM prime slot. Exact topics:
  - [x] QUEUED 017a · Sat 31 Oct (TODAY, 7 PM — URGENT, make first): "Why shagun ends in 1" — ₹101/₹501/₹1100: the real reasons behind the extra ₹1 (tradition/beliefs, explained respectfully), plus a fun money moral.
  - [x] QUEUED 020a · Sun 1 Nov: "Everything on sale, yet record profits?" — how festive sales still make companies money.
  - [x] QUEUED 023a · Mon 2 Nov: "90% of India's crackers come from one town" — Sivakasi, and why cracker prices jump every Diwali.
  - Tue 3 Nov: "Why is the Diwali bonus even a thing?" — history + Payment of Bonus Act, and how to use the bonus smartly.
  - Wed 4 Nov: "Digital gold isn't regulated" — what SEBI warned about digital gold; safer regulated options exist (no product names).
  - Thu 5 Nov (eve of Dhanteras): "Does gold really rise after Dhanteras?" — buy-on-Dhanteras belief vs what past prices show.
  - Fri 6 Nov (Dhanteras): "Diwali card party = F&O brain" — the same gambling instinct, bigger table; moral.
  - Sat 7 Nov (eve of Diwali): MUHURAT TRADING — what it is, WHY it happens (Samvat new year, tradition), should beginners trade it or not (honest, education only), advice + moral.
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
- [ ] 017a why shagun ends in ₹1 (Sat 31 Oct 7 PM, DIWALI, priority, s30_shagun)
- [ ] 020a festive sale: how do they still earn (Sun 1 Nov 7 PM, DIWALI, priority, s31_sale)
- [ ] 022 expiry-day option buying (Mon 2 Nov 9 AM, s24_expiry) · [ ] 023 'buy every dip' (Mon 1 PM, s25_dip) · [ ] 023a Sivakasi crackers (Mon 7 PM, DIWALI, priority, s32_crackers) · [ ] 024 averaging down (Mon 9 PM, s26_average)
- ORDER NOTE: 4 shorts/day now (9 AM, 1 PM, 7 PM, 9 PM). Diwali shorts use 'a'-suffixed folder numbers (017a, 020a, 023a) so they sort into that day's 7 PM slot. Expected: Sat 016/017/017a/018 · Sun 019/020/020a/021 · Mon 022/023/023a/024. If a poster run is ever skipped, everything shifts one slot — check before adding the next Diwali 'a' folder.
- Next needed: Tue 3 Nov 9 AM / 1 PM / 7 PM (Diwali: Diwali bonus) / 9 PM. READY-TO-RENDER scripts (made 31 Oct, not rendered due to the 6-per-run cap): s27_winners (NEXT-4 #4, disposition effect), s28_wifi (everyday #1, free Wi-Fi), s29_gold (trending: gold ~20% below Jan peak before Dhanteras — numbers as of 30 Oct; REFRESH prices before rendering or drop it, it overlaps the Thu 5 Nov Diwali gold topic). Suggested Tue: 025 winners (9 AM), 026 wifi (1 PM), 026a Diwali bonus (7 PM), 027 a trader/SIP mistake (9 PM). Long slots Mon 2 Nov, Wed 4 Nov, Fri 6 Nov 6 PM are EMPTY: longs need a voiceover and ElevenLabs is off — Prateek to decide (own voice recording, or a text-only long format)
- Backups (voiced, generic): s04 "kal se pakka", s05 Instagram comparison
- Topics used: coaching topper ads (011), false urgency (012), shrinkflation (013), delivery-app menu markup (014), COD fee/drip pricing (015), free-trial subscription trap (016), dating-app gender ratio/boosts (017), endowment vs term commission (018), chips packet air/slack fill (019), ₹99 left-digit pricing (020), airport food prices (021), shagun ₹1 tradition (017a), festive-sale economics/pre-sale price hikes (020a), expiry-day option buying/theta (022), buy-every-dip/2008 (023), Sivakasi cracker prices (023a), averaging down/Yes Bank (024)
- Topic ideas next: fantasy/betting apps & the 2025 online gaming law, protein/"healthy" snack labels (FSSAI), BNPL/'pay later' late fees, multiplex popcorn price (why cinemas earn from F&B), cashback that's really coins/points, phone 'storage full' → cloud upsell, festive-sale 'bank offer' fine print, loan apps' 'zero interest' processing fee, refurbished/'open box' tricks, PG/hostel brokerage, gold 'making charges', revenge trading after a loss, SIP stopped in a fall (2020 crash recovery), 8 funds = same stocks, gold/silver weekly move explainer (refresh each week)
- EMPTY LONG SLOTS (6 PM): Mon 2 Nov, Wed 4 Nov, Fri 6 Nov — no voiceover allowed (ElevenLabs off). Prateek to decide: own voice recording or a text-only long format.
- Long idea for Mon 2 Nov: "Dark patterns: 5 tricks shopping apps use on you" (CCPA 13-pattern list + fixes) — can reuse facts from 012/015/016 (false urgency, drip pricing, subscription trap)
- ElevenLabs: 6 voiceovers on 29 Oct ≈ 5,000 credits. Now switched OFF by Prateek. Backups s04/s05 have no vo.mp3 in the repo. Text-only format fills the gap.
