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
> **⚠⚠ `character.xp-awarded` — `PT-2233`, AND THE NAME AND PAYLOAD ARE `Coder`'s, delegated.**
>
> **⚠ `permanent`, FOR THE REASON `character.levelled` IS.** XP earned is a fact about a character's history, not a scratch value, and a save that forgot it would have the character level up twice for one fight. The two travel together and must not have different lifetimes.
>
> **⚠ `xp-awarded` RATHER THAN `xp-gained` OR `experience-awarded`.** *Awarded* is what `EXPERIENCE-01` itself says — *"XP IS AWARDED FOR THE CREATURE'S CHALLENGE RATING"* — and the vocabulary's own style is `character.<past participle>`: `created`, `levelled`, `damaged`, `downed`, `revived`. `xp` rather than `experience` because `progress.xp` is already the field's name and two spellings of one quantity is how a reader comes to miss half of it.
>
> **⚠⚠ AND IT IS AN INCREMENT, WHERE `character.levelled` CARRIES A TOTAL.** That is a real difference and it is stated rather than left to be discovered: `levelled.xp` is *the total at the moment of levelling* — a snapshot, which is what lets an authored character state where it starts — and `xp-awarded.amount` is *what this fight paid*. Replay adds the second and SETS from the first, in log order, so a character made at level 20 and then played accumulates from its stated total rather than from zero.
>
>     subject   who earned it
>     amount    ⚠ the increment, after §3's split — not the encounter's total
>     from      what was beaten, by handle, for the line that says so
>     cr        the challenge rating that was looked up
>     level     the level it was looked up against
>
> **⚠ `cr` AND `level` RIDE THE EVENT BECAUSE THE DERIVATION IS THE ANSWER — `PT-1326`.** A player reading *"+250 — sith-trooper.command-deck.39, CR 3 at level 5"* can check it; one reading *"+250"* cannot. And a log that carries only the total cannot be re-derived the day the table is retuned.

> **⚠ A ROW IS NOT A KIND.** Rows name one, two or three in `a.b / .c` shorthand — **39 rows carry 50 kinds, and a reader counting rows is eleven short.** ⚠ `PT-1612` — this said *24 rows carry 36* and the extract's own note said *24 carry 33*; **three numbers for one fact, in a sentence whose subject is that counting rows misleads.** The extract computes it now.
| `character.xp-awarded` | permanent | ⚠⚠ `PT-2233` — **NEW.** |
| `character.levelled` | permanent |
| `character.damaged` / `.healed` | transient — *until the encounter ends* |
| `character.downed` / `.died` / `.revived` | campaign |
| `character.dying` | **transient — *until the encounter ends*** ⚠ `PT-1618` — newly declared |
| `character.condition-applied` / `.condition-expired` | transient — *until its own duration* |
| `character.moved` | **campaign** ⚠ `PT-1417` — was `session` |
| `character.alignment-shifted` | **permanent** — `PT-1279`, alignment history is not compactable |
| `character.side-chosen` | **permanent** — `PT-2433`, and see below |
| `character.faction-changed` | campaign |

> **⚠⚠⚠ `character.side-chosen` IS THE ONE KIND HERE I INFERRED RATHER THAN WAS TOLD, AND IT IS FLAGGED AS SUCH.** `PT-2433` ruled *"add the chosen-side field to the character record the same way"*, and a record field with **no writer** is the exact defect `replay`'s own comment names about `progress`: *"a declared field on a record nothing ever set — declared-and-read-by-nothing from the writing side — while sixteen readers asked for it and every one got the default."* The field cannot be real without a kind to set it, so this is the minimum the ruling requires. **Rename or reject it freely; nothing else depends on the spelling.**
>
> **⚠⚠ `permanent`, FOR THE REASON EVERY OTHER CHARACTER *CHOICE* IS.** `species-set`, `origin-set`, `feat-taken` and the other fifteen creation kinds are all permanent, and a chosen side is the same kind of fact: a declaration about who the character is, not a state a fight or a session resolves.
>
> **⚠⚠ AND IT IS NOT `character.alignment-shifted`, WHICH ALREADY EXISTS AND WHICH THIS MUST NOT QUIETLY BECOME.** That kind records a **shift** — a movement of the score — and `PT-1279` keeps it permanent because *"alignment history is not compactable."* Nothing emits it yet; `play_state.dart` says so in place. A chosen side is not a shift and does not move the score at all: it is the direction meditation is allowed to push in. Folding one into the other would be **one capability kept in two places**, and the drift mechanism `PT-2431` built is a third thing again — it folds `power.cast`, the deed, and derives the movement rather than recording it. When `§2.4`'s story shifts land, `character.alignment-shifted` is the kind they belong to, and the fold should read it alongside the deeds.

