# STUDY 10 — WHAT TO BUILD ON

*A recommendation, not a study. Part one is background. Part two is the answer.*

**⚠ One honest caveat before anything else.** Parts of this rest on my knowledge
of tool ecosystems rather than on files I opened. Version numbers and current
release states in particular may have moved since my information was current —
**verify the specific versions before committing.** The architectural reasoning
does not depend on them; the maturity claims do.

---

# PART ONE — WHAT THE GAMES WERE BUILT ON

## Briefly, and it is mostly irrelevant

| | KOTOR 1 | KOTOR 2 | NWN |
|---|---|---|---|
| engine | Odyssey (BioWare) | Odyssey, Obsidian fork | Aurora (BioWare) |
| language | C++ | C++ | C++ |
| rendering | fixed-function OpenGL/D3D8 era | same, plus shader work | same lineage, older |
| scripting | NWScript → NCS bytecode | same | same |
| UI | own immediate-ish panel system | same | same |

**We will use none of it.** It is 2003 C++ against a fixed-function pipeline,
and every architectural decision in it was shaped by a 64 MB Xbox.

The class names visible in the binaries — `CExoKeyTable`, `CExoLinkedList`,
`CExoString`, `CExoMoviePlayerInternal` — are BioWare's own C++ foundation
library, which is the only interesting thing about the code layer: **they wrote
their own containers and string type rather than using the STL**, which was
normal for 1999 and tells you the codebase predates the games by years.

---

## ⚠ The UI layer, in detail — and what a reimplementation would require

This is the part that matters, because you are reproducing it.

### What a KOTOR panel actually is

A `.gui` file is a **GFF tree, at most two levels deep**, of absolutely
positioned controls. Verified across every panel in both games:

```
                       K1 (84 panels)      K2 (159 panels)
Label                       1,155                2,509
Button                        711                1,147
Panel                          84                  159
ListBox                        81                  157
ScrollBar                      81                  157
ProtoItem                      77                  177
Progress                       75                   98
CheckBox                       73                  113
Slider                          7                   14
nesting depth 0 / 1 / 2   84 / 2,099 / 161   159 / 4,060 / 312
```

**Nine control types. No text input. No tabs, no menus, no tree view, no
grid, no combo box, no tooltip, no modal.**

### What a control carries

```
EXTENT        LEFT · TOP · WIDTH · HEIGHT     absolute, in a fixed design space
BORDER        the normal visual state
HILIGHT       the hover state
SELECTED      the toggled state          }  present on only 73 K1 / 113 K2 controls
HILIGHTSELECTED  toggled + hover         }  — i.e. only CheckBoxes
TEXT          the text block
PROTOITEM     the row template, on ListBoxes
SCROLLBAR     a nested control
COLOR · ALPHA · PADDING · DRAWMODE · LOOPING · PULSING
```

Each visual state block is:

```
CORNER · EDGE · FILL      three greyscale texture resrefs — a NINE-SLICE
DIMENSION                 border thickness in pixels, DECOUPLED from texture size
INNEROFFSET               content inset
COLOR                     an RGB triple applied as a runtime TINT
FILLSTYLE                 how the centre is filled
PULSING                   an animation flag
```

Observed `DIMENSION` values: 0 (no border) on the large majority, then 1, 2, 4,
6, 14, 16, 32 in K1; K2 adds 3, 8, 9, 18, 24 and uses **16 heavily (919
controls)**.

And the text block:

```
FONT        a resref — 'fnt_console', 'dialogfont16x16'
TEXT        a literal string, or
STRREF      an index into the game-global string table
ALIGNMENT   a BITFIELD: H-left 1 · H-centre 2 · H-right 4
                        V-top 8 · V-centre 16 · V-bottom 32
COLOR · PULSING
```

### ⚠ So what would a modern toolkit have to do

**Eight requirements, and only the last is a problem.**

1. **Nine-slice draw from three greyscale sources, tinted at runtime, at an
   arbitrary border thickness that is not the texture's own size.** This is the
   core primitive and everything visual is built from it.
2. **Absolute positioning in a fixed design space**, with resolution handled by
   *authoring separate panels per resolution* — the games ship `8x6`, `10x7`,
   `12x9`, `16x12` families. No layout engine is wanted; a constraint solver is
   an obstacle here, not a help.
3. **Bitmap fonts from a texture atlas**, with a uniform advance. (Earlier work
   established the console font as 8×8 cells on a 16×16 sheet, 127 glyphs.)
4. **Four visual states per control**, styled independently.
5. **Per-control alpha and colour tint**, animated (`PULSING`).
6. **A row-template list** — `ProtoItem` is a control used as a repeated row.
7. **Text resolved from an integer index** into a string table.
8. **⚠ Real text input, which the source gives you no pattern for at all.**

**On point 8 — say it plainly.** Both games have exactly **two** typed fields
(a character name and a save name) and both are **`Label` controls the engine
writes keystrokes into**. There is no edit-box control type in the format.

Your primary dialogue interface is free-typed text. **The UI vocabulary you are
reproducing cannot express your most important control**, so that one is
designed from scratch regardless of stack — and it needs to look like it belongs
beside eight controls that were never designed to have a sibling like it.

