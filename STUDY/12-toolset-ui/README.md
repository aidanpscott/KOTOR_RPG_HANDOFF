# STUDY 12 — Aurora's toolset UI: what it looks like and how it is arranged

**The question:** we are choosing between a multi-window Builder and a single
window with docked panes. Flutter's stable channel cannot open a second native
window (`STUDY/11-spike`). Before paying the main-channel stability cost, what
were Aurora's extra windows actually *for* — and would panes have served?

**The answer:** Aurora had almost no extra windows. It is a single window with
three docked panes and a pile of modal dialogs, and its accessibility came from
somewhere else entirely.

---

## The short version

| | |
|---|---|
| Toolkit | **Borland/Embarcadero VCL** — no MFC, zero `RT_DIALOG` resources |
| UI units | **105 binary DFM forms**, all parsed |
| MDI | **none** — no `fsMDIForm`, no `fsMDIChild`, an empty hidden `&Window` menu |
| Main window | tree left (201px) · **canvas centre** · palette right (219px) · log bottom (77px) · 3 splitters |
| Dialogs | 77 `Tdlg*`, at least 48 dismissing with a `ModalResult` |
| Frames (panes) | 15 `Tfra*` — by VCL type, these *cannot* be windows |
| Floating windows | **5**, all `fsStayOnTop`, all lookups or monitors |
| True second windows | **1** — the Script Editor |
| Tabs | **240 `TTabSheet`** across 43 forms |
| Creation verbs in the toolbars | **zero** |

## Reading order

- **`RECORDS.md`** — description only. Thirteen records, `R12.01`–`R12.13`.
- **`FLAWS.md`** — judgement, citing records. Seven findings, `F12.01`–`F12.07`.
- **`code/`** — the PE and DFM readers, so the parse is reproducible.

## The finding that settles the decision

**`F12.05`. The accessibility had nothing to do with multi-window.**

There was barely any window arrangement to remember. What made Aurora
approachable is three things, none of them a property of how windows are
arranged:

1. **No verbs to learn.** The entire main toolbar set is file operations, camera
   moves, a *two-state* Terrain/Objects toggle, visibility filters and render
   toggles. **Not one button creates anything.** Placing content is effectively a
   single verb — pick from the palette, put it in the area.
2. **Everything makeable is enumerated in a permanent pane** — the palette,
   Standard and Custom, always visible, always resizable.
3. **The hard parts are wizards, not blank forms** — 18 of them.

All three survive being ported to a single window with docked panes. **The
variable is independent of the decision.**

## What corrects the brief

The brief expected "property inspectors" on the right. **There is no property
inspector anywhere in Aurora.** The right pane is the palette; object properties
live in modal dialogs you open, change and close. That matters, because a
persistent inspector is the usual argument *for* a second window — and Aurora
never had one.

## ⚠ Scope

Everything structural comes from **binary inspection of one file**: Beamdog's
Enhanced Edition toolset, `1.5.0.5`, built 2025-10-06. **No 1.69-era binary
exists in this install.** Runtime behaviour — modality, drag-and-drop, runtime
parenting — lives in compiled Object Pascal that was **not** disassembled, and
every claim that depends on it is flagged in place. The toolset was **not run**.
