# BUILD 162 — a creature carries skills, and Hide is a key you can press

---

## 1 · ⚠⚠ `PT-1843` — THE FIELD FIVE ACTIONS WERE WAITING ON

`AUTHORED-CHARACTER-01`'s `[skills]` — `points_per_level` plus explicit ranks
where a scripted check needs one — read into `OpenedCharacter` and **carried
across the combatant seam**.

**⚠ THE AUTHORED NUMBER IS THE NUMBER, AND NOTHING IS ADDED TO IT.** The
player's total is `PT-1326`'s *"rank 4 + aptitude 2"*, and aptitude is a
**chargen** derivation — class skills, species, homeworld, background — off a
`CharacterRecord` an authored creature does not have. The schema says *"ranks
are authored explicitly when a specific check matters against this creature"*,
so deriving a second term would make an authored `4` mean something other
than 4.

**⚠ ABSENT IS ZERO, AND THAT IS THE SCHEMA'S RULE** rather than a default
invented here. Absence is a **value** — the one case this corpus's
absence-versus-error rule usually argues against — and it is safe precisely
because the document says what absence means.

**⚠ CARRIED ACROSS THE SEAM, AND GUARDED THERE.** `combatantFrom` is exactly
where `PT-1708`'s `baseAttackBonus` was dropped — *"its one caller never passed
it"* — at a cost of every creature in the product having a reaction pool of
zero. The test drops the line and watches two cases fail.

**⚠ AND A BLUEPRINT WITH NO `[skills]` IS NOT AN ERROR.** Every blueprint in
every existing package predates the field.

## 2 · ⚠ THE TWO CONDITION KINDS WERE THE ROADMAP, NOT A PROPOSAL

`EVENT-KINDS-01` has carried `character.condition-applied` and
`.condition-expired` at `transient` since it was written, among the kinds it
calls *"declared and unimplemented… a roadmap, not a defect."* `ledger.dart`
had no constants for them, so the vocabulary declared a state the code could
not name. Unlike `PT-1122`'s two, these needed **no proposal**.

`transient` is why hiding does not survive a save, and that is **right**: a
player who reloaded still hiding from an encounter that is over would carry a
condition nothing can end.

## 3 · ⚠⚠ `PT-1108` — HIDE

`s`, on the `d`-Disengage precedent. **The letter is a proposal**: `h` is the
natural one and `PT-1843` gave it to Hustle, so Hide takes the letter of its
own check — a **S**tealth check. `d`, `f`, `i`, `m` and `space` are the whole
vocabulary and it collides with none of them. One line to change.

One roll per watcher, the engine's own `resolve`; `hiddenFromAll` holds the
reading that **one watcher seeing you ends it**. The fallen get no roll — a
dead watcher still opposing the check would make a won fight harder to hide in
than a lost one.

**⚠ SWINGING BREAKS COVER** — `PT-1682`, *"what gives you away is the shot
rather than the hit"* — so it fires **before** the blow resolves and a miss
reveals exactly as a hit does. After the turn check and before the spend, so a
**refused** swing does not reveal: nothing was thrown.

**⚠ AND THE REVEAL SAYS NOTHING, DELIBERATELY.** The blow sets `_said` to its
own sentence the moment it returns — a line written there would be overwritten
inside the same synchronous call, which is the *held rather than shown* shape
this screen already records for a reaction. **The indicator is the signal.**

**⚠ THE STEALTH FIELD IS NOT WIRED, AND IS NAMED.** `§4`'s generator is an ITEM
and no item in the catalogue declares itself one yet. Passing `false` is this
build having no field, not a decision that the rule does not apply.

## 4 · ⚠ THE INDICATOR IS ITS OWN LINE NOW

`PT-1108` asks for *"a real, clearly visible indicator — not the small
easy-to-miss checkbox the source games actually used."* `hidden` was **one
dimmed word in a dot-joined line**, between *in the fight, and the round does
not hold it* and *noticing*. That is the treatment the ruling names, arrived at
honestly and rejected by name.

**The word is unchanged, deliberately** — renaming a state while moving it is
how a guard stops matching something that is still true.

⚠ And the acceptance reads `find.text('hidden')`, not `textContaining`: the
Action's own sentence is *"hidden — 16 beat 4"*, so a containing match could
pass on the message while the row showed nothing.

## 5 · ⚠⚠ AND MY FIRST FIXTURE MISUNDERSTOOD THE RULE IT WAS TESTING

A thug written with `awareness = -20` and no `alertness` **looks blind and is
not**: the defender rolls the better of the two, an unwritten skill is rank 0,
and **zero is still a roll.** `d20 + 0` beat the hiding player and the feature
read as broken.

That is `§4.1` arriving from the other direction — *"two skills that fail
differently is worth more than one that is simply better"* — so **ruining one
sense does not ruin the creature.** Kept as its own test rather than quietly
corrected.

## 6 · ⚠ FLAKE SIGHTING, THE FIRST

`whole_loop_test` failed once inside a full run and passed alone and on a
re-run. Not caused by anything in this slice, and named rather than re-run
until green and forgotten.

---

## Tests

    Lodestar   721 pass   (stealth_test +16 total)
    App        581 pass   (hide_test +5, stealth_gap_test −3: the debt is paid)

`check_engine_pin` 4 compared, all level.

## Still open

- **`§2`'s character screen** — its entry is the **click**, which `PT-1443`
  still owns. The keyboard path is not blocked and never was.
- **`Dash`/Hustle** is unbuilt, so *Hidden disables running* has nothing to
  disable. Key decided: `h`.
- **Scan, Slice, Treat, Repair** — now unblocked by `[skills]`, unbuilt.
- **`PT-1841`** — room position memory across doors, and where a companion
  lands relative to the entry point. Raised by the owner, not yet scoped.