> **⚠⚠ `PT-1618` — `dying` IS THE ORDINARY FAILURE STATE AND IT HAD NO KIND.**
> `Tester` counted twenty saves: **125 crossings at or below zero, of which 40
> are exactly zero and 85 are negative.** `down` is reached only at exactly
> zero; **`dying` is 85 of 125 and there was no kind for it in the ledger or in
> the shipped rules.**
>
> **⚠ AND IT IS `transient`, FOR THE RULE `PT-1612` JUST USED.** `PT-1427`:
> *a fight is not a fact; its outcome is.* Dying is a state INSIDE a fight and
> **the fight resolves it** — you stand at 1 when combat ends, you are healed,
> or you die. **Whatever survives is already recorded**, by `encounter.ended`,
> `character.died` or `character.revived`.
>
> **⚠ AND ITS NEIGHBOUR ALREADY SAYS IT.** `character.damaged / .healed` is
> *transient — until the encounter ends*, and dying is a consequence of damage
> in the same band, ending at the same boundary.
>
> **⚠ AND A `campaign` ONE WOULD BE FOLDED BY NOTHING.** `projectPlayState`
> folds `died` and `revived`; a third unfolded campaign kind is `PT-1606`'s
> fifth state again. **And 85 of 125 is a frequency argument FOR transient**:
> a kind firing in two thirds of crossings and read by nobody would be the
> largest thing in the save, which is the case `SAVE-LOAD-01 §4` gives
> lifetimes their job for.
>
> **⚠⚠ AND THE TENSION IS NAMED RATHER THAN SMOOTHED: `character.downed` is
> `campaign` and is the same shape** — a crossing inside a fight that the
> fight resolves — **and it is folded by nothing either.** If `dying` is
> transient then `downed`'s lifetime is the anomaly, not this one. `PT-1618`
> preserved `downed` explicitly, so it stands; the question is recorded here.

### Equipment and items

| Kind | Lifetime |
|---|---|
| `item.equipped` / `.unequipped` | session |
| `item.acquired` / `.lost` | campaign |
| `item.used` | transient |

**⚠ `item.*` events exist even though KOTOR gave items zero hooks.** An item that cannot react is an item that cannot be a trap, a cursed blade, or a thing that reacts to being drawn.

