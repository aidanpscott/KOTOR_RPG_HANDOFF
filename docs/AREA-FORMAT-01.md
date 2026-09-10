# AREA-FORMAT-01 — what is inside an area

**`PACKAGE-FORMAT-01` declares areas in the manifest and gives them the only numbered names in the format. It does not say what an area file CONTAINS.** That gap is the last piece of format work between here and running code — **the two-area test package cannot exist without it.**

---

## 1 · An area is a grid and the things on it

> **A grid, its contents, and its connections. Nothing else.**

**`PT-1103`: 2D grid movement, a digital tabletop mat.** No heightmap, no terrain mesh, no walkmesh — **`PT-1319` settled that a character is a portrait and nothing renders in three dimensions**, so an area has no geometry to describe.

```toml
[area]
name    = "Endar Spire — Command Deck"
size    = [24, 18]                    # tiles, width × height
```

**⚠ Size is in TILES, not pixels.** `PT-1146` locks zoom as one continuous range, so a tile has no fixed screen size — **the area does not know how large it looks.**

---

## 2 · ⚠ Tiles are declared by exception

**A 24×18 area is 432 tiles. Writing 432 entries by hand is intolerable, and a package should be readable in a diff (`§2` of the format).**

```toml
[tiles]
default = "floor"
walls   = [[0,0],[1,0],[2,0]]         # or a run notation
```

**Everything is `default` unless something says otherwise.** `TRACE-82` found KOTOR's 2DA files using `****` for "no value" and **losing that distinction on compile** — a default that cannot be told from an explicit value. **Ours is explicit: `default` is a declared value, not an absence.**

### ⚠ The notation is a TEXT MAP — `PT-1345`

```toml
[tiles]
legend = { "#" = "wall", "." = "floor", "+" = "door" }
map = """
########################
#......................#
#..........#...........#
#..........#...........+
########################
"""
```

**⚠ You can see the room in the diff.** `§2` of the format makes *readable in a diff* a **requirement**, and a rectangle list satisfies its letter but not its purpose — **nobody reads `[[0,0,24,1],[0,1,1,16]]` and pictures a corridor.**

**One tile change is one character change.** A minimal diff that says exactly what moved.

**It is hand-writable**, which the test package needs today, and **the legend keeps it extensible** — a new tile type is a new character, not a new field.

**⚠ The costs, stated:** whitespace becomes significant, so **an editor that strips trailing spaces will corrupt an area**; wide areas make long lines; and **the Builder must round-trip it faithfully rather than reformatting.**

**Rejected: a rectangle list.** More compact, unambiguous, immune to whitespace — **and unreadable.** At 24×18 legibility is worth more than compactness.

**⚠ And this is invisible to players.** It governs what a person editing a package by hand sees. **How the grid LOOKS on screen is a separate and still-open question** — see `APP-UI-VISION-01`, where tile art, grid weight, wall rendering and selection are all placeholder.

---

## ⚠ 2·0 An area ALWAYS declares its tiles — `PT-1365`

**The stop at `4b`: an area file with no `[tiles]` section cannot be drawn, and the agent refused to pick a reading.** It offered three; **the third is right.**

> **An area IS a grid. A file with a name and a size and no tiles is not an incomplete area — it is not an area.**

**⚠ So `[tiles]` is REQUIRED, and `PT-1363`'s `New Area` was incomplete.** It must write:

```toml
[tiles]
default = "floor"
```

**A minimal area is a lit floor with no walls.** You paint walls in afterwards — **`4c`'s job, not the format's.**

**⚠ Why this rather than "no section means all floor":** that would make **an absence into a default**, which `§2` forbids in the same breath it defines `default`. And it is `TRACE-82`'s `****` exactly — **KOTOR lost the distinction between "no value" and "a value that happens to be blank" on compile, and never got it back.**

**⚠ The refusal stays.** A file without `[tiles]` **remains an error** rather than becoming impossible — a hand-edited or truncated file must still fail loudly, per `F35`.

---

## ⚠ 2·0a The tile type vocabulary — `PT-1365`

**`PT-1361` ruled types are ours and fixed — *"we write the list, the engine knows every entry"* — and nobody wrote the list.** The agent found it missing and **declined to invent one**, which was right.

**⚠ Checked: `ENGINE-SPEC-04` requires no tile types at all**, so nothing constrains this from below. **Kept minimal deliberately — adding a type later is cheap, removing one is not.**

| type | passable | blocks sight | note |
|---|---|---|---|
| **`floor`** | yes | no | the default |
| **`wall`** | **no** | **yes** | drawn as mass, `§2b` |
| **`water`** | **no** | no | **⚠ not merely slow — you cannot simply walk over it** |
| **`difficult`** | yes | no | **costs DOUBLE to cross — `PT-1513`** |
| **`hazard`** | yes | no | crossing it does something. **⚠ What, is unruled** |

