# TO-MAIN-01 — S12 status, from the session that picked up after you

**⚠ Nothing here is authoritative. The working tree is. Written so you can see what moved and why, without re-deriving it.**

**Rulings `PT-410` through `PT-424`. Index at 409.**

---

## What I was asked to do, and what I actually did

**The bootstrap pointed me at beast feats. ⚠ I have not started them.** **Two things had to come first and both turned out bigger than they looked.**

---

## 1. ⚠ The gate has been blind since the directory reorganisation — `PT-410`

**`python3 scripts/gate.py` — not `feats/gate.py`; the bootstrap path does not exist.**

**It reported 12 blocking failures. Ten of them are `FileNotFoundError`.**

    audit_sheets · audit_refs · audit_skills · audit_skillfeats
    audit_classfeats · audit_classskills · audit_chassis
    audit_rulings · audit_seed · audit_classroster

**21 scripts resolve documents at `scripts/../NAME.md`. The documents live in `rules/`, `playtest/`, `comms/` now.**

> **⚠ `gate.py` judges a check on returncode alone and filters stdout for `>>`. A crash and a real defect are the same signal.**

**Those ten checks would report BLOCK on a spotless corpus and BLOCK on a filthy one. They have had zero discriminating value since the move.** **Any "the gate caught it" attributed to them since then was attributed to a check that never opened a file.**

**⚠ `audit_paths.py` PASSES.** **It tests for hard-coded ABSOLUTE paths. These are relative.** **`PT-407` exactly — a correctly scoped check whose scope excluded the only tree with the answer.**

**⚠ `playtest/make_index.py` and `scripts/make_index.py` are byte-identical and only the `playtest/` one runs.** **The other throws the same `FileNotFoundError`. Same defect, in the tool that feeds the library.**

**NOT FIXED. Left for you or for me next session.** **The fix is mechanical — repoint the 21 scripts — plus one line in `gate.py` so a crash prints `[ERROR]` rather than `[BLOCK]`.** **Without that second part this recurs the next time anything moves.**

---

## 2. `PT-379`'s fork is closed — `PT-423`. ⚠ And I was wrong about which side was stale

**Fork list 39 → 0. `audit_duplicates` passes for the first time.**

### ⚠ Read this part if you read nothing else

**I proposed deleting the `rules/` duplicates. That would have destroyed live work.**

**I had two data points — `PLAYTEST-RULINGS-01` 72 rulings behind, `AGENDA-CURRENT` pre-S11 — and generalised from them.** **Derived per pair, `rules/` was AHEAD or diverged on 26 of 32.**

> **⚠ `rules/FORMS-01.md` held 248 lines absent from `force/`, including `§2.2` — the implementation of `PT-185`.**

**The bootstrap says `force/` is STALE. It is. Which is precisely why the `rules/` copy was the live one there.**

**⚠ `PT-379` was not a bulk copy that got abandoned. It was a bulk copy after which BOTH sides kept receiving edits.**

### Method, so you can audit it

**Merge base per pair = the earlier-created path's blob at the commit where the SECOND copy was added.** **At that instant they were identical, which is what makes it a base.**

**`git merge-file --diff3` on 29 pairs: 27 clean, 2 conflicts.**

| | |
|---|---|
| Byte-identical, deleted | 10 |
| Canonical ahead, deleted | 7 |
| Three-way merged into canonical | 27 |
| Conflicts adjudicated | 2 |
| Check defect, not a fork | 1 |

**⚠ The merge DROPPED content and that was correct.** **`ACTION-ECONOMY-01` lost `comms/`-only lines because `rules/` had deleted them deliberately:**

    "Read the Ground"   base ✓  rules ✗  comms ✓  merged ✗   PT-207 replaced it
    "Terrain Sense"     base ✗  rules ✓  comms ✗  merged ✓

**A three-way merge preserves deletions. A two-way union would have resurrected `Read the Ground` and the pre-`PT-144` Jedi armour rule.**

### ⚠ Seventeen documents were serving superseded class names

**Every small divergence was a rename the project had RULED, applied on the `rules/` side and not the canonical one:**

    Scoundrel → Smuggler          PT-73
    Combat Droid → Marksman       PT-75
    Expert Droid → Engineer       PT-76
    Tech Specialist → Machinist   PT-83, PT-225
    Explorer → Treasure Hunter    PT-238
    Doctor → Medic                PT-243
    Force Focus → Force Channel   PT-103, PT-186
    C-ids → PT-ids                PT-113

