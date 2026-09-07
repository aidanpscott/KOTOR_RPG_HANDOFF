# STUDY 12 — Aurora's toolset UI: records

**Description only.** Judgement is in `FLAWS.md`.

## ⚠ Provenance and scope — read first

Everything structural below comes from **binary inspection of one file**:

```
bin/win32/nwtoolset.exe   12,201,984 bytes
PE32, i386, GUI, 9 sections, linker subsystem 5.00
PE timestamp        2025-10-06 18:18:47 UTC
CompanyName         Beamdog Corp.
FileVersion         1.5.0.5
LegalCopyright      Copyright Beamdog © 2017-2019
ProductName         Aurora Neverwinter Nights Toolset
```

**⚠ This is Beamdog's Enhanced Edition toolset, not BioWare's 2002 original.**
No 1.69-era toolset binary exists anywhere in this install — I searched the
whole tree for `*toolset*` and found exactly one file. Where a finding is
plausibly an EE change I say so; where I cannot tell, I say that instead.

**What is evidence here:** the PE import table, the resource directory, and 105
fully-parsed binary DFM form streams. Nothing below is inferred from running the
program, which I cannot do.

**What is NOT evidence here:** anything about behaviour that lives in compiled
code. Modality, drag-and-drop, and runtime parenting are all set in Object
Pascal I did not disassemble. Each is flagged where it arises.

---

## R12.01 · The toolkit is Borland/Embarcadero VCL, not MFC or raw Win32

**No MFC.** The import table has no `MFC*.DLL`, and the resource directory
contains **zero `RT_DIALOG` and zero `RT_MENU`** resources. Windows dialog
templates are not how this program is built.

Imports are the plain Win32 set — `USER32` (219 functions), `GDI32` (117),
`KERNEL32` (177), `COMCTL32` (36), `OPENGL32` (62), `COMDLG32`, `OLE32`.

The identifying evidence is the section layout plus the resource types:

```
sections   .text .data .tls .rdata .idata .didata .edata .rsrc .reloc
resources  RCDATA 107, STRING 27, BITMAP 10, CURSOR 9, GROUP_CURSOR 9,
           ICON 6, GROUP_ICON 1, VERSION 1, MANIFEST 1
```

`.didata` (delay-import) and `.edata` in a GUI executable, with forms stored as
**RCDATA**, is the Borland/Embarcadero signature. **105 of the 107 RCDATA
entries begin with the four bytes `TPF0`** — the binary DFM stream header. The
remaining two are not form streams.

All 105 parse without error with a from-scratch DFM reader.

## R12.02 · The form inventory is complete and self-describing

VCL naming convention, used consistently:

| prefix | VCL meaning | count |
|---|---|---|
| `Tdlg*` | dialog | **77** |
| `Tfra*` | **`TFrame` — an embeddable panel, not a window** | **15** |
| `Tfrm*` | form | **11** |
| other | `TColorPicker`, `TSEditCodeCompletionList` | 2 |

**`Tfra*` is the load-bearing detail.** A `TFrame` in VCL cannot be a window at
all; it exists only to be parented inside something else. Fifteen of Aurora's
105 UI units are, by their own type, panes.

## R12.03 · There is no MDI

`FormStyle` across all 105 forms takes exactly two values:

```
<not written, i.e. fsNormal>   100
fsStayOnTop                      5
```

**`fsMDIForm` and `fsMDIChild` do not appear.** Aurora is not an MDI
application. It has no child-window frame and no window-tiling model.

**⚠ A vestige:** `TfrmFrame` carries a top-level menu item `miMainWindow`,
`Caption = '&Window'`, **`Visible = False`, and with no child items at all**. An
empty, hidden Window menu. That is the shape a removed MDI window-list leaves
behind, but the DFM cannot tell me whether it was ever populated. Recorded as an
observation; the inference is in `FLAWS.md`.

## R12.04 · The five windows that genuinely float

The only forms with `FormStyle = fsStayOnTop`:

| form | caption | size |
|---|---|---|
| `TfrmPreview` | Preview | 591×276 |
| `TfrmObjectList` | Inaccessable Objects *(sic)* | 215×248 |
| `TdlgFindInstance` | dlgFindInstance | — |
| `TfrmHelp` | NWToolset Help | — |
| `TSEditCodeCompletionList` | *(none)*, `bsNone` | — |

Four utilities and one autocomplete popup. Every one is a lookup or a monitor —
none is an authoring surface.

## R12.05 · The main window: three docked panes, three splitters, one canvas

`TfrmFrame`, caption `NeverWinter ToolSet - No Module`, laid out purely by VCL
`Align`:

