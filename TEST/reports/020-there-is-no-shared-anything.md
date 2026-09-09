# 020 · There is no shared anything, and a flag cannot be set

**From `Tester`. Unrequested number.** `PT-1512` followed: packages and saves
backed up first. **Nothing changed this run** — all packages `diff` **IDENTICAL**
and **no save changed size**.

**Built 18:15 from:**

    Lodestar 2e19964 · Lens 9ca5982 · Loom 7fc9d2d · app da360c7

**Pins honest** — both locks resolve `lodestar` to `2e19964` = `HEAD`. 1280×720.

---

## ⚠⚠ EVERY KIND OF WORLD STATE THERE IS, AND ALL OF IT IS THE CHARACTER'S

You asked about doors, flags and quests because vitality is one kind. **I went
and got the whole list.** `EVENT-KINDS-01`'s vocabulary in `ledger.dart` is:

| kind | lifetime | what it holds |
|---|---|---|
| `encounter.ended` | campaign | **what a fight left behind** — `018`, `019` |
| `character.revived` | campaign | **stood back up at 1** |
| `quest.flag-set` | campaign | **flags** — `flagsFrom` folds them |
| `quest.concluded` | campaign | **quests** — `questsFrom` folds them |
| `character.moved` | campaign | where you are standing (`PT-1417` raised it) |
| `character.faction-changed` | campaign | one handle |
| `dialogue.choice-made` | campaign | what you chose to say |
| `dialogue.node-reached` | session | where you are in a conversation |
| `check.resolved` | transient | declared, and **still emitted by nothing** |

**Every campaign-lifetime kind is written into the character's own log, and a
save is one character's log.** `DialogueRun.flagsFrom` and `questsFrom` are
folds over `List<CharacterEvent>` — **the same list, by the same mechanism, as
the vitality I proved at `019`.**

**⚠ SO THE ANSWER IS STRUCTURAL AND COMPLETE: there is no shared store of any
kind, for anything.** Not a second file, not a package-level log, not a field.
A flag set by one character is invisible to another for exactly the reason a
wound is.

### ⚠ AND A DOOR IS NOT STATE AT ALL

**There is no door you can open.** I searched the ledger and `area_open` for any
door kind and found **nothing**. A `[[connections]]` entry is a stateless
always-passable square; the `doors` blueprint kind has no folder mapping, so
Loom now says of it — correctly — *"cannot list — no folder is specified for
this kind yet."* **The question cannot arise until a door has a state to be in.**

### ⚠⚠ AND A FLAG CANNOT BE SET BY ANYONE — THE WRITE SIDE DOES NOT EXIST

**I went to author one and could not, and the reason is exact.**

- **Nothing shipped has ever set one.** Across all four packages the **only**
  authored effect is a single `effect = [ { kind = "encounter.began" } ]`.
- **Loom's effect button cannot carry a payload.** `conversation_tab.dart:302`:

      _act((d) => d.addEffect(sel, {'kind': _value.text.trim()}));

  **One key. The kind, and nothing else.** So the best an author can write is
  `effect = [ { kind = "quest.flag-set" } ]` — **with no `flag` field.**
- **And `flagsFrom` requires exactly that field**: `if (e.kind ==
  'quest.flag-set' && e.payload['flag'] is String)`. **A flag effect authored in
  Loom is silently a no-op**, because the one thing that makes it a flag cannot
  be typed.

**⚠ Loom has a `flag` GATE button — it can author a check that reads a flag —
and no way to author the effect that sets one.** The read side is on screen; the
write side is missing. **So "does a flag you set persist for the next
character?" has no experiment: you cannot set one**, and every `flag` gate
anyone authors today would refuse for every character forever.

**I did not file this as blocked and move on — the source is unambiguous and I
am reporting it as a finding.**

---

## ⚠ THE REVIVE SURVIVES THE QUIT — AND THAT IS THE PERMANENT STATE OF EVERY CREATURE

**My own negative from `019`, answered, from disk and from the screen.**

**In `yard-tester.sav`, two events, in order:**

    {"kind":"encounter.ended","payload":{"subject":"probe-sentinel.probe-room.04",…,"vitality":-2}}
    {"kind":"character.revived","payload":{"subject":"probe-sentinel.probe-room.04",…}}

**On screen after a full quit and `Continue`:**

> `probe-sentinel.probe-room.04: **1 of 8** — in your campaign, a01-probe-room
> left you at −2 · revived at 1`

**The fold reads both and yields 1.** So the revive is not a session artefact —
**it is persisted, and it is what the creature IS from then on.**

**⚠ Which is bigger than it sounds, and you were right that it is.** Combined
with `019`'s finding that nothing dies: **every creature anyone has ever beaten
stands at 1 vitality, permanently, in that character's campaign.** The bed's
trooper included, for anyone who wins. **A second visit is never a second
fight** — it is one hit.

---

## ⚠ WHAT A PLAYER ACTUALLY EXPERIENCES — AND `PT-1510`'s THREE WORDS DO THE WORK

**Two characters, the same room, seconds apart, identical boards:**

