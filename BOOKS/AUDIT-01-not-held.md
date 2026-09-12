# AUDIT-01 — every `RULED · NOT HELD` mark, re-measured against `MAIN_WORK`

**Run after discovering `MAIN_WORK` is directly readable on this machine at
`/mnt/ga/SteamLibrary/steamapps/common/KOTOR_APP_PROJECT/MAIN_WORK`.** `OUTLINE-02`'s
`NOT HELD` marks were all measured against `HANDOFF` alone, on a belief about access
that stopped being true when the work moved machines.

**Method:** 32 lines in `OUTLINE-02` carry a `NOT HELD` mark; 48 distinct documents are
cited on them. Each was searched for across the whole `MAIN_WORK` tree by exact name,
then by stem for near-matches, so an "absent" here means absent rather than renamed.

---

## Result: 37 present, 11 absent

**The 11 absent are not scattered — they fall into two groups, and neither is a
`MAIN_WORK` problem.**

### Absent — temporal and deep-history research (8)

`ERA-VITIATE-01` · `TEMPORAL-ENUM-01` · `TEMPORAL-SWEEP-LEGENDS-01` ·
`RULING-SWTOR-DEEP-HISTORY` · `AMENDMENT-DEEP-HISTORY-BOUND` · `D-REVAN-04` ·
`D-VIT-01` · `GAZETTEER-PART-D`

### Absent — Library-consolidated findings (3)

`RCR-REPUTATION-FINDINGS` · `DECISION-FLESH-RAIDERS` · `PORT-02-v2`

**All eleven are Library-held, and the Library is not on this machine** — no `C0x`
consolidated category file exists anywhere on this filesystem. So the remaining
blockage is a Library-access question, not a `MAIN_WORK` one, and it is far narrower
than the outline currently implies.

---

## What this changes, book by book

| Book | Was | Now |
|---|---|---|
| **One — Player's Handbook** | Two gaps: `CHARACTER-CREATION-01`, `DICE-01` | **Both present.** `CHARACTER-CREATION-01` is the twelve-step creation order the PHB's own second chapter was blocked on |
| **Two — Gamemaster's Holocron** | Nine of fifteen chapters unheld | **All but two present.** `INFLUENCE-01` (in `force/`), `FACTIONS-01`, `EXPERIENCE-01`, `PARTY-01`, `ENCOUNTER-01`, `GROUND-AI-01`, `SPACE-AI-01`, `PAZAAK-01`, `SWOOP-01`, `REST-AND-MEDITATION-01`, `LOOT-01`. Only `RCR-REPUTATION-FINDINGS` and `PORT-02-v2` absent, both Influence-supporting rather than load-bearing |
| **Three — Galactic Threat Database** | **Nine of fourteen chapters unheld — the most blocked book** | **Fully present.** All nine `BEASTS-*` documents, plus `GM-CREATURES-01` and `ENCOUNTER-01`. This book goes from mostly-blocked to draftable in one step |
| **Four — Planetary Atlas** | World entries in the Atlas repo | **Unchanged** — not audited here; the Atlas repo is a separate question |
| **Five — Galactic Timeline** | *"Not startable — every chapter absent"* | **Partly startable.** The dated spine is present: `EVENTS-01`, `TIMELINE-01`, `CLOCK-01`, `EVENTS-PLAN-01`, `CANON-01-v2`, `METHOD-RECORD-01`. The deep-history and sweep research is the absent group above — so the book can open, but its Revan, Vitiate and Tales-of-the-Jedi chapters still can't |
| **Six — Species Compendium** | `DECISION-FLESH-RAIDERS` for non-playable species | **Still absent** — the one candidate source for that chapter remains Library-held |
| **Seven — Armory** | **Four chapters unheld; book declared at its ceiling** | **All four present.** `WEAPON-MATRIX-01`, `CRAFTING-01`, `LOOT-01`, `STARSHIPS-01`, `SPACE-COMBAT-01`, `MOUNTED-COMBAT-01`, `DROID-CONSTRUCTION-01`, `DROIDS-UPGRADE-01`, `PROPERTY-VOCAB-01`. **Armory is not at its ceiling — it has four more draftable chapters** |
| **Eight — Advanced Player's Guide** | Beast ownership unheld | **`BEASTS-OBEDIENCE-01` and `BEASTS-PLAYER-01` present.** The prestige-class feature gap is unchanged — that was never a holdings problem, it's genuinely unwritten |

---

## The one claim this audit does not overturn

**Prestige class features still do not exist.** `MANIFEST`'s *"prestige classes have no
lists anywhere — that is an open design question, not an omission. Do not synthesise"*
was never about a document being unreachable. Having `MAIN_WORK` open changes nothing
there, and the `GAP` mark on Book Eight's prestige chapter stands as written.

**Likewise beast "upkeep"** — flagged in Chapter Eight of Armory as unauthored anywhere
rather than merely unheld. Now checkable against the real `BEASTS-*` set rather than
inferred, but not checked in this pass.

---

## What this audit was, and was not

**Was:** a filesystem measurement of whether cited documents exist. Mechanical, cheap,
and exactly as reliable as `find` is.

**Was not:** a read of any of those 37 documents. **Present is not the same as saying
what they contain, or that what they contain matches what `OUTLINE-02` claims about
them.** Several outline rows make specific claims — `STARSHIPS-01`'s "21 hull rows,"
`BEASTS-ENTRIES-01`'s "27 creature companions" — sourced from correspondence rather than
the documents themselves. Those remain unverified and should be treated as such until
each chapter is actually drafted against its source.