```
TfrmFrame
├── TControlBar  ctlbFrame      alTop     h=30   ← 5 drag-arrangeable toolbars
│     pModuleFile "File" · pModuleDisplay "Display" · pSelectionMode
│     "Selection Mode" · pMode "Filter" · pPreviewPanel "Preview"
├── TPanel       pFrame         alClient
│   ├── TfraMainInventory  fraInventory   alLeft   w=201   ← module contents tree
│   ├── TSplitter          spInventory    crHSplit
│   ├── TPanel             pArea          alClient        ← THE WORK SURFACE
│   ├── TSplitter          spPalettes     alRight crHSplit
│   └── TfraMainPalette    fraPalettes    alRight  w=219  ← the palette
├── TSplitter    spBottom       alBottom  crVSplit
└── TPanel       pBottom        alBottom  h=77
    ├── TMemo      mMessages    alClient                  ← message log
    └── TStatusBar sbFrame
```

**`pArea` is an empty panel in the DFM.** It has no design-time children at all.
The area viewer is parented into it at runtime — and the form that goes there,
`TfrmViewerArea`, is the only `Tfrm*` with **`BorderStyle = bsNone`**, a
borderless form, which is the standard VCL idiom for embedding a form as a pane.

**⚠ The runtime parenting itself is in code I did not disassemble.** The
borderless style and the empty `alClient` host are strong circumstantial
evidence, not proof.

Three splitters, all with resize cursors (`crHSplit`, `crVSplit`), make every
pane boundary draggable.

## R12.06 · The panes are named "Interface Panels" in the shipped UI

`View → Interface Panels` toggles, each backed by a `TAction`:

```
actShowPaneMessageLog             Message Log
actShowPaneModuleContents         Module Contents
actShowPanePalette                Palette
actShowPaneToolbar                Toolbar
actShowPaneVisualCameraControls   Visual Camera Controls
```

Separately, `View → Toolbars` toggles the five toolbars individually, and a
`TPopupMenu pmToolbars` offers the same on right-click.

Aurora's own vocabulary for these regions is **panel**, not window.

## R12.07 · The dominant idiom is the tabbed dialog

| control | instances | forms |
|---|---|---|
| `TPageControl` | 53 | 44 |
| `TTabSheet` | **240** | 43 |
| `TSplitter` | 25 | 13 |
| `TToolBar` | 12 | 7 |
| `TControlBar` | 1 | 1 |

Overall control census, top of list: `TLabel` 771, `TButton` 724, `TPanel` 415,
`TEdit` 372, `TComboBox` 289, `TCheckBox` 256, `TTabSheet` 240, `TRadioButton`
135, `TTreeView` 54.

**240 tab sheets against 105 forms.** Depth in this tool is bought with tabs.

## R12.08 · Modality: 48 forms dismiss with a `ModalResult`

48 of 105 forms contain at least one button with a non-zero `ModalResult`. Of
those, **42 also carry `BorderStyle = bsDialog`** — a fixed, non-resizable
frame — and `Position` is `poMainFormCenter` (24 forms) or `poOwnerFormCenter`
(23) across the set.

**⚠ This is strong evidence, not proof.** In current VCL, assigning
`ModalResult` also closes a form shown non-modally, so the property alone does
not establish modality. `bsDialog` + owner-centred position + an OK/Cancel pair
is the conventional signature of a modal dialog, and I am reading it as such.
**The `ShowModal` call sites are in compiled code I did not disassemble.**

Of the four editors on the `Tools` menu:

| editor | `ModalResult` buttons | `BorderIcons` | reading |
|---|---|---|---|
| Conversation | **one, `bOK` captioned "Done"** | default (min+max) | dialog-style dismissal |
| Faction | `bOk` / `bCancel` | default | dialog-style dismissal |
| Journal | `bOk` / `bCancel` | max only, **no minimise** | dialog-style dismissal |
| **Script** | **none** | **min + max + help** | **a real window** |

The Script Editor is the one large editor with no modal dismissal and a full set
of border icons including minimise. `TdlgScriptEditor` is 760×540 and contains a
splitter.

## R12.09 · The Conversation Editor: one window, master over detail

`TdlgConversationEditor`, 939×660, **no `TMainMenu`** — driven by toolbars and a
32-action `TActionList` of its own.

```
TdlgConversationEditor
└── TPanel pClientArea  alClient
    ├── TPanel      pTree    alClient          ← the tree half
    │   ├── TToolBar     tlbText   alTop  h=27
    │   ├── TToolBar     tlbTree   alLeft w=24
    │   ├── TPageControl pcMainText alClient   ← one tab per open conversation
    │   └── TStatusBar   RightViewStatusBar
    ├── TSplitter   splMain  alBottom crVSplit
    └── TPanel      pBottom  alBottom h=308    ← the detail half
        ├── TPageControl pcBottom alClient
        │     tabs: Data · Bookmarks · Search
        └── TPanel       pButtonBase alBottom h=30
```

`pcMainText` holds a single design-time tab captioned **`Scrap`**; real tabs are
created at runtime. So the editor is **multi-document inside one window**.

The tree itself is `TfraConversationTree` — **a `TFrame`, i.e. a pane** —
containing exactly one `TTreeView tvMain` at `alClient`, with `DragMode =
dmAutomatic`, a 15-action list and a context menu:

