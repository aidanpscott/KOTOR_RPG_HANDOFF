# STUDY 12 — judgement

Records are in `RECORDS.md` and are cited by number. This file judges; it does
not describe.

---

## F12.01 · Your model of Aurora is wrong in one specific, decision-relevant way

You expected: *"a main window with a module tree, a 2D area painter, property
inspectors, a conversation editor, a script editor."*

Four of those five are right. **The property inspector is not.** There is no
inspector pane anywhere in Aurora. The right-hand pane is the **palette** — the
thing you paint *from* — and object properties live in **modal dialogs you open,
change, and close** (`R12.05`, `R12.08`, `R12.10`).

That single correction reshapes the question you are asking. A property
inspector is the classic argument *for* a second window or a persistent dock:
you want it visible while you work. Aurora never had one. It answered "edit this
object's properties" with a dialog, and it was still the most accessible
authoring tool of its generation.

## F12.02 · Aurora is not a multi-window application, and never was

`FormStyle` has no `fsMDIForm` and no `fsMDIChild` in any of 105 forms
(`R12.03`). There is no MDI frame, no child-window tiling, no window list. The
`&Window` menu exists, is **empty**, and is **`Visible = False`**.

What actually exists:

- **one main window** with three docked panes and three draggable splitters
  (`R12.05`)
- **77 dialogs**, at least 48 of which dismiss with a `ModalResult` (`R12.08`)
- **15 frames** — objects that by their VCL type *cannot* be windows (`R12.02`)
- **five floating helpers**, all of them lookups or monitors, none an authoring
  surface (`R12.04`)
- **one genuine second window**: the Script Editor (`R12.08`)

The count that matters: of Aurora's authoring surfaces, **exactly one** is a
real, non-modal, minimisable second window.

## F12.03 · The window inventory, judged one at a time

The brief asked for a judgement per window, not a list. Grouped by verdict.

### Already a pane — the question does not arise

| surface | evidence | note |
|---|---|---|
| Module contents tree | `TfraMainInventory`, `alLeft` in `TfrmFrame` | a `TFrame`; cannot be a window |
| Palette | `TfraMainPalette`, `alRight` | a `TFrame` |
| Plot manager | `TfraPlotManager` inside the palette | a frame in a frame |
| Message log | `TMemo` in `pBottom`, `alBottom` | |
| Area canvas | `TfrmViewerArea`, `bsNone`, into empty `pArea` | a form *made* into a pane |
| Conversation tree | `TfraConversationTree` | a `TFrame` |
| The 9 `Tfra*Situated*` property pages | frames on tab sheets | |

Seven of Aurora's most-used surfaces are already panes. **This is the majority
of the time a module author spends.**

### Would have been *better* as a pane

**The Script Editor** (`TdlgScriptEditor`, 760×540, non-modal, min+max+help,
contains a splitter). Today this is the one real second window, and it is the
one case where a second window earns its keep: you write a script *about* the
thing you selected in the area, and wanting both visible is legitimate.

But a dockable pane or a tab would serve identically — and Beamdog's own
direction of travel (`R12.13`) is toward tabs, not windows.

**Verdict: a pane would have served, and better.**

### Genuinely wants to be its own window

**Nothing, with one honest partial.**

The **Conversation Editor** is 939×660, has its own 32-verb action list, its own
New/Open/Save/Save All/Close/Quit document lifecycle, its own Find In Files, its
own import/export, and its own status bar (`R12.09`). It is a second application
wearing the toolset's process.

That is a real argument for a separate window. But note what Aurora actually
did: it gave it a **single button captioned "Done" with `ModalResult = 1`**
(`R12.08`). Aurora's own answer was "this is a place you go, finish, and leave" —
a mode, not a companion view. **A full-window tab would express that identically.**

### Correctly a dialog, and no argument otherwise

All 18 wizards, all 18 object editors, the faction editor, the journal editor,
inventory, portrait/loadscreen/token/faction pickers, options, verify, import
and export (`R12.08`, `R12.10`). Seventy-odd forms whose entire job is *ask a
question, return an answer*.

### Correctly floating

`TfrmPreview` and `TfrmObjectList` (`R12.04`) — small, `fsStayOnTop`, monitors
rather than editors. Both would also work as collapsible panes.

### Not windows at all

`nwhak.exe` and `GFFEditor.exe` are **separate executables** (`R12.12`). When
BioWare hit something that genuinely did not belong in the toolset's window,
they did not open a second window — **they shipped a second program.**

## F12.04 · The conversation editor is the one that should worry you, and it is a tab

`TRACE-87` says dialogue carries more attachment points than every object hook
in the game combined. Aurora's presentation of that is worth copying and worth
improving on.

**What it did:** a plain `TTreeView`, `alClient`, filling the top half; a
vertical splitter; a three-tab detail panel (Data, Bookmarks, Search) filling the
bottom half (`R12.09`). Master over detail, one window, resizable divider.

**What it did not do:** a node graph, a canvas, a second window per
conversation. Branching is expressed by tree indentation, and the DAG — the same
reply reachable from several places — is expressed by a context-menu verb,
**`Paste As Link`**.

