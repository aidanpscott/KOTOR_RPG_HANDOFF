# STATE — every repository and package, as of the last push

**⚠ Rewritten in full each time, never appended.** If a line here disagrees
with a slice report, this file is the later one.

---

## Repository heads

| Repo | Head | Visible to the owner? |
|---|---|---|
| `KOTOR_RPG_MAIN_WORK` | `d4a4ca1` — check_decisions.py | ✓ |
| `KOTOR_RPG_HANDOFF` | this commit | ✓ |
| `Lodestar` | `fe58cfe` — `PACKAGE-FORMAT-01 §4·1`, required fields | ⚠ no |
| `Lens` | `d532c0a` — an arrival can be emphasised, keyed by name | ⚠ no |
| `Loom` | `ff4ff81` — required fields, where validate runs, deleting an arrival | ⚠ no |
| `KOTOR-RPG-APP` | `b1e57ae` — Backstory one tab, and Abilities | ⚠ no |

All six clean and level with origin.

## What each repository is

**`Lodestar`** — the rules engine. Pure Dart, no Flutter. Opens packages, areas
and characters; validates a package; answers where packages and saves live
(`Locations`, needs D and E). 10 test files.

**`Lens`** — the shared view layer, `PT-1381`. The area board, its palette, its
metrics and the pan/zoom viewport. Exists because `AREA-FORMAT-01 §2b` governs
how an area looks in **both** Loom and the app, the engine may hold no widgets,
and neither program may depend on the other.

**`Loom`** — the Builder. Package and area creation, tile painting, placing,
connections and arrivals, Package Properties, and `validate` on open with a
re-runnable Verify dialog. 12 test files.

**`KOTOR-RPG-APP`** — the play client. Console Home, the Package Main Menu, the
area and the walk, and character generation as far as the hub. 10 test files,
70 tests.

## The shelf — `~/.local/share/kotor-rpg/packages/`

| Package | What it is |
|---|---|
| `base-rules` | ⚠ **Generated, not authored.** 22 TOML files, 2,533 records. `PACKAGE-FORMAT-01 §3c`. Rebuild with `scripts/gen_base_rules.py` in MAIN_WORK. |
| `endar-spire` | The two-area test bed, made entirely in Loom |
| `taris-undercity` | A second package, so the library holds more than one tile |

## What runs end to end

Console Home lists three packages → selecting one reaches the Package Main
Menu → New Game opens the character entry screen → Create New Character runs
the pre-hub (Species → Model for droids → Class) → the hub opens with its step
strip → Back reaches the area → the marker walks through a door and arrives at
the named point in the second area, and back.

## ⚠ What is open