```
Add · Copy · Cut · Delete · Paste · Paste As Link · Bookmark
Save · Close · Test · Expand All · Collapse All · Check Spelling
```

**A branching conversation is presented as a plain Win32 tree view.** Not a node
graph, not a canvas. `Paste As Link` is how the tree expresses a DAG rather than
a pure tree.

The editor carries its own document verbs — `actNew`, `actOpen`, `actSave`,
`actSaveAll`, `actClose`, `actQuit` — plus `actFindInFiles`, `actImportDialog`,
`actExportDialog`, `actCheckSpelling`, `actLaunchScriptEditor`.

## R12.10 · There are no creation verbs in the toolbars or the menus

The complete toolbar inventory of the main window:

| toolbar | buttons |
|---|---|
| File | New, Open, Save, \| , Undo, Redo |
| Display | Goto Start Location, Reorient Camera |
| **Selection Mode** | **Select Terrain, Select Objects** — *two, toggled by F10* |
| Filter | Show Creatures / Doors / Encounters / Items / Merchants / Placeables / Sounds / Triggers / Waypoints / Start Location, Show All, Hide All |
| Preview | Display Shadows, Show Fog, Use Area Lighting, Play Ambient Sound, Play Ambient Music, Play Placed Sounds |

**Not one of these creates anything.** File operations, camera operations, a
two-state selection mode, visibility filters, and render toggles.

The menus agree. `File`, `Edit` (undo/redo/cut/copy/paste, resize/rotate area,
Find Instance, Module/Area Properties), `View`, `Environment` (render and sound
toggles), `Build` (Verify Area, Verify Module, Test Module, Area Statistics),
`Tools` (four editors + Options), `Wizards`, `Help` (two items).

**The entire creation surface is the palette and the wizards.** `Wizards` lists
18 forms: Module, Area, Plot, and one per placeable object type — Creature,
Door, Encounter, Item, Store, Placeable, Sound, Trigger, Waypoint.

## R12.11 · The palette pane

`TfraMainPalette`, 219 wide:

```
TfraMainPalette
├── TPanel       pTop     alTop h=57
│     TSpeedButton sbTerrain · TSpeedButton sbStartLocation
│     TPanel pPaletteSwitcher · TComboBox cbPalettes (Visible=False)
├── TPageControl pcMain   alClient    tabs: Standard · Custom
├── TSplitter    spPlot   alBottom crVSplit
└── TPanel       pPlot    alBottom h=85
      TfraPlotManager fraPlotManager1 alClient
```

Context menu: `Edit`, `Edit Copy`, `New`, `Delete`, `Update Instances`,
`Find Text`, `Find Next`, `Refresh Palette`.

The blueprint trees inside `tsStandard` / `tsCustom` are built at runtime; the
tab sheets are empty at design time.

**⚠ I could not confirm drag-to-place from the binary.** `DragMode =
dmAutomatic` appears on exactly four tree views in the whole program —
`TfraConversationTree.tvMain`, `TdlgInventory.tvItems` and `.tvCustomItems`, and
`TdlgItemGeneratorEdit.tvItems`. The palette's own tree is not among them
**because it does not exist at design time**, so its drag behaviour is set in
code I did not read. Neither confirmed nor refuted.

## R12.12 · Some "windows" are separate programs

Shipped beside the toolset in `bin/win32` and `util/win32`:

| binary | size | forms | what |
|---|---|---|---|
| `nwhak.exe` | 3.2 MB | 3 — `TfrmFrame` "Hak Pak Editor", `TfrmAbout`, `TdlgYesNoAll` | hak packaging |
| `GFFEditor.exe` | 802 KB | *(no DFM forms; 2 RCDATA)* | raw GFF inspection |
| `DebugServer.exe` | 811 KB | — | script debugging |

`nwhak.exe` is VCL like the toolset. `GFFEditor.exe` is a different build —
8 sections, no `.didata`, 21 bitmaps, no form streams.

**The toolset also has its own `TdlgHakPak`** ("Hak Pak Conflict Analysis"), so
hak *analysis* is in-process while hak *building* is a separate executable.

## R12.13 · Documented Enhanced-Edition UI changes

From the shipped changelogs in `lang/en/docs/` — **this is documentation, not
binary inspection**:

> `Tabs are disabled by default. To enable them, go to Toolset settings -> Area
> editor -> Open areas in tabs, then restart the Toolset.`

Area tabs are a **Beamdog addition, off by default, needing a restart**. This
matches `TfrmFrame`'s `TPopupMenu pmEditorTab` (single item, `Close`), which has
no other explanation in the DFM.

Other toolset entries mention "a reported regression vs 1.69", confirming the EE
build is a maintained continuation of the original rather than a rewrite.

**⚠ I could not determine** which of `actShowPane*`, the `TControlBar`, or the
hidden `&Window` menu are original and which are EE-era. The changelogs do not
say and no 1.69 binary is present.
