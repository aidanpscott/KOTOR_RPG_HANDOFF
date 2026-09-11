# STUDY — how the source games are put together

**Purpose.** A structural map of KOTOR 1, KOTOR 2 and NWN's Aurora toolset, produced across seven batches, in a shape that **composes**. Not to build an exporter — that was ruled a hope and declined at `PT-1269`. **To learn from the design before we commit to our own format.**

**⚠ The output format matters more than the batching.** Seven runs of prose produce seven essays. Seven runs of *identical records* produce one map. **Use the template below without deviation**, even where a field feels redundant for a given type.

---

## The seven batches

| # | Folder | Covers |
|---|---|---|
| 1 | `01-container` | packaging and lookup — BIF/KEY, ERF/RIM/MOD, Override precedence, load order |
| 2 | `02-definition` | the rules layer — 2DA tables, the TLK string table |
| 3 | `03-blueprint` | reusable object templates — UTC, UTI, UTP, UTD, UTT, UTM, UTS, UTW |
| 4 | `04-world` | modules and areas — IFO, ARE, GIT, and how they bind |
| 5 | `05-behaviour` | scripts and conversation — NSS/NCS, DLG |
| 6 | `06-presentation` | audio, music, movies, cutscene authoring, and the model layer **as far as animation and cutscene staging reach** |
| 7 | `07-toolset` | **Aurora ↔ NWN** — how the toolset hands a module to the game |

**Both KOTOR games in every batch.** Differences are recorded on the record itself, never as a separate pass — comparing from memory across runs is how divergences get missed.

**NWN is scoped to batch 7 only**, except where a KOTOR structure is obviously inherited and the ancestor explains it.

---

## ⚠ Everything after the seven — and this index went SIXTEEN STUDIES STALE

**The seven above were the original plan. Sixteen more landed and none were
listed here.** `STUDY 24` was re-briefed as unstarted work **because it was in
git and not in this file** — the front door stopped at 7.

⚠ **`STATE.md`'s own shape, in my own directory**: *a thing neither built nor
tracked is the one that gets forgotten.* **Anything added to `STUDY/` is added
to this table in the same commit.**

