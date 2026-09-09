# EVENT-KINDS-01 — what the log records

**Closes `AGENDA-RECORD-01` item 3.** `PLAY-STATE-01 §2` gave four lifetimes and no vocabulary; `ATTACHMENT-01 §3` gave reactions a shape and no list of things to react to. **This is the list, and it is the same list.**

**⚠ One vocabulary, two consumers.** An event is what the log records *and* what a reaction listens for. **They must not be separate lists** — `PT-1268`'s reasoning applied here: two lists that mean the same thing drift, and the drift is invisible until something fails to fire.

---

## 1 · What KOTOR had, and the two hooks that are confessions

`TRACE-87` enumerated every script-bearing field on every object type:

```
module 14    creature 14    door 14    placeable 15/16
trigger 7    encounter 5    area 4     store 1
items 0      waypoints 0    sounds 0
```

**⚠ Three of nine blueprint types are completely inert.** An item cannot react to anything.

**And two hooks are symptoms rather than models:**

- **`UserDefined`** — an integer-coded event scripts raise on each other. **The only open extension point in the game**, and it is untyped.
- **⚠ `Heartbeat`** — **a poll, because there is no event for what the author needed.** Every use of it is a question the vocabulary could not answer.

**`ATTACHMENT-01 §3` excluded polling. `Heartbeat` is the evidence for why** — and the test for this document: **if an author would reach for a heartbeat, a kind is missing.**

---

## 2 · The shape of a kind

```
kind        what happened            past tense, always
subject     who or what it happened to
lifetime    permanent | campaign | session | transient
payload     the specifics
```

**⚠ Kinds are TENSELESS, and this is a rule rather than a style — corrected at `PT-1288`.**

An earlier draft said *past tense*. That was imprecise. **`character.damaged` does not mean "the character was damaged" — it means "damage occurs at index 47."** Past tense smuggles in a moving *now* that **the log does not have**.

**The log is a fixed series.** Event 47 does not become more past as the campaign runs. *"Now"* is replay to the end; *"then"* is replay to index 47. **Both are equally available**, which is why `PT-1272`'s projection model works at all.

**What the rule is actually about is direction of fit: an event RECORDS, it does not REQUEST.** `TRACE-85` found KOTOR's combat API entirely observational — `GetLastAttackResult` — **so you see resolution and cannot replace it.** A limitation for KOTOR; correct for us.

**A reaction that could prevent an event would make the log a negotiation.** It is not.

---

## 3 · The kinds

**Grouped by what they are about. Lifetime is declared per kind, per `PLAY-STATE-01 §2`.**

### Character — the log's core

| Kind | Lifetime |
|---|---|
| `character.created` | permanent |

**⚠ THE FOURTEEN CREATION KINDS — `PT-1418`.** *(A heading, outside the table. `PT-1419`: as a ROW it was read as a fifty-first kind with no lifetime.)*

| Kind | Lifetime |
|---|---|
| `character.species-set` | permanent |
| `character.model-set` | permanent |
| `character.class-added` | permanent |
| `character.origin-set` | permanent |
| `character.gender-set` | permanent |
| `character.backstory-set` | permanent |
| `character.ability-set` | permanent |
| `character.skill-ranked` | permanent |
| `character.feat-taken` | permanent |
| `character.power-taken` | permanent |
| `character.grant-resolved` | permanent |
| `character.equipment-set` | permanent |
| `character.identity-set` | permanent |
| `character.step-reopened` | permanent |

> **⚠ `PT-1420` — AN EMITTED KIND REPLAY IGNORES MUST SAY IT NEED NOT PERSIST.** Check A asserts `emitted == handledByReplay`, **which holds only because the two sets currently coincide.** `attack.resolved` is **transient** and replay will never fold it — **so the first combat emission breaks that assertion.**
>
> **The generalisation, and it is the agent's:** **⚠ a PERMANENT kind replay ignores is the bug; a TRANSIENT one is the design.** The check must compare against **lifetime**, not against replay's switch.
>
> **⚠ CORRECTED at `PT-1435` — REPLAY IS NO LONGER THE ONLY PROJECTION.** `PT-1427` built `projectPlayState`, and dialogue proved the gap: **`quest.flag-set` is PERMANENT, replay does not fold it, and that is correct** — it is world state, and the character record was never going to hold it.
>
> **The rule as written would call that a bug.** It should read: **⚠ a permanent kind that NO PROJECTION folds is the bug.** The check compares against the **union** of what every projection folds, not against `replay`'s switch alone.
>
> **⚠ And dialogue introduces DATA-DRIVEN EMISSION, which check A cannot see at all.** Its `emitted` set is *"every kind this build can write"*, **listed by hand** — and **a package's `effect` may name any declared kind.** The validator checks those against this document; **nothing checks their lifetimes.**

