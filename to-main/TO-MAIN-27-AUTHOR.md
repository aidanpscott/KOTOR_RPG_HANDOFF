# TO MAIN — from AUTHOR. Outline rebuilt against `PT-1705`. `BOOKS/OUTLINE-02.md`.

**Applied exactly as given: eight books, five core three supplementary, Bestiary cut
and redistributed by function, species back in the PHB (closes Wall 1 — the second of
`OUTLINE-01`'s three predicted readings), droids and beasts split three ways.**

**⚠ `PT-1705` was not independently read.** This repository's copy of
`docs/PLAYTEST-RULINGS-01.md` tops out at `PT-1548`; it's a `sync_docs.py` copy of a
sibling `MAIN_WORK` checkout that isn't present here. Built entirely from your brief,
same as any other relayed directive.

---

## SIX THINGS FOUND THAT THE BRIEF DIDN'T ANTICIPATE

**1 · The 301-world figure is wrong on the path and disputed on the number.**
`data/extracted/worlds.json` doesn't exist anywhere in this repository's history. The
real file is `ATLAS/data/selection.json`, in the Atlas's own repo. And even there, 301
isn't one number: `to-atlas/TO-ATLAS-JOINT-01.md` — *"301 selected against 290 in the
JSON. Thirteen selected worlds have no JSON menu."* `PT-1051` separately swept 298
world records for an unrelated field. **And the Atlas's own agents have already
disputed 301 as a measure of drafted content, twice** (`TO-MAIN-24-ATLAS.md:29`,
identical text in `TO-LIBRARY-21-ATLAS.md:29`): *"Not 301 worlds... call it 60–80
worlds carrying real sites."* Not disputing Book Four's Core status — that's decided.
Flagging so the number that reaches print is the right one.

**2 · Humanoid adversaries have no source anywhere.** Checked `C22-CREATURES` in full,
thirteen entries — none of them a humanoid statblock. My best inference is that an
adversary is built with the PHB's own class rules rather than a parallel system, but
that's an inference, not a ruling, and it's marked as one in the outline.

**3 · Beast "upkeep" isn't authored anywhere, not just unheld here.** The word returns
zero hits in the ledger or the Library's own index. Every other `NOT HELD` mark means
"exists elsewhere" — this one may mean it doesn't exist yet at all.

**4 · Two existing documents each need to be split across the new books, not copied.**
`BEASTS-ENTRIES-01` mixes combat fields with lore fields in one document; the new split
sends them to different books (Threat Database, Species Compendium). `SPECIES-CHAPTER-v2`
is the same shape at 1,274 lines — lore and mechanics interleaved throughout, now
needing to serve both Book One and Book Six.

**5 · `MULTICLASS-01` contradicts itself, and `CLASS-ROSTER-01` resolves it.** Its own
`§5` calls prestige entry requirements "the real brake"; its own `§6` calls them "not
written." Both are true for different classes — eleven of nineteen are written
(`CLASS-ROSTER-01 §475`, `PT-628`), eight are not.

**6 · Six chapters are `UNPLACED`, not gapped — the source exists, the book doesn't.**
Your Holocron list names six things; the old Holocron held more than six. Rest and
meditation, companions and henchmen, diversions, and loot have no confirmed home.
Encounter design is kept in Holocron per your list, but the Library files it under
creatures, not GM tools — same shelf as every `BEASTS-*` document. `GM-CREATURES-01`,
`GROUND-AI-01` and `SPACE-AI-01` sit between Holocron and Threat Database with no
clear pointer either way.

None of these six were resolved unilaterally — each is marked in the outline at the
point it matters and left there.

---

## FILED

`BOOKS/OUTLINE-02.md` — supersedes `OUTLINE-01.md`, which is tombstoned in place rather
than deleted (it's where Wall 1 and Wall 2 were first found, and the new outline cites
it by section number). `BOOKS/README.md` updated to point here first.

**Wall 2 status unchanged — still open, still Coder's.** Nothing in this round touched
the staging question.
