# RECON — where the world roster and its menus actually are

**⚠ Reconnaissance only. Nothing extracted, nothing staged, nothing changed.**
Whether the Atlas becomes a staged source, a repo in scope, or something copied
across is a decision above this agent.

---

## 1 · What I can read

**⚠ `aidanpscott/KOTOR_RPG_ATLAS` IS READABLE FROM HERE.** Private, `main`,
183 entries. It 404s to the owner's token and does not to mine.

`gh repo list` returns **21 repositories**, and two more carry project material
that **nobody has named in any brief**:

| Repo | Bearing on this |
|---|---|
| `KOTOR_RPG_ATLAS` | ⚠ the worlds, the menus, and the decisions that govern both |
| `KOTOR_RPG_Library` | ⚠ holds `sources/atlas-reference/menus__ATLAS-COPY-*.py` — a **copy** of the Atlas menu corpus, and `incoming/WORLDS-REGISTER-01__FILED-C12-*.md` |
| `kotor-engine` | `research/TRACE-*` only. Not world data |

## 2 · ⚠ `WORLDS-MENUS-01` DOES NOT EXIST

Searched all four project repositories by tree. **No file of that name anywhere.**
`CHARGEN-DATA-01` names it as the source for the Origin world list and skill
menus; **the name refers to nothing.**

## 3 · What the world data actually is — three separate things

| | What | Where | Size |
|---|---|---|---|
| **the gazetteer** | `system · sector · region · coord`. **No mechanics at all** | `ATLAS/data/register.json` | **4,931** systems |
| **the selection** | the worlds actually in play: `tier · system · sector · region · coord · note` | `ATLAS/data/selection.json` | **301** |
| **the menus** | ⚠ **a program, not a data file** | `ATLAS/tools/menus/` | 6 modules, ~1.2 MB |

**⚠ `worlds-policy.json` in MAIN_WORK is a fourth thing again** — the register's
*admission policy*, 47 rows of exclusion classes and evidence predicates. It was
never a roster and is not one now.

## 4 · ⚠ THE MENUS ARE FOUR SKILLS, NOT THREE

`ATLAS/decisions/D-MENU4.md`, owner ruling:

> **"A world offers four trainable skills. The player picks one at character
> creation. The pick receives +2 and aptitude."**
> *"Supersedes the verbal three-skill ruling made during the menu build."*

**`CHARGEN-DATA-01` and `APP-UI-VISION-01 §0` both say THREE.** They predate this
and nobody carried it across. **The app's Origin screen currently says three; it
is wrong, and it is wrong because it was told three.**

### The live corpus, asked through its own resolver

`tools/menus/README.md` says *"Ask the program. Do not read a list here."*
`edit_entry.MODULES` → `menus.py · menus2.py · m_a.py · m_b.py · m_c.py · m_d.py`.
`resolve.menus()` returns:

    298 worlds
    272 with FOUR skills      D-MENU4 applied
     13 with THREE            ⚠ D-MENU4 is "applied where the menu is
                                finished, and nowhere else"
     13 with NONE             D-NOMENU-01 — the added worlds take no menu
     25 distinct skills used, and Survival IS among them

**⚠ So the corpus is CURRENT and PARTIALLY MIGRATED.** It postdates `PT-552`,
which added `Survival` — unlike `data/teaching_menus__SUPERSEDED-EXPORT-PRE-PT552.json`,
which holds 284 worlds at exactly three skills and is marked superseded in its
own filename.

**There is no current EXPORT.** The only machine-readable menu file in the Atlas
is the superseded one. The current data exists only as executable Python.

## 5 · The cardinality band exists too

`ATLAS/decisions/D-CARD-01.md` — owner ruling, governs **which worlds a species
may claim as a homeworld**. Its own reasoning: *"47 species records × 290 worlds
is 13,630 combinations… a character sheet reading `Rakata, homeworld Coruscant`
would pass silently."* `CHARGEN-FLOW-MAP-01 §4` feeds a cardinality band from
Origin, and this is it.

## 6 · What this means for the Origin stop

The data is not missing. **It is in a repository outside the staging path, in a
form nothing downstream can read, under a ruling the consuming documents do not
know about.** Three separate problems, and only the first is a staging fix:

1. the Atlas is not in the staging path
2. the menus are a **program**, not an export — and the only export is superseded
3. `D-MENU4` says four and `CHARGEN-DATA-01` says three

**⚠ (3) is the one that matters most**, because it is the same shape as
`TRACE-100`: a downstream consumer faithfully implementing a superseded number.
The Origin screen would have shipped a three-skill menu and passed every test.
