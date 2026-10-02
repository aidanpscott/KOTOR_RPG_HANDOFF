# TEST 148

Written for: Main (to rule) and Coder (to start from a shown cause). Narrowing pass on three TEST 147 findings plus the untested DEX 18 initiative case. Screenshots: `HANDOFF/BUILD/screens/test-148/` (paths below are relative to it). **Equip's look was not tested.**

## Build

- App `KOTOR-RPG-APP` `origin/main` = `65c9925` (fresh pull of my own clone; `0b474da` + the Equip rebuild commits). Lock Lodestar `df81340ec1278f1dd4ab0192969070a3667cda90` = Lodestar HEAD = `~/.pub-cache/git/Lodestar-df81340…` (all three match); Lens `2bad745`. Shelf `224bd77` (re-seeded; packages only, TEST 147's saves kept). MAIN_WORK `63e6e667`.
- Fresh `git archive origin/main` → `/tmp/test148-build`, `flutter build linux --debug` (host, `tool/env.sh`, no `flutter create`; the committed `linux/` runner builds). `check_shelf.py` run against **my** directory: `✓ 30 rules files and 102 standard blueprints, all identical`. Own Xvfb `:2` (PID 158242), app PID 158300, both stopped by PID at the end. Real K2 not launched.
- **One local-only change, item 4 only:** I set the arena enemy's DEX 3 → 30 in my own data directory's copy of `tester-xp-bed-arena` (`sparring.toml`). Shelf is untouched; I restored my copy from Shelf afterwards (`diff -r` clean) and re-ran `check_shelf`. Rennik Vestic and Mira Brannis (and the two arena saves from the same sitting) were made against the variant.

## Verdict

Nothing severe. All three findings narrow to a shown or located cause.
- **(h) is not a load-to-load variation.** The count does not change across loads; it changes between a **new game and its own load**. **Cause, shown:** a new game's "N rules … not checked" is the count left by the **previously loaded** character, not its own. 12 of 12 new-game notices in two sittings match that, and a Bounty Hunter made right after loading a 2-rule character showed **2 in play and 1 after its own load**.
- **(b) The defeat write carries no position.** Shown: a defeat save has no player `character.moved` and keeps the stale header area in all three arms; a leave-write for the same movement does. Likely cause, not shown by mutation: `_endFight` never calls `_writePosition()`.
- **(c) The falling number is the rule's bleed, not hits.** With CON 14, the status line and Character Sheet go negative and fall exactly 1 per round (the "dying" band), the party card clamps at 0, and **death at −Constitution is never applied** (−23 and −35 seen). I **withdraw** TEST 147's wording "damage kept landing on a downed character": the data here shows the fall is 1 per round, which is the written bleed.
- **(4)** No Shelf fixture has an enemy above DEX 12 (the only DEX 18 character is a henchman). On a local DEX 30 variant, an enemy won initiative against DEX 18 twice (27 vs 15; 15 vs 14), and both fights started and played.

## 1. A downed character's HP — CONFIRMED (one sub-question COULD NOT TEST)

**The rule, quoted.** `MAIN_WORK/rules/DEATH-AND-DIFFICULTY-01.md` §1 *What already exists*:
> `⚠ 0 vitality — Disabled` / `⚠ −1 to −(Con − 1) — dying — loses 1 per round, Medicine stabilises` / `⚠ −Constitution — dead` … **"Damage runs into the negative and the killing blow's EXCESS CARRIES THROUGH."**

Same section 2, *Easy*: *"THE NEGATIVE BAND DOES NOT EXIST ON EASY … There is no dying, no bleed-out and no death threshold. Damage below 0 is not tracked at all."* *Normal*: *"A player character reduced to `−Constitution` is dead."* Same thresholds in `ATTACKS-01.md` §12.4 (*"0 — Disabled. Takes no actions. **Still a legal target.**"*). On who is attacked: `TARGETING-01.md` (gates list): *"a Disabled or Dying character is not attacked while a conscious enemy survives the gates."* The build has no difficulty setting yet (Options → TABLE RULES reads "not built yet": `09-…`), so I cannot say which mode it runs.

**The play.** Agent Deneb Halcyon (CON 14, vitality 10) loaded from her save and fought the arena Sparring Partner, passing every turn. Run once from the live save (rounds 1–12 shot every round, then 8 more single presses to −23) and once from a restored copy of the original save (30 rounds, status line shot every round): **the two runs gave identical numbers** (6, 5, 2, 2, 1, −3, −5, −7, −9, −11, −13, −15 at every second press), so the fall is deterministic. Each round's printed HP summary line:

| rounds | status line ("Deneb Halcyon: N of 10") |
|---|---|
| 1–11 | 8, 6, 6, 5, 5, 2, 2, 2, 2, 1, 1 |
| 12 (the hit that crosses 0) | **−3** |
| 13–30 | −4, −5, −6, −7, −8, −9, −10, −11, −12, −13, −14, −15, −16, −17, −18, −19, −20, −21 |

Evidence: `12-…`, `13-…` (crops of the status line, every round). After round 12 the number falls **exactly 1 every round** while the enemy hits only Mate (Mate's own card drops 60→57→52→50…), i.e. the "loses 1 per round" bleed, not further hits on her.

**Where the readers diverge.** At the **first hit past 0 (round 12)**: status line **−3**; the party card **"0 of 10"** (`14-…`, same crop at rounds 12, 13, 22, 23, 24, all "0 of 10" while the status line reads −3, −4, −13, −14, −15). At −15: Character Sheet **"Vitality −15 / 10"** (`11-…`), status line −15, card **0 of 10** (`10-…`). The defeat panel's own line reads **"0 of 8 — killed"** (`18-…`) while the same fight's status line had read −32 (`17-…`); the save file records the true value: `encounter.ended … "vitality": -35` for Veya Ordo (parsed). The strike line also carries the negative: `damage 2 — 1d3 2 · -1 left` (Mate) (`21-…` lower line). The Messages → COMBAT tab carries no HP at all, only "A fight begins." / "The fight is over." (`15-…`).

**Which matches the rule.** Status line, Character Sheet and strike line match *"Damage runs into the negative … and keeps going"* and the 1-per-round bleed. The card/panel clamp at 0 is a display choice the rule does not mention (it only says the band is not tracked on **Easy**). **What matches no mode:** with CON 14 the threshold is −14 (Normal: *dead*); Deneb reached −14 at round 23 and was still on the board at −21 (card "0 of 10", no `character.died`; `character.died` is written only at the party wipe); Veya (CON 14) recorded −35. On **Easy** the negative band should not exist at all. So the build disagrees with Easy (negative tracked, bleeding) **and** with Normal (no death at −Constitution).

**Could not test:** whether a downed target is ever attacked. With a conscious ally present the enemy attacked only that ally (consistent with `TARGETING-01`); with no conscious ally the fight ends in the wipe first, so the "lone downed target" case never occurs in this fixture. Reporting as COULD NOT TEST, not as a defect.

## 2. The defeat save's area — CONFIRMED, narrowed (cause shown at behaviour level; code location not mutated)

Jedi Consular Veya Ordo (one save, restored from a backup copy before each arm; hash checked). Each arm: lose the fight by passing turns, then parse the `.sav` (header area string + every `character.moved`).

| arm | what I did | header area | player `character.moved` in log |
|---|---|---|---|
| A | lose in `a01-room`, never moved (Dummy kills Veya and Mate) | `a01-room` (**right**) | none |
| B | walk `a01-room` → door → `a02-arena`, lose there | `a01-room` (**wrong**) | **none** |
| C | as B, plus one extra move inside the arena (HUD read `a02-arena · 3, 1`) | `a01-room` (**wrong**) | **none** |

`20-…`/`21-…` (arm A), `22-…` (B), `23-…`/`24-…` (C). In the Load list the arena-defeat save is listed `level 1 jedi_consular · a01-room` (`25-…`), while a save written by leaving the session is listed `a02-arena`. **Control — the leave-write does record it:** Deneb Halcyon's save before/after one move + Leave Session: 44 → 45 events, the added event `{"kind":"character.moved","payload":{"subject":"Deneb Halcyon","area":"a02-arena","x":4,"y":2}}`, header area `a02-arena` (`26-…`). So the defeat write drops both the arrival crossing (arm B) and a position inside the area (arm C), and arm A is "right" only because nothing had moved.

**What the defeat write reads.** Read-only, from the source: `_endFight` (`play_screen.dart` ~14130–14165) appends `[..._pendingCrossings, ..._writeOutcome(f)]` and nothing else; `_leaveScreen` (~12094) calls `_writePosition()` **first**, then `_endFight`'s equivalent. **Likely cause, not shown by mutation:** `_endFight` never calls `_writePosition()`. Not testable in play: where the party would stand if a defeat save were resumed (opening it shows the defeat panel, not the map).

## 3. The unchecked-rules count — CONFIRMED, cause shown

**Load alone does not vary it.** Deneb Halcyon's save loaded five times without playing (the file's hash and mtime unchanged before and after each: `76fea13e`, `1790962576`): **2 rules** every time (`31-…`). Then one move, Leave Session (a real write; hash changed `76fea13e` → `e032b72d`; diff = the single `character.moved` above), reload: still **2** (`26-…`).

**What does vary: new game vs its own load.** Rennik Vestic (fresh Scout, DEX 18): **1 rule** at play entry (`34-…`); after leaving and loading the same save: **2 rules** (`35-…`). My TEST 147 observation (Oreth 2→1, Nyla 1→2, Veya 2→1) is this, not a load-time wobble.

**Cause, shown.** Source read: `_handlePlay` (the new-game hand-off, `main.dart` ~567–600) calls `validateRecord(...)` and uses only `.legal`; it **never assigns `_unchecked`**, which only the **load** path sets (`main.dart:481`). So a new game shows whatever the last loaded character left. Predicted and checked, **12 of 12**: every new-game notice in TEST 147 and 148 equals the count of the character loaded just before it, and the first game of the sitting (Avel Malick, nothing loaded yet) shows **no count at all** (`38-…`: Avel, [none], Oreth 2 (after Avel's defeat save was opened; Avel's own count is not visible under the defeat panel, but by the derived rule below a Soldier with two granted feats and a chosen one is 2 — inferred, not read), Nyla Mourn 1 (after Oreth's reload, 1), Cassar 1, Deneb Halcyon 1, Garon 1, Deneb Ordo 1, Nyla Sabek 1, Teyla 2 (after Nyla Sabek's load, 2), Veya 2). **The discriminating test:** the last load before it was Rennik (2), and a fresh **Bounty Hunter whose own count is 1** showed **2 in play** (`36-…`) and **1 after its own load** (`37-…`).

**Which rules.** The screen does not name them (the notice is not clickable; the Messages log has no entry). From `record_validate.dart` the only two `RuleNotChecked`s a level-1 organic can produce here are *"every granted feat appears in that class's schedule"* (line ~299) and *"every chosen feat's prerequisites are met"* (~308). Counts after load across eleven characters, from the screens: **2** for Sentinel, Guardian, Scout (Garon, Rennik), Agent, Brawler, Medic (each has a granted feat + Conditioning chosen), **1** for Bounty Hunter (Ordo, Mira), Consular, Smuggler (Conditioning only, no granted feat) — 11 of 11 fit "(has a granted feat) + (has a chosen feat)" (`32-…`, `33-…` show the notice beside each sheet's feat list). That mapping is derived, not displayed.

## 4. DEX 18 where the enemy wins initiative — CONFIRMED on a local variant; none exists on Shelf

- **No fixture has one.** Highest enemy DEX across every Shelf package is **12** (Hostile, `tester-visual`). The only DEX 18 character (`Shooter`, `ion-vs-droid`) is a **henchman**; the arena enemy is DEX 3 (mod −4), so a DEX 18 player wins it ~83% of the time. (My eight DEX 18 fights in TEST 147 all went to the player.)
- **Local variant** (arena Sparring Partner at DEX 30, my directory only): Rennik Vestic (Scout, DEX 18, +4): **Sparring Partner 27, Rennik 15, Mate 10** — the enemy acted first (rolled 8, needed 14, miss) and the fight carried on normally (`40-…`). Mira Brannis (Bounty Hunter, DEX 18): **Partner 15, Mira 14, Mate 9** (`41-…`), enemy first again, same. Two of two. Neither fight hung or refused to start.
- Tie: TEST 147 saw Consular (DEX 18) 10 vs Partner 10 with the player listed first. Not re-tried here.

## Seen, not chased

- **Initiative is not always the same after a reload.** Veya Ordo's first fight in the arena (TEST 147, `44-jedi-consular-fight-line-17.png`) was Veya 10 / Sparring Partner 10 / Mate −1; every fight after she was loaded (arms A, B, C here, against two different DEX 3 enemies) was Veya 17 / Mate 0 / enemy −3. TEST 147's Oreth was identical before and after a reload (19 / 12 / 7), so this is not universal. Cause not investigated.
- The defeat panel hides the Escape menu, so "Main Menu" is the only way out of it.

## What I did not check

Whether a difficulty mode can be chosen (the screen is unbuilt); that the death at −Constitution is intended for this build's mode; where a defeat save would resume the party; DEX 18 with an enemy of ordinary DEX winning initiative; the classes and levels outside the arena fixture; Equip's look (ordered not to).

## Method notes

Three of my own slips, all caught before they reached this report: (1) the Load list reorders by modified time and grows by one row per new save, so my fixed-coordinate click twice loaded the wrong character — I now read the name on screen before using a loaded state (Deneb Ordo instead of Veya; Rennik instead of Mira); (2) in-fight, the Options layout puts LEAVE SESSION at a different row than out of a fight, so a blind click opened LOAD GAME — screenshot first; (3) in TEST 147 I over-read the falling HP as "damage landing"; that is withdrawn above. The defeat panel also blocks the Escape menu — "Main Menu" is the way out.

Skills used: `research` (read `DEATH-AND-DIFFICULTY-01` / `ATTACKS-01` / `TARGETING-01` before calling anything a bug); `diagnosing-bugs` (a tight loop per finding: one save, restored before each arm, one number read per round; the 3-arm test with a leave-write control for (b), the discriminating Bounty Hunter for (h)); `verification-before-completion` (every CONFIRMED has a screenshot or parsed save line; the cause for (b) is labelled likely, not shown); `writing-for-agents` (this report). `handoff` not needed: `TESTER-STATE.md` is current.