> **⚠ `PT-1418` — THE FOURTEEN, AND WHY `permanent`.** `PT-1415` proposed them as a reading and the check made the debt runnable: **fourteen of fifteen emitted kinds were undeclared.** They are **`permanent` because `character.created` is** — a creation choice never expires and never resolves.
>
> **⚠ And `step-reopened` is permanent too, which looks wrong and is not.** It carries **the list of steps it discarded**, so replay can clear exactly those slices — **the discard is a fact about the character's history, not a scratch value.** `PT-1415`: *a correction is a new event, not an edit.*
>
> **⚠ A ROW IS NOT A KIND.** Six rows name two or three in `a.b / .c` shorthand — **24 rows carry 36 kinds, and a reader counting rows is twelve short.**
| `character.levelled` | permanent |
| `character.damaged` / `.healed` | transient — *until the encounter ends* |
| `character.downed` / `.died` / `.revived` | campaign |
| `character.condition-applied` / `.condition-expired` | transient — *until its own duration* |
| `character.moved` | **campaign** ⚠ `PT-1417` — was `session` |
| `character.alignment-shifted` | **permanent** — `PT-1279`, alignment history is not compactable |
| `character.faction-changed` | campaign |

### Equipment and items

| Kind | Lifetime |
|---|---|
| `item.equipped` / `.unequipped` | session |
| `item.acquired` / `.lost` | campaign |
| `item.used` | transient |

**⚠ `item.*` events exist even though KOTOR gave items zero hooks.** An item that cannot react is an item that cannot be a trap, a cursed blade, or a thing that reacts to being drawn.

### Quest — `QUEST-MODEL-01`

| Kind | Lifetime |
|---|---|
| `quest.flag-set` | **permanent** — `PT-1284`, flags are never unset |
| `quest.concluded` | **permanent** — carries *which* conclusion |

### World and party

| Kind | Lifetime |
|---|---|
| `area.entered` / `.left` | **campaign** ⚠ `PT-1417` — was `session` |
| `party.joined` / `.left` | campaign |
| `door.opened` / `.locked` / `.unlocked` | campaign |
| `container.opened` | campaign |

### Encounter

| Kind | Lifetime |
|---|---|
| `encounter.began` / `.ended` | campaign |
| `turn.began` / `.ended` | transient — *until the encounter ends* |
| `attack.resolved` | transient |
| `check.resolved` | transient |

**⚠ `check.resolved` carries its whole derivation**, which is `PLAY-STATE-01 §5`: KOTOR persisted *"Defense Breakdown: 18 = base 10 + dex mod 4 + class 4"*. **Every modifier named.** That is what makes a derived system honest, and turn-based gives us more room to show it, not less.

### Authoring and social

| Kind | Lifetime |
|---|---|
| `dialogue.node-reached` | session |
| `dialogue.choice-made` | campaign |
| `note.written` | **⚠ campaign, and unreadable** — `PT-1253`: Personal Notes are private. **The event records that a note exists, never its content.** |

---

## ⚠⚠ 3b · WHAT A KIND CARRIES IS MOSTLY UNWRITTEN — named at `PT-1516`

**This document declares kinds and their LIFETIMES. It does not say what any of them CARRIES**, and `PLAY-STATE-01 §6` leaves every payload **deliberately unspecified**. That is a real gap and it is named here rather than filled.

**⚠ It bit for the first time at `PT-1516`.** `Loom`'s effect button wrote `{ kind: … }` and nothing else, so the best an author could produce was:

```toml
effect = [ { kind = "quest.flag-set" } ]
```

**`DialogueView.flagsFrom` matches on a `flag` field.** So **a flag effect authored in Loom was silently a no-op** — beside a `flag` GATE button that could read one. **A readable half with no writable half, offered as if complete.**

### The three kinds something actually reads

**Derived from the CONSUMERS, not from what a field name suggests:**

| kind | carries | read by |
|---|---|---|
| **`quest.flag-set`** | **`flag`** — a string | `DialogueView.flagsFrom` |
| **`quest.concluded`** | **`quest`, `conclusion`** — both strings | `DialogueView.questsFrom` |
| **`encounter.began`** | **nothing.** The kind alone is the whole effect | `PT-1437`, `Beat.endsInFight` |

