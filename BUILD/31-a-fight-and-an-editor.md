# 31 · `PT-1437`, and the Builder's conversation editor

**258 Lodestar · 204 app · 108 Loom.** All three analyze clean.

---

## 1 · A conversation may end in a fight

**No new kind, and no reader change either** — `encounter.began` was already
declared, already campaign, and **already not in `engineWrittenKinds`**, so an
effect naming it was legal the moment the permission existed. `PT-1418`'s
checks are untouched, and there is a test asserting the forbidden set is still
exactly two.

**`Beat.startsFight` is DERIVED from the events**, not a second field. **The
effect IS the fact**; a flag an author could set separately would be a second
channel that could disagree with the first.

**In the bed:** `[[player]] shove-past` → `[[npc]] opens-fire`, whose only
effect is `encounter.began`. **The trooper who tells you to turn around and
shoots when you do not is one node with one effect**, and the path is walked by
three tests rather than asserted.

### ⚠ The placeholder is gone, and one new rule took its place

`PT-1436`'s *talk-first-fight-after* made **hostility a function of whether a
file exists**. **Removed.** A creature with a conversation is always spoken to,
and the fight starts when the conversation says so.

**⚠ And a rule the removal made necessary, which is NOT the placeholder
returning: once a node has fired `encounter.began`, that creature no longer
talks.** Re-opening its tree would **undo the outcome the author wrote.** It is
a function of *what the conversation did*, not of what files exist.

**⚠ A test found it, not reasoning.** `wound_survives` kept walking back into a
trooper it had already fought and getting the conversation again, so the walk
to the door never happened. **The test was right and the app was wrong.**

---

## 2 · The Builder's conversation editor — the `PT-1346` debt, paid

**`BUILD/30` said the Builder owed one. The next Loom run said why:** the
creature dialog rewrote the trooper's blueprint and **silently erased the
hand-added `conversation` line.**

> **Anything the Builder cannot write, the Builder eventually destroys.**

**Three pieces, and the shape is `STUDY 14`'s rather than invented:**

- **`ConversationWriter`** renders a `Conversation` the reader produced. **It
  never parses** — the reader is still the only thing that decides what the
  format means — and a file it writes is read back by `parseConversation` like
  any other. **A gate goes on one line, because `§4`'s stated ceiling is that
  TOML inline tables cannot span lines**; a writer that wrapped one would emit
  a file it could not read back.
- **`ConversationTab`** is **master over detail** — a tree over a detail panel.
  **`STUDY 12` found the tree is a plain `TreeView`, not a node graph**, so a
  node reached twice is **drawn twice and the second is marked** — Aurora's
  *Paste As Link*, and ours is two links naming one id. **The validator's
  findings are on screen**, because `PT-1379`'s principle is that Loom must not
  be able to create the fault it detects, and one it detects and hides is the
  same thing.
- **The creature dialog carries `conversation`**, on its own row — a package
  path is long and the three fields it first shared a row with are short.

**⚠ AND THE BED'S CONVERSATION IS LOOM'S OUTPUT NOW.** `bed_creature_test`
writes it on every run, so the file begins *"# Written by Loom"* and **the line
saying it was hand-written is gone.** The tab is reachable: conversations are
listed under the tree's own `conversations` row, **which had a name and nothing
under it.**

**⚠ One cost of a generated file, stated:** regenerating loses hand comments.
`DIALOGUE-FORMAT-01` has a per-line `note` for that, and **file-level
commentary has nowhere to go** — the PT-1437 explanation that was in the file
now lives only here.

---

## 3 · ⚠ Two things found on the way, both reported

- **⚠ A CLICK ON AN OPTION BELOW THE FOLD LANDS ON A DIFFERENT REPLY.** With
  five options the last sit under the panel's half-height cap, and a tap on a
  clipped row hits **whatever is at that point.** In the test it silently chose
  `push` instead of `shove-past`. **This is `BUILD/30`'s coverage finding with
  teeth** — it is no longer only that you cannot read an option, it is that you
  can pick the wrong one. **Not fixed: it wants the real viewport
  `UI-STYLE-VALUES-01 §7` asks for.**
- **⚠ THE CONVERSATION'S `owner` IS STALE AND NOTHING NOTICED.** It names
  `sith-trooper.command-deck.07`; Loom's own bed test has re-placed the trooper
  and the tag is now `.16`. **The validator lists speaker tags as `unchecked`**
  — `§11` records that checking one needs the area — **and this is that gap
  happening.** Nothing used `owner`, so nothing broke; a screen that trusted it
  would have.

---

## 4 · Still open, and not this slice

**The panel's top edge cuts the row the speaker is standing in.** Confirmed by
looking, carried forward.

## 5 · Not built

No AI, no escalation, no character brain. **The editor opens, shows and writes;
it does not create or delete a node.**