**Nothing in requirements 1–7 is hard for any modern toolkit.** They are all
"draw an image nine ways and put a glyph at an exact pixel." The question in
part two is not *can* a stack do this — all three can — but *how much the stack
fights you while you do it*.

---

# PART TWO — WHAT TO BUILD ON

## The requirements, restated as technical constraints

1. **2D, custom-drawn, pixel-exact.** Not native widgets. Not a document layout.
2. **Desktop and mobile** from one codebase.
3. **A grid play surface** — pan, zoom, hit-test, tokens.
4. **App-shaped surfaces too** — character sheet, inventory, dialogue.
5. **A Builder**: a desktop authoring tool. Trees, inspectors, text editing,
   file dialogs, undo. IDE-shaped.
6. **⚠ One shared engine**, called by both, or they drift.
7. **Multiplayer, host-is-server.**
8. **An AI layer** for dialogue and generation.
9. **⚠ Stability weighted heavily. Boring beats clever.**

**Requirement 6 is the one that rules things out**, and the ruling is simple:
**if the app and the Builder are written in different languages, the engine has
to be callable across a language boundary.** That means either an FFI layer, a
local RPC, or writing the rules twice.

All three are worse than the alternative. **The cheapest correct answer is one
language for the engine, the app and the Builder.** That single decision
eliminates most of the option space, and everything below assumes it.

---

## Option A — Flutter (Dart)

**What it makes easy.**

Flutter **does not use native widgets at all.** It ships its own renderer and
draws every pixel itself. That is not a workaround you adopt for pixel control —
it is the framework's founding decision, and it means your requirement 1 is the
default rather than a fight.

`CustomPainter` gives you a raw canvas with transforms, clipping and blend
modes. Nine-slice is built in (`centerSlice` on image drawing) and trivially
hand-rollable when you need the decoupled `DIMENSION` behaviour. Colour tinting
is a `ColorFilter`. Bitmap-font atlas rendering is a straightforward custom
painter.

One codebase genuinely covers Windows, macOS, Linux, Android and iOS.

**The Builder is where this option wins.** It is an IDE-shaped tool, and Flutter
is good at IDE-shaped tools — scrolling trees, split panes, property
inspectors, text fields, file pickers — while still drawing everything custom,
so the Builder can share the app's visual language instead of looking like a
different product.

**What it makes hard.**

No game loop, no sprite batching, no scene graph, no built-in physics or
particles. Your grid surface is a `CustomPainter` you write, including pan/zoom
maths and hit-testing. Thousands of apps do this; it is real work rather than
free.

**No built-in multiplayer.** You write the netcode over sockets. Host-is-server
is straightforward but it is yours to build.

Dart's ecosystem is smaller than JavaScript's. AI SDKs are Python- and
JS-first, so you call HTTP endpoints directly. That is fine — the APIs are HTTP
— but you write the streaming client rather than importing one.

**The risk.** Flutter has been through a renderer migration (Skia → Impeller).
Renderer changes are exactly the kind of churn that bites a pixel-exact project,
because "looks identical" is your acceptance criterion. **Check the current
state of that migration on your target platforms before committing.**

**Maturity.** Stable since 2018, Google-backed and load-bearing for Google's own
products, breaking language changes rare and well-managed. On the stability axis
this is a strong showing — with the renderer caveat above as the one real
question mark.

---

## Option B — Godot 4 (GDScript or C#)

**What it makes easy.**

Godot is a game engine, and roughly half your requirements are game-shaped.

`NinePatchRect` is **literally the control KOTOR's border system describes** —
a nine-slice image with configurable margins, plus `modulate` for runtime
tinting. The `Theme` system does per-state styling. `Control` nodes position
absolutely by default. Bitmap fonts are a supported font type.

The grid surface, sprites, audio, animation and scene management come free.
So does **multiplayer**: Godot ships a high-level networking API whose default
shape is authoritative-host, which is your requirement 7 almost exactly.

Exports to desktop and mobile from one project.

**What it makes hard.**

**The Builder.** Building an IDE inside a game engine means building trees,
inspectors, dockable panels, text editing and file dialogs out of `Control`
nodes. Godot's own editor proves it is possible — but Godot's editor is a large
C++ project, not a weekend of GDScript.

If you write the engine in GDScript you are betting the rules layer on a
game-engine scripting language: dynamically typed, engine-coupled, awkward to
run headless or on a server, and hard to unit-test outside the editor. If you
write it in C# you get a better language and inherit .NET-on-mobile as an extra
risk surface.

**The risk.** The Godot 3 → 4 transition broke a great deal and was painful for
projects mid-flight. That is a real signal about future churn tolerance on a
multi-year project. 4.x has settled substantially since release, but the
precedent is recent.

**Maturity.** Godot 3 was very stable. Godot 4 arrived in 2023 and has matured
across several releases; C#-on-mobile support arrived later than the core. It is
mature enough to build on and it is the youngest of these three by some margin.

---

## Option C — TypeScript, canvas/WebGL, shipped via a shell