**The structural point for us:** `pcMainText` is a `TPageControl` holding one tab
per open conversation. **Aurora's own answer to "I need two conversations at
once" was a tab, inside one window.** It did not open a second window even for
its single largest authoring surface.

## F12.05 · ⚠ THE JUDGEMENT YOU ASKED FOR: the accessibility had nothing to do with multi-window

**Say it plainly, because you asked for it plainly: no, it was not the window
arrangement. There was barely any window arrangement to speak of.**

Aurora was one window with three panes and a pile of modal dialogs. Anyone
remembering it as a rich multi-window environment is remembering a tool that
does not exist. The evidence is `R12.03` — no MDI, no window list, an empty
hidden `&Window` menu — and `R12.02`: fifteen of its UI units are frames that
*cannot* be windows.

What made it accessible is visible in the binary, and it is three things:

**1 · There are no verbs to learn.** This is the strongest finding in the study.
The complete main toolbar set is File, camera, a **two-state** Terrain/Objects
toggle, visibility filters, and render toggles. **Not one button in the main
window creates anything** (`R12.10`). Compare any 3D tool of the era, or any
today: a tool palette of fifteen verbs is the standard barrier. Aurora's verb
count for placing content is effectively **one**: pick a thing from the palette,
put it in the area. `TRACE-16` called this the one-verb Paint model; the toolbar
inventory is independent confirmation, because the alternative would have left
buttons behind and there are none.

**2 · Everything you can make is enumerated in front of you.** The palette is a
permanent, resizable, always-visible pane holding a tree of every blueprint,
split Standard/Custom (`R12.11`). You do not have to know what exists. The tool
shows you, and the answer to "how do I add a goblin" is "find the goblin".

**3 · The hard parts are wizards, not blank forms.** 18 wizard forms
(`R12.10`) — one per object type, plus Module, Area and Plot. A beginner never
faces an empty property sheet; they answer questions. The 240 tab sheets
(`R12.07`) are where the depth lives, and a beginner never has to open them.

**None of these three is a window-arrangement property.** Every one of them
would survive being ported to a single window with docked panes. Every one of
them would also survive being ported to a multi-window shell. **The variable is
independent of the thing you are deciding.**

## F12.06 · What this means for the decision, stated as narrowly as the evidence allows

You are weighing a multi-window Builder against a single window with docked
panes, and asking whether to pay Flutter's main-channel stability cost.

**On the evidence in this study, Aurora does not justify that payment.**

- The tool everyone remembers as accessible **was the docked-pane design**
  (`R12.05`). Not a compromise version of it — that *was* it.
- Its own vocabulary for those regions is **"Interface Panels"** (`R12.06`).
- Its one true second window is the Script Editor, and a pane serves that better
  (`F12.03`).
- Its largest authoring surface chose **tabs in one window** over a second
  window (`F12.04`).
- Its maintainers, with two decades of hindsight and user feedback, added **area
  tabs** — not area windows (`R12.13`).
- When something genuinely did not fit, the answer was **a separate program**,
  not a second window (`R12.12`).

**⚠ The honest limit of that conclusion.** This study establishes that
multi-window was not the source of Aurora's accessibility, and that Aurora
itself did not need it. It does **not** establish that *our* Builder will not
want a second window for something Aurora never attempted. A detached preview on
a second monitor is a 2026 expectation that a 2002 tool had no reason to have,
and no amount of reading `nwtoolset.exe` will tell you whether your authors want
one.

What it does tell you is that **the second window is not on the critical path to
accessibility**, so it should not be bought early, and certainly not by taking a
dependency on an unreleased channel. Ship the panes. If a second window is still
wanted once real authors are using it, buy it then, when the feature has left
experimental and the cost is a version bump instead of a channel switch.

## F12.07 · One thing worth stealing that has nothing to do with windows

`TfrmFrame` drives its entire UI through a **59-action `TActionList`**, with menu
items and toolbar buttons bound to `TAction` objects rather than carrying their
own handlers (`R12.05`, `R12.10`). Enable/disable, caption, hint, shortcut and
icon all live on the action; the menu and the toolbar are two views of it.

That is why `View → Toolbars` and `View → Interface Panels` are cheap, and why
the same verb appears in a menu, a toolbar and a context menu without
duplication. It is a command-registry pattern, it is orthogonal to window
arrangement, and it is the part of Aurora's architecture I would copy first.

---

## Judgements about our own design, kept separate

**On the spike's finding.** My spike proved Flutter's stable channel cannot open
a second native window. This study says that constraint is **not binding on the
design Aurora validates**. The two findings agree: build the single window with
docked panes, and the Flutter limitation costs nothing we can currently show a
need for.

**On the conversation editor specifically.** Ours is the biggest surface we have
and Aurora's is a tree over a tab strip. That is a floor, not a ceiling. I would
copy the master-detail split and the `Paste As Link` idea for expressing a DAG,
and I would not copy the modal "Done" — a full-window tab expresses the same
"go here, finish, come back" without freezing the rest of the tool.

**A caution I want on the record.** Everything here describes a **2026 Beamdog
build** (`R12.01`). The forms are plainly inherited from BioWare, but I cannot
separate original from modified, and I said so at every point where it mattered
rather than at the end. If this decision is going to lean hard on "Aurora did
X", the 1.69 toolset should be read before it is treated as settled.