| | Need |
|---|---|
| **Worlds** | ✓ **closed at `PT-1396`.** 301 worlds ship in `base-rules`, exported from the Atlas resolver. Origin completes and the strip unlocks past step 1 |
| **13 unfinished menus** | 13 worlds carry three skills because `D-MENU4` is applied only where a menu is finished. They ship, and are not offered |
| **`ATLAS/decisions/`** | ⚠ 34 files `MAIN_WORK` has never read. `D-MENU4` sat there superseding a ruling three documents still carried |
| **Droid ability scores** | ✓ **closed at `PT-1403`.** `chassis.toml` ships 7 production spreads, all totalling 72 — 4 derived, 3 inferred and marked as such on screen. A droid completes Abilities |
| **Droid skills** | ✓ **closed at batch 5.** `droid_skills.toml` ships the four bodies. A droid completes Skills |
| **`DROID-SKILLS-01` §2.3 vs §2.4** | ✓ **closed at `PT-1405`.** The grid is right and the totals lag: Assassin 15, Battle 13. `stated_total` still carries what `§2.4` says, with the ruling named beside it. Athletics is offered |
| ⚠ **Science and Survival for droids** | On the 25-skill roster and **nowhere in the chapter**. Neither opened nor closed. Withheld, and said on screen |
| ⚠ **`PT-621`'s Protocol carve-out** | Opens `Persuade` to a "Protocol chassis" that is not one of `§2.3`'s four bodies. The carve-out names an axis the table cannot express |
| **Three Sith base classes at creation** | ✓ **closed at `PT-1407`.** One feat at first level. `first_level_feats.toml` carries it as an override with `sets_cadence: false` |
| ⚠ **Three Sith base classes at LEVEL-UP** | Still open, and `PT-1407` says so. Level-30 totals are authored — `PT-126` fixes the Sith Assassin's at 12 — and **when they gain the other eleven is unwritten** |
| ⚠ **`CLASSES-FORCE-PHB`'s Jedi Guardian attack row is transposed** | It reads `picks 18 · chains 20`; `CLASS-ATTACKS-01` gives Combat **36** picks and assigns the Guardian **18** chains with **20** feats at 30. Capstones match at 11, which says the row was built from `§2.3` and the two numbers crossed. **The extraction is faithful; the source is wrong.** Reported, not fixed |
| ⚠ **`PT-126` vs the Sith Assassin's rate** | `PT-126` ruled it **`Specialist`** *"by owner instruction"* and said the Sith side loses its `Middle` class; `CLASSES-FORCE-PHB` and `classes.json` both carry **`Middle`**. Does not touch creation; does touch attacks |
| **`attack_chains` / `attack_picks_at_30`** | Populated for **14** classes, not one. Read from each PHB chapter's record table, which 5 of 6 Force classes and all prestige classes lack. **`picks` is derivable from `rate`** (`§3`: 36/27/18); **`chains` is not** — `§2.3` makes it a per-class assignment inside a band, and its table is headed *"Assigned so far"* |
| ⚠ **`FEAT-SCHEDULE-01`'s "Seven schedules" row** | Reads `Every third from 1 · Sith Assassin · 10`, where its own summary gives Sith Assassin **12** and the grid's `Assassin` column reaches 10 on that cadence. Either a mislabel of the prestige Assassin, or a cadence contradicting `PT-126`'s owner-instructed 12. **Reported, not resolved** |
| ⚠ **Skill Focus** | Half closed at `PT-1405`: the aptitude applies from level 2 and Skills are not repriced. **Still unbuildable** — `SKILLS-01 §12` says 23 exist, one per skill, and the library holds **one generic record with no skill on it** |
| **13 unfinished menus → aptitude** | The 13 three-skill worlds grant one fewer aptitude source than the 288 four-skill ones. They are not offered, so nothing is wrong today |
| **Hub step 8, Equipment** | ✓ **closed at batch 6.** `PT-1200` resolves: the item is named and priced against the array. Route 1 only |
| ⚠ **Route 2, the purse** | Needs the array's own credit value, which is **not written**. The arrays name items in prose and only **18 of 41** names resolve to exactly one catalogue row; `§2c` disambiguates 14. Not offered |
| ⚠ **Five `ITEMS` file headers are stale** | `ITEMS-01, 02, 04, 05, 08` state a total their own category headings do not add to, and `ITEMS-09` states none. **All 44 category counts are right.** Same shape `ITEMS-07` documents at `PT-871` |
| ⚠ **`STARTING-EQUIPMENT-01`'s status block says 18 twice** | `§4` and `§4a` each carry **19** — all 19 base classes. The nineteenth is the **Saboteur**, new at `PT-784`. `classes.json` already records this class going missing in three places; this is the fourth and fifth |
| ⚠ **Three grants name no item** | `Augmented`, `Dancer`, `Initiate` depend on the character, so `§5` names no resref and no price. 13 of 16 slot-fillers resolve |
| **Hub step 9, Identity** | ✓ **built.** Three stages in place, with a back control. All nine steps are built and **Play can unlock — `PT-1216`** |
| ⚠ **There is no portrait set** | `UI-ASSETS-01 §2` asks for presets per species — *"the largest art commitment in the flow"* — and `ASSET-REPLACEMENT-01` carries the row as **ours and unticked**. `§2`'s own current state is *"a filled circle"*, which is what the screen shows. **The first place a player can see that we ship no source assets** |
| ⚠ **An import cannot fill it** | K1's **181 `po_*` portraits are named for the games' own characters**, not for a species. `PT-1214` asks for species presets; the art import answers a different question |
| ⚠ **The custom-portrait spec is unwritten** | `PT-1180`: ours supports a player-side folder like NWN's. `§2`: *"A custom portrait needs no art, but it needs a spec: accepted formats, dimensions, and what happens to an image of the wrong aspect."* **The half of this that needs no drawing** |
| **The save file** | ✓ **built at batch 2.** `KRSV` header + gzip payload, `.sav`, in `Locations.saves`. **`PT-1265`'s bit-identical guarantee runs**, on a synthetic log and on a real chargen one |
| ⚠ **The compressor is `gzip`, not `zstd`** | `PT-1328` recommended zstd-10 and measured the gap at **0.09 MB on 16.3 MB**. Dart ships gzip and no zstd; every zstd on pub is an FFI binding. **The header records which**, so switching later orphans nothing |
| ⚠⚠ **THE WHOLE LOOP RUNS** | ✓ **batch 3.** Make a character, Play, quit, reopen, Continue, same character. **The first thing here to survive a restart** |
| **`Continue` and `Load Game`** | ✓ **alive.** Continue opens the most recent and **the disk decides which**; Load Game lists them with each save's rules version |
| ⚠ **"The same place" is the entry area** | `character.moved` and `area.entered` are **`session`** lifetime, and `§4` makes lifetimes decide what is written at all. **By the vocabulary's own rules a save cannot know where you were standing.** A player who walks to the second area and continues arrives back at the first |
| ⚠ **Three of `§4`'s twelve rules cannot be checked** | derived-aptitude skill caps, granted feats against a class schedule, and feat prerequisites — each missing its data. **Returned, not skipped**, and the play HUD shows the count |
| **`§5`'s five load steps** | 3, 4 and 5 built. Step 1 is done by the time it runs; step 2 has no snapshots and `PT-1327` makes them a cache |
| **Save slots and rewind** | `§5·0` specifies a slot as **a point in the log** with a rewind event. **Specified, not built** |
| ~~⚠⚠ **What a save is NAMED, and how many**~~ | ✓ **answered at `PT-1416`** |
| ⚠⚠ **What a save is NAMED, and how many** | `§5a` settles where; **nothing settles how many or what one is called**, and the header carries **no time, no name, no character and no package**. `Continue` cannot order saves without a field the format does not have. `§6`'s *"a save that is a log may want showing differently from a save that is a slot"* is the same question |
| **Loading is step 3 of five** | `§5`'s sequence is resolve packages · snapshots · replay · validate · open. **Only replay is built** |
| **The log and replay** | ✓ **built at batch 1**, in `Lodestar/lib/src/ledger.dart`. Chargen writes events; `replay()` reproduces the character field by field for **both** shapes. **In memory only** |
| ⚠ **14 emitted kinds are not in `EVENT-KINDS-01`** | `PT-1415`'s thirteen plus `step-reopened`. **Now asserted rather than reported**: check A names them as an exception list, every entry is owed to the document, and a fifteenth fails the build. Writing them in is the owner's |
| **The vocabulary reaches the code** | ✓ **extracted** to `event_kinds.toml` — 36 kinds from 24 rows — so both checks compare code to the DOCUMENT, and `check_extracts.py` watches it |
| **Replay's silent no-op** | ✓ **closed.** `replayDetailed` returns every kind it had no case for; `replay()` drops the report. **The fix is the report, not the test** |
| **Every kind has a lifetime** | ✓ **checked.** 36 of 36, and the four are exactly `PLAY-STATE-01 §2`'s |
| ⚠ **The re-lock ruling is Claude's** | `character.step-reopened` carries its own discard list so an old log replays the same way after the flow changes. **Flagged, not ruled** |
| ⚠ **`CHARACTER-RECORD-01 §2` vs `§5` on `abilities`** | `§2` says final scores, `§5` says bought scores. The ledger follows `§5` and `§1`'s principle. **Reported, not resolved** |
| ⚠ **A droid model has no `id`** | `DROID-MODELS-01` is keyed by chassis; `character.model-set` records the **name** because there is nothing else |
| **Combat `resolve()`** | ✓ **slice 1.** Four check types, one attack, the whole derivation. **Callable without a game.** No pools, no turn order, no damage applied |
| ⚠ **A tie in an opposed roll** | Goes to the defender because it had to do something. **Nothing rules it** |
| **Check A compares against lifetime** | ✓ **`PT-1420`, fixed on its own before the emission.** A `permanent` kind replay ignores is the bug; a `transient` one is the design — **and the rule is proved against a case it does not yet have**, so it cannot pass vacuously |
| **Pools, damage, the death boundary** | ✓ **slice 2.** Vitality is one pool with a negative band; the Force pool has three values. Difficulty enters here and only here |
| ⚠ **`DEATH-AND-DIFFICULTY-01` Hard says −10, `§5b` supersedes it** | *"E-2's flat −10 is superseded — the threshold SCALES with Constitution."* The superseding line is followed. **Reported, not resolved** |
| **The round** | ✓ **slice 3.** Five budgets on **three** reset boundaries, initiative, surprise, and the dying countdown. **A character can now die untouched** |
| **Enemy decisions** | ✓ **slice 4, doctrine only.** `SPACE-AI-01`'s four questions; deterministic, and a doctrine that rolls takes the injected die |
| **A doctrine is not a reaction** | `PT-1373`: a trigger produces an event and a reaction consumes one. **A doctrine is asked, at a known point.** Two mechanisms, one built |
| ⚠ **`§6a` slot 1.5's `Cleave` is a CHAIN, not a feat** | It is in `ATTACKS-05` — level 1/4/8, Strength 12 — and **not in `feats.json`**. The `on_kill` recursion it tests runs through the attack system |
| **`§6a` slots 1, 3 and 7 verify** | Against the 104 extracted powers, **and slot 7's prerequisites are in the data** |
| **The seam** | ✓ **built, both sides.** A placement becomes a combatant through the blueprint it names, and one attack runs from the app. **The vitality formula was already ruled at `PT-648` — nothing is rolled** |
| **The bed has a creature** | ✓ **made in Loom by clicking** — the dialog, then a click on a square. A Sith Trooper stands at `[6, 4]` on the command deck, and **Lodestar reads back what Loom wrote** |
| **Walk into it to attack** | ✓ **and it is Claude's reading.** A step onto an occupied square strikes instead of moving; no document rules it |
| ⚠ **The New Creature dialog overflows by 58px at 1280×720** | Found by clicking it. **Reported, not fixed** — Loom's layout, and nobody asked |
| ⚠⚠ **The wound does NOT survive leaving the area** | Combatants are rebuilt from the blueprint on every entry, which is what `§4` rules — *"not written: current vitality."* **The other choice would have been `PLAY-STATE-01` arriving**, and a persistent wound is a design question rather than a line of code |
| **The second projection** | **Not forced a fourth time.** A multi-round fight needs who-is-standing across turns, and `§4` puts every one of those facts on its not-written list. **The thing that would force it is a fight that survives being left, and this one does not** |
| **The enemy takes a turn** | ✓ **slice 5.** Initiative, five budgets, doctrine, round boundary, dying countdown — the app calls all of it |
| ⚠ **A fight can always be left, and never lost by leaving** | Two readings, both falling out of `§4` writing nothing. **Fleeing is not built; this is what transience gives you** |
| **The dying countdown, in a real fight** | ✓ **and the risk lay the other way.** A dying combatant is not standing, so the advance skips it and the round boundary fires **sooner**, not never |
| ⚠⚠ **SIX things have had to behave somehow** | slice 1: the opposed tie and crit confirmation — **both ruled at `PT-1420`**. Slice 2: healing past `max`, negative damage as healing, `down → dead` in one blow. **Slice 3: a tie in INITIATIVE** |
| **Five of the six are ruled** | `PT-1420` took two, `PT-1422` took the initiative tie **and the targeting tie with it**, and the brief ruled the clamp and the named heal door. **One left: `down → dead` in one blow writes only `character.died`** |
| **The second projection** | **Not forced by the round.** `§4` makes a round transient; the encounter answers *who is standing* from its own combatants. `PLAY-STATE-01` is owed for state that outlives a fight |
| ⚠ **`campaign` kinds replay ignores are owed a second projection** | `character.died` and friends are `campaign` and the character record has no *alive* field, by design. **`PLAY-STATE-01` owns current state and nothing has built it** |
| **`§5` difficulty** | **`resolve` never sees it** — the mode acts at the death boundary, not on the dice |
| ⚠⚠ **What Play owes: a LOG, not a record** | `CHARACTER-RECORD-01`: *"This record is a **PROJECTION** of the event log, not the store… the log is what persists."* `SAVE-LOAD-01`: *"the save is the log."* So the next stretch is not serialising the hub — it is writing the choices as **ordered events** |
| **The re-lock as an event** | ✓ **answered at batch 1** — and building it found that the hub **kept the value of the step it re-opened**. Nothing read it back, so nothing had noticed |
| **`backstory.lifestyle`** | ✓ **answered: no event.** `PT-1411` marks it orphaned; an event for a choice nobody makes invents a value |
| **`identity.story_origin`** | `CHARACTER-RECORD-01` calls it *"proposed here, not ruled"*. The screen produces all three values |
| **The profession grant is a category** | ✓ **resolved at batch 6.** `STARTING-EQUIPMENT-01 §5` names the item behind each category and prices 13 of 16 |
| ⚠ **An annotation past the closing pipe drops a value** | `PT-1408`'s inline correction made the Guardian's rows three cells and `read_phb` took only two — the correction **silently un-extracted both fields**. Fixed in the reader; worth remembering as a shape, not a one-off |
| **The import question** | ✓ **Answered: ART.** `ITEMS-01..09` already hold 1,425 converted resrefs under seven named rulings; a stats import would overwrite them with the game's balance. See BUILD 12 |
| ⚠ **`PT-1369`'s pairing must count ICONS, not items** | K1 ships **183 `ii_*` icons across 38 classes** against **557** `.uti` blueprints — icons are per class + variation. Counted against items the pairing can never balance |
| ⚠ **K2's item icons not located** | No `ii_*` in K2's `chitin.key`, and this Steam build's `TexturePacks/` holds only controller overlays. Not checked: module `.rim`/`.erf`, `override/` |
| ⚠ **Powers at 1st level reads two sources one way** | `MULTICLASS-01 §2.2a` states 2 at Jedi level 1 and `PT-128` corrected the Sith Assassin to it; `POWER-COSTS-01 §6` calls acquisition **open**. Read as compatible — §6's open item is the schedule *after* level 1 — **and that reading is Claude's, not a ruling** |
| **Character record** | Nothing is written and nothing is saved. `Continue` stays disabled |
| **`base-rules` distribution** | `§3c` says it ships with the product and does not say from where. It is generated onto the shelf and lives in no repository |
| **Five species parents** | The ruling asks for 57 records as 35 parents + 22 subraces; the corpus has 57 with all five parents present since `PT-1333`. ✓ closed at batch 4 |
| **Feat grant levels** | `granted` vs `selectable` is structural and carried; the per-level `_granted` column lives in `feat.2da`, a game file |
| **`recommend_order`** | Unauthored. Scoped negative across all staged files |
