# TEST 217: Flurry, Critical Strike, Rapid Fire, Precise Shot, Charged Shot, Cautious, and the speaker's gates

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my talk bed are in `KOTOR_RPG_MAIN_WORK/media/screens/test-217/` (MAIN_WORK `523498ee`). The step-by-step notes are below the table; there's no separate log.

## Build

- **App**: main `197d5d4`, a worktree beside my clone. `gate.py --at 197d5d4`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at 197d5d4, 5411 tests, 0 failed"; ARCHIVE last green at 197d5d4. Lodestar `2d438df` = lock = compiled. Built through the lock in 10.2 s; git status clean.
- **Settings**: defaults. **Shelf** `411c1e2`, synced; check_shelf clean (33/125).
- **Beds**: `author_tester_test217_saves.dart` (Flurry One, Rapid One, Cautious One), with pristine copies kept so a replay starts clean. My own **tester-217** "Talk Room": Talk Human (Human Soldier 4), companion Bith Mate (Bith Soldier 4), and a copy of the Endar Spire's Sith Trooper with its `trooper-challenge` dialogue (reply "you-are-speaking" gated `species = "human"`).

## Summary: all pass except three parts not reached; one small item

| # | Check | Result |
|---|---|---|
| 1 | Flurry One | **PASS, two parts not reached**. See 1a–1e |
| 2 | Rapid One | **PASS, the critical not reached**. See 2a–2c |
| 3 | Cautious One | **PASS on the numbers, the label not seen** (small 1). Stealth +7 = Dexterity 4 + 3; Demolitions +16 = Intelligence 3 + the Micro-Optics' Demolitions +10 + 3. Neither is +6. No "Master Cautious +3" line appears on the Skills page, and the hide roll shows only "hidden — 26 beat 4", so the +3 isn't visible in any terms |
| 4 | Speaker's gates | **PASS (species)**. As Talk Human the trooper offers six replies, including "3. [Human] You are speaking to a commissioned officer of the Republic."; controlling Bith Mate it offers five, without it. No dialogue on the shelf has a background gate, so that half is unexercised |
| 5 | gate-and-grant notes | **PASS**. The notes end "THE GRANT IS SEEN ON THE FEATS TAB … while the mask is worn the player's Feats tab lists Weapon Focus: Blaster and Weapon Focus: Blaster Rifle, and the mask's `+2 Dexterity` proves it is worn." |
| 6 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 54 ("reg217"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 114 of 196) |

### 1. Flurry One

- **1a Flurry**: three lines, each "… d20 14 + attack 8 + Strength 3 − Flurry 4 · needed 10 — hit …". Before it the Brute "needed 14" against me; after it, "needed 12" (Defence −2). The line doesn't name the −2.
- **1b Critical Strike on the brute**: "… threat confirmed … 2d10 2+4 + Strength 4×2 × 2 critical · 353 left · d20 2 + fortitude 2 = 4 vs 21 · stunned". Log: "Brute is stunned." In round 3 the brute's turn is "Brute is stunned"; a round later it acts again ("Brute: unarmed · … needed 13 — miss").
- **1c Defence −1**: the round after a Critical Strike the Brute "needed 13" (14 − 1). At the start of my turn the Defence line reads 14 again.
- **1d Threat span**: a natural 18 threatened: "rolled 29 — d20 18 … threat confirmed: rolled 30 … × 2 critical". 18–20 confirmed.
- **1e Ironhide**: "d20 17 + fortitude 12 + Constitution 10 = 39 vs 21 · slowed".
- **1f Flurry into the weakling**: "… damage 13 … −10 left · dies"; the log has one Flurry One line and "Weakling dies", nothing after, and the Brute stayed at 353.
- **Not reached**: a missed first swing. Against the brute's "needed 10" with +11 every Critical Strike hit (11 in a row, including a d20 3); only a natural 1 misses. Flurry One holds no off-hand weapon, so "even if the off hand hits" can't come up with this save.

### 2. Rapid One

- **2a Rapid Fire**: three shots, each "… − Rapid Fire 4 − point blank 4 · needed 10".
- **2b Precise Shot**: "… d20 2 + fortitude 2 = 4 vs 20 · stunned".
- **2c Charged Shot on the brute**: "… − Charged Shot 3 … damage 8 — 1d8 4 + 1d6 1 + Dexterity 3 · 361 left · prone — d20 16 = 16 vs 21 · takes hold"; the brute moved from beside me (column 5) to column 8, 3 squares east.
- **Gunman**: 19 Charged Shots over two runs, never a prone or knockback line.
- **Not reached**: a confirmed critical. One natural 20 ("threat not confirmed: rolled 6 …") in two runs; Rapid One fell both times (after 9 and 11 rounds).

## Small

1. Cautious One's Skills page shows only the Bonus total (+16, +7); "Master Cautious +3" appears nowhere on it, on hover, or in the hide roll.

Seen, not filed:
- The trooper's "My mistake." loops back to "This deck is sealed. Turn around." and Escape doesn't close the conversation, so the only ways out are the bribe, the checks or a fight. That's the shelf's dialogue as written (`my-mistake` → `this-deck-is`).
- Flurry and Critical Strike damage add "Strength 4" against "Strength 3" on the attack (the PT-2222 1.5×, ruled).

KNOWN, not filed: tiers 2 and 3 and the chains' extras.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
