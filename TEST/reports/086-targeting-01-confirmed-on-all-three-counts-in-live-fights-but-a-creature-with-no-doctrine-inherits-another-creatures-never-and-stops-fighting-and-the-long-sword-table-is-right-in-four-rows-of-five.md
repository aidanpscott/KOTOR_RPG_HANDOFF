# TEST 086 — TARGETING-01 confirmed on all three counts in live fights:
# adjacency beat a preference at range, a Never held absolutely and said
# `none:all-excluded`, and round memory flipped the target mid-fight,
# overriding a standing preference by exactly the predicted margin.
# ⚠ But a creature that names NO doctrine inherits the first authored one
# in the area — INCLUDING its Never — and stops fighting altogether.
# Separately: the final Long Sword table is right in four rows of five.

## Build state

    Loom            HEAD 0e5d82f  pin to the engine carrying the round memory
    KOTOR-RPG-APP   HEAD 94c4746  the fight feeds the round memory
                                  -- TARGETING-01 slice 2, reachable
    lodestar        20f9c595 — recorded and resolved agree, both repos

Both trees clean, no drift. `check_shelf.py`: `✓ 25 rules files, all
identical to what the extracts generate` — the gate for the weapon half.
All app PIDs killed by PID, confirmed gone.

**I read `targeting.dart` before testing**, so the scenarios below are
built against the actual score rows rather than guessed at:

    adjacent (≤1)                    +4        preference (any, once)   +2
    within your own movement          +2        damaged you              +3
    beyond                             0        attacked them last round −3
    tiebreak 1 · the nearer                     closed on you            +2

---

# 1 · TARGETING-01 — three live scenarios

**Fixture:** a purpose-built `targeting-probe` package — three areas, five
creatures, four doctrines, hand-written. Coder's brief said *"author or
find a doctrine"*, so this is sanctioned instrumentation; it is declared in
full under **State** and left on disk as a re-usable TARGETING-01 fixture.

### ✓ (a) Adjacency beats a preference at range

`foe-prefer` carries a doctrine preferring the companion by handle. The
player stood **adjacent**; the companion `mate` was pinned four squares off
with the sidebar's own **Wait here**.

    player   adjacent            4
    mate     within movement 2 + preference 2 = 4   → tie

On the opening round, with mate still at (4,0):

> `foe-prefer.adjacency.01: unarmed · rolled 21 — d20 20 + attack 1 ·
> **needed 15** — hit · damage 3 · 9 left`

**`needed 15` is the player's defence** (base 10 + Dex 2 + class 3);
everything else in these fixtures is 13. So the foe took the man in its
face and **did not walk past him to chase its preference** — the tie
resolved on tiebreak 1, *the nearer*, exactly as `§3.5` describes.

**And the converse held on the next round**, which is the better half of
the evidence: once `mate` closed to adjacent it scored 4 + 2 = 6 against
the player's 4, and the foe switched to it (`needed 13`). The preference
loses at range and wins at equal range — the score is tracking distance
round to round, not applying a fixed rule.

### ✓ (b) A Never exclusion holds absolutely — and says which kind of nothing

`foe-never` carries `[[never]] match = { role = "player" }`. I put it in a
room where **the player was the only possible target** — no companion at
all — so the exclusion had nowhere to hide:

> `foe-never.never.02 **holds — none:all-excluded**`

It refused to act rather than attacking an excluded target, and named the
*kind* of nothing, which is precisely what `DOCTRINE-FORMAT-01 §2`
specifies: *"the hull is not chosen even when it is the only thing left —
and `none:all-excluded` is a decision that says which kind."* Held for
**seventeen consecutive rounds**; the player finished untouched at 12/12.

### ⚠⚠ But an un-doctrined creature inherits that Never and stops fighting

In the same room stood `foe-plain`, which named **no doctrine at all**. It
never attacked either. Seventeen rounds, player at 12 of 12, both foes at
60 of 60.

**A/B, run twice, changing one line:**

| `foe-plain` | result over the fight |
|---|---|
| **no doctrine** | never attacked · player **12 of 12** after 17 rounds |
| **its own `plain-aggro`** (no exclusions) | attacked normally · player **12 → 1 of 12** in 6 rounds |

