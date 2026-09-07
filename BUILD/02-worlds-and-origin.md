# 02 · The world menus exported, and Origin completes

**`MAIN_WORK` `e5d68ab` · `KOTOR-RPG-APP` `addeb81`.** 72 tests pass.
`check_extracts.py`: **current 21, stale 0**.

---

## Asked the program, exported once, shipped the export

`ATLAS/tools/menus/README.md`: *"Ask the program. Do not read a list here."*
`edit_entry.MODULES` → six modules; `resolve.menus()`, `resolve.status()`,
`resolve.key()` answered.

**301 worlds** from `selection.json`, now `base-rules/rules/worlds.toml`.
base-rules is **11 kinds, 972 records**.

## ⚠ Four menu states, and they were distinguished by ASKING

| state | n | what it means |
|---|---|---|
| `complete` | **271** | four skills — `D-MENU4` applied |
| `unfinished` | **13** | three skills — `D-MENU4` is *"applied where the menu is finished, and nowhere else"* |
| `none` | **12** | `D-NOMENU-01` — a place described inside another entry |
| `ineligible` | **5** | ⚠ **not a world at all** — a region, a cluster, a void |

**⚠ I did not infer these from a skill count.** `resolve.status()` returns
`('ok'|'ineligible'|'missing', detail)` and its own docstring calls it *"the
distinction the old checker lacked"*. Skill count separates `complete` from
`unfinished` from `none`; **only the resolver separates a world with no menu
from a thing that is not a world.** Inferring would have merged the last two,
which is `TRACE-82`'s `****` a fifth time.

**⚠ And the brief's "13 and 13" was 13, 12 and 5** — the second 13 was counted
over `menus()` (298 keys) rather than over `selection.json` (301 rows).

## ⚠ The band is not a world property

`D-CARD-01`: *"Cardinality is a property of the **species**, not the world. The
world says who lives there."* So **no world carries a band.** The band travels on
each `species_presence` entry, which is where the two meet at the character sheet.

**41 of 301 worlds list any species**, and that is by design: *"THE OTHER 256 ARE
NOT EMPTY — they are UNLISTED, which under Regional and Diaspora means UNKNOWN."*
Exact only under Locked and Paired.

## ⚠ Provenance is the resolver, not a digest

A fingerprint proves an extract matches its source and says **nothing about
whether that source was superseded**. `teaching_menus__SUPERSEDED-EXPORT-PRE-PT552.json`
would have passed one perfectly while being three skills and pre-`Survival`.

So `_source` is `kind: resolver-export` and records the repo, the **commit**
(`83748f7b`), which functions were asked, the six modules and their digests, and
the export time. `check_extracts.py` recognises the kind and reports it.

## Origin, rebuilt

Four skills, not three. **The screen said three because `CHARGEN-DATA-01` said
three, and it was carrying a number `D-MENU4` had superseded** — the same shape
as `TRACE-100`: a faithful implementation of the wrong thing, passing every test.

**Only `complete` worlds are offered.** A three-skill menu is unfinished
authoring, not a smaller offer; picking from one would grant an aptitude the
ruling has not settled.

**⚠ 17 worlds carry more than one stratum**, each with its own four — Taris by
Upper City, Lower City and Undercity; Arkania by Pureblood and Offshoot. Picking
a world resolves to its first stratum and **clears any aptitude chosen under
another**, because a different stratum offers a different four.

> **Origin now completes, so the strip unlocks past step 1 for the first time
> and GENDER is reachable for an organic.**

## For the owner — `ATLAS/decisions/` holds 34 files

**⚠ `MAIN_WORK` has never read any of them, and `D-MENU4` sat here superseding a
ruling three of our documents still carried.** Filenames only, not read:

    ATLAS-CORRECTIONS-01  ATLAS-RECON-01
    D-AGE-01   D-BLOCK-01  D-CARD-01   D-CLOSE-01
    D-CRAFT-01 D-CRAFT-02  D-CRYSTAL-01 D-CURRENCY-01
    D-DUDS-01  D-EXCEPT-01…07  (seven)
    D-MAL-01   D-MANDO-01  D-MENU4     D-NAMES-01
    D-NOMENU-01 D-OPEN-01  D-REVAN-01…04 (four)
    D-ROLE-01  D-SWTOR-01  D-TIEBREAK-01  D-TIEBREAK-01-RULE3
    D-URKUPP-01 D-VIT-01

**Bearing on chargen by name alone, unverified:** `D-AGE-01` (a minimum age rule
`D-CARD-01` already leans on for Dashade), `D-VIT-01`, `D-ROLE-01`,
`D-NAMES-01`, `D-CRYSTAL-01`, `D-OPEN-01`.
