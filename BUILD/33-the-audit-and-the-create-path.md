# 33 · The audit, and Loom authors a conversation

**258 Lodestar · 206 app · 110 Loom · 4 Lens.** All analyze clean. **Captures
re-taken against the conversation Loom made.**

---

## 1 · ⚠ The audit — every file in the bed, and which Loom action made it

**Five files. Four were the Builder's; one was not, and it is the one already
known.**

| file | the action that made it |
|---|---|
| `package.toml` `[package] id/name/version` | **New Package** |
| `package.toml` `authors` · `summary` | **Package Properties** |
| `package.toml` `[order] areas` | **New Area** (appends as it writes the area) |
| `package.toml` `[entry] area` | **the entry verb** — `PT-1380` |
| `areas/a01…` `a02…` `[area] name/size/tileset` | **New Area** |
| `[tiles] legend` + `map` | **painting squares** — `TilesWriter` |
| `[[connections]]` | **placing a doorway** on the grid |
| `[[arrivals]]` | **placing an arrival point** on the grid |
| `[[contents]]` + `tag_seq` | **placing the creature** by clicking a square |
| `blueprints/characters/sith-trooper.toml` | **New Creature** |
| `dialogue/trooper-challenge.toml` | ⚠ **hand-written at `BUILD/30`** — and **now the conversation editor**, `§2` |

**⚠ So the answer is: only the conversation, and the audit was cheap.** Nothing
else reached the bed without a Builder action.

### ⚠⚠ But the other direction found four more, and that is the sharper rule

> **Anything the Builder cannot write, the Builder eventually destroys.**

**Fields the readers READ and Loom cannot WRITE:**

| field | read by | |
|---|---|---|
| `[requires]` | `package_open` | **⚠ `new_package.dart` says in a comment that it *"belongs in package properties"* — and properties does not offer it.** A dependency is unwritable. |
| `[continues]` | `package_open` | Never mentioned anywhere in Loom. `CANON-01 v2`'s cross-campaign carry has no way in. |
| `[character] equipment` | `character_open` | Eleven slots read; no field, no dialog, nothing. |
| `[character] attachments.doctrine` | `character_open` | **⚠ And this one has teeth: `PT-1423` built the doctrine layer and the play screen still fights with a hardcoded `plainAggression` fixture** — because no authored creature can carry a doctrine. |
| `[character] attachments.reaction` | `character_open` | Same section, same absence. |

**And one weaker variant, worth separating:** `[[connections]] from` — the
optional door template of `AREA-FORMAT-01 §4a` — **is written by
`ConnectionWriter` and never offered by the place-way dialog.** The writer can;
the UI cannot ask. **Not a destroy risk today** (the writer omits it rather than
clobbering it), but it is the same gap one step earlier.

**⚠ Every one of these is the erased-`conversation`-line defect waiting.**
Reported, not fixed — each is its own piece of Builder work.

---

## 2 · Loom authors a conversation from nothing

**`BUILD/31` regenerated a file the reader had produced.** That proves a file
survives a read and a write. **It does not prove anything can be made**, and
**only the second is what `PT-1346` is for.** I reported the debt as paid and
it was not.

**`ConversationDraft`** holds editable state and assembles **the same immutable
types the reader produces** — nothing in Loom parses, and the reader keeps its
monopoly on meaning.

**The create path, every verb a button:** new conversation (name + owner) ·
`+ line` · `+ reply` · `link` to an existing id · a **gate chosen from
`gateKeys`** and filled in · `effect` · `tag`.

**⚠ THERE IS NO BOX YOU CAN TYPE A GATE INTO**, for the same reason there is no
`label` field: `§4`'s vocabulary is closed, and a free-text gate is an
extension point by another name.

**⚠ And the bed's conversation is deleted and made again by clicking** —
including the node whose only effect is `encounter.began`, so **`PT-1437`'s
fight is reachable through the create path.** The re-entrant link is authored
too, with the `link` verb: **two links naming one id**, which is `STUDY 12`'s
finding and the only thing a DAG can be here.

**The app's 206 tests pass against the conversation Loom made**, and the
captures were re-taken from it: `[Lie]` `[Persuade]` `[Human]`
`[Bribe · 50 credits]`.

---

## 3 · ⚠ Four defects found on the way, and three are the viewport pass again

- **⚠ An async read in `initState` hung a widget test for ten minutes.** The
  same hazard this project has paid for before. **The tab reads synchronously
  now** — `parseConversation` is the same function `openConversation` calls;
  only the bytes arrive by a different road.
- **A tree row overflowed its pane by 48px** the moment `conversations` got a
  `+`. A tree row is as wide as the pane, never as wide as its words.
- **Every fixed `Row` in the editor overflowed when the pane is narrow.** They
  wrap.
- **⚠ Two test files shared the bed's conversation while `flutter test` runs
  files in parallel.** The author test deletes it; the tab test read it. **The
  failure looked like a layout bug for two runs.** The tab test has its own
  fixture now.

---

## 4 · Not done

**Not the side panel** — that is a design decision and this was a correctness
one. **And the five unwritable fields in `§1` are reported, not built.**