> **⚠⚠ IT COSTS DOUBLE, AND THE MULTIPLIER IS ON THE CREATURE — `PT-1513`.** `TEST 016` found it **costs nothing**: the move budget spends a flat 1 with no tile lookup, and `difficult` appears nowhere else in either repo.
>
> **⚠ And `STUDY 19` found the harder half: NEITHER SOURCE ENGINE EVER MODELLED IT.** `surfacemat.2da`'s `walk` and `walkcheck` are **booleans in K1 and NWN**, with no cost column — **Swamp, Mud and Water price identically to Stone.** So our code matched KOTOR exactly **and this document was the outlier.**
>
> **RULED: the document wins, because the tile type is offered.** Loom paints `difficult` beside four types that do something, in an idiom that reads like a rule — **an author paints it expecting it to bite.** A type that is offered and inert is `PT-1500`'s defect one layer up.
>
> **⚠ AND BG3'S ANSWER TRANSFERS AND OURS SHOULD COPY IT: the multiplier is a property of the CREATURE, not the tile.** `ActionResourceConsumeMultiplier(Movement, 4, 0)`, grouped so **one immunity clears every source at once.** Put it on the tile and every future exemption — a hover droid, a Force power, a boot — has to know about every terrain kind separately.
>
> **⚠ And `hazard` stays inert and stays unruled.** `§2·0a` says what it does is undecided, and **that is a different problem from a type whose cost was written and never spent.**


**⚠ Five. Nothing else exists, and a package cannot add one** — `PT-1361`. A swamp is **`water` and `difficult` with swamp art**, not a new type.

**⚠ And `door` is NOT a tile type**, though `§2`'s own legend example shows one. `§4a` makes a door **a connection with an optional template.** The example is wrong and is the kind of thing that would have become a second door model.

**Open:** whether `hazard` needs a magnitude, and whether `water` is one type or a family (shallow, deep). **Neither blocks `4c`.**

### ⚠⚠ `2·0c` What `difficult` COSTS, and where the number lives — `PT-1513`

**A square of `difficult` costs two.** This table has said *"costs more to cross"* since it was written and **nothing ever charged for it.**

> **⚠ `STUDY 19` found neither source engine modelled it either.** `surfacemat`'s `walk` and `walkcheck` are **booleans** in K1 and NWN with no cost column, and **Swamp, Mud and Water price identically to Stone.** **Our code matched KOTOR exactly and this document was the outlier.**

**The document wins anyway, and the reason is a Builder one:** `Loom` paints `difficult` beside four types that **do** something, in an idiom that reads like a rule. **An author paints it expecting it to bite.** A type offered and inert is `PT-1500`'s defect one layer up.

**⚠⚠ AND THE MULTIPLIER IS A PROPERTY OF THE CREATURE, NOT THE TILE.** Copied from BG3's `ActionResourceConsumeMultiplier(Movement, 4, 0)` rather than invented — **the tile names what kind of hard it is; the creature prices it**, and the multipliers are **grouped so one immunity clears every source at once.**

**Why the direction matters:** put the number on the tile and every future exemption — **a hover droid, a Force power, a boot** — has to know about every terrain kind separately, and **every kind added later silently escapes all of them.**

**⚠ `hazard` STAYS INERT.** `§2·0a` leaves what it does undecided, and **that is a different problem from a cost that was written and never spent**: the first waits for a ruling, the second was a defect.

**⚠ Stacking cannot arise, per `PT-1366`:** *"a text-map cell is one character and therefore ONE TYPE"* — a swamp is composed from `water` tiles and `difficult` tiles — so **a square names at most one costed source.** The engine takes the highest applicable multiplier, recorded so that whoever makes tiles combinable finds the decision rather than rediscovering it.

---

## ⚠ 2·0b The drawn look is a CHOICE, not a fallback — `PT-1366`

**`§2b` framed the untextured default as what you get *before* art.** Having seen it drawn — a lit surface, a recessed water plane, a stipple for difficult ground — **it is good enough to be a preference rather than an absence.**

> **A tileset is an OPTION. The drawn look is not a placeholder for one.**

**⚠ And that materially changes `PT-1351`.** The open question was *what happens to someone who does not own the games*, with three answers ranging from **extraction required** to **we recreate everything.**

**For the play surface, this answers it: neither.** The board is **drawn, ours, and complete** — and a tileset, whether extracted from KOTOR or authored by a stranger, **is something you turn on.**

**⚠ It does not answer `PT-1351` for the rest** — icons, portraits and UI chrome have no drawn equivalent. **But the largest surface in the product now stands alone**, which shrinks the question to the chrome.

---

## ⚠ 2·0c Painting, art and prefabs — one system, three sizes, `PT-1367`

**The verb is still Paint** (`TRACE-16`, `TRACE-104`, `TRACE-106` — confirmed three times). **What changes is the payload and the size.**

### Paint works on a REGION

**Drag a box, the rectangle fills.** Not click-click-click forty times. **A 3×4 of floor is one gesture.**

### ⚠ Textures are 1×1, with VARIANTS

**One image covers one square and repeats.** A KOTOR floor texture is a single-square thing.

