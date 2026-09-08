# DIALOGUE-FORMAT-01 — what is inside a conversation

**`PACKAGE-FORMAT-01 §3` names a `dialogue/` folder and specifies nothing inside it.** `AREA-FORMAT-01` closed the same gap for areas; this closes the last one of that shape.

**⚠ This document designs a FILE. It does not design the model.** `ENGINE-SPEC-03 §2` settled the model — *"THE BIOWARE MODEL, UNCHANGED"* — and `STUDY 18` verified it against 1,065 K1 and 973 K2 shipped conversations. **Nothing here reopens it.**

**⚠ AND IT COVERS ONE OF THE TWO KINDS OF DIALOGUE.** `ENGINE-SPEC-03 §1`: an authored NPC is **a tree**; a generated NPC is **a filter over a shared topic space** and *"doesn't need a tree at all."* **This format is the tree. It is not the topic space, and a package with only generated NPCs has no `dialogue/` folder.**

---

## 1 · A conversation is three lists and nothing else

> **NPC lines, player lines, and the ways in. A link carries a target and a gate. Walk links in order and take the first that passes.**

That is `§2` verbatim, and `STUDY 18 R18.02` confirms it is what the shipped files do. **The alternation is structural:** an NPC line's links may only name player lines and a player line's links may only name NPC lines. **It is not a rule the format asks you to follow — there are two lists, and a link that crosses wrongly names an id that is not in the list it must be in.**

```toml
[conversation]
id    = "trooper-challenge"
owner = "sith-trooper.command-deck.07"     # whose conversation this is
```

**`owner` is a placement tag, not a blueprint path** — `PT-1331`, a tag names ONE placed thing. **It is the default speaker for every NPC line and the only thing the file says about who you are talking to.**

---

## 2 · ⚠ Nodes are addressed by NAME. There is no index

**This is the one place the file departs from `.dlg`, and it is not a model change.** `STUDY 18 R18.02`: their link carries `Index`, an offset into the other list.

**⚠ `ENGINE-INTERFACE-01`: *never expose an ordinal.*** `TRACE-83` found position-as-identity across 155 KOTOR tables, and `F35` found the engine writing an appearance index **past the end of the table it indexed with nothing rejecting it**. `AREA-FORMAT-01 §3` already applied the rule: *"`from` is a PATH, never an index."*

**And the practical case is decisive for a hand-written file:** insert one node into an index-addressed list and **every link after it silently points somewhere else.** A diff shows a renumbering; it does not show a broken conversation.

    id      unique within this file, kebab-case
    link    names an id, never a position

**⚠ Order still matters and is still array order.** `§2`'s *"walk links in order, first pass wins"* is unchanged — **the order is the order the links are written in**, which is visible in the file and in the diff. Names replace indices as identity; **they do not replace order as precedence.**

---

## 3 · ⚠ The eight fields, not the forty-eight

`STUDY 18 F18.04`: of K2's ~48 node fields **about eight carry meaning rather than staging**, and `PT-1319` deleted the rest for us before this document existed — a character is a portrait, nothing animates, there is no model.

**An NPC line:**

```toml
[[npc]]
id      = "challenge"
say     = "This deck is sealed. Turn around."
replies = ["bluff", "back-off"]
```

| field | | required |
|---|---|---|
| `id` | its name in this file | **yes** |
| `say` | the authored line | **yes** |
| `replies` | ordered links to player lines | no — absent means the conversation ends here |
| `by` | speaker override — `§6` | no |
| `to` | who it is addressed to | no |
| `effect` | what it writes — `§5` | no |
| `pinned` | never rephrase this line — `§4b` | no |
| `note` | the author's comment, read by nobody at runtime | no |

**A player line:**

```toml
[[player]]
id   = "bluff"
say  = "Command sent me. Check your board."
tag  = "lie"
then = ["believed"]
```

| field | | required |
|---|---|---|
| `id` `say` `effect` `note` | as above | `id`, `say` |
| `then` | ordered links to NPC lines | no — absent ends the conversation |
| `tag` | a **manner** tag. `§4c`'s muted grey: *nothing rolls* | no |

**⚠ `tag` is not a gate and must never be one.** `§4c` keeps `LIE` as *"available to anyone, no roll, pure tone."* A tag changes how a line reads; **a gate changes whether it is offered.** Two fields because they are two things — `TRACE-93`'s whole finding was one channel carrying several meanings.

