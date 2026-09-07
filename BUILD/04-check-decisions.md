# 04 · `check_decisions.py` — the boundary nothing watched

**`MAIN_WORK`.** Registered in `gate.py` as **reporting, not blocking**.
Current run: **resolved 346 · family 3 · unresolved 1 · citation-older-than-decision 2.**

---

## ⚠ FOUR REGISTERS, NOT THREE

The brief named three. **The check found a fourth, by reporting 44 ids as
missing and being right about the lookup and wrong about the world.**

| Scheme | Where |
|---|---|
| `PT-*` | `MAIN_WORK` |
| `D-NAME-NN` | `ATLAS/decisions/` — 34 files |
| `D-XY` | `KOTOR_RPG_Library` |
| ⚠ `D-Wn` | **`MAIN_WORK/rules/WORLDS-REGISTER-01.md`** — 44, defined in its own headings |

**Nobody had counted the fourth as a register**, including me, in the report that
said there were three.

## ⚠ AND THE LIBRARY HAS MORE THAN ONE REGISTER

The brief pointed at `consolidated/C12-DECISION-REGISTER.md`. Reading only that
one reported **`D-AG`, `D-AH`, `D-AI` and `D-AT` as resolving to nothing.** They
are in **`LIBRARY-INDEX-01.md`**, which C12 does not contain.

> **⚠ That is a wrong-place negative, produced by the check written to catch
> wrong-place negatives.** It was caught by not believing the first answer —
> the brief said `D-AJ` was a Library id, the check said it was not, and the
> disagreement was the signal.

`D-AJ` itself appears in C12 **only inside a `_dead/` filename**, so it is a
retired Library decision rather than a live entry.

## How it resolves — by MEMBERSHIP, never by shape

`D-MENU4` has no dash before its digit; `D-AGE-01` does. **A shape rule would
have split them into the wrong registers.** So the check asks each register for
its own id list and resolves by membership. Anything matching none is the
finding.

**One more trap it had to learn:** a naive `D-[A-Z]{1,3}` over the Library text
harvests a phantom **`D-AGE`** out of the Atlas's `D-AGE-01`. Negative lookahead.

## What it found

**⚠ 2 · CITATION OLDER THAN THE DECISION IT CITES** — the `D-MENU4` failure shape,
live:

    D-OPEN-01   rules/DROID-MODELS-01.md
                decision changed 2026-09-03 · document last touched 2026-09-02
    D-OPEN-01   rules/ENCOUNTER-01.md
                decision changed 2026-09-03 · document last touched 2026-09-03

Both cite an Atlas decision that has moved since. **Neither is resolved here** —
whether the documents still agree with `D-OPEN-01` is a read, not a date.

**1 · UNRESOLVED** — `D-AJ-SENTINEL`, cited by `REGISTER.md`,
`comms/INTEGRATOR-HANDOVER.md` and `comms/LIBRARY-HOLDINGS-QUERY.md`. It names a
Library file that now sits in `_dead/`.

**3 · FAMILY REFERENCES, NOT MISSING IDS** — `D-CARD`, `D-EXCEPT`, `D-REVAN`.
Prose naming a family whose members are `-01`, `-02`… **Reported as their own
class**, because calling them missing would be the same error as calling `D-W1`
missing.

## ⚠ IT FAILS LOUDLY WHEN IT CANNOT LOOK

If either remote register is unreachable it prints **"CANNOT RUN — this check has
NOT looked and is reporting nothing, not finding nothing"**, names the repo and
the error, and says the access is asymmetric. It does **not** return a clean run.

> **This is the fourth wrong-place negative in the project, and the third was
> `check_extracts.py` itself** — reporting *source not on disk* for a file that
> was on disk, because it never searched `force/`.

## ⚠ THE LIMIT, IN THE SCRIPT'S OWN OUTPUT

Every run ends with it:

> **NAMES AND DATES ONLY. This cannot tell whether a decision's CONTENT still
> agrees with the document citing it — `D-MENU4` changed three to four without
> changing its filename. A fingerprint proves a match, never that the match was
> right.**

Same limit as `check_extracts.py`. Third time it has been the important sentence.

## The access gap, unsolved

It runs from this agent's token and **404s from the owner's**. A register it
cannot reach makes it refuse rather than pass. **A check that runs for one
participant is a check with a gap in it**, and closing that is a token decision,
not a code one.

## Not done

Did not read the other 28 Atlas decisions. Did not resolve the two `D-OPEN-01`
citations. Did not rule on whether four registers should become one.
