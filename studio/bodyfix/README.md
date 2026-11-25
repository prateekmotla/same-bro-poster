# BODY FIX series (25 Nov 2026)
50 animated health/body-signal shorts with Sid (constipation, bloating, nosebleed, ...). Format: hook -> A/B/C quiz -> answer + why -> fix steps -> "see a doctor if" -> share CTA. Rinku voice (eleven_v4, one take, atempo 1.08).
- `bodyfix.py` engine (on vshort.Short), `bodyfix_topic.py` scene builder, `topics_all.py` data for #2-#50 (#1 lives in sid/shorts/b01_constipation/make.py).
- Copy into /home/claude/sid/shorts after the usual studio setup; `gen_topics.py` makes b<NN>_<slug>/ folders.
- Queue: `queue/<096+N>b-body-fix-<NN>-<slug>` so each Body Fix posts right after one existing short (alternating).
