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
