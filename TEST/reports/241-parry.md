# TEST 241: Parry (Parry, Riposte, Counter Strike)

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-241/`; names in brackets below are files there. The log lines are quoted from the in-game Combat log (Journal > Messages > Combat), read by OCR and checked against the screenshot where a line was garbled.

## Build

- **App**: main `0ee88fb`, a worktree beside my clone. `gate.py --at 0ee88fb`: "SENDABLE — 5 warning(s)"; "FOR TESTER — CORE at 0ee88fb, 5735 tests, 0 failed"; ARCHIVE last green at 0ee88fb.
- **Lodestar**: the lock pins `9050943`, and that is what compiled (package_config.json), as the order says.
- **Settings**: defaults (no settings.json) at the start. **Shelf**: `222a7a8`, check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: all 22 `author_tester_*` tools ran first time with no errors, the parry tool included. Every run starts from a pristine copy of its save in a relaunched app.
- Every step ran on this build.

## Summary: every step passes, no findings

| # | Check | Result |
|---|---|---|
| 1 | Gameplay row | **PASS**. "Parry: Ask" by default. |
| 2 | Parry One, Always | **PASS**. One parry, a strike back at −4, no damage for the turned blow; reactions 3 to 2. |
| 3 | Riposte One, Always | **PASS**. Two parries, strike backs at −2, half again the damage, rounded down. |
| 4 | Counter One, Always | **PASS**. Three parries, strike backs at no penalty, double damage. |
| 5 | Ask | **PASS**. Asked before each blow, the Charger before it walks; No lands; Yes on a miss spends nothing. |
| 6 | Never | **PASS**. No parry line in five rounds. |
| 7 | Gun One | **PASS**. No parry; blows land. |
| 8 | The Fencer parries you | **PASS**. Its losses and a win: my blow misses, then "Strike back: Fencer attacks …". |
| 9 | No reaction to a strike back | **PASS**. Seen in both directions, with reactions in hand. |
| 10 | TEST 240's checks | **PASS**. The hub shows the raised score before Accept; Power One and Power Four both listed. |
| 11 | Dice; regression | **PASS**. SAME17; slot 78 to 79, a mid-fight save and load, the fight won. |

## 1: Options > Gameplay

The page lists Opportunity attack: Ask, Force Deflection: Always, Force Redirection: Ask, and **Parry: Ask** (`s1-gameplay`). Its text: "A melee blow at you would hit: turn it with an opposed attack roll, for one reaction. On a win the blow misses and you strike back (Parry -4; Riposte -2 for half again the damage; Counter Strike, no penalty, for double)." `−` turned it to "Parry: Always" (`s2-always`), and settings.json then read `"reactions":{"parry":"always"}`. For steps 5 and 6 I set Ask and Never in settings.json before launching.

## 2: Parry One, Always

Bump Right; the Fencer opens round 1 (`b1-log`):

> Fencer attacks Parry One : \*hit\* : (16 + 8 = 24)
> Parry One parries: 9 + 15 = 24 vs. attack 24
> the attack misses
> Strike back: Parry One attacks Fencer : \*hit\* : (10 + 11 = 21)
> Parry One damages Fencer for 11 damage

- A tie, and hers. No "Fencer damages Parry One" line for the turned blow. Her plain attack bonus is 15 (her own swings read "+ 15"), so 11 is 15 − 4.
- **Once only**: rounds 2 to 4 have six more hits on her (the Charger and the Fencer, including two critical hits), and none is parried (`b4-log`).
- **The pip**: "Reactions (out of turn): three" before any reaction (`a1-q`, the same save); after the parry the portrait hover reads "move 5 of 5 · reactions 2 of 3" (`b1-hovslot`), still 2 of 3 after round 4 (`b4-hov`).

## 3: Riposte One, Always

(`r5-logup`, `r5-log`, `fr0-logup`)
- Round 1: "Riposte One parries: 9 + 15 = 24 vs. attack 24", then "Strike back: Riposte One attacks Fencer : \*hit\* : (10 + 13 = 23)" and "Riposte One damages Fencer for 16 damage".
- Round 2: "Charger attacks Riposte One : \*hit\* : (15 + 3 = 18)", "Riposte One parries: 14 + 15 = 29 vs. attack 18", then "Strike back: Riposte One attacks Charger : \*hit\* : (5 + 13 = 18)" and "Riposte One damages Charger for 9 damage".
- Rounds 3 to 5: four more hits on her, none parried. Reactions 1 of 3 at the end (`r5-hov`).
- 13 is 15 − 2.
- **The damage**: the status box only keeps the round's last line, so the strike back's damage roll is not on screen. I aligned the runs instead: the three saves share one dice stream (every round-1 roll is identical), and so do the strike backs.
  - At the Fencer, all three rolled d20 10 and did Parry 11, Riposte 16, Counter 22.
  - At the Charger, all rolled d20 5 and did Riposte 9, Counter 12.
  - floor(11 × 1.5) = 16 and floor(6 × 1.5) = 9 (with 2 × 6 = 12 at the Charger). The Fencer's health agrees: 389 after Parry One's strike back, 384 after Riposte One's.

## 4: Counter One, Always

(`c6-logtop`, `c6-logup`, `c6-log`)
- Round 1: "Counter One parries: 9 + 15 = 24 vs. attack 24", "Strike back: Counter One attacks Fencer : \*hit\* : (10 + 15 = 25)", "Counter One damages Fencer for 22 damage".
- Round 2: the Charger (18) parried, 29 vs 18; strike back "(5 + 15 = 20)" for 12. Then the Fencer's critical hit (19 + 8 = 27) parried, 35 vs 27; strike back "(13 + 15 = 28)" for 10.
- Rounds 3 to 6: none parried. Reactions 0 of 3 at the end (`c6-hov`).
- No penalty (15). Double: 22 = 2 × 11 and 12 = 2 × 6 against the same dice as steps 2 and 3, and 10 is even.

## 5: Ask, Parry One

- **The Fencer's question** (`a1-q`): "Parry / Fencer swings at you / one reaction · 3 left · spent only if the blow would hit", Yes and No. I answered **No**: "Fencer attacks Parry One : \*hit\* : (16 + 8 = 24)", then "Fencer damages Parry One for 11 damage". The blow lands.
- **Blade's question** came next (`a2-q`). I answered **Yes**; its blow missed, "(9 + 3 = 12)". There was no parry line and reactions stayed at 3 of 3 (`a3-log`, `a3-hov`).
- **Round 2, the Charger's question** came while its token was still at (6,4), visible behind the dialog at (1242, 435) (`a4-chargerq`). That is before its walk. Yes; it missed (13), and the Fencer's question that followed still said "3 left".
- **The Fencer, Yes**: "Fencer attacks Parry One : \*hit\* : (17 + 8 = 25)", then "Parry One parries: 15 + 15 = 30 vs. attack 25", "the attack misses", and "Strike back: Parry One attacks Fencer : \*hit\* : (4 + 11 = 15)" for 8. Reactions 2 of 3 (`a5-log`, `a5-hov`). Blade's next blow was not asked about, since her one use was spent.

## 6: Never, Counter One

Five rounds (`n5-logup`, `n5-log`). There were no prompts. The round-1 blow that she parried on Always, "Fencer attacks Counter One : \*hit\* : (16 + 8 = 24)", now reads "Fencer damages Counter One for 11 damage". Neither log has a "parries" or "Strike back" line. Reactions 3 of 3 at the end (`n5-hov`).

## 7: Gun One, Always

Five rounds (`g5-logup`, `g5-log`): no parry or strike back line. "Fencer attacks Gun One : \*hit\* : (16 + 10 = 26)" lands for 11, and so do the later hits. Reactions 3 of 3 (`g5-hov`).

## 8: The Fencer parries you

I clicked the Fencer at (3,3) on my turns, over several runs: Parry One, Riposte One and Counter One, waiting 0 to 3 turns first (`f1-log`, `f4-log`, `fc-log`, `fr0-*`, `fp1-*`, `fp2-*`, `fn0-*` to `fn3-*`).
- **Losses**: "Fencer parries: 14 + 8 = 22 vs. attack 30", then "Parry One damages Fencer for 8 damage". The blow lands, as the rule says. Others: 9 + 8 = 17 vs 35; 2 + 8 = 10 vs 34; 3 + 8 = 11 vs 24; 20 + 8 = 28 vs 34.
- **It parries twice a fight, no more.** The bed gives it two reactions, so after two tries the rest of my blows land with no parry line.
- **Wins**:
  - Parry One, waiting two turns (`fp2-log`, round 4):
    > Parry One attacks Fencer : \*hit\* : (2 + 15 = 17)
    > Fencer parries: 15 + 8 = 23 vs. attack 17
    > the attack misses
    > Strike back: Fencer attacks Parry One : \*hit\* : (12 + 8 = 20)
    > Fencer damages Parry One for 16 damage
  - There is no damage line for my blow. The strike back is at +8, the Fencer's full bonus (Counter Strike, no penalty), and 16 is even.
  - The same win happened in `fn2` with Counter One.

## 9: No reaction to a strike back

- **A strike back is not parried**: in `fr0`, Riposte One's round-1 strike back hits the Fencer, "(10 + 13 = 23)", with no "Fencer parries" line. The Fencer had both reactions then, and it parried twice later in that fight. The same holds in every Parry/Riposte/Counter run.
- **Nobody strikes back at a strike back**: `fn2` (Counter One, on Never for three rounds, then switched to Always in-game before her first swing, `fn2-set`).
  - Round 4: she parried the Fencer (her 1st use, 34 vs 25).
  - The Fencer then won against her blow, and its strike back, "(12 + 8 = 20)", hit her for 16 with no parry line. She was on Always with two uses and two reactions left.
  - In round 5 she parried twice more, "1 + 15 = 16 vs. attack 19" (lost; the Charger's 5 damage lands) and "12 + 15 = 27 vs. attack 25", reaching three uses.
  - So the strike back was not passed over for want of uses.

## 10: TEST 240's checks

- **The hub**: no save is a Soldier 3 with the XP for 4. Every level-3 bed holds exactly 3000, and none carries an award that reaches 6000. So I used **Lu Eight** (Tester Attacks), Soldier 7 to 8, 28500 XP, needed 0 (`l1-sheet`). Level 8 also carries an ability point.
  - Level Up, then class OK. A "granted the following feat(s)" box listed Squad Tactics, Improved and Master Squad Tactics, then OK.
  - Attributes, then Strength 14 to 15, Remaining 1 to 0, then OK (`l5-attr-plus`).
  - **The hub reads "Strength 15 (+2)"** at once, with Skills now current and Accept not yet pressed (`l6-hub-after`; before, "14 (+2)", `l3-hub`).
  - Back, then Cancel on the Class page, to leave.
- **The load list**: the Tester Power card lists **Power One** (`p-1`). Tester Powers lists Fearless One, **Power Four** and Aura Saver (`p4-2`).

## 11: Dice and regression

- **Dice**: the right Dice One Quick Save; the first 17 lines match the TEST 206 baseline (SAME17).
- **Regression**: Icon Nine.
  - Loaded slot 78 (reg240, 11:24:08) and saved it as slot 79 ("reg241", 16:49:37).
  - A quick save mid-fight (16:49:42), then loaded slot 79.
  - Won the fight: "Icon Nine: 85 of 196", "FIGHT OVER".

## Odd, not filed

- Enemies hit Gun One at +2 over the others ("Fencer attacks Gun One : (16 + 10 = 26)" against "(16 + 8 = 24)" at Counter One). Gun One holds a Blaster Pistol in melee, so this looks like the closed-on-a-ranged-weapon bonus, and I didn't file it.
- Step 10 ran on a Soldier 7 to 8, not 3 to 4, because no bed holds a ready Soldier 3 (see above).

## What I got wrong

- The OCR reads "RIPOSTE" as "Rmeoste", so the first Riposte load stopped at the name check and loaded nothing. A pattern allowing for the misread loaded it.
- My first Parry One win in step 8 was no use for step 9's second half: she had already spent her one use. I set up `fn0` to `fn3` (Never, then Always before swinging) for a case with uses in hand. `fn2` gave it.