**⚠ AND THERE IS NO `label`, `bracket` OR `prefix` FIELD. Deliberately.** `§4c`: *"ours renders from the gate field, so `[Persuade]` appears if and only if a Persuade gate exists."* `STUDY 18` measured what the alternative costs — **62% of K1's bracketed replies have no gate and 1,528 gated replies carry no bracket**, because there the bracket is literal text typed into the string. **A field an author can type is a field an author can type wrongly. There is nowhere to type it.**

---

## 4 · ⚠⚠ The gate is data, and there is nowhere to put a write

`STUDY 18 F18.01` is the finding this section exists to answer:

> Our gate is a declared predicate — **a question you may ask twice.** Their `Active` is a procedure that returns a number, and in `bastila.dlg` **eleven of eleven opening gates write to global state while deciding.**

**⚠ The requirement is that the format make that impossible, not discourage it. Three properties do it, and none of them is a convention:**

- **There is no field that can name code.** No `script`, `call`, `expr`, `condition` or resref anywhere on a link. **A gate cannot write because a gate has nowhere to put a write.**
- **The grammar is a closed vocabulary of comparisons.** A gate is a table whose keys come from the list below and nothing else. **An unknown key is a load failure, not an extension point.**
- **Every term reads a PROJECTION.** `PLAY-STATE-01`: a projection is a fold over the log. **Evaluating a fold cannot change what it folds.**

### The vocabulary

```toml
replies = [ { to = "push", gate = { skill = "persuade", dc = 14 } } ]
```

| term | reads | renders as `§4c` |
|---|---|---|
| `skill` + `dc` | a check against the eight of `§4c` | **amber** — it rolls |
| `skill` + `opposed = true` | `RULES-02 §3`'s opposed form | **amber** |
| `flag` | `quest.flag-set`, projected | invisible — it is not a check |
| `quest` + `status` | `quest.concluded` | invisible |
| `attitude` | `RULES-02 §5`'s five | invisible |
| `payment` | credits — `PT-1315` | **`[Bribe · 50 credits]`**, the one surviving number |
| `party` | is this companion with you | invisible |
| `species`, `background` | who the character **is** | **teal** |
| `alignment` | the band, derived per `ALIGNMENT-01-v2` | **teal** |
| `all_of`, `any_of` | composition, nesting arbitrarily deep — `§4b.1` | of its parts |

**Two shapes, and the second is the exception:**

```toml
[[npc]]
id  = "challenge"
say = "This deck is sealed. Turn around."
replies = [
  # ONE TERM — the common case, and it fits on the line it belongs to
  { to = "push", gate = { skill = "persuade", dc = 14 } },
  # COMPOSED — the exception. ⚠ It must fit on ONE line; see below
  { to = "name-officer", gate = { all_of = [ { flag = "spire.alarm-raised" }, { any_of = [ { skill = "persuade", dc = 14 }, { attitude = "friendly" } ] } ] } },
]
```

**⚠ The composed form is rare and the format should not be shaped around it.** `STUDY 18 R18.07` measured K2's actual gates: the four most-used conditions in the entire game are single comparisons — `c_global_eq` at 1,708 sites, `c_local_notset` at 1,489, `c_local_set` at 1,192, `c_global_gt` at 502. **A one-term gate fits on the line it belongs to; nesting is available and mostly unused.**

**⚠ AND TOML PUTS A HARD CEILING ON THE COMPOSED FORM, WHICH IS A COST OF `§8`'s CHOICE AND IS STATED RATHER THAN DISCOVERED LATER.** **An inline table cannot span lines in TOML 1.0.** A one-term gate is comfortable and a two-level gate is a long line; **past that the file stops being legible and the format is at its limit.** `§11`.

**⚠ A hoisted named-gate table (`gate = "some-name"` resolving elsewhere in the file) was considered and rejected** — it buys shorter lines at the cost of a second namespace and a second lookup. **It is the obvious answer if the ceiling above ever binds**, and it is named here so that it is a decision rather than a rediscovery.

### ⚠ `not` is proposed and is NOT in `RULES-02`

`RULES-02 §3` shows `all_of` and `any_of` and no negation. **`STUDY 18` says negation is not optional:** `c_local_notset` is K2's **second most-used condition in the game, 1,489 sites**, and `PT-1284` makes flags permanent — *"flags are never unset"* — so **"this has not happened yet" is the only way to express a thing that stops being offered.**

```toml
gate = { not = { flag = "spire.alarm-raised" } }
```

**Proposed as a fourth composition form. It is mine, it is not in `RULES-02`, and it wants an owner ruling before a package relies on it.**

---

## 5 · Effects are on NODES, never on links — and they name declared event kinds

