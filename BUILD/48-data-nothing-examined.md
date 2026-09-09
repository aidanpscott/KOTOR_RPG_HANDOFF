# 48 · Data nothing examined — the sweep, and two corrections

**637 green.** `MAIN_WORK a46f6e9`. **Three of four extracts re-run; `feats` is
a stop.** And the sweep found the class, with one instance that matters.

---

## 1 · ⚠⚠ THE CLASS — data nothing examined

**Twice in two slices the answer was authored, shipped, and read by nothing.**
`droid_arrays.toml` and then `section`. **So I swept every shipped rules file
against every reader in all four repositories.**

**Two are read by nothing at all:**

| | rows | |
|---|---|---|
| ⚠⚠ **`item_disambiguation`** | **14** | **the one that matters — below** |
| ⚠ **`two_weapon`** | **19** | the per-class two-weapon kit: *"CHOOSE — two Short Swords or a Quarterstaff"* |

**Everything else has a reader.** `classes`, `equipment` and `species` are
loaded by an explicit `File(...)` rather than the `maybe()` helper, which a
first pass missed — **stated because it is the kind of near-miss that makes a
sweep look cleaner than it is.**

### ⚠⚠ `item_disambiguation` is the answer to a blocker I have cited twice

`STATE.md` has said, in my own words, that arming the player is blocked
because *"the arrays name items in prose and only **18 of 41** names resolve to
exactly one catalogue row; **§2c disambiguates 14**."*

> **`item_disambiguation.toml` IS those 14, it ships in `base-rules`, and
> nothing opens it.**

    item = "Blaster Carbine"
    resref = "w_brifle_01"        cost = 35
    other_resref = "g_w_blstrcrbn001"   other_cost = 500

**I sized "arm the player" as blocked on unresolved names — twice — while 14 of
the ambiguities had their answer shipped and unread.** That does not make the
job small, but **it makes my sizing wrong**, and the remaining gap is 41 − 18 −
14 rather than 41 − 18.

### The shape of the class, stated

**It is not a check that examined nothing** — that family was `BUILD 41`'s.
**It is data that nothing examines**, and the two differ in where the silence
is:

- **A check that examined nothing reports success.** You catch it by asking
  what its denominator was.
- **Data nothing examines reports nothing at all.** There is no run, no exit
  code, and no output. **You catch it only by asking, of each shipped file,
  who opens this** — which is why it took two accidents to notice.

---

## 2 · ⚠ My second data claim was wrong, and I read a stale duplicate

**`Plating Proficiency: Light` IS in `FEATS-LIBRARY-01`** — line 80, under
`§3 Organics only`, its own text saying **DROID ONLY**. **The extraction is
faithful and the source row is misfiled.** Corrected.

**⚠ AND THE CAUSE IS WORSE THAN THE ERROR.** There are three copies of that
document:

    HANDOFF/docs/FEATS-LIBRARY-01.md        1434 lines   0 × "Plating"   ← I grepped this
    MAIN_WORK/rules/FEATS-LIBRARY-01.md     1670 lines   3 × "Plating"   ← the real one
    HANDOFF/STUDY/_reference/…              1670 lines   identical to source

**`HANDOFF/docs/` is 236 lines behind.** I grepped the stale copy and concluded
the row was absent from the corpus.

**⚠ This is my third wrong-place negative this session and the SECOND from this
exact cause** — I diagnosed the same two-copies divergence for
`EVENT-KINDS-01` at `BUILD 44` and then walked into it one slice later.

### ⚠⚠ And it is not two documents. It is twenty-three

    23 of 30 duplicated documents have DIVERGED
    PLAYTEST-RULINGS-01   docs 11,781 lines   ·   source 54,233
    SKILLS-01                  538           ·          830
    CLASS-ROSTER-01            889           ·        1,112

**`HANDOFF/docs/` is the copy visible to the owner's token** — that is the
whole reason `HANDOFF` exists — **and it is stale in twenty-three of thirty
documents.** Anyone reading it, me or `Tester` or the owner, is reading an old
corpus.

### ⚠ There is a tool for this, it was built for this, and it reports success

`HANDOFF/sync_docs.py`, whose own docstring is this failure:

> ***`PT-245`. For eight files the designer was reading a version older than
> the rules, and two agents spent three exchanges arguing about a gating figure
> that was correct in the repo and stale in `docs/`.***

**Its paths no longer exist.** It looks for `HANDOFF/handoff/docs` — the real
directory is `HANDOFF/docs` — and for sources at `HANDOFF/*.md`, where the
sources are `MAIN_WORK/rules/` (102 files).

    $ python3 sync_docs.py
      0 file(s) refreshed in docs/
      docs/ matches the working tree          ← rc 0

> **It globs a directory that does not exist, finds nothing, and asserts that
> `docs/` matches.** Fourth instrument of that family this session, **and the
> only one that states a false claim rather than staying silent.**

**Not fixed here.** Repointing it regenerates 23 files in a directory that is
not on my one-writer list, including an 11k→54k line ruling record. **That is
its own slice and it is the obvious next one.**

---

## 3 · Three extracts re-run; `feats` is a stop

**`chassis`, `droid_skills` and `first_level_feats` — all three REAL LAGS**,
content changed in each. `base-rules` regenerated, 637 green.

**⚠ AND RUNNING AN EXTRACTOR BARE WRITES NOTHING, SILENTLY.** Every one guards
its write with `if len(sys.argv) > 1`, so a run with no destination computes
everything, prints its summary, and saves nothing. **I did exactly that first
and the stale flags did not move.**

### ⚠⚠ `feats.json` — two reasons, either sufficient

1. **There is no `extract_feats.py`.** It was extracted ad hoc — *"re-extracted
   at batch 3c"* — exactly as `equipment.json` was before `PT-1452`. **Re-extracting
   requires writing an extractor for 320 records across five sections with
   chains**, and any error corrupts the feat corpus.
2. **⚠ `PT-1462`'s marks were appended to the EFFECTS CELL** of the two rows —
   and that column is extracted into `effect`, **the field the Feats screen
   shows a player.** A naive re-extraction would put *"⚠ `PT-1462` — IN THE
   WRONG SECTION"* into player-facing text. **That is `D3`'s shape**, source-side
   text reaching a player, from the other direction.

> **What is missing: somewhere for a defect annotation to live that is not a
> data cell.** The marks are correct and belong in the document; the extractor
> reads that cell verbatim, and neither is wrong on its own.

**`event_kinds` stays stale, deliberately** — re-stamping silences the only
signal pointing at `emitted_kinds_test` still using `handledByReplay` alone.
