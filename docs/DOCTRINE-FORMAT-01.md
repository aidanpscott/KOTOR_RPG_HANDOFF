# DOCTRINE-FORMAT-01 — what is inside a doctrine

**`PT-1441` gave it a home: `blueprints/doctrines/`, beside `characters/`.** This is what goes in the file.

**⚠ DERIVED FROM THE CODE, NOT FROM A DOCUMENT.** `PT-1423` built the decision procedure and `ENGINE-SPEC-04 §6` does not carry its shape — `SPACE-AI-01 §1`'s four questions are the design, and `doctrine.dart` is the only place the answers are written down. **This document describes what already runs.**

---

## 1 · A doctrine answers four questions

`SPACE-AI-01 §1`, and the file is laid out in the order they are asked:

    1  what is my goal this fight?       goal
    2  when do I break off?              [break_off]
    3  which target serves it?           [[never]] then [[prefer]]
    4  what range does my doctrine want?  want_range

**⚠ BREAK OFF IS SECOND, NOT FOURTH, AND THE FILE SAYS SO.** `PT-1423`: *"a doctrine that is leaving does not pick who to leave."* `decide()` answers it before it looks at a target, and **the file reads in the order the engine asks.**

```toml
[doctrine]
name       = "Sith line"
goal       = "hold the deck"
want_range = "close"

[break_off]
when = "never"
```

| field | | |
|---|---|---|
| `name` | what the decision records | **required** |
| `goal` | the faction's own word for what it wants — `SPACE-AI-01`'s *"capture, not destruction"* | **required** |
| `want_range` | `close` · `medium` · `long` | no — `medium` |
| `keep_at_least` | how many squares a caller should keep this doctrine from its target, even while it still fights — `PT-2628`/`PT-2649`/`PT-2650`, Defensive's own field | no — `null`, no minimum kept |
| `holds_ground` | `true`/`false` — Stand Ground, `PT-2610`/`PT-2656`: never move under any circumstances, still choose a target and still attack with whatever is already in reach | no — `false` |
| `item` | a bare item id this doctrine tries to use offensively — `PT-2610`/`PT-2656`/`PT-2659`, a genuinely new capability class distinct from `[[support]]`'s own ally/self-directed powers | no — `null` |
| `[break_off] when` | `never` · `alone` · `below` (with `fraction`) | no — `never` |
| `[break_off] retreat_at_least` | how many squares a caller should walk this doctrine away once it breaks off — `PT-2649`/`PT-2650` | no — `null`, breaking off just holds |

**⚠ `never` IS THE DEFAULT AND IT IS A REAL ANSWER**, not an absence: `SPACE-AI-01` — *"NEVER, and this one is a culture, not a tactic."*

**⚠⚠⚠ `retreat_at_least` IS NOT NESTED UNDER `below` SPECIFICALLY** — `PT-2628` names retreat as *"a conditional low-health behavior"*, which is `below`'s own shape, but the engine does not itself restrict which break-off rule may carry a flee distance: `decide()` runs the same targeting pipeline regardless of which `BreakOff` fired, so a doctrine that breaks off `alone` and also names a distance flees too. **The field sits beside `when`, not inside one branch of it, because the code draws no line there and the format does not invent one.**

**⚠⚠⚠ `keep_at_least` IS NOT A `[break_off]` FIELD AT ALL** — Defensive, `PT-2628`, is *"a ranged-weapon-holder actively keeping distance from an approaching melee threat"* while it is still choosing a target and still attacking; it has nothing to do with leaving the fight. It sits beside `want_range` in `[doctrine]` instead — the symmetric counterpart to closing a distance, not a break-off condition. `PT-2628` also rules the exact number a balance/playtesting question, not a design one: **2 or 3 squares is a reasonable starting value, and it is content, tunable per doctrine, never a hardcoded engine constant.**

**⚠⚠⚠ `holds_ground` IS A BOOL, NOT A DISTANCE.** Stand Ground, `PT-2610`/`PT-2656`, is source-confirmed against K2's own real `k_inc_generic.nss`: a `NPC_AISTYLE_PARTY_STATIONARY` branch exists with a genuine, documented intent — *"Just stand in one place and shoot. Don't move under any circumstances"* — but its own call to the routine that would do it is commented out, and the branch silently falls through to the SAME function the Ranged preset calls. Shipped K2 "Stationary" is Ranged wearing a different name; this field is what the source's own comment actually describes. **Not the same thing as `want_range`'s own `medium`/`long` "holds where it is" fallthrough** — that is an accident of a band nobody gave real squares to, not a deliberate choice.

**⚠⚠⚠ `item` NAMES ONE ITEM, NOT A LIST** — unlike `[[support]]`, which is a real priority ladder of several powers. `GN_GetGrenadeTalent` picks ONE grenade type dynamically, by what the thrower actually carries and whether the target is a droid; an authored priority order over several item ids would be answering a question the real source resolves at throw-time, not authoring-time. **Named unconditionally, the same reason `want_range`/`keep_at_least` are** — `decide()` stays grid-free, and whether a good AoE cluster actually exists this turn is a real geometry question only a caller with a real board can answer.

---

## 2 · ⚠⚠ Exclusions are their own section. **A file cannot write one as a preference**

> **`PT-1423`: *"never is not a preference that lost."*** The engines, then the turrets, **never the hull** is an ordered preference **and** an exclusion, and they are different shapes. **Exclusions apply before every preference**, so the hull is not chosen *even when it is the only thing left* — and `none:all-excluded` is a decision that **says which kind**.

