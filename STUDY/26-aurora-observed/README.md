# STUDY 26 — Aurora, observed

**From `Tester`.** Every earlier Aurora study read the binary. **This one looked
at it.** Sixteen screenshots, in this folder, numbered in the order I walked it.

**It launched on the first attempt.** `wine nwtoolset.exe` from
`Neverwinter Nights/bin/win32`, in a throwaway `WINEPREFIX`. No Proton, no
tricks. **NWN:EE toolset `v89.8193.37-17`, module `To Heir is Human.mod`** —
a stock module, chosen after the owner pointed out that one needing haks
crashes.

**⚠ Nothing was saved.** I placed one test creature to reach the instance
context menu and killed the process rather than risk a save. The NWN install
was read, never written.

**⚠ `PT-1496`'s limit is applied throughout**: I say where a thing is an answer
worth taking and where it is only what a 2002 Win32 app had to do.

---

## 1 · It opens on a question, and never shows you an empty tool

**`01-opens-on-a-question.png`, `02-empty-window-behind-the-question.png`**

**`TRACE-106` is right, and it is the first thing you see.** A modal
**"Welcome!"** dialog, centred, before anything:

> **What would you like to do?**
> ● Create a new Module
> ○ Open an existing Module   ← with a list of every module found
> ○ Start normally
> ☑ Show this screen at startup

**The main window is already built behind it** — menu bar, a toolbar of ~25
icons, an empty tree pane, an empty document pane. **You never look at that
empty window without something on top of it asking what you want.**

**⚠ The answer transfers and we already half-take it.** `PT-1356` puts a picker
*in the pane*; Aurora puts a question *over the window*. **Aurora's is stronger
in one respect:** the third option is `Start normally`, so the question is
escapable and its checkbox is right there. **Ours has no way to say "just let me
look".**

---

## 2 · The module tree has THREE roots — and the nine kinds live under an AREA

**`03-module-tree-three-roots.png`, `04-an-area-holds-nine-kinds.png`,
`05-instances-are-named-by-tag.png`**

    Areas
    Conversations
    Scripts

**That is the whole top level.** `STUDY 16` got the shape right and the
*scale* is the surprise: **three rows, where ours has thirteen** (areas,
conversations, ten blueprint kinds, scripts).

**Expand an area and the nine kinds appear underneath it:**

    Cavern Entrance
        Creatures · Doors · Encounters · Items · Merchants
        Placeables · Sounds · Triggers · Waypoints

**And expanding `Doors` gives `CavToDrow`, `CavToFor` — instance TAGS.**

**⚠⚠ THIS IS THE BIGGEST STRUCTURAL DIFFERENCE AND IT IS NOT A WIN32 ARTEFACT.**
Aurora separates two things we have collapsed into one:

| | Aurora | ours |
|---|---|---|
| **blueprints** you can place | the **palette**, right-hand pane | `blueprints/*` in the tree |
| **instances** actually placed | the **tree**, under their area | **nowhere** |

**Our placements have no home in any surface.** They exist only as
`[[contents]]` rows in a file. **A tag we generate is never shown to the author
who made it.** Aurora's tree is a list of what is *in the world*; ours is a list
of what *could be*.

---

## 3 · Three panes, and the palette is contextual

**`06-three-panes-tree-tab-palette.png`**

**tree | tabbed document | palette.** That is our shape, and seeing it confirms
`PT-1340`'s single-window decision rather than challenging it.

**What differs:**

- **The area opens as a TAB** (`cavernenterance`), with a row of pan / zoom /
  rotate controls beneath it. Same as ours.
- **The palette CHANGES with what you are doing.** With an area open it offers
  `Features · Groups · Terrain`. It is not a fixed list of everything.
- **The palette has its own toolbar** above it, and its own tabs
  (`Standard` | `Custom`).
- **The status bar names the selected object's Tag** — `Tag : Cavernenterance`
  bottom-left, mode (`Select` / `Paint`) bottom-right. **We show neither.**

---

## 4 · Terrain has an Eraser, and it is just another brush

**`07-terrain-has-an-eraser.png`**

    Terrain
        Bridge · Cliff · ERASER · Forest · Pit · Road · Stream · Wall

**The eraser is an entry in the palette, alphabetically among the things you
paint.** Not a mode, not a modifier key — a brush.

**⚠ Directly relevant to `TEST 017`**, where I found we have no eraser and
concluded that painting floor over a tile *is* the eraser. **Aurora's answer is
to name it.** Ours works; theirs is discoverable.

**⚠ And the terrain list itself does NOT transfer.** Bridge/Cliff/Forest/Pit are
*tileset features* — 2002 tile art. Ours are five **passability** kinds
(floor/wall/water/difficult/hazard) because our rules read them. Different
model, and ours is the one our rules need.

---

