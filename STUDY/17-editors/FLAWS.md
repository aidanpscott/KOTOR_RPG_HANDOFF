# STUDY 17 — judgement

Records in `RECORDS.md`, cited by number.

---

## F17.01 · `STUDY 12`'s guess was right, and one correction matters

**Confirmed: Aurora has three editing surfaces and everything else is a dialog**
(`R17.01`, `R17.02`). Three forms score above 30 and the fourth scores 13.

**⚠ The correction: the third is not the area viewer. It is `TfrmFrame` itself.**

`STUDY 12` said "77 dialogs, 15 frames, one genuine second window, and a
conversation editor". Read as *which windows exist* that is right; read as
*which surfaces you dwell in* it misses that **the main window is one of the
three** — and the one with the most of everything: 59 actions, five toolbars, a
status bar, four splitters, and five document actions.

**The three, and what each is the editor OF:**

| surface | the document | evidence |
|---|---|---|
| `TfrmFrame` | **the module** | New · Open · Save · Save As · Close |
| `TdlgConversationEditor` | **a conversation** | all seven, incl. Save All and Quit |
| `TdlgScriptEditor` | **a script** | six of seven, and no dismissal button |

**⚠ And the area viewer is NOT one of them** (`R17.05`) — no splitter, no status
bar, **no document lifecycle**. It is a *view inside* the module's editor, which
is why it is `bsNone` and parented into `pArea`.

## F17.02 · ⚠ The line is the document lifecycle, not the furniture

**The test you asked for, and the data gives a sharper one than "dwell versus
errand".**

> **A surface is an editor if the thing in it can be created, saved and closed
> independently. Everything else is a dialog, however elaborate.**

**Two forms prove it is not about richness:**

- **`TdlgTriggerEdit`** (`R17.07`) has **four splitters, six tabs and a status
  bar** — more furniture than the script editor — and is `bsDialog` with
  OK/Cancel and **zero actions.** A trigger is not a document; it is a property
  sheet on something that lives in an area.
- **`TdlgJournalEditor` and `TdlgFactionEditor`** are *named* editors and both
  dismiss with **OK/Cancel** and own **no document action** (`R17.06`).

**⚠ So Aurora draws the line twice, not once.** `TRACE-104` found it drawn at
properties — no inspector, properties are dialogs. This study finds the same
line drawn at **journal, faction and trigger**, which are the cases most likely
to have been given a pane by a careless designer. **Aurora refused each time.**

**And it explains the "Done" button.** The conversation editor dismisses with a
single `ModalResult` (`R17.03`) — it *is* a place you leave, and it still owns
its documents. **Owning a lifecycle and being dismissible are independent**, and
conflating them is what made me hedge on modality in `STUDY 12`.

## F17.03 · What the area surface actually holds, and one thing I did not expect

**`R17.05` fills the gap `STUDY 12` left.** Beyond the canvas: **a console with
a command box and a response box**, eleven camera buttons plus three
object-rotation buttons, **its own `TMainMenu` carrying Edit ▸ Undo**, and 32
context actions on a selected instance.

**⚠ Three of those are load-bearing for us.**

- **The 32 actions are almost entirely a right-click menu on a placed thing** —
  Properties, Delete, Adjust Location, Variables, Edit Inventory, Edit
  Conversation, Add to Palette, and animation states for doors, placeables and
  sounds. **That is what "editing an area" mostly IS**: not painting, but acting
  on what you placed. Our `4d` has none of it because nothing is placed.
- **`Add to Palette` appears here as well as in the tree** (`STUDY 16`). **Two
  routes into the palette, both from a thing that exists.**
- **⚠ The camera controls are one of the toggleable Interface Panels**, driven
  by `actShowPaneVisualCameraControls` from the main window. **A pane inside a
  pane**, and the outer window owns its visibility.

**The console I would not copy.** It is a developer affordance from a 3D engine
and `PT-1319` removed the render layer it belongs to.

## F17.04 · Our five, judged one at a time

**Aurora's own answer for each, then ours.**

| ours | Aurora's counterpart | verdict |
|---|---|---|
| **quests** | `TdlgJournalEditor`, **a dialog** with OK/Cancel (`R17.06`) | **DIALOG.** Aurora put its journal behind `Tools` and refused it a pane |
| **the manifest** | scattered across `TfrmIFOProp`'s five tabs, **a dialog** | **DIALOG** — package properties, which `STUDY 16` already placed there |
| **tilesets** | **none. Picked, never edited** (`R17.08`) | **NOTHING in Loom.** A tileset is authored elsewhere and selected here |
| **strings** | TLK is a combo box in module properties | **NOTHING yet.** Aurora edited TLKs in a separate program |
| **rules** | ⚠ **nothing at all — not one form mentions 2DA** | **NOTHING yet, and this is the one to watch** |

**⚠ `rules/` is the folder KOTOR does not have** — `PACKAGE-FORMAT-01 §3` says
so explicitly, and `TRACE-82` found no module-local rules table in either game.
**So there is no precedent to copy, in either direction.** Aurora's silence here
is not a judgement that rules need no surface; it is that Aurora had no such
thing to give one to.

**None of the five earns a tab.** Four are dialogs or nothing; the fifth is
unprecedented and unbuilt.

## F17.05 · ⚠ THE ANSWER: four tabs, and three of them come straight from Aurora

> **Packages · Area · Conversation · Script.**

**Argued from what Aurora dwells in rather than from what toolsets have:**

- **Conversation and Script are Aurora's own two document editors** (`F17.01`),
  and both are things you come back to with your place kept. **Direct copies.**
- **Area is ours where Aurora's was a view.** Aurora's area viewer owns no
  lifecycle because the *module* is the document and an area is part of it.
  **Ours is genuinely a file** — `areas/a01-x.toml`, opened, edited and saved on
  its own — so it earns what Aurora's did not. **A departure, and a justified
  one.**
- **Packages is ours because Aurora had one module and we have a library.**
  Aurora asked "which module" once, in a modal, at launch (`TRACE-106`); with
  nothing open its main window was simply empty. **We have Console Home listing
  many packages, so "which package" recurs** — and `PT-1356` already ruled the
  picker a pane rather than a modal.

**Nothing in `F17.04` adds a fifth.** Quests and the manifest are dialogs by
Aurora's own repeated refusal; tilesets and strings are picked, not edited; rules
have no precedent and no caller.

### ⚠ One honest departure inside the ruling

**`PT-1375` says one tab per KIND, with the tree selecting within it. That is not
Aurora's shape.**

Aurora is **one WINDOW per kind, containing one TAB per open thing** — the
conversation editor's `pcMainText` had per-conversation tabs from the start
(`R17.03`), and Beamdog added per-area tabs in 2018 (`R17.09`).

**Ours collapses Aurora's window layer into a tab and drops its per-thing tabs.**
That follows from `PT-1340`'s one window, and it is coherent. **But it means the
tree is doing a job Aurora gave to tabs**, and the thing to watch is the case
Aurora's design handles and ours does not: **two conversations open at once,
compared side by side or copied between.** Aurora's `Paste As Link` and
`Find In Files` both assume you are moving between conversations.

**I am not proposing a change.** I am recording that the one place our model is
thinner than Aurora's is switching between two things of the same kind, and that
`STUDY 14` found Aurora's answer to that was a tab.