**⚠ And repetition is solved the way `TRACE-95` found Daggerfall solving it: seeded, not re-rolled.** A tileset ships three or four floors and **the engine picks one from a hash of the tile's position** — same square, same variant, forever. **Varied without shimmering**, and it costs an author four drawings instead of one.

### ⚠ Multi-tile art is PIXELS ONLY. It never decides what a square IS

**A cargo-bay image spanning twelve squares changes how they LOOK and nothing else.** They were floor before and they are floor after.

**⚠ This is the load-bearing rule.** If art declared tile types, **two truths would exist about one square** — what the map says and what the art claims — and every one of *which wins*, *what happens on delete*, *what happens when two overlap* becomes a rule to write and a bug to find.

> **The map is the single answer. Art is decoration over a board that already knows what it is.**

**And the player-facing version: what you see is what the board IS.** A square that looks like floor is floor. **Nobody ever asks "why can't I walk there?"** — the question that ruins a tabletop app, because its answer lives in a file they cannot see.

### ⚠ Art SNAPS to the grid

**It cannot land half a square off, and it cannot be sized to a fraction of a tile.** Always exactly twelve squares, never eleven-and-a-bit.

**⚠ Snapping is what makes pixels-only cheap.** The objection — *paint first, then place art* — mostly dissolves when art can only land on squares that already exist. **And the Builder can then tell you when it does not fit**, because it knows both.

**And grid-locked art rotates in quarter-turns** — `TRACE-107` found Daggerfall's rotation is **two bits, four values across all 920 blocks.** *"A palette of 900 corridor pieces is unusable; 225 with a rotate key is a palette."*

### ⚠ A PREFAB is a saved selection — and it PASTES

**Paint a room, drop art on it, select it, save it. It is now in the palette and anyone can drag it into any map.**

**⚠ So a prefab is not a separate authored thing with its own format.** It is **what an author already made**, kept. That is the accessibility goal: **premade rooms for people who do not want to paint one, made by people who did.**

**⚠ And a prefab DOES carry tile types — which does not break the rule above, because a prefab PASTES rather than OVERLAYS.** Stamping writes tiles into the map and **then the prefab is gone.** What remains is tiles and art, exactly as if painted by hand.

**No live layer, no second source of truth, no delete semantics.** `PT-1361` still holds: **a prefab carries art and tiles from OUR fixed vocabulary, never a rule** — so a stranger's room cannot break your game.

---

## ⚠ 2·0d The canonical glyphs — `PT-1370`

**`§2`'s example gave `.` and `#`. The other three were the agent's invention, and it flagged that they are now written into every file the tool produces.**

| glyph | type |
|---|---|
| **`.`** | `floor` |
| **`#`** | `wall` |
| **`~`** | `water` |
| **`:`** | `difficult` |
| **`!`** | `hazard` |

**Adopted as written.** `~` for water is near-universal; `!` for hazard reads; `:` for difficult is arbitrary and **arbitrary is fine for a legend that is declared per-file.**

**⚠ Ruled now BECAUSE the cost of not ruling is asymmetric.** The agent's own warning: **a legend is per-file and both old and new files would parse**, so changing later means **either a migration or two conventions coexisting silently.** **Silent divergence is the worse outcome and the reason this is settled while three files exist rather than three hundred.**

**⚠ The legend is still written into every file.** These are the glyphs our tool emits — **not a fixed alphabet a hand-authored file must use.** A file declaring `W = "wall"` is legal and always was.

---

## ⚠ 2·0e TYPE, VARIETY, VARIANT — three words, `PT-1371`

**The palette shows FIVE things today and looked like it could only ever show five.** It cannot — **three different ideas were collapsed into one word.**

| | | |
|---|---|---|
| **TYPE** | `floor` `wall` `water` `difficult` `hazard` | **ours, fixed, five.** `PT-1361`. **Mechanics** |
| **VARIETY** | *deck plating* · *grating* · *scorched deck* | **all type `floor`, different art. ⚠ THE AUTHOR PICKS.** Unlimited, tileset-supplied |
| **VARIANT** | four near-identical deck platings | **the ENGINE picks**, seeded by position so a big room does not visibly tile. `PT-1367`. **The author never sees them** |

**⚠ So the palette lists VARIETIES GROUPED BY TYPE, not types.** With no tileset there is **exactly one variety per type — the drawn look** — which is why it looks like five. **The structure does not change when a tileset arrives; the lists get longer.**

### ⚠ Aurora is already this shape — copy it, do not invent one

**`STUDY 16`: the palette is two axes crossed — `Standard | Custom` × nine categories, each tab holding a tree of entries.**

**A category holds many entries; you pick an entry; the category is the mechanics and the entry is the thing.** That is **variety-grouped-by-type, built in 2002.**

### ⚠ And ONE DELIBERATE DEPARTURE, which is the most important line in the study

**Aurora's `Terrain` tab is STANDARD-ONLY and sits outside the nine.** It **separated the tiles you paint the ground with from the objects you place on it, and allowed custom content on the object side ONLY.**

> **⚠ Our varieties are precisely the thing Aurora refused to let be custom.**