## 5 · The palette is a mode selector — nine kinds, nine buttons

**`08-the-palette-is-a-mode-selector.png`, `10-the-nine-paint-modes.png`**

Hovering the palette's toolbar gives nine tooltips, in order:

    Paint Creatures · Paint Doors · Paint Encounters · Paint Items
    Paint Merchants · Paint Placeable Objects · Paint Sounds
    Paint Triggers · Paint Waypoints

**Exactly the nine kinds that hang under an area.** One-to-one.

**⚠ So "what does authoring a door look like?" has a plain answer: you switch
the palette to Doors and paint one, exactly as you paint a tile.** There is no
"New Door" dialog. **Placing is the authoring verb.** Our eight inert kinds do
not need eight dialogs — they need to be paintable.

**Our ten map onto their nine plus one**: their `Merchants` is our `stores`, and
**`doctrines` is ours alone** — Aurora has no behaviour blueprint because its AI
is scripts.

---

## 6 · How a list of many things reads: four levels and a Standard/Custom split

**`09-four-levels-of-taxonomy.png`**

    Monsters
        Aberrations · Animals · Constructs · Dragons · Elementals · Giant
        Humanoid · Insects · Magical Beasts · Miscellaneous · Planar
        Shapechangers · Undead
            Humanoid → Bugbears · Fey · Goblin · Lizardfolk · Minotaur · Orc · Other
                Goblin → Goblin · Goblin · Goblin Chieftain · Goblin Elite ·
                         Goblin Elite · Goblin Shaman · Goblin Shaman ·
                         Hobgoblin · Hobgoblin Shaman

**Four levels, and no flat list anywhere.** Plus **two tabs — `Standard` and
`Custom`** — separating what the game ships from what this module adds.

**⚠ That is the answer for our 271 worlds, 320 feats and 104 powers**, which are
flat today. **And the Standard/Custom split is a distinction we do not have at
all**: our palette shows only the package's own blueprints, and never says
"here is what the rules ship with".

**⚠ One thing Aurora gets WRONG and we already get right.** Look at that leaf
list: **two "Goblin", two "Goblin Elite", two "Goblin Shaman"** — identical
labels, no way to tell them apart. **Aurora lists blueprints by display name.**
`PACKAGE-NAMING-01` makes the path the identity and Loom refuses a duplicate id.
**Ours is better and this screenshot is why.**

---

## 7 · A placed instance has ten verbs. A blueprint has four

**`11-blueprint-context-four-verbs.png`, `12-instance-context-ten-verbs.png`**

**Right-click a palette blueprint:**

    Edit Copy · Update Instances · Find Text · Find Next

**Right-click a placed instance:**

    Add To Palette · Adjust Location · Create Waypoint · Conversation
    Inventory · Levelup Wizard · Setup Store · Delete · Variables · Properties

**⚠ THE INSTANCE IS THE RICHER OBJECT, AND OURS IS A ROW IN A FILE.** Of those
ten, we have **Delete** and a partial **Properties**. What we do not have:

- **`Add To Palette`** — promote a placed, tweaked instance back into a reusable
  blueprint. **We have no path from instance to blueprint at all.**
- **`Conversation`** — open the conversation editor *for this creature*, from
  the creature. **This is exactly `TEST 015`'s F4**, where I found a creature's
  conversation can only be set at creation and no edit path exists. **Aurora
  answers it with one menu item.**
- **`Inventory`**, **`Variables`** — sub-editors for what it carries and
  arbitrary per-instance data. We have one `equip` field and nothing.
- **`Adjust Location`** — type the position. **We can only click a square.**

**⚠ `Update Instances` is a verb we should NOT copy.** It exists because Aurora
*copies* blueprint data into each instance. Our placements re-read the blueprint
every load, so the problem it solves cannot arise for us. **A good example of an
answer that does not transfer.**

---

## 8 · The creature editor: eleven tabs, a live preview, and a way out to the conversation

**`13-creature-property-sheet-eleven-tabs.png`**

**Two rows of tabs:**

    Advanced · Feats · Spells · Special Abilities · Comments
    Basic · Statistics · Appearance · Classes · Skills · Scripts

**The `Basic` tab, left half: a live 3D model of the creature.** Right half:
First/Last Name, **Tag**, Race, Appearance, Phenotype, Gender, Description,
Challenge Rating; a **Portrait** group with a thumbnail; a **Conversation**
group with a dropdown, a `...` and an **`Edit` button**; and an
**`Inventory ...`** button pinned bottom-left.

**⚠ What to take:**

- **Splitting one long form into tabs.** Our New Creature is a single scrolling
  dialog that already runs past 720px (`TEST 014`). **Eleven tabs is more than
  we need; two or three is the idea.**
