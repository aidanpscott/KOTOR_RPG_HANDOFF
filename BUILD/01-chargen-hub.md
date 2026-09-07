# 01 · Chargen step 2 — the hub opens

**`KOTOR-RPG-APP` `592ec4b`.** analyze clean, 70 tests pass, the walk intact.
**One stop, and it is larger than the step it sits in.**

---

## The thing to check first: `models.json` was UNWIRED, not missing

`pre_hub.dart` read `models: const []` while `models.toml` carried **38 models
across seven chassis** with skill menus, model feats and frame prices. The MODEL
screen refused for two slices for two different reasons — first the extraction
did not exist, then nothing wired it. **Both are closed.**

A droid now reaches the hub. The screen names the chassis it was given, lists
only that chassis's ownable models, and shows frame price, CR, model feat and
skill menu on selection.

## 1 · The step strip — `PT-1215`, `PT-1216`

Four states plus Play. The numeral is a filled circle **beside** the button, so
the padlock replaces the *numeral* and the step name stays readable. Completed
renders grey, not highlighted. NWN's width, not KOTOR's.

**⚠ A step that does not apply is not rendered at all, and the strip renumbers.**

| Character | Steps | Play is | Missing |
|---|---|---|---|
| organic, Soldier | 8 | 9 | Powers |
| organic, Jedi Guardian | 9 | 10 | — |
| droid, Battle | 7 | 8 | Origin |
| droid, Astromech | 6 | 7 | Origin **and** Gender |

**⚠ Play stays locked.** Correct output with two steps built, not a stub.

**⚠ The seven unbuilt steps are NOT padlocked, and that is a decision.**
`APP-UI-VISION-01` makes the padlock deliberate over a dimmed number because it
*"states why a step can't be clicked rather than only that it can't"*. Padlocking
a screen nobody has written would state a reason that is not the reason.

## 2 · Origin — half works, half is the stop

**Upbringing works.** Nine records, labelled *"grants nothing — flavour only"*.
⚠ The extraction's null `grants` is `PT-705` being obeyed, not data missing, and
it was not treated as an absence.

**⚠ The homeworld half has no data.** `CHARGEN-DATA-01` names `WORLDS-MENUS-01`
and the Atlas for the world list and its three-skill menus. **Neither is staged
and neither is extracted.** `worlds-policy.json` is the register's *admission
policy* — exclusion classes and evidence predicates, 47 rows — not a roster.
`WORLDS-REGISTER-01` is staged and is also policy: `D-W1`–`D-W5` are admission
rules, not planets.

## 3 · Gender — `PT-1236`, `PT-1190`

`GENDER` for an organic, `VOICE` for Assassin and Battle, and the step **does not
render at all** for Astromech and Remote. Header bars only, large unboxed
buttons, no entry popup — `PT-1235` names this screen as that rule's exception.

**⚠ The options are the screen's own.** Nothing in the corpus enumerates them and
no kind in `rules/` carries them. Flagged in source rather than presented as
extracted.

## ⚠ THE STOP — the missing worlds block more than Origin

`§5`'s unlock is sequential: the first incomplete step is encouraged and every
step after it is locked. **Origin is step 1 for every organic and it cannot
complete**, because the world grants aptitude #1 in `§4`'s dependency graph.

> **So the missing world data does not block one step. It blocks the whole strip
> for every organic character.** Gender is reachable today only by a droid, for
> whom Origin does not exist. There is a test asserting exactly that.

**Origin was not allowed to complete on upbringing alone.** Upbringing grants
nothing; ticking Origin without a homeworld would produce a character missing an
aptitude the graph requires, and would hide the gap behind a tick.

**THE NEED:** a world roster with each world's three-skill menu, and its
cardinality band, which `§4` also feeds from Origin.

## What was not built

Steps 3–9. No character record, no save; `Continue` stays disabled.
No explanatory popups — `§6` gives every screen a one-time one with its own
glyph, which needs a seen-once store, and that is save-adjacent.
No re-lock warning — `§5` requires one, and nothing after Origin can complete,
so it could not be exercised.
No `RECOMMENDED` — `PT-1226` marks it under review.

**⚠ One layout fix worth naming:** the strip's last two rows fell below the fold
at 1280×720 and **Play — the thing the hub counts towards — was invisible.**
Rows are tighter and all ten fit without scrolling. **Found by capture, not by
test**, which is the second time a screenshot has caught what a passing suite
did not.
