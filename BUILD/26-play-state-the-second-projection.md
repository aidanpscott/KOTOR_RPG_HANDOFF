# 26 · PLAY-STATE-01 — the second projection

`PLAY-STATE-01` is built. **198 app tests · 194 Lodestar · 101 Loom.** All three
analyze clean.

---

## 1 · It is not one more record

`§1`'s own heading is the design, and the code follows it literally:

| | what it is | where it lives |
|---|---|---|
| `CharacterRecord` | what a character IS | a fold over the log |
| `PlayState` | what is TRUE RIGHT NOW | **a second fold over the same log** |
| the log | what happened | the only thing that persists |

`projectPlayState()` sits beside `replay()` in Lodestar. It reads the same
`List<CharacterEvent>`; there is no second store, no snapshot, and no
play-state file. `PT-1327` withdrew compaction and nothing here reintroduces
a cache.

---

## 2 · ⚠ The lifetime question, answered first — and no new event kind

`character.damaged` and `character.healed` are **`transient` — until the
encounter ends**. `§2` gives lifetimes their new job: *"they decide what is
written in the first place."* **So the blows are never in the log to fold.**

What survives is the **outcome**, written on `encounter.ended` —

- already declared in `EVENT-KINDS-01`,
- already `campaign`,
- and `§6` leaves every payload deliberately unspecified.

Payload: `subject`, `encounter`, `vitality` (and `force` / `force_ceiling`
when a Force pool exists). **No new event kind was required, so none is
proposed.**

### ⚠ It REFINES `ENGINE-SPEC-04 §4`; it does not contradict it

The owner's reading is right. `§4`'s not-written list is about the **round** —
hit, miss, whose turn it is, position inside a fight — and **every one of those
is still not written.** Leaving an area still calls `Fight.abandon()`; turn
order, movement left and spent reactions are all lost, exactly as `§4` says.

What is written is *where the fight left you*, which is the same category as
`§4`'s own written column — *who died, what was destroyed, what the party
took.* **A fight is not a fact; its outcome is.**

---

## 3 · The exploit closes as a consequence

Nothing in the code says *"fights persist."* The sequence is unchanged:

1. entering an area rebuilds every creature **from the blueprint, whole**;
2. then the log is folded over each one.

Walk out at 3 vitality, walk back, and the trooper is at 3 — because there was
never a stored *"fresh trooper's current vitality"* to reset to.

**⚠ And the real hole was walking out MID-fight.** `Fight.abandon()` wrote
nothing, so an abandoned fight lost the wound with the round. `_enter` now
writes the outcome before it opens the next area. The round is still
abandoned; the wound is not.

`test/wound_survives_test.dart` drives it through the screen: fight the
trooper, walk through the door at `[7,2]`, come back through `[2,3]`, and the
screen still explains the wound. **It opens with a control** — a fresh area
explains nothing — so it cannot pass because the line always shows.

---

## 4 · `§5` show the working

`PoolState.working` carries the sentences, and `PoolState.line` reads
`12 of 25 — encounter a01-command-deck left you at 12`. It is **the same rule
as `resolve`'s derivation**, not a second one: a derived value names its
sources.

On screen it is a HUD line that appears **only when someone has something to
explain** — in a fight, or when a wound has outlived its encounter. A
full-health creature standing in a quiet room says nothing.

---

## 5 · `§3b` — does the field set force a visibility decision now?

**No, and the shape is already right.** `PT-1330` puts **everything in `§3`**
in the shared column — pools, conditions, position, alignment, faction. The
private column holds Personal Notes, last-open panel and settings, **none of
which is in `§3`.** So a per-player field on this projection would have nothing
to hold.

**The one thing to keep true is on the EVENT, not the projection.**
`ENGINE-SPEC-01`'s visibility set marks what **the table** can see — the gap is
table-vs-engine, not player-vs-player. `CharacterEvent` has no such field yet.
Adding one later is a **payload change**, not a reshaping of the projection,
because the fold already keys on `subject` and reads payloads it does not own.
**Flagged, not built.**

---

## 6 · ⚠ What is in `§3` and deliberately NOT projected — named, not silently empty

`PlayState.notProjected` carries both, in words, at runtime:

- **Conditions.** `§3` gives them five fields including `exposed` and
  `survives_load`. **Nothing emits `character.condition-applied`**, so an empty
  list would read as *"no conditions"* rather than *"nothing has ever applied
  one."*
- **Alignment.** `§6` closed it at `PT-1279`, **but the derivation is not
  pure**: `§1.2`'s directional hysteresis makes the prior band an input, so the
  band is a fold, not a lookup. `ALIGNMENT-01-v2` explicitly warns that a
  symmetric deadband **silently disables mastery gain by drift** and produces
  zero band flips that look like success. Nothing emits
  `character.alignment-shifted`. **Building it now would be building the trap
  the document names, with no caller.**

Faction and position DO fold — `character.faction-changed` and
`character.moved` are both `campaign`, and `PT-1417` moved the latter up for
exactly this reason.

---

## 7 · Not built

Multiplayer. Snapshots. Compaction triggers (`§6` leaves *when* unspecified).
An action queue — `§4` says if the design ever grows one, something has gone
wrong.

**And one gap to name:** the play log lives in the play screen for the
session. Nothing appends it to the save. That needs a ruling that is not mine —
**whether play events join the character's log or a campaign log** — and
`SAVE-LOAD-01` says *"the save is the log"* without saying which log an
`encounter.ended` belongs to when three characters were in the fight.