- **The `Edit` button beside the conversation field.** Set it *and* go there.
- **Seeing the thing you are editing.** `PT-1319` says a character is a portrait
  and no art exists — so not a 3D view, but **the empty portrait circle could be
  doing more work than it does.**

**⚠ What not to take:** the `...` buttons beside First/Last Name are the
**localised-string editor** — a 2002 multi-language requirement. We are one
language and should stay one field.

---

## 9 · ⚠⚠ THE SINGLE MOST USEFUL SCREEN: Statistics shows its arithmetic

**`14-statistics-shows-the-arithmetic.png`**

    Ability Scores
                   Score  +  Racial Modifier  =  Total    Bonus
        Strength     10   +        0          =   10        0
        Dexterity    14   +        0          =   14        2
        Constitution 13   +        0          =   13        1
        Intelligence 10   +        0          =   10        0
        Wisdom       12   +        0          =   12        1
        Charisma     17   +        0          =   17        3

    Saves          Base + Ability Modifier + Bonus = Total
    Armor Class    Natural AC · Base · Dexterity Bonus · Size Modifier · Total
    Hit Points     Base Hit Points · Hit Point Bonuses · Total Hit Points

**Every group on this tab shows the components AND the total. Never one without
the other.**

**⚠ THIS IS THE ANSWER TO `TEST 024` AND `TEST 025`.** I found that our
character sheet shows the species-adjusted total, our log stores the bought
score, and the fight silently uses the bought one — a Gamorrean whose sheet says
**STR 18** swings at **Strength 2**. **The bug is ours to fix, but the reason it
went unseen for so long is that no screen of ours shows `bought + racial =
total` together.** Aurora puts all four numbers on one row and the discrepancy
would have been unmissable.

**And `Armor Class` is the shape `PT-1531` is reaching for**: `Natural + Base +
Dexterity + Size = Total`, each its own field. **Our `defence: 10` with a
comment explaining the gap is honest; this is what it becomes when it is filled.**

**⚠ This transfers completely. It is not a Win32 idea — it is a
show-your-working idea, and it is the same one `PT-1326` already made for
checks.**

---

## 10 · The conversation editor: master over detail, and a word count

**`15-conversation-editor.png`**

**`STUDY 14` is right — master over detail.** A tree of lines on top; a detail
pane beneath, split left and right.

- **Left detail:** `Speaker Tag` (dropdown + `Add`), a large `Text` box, and
  tabs `Data | Bookmarks | Search`.
- **Right detail:** a tab strip — `Text Appears When… | Actions Taken | Other
  Actions | Comments | …` **with ‹ › arrows because the tabs overflow** —
  holding a Script dropdown, a Name/Value table, and a **Script Preview**.
- **A vertical toolbar** down the left edge of the tree.
- **`Scrap` tab** beside the conversation's own tab.

**⚠ Three things worth having:**

1. **`Line Letter Count · Line Word Count · File Word Count · Module Word Count`**
   — live, in a strip between master and detail. **A writer's tool, and we have
   nothing like it.** For a game that is mostly dialogue this is a real
   omission.
2. **The `Scrap` tab** — somewhere to park a line you have cut but not decided
   about. **Our editor refuses to write a dead check** (`PT-1461`); a scrap area
   is the other answer to the same problem, and the two are complementary.
3. **`Speaker Tag` chosen per line, with `Add` inline.**

**⚠ Two things that are Win32 and not to be copied:** the editor is a **separate
top-level window** rather than a tab — `PT-1340` already decided against that —
and **the detail tabs overflow their strip**, which is what happens when a fixed
tab control meets more tabs than fit. **Our row of buttons cannot overflow.**

---

## 11 · Doors are filed by tileset, then by material

**`16-doors-by-tileset-then-material.png`**

    Tileset Specific
    Universal
        Metal · Other · Stone · Wood

**A blueprint can be scoped to the tileset it belongs with.** We have no notion
of a blueprint that only makes sense in some areas. **Worth knowing when the
eight inert kinds get built** — the question "where does this belong?" has an
answer here.

---

## ⚠ What I did not look at

- **`Encounters`, `Triggers`, `Sounds`, `Placeables`, `Merchants` editors** —
  I opened the creature sheet and the conversation editor only.
- **The `Custom` palette tab** — never populated it, so I do not know what an
  author's own blueprint looks like listed beside the shipped ones.
- **`Build` / `Wizards` / `Tools` menus** — never opened. `Wizards` in
  particular is a whole surface I have not seen.
- **The area's own properties**, the tileset picker, and how a NEW area is made.
- **Scripts** — the third tree root, never expanded.
- **`Levelup Wizard`, `Setup Store`, `Variables`** — seen on the menu, never
  opened.
- **Any list long enough to need scrolling in the palette** — the goblin leaves
  fit on screen.
- **How it behaves at a small window size.** I ran it at 1500×1010.
