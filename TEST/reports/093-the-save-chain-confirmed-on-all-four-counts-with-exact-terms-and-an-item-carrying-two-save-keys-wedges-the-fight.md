# TEST 093 — THE SAVE CHAIN IS RIGHT ON ALL FOUR COUNTS, and every term is
# visible on the line. A level-1 Soldier rolled `fortitude 2`, a level-20 one
# `fortitude 12` — the ten points that did not exist before. The two
# interpolation holes both answered with real numbers: L22 → 13, L27 → 15.
# The fold is asymmetric exactly as ruled: two penalties SUMMED to `− gear 6`,
# a `+2` and a `+4` took the HIGHEST at `+ gear 4`, and the two together came
# out `− gear 1`. An `all` item reached a Fortitude roll and did not double
# with a specific one.
# ⚠⚠ AND ONE FINDING: a creature wearing an item that states TWO save keys
# (`all` and a named save) WEDGES THE FIGHT — the round never advances past
# the creature before the player. Reproduced on two fresh runs and bisected to
# one variable. The item is mine, not shipped, so it is latent — but the format
# permits it and the engine has a branch for it.

## Build state

    Loom            HEAD 53e7f29  (not launched this session)
    KOTOR-RPG-APP   HEAD c1954dc  — and this is what I built from
    lodestar        ed899604 — lock and the pub-cache checkout agree, both repos

Both trees clean at start and end, and HEAD did not move under me this time.
`check_shelf.py` green at both ends: `✓ 26 rules files and 65 standard
blueprints`.

⚠ **Bundles stale again — sixth session.** Loom's blob is still from the 13th;
the app's was `2026-09-15 12:48` against a HEAD of `14:57`. Rebuilt the app's
Dart side with `flutter assemble … debug_bundle_linux-x64_assets`, ran from a
private copy, left both shared bundles byte-for-byte as I found them.

⚠ **I did not launch Loom**, so the worn items are hand-transcribed from their
catalogue rows into the blueprint format (`[item.saves]` with `fortitude = -2`,
or `all`), as in TEST 092. What is under test is the app reading them.