The cause is in `play_screen.dart`'s `_loadDoctrine`, and the code states
it plainly:

```dart
_doctrines[p.placement.tag] = d;
// ⚠ THE FIRST ONE IS STILL THE FALLBACK, so a creature that names none
// fights by a doctrine an author actually wrote rather than by
// scaffolding — which is what this screen did for every enemy before.
_doctrine ??= d;
```

with `doctrineFor(handle) => doctrines[handle] ?? doctrine`.

**So the per-creature lookup is correct** — a creature that names a
doctrine gets its own, which is what Coder asked me to confirm and it
holds. The problem is the fallback: the first authored doctrine loaded in
an area becomes the default for **every** creature that names none, and it
is inherited **whole, exclusions included**.

**Why I think this is worth a ruling rather than a shrug.** The fallback's
stated reason — *fight by something an author wrote rather than by
scaffolding* — is reasonable **for preferences**. It is the opposite of
reasonable for exclusions, and `DOCTRINE-FORMAT-01 §2` is emphatic about
exactly this distinction: ***"never is not a preference that lost."***
Exclusions get their own section precisely because they are a different
kind of thing, and the format goes out of its way to make an author unable
to confuse them. The fallback then confuses them anyway, at load time.

The practical effect is severe and silent: **an author who gives one
creature a Never exclusion disarms every un-doctrined creature in the same
area.** Nothing says so — no Verify problem, no message in play. The only
symptom is enemies standing still, and `holds — none:all-excluded` is
printed for the creature that *legitimately* holds, so the fallback
victims are invisible even in the status line.

*Suggestion, offered as one: inherit `[[prefer]]` from the fallback and
never `[[never]]` — an exclusion is a statement about one creature.*

### ✓ (c) Round memory visibly changes who an enemy goes after

`foe-mem` prefers the companion. All three adjacent, so:

    mate    adjacent 4 + preference 2 = 6
    player  adjacent 4                = 4

**Baseline — every round, no damage from me:** `needed 13` · mate takes
the blows · foe-mem untouched at 60 of 60 · player 12 of 12.

**Then I landed one blow** on my turn (last in initiative):
`rolled 22 … hit · damage 7 · 53 left`.

**Its very next action:**

> `foe-mem.memory.02: unarmed · rolled 16 — d20 15 + attack 1 ·
> **needed 15** — hit · damage 3 · **9 left**`

The player went 12 → 9; mate stayed at 57. **It switched off its preferred
target onto whoever had just hurt it** — player 4 + 3 = 7 against mate's
6, which is the predicted margin exactly.

**⚠ My first attempt at this was inconclusive and I am naming why**, since
it would otherwise have read as a defect: the companion was also attacking
`foe-mem`, so it earned the *same* +3 and stayed ahead at 4 + 2 + 3 = 9.
The fixture, not the product, was at fault. I gave the companion a
doctrine excluding every foe so it would hold and land nothing, and only
then did the test isolate the variable.

---

## ⚠ Also found — a companion told to hold position still advances in combat

In scenario (a) I used the sidebar's **Wait here**. It reported
*"Mate will wait here"* and the row read **holding position**. Mate stayed
put through the opening round — but on its next combat turn it advanced
**two squares** to engage, while the sidebar still said *holding position*.

`fight.dart` never consults the standing order: `party_sidebar.dart:543`
renders `holding` from the `held` map, and `fight.dart`'s own `waiting`
set is a different thing (`PT-1686`'s *arrived this round, acts the next*,
and its comment says so). So the order governs exploration and not combat.

That may well be intended — *hold position* plausibly means *don't trail
me between rooms*. What makes it read as broken is that **the label stays
on screen during the fight while the companion walks off the square**. It
also materially interfered with this test, which is why I am raising it.

---

# 2 · THE FINAL LONG SWORD TABLE — four rows of five

**This supersedes TEST 085**, which checked the earlier 1d8 / 1d12 version.
That report's values are now stale and its "two things called Long Sword
roll different dice" observation is **resolved** — the base type and both
catalogue rows now agree at 1d6.