**This is the other half of `§4`'s guarantee.** A link may not carry an effect; **the link table has no `effect` key.** A node may, because a node's effect fires **when the line plays** — once, at a moment the format names — and not while a list is being built.

```toml
[[player]]
id     = "hand-over-codes"
say    = "Take them. I was never here."
effect = [ { kind = "quest.flag-set", flag = "spire.codes-surrendered" } ]
then   = ["dismissed"]
```

**⚠ An effect names a kind from `EVENT-KINDS-01` and nothing else.** The kinds a conversation needs already exist and **no new kind is required:**

    quest.flag-set              permanent
    quest.concluded             permanent
    dialogue.node-reached       session
    dialogue.choice-made        campaign
    character.alignment-shifted permanent
    item.acquired / item.lost   campaign
    character.faction-changed   campaign

**This is `RULES-02 §3`'s `on_reveal: set_flags:` generalised** — the same idea, spelled as the ledger vocabulary the rest of the engine already uses.

**⚠ And `dialogue.node-reached` / `dialogue.choice-made` are written by the ENGINE, not by an author.** They are listed so a reader knows a conversation already logs itself; **an `effect` naming one of them is a load failure.**

---

## 6 · ⚠ Who speaks — `by`, and what it is FOR

**`STUDY 18` named this as a gap in our documents:** `Speaker` is set on **23.1% of K1 NPC lines and 25.5% of K2's**, and in `bastila.dlg` three of 26 NPC lines are spoken by Carth.

**What it is for, before proposing a field: a conversation has one owner and more than one participant.** A companion interjects; a second guard answers for the first; a prisoner speaks over their captor. **Without it, every multi-party scene has to be split into separate conversations that cannot see each other's state**, which is the shape their writers avoided by using the field a quarter of the time.

```toml
[[npc]]
id  = "carth-cuts-in"
by  = "carth"                 # a placement tag in the current area
say = "Don't. He's baiting you."
```

**⚠ `by` names a placement tag and defaults to `conversation.owner`.** It does **not** name a blueprint — `PT-1331` again: the tag is the instance's identity.

**⚠ And the format cannot say who is PRESENT.** If `by` names a tag that is not in the area, that is `PACKAGE-FORMAT-01 §6a`'s question and this document does not answer it. **Named in `§11`.**

---

## 7 · ⚠ `IsChild` gets no field, and that is a measurement rather than a judgement

**`STUDY 18` flagged it as possibly an editor artefact. It was tested rather than assumed.**

**The test:** does `IsChild` mark a link into a node that has more than one parent — i.e. a node the editor draws once and references elsewhere?

```
                              K1                    K2
IsChild on a link into a
  UNIQUELY-parented node      81 of 37,305 = 0.2%   68 of 34,459 = 0.2%
IsChild on a link into a
  multi-parent node           19,442 of 27,050      21,514 of 28,944
                              = 71.9%               = 74.3%
```

**⚠ It is a tree-display marker.** It says *"the node this points at is drawn somewhere else in the editor"* — and **whether a node has more than one parent is already computable from the links.** It carries no information the graph does not carry.

**⚠ And it is not even maintained reliably**, which is the signature of bookkeeping rather than a rule: **7,608 K1 and 7,430 K2 multi-parent links are NOT flagged**, and 81 and 68 uniquely-parented ones are.

**So: no field.** A conversation whose graph re-enters is expressed by two links naming the same id, which is what re-entrancy is.

---

## 8 · ⚠ TOML — and the tree objection dissolves rather than being overruled

**The trade is `PT-1345`'s exactly: consistency against legibility.** There, `AREA-FORMAT-01` kept the file TOML and put the one genuinely awkward structure — a 432-tile grid — into a multiline string with a legend, **because you can see the room in the diff.**

**The objection here is that a conversation is a tree and TOML has no trees.** It is a real objection to a **nested** encoding. **It does not survive `§2`.**

**⚠ Once nodes are addressed by name, the file is not a tree. It is two flat lists and a set of named edges** — and a flat list of tables is the single thing TOML's array-of-tables is best at. **The awkwardness was in the encoding, not in the subject.**

    a nested encoding    [[npc.reply.then.reply]]  — unreadable past depth 2
    a named-edge list    [[npc]] ... replies = [...]  — flat, one shape

**So: TOML, and no second notation.** Four supporting reasons:

- **Every other file in a package is TOML** — the manifest, areas, blueprints, `rules/`. `PT-1386` chose it *"precisely so an author could hand-edit."*
- **The reader exists.** Lodestar already parses TOML for areas and blueprints. **A new notation is a new parser, and `§9`'s example must be hand-writable today.**
- **`PACKAGE-FORMAT-01 §2` makes readable-in-a-diff a requirement.** One changed line is one changed line; adding a reply is three added lines and nothing renumbered.
- **⚠ The text-map argument does not transfer, and that is the honest reason.** A grid earns a custom notation because **the notation looks like the thing** — you see a corridor. **A conversation drawn as ASCII does not look like a conversation**; it looks like a flowchart with worse tooling. `PT-1345`'s test was *purpose, not letter*, and a text block here would satisfy neither.

**One file per conversation**, at `dialogue/<id>.toml`. **A blueprint names it in one line — `conversation = "dialogue/trooper-challenge"` — and that one line is an addition to the creature blueprint, flagged in `§11`.**

---

## 9 · A worked example

**`dialogue/trooper-challenge.toml`** — for the Sith trooper Loom placed on the Command Deck at `PT-1425`. **Original text, ours. Small on purpose.**

```toml
[conversation]
id    = "trooper-challenge"
owner = "sith-trooper.command-deck.07"

[[npc]]
id      = "challenge"
say     = "This deck is sealed. Turn around."
replies = [
  "bluff",
  { to = "flash-rank",  gate = { background = "republic-officer" } },
  { to = "buy-passage", gate = { payment = 50 } },
  { to = "push",        gate = { skill = "persuade", dc = 14 } },
  "back-off",
]

[[player]]
id   = "bluff"
say  = "Command sent me. Check your board."
tag  = "lie"
then = ["not-on-my-board"]

[[player]]
id   = "flash-rank"
say  = "You are speaking to a commissioned officer."
then = ["stands-down"]

[[player]]
id     = "buy-passage"
say    = "Fifty credits says you saw nobody."
effect = [ { kind = "item.lost", item = "credits", count = 50 } ]
then   = ["stands-down"]

[[player]]
id   = "push"
say  = "You are one man on a dying ship. Move."
then = [
  { to = "stands-down", gate = { skill = "persuade", dc = 14 } },
  "not-on-my-board",
]

[[player]]
id   = "back-off"
say  = "My mistake."

[[npc]]
id      = "not-on-my-board"
say     = "My board says otherwise. Last warning."
replies = ["back-off", "push"]

[[npc]]
id      = "stands-down"
say     = "…Go. I saw nothing."
effect  = [ { kind = "quest.flag-set", flag = "spire.trooper-passed" } ]

[[npc]]
id  = "carth-cuts-in"
by  = "carth.command-deck.01"
say = "Don't push him. He is looking for a reason."
```

**⚠ Six things in the example are the format's whole argument:**

- **`push` is reachable from two places** (`challenge` and `not-on-my-board`) — two links naming one id. **That is `§7`'s re-entrancy, with no `IsChild`.**
- **`push`'s check is on its OUTBOUND link, not on the node.** The reply is always offered; **the roll decides where it goes**, and failure lands on `not-on-my-board`. `§4c`: *a pass and a fail are already different nodes.*
- **`flash-rank` is teal and `buy-passage` shows a price**, both derived from the gate — **no author typed a bracket.**
- **`bluff` carries `tag = "lie"` and no gate at all.** Grey, nothing rolls, available to anyone.
- **`back-off` has no `then`.** The conversation ends. **Absence is the terminal, not a field.**
- **`carth-cuts-in` is unreachable as written**, and the format does not care. **A validator should.** `§11`.

---

## 10 · What is NOT in a conversation

**No camera, emotion, facial animation, animation list, fade, stunt model or cutscene flag.** `PT-1319` removed the render layer; `STUDY 18` measured what that deletes — **about forty of K2's forty-eight node fields**, plus most of the top level.

**No VO.** `VO_ResRef` is on 77% of K1 nodes. **We have no recorded lines**, and a field for a thing nothing reads is `AREA-FORMAT-01 §5`'s own rule.

**No scripts, inline or referenced.** `§4` and `§5` are the whole of what a conversation may cause.

**⚠ No runtime state.** No visited flag, no ask counter, no "already said this". **`PLAY-STATE-01`: state is a projection of the log.** A conversation file is authored content and never changes.

**⚠ This is the rule most likely to be broken first**, and `STUDY 18` found where: `bastila.dlg` puts *"has this been said"* inside the gate that decides whether to say it. **The temptation is real, it shipped in a real game, and the format's answer is that a gate has nowhere to write.**

**No topic space, no facts, no deflection stances.** Those are `ENGINE-SPEC-03 §3` and `RULES-02 §3`, they belong to the character, and **a generated NPC has no file here at all.**