**`validateConversation` requires exactly those fields and nothing else**, and `PT-1379` means `Loom` therefore cannot author one that is missing them.

### ⚠ And the gap is left open on purpose

**Every other declared kind has no specified payload and no consumer reading one.** Requiring fields nobody reads would be **a validator inventing a format.**

> **⚠⚠ `item.lost` IS THE SHARP CASE.** `DIALOGUE-FORMAT-01 §9`'s own worked example writes `{ kind = "item.lost", item = "credits", count = 50 }` — **and nothing in this project reads it.** The fields look load-bearing and are decoration. **An author following the format's own example writes an effect that does nothing**, and the only reason that is not `PT-1516` again is that no gate reads a purse.

**What would close it:** a payload column in the tables above, written **when a consumer exists** — kind by kind, as each one gains a reader. **Not all at once, and not from what the names imply.**

---

## ⚠⚠ 3c · THE THIRD WAY THIS DOCUMENT AND THE CODE CAN DISAGREE — `PT-1523`

**Two directions were checked and the third was not:**

| | | |
|---|---|---|
| **A** | a kind **emitted** and **undeclared** | `PT-1418` — fourteen of fifteen |
| **B** | a kind **declared** and replay **ignores** it | `PT-1418` |
| **⚠⚠** | a kind **declared**, **folded by a projection**, and **written by nobody** | **unseen until `PT-1523`** |

**`character.moved` was the third.** Declared `campaign` **with the reason in its own comment** — `PT-1417` moved it up from `session` *because a save needed to know where a player was standing* — folded by `projectPlayState` into a `Position`, and **emitted by nothing at all.** `TEST 021` checked all 17 saves: **zero occurrences.** It passed both checks.

**⚠ Neither could see it, and the reason is structural:** both compare THIS DOCUMENT against a set of kinds **the code declares it handles.** Neither asks *is there a construction site* — which is a plain source-level fact and nothing was reading it.

**`scripts/check_event_producers.py` reads it now.** ⚠ **Its honest limit is data-driven emission**, which `PT-1435` already named: a package's `effect` may name any declared kind, so the runtime writes it through a site that names no kind at all. The check therefore carries an **explicit allowance list with a reason per entry** — because *a check that excuses whatever it finds checks nothing* — and verifies that list **both ways.**

> **⚠⚠ AND IT FOUND ONE MORE WHILE PASSING: `character.faction-changed` is folded and no engine code writes one.** `FACTIONS-01 §4b` gives a character **one handle and explicitly not a standing track**, so there is nothing for the engine to move. **Allowed with that as the reason**, so the day something should change a faction, this is the argument to overturn.

---

## 4 · What is deliberately absent

**No `heartbeat`, no `tick`, no timer.** `§1` — a heartbeat is a missing kind wearing a costume. **If an author reaches for one, add the kind.**

**No `user-defined`.** KOTOR's only extension point was an untyped integer. **A package that needs a kind we do not have should say so**; an escape hatch that accepts anything is a vocabulary that has given up.

**No pre-resolution events.** `§2` — no `attack.attempting`, no `check.about-to-resolve`. **Past tense only.**

**No perception, no AI state, no animation.** `PLAY-STATE-01 §4` excluded these as continuous-time machinery.

---

## 5 · How a reaction uses this

**`ATTACHMENT-01 §3` now has its vocabulary:**

```
reaction:  on: character.downed      then: doctrine.rally
reaction:  on: door.opened           then: dialogue(dlg.confront)
reaction:  on: quest.flag-set        then: ...
```

**A reaction names a kind and optionally filters on payload.** It **listens**; it does not poll, and it cannot prevent.

---

## 6 · Open

- **⚠ Payload shapes.** Every kind names a payload and none is specified. **That is deliberate** — payloads follow from the systems that emit them, and inventing them here would produce a parallel definition.
- **Filtering.** `§5` says a reaction *may* filter on payload; the expression is unspecified. **⚠ `TRACE-87` is the guide: K1 needed 2,345 bespoke gate scripts, K2 needed 509, because the operand moved into the content file and the operator stayed in code.**
- **Whether a package may declare its own kinds**, and how they scope.
- **Ordering within a turn** — whether two events in one turn have a defined order, and whether reactions can see each other's events.
