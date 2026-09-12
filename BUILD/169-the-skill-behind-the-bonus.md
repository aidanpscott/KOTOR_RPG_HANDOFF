# BUILD 169 — the skill behind the bonus, and a case that cannot happen

---

## 1 · ⚠ `PT-1850` — 39 SKILL BONUSES NOW CARRY A NAME

`Armory` Chapter Seven carried *"a skill bonus whose **size** is known and whose
**skill** is not"* — the games store the skill as a numeric index and it had
never been mapped back.

**⚠ BOTH GAMES SHIP THE SAME TABLE, CHECKED RATHER THAN ASSUMED.**
`k2_skills.2da` and K1's `skills.2da` are row for row identical, so one mapping
serves the chapter. The script **refuses outright** if they ever disagree.

**⚠⚠ NOTHING WAS RESOLVED FROM THE PAGE.** The chapter keeps each index in its
own margin — but a margin is a **transcription**. Every index was read back off
the item's own `.uti` and matched on **both the subtype and the magnitude**, so
a row whose margin disagreed with its blueprint would have been reported rather
than rewritten.

    39 resolved · 0 refused

**⚠ AND THE REFERENCE ROW WAS THE CHECK.** `Advanced Droid Interface` already
carried four skills by name; its own indices — 3, 0, 1, 6 — resolve to exactly
the four names it was already printing.

**⚠⚠ A 39TH MARKER WAS WRITTEN IN A DIFFERENT SHAPE.** One row reads
`DecreasedSkill ⚠ (unresolved — skills subtype 3)` rather than
`Skill bonus +N` — a different **property** (21, not 36) and the same table. A
pattern aimed at the commonest wording walks straight past it: **a check keyed
to a SPELLING of its subject**, the fifth sighting in this corpus.

Verified line by line that the **only** difference in each of the 33 changed
rows is the resolved label. Chapters Five, Six and Eight carry none of this
marker. The chapter's own `§1` account is updated so it no longer describes as
unresolved the thing it now resolves: **22 rows remain** — eight saving-throw
subtypes, ten character-locks, four racial subtypes, one Defence type.

## 2 · ⚠⚠ `PT-1849` — THE APPROVED FIXTURE WAS NOT THE ANSWER

A high-Constitution player would not have reached the fallen-companion state,
**because the state does not exist in this product.** Two rulings stacked:

    1. PT-1633   no individual death threshold on Easy or Normal.
                 "Only a wipe kills" — and a wipe ends the fight.
    2. the app   has NO difficulty setting. Encounter defaults to
                 Difficulty.normal and nothing passes another.

Together: a companion is `dead` only in a wipe, and a wipe ends the fight. So
*fallen companion, fight still running* is **unreachable**, not merely hard to
build. `_nameOf` covers it by construction either way.

Reason 1 is already pinned by `round_test` and `play_state_test` — **not
repeated**. Reason 2 is pinned now, written to **fail the day a difficulty
setting arrives**, which is exactly the day the case becomes reachable.

**⚠⚠ AND THAT PIN COULD NOT FAIL ON ITS FIRST WRITING.** It scraped with
`Encounter\(([^)]*)\)`, and the real call —
`Encounter(combatants: [me, ...joining.map((x) => x.combatant)])` — contains
**nested parentheses**, so the match stopped at the first `)` and never saw the
argument list. It passed against a build that really did pass a difficulty.
Replaced with a balanced-paren scan and re-proved by planting
`mode: Difficulty.hard` and watching it fire.

---

## Tests

    App  592 pass   (two_enemies +1)

## Still open

- **A real target picker**, before power effects resolve — `PT-1847`.
- `§2`'s character screen (the click, `PT-1443`'s) · `Dash`/Hustle unbuilt ·
  `Scan`, `Slice`, `Treat`, `Repair` unblocked and unbuilt · the stealth field
  generator has no item.
- **22 unresolved rows** in `Armory` Chapter Seven, of three remaining kinds.
- ⚠ The suite is flaky under load — `BUILD 167`.