| # | Folder | Covers |
|---|---|---|
| 8 | `08-census` | census of the source data |
| 9 | `09-dialogue-options` | dialogue options, as counted |
| 10 | `10-stack` | the resolution stack |
| 11 | `11-spike` | a spike |
| 12 | `12-toolset-ui` | **Aurora's toolset UI** — the conversation tree is a plain `TreeView`; *Paste As Link* expresses a DAG |
| 14 | `14-toolset-flow` | Aurora's flow, launch to a placed creature — **the editor is a TAB, master over detail** |
| 15 | `15-blocks` | **Daggerfall's** prefab and block system |
| 16 | `16-tree` | Aurora's module tree — found `characters` at top level where it belonged under Blueprints |
| 17 | `17-editors` | which editors Aurora has and which we need — **three editing surfaces, 32 context verbs** |
| 18 | `18-dialogue-compare` | the three dialogue systems, and whether theirs imports into ours |
| 19 | `19-input-and-combat` | **input and combat across K1/K2/NWN/BG3.** `actions.2da` is 3 columns; `surfacemat` prices nothing; `keymap.2da` is 4 columns in NWN and 22 in K1 |
| 20 | `20-bg3-observed` | BG3's combat presentation from the UI layer — **and the record of why BG3 cannot be run here.** ⚠ its `§3` world-space question is **CLOSED WITH NO ROUTE** |
| 21 | `21-bg3-hotbar-and-ceremony` | the hotbar, the partial-move dial, the dice ceremony, the two log surfaces |
| 22 | `22-keyboard-bar-and-wording` | **`PT-1517` verified** — folder = state, filename = identity; the written cost; `<LSTag>` answers `§4c` |
| 23 | `23-dying-and-what-remains` | **KOTOR has no dying band**; a corpse is the creature itself; `NoPermDeath` is literally the party rule |
| 24 | `24-one-file-deeper` | **`k_ai_master` does nothing about the body** (`PT-1525`); the GIT half closed; **the BG3 combat-log grammar** |
| 25 | `25-the-three-classes-and-the-defence` | **Marksman and Engineer BAB found** in `CLASS-TABLES-DROID` (= K1's `CombatDroid`/`ExpertDroid`); **only the Saboteur is truly absent**; BAB is binary and `Rate` does not give it; **Defence has one data point and no second** |
| 26 | `26-the-defence-ladder-in-the-games` | **the games DO have a class Defence ladder** — `classes.2da.armorclasscolumn` → `acbonus.2da`. ⚠ K2 flattened attack and **kept** defence. K1 2 tracks, K2 6. **All values EVEN, so RCR's `+1` offset is unrepresentable.** ⚠ RCR gives the Soldier the best ladder; K1 gives it **zero** |
| 27 | `27-perception-range` | ⚠ **NOT a third negative** — `.utc PerceptionRange` indexes `ranges.2da`, which carries **sight AND hearing in metres**. Default 20/20; 97.8% of 4,397 creatures use it. **Droids and organics indistinguishable.** NWN's blank default is the row KOTOR runs on; player sight 35 m → **250 m** |
| 28 | `28-examples-that-cannot-parse` | **`PT-1575`'s document half** — 43 worked examples parsed, **3 defects**: `AUTHORED-CHARACTER-01:86` (`;` as separator, the one Tester copied) and `PACKAGE-FORMAT-01:132,463` (bare `⚠` with no `#`). ⚠ **Two are the house style working as designed, in the wrong place** |
| 29 | `29-the-diagonal-was-already-ruled.md` | ⚠ **the diagonal COST is already ruled** — `PLAYTEST-RULINGS-01:238`, *"diagonal costs 1 square"*, the same sentence `PT-1581` took its reach half from. **`AREA-FORMAT-01:464` asserts a corpus silence that is not there**, and the runtime's Chebyshev already implements the ruling. ⚠ **RCR is not on this machine** |
| 30 | `30-a-ruling-with-no-number.md` | the unnumbered diagonal ruling is **one case, not a class**. ⚠ **Nine ids carry two headings, six live** (`PT-368` was my false positive — the suffix is part of the id). ⚠⚠ **Four of the six are ONE event** — `# Added after S6` appears twice. `PT-484` is the near miss: its citations rely on the second heading and the unmarked first is narrower |
| 31 | `31-how-enemies-enter-combat.md` | ⚠ combat start is **perception-driven at 20 m, not contact**, with a reaction delay of `distance/10` s. ⚠⚠ **There is NO combat roster** — `GetIsInCombat` is per-creature and nothing returns the set. **Visibility IS membership** (`PERCEPTION_SEEN` in the disengage test). ⚠⚠ **KOTOR's HUD has ONE enemy: `LBL_NAME` + `PB_HEALTH`. No enemy list exists** |
| 32 | `32-does-bg3-need-a-roster.md` | ⚠⚠ **BG3 DOES have a roster** — `Combat.Participants`, `CurrentCombat`, `BringIntoCombat`, and *"Flee failed: not in combat"*. **The panel binds to the roster, not to visibility** — an enemy out of sight stays listed. ⚠ **Opposite shape to KOTOR on all four questions**, and turn order is why |

*(There is no batch 13.)* **`_reference/`** holds our own design documents for comparison — not a batch.

### ⚠ Tools live with the study that needed them

`19-input-and-combat/tools/` — `keybif.py` (chitin.key/BIF, **written because it
did not exist**), `d2.py` (2DA V2.b *and* V2.0 text), `lspk.py` + `lz4block.py`
(BG3 LSPK v18, stdlib only, nothing installed).
`22-keyboard-bar-and-wording/tools/loca.py` (Larian `.loca`, 232,878 strings).

---

## The record — one per resource type, every field, every time

```
## <EXT> — <plain-language name>

WHAT IT IS          one sentence, no jargon

CONTAINER           which archive type holds it, and where it is found

STRUCTURE           top-level shape. GFF struct? table? binary? text?
                    the fields that carry meaning — not an exhaustive dump

REFERENCES OUT      what this points AT, and BY WHAT MECHANISM
                    resref string / row index / numeric id / filename
                    ⚠ the mechanism matters more than the target

REFERENCED BY       what points at THIS, same detail

SCOPE               module-local, game-global, or campaign-level
                    ⚠ call this out explicitly — it is where KOTOR hurts

AUTHORED BY         a human in a tool? generated? hand-edited 2DA?

READ WHEN           load time, area transition, on demand, every frame

K1 vs K2            differences, or "none found"

SAMPLES             3-5 real instances, named, chosen for SPREAD:
                    one minimal, one complex, one oddity
                    give the file and module each came from

UNKNOWN             what you could not determine, and what it would take
```

**⚠ Description only. No critique in these records.** Facts and judgements in one document make the facts harder to trust later. Flaws go in a separate catalogue — see below.

---

## Two further deliverables

**`FLAWS.md`** — a catalogue of design problems, **each citing the record it follows from**. The one already known: the TLK is a single game-wide string table, and the journal is a single game-wide `.jrl`. Both make two mods collide by construction. Look for others of that shape — anything global that had no reason to be.

**`NAMING.md`** — a table: *KOTOR's name · what it actually is · a clearer name.* `UTC` means "creature blueprint"; `GIT` means "everything placed in this area". This becomes the vocabulary for our own format, and eventually the map an importer would use.

---

## Rules for every batch

**Read, do not infer.** Open files. A structure guessed from a filename is not a finding. Where something is inferred rather than read, **say so on the record**.

**Scope every negative.** *"No reference found"* is only useful with *"searched X, Y, Z."*

**Say what you did not check.** An honest gap is worth more than a confident guess, and this project has been bitten by wrong-shape negatives repeatedly.

**Commit each batch to its folder before starting the next.** Partial work in the repository beats complete work lost.
