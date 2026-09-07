# STUDY 17 — which editors Aurora has, and which we need

`PT-1375` rules one tab per kind — **Packages · Area · Conversation · Script** —
and four was a guess about how many kinds of thing need an editing surface.

**The guess is right. Here is why, from the binary.**

---

## The measurement

Every one of 105 forms scored on what marks a dwelling-place. **Three forms score
above 30; the fourth scores 13.**

```
TfrmFrame                45      the MODULE
TdlgConversationEditor   35      a CONVERSATION
TdlgScriptEditor         30      a SCRIPT
──────────────── a gap of 17 ────────────────
TdlgTriggerEdit          13      …and it is a dialog
```

## ⚠ The line is the document lifecycle

> **A surface is an editor if the thing in it can be created, saved and closed
> independently. Everything else is a dialog, however elaborate.**

**Only three forms in 105 own `New`/`Open`/`Save`/`Close` actions.** And richness
proves nothing: `TdlgTriggerEdit` has **four splitters, six tabs and a status
bar** — more furniture than the script editor — and is `bsDialog` with OK/Cancel
and zero actions.

**Aurora draws this line three more times than `TRACE-104` found.** The journal
and faction "editors" both dismiss with OK/Cancel and own no document action.
**Every case most likely to be given a pane by a careless designer, Aurora
refused.**

## The correction to STUDY 12

`STUDY 12` counted windows. Counting *surfaces*, **the third is `TfrmFrame`
itself** — 59 actions, five toolbars, four splitters — and **the area viewer is
not one of them**. It has no splitter, no status bar and no lifecycle: it is a
view *inside* the module's editor, which is why it is `bsNone`.

## What the area viewer actually holds

`STUDY 12` left this blank. Beyond the canvas: **a console with a command box
and a response box**, eleven camera buttons, three object-rotation buttons, **its
own menu carrying Edit ▸ Undo**, and **32 context actions on a selected
instance** — Properties, Delete, Adjust Location, Variables, Edit Inventory,
Edit Conversation, Add to Palette, and animation states for doors, placeables
and sounds.

**⚠ That is what editing an area mostly IS** — not painting, but acting on what
you placed.

## Our five, and none of them earns a tab

| | Aurora | verdict |
|---|---|---|
| quests | journal is a **dialog**, behind Tools | **dialog** |
| the manifest | module properties, a **dialog** | **dialog** |
| tilesets | **picked, never edited** | **nothing in Loom** |
| strings | TLK is a combo box | **nothing yet** |
| rules | ⚠ **not one form mentions 2DA** | **nothing yet — no precedent either way** |

## The answer

**Four: Packages · Area · Conversation · Script.**

Conversation and Script are Aurora's own two document editors, copied. **Area is
ours where Aurora's was a view** — ours is genuinely a file, so it earns what
Aurora's did not. **Packages is ours because Aurora had one module and we have a
library.**

**⚠ One honest departure:** Aurora is *one window per kind containing one tab per
open thing*. Ours collapses the window into a tab and drops the per-thing tabs,
which follows from one-window but leaves us thinner in exactly one place —
**two conversations open at once**, which Aurora's `Paste As Link` and
`Find In Files` both assume.

## Reading order

- **`RECORDS.md`** — description only, `R17.01`–`R17.09`.
- **`FLAWS.md`** — judgement, `F17.01`–`F17.05`.

## ⚠ Scope

Binary inspection of Beamdog EE `1.5.0.5`, 105 parsed DFM streams, plus the
shipped changelogs for `R17.09`. **The toolset was not run.** The scoring in
`R17.01` is my own construction; the document-lifecycle count in `R17.02` is a
direct reading of action names and is what the conclusion actually rests on.