**⚠ SO THE FORMAT GIVES THEM TWO SECTIONS AND NO WAY TO CONFUSE THEM.**

```toml
[[never]]
match   = { role = "companion_beast" }
because = "not the animals"

[[prefer]]
rule = "weakest"

[[prefer]]
match   = { handle_starts = "carth" }
because = "the officer first"

[[prefer]]
rule = "any"
```

**A file with an exclusion written last in `[[prefer]]` is not expressible.** There is no `never` value for `prefer.rule` and no `match` semantics that exclude. **The distinction cannot be lost by an author, because the author has no way to write it wrongly** — the same argument as `DIALOGUE-FORMAT-01 §4`'s closed grammar, and for the same reason: **a rule you can only state correctly cannot drift.**

### `[[prefer]]` is ordered and the order is the preference

**Tried in order; the first that picks anything wins**, and `ruleFired` records which. A tie takes **the first in initiative order** — a fact of the fight rather than of the file — unless the caller supplies a die.

| `rule` | |
|---|---|
| `nearest` | ⚠ **declines rather than guessing** when the caller supplied no distances — `PT-1423` |
| `weakest` | the least vitality left |
| `any` | ⚠ the last resort, and deliberate: with every preference declined a doctrine still has to act |
| *(omitted, with `match`)* | the general form — *"the one with the lightsaber"* |

---

## 3 · ⚠ `match` is a closed vocabulary, because it is a predicate in a file

`Never` and `Prefer` carry `bool Function(Combatant)` in the code. **A file cannot carry a closure**, so a match is **data**, and the vocabulary is closed exactly as `DIALOGUE-FORMAT-01 §4`'s gate is.

| key | tests | |
|---|---|---|
| `role` | `player` · `companion_droid` · `companion_beast` · `henchman` | `pools.dart`'s `Role` |
| `handle` | the placement tag exactly — `PT-1331` | |
| `handle_starts` | its prefix, so one rule covers `sith-trooper.*` | |
| `below` | vitality at or under this fraction of capacity | 0.0–1.0 |

**⚠ AN UNKNOWN KEY IS A LOAD FAILURE, NOT AN EXTENSION POINT.** Same rule, same reason.

**⚠ AND A `match` READS THE COMBATANT AND NOTHING ELSE.** It cannot reach the log, the world or a projection — a doctrine decides from `DoctrineView`, which `PT-1423` made *"a state and a declaration, never a world."*

---

## 4 · A creature names a PATH

```toml
[attachments]
doctrine = "doctrines/sith-line"
reaction = [ { on = "character.downed", then = "rally" } ]
```

**`PT-1441`: a path, not a handle.** `PACKAGE-NAMING-01` makes the path identity and **every other cross-reference in the format is one** — `from`, `tileset`, a conversation's `owner`. **A handle needs a lookup table and nothing declares one.**

**⚠ AND A REACTION IS INLINE WITH NO FILE.** `ATTACHMENT-01 §3` makes it two fields, `on` and `then`; **a file per two-field record is worse than the record.** A doctrine earns a file because it carries preferences, exclusions and a break-off rule. **Written out like this it also stops dangling** — `§2`'s bare list of names pointed at nothing declared anywhere, and this points at itself.

---

## 5 · What is NOT in a doctrine

**No scripts.** `§2` and `§3` are the whole of what a doctrine can say.

**No randomness.** `PT-1423`: *"given a log, the same fight must play the same way."* A doctrine that wants a random choice among equals **is given the die by the caller** and it is the injected one. **There is no seed field and there must not be.**

**No target it can reach for.** A doctrine sees `DoctrineView` — self, enemies in initiative order, allies, and distances **if the caller has them.**

**⚠ No reactions.** `PT-1373`: a trigger produces an event and a reaction consumes one; **a doctrine is neither — it is a decision procedure invoked at a known point.** They are two mechanisms and this file is one of them.

---

## 6 · ⚠ What this format cannot express

- **⚠ A goal that means anything.** `goal` is a string the decision carries and **nothing reads it** — `SPACE-AI-01`'s *"capture, not destruction"* changes what a fleet does, and here it changes nothing. **It is recorded for the narrator and is otherwise inert.**
- **A match on anything but a combatant.** No *"the one holding the codes"*, because equipment is not in `DoctrineView`.
- **Per-ally rules.** `allies` is in the view and no rule reads it except `alone`.
- **⚠ A doctrine that changes mid-fight.** It is picked once and asked every turn. Escalation is `PT-1316`'s and is not this.

---

## 7 · Open

- **`goal` is inert** — `§6`. It wants either a vocabulary or a ruling that it is narration only.
- **Whether an instance may override its template's doctrine.** `AUTHORED-CHARACTER-01 §4` allows an instance to override an attachment *"only if the template permits it"* — and **no field says which attachments are overridable.**

**⚠⚠⚠ CLOSED — `want_range` HAD A CALLER BEFORE THIS DOCUMENT NOTICED.** `PT-1442` stored it, `PT-1593` gave `Fight.enemyTurn`'s `closeOn` a real caller for it — this document's own §6 and this section both still claimed otherwise until `PT-2628`/`PT-2649`/`PT-2650` Slice 4 corrected them, having built `retreat_at_least` and `keep_at_least` right beside it. **The reading was stale before this thread ever started; nobody had come back to update it once the code moved.**