**What it makes easy.**

TypeScript is the most boring language of the three, in the way you want:
enormous ecosystem, huge hiring pool, exceptional tooling, and a language spec
that changes carefully.

**Drawing to a canvas sidesteps the thing you ruled out.** You said not a
conventional web layout — canvas is not one. You get an immediate-mode surface
and full pixel control, and you never touch CSS layout for the game UI.

**The AI layer is best-in-class here** — every model SDK is JS-first, streaming
included, and you will be writing that integration whichever way you go.

The engine as a plain TypeScript module is imported identically by app, Builder
and — if you ever want it — a server. That is the cleanest possible answer to
requirement 6.

**What it makes hard.**

**You assemble the shipping story from parts.** Desktop needs Electron (mature,
heavy) or Tauri (lighter, Rust toolchain, mobile support is comparatively
recent). Mobile needs Capacitor or a PWA. That is two or three separate
packaging technologies, each with its own release cadence — and **that assembly
is the least boring thing in this document**, despite the language being the
most boring.

Canvas means you implement everything: hit-testing, focus, keyboard navigation,
scroll momentum, text input handling. Requirement 8 — the typed dialogue box —
is genuinely easier here than anywhere, because you can overlay a real DOM
`<input>` on the canvas. That is a meaningful point in its favour.

**The risk.** Webview performance on low-end mobile, and the packaging layer
churning under you.

**Maturity.** The language and browser APIs are extremely stable. Electron is
very mature. Tauri's mobile support is the newest thing named in this document
and I would not bet a long project on it without checking its current state
carefully.

---

## ⚠ What I would pick, and why

**Flutter.**

The reasoning, in order of weight:

**1. It is the only one of the three where "no native widgets, we draw
everything" is the framework's own design rather than something you impose on
it.** Your hardest constraint is its default. With Godot you are using a game
engine's UI layer for an app; with canvas you are building a UI layer from
scratch. With Flutter you are using the thing as intended.

**2. The Builder decides it.** You are building two applications, and one of
them is an authoring tool with trees, inspectors and text editing. That is the
piece Godot is worst at and Flutter is best at, and it is not a small piece of
the project. Choosing a stack that is excellent for the play surface and painful
for the Builder optimises the wrong half.

**3. One language, no boundary.** Dart for the engine, the app and the Builder.
Requirement 6 is satisfied by construction rather than by an FFI layer you
maintain forever. The engine can also run headless for tests, which matters more
than it sounds for a rules system you will be changing for years.

**4. The desktop-and-mobile story is genuinely one codebase**, which is not
quite true of the canvas option and is true-with-caveats of Godot.

**What you give up, stated honestly:** Godot's free multiplayer and free game
loop. You will write netcode and a render loop that you would not have written
otherwise. That is perhaps a few weeks of work, once — against a Builder that
would be painful for the life of the project.

**When I would switch to Godot instead:** if the play surface turns out to be
more game than app — real-time animation, many simultaneous moving sprites,
particle effects, or if the KOTOR-style cutscene staging you studied in batch 6
becomes a feature you actually want rather than a reference. At that point
Godot's free scene system and networking outweigh its bad Builder, and the
answer becomes *Godot for the app, and accept that the Builder is a separate
Flutter or web application sharing a file format rather than a library.*

**When I would switch to TypeScript instead:** if the AI layer turns out to be
the dominant complexity rather than the UI, or if hiring is a constraint. Both
are plausible and neither is knowable yet.

---

## What I would rule out, briefly

**React Native, or anything mapping to native OS widgets.** Directly contrary to
your stated constraint. You would spend the project fighting the framework's
purpose.

**Unity.** Its 2D custom-UI story is weaker than Godot's for this specific job,
it is much heavier, and the 2023 licensing episode is a stability signal of a
different kind — the risk is commercial, not technical, and you are weighting
stability heavily.

**Rust GUI toolkits (egui, iced) or Bevy.** Genuinely interesting and genuinely
too young. "Boring and solid" excludes them.

**Qt/QML.** Good custom drawing and very mature, but the mobile story is weak
and the commercial licensing is a live consideration for a shipped product.

**⚠ Different stacks for app and Builder with a shared native engine library.**
This is the tempting one and I would avoid it. It buys you the best tool for
each front-end and costs you an FFI boundary, two build systems, two debugging
stories, and a marshalling layer between the rules and everyone who calls them.
For a project weighting stability, one language everywhere is worth more than a
locally optimal choice on each side.

---

## The one thing to prototype before committing

**Build a single KOTOR panel, faithfully, in your top two candidates.**

Take one real panel — `character_p` or `equip_p` — and reproduce it: nine-slice
borders from three greyscale sources tinted at runtime, a bitmap font at exact
metrics, four control states, and a `ProtoItem`-style list with a scrollbar.

That is perhaps two days per candidate and it answers the only question that
actually matters here, which is **how much the toolkit fights you when the
acceptance criterion is "identical."** Every other consideration in this
document is a judgement; that one is a measurement.

**And prototype the text input on the same panel**, because it is the control
the source cannot teach you and the one your design depends on most.
