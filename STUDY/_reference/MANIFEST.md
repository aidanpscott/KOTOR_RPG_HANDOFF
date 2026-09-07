# Extraction sources — fingerprinted

**Placed here because the extraction agent cannot read `MAIN_WORK`.** These are copies. **Do not edit; report instead.**

| File | md5 | lines | §1 heading |
|---|---|---|---|
| `SKILLS-01.md` | `e157dea6` | 735 | **TWENTY-SIX SKILLS — 25 CHARACTER + `Fly`, BEAST-ONLY** |
| `CLASSES-FORCE-PHB.md` | `ebc82531` | 222 | — |

**⚠ `CLASSES-FORCE-PHB` hashes to `ebc82531`, which matches `WHERE-IS.md` exactly.** The Library's index and this copy are the same file.

**⚠ `SKILLS-01` does NOT match `WHERE-IS`'s `15316c4f`, and that is expected** — it was edited today: descriptions added (`PT-1291`), the count corrected to 25 (`PT-1292`, `PT-1293`), and **`§9.2b` written** with the merged class lists (`PT-1299`).

**What the agent flagged as stale is confirmed stale.** `docs/SKILLS-01.md` at `53fcd1b2`, 538 lines, "Twenty-two skills" — **that is a much older snapshot and must not be used.** The file here is 735 lines and says twenty-six.

## What to extract

**`SKILLS-01`** — the master table (26 rows, one marked `BEAST ONLY`) and the **Descriptions** section near the end.

**`SKILLS-01 §9.2b`** — merged standard class lists, **14 classes**. This supersedes `§9.2` and `CLASSES-STANDARD-PHB`.

**`CLASSES-FORCE-PHB`** — the six Force classes. **⚠ Verify they agree with `§9.2` rather than assuming it** — they did when checked at `PT-1299`, and that agreement is itself the evidence dating the standard-class conflict.

**⚠ Prestige classes have no lists anywhere. That is an open design question, not an omission. Do not synthesise.**


---

## Batch 2 sources — the remaining eight extractions

**Same rules as before: fingerprint before extracting, count and diff by name, leave unclear values null and say so.**

| File | md5 | lines |
|---|---|---|
| `UPBRINGING-01.md` | `d329117d` | 105 |
| `PROFESSIONS-01.md` | `2dbd0350` | 459 |
| `PROGRAMMINGS-01.md` | `b1a8469e` | 143 |
| `SPECIES-CHAPTER-v2.md` | `404f5193` | 1274 |
| `CLASS-ROSTER-01.md` | `409c0618` | 1097 |
| `FEATS-LIBRARY-01.md` | `5d467121` | 1667 |
| `WORLDS-REGISTER-01.md` | `2107a586` | 560 |
| `EQUIPMENT-01.md` | `10246592` | 322 |

**⚠ Expected counts, so a mismatch is visible immediately:**

| Extract | Expect | Source |
|---|---|---|
| `upbringings.json` | **9** | `UPBRINGING-01` |
| `professions.json` | **21** | `PROFESSIONS-01` |
| `programmings.json` | **17** | `PROGRAMMINGS-01` |
| `species.json` | **31 organic** + droid chassis | `SPECIES-CHAPTER-v2` |
| `classes.json` | **18 base** (12 standard + 6 Force) + prestige | `CLASS-ROSTER-01` |
| `feats.json` | **156** | `FEATS-LIBRARY-01` |
| `worlds.json` | — no expected count; report what you find | `WORLDS-REGISTER-01` |
| `equipment.json` | — no expected count | `EQUIPMENT-01` |

**⚠ Where a count is absent above, that is deliberate — do not invent one to check against. Report the number you get and say it was unverified.**

### Two traps this corpus has already sprung