---

## 11 · ⚠⚠ What this format CANNOT express

**Named now because every format so far has had something, and finding it in the first package is more expensive.**

- **⚠ A flag cannot be un-set.** `PT-1284`: *"flags are never unset."* So a conversation cannot return to an earlier state — **only `§4`'s proposed `not` can express "not yet", and once a flag is set that door is shut for the campaign.** Their writers reset globals from inside conditionals; we cannot, by two separate rules.
- **⚠ "The third time you ask" is not in the file.** `PT-1316` makes escalation **per conversation, per topic, derived and never stored**. The file has no counter and no place for one. **A line that should read differently on a repeat cannot say so** — the engine varies tone, the author does not author it.
- **No priority between links.** If two gates both pass, the earlier wins and there is no way to say otherwise. **Same as theirs** — `STUDY 18 R18.02`, no ordering field exists in either game. It is a limit, not an oversight.
- **No stage directions.** `§4c` records them as *"confirmed real, confirmed needed, nothing built"* with **no slot**. This format inherits that and **does not invent one** — a non-verbal beat has nowhere to go.
- **No timing.** No pause, no beat, no `Delay`. Removed with the render layer, but **a beat is not purely visual** and this is the one deletion that may want revisiting.
- **⚠ No cross-conversation link.** `then` and `replies` name ids **in this file only**. A conversation cannot hand off to another. **Theirs cannot either** — a `.dlg` is closed — so this is inherited rather than chosen, and it is the first thing a large package will ask for.
- **Nothing about who is PRESENT.** `by` names a tag; whether that tag is in the area is not the file's business and no rule says what happens when it is not. **`PACKAGE-FORMAT-01 §6a` distinguishes a missing asset from a missing dependency and does not cover this case.**
- **`pinned` is per line, not per character.** `§4b` says *"pinned inverts from exception to default for canonical characters"* — **the file cannot say that.** It is a blueprint property and the blueprint has no field for it.
- **No XP.** `PlotXPPercentage` is on their nodes; **whether a conversation awards XP in our design is not ruled anywhere I could find.**
- **⚠ A gate nested more than two deep.** **TOML inline tables cannot span lines**, so a composed gate is one line however long it gets. `§4`'s measurement says one-term gates are the overwhelming case and this may never bind — **but it is a limit of the file, not of `§4b`'s schema, which nests arbitrarily deep.** The escape is `§4`'s rejected hoisted-gate table.
- **A validator is assumed and not specified.** Unreachable nodes, links naming a missing id, an alternation violation, an unknown gate key, an `effect` naming an engine-written kind — **all detectable, none specified here.** `§9`'s `carth-cuts-in` is deliberately left unreachable to make the point.

---

## 12 · Open

- **`not` as a gate form.** `§4`. **Proposed by me, not in `RULES-02`, and wanted before a package relies on it.**
- **`conversation = "dialogue/<id>"` on a creature blueprint.** One line, and it belongs to the blueprint's format rather than this one. **Flagged, not added.**
- **`RULES-02 §3`'s examples are pre-conversion.** They read `payment: 50gp` and `skill: diplomacy`; ours are **credits** and the eight skills of `§4c`. **The SHAPE is what this document adopts. The example values are stale and are not corrected here** — that is a document change and an owner's call.
- **`ENGINE-SPEC-03 §4c` still carries a superseded block.** `STUDY 18 F18.06`: the `PT-1306` two-stage reveal with `[Persuade DC 14]` and a greyed `[Slicing DC 18]` sits below `PT-1307`'s *"NO NUMBERS ANYWHERE"* and is not marked superseded. **This document follows `PT-1307`.** If that is wrong, `§3`'s no-`label` rule and `§4`'s render column both change.
- **⚠ `TRACE-112` COULD NOT BE READ AND IS NOT REFLECTED HERE.** The brief cites it as having *"just gave it more than most formats start with."* **The corpus I can read ends at `TRACE-111`** (`PLAYTEST-RULINGS-01.md`, newest ruling `PT-1426`). **This document is built from `ENGINE-SPEC-03`, `RULES-02`, `PACKAGE-FORMAT-01`, `AREA-FORMAT-01` and `STUDY 18`, all of which were available.** The one decision it could plausibly move is **`§8`'s serialisation choice**; nothing in `§1`–`§7` depends on it.
- **Whether a conversation may be attached to something other than a creature** — a door, a terminal, a placeable. **Their `ConversationType` and `ComputerType` fields say theirs could.**