| Coder's table | shelf | |
|---|---|---|
| Long Sword, both games: **1d6, no bonus** | base type `1d6`; `g_w_lngswrd01` and `w_melee_02` both `1d6, 20–20 ×2` | ✓ |
| Krath War Blade: **1d6+2 physical** | **`1d6 + 1`**, `properties = "Enhancement 1"` | ✗ |
| Trandoshan Sword: **1d6+4 slashing** | `1d6 + 4 slashing` | ✓ |
| Naga Sadow's: **1d6+2+2d6**, **10,000** | `1d6 + 2 + 2d6`, cost `10000` | ✓ |
| Shyarn: **1d6+5 slashing+2d6**, **24,000** | `1d6 + 5 slashing + 2d6`, cost `24000` | ✓ |

**Krath War Blade is the one that disagrees**, in both the number and the
type: the message says *+2 physical*, the shelf says *+1* with no damage
type named. I traced it rather than just reporting the mismatch — the
source document `MAIN_WORK/rules/ITEMS-02.md:259` reads:

    | **Krath War Blade** | `g_w_lngswrd02` | K1 | 1 | 150 |
    | 1d6 + 1, 20–20 ×2 | Fully Upgradeable | Enhancement 1 |

and `extract_items.py` says of itself *"This copies the cells across and
changes no value."* `check_shelf` is green. **So the whole chain is
self-consistent at +1** — document, extract and installed shelf agree. The
disagreement is between Coder's message and the document. Either the
message mis-stated it, or an intended edit to `ITEMS-02.md` did not land;
I cannot tell which from here, and am not guessing.

**Naga Sadow's poison survives** — `properties` carries
`OnHit (ItemPoison) 10`. ⚠ It has **no `[[items.effects]]` block**, so the
poison is catalogue text and not a modelled effect. Same shape as TEST
084's grenades; naming it, not filing it.

### ⚠ The prices are correct and nothing displays them

10,000 and 24,000 are both right in the data. **Scoped negative, and here
is where I looked:** I grepped `KOTOR-RPG-APP/lib/` and `Loom/lib/` for
any read of an item's `cost`. The only hits are chargen's flat 100
starting credits, a dialogue `[Bribe · N credits]` gate, and a Force
power's `cost` at `play_screen.dart:7218`. **There is no store, merchant
or item-price surface anywhere**, so *"confirm the new prices show
correctly wherever they're displayed"* has the answer: correct in the
data, displayed nowhere yet.

---

## What I did not do

- **Did not test the −3 `attacked them last round` row.** It is suppressed
  against anyone adjacent (*"you do not drift off the man in your face"*),
  and every scenario that isolates it needs a ranged attacker the player
  does not have.
- **Did not test `closed on you`** for the same reason — the player cannot
  damage at range, so a closing scenario cannot be separated from the
  adjacency band.
- **Did not exercise the two rows `whatIsNotScoredYet` names** (Force heat,
  Guarding Stance / Interpose / Bulwark) — the module names them as
  unsuppliable, which I take at its word.
- **Did not re-test** the extension rename or grenade saves (TEST 084);
  nothing this session touched them.

## State

- **New package `targeting-probe` is mine and left on disk** — three
  areas, five creatures, four doctrines. It is a working TARGETING-01
  fixture and may be worth keeping. Its `[entry]` has been restored to
  `a01-adjacency`; I repointed it to a02 and a03 during the run to reach
  each scenario without fighting through the others.
- ⚠ **Mid-run fixture edits, declared:** `foe-plain` and `mate` gained
  doctrine attachments during testing (the A/B above, and the passive
  companion for (c)); a02's companion was removed to isolate the Never.
  Those edits are still in the files, which is why the fixture now reads
  as it does.
- ⚠ **A fixture artefact, mine not the product's:** I reused one `mate`
  blueprint across areas, so entering a second area adds a second Mate to
  the party. Cosmetic, and only visible in my package.
- `strongroom-rebuilt`, `locked-and-trapped` and `tester-strongroom`
  untouched.
- Several saves in `targeting-probe`, not cleaned up.
- All app PIDs killed by PID, confirmed gone.