*(Routing note: the brief's PT numbers do not match the log. The commits are
`4a8934c` "save, step 1: savesAt interpolates" and `2716fa2` "save, step 5: the
save is the target's own, at both roll sites". Also `6146a9e PT-2160: the
spring consults resistance and immunity, as the boundary always did` — that is
TEST 092's finding, closed.)*

---

## The instrument, and why this roll site

There are two save roll sites — the on-hit seam (`attack.dart:1238`) and the
hazard spring (`play_screen.dart:825`). **I exercised the on-hit one**, because
it rolls the save of a *creature*, and a creature can be any level and wear
anything; the hazard rolls the player's, and the player is level 1 out of
chargen with no way to reach 22. Both now call one function — `saveCheckFor`
→ `saveCheck` — which exists, in its own words, *"so the two roll sites cannot
drift"* after `PT-2035` and `PT-2160` each had to reconcile them.

The weapon is **Naga Sadow's Poison Blade**, whose on-hit effect now carries
`kind = "fortitude"`. **The kind is what routes the roll**: `saveKindOf(null)`
returns null and the check falls back to the bare `d20` it always was, so an
effect with no save kind still rolls untrained. Twenty-one catalogue effects
carry a save — nineteen fortitude, one reflex, one will.

Nine Soldier targets on a firing line, unarmed, `never-player`, 900 vitality.

# 1 · THE MODIFIERS ARE THERE, AND THEY ARE THE TARGET'S OWN

> `poison — d20 14 + **fortitude 2** + **Constitution 2** = 18 vs 10 · resisted`

| target | level | Con | the terms on the line |
|---|---|---|---|
| `s-l1` | 1 | 14 | `fortitude 2` + `Constitution 2` |
| `s-l20` | 20 | 14 | **`fortitude 12`** + `Constitution 2` *(twice)* |
| `s-con20` | 1 | **20** | `fortitude 2` + **`Constitution 5`** |

**A level-20 Soldier rolls ten points better than a fresh one**, which is the
whole of the fix — before it both rolled a bare `d20`. And the ability half
moves independently: same class, same level, Con 20 instead of 14, and the term
goes from `2` to `5`.

The derivation prints in full, so the number can be checked rather than
believed: `d20 14 + fortitude 12 + Constitution 2 = 28`.

# 2 · BOTH INTERPOLATION HOLES ANSWER WITH REAL NUMBERS

The shelf's Soldier ladder lists **L1 … L20, then 25 and 30 only**:

    L1  fort 2      L20 fort 12     L25 fort 14     L30 fort 17
                    L21-24 ABSENT   L26-29 ABSENT

| target | level | reading | between |
|---|---|---|---|
| `s-l22` | 22 | **`fortitude 13`** *(twice)* | 12 and 14 ✓ |
| `s-l27` | 27 | **`fortitude 15`** | 14 and 17 ✓ |

So the progression reads `2 → 12 → 13 → (14) → 15 → (17)` — monotonic, no
reversion, and nothing missing where the document is silent. Under the old
clamp these two levels returned `null` and the sheet printed `—`.

# 3 · THE FOLD IS ASYMMETRIC, AND BOTH HALVES SHOW

| target | wears | the line says | |
|---|---|---|---|
| `s-pen` | fortitude **−2** and fortitude **−4** | **`− gear 6`** | the penalties **SUM** |
| `s-bonus` | fortitude **+2** and all **+4** | **`+ gear 4`** | the bonuses take the **HIGHEST** |
| `s-mixed` | all **+4** and fortitude **−5** | **`− gear 1`** | best `4` **plus** penalties `−5` |

`− gear 6` is the one that settles it: two items, `−2` and `−4`, and the result
is `−6` rather than the `−4` a symmetric fold would give. And `s-mixed` shows
both rules acting at once in a single number.

Full line, for the arithmetic:
> `poison — d20 1 + fortitude 2 + Constitution 2 − gear 6 = -1 vs 10 · takes hold`

# 4 · `all` EXPANDS, AND DOES NOT DOUBLE WITH A SPECIFIC ONE

`s-bonus` wears the **Adrenaline Stimulator** (`all = 4`) and the
**Cardio-Regulator** (`fortitude = 2`). The roll was a **Fortitude** save, and:

- the `all` item reached it at all — so `all` is expanded to each of the three
  rather than folded as a fourth key;
- the line reads **`+ gear 4`**, not `+6` — the specific `+2` did not add to it.

**Highest wins for that specific save**, which is the fourth ask exactly.

---

# ⚠⚠ THE FINDING — an item stating TWO save keys wedges the fight

`_saveTable` gathers `all` and a named save per kind before folding, and its own
comment says why that branch has never run:

> *"**No catalogue item states two save effects at all today, counted**, so this
> branch is unexercised by shipped data — it is here because the format permits
> what the data has not yet used."*

I wrote the smallest item that exercises it — one blueprint, `all = 2` and
`fortitude = 5` — and put it on one of nine creatures.

**The fight stops.** After the player ends their turn the round never comes
back: the turn marker sits on the creature immediately before the player and
stays there. I watched it for thirty seconds, clicked the board, pressed space
again — nothing. The process is alive and rendering; **nothing is written to
stdout**, so it is not an uncaught throw reaching the console.

### Bisected to one variable

| the fixture | the item on `s-both` | result |
|---|---|---|
| nine creatures | `all = 2` **and** `fortitude = 5` | **wedges** — run 1 |
| nine creatures | `all = 2` **and** `fortitude = 5` | **wedges** — run 2, fresh app, clean pacing |
| eight creatures *(that one removed)* | — | runs |
| **nine creatures** | **`fortitude = 5` only** | **runs** — four consecutive rounds completed |

The last two rows are the ones that matter: **same nine creatures, same
creature, same slot — only the item's second key differs.** With one key the
rounds complete and print `s-pen.probe.06 holds — none:all-excluded` each time;
with two they never come back.

**⚠ The item is mine, not shipped**, so nothing in the game triggers this today
— which is exactly what the source comment predicts. But the blueprint format
permits two keys, the engine has a branch for them, and the failure is a fight
that stops rather than a refusal that says so. Given `PT-1500`'s standing
distinction, an item this reader cannot fold ought to refuse out loud.

---

## ⚠ Also found — six of the twelve `Lower Saves` bands are mislabelled

The brief names `g_i_frarmbnds16-21` as the items to test with. **Six of the
twelve bands have a name that contradicts their own property and effect:**

| name | property | effect |
|---|---|---|
| Lower Saves, **Reflex** 2 / 4 / 5 | `(Will)` | `will` |
| Lower Saves, **Will** 2 / 4 / 5 | `(Reflex)` | `reflex` |
| Lower Saves, All 2 / 4 / 5 | `(All)` | `all` ✓ |
| Lower Saves, Fortitude 2 / 4 / 5 | `(Fortitude)` | `fortitude` ✓ |

The Reflex and Will pairs are **swapped**. The engine follows the property,
which is the mechanical field and the right choice; it is the *name* that
disagrees. These are developer items in the source, so the crossing may well be
original — I cannot tell from here which is authoritative, and I am not
guessing. But an author who picks "Lower Saves, Reflex 4" out of the palette
gets a Will penalty, and `16-21` is precisely the range the brief points at.

**I used the Fortitude (`13-15`) and All (`10-12`) bands instead**, because
Naga Sadow's save is Fortitude and those four sets are internally consistent.

## Method, and what was mine

- ⚠ **I lowered the high-level targets' Dexterity to 3.** A level-20 Soldier's
  class Defence made every swing `needed 22`, and five in a row missed. Fortitude
  is Constitution-based, so this does not touch any number reported above — it
  only made them reachable.
- ⚠ **My first run's pacing pressed keys during AI turns**, and I considered
  that as the cause of the stall. It is not: the stall reproduced on a fresh app
  with deliberate waits, and the bisect isolates the item with everything else
  held still.

## What I did not do

- **Did not exercise the hazard roll site.** It is the same `saveCheck` through
  the same `saveCheckFor`, and the player cannot be levelled past 1, so the
  interesting half of this routing is not reachable there.
- **Did not test Reflex or Will saves.** Only two of the twenty-one catalogue
  effects carry a non-fortitude kind (`Poison Grenade`, reflex; `Concussion
  Grenade`, will), and neither is a weapon on-hit.
- **Did not test the other eleven affected classes** — Soldier is the one the
  brief confirms and the one whose ladder I read.
- **Nothing on conditions**, as instructed — though `ed22bc7 conditions: a flash
  mine stuns you — the first real producer` has landed since the brief was
  written, so that may be testable sooner than the note suggests.

## State

- **New package `save-probe` is mine and left on disk**, deliberately **in the
  state that reproduces the stall** — `items/misc/both-on-one.toml` carries both
  keys again, and its comment says what removing the `all` line does. Nine
  creatures, one area, seven worn-item blueprints, one weapon.
- ⚠ `items/weapons/blaster-rifle.toml` and `short-sword.toml` are Naga Sadow's
  Poison Blade, at the path chargen equips. Declared so nobody reads them as
  mis-authored.
- ⚠ The worn items are hand-transcribed from their catalogue rows; Loom was not
  launched.
- ⚠ My `flutter assemble` output sits in the app repo's `build/` and in my
  scratchpad — gitignored, regenerable, shadowing neither desktop bundle.
- Saves from four runs, not cleaned up.
- App PIDs `173456`, `174281`, `174915` and the two later ones all killed by
  PID, all confirmed gone. No Loom launched; nothing of Coder's touched.