**⚠⚠ `item.acquired` HAS A PRODUCER AND A CONSUMER NOW — `PT-1525`.** Looting a dead creature writes one per item, carrying `subject`, `item` (a blueprint path — `PT-1452` makes `[equipment]` a path always), `from` (the pile's placement **tag**) and `area`. `remainsIn` folds it back, and `carriedBy` is what the player reads.

**⚠ `item.lost` still has neither, and that is deliberate rather than forgotten.** Nothing takes an item away yet. A fold for a kind nobody writes is exactly `PT-1523`'s `character.moved` — declared, folded, emitted by nothing, **zero occurrences across seventeen saves** — and `check_event_producers` exists to see that shape. Its first producer will be `DIALOGUE-FORMAT-01 §9`'s effect, and the fold arrives with it.

**⚠⚠ `PT-2585` — THE PREDICTION LANDED.** `creditsAfter` folded `item.acquired`/`item.lost` for credits specifically (`PT-2548`), and `carriedBy`/`remainsIn` for everything else; both are real readers now. The trigger/effect system's tier one gives both kinds a THIRD producer beside looting and consumables spend: an authored `effect` naming `item.acquired` (give) or `item.lost` (take), `item` a blueprint path or the literal `credits`, `count` defaulting to 1. **`subject` is never asked** — `Loom`'s picker writes `subject = "you"` itself, matching `a_give_item`/`a_take_item`'s own real behaviour (`GetPartyLeader()`, never a picked target) and `store.opened`'s own precedent for a field with one obviously correct answer.

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
| `party.waiting` / `.following` | ⚠⚠ campaign — `PT-1832`. Standing orders (Wait here / Follow-regroup) did not survive a save until declared: `_persist` keeps only what `campaignKinds` names, and neither kind was in it. Confirmed as the only two undeclared kinds in the build by diffing every `CharacterEventKind` constant against the shelf. |
| `door.opened` / `.locked` / `.unlocked` | campaign |
| `container.opened` | campaign |

> **⚠⚠ `PT-2585` — `door.unlocked` AND `container.opened` GAINED A SECOND
> PRODUCER.** `BUILD 182` gave them a picked-lock producer and `unlockedIn`'s
> fold; the trigger/effect system's tier one gives them an AUTHORED one — a
> terminal or a dialogue reply's own `effect` list, written by `Loom`'s
> picker. Same kind, same fold, same `subject` field (the door or
> container's own tag). **`door.opened` and `.locked` remain declared and
> unproduced** — nothing in this pass writes a momentary "opened" fact or a
> re-lock; `unlockedIn` is a monotonic set and re-locking a picked door is a
> real question this pass did not answer, held rather than guessed at.
| `hazard.set` | ⚠⚠ campaign — `PT-1957`. A mine the PLAYER put down. Authored content is read-only at runtime, so a set mine cannot join the `[[hazards]]` an author wrote: the room's hazards become *authored + set − sprung − disarmed*, which is the shape `door.unlocked` already gives a door. **Campaign because a mine you set and walked away from is still there when you come back** — that is the whole point of setting one. Payload: the area, the square, the item it was set from, and the two DCs, which the setter's own Demolitions decides at the point of placement and the event then remembers. |
| `hazard.disarmed` / `.sprung` | ⚠⚠ campaign — `TEST`. **The other two terms of the formula the row above states.** `hazard.set` has said *authored + set − sprung − disarmed* since it was ruled, and neither subtraction had a kind: both were sets in the play screen that started empty on every load. So a defused mine came back live, a spent one came back armed, and a mine with a `recovers` handed out its item again every visit while the copies already carried were remembered — **an unlimited supply of a unique item, and no authored hazard that could ever be permanently cleared.** Campaign for the reason a picked lock is (`BUILD 182`). Two kinds rather than one because a mine that fired and a mine somebody defused are different facts about the same square; they are folded together only where the question is *is it still here*. Payload: the hazard's tag as `subject`, and the area. |

### Encounter

| Kind | Lifetime |
|---|---|
| `encounter.began` | **transient — *until the encounter ends*** ⚠ `PT-1612` — was `campaign` |
| `encounter.ended` | campaign |
| `turn.began` / `.ended` | transient — *until the encounter ends* |
| `attack.resolved` | transient |
| `check.resolved` | transient |

> **⚠⚠ `PT-1612` — A FIGHT IS NOT A FACT; ITS OUTCOME IS.** `PT-1427`'s own
> sentence decides it. **`encounter.ended` is `campaign` because a wound
> outlives the fight**; `encounter.began` describes a moment that is over the
> instant the fight resolves, and `PT-1606` confirmed **its single consumer
> reads the in-memory beat and never the log.**
>
> **⚠ And `§5` forbidding an author from NAMING it is not an argument for
> PERSISTING it.** That rule stops an author faking a fight; it does not make
> the fight a durable fact.
>
> **⚠⚠ AND THIS IS ONE CELL RATHER THAN A CODE CHANGE, WHICH IS THE REAL
> FINDING.** `PT-1603` made the app filter what it writes **by the declared
> lifetime** instead of by a hand-picked list — so **the lifetime is now the
> only thing that decides, a lifetime question is answered in this document,
> and the product follows.** The two rows above were one row until now, and a
> combined row is a cell that cannot be changed for one of its kinds.

**⚠ `check.resolved` carries its whole derivation**, which is `PLAY-STATE-01 §5`: KOTOR persisted *"Defense Breakdown: 18 = base 10 + dex mod 4 + class 4"*. **Every modifier named.** That is what makes a derived system honest, and turn-based gives us more room to show it, not less.

### Time, meditation and alignment — `PT-2433`

| Kind | Lifetime |
|---|---|
| `time.advanced` | campaign |
| `session.started` | campaign |
| `power.cast` | campaign |
| `meditation.short` | campaign |
| `meditation.long` | campaign |

> **⚠⚠⚠ ALL FIVE ARE `campaign`, AND THE REASON IS ONE REASON.** `ALIGNMENT-01 v2` is path-dependent by design — a character's standing is not a stored number but **a fold over what they actually did**, which `PT-2429` confirmed the ledger already satisfies for free. A fold can only be recomputed from events the save still holds. `PLAY-STATE-01 §2`'s `session` lifetime does not survive to disk, so any of these five written as `session` would be **written and dropped**, and the fold would answer 50 for every character forever.
>
> **⚠⚠ `power.cast` IS `campaign` FOR `encounter.ended`'s OWN REASON — `PT-1612`, `PT-1427`: *a fight is not a fact; its outcome is.*** Reaching for the dark side is not a moment inside a fight that the fight resolves; it is the outcome, and `§2.1` says so outright — *"the moral event is reaching for the dark side, not the number of times the trigger is pulled after."* It travels with `encounter.ended`, which is already `campaign`, and the two must not have different lifetimes for the same reason `character.levelled` and an xp award must not.
>
> **⚠⚠ `meditation.short` LOOKS LIKE THE WEAKEST OF THE FIVE AND IS NOT.** Its only reader is `§3`'s *"maximum two per day"* cap, which never looks further back than today — so `transient` reads as the honest answer. It is the wrong one: **a cap that does not survive a save is not a cap.** `PT-2432` shipped that hole knowingly, holding the count in screen state, and recorded it as a real one a player could walk through by reloading. The lifetime is what closes it.
>
> **⚠ `time.advanced` AND `session.started` ARE THE TWO BOUNDARIES THE OTHER THREE ARE COUNTED AGAINST** — `CLOCK-01 §5`'s elapsed clock and `PT-2430`'s accounting window. A boundary with a shorter lifetime than the things it separates would leave the fold unable to say which day or which sitting anything happened in, which is `§4`'s *"once per day"* and `§2.6`'s *"an entire session"* both unanswerable.

### Authoring and social

| Kind | Lifetime |
|---|---|
| `dialogue.node-reached` | session |
| `dialogue.choice-made` | campaign |
| `note.written` | **⚠ campaign, and unreadable** — `PT-1253`: Personal Notes are private. **The event records that a note exists, never its content.** |
| `store.opened` | **⚠ session, not campaign** — `PT-1152`, `PT-2548`. An author places it on a dialogue reply's own `effect` list, the same as `quest.flag-set`; the app watches for it in a beat's own events and opens the merchant it names. Nothing folds it into persistent state — a store visit does not need to outlive the sitting, and re-opening on a reload is not a defect.

### Presentation and discovery — `PT-2583`, `PT-2584`, `PT-2585`

**Three new kinds, the trigger/effect system's tier one.** `PT-2583`'s research swept both games' real terminal/console dialogues (234 found, 580 distinct action-script resrefs) and found real, confirmed analogues for these three with no existing kind to extend — unlike doors, containers and items, which already had one.

| Kind | Lifetime |
|---|---|
| `camera.shown` | **session** — matching `store.opened`'s own reasoning: a presentation moment, not a fact to remember. Re-showing on a reload is not a defect. |
| `map.revealed` | **campaign** — matching `area.entered`'s own lifetime. An area whose map has been revealed stays revealed. |
| `log.written` | **campaign** — matching `note.written`'s own lifetime, on purpose: `log.written` is that kind's deliberate opposite. A note is private and its text never enters the log; a `log.written` entry is discoverable CONTENT an author writes and a player is meant to read back. A recovered log should not need recovering twice. |

**⚠⚠ `camera.shown` CARRIES NOTHING, AND THAT IS A FINDING, NOT A GAP LEFT OPEN.** Real KOTOR's `SetDialogPlaceableCamera(nCamera)` names a camera INDEX — a 3D scene's own placed camera. This project has no camera concept at all; a top-down, paper-doll interface has nothing a camera index could mean. Inventing a field now would be `§3b`'s own warning one level up — a payload invented ahead of the consumer that would give it meaning. So the kind is declared and authorable, the same shape `encounter.began` already has (the kind alone is the whole effect), and it is inert until a real presentation concept exists to read it.

**⚠ `map.revealed` (`area`) AND `log.written` (`log`, `text`) HAVE NO CONSUMER YET EITHER, AND ARE VALIDATED ANYWAY** — the opposite call from `item.lost`'s old one, above. The fields are not invented for this document: `area` is the same field `door.unlocked`'s own producer already writes, and `log`/`text` are the same shape `quest.flag-set`'s `flag` already is. Validating them now means whichever future system reads a journal-style discoverable-logs screen inherits well-formed data across every package already authored, instead of repeating `item.lost`'s own gap.

---

## ⚠⚠ 3b · WHAT A KIND CARRIES IS MOSTLY UNWRITTEN — named at `PT-1516`

**This document declares kinds and their LIFETIMES. It does not say what any of them CARRIES**, and `PLAY-STATE-01 §6` leaves every payload **deliberately unspecified**. That is a real gap and it is named here rather than filled.

**⚠ It bit for the first time at `PT-1516`.** `Loom`'s effect button wrote `{ kind: … }` and nothing else, so the best an author could produce was:

```toml
effect = [ { kind = "quest.flag-set" } ]
```

**`DialogueView.flagsFrom` matches on a `flag` field.** So **a flag effect authored in Loom was silently a no-op** — beside a `flag` GATE button that could read one. **A readable half with no writable half, offered as if complete.**

### The kinds something actually reads

**Derived from the CONSUMERS, not from what a field name suggests.** Three at
`PT-1516`; `PT-2585` adds five real readers and two validated-ahead-of-time
kinds in the same pass that found `item.lost`'s own long-open gap.

| kind | carries | read by |
|---|---|---|
| **`quest.flag-set`** | **`flag`** — a string | `DialogueView.flagsFrom` |
| **`quest.concluded`** | **`quest`, `conclusion`** — both strings | `DialogueView.questsFrom` |
| **`encounter.began`** | **AN AUTHOR'S carries nothing.** The kind alone is the whole effect | `PT-1437`, `Beat.endsInFight` |
| **`encounter.began`** ⚠ ENGINE | **`subject`, `encounter`** — `PT-1672`, the same payload `encounter.ended` carries | `combatRoster` |
| **`door.unlocked`** | **`subject`** — the door's own tag | `unlockedIn`, `BUILD 182` |
| **`container.opened`** | **`subject`** — the container's own tag | `unlockedIn`, `BUILD 182` |
| **`item.acquired`** | **`subject`, `item`, `count`** (defaults to 1) | `creditsAfter` (when `item = "credits"`); `carriedBy`/`remainsIn` otherwise |
| **`item.lost`** | **`subject`, `item`, `count`** (defaults to 1) | same two, the withdrawing half |
| **`map.revealed`** ⚠ | **`area`** — validated, no consumer yet | none — see below |
| **`log.written`** ⚠ | **`log`, `text`** — validated, no consumer yet | none — see below |

**⚠⚠ TWO PRODUCERS, ONE KIND, AND THE PAYLOAD IS WHAT SEPARATES THEM — `PT-1672`.** An author's is a **request to start a fight**; the engine's is the **record that somebody is in one.** Began and ended are the two halves of one membership, so they carry the same payload, and a matched pair is the only shape a fold can close.

**⚠ So `combatRoster` requires a `subject`, and a `began` that names nobody joins nobody.** A fold that fell back to a placeholder would put a row on the panel with a health bar for a creature that does not exist — and `PT-1672`'s whole reason is that **an absence has to mean one thing.**

**`validateConversation` requires exactly those fields and nothing else**, and `PT-1379` means `Loom` therefore cannot author one that is missing them.

### ⚠ And most of the gap is left open on purpose

**Every OTHER declared kind has no specified payload and no consumer reading one.** Requiring fields nobody reads would be **a validator inventing a format.**

> **⚠⚠ `item.lost` WAS THE SHARP CASE, AND IT CLOSED — `PT-2585`.** `DIALOGUE-FORMAT-01 §9`'s own worked example wrote `{ kind = "item.lost", item = "credits", count = 50 }` while **nothing in this project read it** — an author following the format's own example wrote an effect that did nothing, and the only reason that was not `PT-1516` again was that no gate read a purse. `creditsAfter` and `carriedBy`/`remainsIn` are real readers now, so the table above requires exactly those fields.

> **⚠ AND `map.revealed`/`log.written` ARE THE OPPOSITE CHOICE, MADE DELIBERATELY.** No consumer exists for either, and they are validated anyway — reasoned through at `PT-2585`: the fields are not invented for this document, they reuse a shape every other spatial/named kind here already has, so validating now means a future consumer inherits well-formed data across every package already authored instead of repeating `item.lost`'s own gap. **This is a real, considered exception to the rule stated two lines up, not a quiet contradiction of it.**

**What would close the rest:** a payload column in the tables above, written **when a consumer exists** — kind by kind, as each one gains a reader. **Not all at once, and not from what the names imply.**

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

### ⚠⚠ `3d` · A FOURTH STATE, AND ALL THREE CHECKS ARE BLIND TO IT — `PT-1509`

`§3c` names three ways this document and the code can disagree. **There is a fourth, and it has no end at all:**

> **`area.entered` has NO CONSTANT, NO PRODUCER AND NO CONSUMER anywhere in the project.** Declared `campaign` at `PT-1417`, and **entirely unimplemented.**

**Check A** wants *emitted and undeclared*. **Check B** wants *declared and replay ignores it*. **`check_event_producers`** wants *a fold with no producer*. **A kind with neither end is invisible to all three.**

**⚠ AND IT IS NOT ADDED TO THE CHECK, DELIBERATELY.** *Declared and unimplemented* describes most of this vocabulary — `door.opened`, `container.opened`, `party.joined`, `item.used` — and that is **a roadmap, not a defect.** (`item.acquired` left that list at `PT-1525`; `encounter.began` gained an engine producer at `PT-1672`.) A check that flags a roadmap is a check somebody switches off, which is `TEST 016 F3`'s lesson applied before the fact.

**⚠⚠ IT WAS A DEFECT HERE ONLY BECAUSE A RULING LEANED ON IT.** `PT-1509` calls the map *"nearly free"* **because `area.entered` is campaign lifetime** — a premise that reads as *the event is there* and is not. The map folds `character.moved` instead, which carries `area` and has been written at every arrival since `PT-1523`.

**The premise held for a different reason than the ruling gave**, and that is the thing to know before anyone else builds on `area.entered`.

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
