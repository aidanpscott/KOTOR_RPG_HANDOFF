# 05 · Two fixes to `check_decisions.py`, and what the stale citations said

**`MAIN_WORK`.** Current run: **resolved · 1 unresolved · 3 family · 2
citation-older-than-decision.** ⚠ **And a contradiction the date test could not
see.**

---

## 1 · ⚠ IT CRASHED ON THE FAILURE IT MET, NOT THE ONE IT EXPECTED

`gh` is not installed in the owner's container. The script raised
`FileNotFoundError`, the gate printed `[ERROR]` and a traceback fragment, **and
still reported sendable.**

The fail-loudly path covered a register returning **404**. It did not cover the
**tool being absent** — so the check built to prevent wrong-place negatives
produced one, in its own error handling. **Fifth in the project, second inside a
check written to stop them.**

Fixed: `gh` missing now raises `ToolMissing` and takes the same *"CANNOT RUN —
this check has NOT looked and is reporting nothing, not finding nothing"* path,
naming `gh` rather than a repo. **No traceback, and the local register is still
counted so the reader can see what was skipped.**

## 2 · ⚠ IT NOW PRINTS ITS OWN SCOPE, EVERY RUN

    registers consulted:
       atlas             34 ids    aidanpscott/KOTOR_RPG_ATLAS decisions/
       library           47 ids    …/C12-DECISION-REGISTER.md, LIBRARY-INDEX-01.md
       worlds-register   44 ids    rules/WORLDS-REGISTER-01.md

and, when it cannot look:

    atlas             ⚠ NOT READ
    library           ⚠ NOT READ
    worlds-register   44 ids

> **Nothing enumerates registers. Each was found by tripping over it.** A fifth
> will announce itself as an id resolving to nothing, and the reader can now see
> immediately which shelves were searched.

**Two placeholders also classified:** `D-NAME-NN` and `D-XY` are the *notation
for a scheme*, written in documents describing the registers. They name a shape,
not a decision.

## 3 · The two stale citations — one agrees, one does not

### `DROID-MODELS-01` — ⚠ AGREES

> *"THEIR MENUS ARE AUTHORED, NOT DERIVED, AND THEY ARE MARKED SO.
> `D-OPEN-01`'s `blank` IN A DIFFERENT SCHEMA."*

An **analogy**, borrowing the vocabulary. `blank` still means a name and nothing
else, so the analogy still holds. **Flagged by date, sound on reading.**

### `ENCOUNTER-01` — ⚠⚠ CONTRADICTED BY THE DATA

> *"`D-OPEN-01` DEFINES THREE VALUES 'ON EVERY WORLD RECORD.' **NO WORLD RECORD
> CARRIES ONE.** I SWEPT ALL 298: `openness` APPEARS ON ZERO ENTRIES. IT EXISTS
> **ONLY IN THE RULING THAT DEFINES IT**."*
>
> *"`§5c` IS WRITTEN AGAINST A FIELD THAT WAS NEVER POPULATED."*

**`ATLAS/data/openness.json` carries `openness` for all 298 worlds** — `open`
247, `dense` 41, `blank` 10 — each with a `basis`, a `ruling` of `D-OPEN-01`,
and **`asserted: 2026-09-01`**. Populated at `PT-1061` by `tools/openness.py`,
proposed-and-reviewed, with four hand overrides that each record why.

**I exported it this week: 292 of 301 worlds in `worlds.toml` carry it.**

> **The sweep was true when it was run and is not true now.** `PT-1051` blocked
> on it and nothing unblocked.

### ⚠ AND A THIRD DOCUMENT CARRIES IT, WHICH THE DATE TEST DID NOT CATCH

`design/ENGINE-SPEC-02-GENERATOR.md:252`:

> *"**BLOCKED — `PT-1051`.** THE ATLAS SWEPT ALL 298 WORLDS: `openness` APPEARS
> ON ZERO ENTRIES."*

**A generator feature is marked BLOCKED on a claim the data contradicts.**

    D-OPEN-01 changed            2026-09-03T12:55Z
    openness asserted            2026-09-01
    ENCOUNTER-01 touched         2026-09-03T12:28Z   ⚠ flagged
    DROID-MODELS-01 touched      2026-09-02T13:30Z   ⚠ flagged, and fine
    ENGINE-SPEC-02 touched       2026-09-05T19:27Z   ✓ passes, and is stale

> **⚠ The stalest of the three passes the date test**, because the document was
> edited for an unrelated reason after the decision moved. **This is the script's
> own stated limit demonstrated on the first case it was pointed at:** names and
> dates only, never whether the content still agrees.

## Reported, not resolved

`ENCOUNTER-01 §5c` and `ENGINE-SPEC-02 §7a` are blocked on a sweep that has since
been answered. **Unblocking them is the owner's**, exactly as `D-MENU4` was — and
`PT-1051` is a ruling, not a note.

## Not done

The other 28 Atlas decisions. Whether four registers become one. The
`_fourth_state` proposal in `openness.json` — `blank` meaning two opposite
things, split by an `emptied` flag — which `ENGINE-SPEC-02:297` already discusses
and which is a live question I did not enter.