**Anyone opening the wrong path got a pre-rename snapshot.**

### `FORCE-POWERS-01` — resolved by derivation, not by reading

**140 lines only in `rules/`, 73 only in `force/`. Ten conflict hunks.** **I keyed both tables by power name instead of adjudicating by eye:**

    canonical-only lines             73
    with a same-named row in rules/  73
    ⚠ ORPHANS                          0

**All 73 are pre-conversion versions of rows `rules/` also holds** — `PT-24`'s seconds ÷ 3, `PT-301`/`PT-302`'s dice caps, `PT-297`'s Afflict figures, the `Force Wound` → `Force Strangle` rename.

### ⚠ Two things I did NOT fix

**`Force Breach` reads *"All six tiers of Force, but the target can reactivate them…"*** — a dangling clause left when `Inspire Followers` moved to the Officer as `Rally`, `PT-221`/`PT-224`. **Repairing it inside a merge would hide a content edit inside a structural one.**

**`README.md` was a CHECK defect — `PT-424`.** **Six per-directory READMEs that are supposed to differ.** **One-name `CONVENTION` exemption added, scope printed.** **⚠ Third defect of this class this session after `PT-410` and `PT-400`: a check correct about its literal test and wrong about what the test stands for.**

---

## 3. The Aqualish — `PT-412` to `PT-422`

**Owner supplied the UAA and Campaign Guide as scans. OCR'd at 400 dpi, columns split by hand.**

**`UAA f.14` was read. Folio offset measured on three anchors — `UAA folio = PDF page − 1`, recorded in `data/books/README.md`.** **⚠ Anchor on the phrase `X Species Traits`, not the species name: the running footer lists neighbours and a bare name matches the facing page.**

**⚠ The book contradicted three things I had asserted from a wiki:**

- **`+4 Swim` for the Aquala was PORTED all along.** **`SPECIES-MASTER` was right, `PT-408` was the departure, and the unexplained edit I flagged was somebody correcting me.**
- **`−2 Wisdom` is in the source.** **`PT-408` dropped it without recording the drop. Restored.**
- **The source DOES differentiate the subraces** — on Swim and on `Fins`. **I had said it did not.**

**`Fins` is a PENALTY in the book. Ported narrowed — `−4` on fine-manipulation gear, weapons excluded — with a benefit added back by owner ruling: full-speed swimming.** **⚠ The Aquala is now the fastest swimmer on the roster, ahead of the Nautolan. Deliberate.**

**⚠ And I broke the skill budget in the same batch that discovered it — `PT-420`.** **43 of 48 entries total exactly `+4`. I gave the Quara and Ualaq three bonuses each.** **A ported value arriving into an authored record is a CLAIM ON THE BUDGET, not an addition. Something already there has to leave.**

**Age bands closed at `UAA f.14`. Roster 33 of 33 — as of `PT-419`, and the next species added makes that false again.**

---

## ⚠ What is open

**`PT-410`** — the 21 scripts, and `gate.py`'s crash-versus-block conflation. **The single highest-value fix in the repo.**

**`PT-415`** — `The New Essential Guide to Alien Species` is unranked and I am citing it in the species chapter under a pending flag.

**Two derived counts are marked `⚠ STALE — regenerate`** in `RACIAL-FEATS-01` and `SPECIES-MASTER §4`. **⚠ I could not reproduce the original generator's counting rule — mine disagrees by nine — and I would not type a number I derived a different way. `PT-59`.**

**`audit_source`** still blocks on `REGISTER.md` and `REPLY-LIBRARIAN-09.md` claiming chain counts that match no roster. **Untouched.**

**Beast feats. Not started.** **`PT-357` ruled the shape; ~250 picks across 27 beasts.**

---

## ⚠ Repo state

**87 files staged in `MAIN_WORK`. NOTHING COMMITTED.** **`send.py` refuses on a blocking gate failure and the gate blocks on 11 — ten of which are `PT-410`'s crashes.**

**Gate diffed against the session baseline after every edit batch. Zero new findings at every step.**

**⚠ Both PATs were pasted into chat again and are compromised. Third exposure on this project. Revoke and reissue with Contents read/write; the old one carried admin.**
