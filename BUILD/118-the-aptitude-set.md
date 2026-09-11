# BUILD 118 — the aptitude set, and nobody on the shelf is illegal

`PT-1662`. `CHARACTER-RECORD-01 §3`'s derivation, built. `PT-1656` closed.

---

## 1 · ⚠⚠ THE VERDICT ON THE THREE, AND IT IS THE WHOLE SHELF

> **Owner: build it, then check all three against it as your first test.**

**All three are legal**, and every rank resolves to a real source:

    kaeda-vos     acrobatics 3 · alertness 3 · beast handling 3   cap 4, classSkill
    ilyana-sorr   athletics 4 · awareness 4 · medicine 4          cap 4, classSkill
                  mysticism 3                                     cap 4, classSkill
    kesh-alaan    athletics 4 · awareness 4 · medicine 4          cap 4, classSkill
                  mysticism 3                                     cap 4, classSkill

**Run across all twenty saves: `0 illegal · 2 undecidable`.** Nothing on the
machine needs a ruling about an already-illegal record.

### ⚠ The two undecidable, and they are not a verdict

`rell-vantt` and `sero-kade` each hold **`beast handling` rank 4** with no
derived source. Both are **Human**, and `SKILLS-01 §11.4` gives a Human a
**freely chosen** racial skill — *"their two `+2`s are already player-chosen,
and the racial skill is one of those two"* — **and none of those choices is
recorded anywhere.** So that rank may be perfectly legal and the record cannot
say.

⚠ **Both took `hunter`, whose `teaches` IS Beast Handling — and both took the
ITEM.** `PT-705`: *"a Doctor takes medpacs OR Medicine."* So the profession
correctly grants nothing, which is exactly why the skill has no source, and the
racial pick is the only remaining explanation. **Consistent, not contradictory.**

## 2 · ⚠⚠ TWO THINGS I GOT WRONG AND CAUGHT BEFORE REPORTING

**A value used as a key, in the derivation written to close a rule gap.**
`ledger_writer` writes `name.toLowerCase()`; every rules file holds Title Case.
Compared raw, the first version reported **every skill on every save as having
no aptitude — including a Soldier's own Athletics** — and would have declared
twenty characters illegal on a casing difference. Both sides fold through
`skillKey` now.

**And the racial pick is a COUNT, not a per-skill question.** The second version
reported `rell-vantt` and `sero-kade` illegal. `§11.4` grants **one** racial
skill, so **at most one** skill can be excused by it — a character with six over
the cap is illegal whatever they picked, and one with a single such skill cannot
be judged. ⚠ **Publishing the first answer would have been an accusation the
data cannot support**, about the owner's own saves.

## 3 · What the derivation is

Five sources, `§11.2`, and they **stack** — so it returns the **set of sources
per skill**, not a boolean, because `§3` requires the sheet to mark which
granted each one.

| source | where it comes from |
|---|---|
| **class** | `classes.class_skills`, **every class held** — `§2` allows three |
| **homeworld** | `origin.aptitude_skill`, always one |
| **profession** | `professions.teaches`, ⚠ **only if `grant_taken == 'aptitude'`** — `PT-705` |
| **Skill Focus** | feat id → skill. ⚠ **Empty, and that is the data**: `§11.2` says 23 exist, `feats.toml` has **one** generic `skill_focus`, and `feats_screen` refuses to offer it for that reason. No character can hold one. |
| **racial** | ⚠⚠ **the one nobody records** — see below |

⚠ **DERIVED, NEVER CACHED.** *"A Skill Focus feat taken at level 8 adds aptitude
the character did not have at level 1."* Same shape `PT-1531` gave defence and
the base attack bonus: read live.

### ⚠⚠ The fifth source is not collected anywhere

`§11.4` makes the racial skill **a choice made at creation**. The record has
`origin.aptitude_skill` for the homeworld and **no equivalent for the species**,
and no chargen step asks. `hub.dart` assembled three of the five and never had
the other two.

So the derivation answers **unknown, not no** — and the three exceptions `§11.4`
names are all handled: a species with one bonus skill is a lookup (*"Duros take
Pilot"*), `Droid, Astromech` takes **both**, and a Human chooses **freely**.
⚠ The free-chooser is **detected from the data** — a bonus line naming no skill
is one that chooses freely — rather than hardcoding an id in the engine.

## 4 · ⚠ AND THE COUNT ON SCREEN IS A REAL SIGNAL NOW — `PT-1655`, `PT-1648`

    UNCHECKED RULES PER SAVE:  1 → 14 saves · 2 → 6 saves

**Fourteen of twenty drop from *"2 rules about this character not checked"* to
*"1"*.** The six that stay at two are the droids (chassis spread) and the two
Humans above. What is left unchecked anywhere: the skill cap **only for those
two**, feat prerequisites, and the droid chassis spread.

⚠ **AND THE SCREEN'S OWN COPY OF THE CAP IS GONE.** `SkillBudget.cap` held
`§11.1`'s expression and `record_validate` had none — **the screen enforced a
rule the validator could not.** It delegates to `skillCap` now.

⚠ **Difficulty untouched.** Normal only, still hardcoded exactly as it was.

---

## Tests

`Lodestar` 503 · `Lens` 7 · `Loom` 244 · `KOTOR-RPG-APP` — see the push.
Pins 4/4.
