# BUILD 145 — a droid is designated, and the ban list was already written down

---

## 1 · ⚠⚠ `PT-1720`, `PT-1722`–`PT-1726`, `PT-1729` — BUILT END TO END

Chassis prefix, two digits, checked against the canon ban list. Four layers,
each the authority for the one below it:

    PT-1729 (the ruling)
      → CHARGEN-DATA-01's designation section     the rule, written down
      → designations.toml + reserved.toml         extracted, shipped
      → Lodestar designationProblem/randomDesignation   the rule as code
      → the name step                             the player types into it

**⚠⚠ THE PREFIX IS THE MODEL'S, NOT THE CHASSIS'S.** `PT-1726` pulled every
model table and the shapes do not agree inside one chassis: an `Astromech` is
`T3-`, `3C-`, `IT-`, `T1-` or `R-` **depending on which line it came off**. The
Model step has been asking that question since `PT-1394`; this is where the
answer finally does something.

| | |
|---|---|
| **38 rows** | every model `models.toml` carries, `free` included |
| **16 with a prefix** | 12 attested, 4 inferred and marked so |
| **22 free-text** | `Battle`, `Labor`, `Remote`, the three generics, `B-4D0` |
| **8 reserved** | `§0c`'s six, plus `HK-50` and `HK-51` |

## 2 · ⚠⚠ THE BAN LIST IS READ, NOT RESTATED — AND `§0c` IS NOT THE WHOLE ANSWER

`PT-1725` already found the list: **`DROID-MODELS-01 §0c`, six designations,
each individually ruled** at `PT-593`, `PT-595`, `PT-598` and `PT-588`. So the
extractor reads that table. **A second copy in Dart would have been two answers
to one question**, which is the standing this corpus gives `campaignKinds`:
*the declaration is the authority, not this code.*

**⚠ AND READING ONLY `§0c` WOULD HAVE BEEN WRONG.** `PT-1726` names **three**
exclusions for the `HK-` prefix and `§0c` carries **one** of them. `HK-50` is a
series `§2` marks *"NOT PLAYABLE, NO MENU"*; `HK-51` is excluded at `PT-586` as
3668 BBY. **Both are legally shaped two-digit designations, so nothing else
would have stopped them.** They are extracted by name, each with its own
citation, rather than assumed into the six.

**⚠ A MODEL NAME IS NOT A UNIT NAME EITHER** — `PT-1726`: an `HK` unit is
*"`HK-` plus two digits **not already a model name**"*. That falls out of the 38
`models.toml` already ships and needed no second list.

## 3 · ⚠⚠ A ROW SAYING `free` IS A RULING. A MISSING ROW IS A FAULT.

`PT-1726` ruled free choice for `Battle`, `Labor` and `Remote` **"made up as
the owner asked, rather than left blank"** — so all 38 models ship a row and 22
of them say so. **The alternative shipped only the 16 with prefixes, and then a
lookup that missed would read as *free choice*** rather than as *this build and
this shelf disagree*.

That is **absence-versus-error**, and it is guarded in two places:

* **the extractor refuses to write** if its model names disagree with
  `models.json`. ⚠ **Watched failing first** — one character in the document
  (`Mover Droid` → `Mover Droids`) and it named both sides and exited 1.
* **the screen refuses the step** when a droid's model has no row, with a
  sentence saying the shelf has no rule for it.

> `PT-1661`: a guard is not a guard until it has been seen to fail.

## 4 · ⚠ WHERE THE RULE LIVES, AND WHY IT IS NOT IN THE APP

`Lodestar`, beside `droidMayWield` — **and it does not know what a droid is.**
`PT-1497` is the standing rule: *"the moment this returned a `SpeciesRecord`,
`Lodestar` would acquire opinions about species, classes and professions it has
deliberately never had."* So `designationProblem` takes **a prefix, a digit
count and the taken names**, and the app gathers those from the shelf.

**⚠ AND `Loom` IS THE REASON IT IS NOT APP-SIDE.** The day the Builder
validates an authored droid blueprint it needs this exact refusal — `PT-1713`'s
shape, where the validator and the runtime say the same sentence **because they
call the same function.** A copy in Loom would be the defect; this placement is
what prevents it.

**⚠ THE GENERATOR CALLS THE VALIDATOR**, rather than reimplementing the test:
that is how a generate control stops drifting from the rule it is generating
under. 500 draws, each one put back through the check.

## 5 · ⚠ THREE THINGS I CHECKED RATHER THAN ASSUMED

**`T3-M4` is refused by the SHAPE, not by the ban list.** `PT-1720` names it as
the first collision to check, and it **is** refused — but `M4` is not two
digits, so the reserved check is never reached. **A case that typed `T3-M4` at
the screen would pass with the ban list removed entirely**, which is the
vacuous-guard shape this project keeps finding, so the screen's case types
`HK-47` at an `HK-24` unit where only the list can refuse it. `T3-M4` still has
its own case one layer down.

**`R-8009` and `HKB-3` keep their own digit counts** — four and one. `PT-1729`
made everything else uniform and named these two as **attested rather than
inferred**, so they are exceptions with evidence, not exceptions with a shrug.

**Editing the document staled two sibling extracts and I re-stamped both.**
`chassis.json` and `first_level_feats.json` also declare `CHARGEN-DATA-01`.
Both re-ran with **byte-identical records** — verified, not assumed —
and `check_extracts` is back to the same three stale comparisons it had before
this slice. **The edit added none.**

## 6 · ⚠ WHAT MOVED THAT WAS NOT MINE TO WRITE

Two existing cases moved **with** the build rather than being worked around:

* `base_rules_test`'s inventory — **22 files and 2,550 records → 24 and
  2,596.** It says in its own comment that *"a total that moves when the corpus
  grows is doing its job"*, and it did it.
* `identity_test`'s droid case asserted the screen's own apology — *"a droid's
  designation follows its chassis, and that is not built yet."* **The apology is
  gone.** The half that was never about the apology stays: a droid is not handed
  `Vash Corrin`, and the organic generator is not offered.

---

## What ran

    Lodestar   659 tests   exit 0   (+15)
    Loom       261 tests   exit 0
    app        523 tests   exit 0   (+10, and two updated)
    flutter analyze         clean, Lodestar and app
    flutter build linux     built
    gate.py                 SENDABLE, the same 2 advisory warnings

Exit codes read from `$?` directly, never through a pipe.

## Heads

    Lodestar        95bc648    engine pin upgraded in the app to match
    Loom            5ed6185    engine pin upgraded to match
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   cc4277f
    MAIN_WORK       15b8da0

**⚠ The shelf gained two files** — `base-rules/rules/designations.toml` and
`reserved.toml`. Nothing else in `base-rules` changed; the generated package
was diffed against the installed one before either was copied in.