**That is a departure, not a copy, and it is deliberate** — `PT-1361` is what makes it safe. **Aurora's palette entries are blueprints and carry RULES**; a creature has statistics. **Ours carry only art**, because the type vocabulary is fixed and a tileset supplies pixels against a list that already exists.

**So we can allow what Aurora could not, for a reason Aurora did not have.**

---

## 2a · ⚠ Tilesets — REOPENED and admitted, `PT-1360`

**`PT-1344` said an area has no tileset, and that was the wrong dismissal.** It ruled out **heightmaps, terrain meshes and walkmeshes** — 3D geometry, correctly gone at `PT-1319`. **But "tileset" in Aurora meant two things at once, and only one of them was geometry.**

**Two admitted. One deferred.**

### ⚠ ADMITTED — a tileset is a visual theme

**Same grid, same semantics, different art.** *Endar Spire* gives metal decking and bulkheads; *Taris Undercity* gives rubble and rusted plate. **A wall is still a wall — only the pixels change.**

```toml
[area]
tileset = "endar-spire"        # a package resource, not a global index
```

**⚠ This costs the engine nothing**, because it changes no rule. **And without it every area in every package looks identical** — flat squares forever, which is what `AREA-FORMAT-01 §6` was quietly heading toward.

**⚠ And it is the first concrete case of `PT-1351`'s open question.** A tileset is exactly the thing that could be **extracted from KOTOR's own floor and wall textures**, or **authored fresh and shipped.** Whichever way that goes, tilesets are where it lands first.

### ⚠ ADMITTED — a tileset carries PREFAB PIECES

**This is closest to what Aurora's tilesets actually were: you painted with PIECES, not with individual tiles.** A corridor section, a junction, a room.

**⚠ And it is the same one-verb Paint model at a larger grain.** `TRACE-106` found nine palette buttons all hinted `Paint …`; a prefab is another thing to paint. **It adds no verb.**

**Stamping a room beats painting forty squares**, and it is the difference between an authoring tool and a spreadsheet.

### ⚠ DEFERRED — a tileset declaring its own TILE VOCABULARY

**`§6` already asks whether a tile has a type beyond passable — cover, difficult terrain, hazard.** A tileset *could* declare its own: a ship has `bulkhead`, a swamp has `water`.

**⚠ More powerful and more dangerous.** If packages declare their own tile types, **the engine must handle types it has never seen** — and `ENGINE-INTERFACE-01`'s *fail loudly* rule means it would have to refuse them, which makes the package unloadable rather than merely plain.

### ⚠ RULED at `PT-1361` — a package invents NOTHING. The vocabulary is ours

> **Tile TYPES are predefined by us and fixed. Tile ART and PREFABS are anyone's and unlimited.**

**Ground, wall, water, and whatever else the rules need — we write the list, the engine knows every entry, and a tileset PICKS from it.** A water tile is water everywhere: **you cannot simply walk over it, and the engine knows that because the type is ours.**

**⚠ AND THAT SPLIT IS WHAT MAKES COMMUNITY TILESETS SAFE.** A tileset someone made in their bedroom **cannot break a package**, because there is nothing in it the engine has to understand. **It supplies pixels and prefabs against a vocabulary that already exists.**

| | Who defines it | How many | Can it break the engine |
|---|---|---|---|
| **tile TYPE** | **us, fixed** | a short list | it is the engine |
| **tile ART** | **anyone** | unlimited | **no** |
| **PREFABS** | **anyone** | unlimited | **no** |

**⚠ So the answer to "what if someone declares `quicksand`" is: they cannot, and they never needed to.** They make quicksand-looking art on a `difficult` tile. **The board still follows the rules.**

**This is a proper game board rather than decoration** — and it is the reason `PT-1334`'s exchange can accept a stranger's work without inspecting it.

---

## 2b · ⚠ How the grid LOOKS — the untextured default, `PT-1364`

**`§6` recorded this as completely untouched, and every mockup this session used flat squares marked placeholder.** Settled against three treatments drawn of the same room.

> **Walls are MASS. Floor is a lit surface. Grid lines are a whisper inside it.**

**⚠ The rejected version is the obvious one: thin lines with walls as dark squares.** It reads as a map, needs no art, and **walls read as ABSENCE rather than substance** — you infer the room instead of seeing it. **Too plain for the surface people look at most.**

**In the chosen version the floor reads as a surface, so the grid lines can drop away inside it** — you no longer need them to tell where a square is. **One outline traces the room's edge**, which is what gives it a shape.

### ⚠ This is the DEFAULT, and a tileset replaces it

**`PT-1361`: types are ours and fixed; art is anyone's.** So a tileset swaps deck plating in for the lit floor and ribbed bulkhead in for the wall mass — **identical grid, identical rules, different pixels.**

**⚠ And the default has to stand on its own, because it is the state a minimal package is always in** and the state everything will be in until a tileset exists. **A default that looks unfinished makes every package without art look broken.**

### ⚠ What does NOT change with the art