**⚠ INTERRUPTED TABLES.** `SKILLS-01`'s master table was broken by two prose lines mid-table, and a consecutive-row parser returned **24 from a 26-row table** — silently. **It was fixed there; ten more interrupted tables exist elsewhere in the corpus** (`PT-1301`). **Read a section before parsing it.**

**⚠ QUOTED HISTORICAL ERRORS.** This corpus records its own corrections **in place**, so a document may contain the text of a claim that was later overturned. `SKILLS-01` line 15 quotes *"twenty-two skills"* as an error `PT-865` fixed. **Read for what a document ASSERTS, not what it QUOTES.**

### Order

**Smallest first** — `UPBRINGING-01` at 105 lines, then `PROGRAMMINGS-01`, then up. **A shape problem is cheaper to find on nine records than on 156.**


---

## Batch 3 — class MECHANICS, powers, models

**⚠ `TRACE-98` extracted `CLASS-ROSTER-01` and took only the roster.** `classes.json` carries `id`, `name`, `tier`, `state` — **no vitality die, no skill points, no class skills, no feat schedule.** Chargen cannot build Abilities, Skills or Feats on it.

| File | md5 | lines |
|---|---|---|
| `CLASSES-STANDARD-PHB.md` | `6b54303d` | 1269 |
| `CLASSES-FORCE-PHB.md` | `ebc82531` | 223 |
| `CLASS-TABLES-JEDI.md` | `e734c5c9` | 224 |
| `CLASS-ROSTER-01.md` | `80ef115f` | 1101 |
| `DROID-MODELS-01.md` | `44dc8178` | 1066 |
| `FORCE-POWERS-01.md` | `ff73a7f4` | 253 |

**⚠ AND `CLASS-ROSTER-01` DOES CARRY MECHANICS — the earlier pass just did not take them.** `§PT-717` has **primary and secondary ability for all base classes**, with `PT-246`'s model: *the first ability sets one strong save, the second sets another; if both point at the same save, the class has one strong save.*

**So this is not a new source. It is the same file, read further.**

### What is wanted

- **`classes.json` REPLACED** — the roster plus every mechanical field `CHARGEN-DATA-01 §3` names
- **`powers.json` NEW** — `FORCE-POWERS-01`, never extracted. `PT-1317` counted 112
- **`models.json` NEW** — `DROID-MODELS-01`, and **⚠ `CHARGEN-DATA-01` never asked for it**, which is why nobody noticed

**⚠ Two count checks already established:** **19 base classes** (`TRACE-98`, and `PT-1295`'s 18 was one short — `Saboteur`) and **38 total**. **112 powers** is from a ruling, not a count — **verify it.**


---

## ⚠ Batch 3a — RE-STAGED, and three files that were never staged at all

**⚠ `SKILLS-01` was STALE and that is my error.** It was staged once, long ago, at `e157dea6`. **`§9.2c` — the ranked prestige lists, `PT-1322` — was written FIFTEEN RULINGS LATER and never re-staged.** The agent read a copy that predates it and correctly reported the section as absent.

| File | md5 | lines |
|---|---|---|
| `SKILLS-01.md` | `f555ee88` | 831 |
| `CLASS-TABLES-AUTHORED.md` | `2a21ce25` | 1152 |
| `CLASS-TABLES-BASE.md` | `248ad8f7` | 348 |
| `CLASS-TABLES-DROID.md` | `203ea695` | 89 |

**⚠ `CLASS-TABLES-AUTHORED` was named by `CLASSES-FORCE-PHB` as holding the Sith progressions and was never staged** — which is why the three Sith base classes have no feat schedule.

**⚠ And `CLASS-TABLES-BASE` and `CLASS-TABLES-DROID` exist and nobody has ever mentioned them.** Four `CLASS-TABLES-*` files exist; **one was staged.**

**Re-run the class extraction against these.** The three Sith progressions, the prestige class skills, and whatever `CLASS-TABLES-BASE` and `-DROID` carry that `CLASSES-STANDARD-PHB` does not.
