# TEST 226: Staggering Shot, Pinning Fire and Lockdown

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-226/` (MAIN_WORK `d4f17cd6`).

## Build

- **App**: main `054174d`, a worktree beside my clone. `gate.py --at 054174d`: "SENDABLE"; "FOR TESTER — CORE at 054174d, 5496 tests, 0 failed"; ARCHIVE last green at 054174d. Lodestar `4d6c401` = lock = compiled; built through the lock; git status clean.
- **Settings**: defaults (no settings.json). **Shelf** `194cc43`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test225_saves.dart` (Staggering, Stagger Plain, Staggering Pair), pristine copies kept.

## Summary: all pass; three parts not reached

| # | Check | Result |
|---|---|---|
| 1 | Staggering (DC 21) | **PASS, two parts not reached**. To measure pace, she shot the Weakling dead, walked to column 0 and fired from 5 squares. **Staggering Shot**: "1d8 6 + Dexterity 3 · 391 left · d20 15 = 15 vs 21 · slowed"; hover "slowed"; log "Brute is slowed. / Brute closes 2 squares — 5 to 3 · out of movement 3 squares short · Brute: unarmed · out of reach". **No −1s**: adjacent and slowed, the brute's attack totals "(8 + 3 = 11)", the same +3 as unslowed "(11 + 3 = 14)". **Pinning Fire**: "d20 15 = 15 vs 21 · held"; hover "held"; log "Brute is held. / Brute out of movement 5 squares short · Brute: unarmed · out of reach": it stays on its square and still takes its turn. **Lockdown**: "d20 17 − Lockdown 4 = 13 vs 21 · held", the brute stays at (3,4); Staggering Pair's "d20 12 − Lockdown 4 = 8 vs 21". **Control**: a plain shot, then the brute closes from (5,4) to (1,3) and attacks. **The hold ends at the start of her next turn**: the brute, acting after her, is held on its turn, and hover shows nothing on her turn. The Gunman, acting before her in the round: pinned, it still attacks ("Gunman attacks Staggering : *hit*"), hover "held" while she has acted, and nothing on her next turn. **Again**: Staggering Shot then Lockdown on consecutive turns reads only "held"; Pinning Fire on the Gunman again two turns later reads one "held". **A miss asks no save**: "Staggering Shot · … rolled 9 … needed 10 … — miss", the line ends there, hover clean. A natural 20 resists: "d20 20 = 20 vs 21 · resists". **Not reached**: (a) "keeps its Bonus": nothing in the yard visibly spends a Bonus; (b) a refresh over a live hold: one shooter with one shot a turn can't overlap a hold that ends at her next turn |
| 2 | Stagger Plain (DC 18) | **PASS, one part not reached**. "d20 20 = 20 vs 18 · resists": hover clean, nothing lands. "d20 13 = 13 vs 18 · slowed", and "17 vs 18 · slowed" twice. **Not reached**: a made save on an 18 or 19, in 21 shots over three runs. Since a natural 20 also makes DC 21, the 20 alone does not prove the DC |
| 3 | Staggering Pair | **PASS**. Each tier is one shot at "− dual-wield 3": "Staggering Shot · Blaster Pistol · … − dual-wield 3 − point blank 4 … d20 20 = 20 vs 21 · resists", "Pinning Fire · … d20 2 = 2 vs 21 · held", "Lockdown · … d20 12 − Lockdown 4 = 8 vs 21". **Control**: a plain Shoot is two: "Blaster Pistol · … hit · damage 10 …", then "off-hand: Blaster Pistol · … − dual-wield 3 … hit · damage 6 — 1d8 3 + Dexterity 3" |
| 4 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 63 ("reg226"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 116 of 196) |

KNOWN, not filed: the Flurry family's P P P O order; the flee and breakoff lines (not reached).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