**Tokens and connections render identically in all three treatments.** `PT-1137` makes a token the sidebar portrait; a door is marked the same way whatever the floor looks like.

**The rule: what matters MECHANICALLY does not change appearance when the art does.** A player learning to read the board learns once.

---

## ⚠ 2·0f The area remembers its tag counter — `PT-1377`

**`4d` found a real defect and could not fix it honestly: a DELETED TAG IS REUSED BY THE NEXT PLACEMENT.**

**Allocation read the tags still in the file** — so delete `…02` and the next placement gets `…02` again. **Two different placed things share one tag across the life of the package**, which is exactly what `PT-1331`'s *never reassigned* exists to prevent, **and the log records tags.**

**⚠ It could not be fixed in the tool because the FILE KEEPS NO MEMORY of a retired tag.** The writer cannot know one existed. **Correct diagnosis, correctly escalated.**

### The fix: one integer, monotonic

```toml
[area]
name    = "Hangar"
size    = [16, 10]
tag_seq = 7          # ⚠ never decreases. The next tag is 8
```

**Tags become `sith-trooper.hangar.07` — readable as before, but numbered from the AREA's counter rather than from a per-template count of what is currently present.**

**⚠ Delete anything and the counter does not move.** A tag retired is retired forever, **because the file remembers the high-water mark rather than the survivors.**

**Why not a retired-tags list:** it grows without bound and **carries no information the counter does not.** One integer cannot go stale or disagree with itself.

**⚠ And this is `PT-1363`'s area-numbering rule made to actually work.** That ruled *one more than the highest, never one more than the count* — **which is correct only while the highest is still there.** Areas are rarely deleted; placements are deleted constantly. **The counter is what that rule needed all along.**

---

## 3 · Contents reference; they do not embed

```toml
[[contents]]
tag  = "guard.command-deck.01"          # PT-1331 — permanent, logged
from = "characters/sith-trooper"          # the template — ⚠ PT-1495, relative to blueprints/
```

> **⚠ THE PATH IS RELATIVE TO `blueprints/` — `PT-1493`. Loom's palette is the outlier.**
>
> **`TEST 014` found three places disagreeing and one of them is Loom:** it writes `blueprints/characters/probe-warden`, while **this document, `contents_writer`'s own doc comment, and `endar-spire`'s shipped contents all say `characters/…`.** **⚠ Three against one.**
>
> **And `PT-1452` settled the same convention for items:** `[equipment]` names **`items/weapons/blaster-rifle`**, not `blueprints/items/…`. **One rule, both folders.**
>
> **⚠ AND THE CONSEQUENCE IS THE HEADLINE: A CREATURE LOOM PLACES IS DRAWN AND IS NOT THERE.** `attack.dart` checks `startsWith('characters/')` and prepends the folder itself, **so a Loom-placed creature never resolves — and you can walk through it.**


