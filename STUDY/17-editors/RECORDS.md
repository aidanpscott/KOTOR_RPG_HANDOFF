# STUDY 17 — Aurora's editing surfaces: records

**Description only.** Judgement in `FLAWS.md`. Same binary as `STUDY 12`, `14`,
`16` — Beamdog EE `1.5.0.5`, 105 parsed DFM streams. **Not run.**

---

## R17.01 · The measurement

**DFM.** Every form scored on the traits that mark a place you *dwell* rather
than an errand: splitters, its own action list, toolbars, a status bar, its own
main menu, document-lifecycle actions, and a penalty for dismissing with a
`ModalResult`.

```
FORM                       score  spl acts tabs tbar  st  doc  dismiss
TfrmFrame                     45    4   59    2    5   1    5  —
TdlgConversationEditor        35    2   32    9    2   1    7  one "Done"
TdlgScriptEditor              30    2   27    8    1   0    6  none
──────────────────────────────── a gap of 17 ────────────────────────────
TdlgTriggerEdit               13    4    0    6    0   1    0  OK / Cancel
TdlgHakPak                     9    3    0    0    0   0    0  none
TfraConversationTree           9    0   15    0    0   0    2  —
TdlgAreaProperties             7    2    4    6    0   0    0  —
TfrmIFOProp                    7    2    0    5    0   0    0  —
TfrmViewerArea                 6    0   32    0    0   0    0  none
```

**⚠ Three forms, then a cliff.** The fourth-placed form scores less than half
the third.

## R17.02 · ⚠ The document-lifecycle test separates them completely

**DFM.** Actions named `actNew`, `actOpen`, `actSave`, `actSaveAs`,
`actSaveAll`, `actClose`, `actQuit` — a thing that can be created, saved and
closed is a **document**:

```
TfrmFrame                 5 of 7
TdlgConversationEditor    7 of 7      ⚠ every one, including Save All and Quit
TdlgScriptEditor          6 of 7
──────────────────────────────────
TfraConversationTree      2   (Save, Close — it is a FRAME inside the editor)
TfraMainInventory         1
TfraBlueprintSelect       1
TfraPlotManager           1
everything else           0
```

**Only three forms in 105 own a document lifecycle**, and two of the four
stragglers are frames living *inside* one of the three.

## R17.03 · The conversation editor

**DFM**, and from `STUDY 14`. `939×660`, **no `TMainMenu`** — driven by two
toolbars and its own **32-action** list.

```
pClientArea  alClient
├── pTree     alClient        ← the tree half
│   ├── tlbText   alTop  h=27
│   ├── tlbTree   alLeft w=24
│   ├── pcMainText alClient   ← ONE TAB PER OPEN CONVERSATION
│   └── RightViewStatusBar
├── splMain   alBottom crVSplit
└── pBottom   alBottom h=308  ← the detail half
    ├── pcBottom   Data · Bookmarks · Search
    └── pButtonBase
```

Its verbs include `actSaveAll`, `actFindInFiles`, `actImportDialog`,
`actExportDialog`, `actCheckSpelling`, `actLaunchScriptEditor`.

**⚠ It dismisses with a single button captioned "Done", `ModalResult = 1`.**

## R17.04 · The script editor

**DFM.** `760×540`, **`BorderIcons = biMinimize · biMaximize · biSystemMenu ·
biHelp`**, **no `ModalResult` buttons at all**, one splitter, 27 actions, eight
tab sheets, one toolbar.

**⚠ The only form of the three with a minimise box and no dismissal button** —
`STUDY 12` called it the one genuine second window and this is why.

## R17.05 · ⚠ The area viewer, which STUDY 12 left blank

**DFM.** `TfrmViewerArea`, **`BorderStyle = bsNone`**, parented into
`TfrmFrame.pArea` at runtime. It contains far more than a canvas:

```
TScrollBox  GLPanel              ← the 3D canvas
TScrollBox  ConsolePanel         ⚠ A CONSOLE
TEdit       CommandBox           ⚠ a command line
TPanel      ResponseBox          ⚠ and its output
TScrollBox  pCameraControls      ← toggled by actShowPaneVisualCameraControls
   bPanLeft · bPanRight · bPanForward · bPanBackwards
   bRotateClockwise · bRotateCounterClockwise
   bPitchUp · bPitchDown · bZoomIn · bZoomOut
   bGobRotateCounter · bGobRotateClockwise · bGobRotateRandom
TMainMenu   AreaMenu             ⚠ ITS OWN MENU — Edit ▸ Undo
TOpenDialog dlgOpen · TSaveDialog dlgSaveAs
```

**⚠ And 32 actions, nearly all context verbs on a SELECTED INSTANCE:**

```
Properties · Delete · Adjust Location · Variables · Add to Palette
Edit Inventory · Edit Conversation · Add Popup Text · Tile Properties
Add Waypoint · Add Spawn Point · Create Set · Reverse Door
Setup Store · Levelup Wizard · Redraw Polygon
door animation      Opening Forward/Backward · Closing from Front/Back
                    Closed · Opened Forward/Backward · Stop
placeable animation Open · Closed · Activated · Deactivated · Destroyed · Default
sound               Turn On · Mute
```

**⚠ It has NO splitter, NO status bar, and NO document-lifecycle action.**

## R17.06 · Two things called "editor" that are dialogs

**DFM.**

| | dismissal | splitters | tabs | status |
|---|---|---|---|---|
| `TdlgJournalEditor` | **OK / Cancel** | 1 | Category · Entry | 0 |
| `TdlgFactionEditor` | **OK / Cancel** | 0 | Basic · Advanced | 1 |

**Both carry `bOk` and `bCancel`. Neither has a single document-lifecycle
action.**

## R17.07 · The richest dialog is still a dialog

**DFM.** `TdlgTriggerEdit`: **`BorderStyle = bsDialog`**, **four splitters**, a
status bar, and six tabs — `Properties · Area Transition · Trap · Events ·
Advanced · Comments`.

**Zero actions. `bOk` and `bCancel`.**

**⚠ So splitters and tabs do not make an editor.** Aurora's most elaborate
property dialog resizes, has six pages, and is still something you open, change
and close.

## R17.08 · ⚠ No surface for tilesets, rules or strings — scoped negative

**DFM.** I searched all 105 forms for `tileset`, `2da`, `TLK`, `strings` and
`rules` in every component name and caption.

```
tileset   TdlgAreaWizard · TdlgAreaProperties · TdlgDoorWizard · TdlgLoadScreen
          — all SELECTION controls. Nothing edits one.
2da       ⚠ NOTHING. Not one form.
TLK       TfrmIFOProp only — a combo box choosing a file.
strings   TdlgOptions only — an option, not a string table.
rules     ⚠ NOTHING.
```

**Aurora's toolset edits none of these.** A tileset is picked; a TLK is picked;
2DA rules are not present at all. **Those were edited in separate programs.**

## R17.09 · One area at a time, until 2018

**DOC**, from the shipped changelogs and `STUDY 12`:

> *"Tabs are disabled by default. To enable them, go to Toolset settings → Area
> editor → Open areas in tabs, then restart the Toolset."*

**Area tabs are a Beamdog addition, off by default.** Originally the area viewer
showed **one area**, replaced when you opened another.

**⚠ Contrast the conversation editor, which had per-conversation tabs from the
start** (`pcMainText`, `R17.03`).