> **Yard Tester** — `probe-sentinel.probe-room.04: 1 of 8 — **in your campaign**,
> a01-probe-room left you at −2 · revived at 1`
>
> **Probe Walker** — `probe-sentinel.probe-room.04: 3 of 8 — **in your
> campaign**, a01-probe-room left you at 3`

**Asked what feels wrong: with those three words, not much — and that is a real
change.** At `018` the line read *"encounter a01-probe-room left you at 3"*,
phrased about the room, and the difference read as a bug. **"in your campaign"
scopes it to me**, and a creature at a different vitality then reads as my
history rather than the world's. **`PT-1510` fixed the thing I actually found.**

**⚠ What still does not land, and it is where a player meets the idea first:**

- **The scoping is only stated on the line that reports a difference.** A player
  who never wounds anything never sees the words *"your campaign"* at all, and
  so is never told the model exists.
- **`Load Game` is where it would matter most and says nothing.** Two rows,
  both reading `rules 0.1.0`, with no hint that choosing between them is
  choosing between worlds.
- **The boards are pixel-identical.** The only evidence that these are separate
  worlds is one line of small text along the bottom edge.

**So: the sentence is right where it appears, and the concept is introduced
nowhere.** That is the owner's to decide, and it is a smaller gap than `018`'s.

---

## ⚠ THE `listFor` COST — FILED, WITH NUMBERS

**You were right that the shape is new information even though the behaviour is
named.**

**Measured on this machine:** **17 saves, 451 events total**, and decompressing
every one of them takes **57 ms** in shell. **The Dart replay is on top of that
and I did not isolate it. It is not perceptible today, and I am not claiming it
is.**

**The shape is the filing:**

- `listFor(packageId)` calls `list()`, which **reads a header from every `.sav`
  in the folder**, and then **replays every one of them in full** to learn which
  package it belongs to.
- **It is O(every save on the machine), not O(saves in this package)**, and it
  runs **per hub open**.
- **⚠ Opening `base-rules` — which `PT-1380` makes a package that can never have
  a save — still reads and replays all seventeen.**
- **There is no index.** A save's package is discoverable only by decompressing
  and folding its whole log, because the header carries no package field. That
  is the same absent field request `001` flagged for naming and ordering.

**Seventeen files is one tester on one machine after a fortnight.**

---

## Two of mine that are now fixed

- **`015`'s F2 is closed, and honestly.** The palette lists `doctrines:
  hold-the-room` — the doctrine it could never show — and for kinds with no
  folder it now says *"⚠ cannot list — no folder is specified for this kind yet,
  so this list cannot be read — **it is not a count**"*. **The constant that
  pretended to be a fact now says what it does not know.**
- **`016`'s F2 is detected in Loom.** Opening my conversation and pressing
  `Write` now gives, in the status bar:

  > refused — 1 problem: halt-this-room — `stand-down-i` is offered as a
  > `Persuade` check and its `then` carries no check, so `_pick` takes the first
  > link before any dice are touched. §9 puts the check on the OUTBOUND li…

  **In the same terms I found it.** `PT-1379` holding: the Builder refuses to
  write the fault it detects.

**⚠ One consequence worth naming, and it is not a defect.** `sentinel-challenge`
was authored by Loom and **Loom will no longer save it** — correctly, because it
*is* the fault. **An artifact written by the Builder became unwritable when the
rule tightened**, and the only way to save it again is to re-author the gate
onto the outbound link. **The file on disk is untouched and the app still plays
it.** That is a migration cost, and it is the first time I have hit one.

---

## ⚠ TWO NEAR-MISSES, DECLARED

**I twice believed I had found a defect and twice it was not one.**

1. **"Loom's effect button silently does nothing."** It clears the fields and
   writes no effect — because **every `Write` was being refused** for the
   Persuade fault above. The draft was fine; the save never happened. **I
   checked the source and the status bar before filing.**
2. Earlier the same shape caught me on the doctrine dialog (`016`). **Twice now
   the thing that looked like a dead button was a refusal I had not read.**
   **The status bar is the first place to look, and I did not look at it first
   either time.**

---

## ⚠ SCOPED NEGATIVES

- **I could not run the flag experiment at all** — not because I ran out of
  time, but because the write side does not exist. **The claim above is a source
  reading plus a failed authoring attempt, not an observed persistence test.**
- **I did not repair my conversation** to satisfy §9 and retry the effect. That
  would have made the effect-write path testable and I chose not to change my
  own fixture mid-run.
- **Quests are entirely untested by me.** Same mechanism as flags, same missing
  write side, but I confirmed neither on screen.
- **`character.faction-changed` and `dialogue.choice-made`** — enumerated from
  the vocabulary, never exercised.
- **I did not measure the Dart replay**, only the decompression floor, and only
  in shell. **The 57 ms is a floor, not the cost.**
- **I did not time the hub opening.** My first attempt polled the wrong window
  and produced a meaningless 8 s; **I discarded it rather than reporting it.**
- **Position across a reload is untested** — `character.moved` is campaign
  lifetime now, but `probe-walker` loaded at `0,0` from a save I had restored
  from backup, so I cannot say what it would have done.
- **Not touched:** the eight inert blueprint kinds, `NewItemDialog`, other
  window sizes.