at   = [12, 4]
```

**⚠ `from` is a PATH, never an index.** `ENGINE-INTERFACE-01`: *never expose an ordinal.* `TRACE-83` found position-as-identity across 155 KOTOR tables, and `F35` found the engine writing an appearance index **past the end of the table it indexed, with nothing rejecting it.**

**⚠ And `tag` follows `PT-1331`: a tag names ONE placed thing and is never reassigned.** A `role` may be refilled; a tag may not. **The log records tags.**

### ⚠⚠ `3a` · `hidden` — an ambush without the machinery, `PT-1550`

```toml
[[contents]]
tag    = "ambusher.command-deck.03"
from   = "characters/sith-trooper"
at     = [7, 1]
hidden = true                             # ⚠ PT-1550 — not shown until something reveals it
```

> **An author may place a creature that is not shown until something reveals it. A PROPERTY OF THE PLACEMENT, NOT A PERCEPTION SYSTEM** — one field, no checks. **An author says what is hidden; nothing computes it.**

**⚠ IT LIVES HERE BECAUSE IT IS A FACT ABOUT ONE PLACEMENT, not about a creature.** The same blueprint placed twice may be hidden once: `from` is a template and `hidden` is this instance's.

**⚠⚠ AND `LOOM MUST BE ABLE TO WRITE IT` — `PT-1440`: *anything the Builder cannot write, the Builder eventually destroys.*** **Today it cannot.** `ContentsWriter.render` emits exactly `tag`, `from` and `at`, so a hidden placement is a hand edit. **⚠ THAT IS A NEED FOR THE BUILDER REBUILD, NOT A DEFECT IN THIS RULING** — and it is the same shape as `conversation`, which `bed_creature_test:113` records as *read and written by nothing* until `PT-1425` gave Loom the field.

**⚠ AND THE HAND EDIT SURVIVES TODAY — checked, not assumed.** Loom **appends and removes whole entries and never rewrites one** (`ContentsWriter.append` / `withTagRemoved`; the only callers are `area_tab.dart:105` and `:183`). So `hidden` written by hand is not silently dropped by a later placement. **⚠ The moment that changes is the moment Loom gains an edit-in-place path** — which is exactly when the rebuild must carry the field.

**⚠ Absent means shown.** A placement with no `hidden` is visible, which keeps every area written before this ruling correct without migration.

### ⚠⚠ `3b` · `stealth` — how well it is hidden, `PT-1564`, `PT-1568`

```toml
[[contents]]
tag    = "ambusher.command-deck.03"
from   = "characters/sith-trooper"
at     = [7, 1]
hidden = true
stealth = 15                              # ⚠ moderate — SKILL-RESOLUTION-01 §2
```

**⚠⚠ THE NUMBER CARRIES ITS OWN LABEL, AND THERE IS NO SECOND FIELD.** The seven tiers of `SKILL-RESOLUTION-01 §2` — trivial 5 · easy 10 · moderate 15 · hard 20 · formidable 25 · heroic 30 · legendary 35, **the middle five being `traps.2da`'s own values** — are offered as a dropdown, and **the FILE carries the number.** Nothing stores the word.

> **`PT-1546` in one field.** Aurora's Encounter category was filed under *Hard*, named *"Hard 001"*, with Difficulty *"Easy"*, and nothing in the UI distinguished the category from the property. **A label computed from a number cannot disagree with it.**

**⚠ And a number off the ladder is still a number.** `§2` names ±2, ±5 and ±10 as its modifiers, so the ladder **recommends rather than constrains** — the dropdown is the recommended values, not the permitted ones.

**⚠⚠ AND A `stealth` WITHOUT `hidden` IS A LOAD FAILURE, NOT AN IGNORED FIELD.** It is how well something in plain sight is hiding: the author has said two things that cannot both be true, and **silently keeping one is exactly the defect above.**

### ⚠⚠ AND IT IS A `stealth` TOTAL BECAUSE A SETTLED DOCUMENT SAYS SO — `PT-1568`

**`SKILL-RESOLUTION-01` is SETTLED (`D-AO`)** and says:

> *"Three of KOTOR's eight skills do not roll against anything… **Stealth and Awareness are a contested pair.** A system that assumed every skill has a DC would have got three of eight wrong."*

and `§4`: ***"the defender rolls the better of Awareness or Alertness"*** — an **OPPOSED** roll.

**⚠ So a fixed DC for Awareness is a resolution mode that document says the skill does not have.** `PT-1564` proposed `dc`; `PT-1568` renamed it **before anything authored against it**. The number is unchanged — **what a finder must beat** — and it is now named for what it is: **the hider's total.**

**⚠ AND `stealth` IS OUR OWN WORD FOR OUR OWN SKILL.** `PT-1547` bars a coined name that collides with something our data already uses; this is the opposite move — **it names the thing the data has**, rather than inventing a term beside it.

**⚠ The seven tiers stay as recommended VALUES.** `§2`'s ladder is what a number to beat looks like at each tier, and **an opposed roll needs one just as a fixed DC does.**

### ⚠⚠ `PT-1571` — NO PER-SPECIES AND NO PER-CHASSIS PERCEPTION TABLE

> **One default, and an author may override it on a placement.**

**⚠ AND IT IS RULED ON DATA RATHER THAN ON SILENCE**, which is the difference between a gap and a finding. Across **4,397 blueprints in both games**, two races, non-default rates of **2.4% against 2.1%**:

> **KOTOR had the field, had the two races, had 4,397 chances, and used it to separate droids from organics ZERO TIMES.**

**⚠ So a per-species table would be OURS, and would be inventing one.** `PT-1424` already found `speed` derived from species rather than stored; this is the same question answered the other way **because the data answered it.**

**⚠ AND THE OVERRIDE IS ON THE PLACEMENT, WHICH IS WHERE `TRACE-83` PUTS IT** — *"an instance is a template plus a named set of permitted overrides."* But `AUTHORED-CHARACTER-01 §3`'s guard is that an override is **declared on the TEMPLATE, never patched onto an instance**, and `TRACE-83` is the evidence for that guard. **The two must be reconciled before the field is written.** Named here rather than assumed either way.

### ⚠⚠ `3c` · `range` — how far off it can be noticed, `PT-1571`, `PT-1573`

```toml
hidden  = true
stealth = 15
range   = 4                               # ⚠ SQUARES. §9 makes one 2 metres
```

**⚠⚠ AND THE NUMBER IS OURS.** KOTOR gives the PLAYER **250 m of sight**, which on our grid is **125 squares — the whole area.** That is a constraint of a real-time 3D game **where the player owns the camera**, not an answer about perception. `PT-1496`: **Aurora's ANSWERS transfer; Aurora's CONSTRAINTS do not.** This is a tabletop RPG and a GM uses distance.

**⚠ TWO INDEPENDENT SOURCES ARRIVE AT TEN SQUARES:**

    KOTOR's effective distances   10 m · 20 m · 35 m, 97.8% on the 20 m default
    RCR darkvision                20 m, flat
    RCR scent                     10 m

**`20 m ÷ 2 m = 10 squares`**, and `§9`'s square makes every one convert **exactly** rather than nearly. **The default is what 97.8% of 4,397 blueprints already carried** — the opposite of a number invented to make a rule runnable.

**⚠ ONE DEFAULT AND AN OVERRIDE ON THE PLACEMENT, NEVER A TABLE — `PT-1571`, and ruled on DATA.** 4,397 blueprints, two races, non-default rates of **2.4% against 2.1%**: *KOTOR had the field, had the two races, had 4,397 chances, and used it to separate droids from organics **zero times.***

**⚠ And a `range` follows `stealth`'s rules**: hidden only, a whole number, and **above zero** — a range of zero is a creature nothing can ever notice, and that is not what `hidden` means.

### ⚠ HOW IT IS FOUND — ruled at `PT-1569`/`PT-1573`, and BUILT

    on approach       after every step, and after arriving in an area
    passive           the finder's number TAKEN AT 10, no dice
    settled once      a failure stands; there is no retrying it

**⚠ AND IT IS AN OPPOSED PAIR, NOT A DC.** `§4`: **the defender rolls the better of Awareness or Alertness** against the hider's `stealth`. **Two skills that fail differently is worth more than one that is simply better** — without a stealth field sight leads, with one hearing does. Nothing models the field yet; **taking the better of the two is what makes it expressible later without changing this.**

**⚠⚠ AND A DISTANCE IS THE GREATER OF THE TWO AXES — `PT-1581`, and it was ALREADY RULED BEFORE THAT.**

**`PLAYTEST-RULINGS-01:238`:** *"**Grid diagonals** — Ruled here: **diagonal costs 1 square**, diagonally touching is adjacent, and diagonal adjacency satisfies both melee reach and flanking."* **One sentence carrying three rulings**, and `PT-4` at line 117 rules flanking geometry consistently with it.

> **⚠⚠ AND THIS PARAGRAPH USED TO ASSERT THE OPPOSITE.** It said *"nothing in the corpus says whether a diagonal counts as one square or more"* and called the number mine. **It does say, and it had said all along.**
>
> **That is a scoped negative that searched the wrong shelf** — `design/` and `rules/`, and **not `playtest/`.** The same defect this corpus keeps finding, in a document rather than in code: *a claim about absence is only as wide as the search behind it, and this one did not name its scope.*

**⚠ AND `REACH` AND `COST` ARE ONE FUNCTION ONLY BECAUSE THE COST IS ONE.** `squaresBetween` answers *how far*; a diagonal step costs what any step costs. **Had the cost alternated — d20's 1, 2, 1, 2 — they would have had to be two**, because an alternating cost depends on the path taken and a reach does not.

**⚠ `PT-1550`'s CONTACT IS THE REVEAL remains the floor and is built** — walking into a hidden creature always finds it, whatever the numbers say.

**⚠ RULED AT `PT-1573`: FIND ON APPROACH**, against find-on-notice. **And the reason it needed a ruling is that at KOTOR's 250 m the two are the same rule wearing different words** — 125 squares is the whole area, so *"on approach"* and *"on entering"* would have been indistinguishable and a hidden creature would never have been a surprise.

**⚠ SO THE DISTANCE HAD TO BE OURS BEFORE THE RULE COULD RUN**, and `§3c` is where it came from.

### ⚠ And what is NOT here — `PT-1550`

**Fog of war on the terrain is ruled OUT.** `wall.blocksSight` **stays `true` and stays UNREAD** — the field is right and nothing consumes it, which `PT-1529` established is a **roadmap rather than a defect**.

> **The board shows what is in the area. What perception governs is WHO IS STANDING IN IT.**

**⚠ The reason is that fog needs a system we do not have.** Hiding requires something to hide **and rules for finding it** — a stealth score, a perception check, a detection radius. **We have none.** Building fog without them produces the worst version: **everything visible except what a wall blocks**, which hides nothing interesting **and stops you seeing the room you are standing in.**

**⚠ AND THE MAP IS THE HALF THAT MATTERS AND IS BUILT — `PT-1509`.** What this character has **stood in** is a real fog of war — **of the WORLD rather than the room** — and it is per-character, so a droid and a Jedi genuinely know different things.

---

## 4 · ⚠ Connections are named on both sides

```toml
[[connections]]
tag  = "door.command-deck.aft"
at   = [23, 9]
to   = "a02-taris-hideout"
lands = "north"                 # a named point IN the target
```

**`lands` names a point, not coordinates.** `TRACE-83` found KOTOR's waypoints override seven fields where a creature overrides six — **arrival points were load-bearing there and they are here.**

**⚠ And the target area must declare that name**, or loading fails loudly per `§6`. **A connection to a point that does not exist is exactly the class of error `F35` shows an engine silently accepting.**

### ⚠ 4·0 An area DECLARES its arrival points — `PT-1378`

**`§6` asked whether an area declares its own points or any coordinate may be named. `4e` stopped on it. Ruled: the area declares them.**

```toml
[[arrivals]]
name = "north"
at   = [12, 0]
```

**And a connection lands on one by name:** `lands = "north"`.

**⚠ The argument is the agent's and it is decisive:** `§4` requires loading to **fail loudly** on a connection naming a point that does not exist. **You cannot fail loudly against a rule that says any coordinate is fine.** A validatable reference needs something to validate against — **so the alternative was never really available.**

### ⚠ An arrival point is neither of Aurora's two waypoints

**`STUDY 17` found Aurora has BOTH**, and the agent corrected its own earlier report to say so:

| | |
|---|---|
| **Aurora's palette waypoint** | a **blueprint instance** — needs a template |
| **Aurora's context waypoint** | a **patrol point owned by a creature** |
| **⚠ OURS** | **a named coordinate owned by the AREA** |

**So the context menu is the wrong home.** Aurora's context verb attaches a patrol point **to a creature**; ours is named by a door **in another area**, no creature owns it, **and you cannot arrive on top of a guard** — it must go on empty floor.

**⚠ The gesture that transfers is the palette one: pick a thing, click a square.** Which is what placing already is.

### ⚠ No template, and no tag

**An arrival point is a name and a coordinate.** No blueprint, no stats, no art — **so unlike every other placeable, it needs no `blueprints/` folder.**

**And no `tag`.** A tag identifies a thing **the log records** (`PT-1331`); the log records that a character *moved*, not that a doorway exists. **`name` is unique within its area and that is all it needs to be.**

---

### ⚠ 4a · A door is CONTENTS that also connects — `PT-1362`

**`TRACE-107` caught the format naming something it could not model: `§4`'s own example is `door.command-deck.aft`, and a connection has no lock.**

```toml
[[connections]]
tag   = "door.command-deck.aft"
at    = [23, 9]
to    = "a02-taris-hideout"
lands = "north"
from  = "doors/blast-door"        # ⚠ OPTIONAL — omit it and it is a doorway
```

**⚠ `from` is the whole change.** No template means an opening you walk through. **The connection is unaltered otherwise.**

### Why a template rather than a lock field on the connection

**The toolset decides it, and the number is the argument. `TRACE-107`: 104 `UTD` blueprints ship in KOTOR 2.** Aurora made a door a full blueprint type **because doors repeat** — the same blast door appears in a dozen places and you author it once.

**⚠ A lock field on a connection cannot do that.** Ten identical doors become **ten copies of the same values**, and changing the blast door means editing ten connections. **That is exactly `TRACE-83`'s finding: 1,589 blueprints for 1,619 placements**, because references pointed at specific things rather than shared ones.

**And we already have the pattern** — `§3` has contents referencing a template by path with a permanent tag. **A door is contents that also connects.**

### ⚠ Four capabilities, not fifty-six fields

**Shut · locked · opened by a key · broken.** `TRACE-107`: one `UTD` sample carries **fifty-six fields including sixteen script hooks**, and that is **the same disease as the 112-field creature.**

**⚠ `OnOpen` is an EVENT KIND, not a field.** `PLAY-STATE-01` makes state a projection of the log, so **a door's runtime state was never going to live here** — `§5` already rules that.

### ⚠ The lock uses the GATE vocabulary, not its own DC

**`RULES-02 §3`'s gate already exists:** `free`, or `any_of` — **attitude, `skill + DC`, payment.** Built for the character brain, and **it is the same question a locked door asks.**

**So picking a lock is `skill: security, dc: N`** — one mechanism, not two. **And it already renders**: `PT-1307` gives it `[Security]` on a dialogue option, and a door is the same gate in a different place.

**⚠ Attitude and payment fall out for free and are not nonsense** — a door someone opens *for* you, or a bribe to the guard holding the key.

---

## 5 · What is NOT in an area

**No lighting, no camera, no music cue, no fog.** `PT-1319` removed the render layer; **an area that described lighting would be describing something nothing reads.**

**No scripts inline.** `PACKAGE-FORMAT-01 §5` ships source as files; an area **references** a script by path.

**⚠ No runtime state.** No door open-ness, no character position after play begins, no visited flag. **`PLAY-STATE-01`: state is a projection of the log.** An area is authored content and never changes.

**⚠ This is the rule most likely to be broken first**, because a door has an obvious open/closed and it is tempting to put it here. **The door's authored state is its starting state; everything after is an event.**

---

## 6 · Open

- ~~The run notation for tiles~~ ✅ **RULED at `PT-1345` — a text map.** The test package is unblocked.
- ~~The grid's visual design~~ ✅ **RULED at `PT-1364`** — `§2b`. **Walls are mass, floor is a lit surface, grid lines whisper.** Still open: exact weights and colours, which want a real viewport.
- **Whether a tile has a TYPE beyond passable.** Cover, difficult terrain, hazard — **`ENGINE-SPEC-04` may already require these; not checked.** **⚠ And `§2a` deferred a related question: whether a TILESET may declare its own types.**
- **Elevation.** The Undercity is below the Lower City. **Is that separate areas connected, or one area with levels?** `PT-1313`'s locality graph says separate zones, which suggests separate areas.
- ~~Whether an area declares its own arrival points~~ ✅ **RULED at `PT-1378` — it declares them.** `§4·0`.
