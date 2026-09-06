# SPIKE — RESULT

**Answering `FAIL-CONDITIONS.md`, which was committed at `65e3fdd` before the
first line of Dart.** Every verdict below is against a condition written in
advance. Nothing here was scored after the fact.

**The question was:** does Flutter fight us when the acceptance criterion is
"identical to KOTOR"?

**The answer is no.** Zero hard fails, one soft fail, one partial soft fail.
Everything that fought me on this spike turned out to be my own misreading of
KOTOR's data — three separate bugs, all mine, none Flutter's. The one real
Flutter limitation is a second native window, and it is a hard limitation on the
stable channel, proven rather than assumed.

---

## 1. What exists, and where

Built, run, and photographed on Linux against a real X display with a GTX 1070.

| piece | file | lines |
|---|---|---|
| nine-slice painter | `code/nine_slice.dart` | 115 |
| bitmap-font renderer | `code/bitmap_font.dart` | 68 |
| engine call | `code/engine.dart` | 53 |
| text input | `code/text_input.dart` | 78 |
| the panel | `code/panel.dart` | 226 |
| app shell, menus, dialogs | `code/main.dart` | 172 |
| multi-window probe | `code/probe_window.dart` | 34 |
| **hand-written total** | | **746** |

Plus `panel_data.dart`, **2,060 lines of generated geometry** read out of the
shipped `equip_p.gui` — not hand-written, not committed, regenerable.

**No game art is committed.** `ASSET-REPLACEMENT-01` governs. Seventeen textures
were extracted to PNG as prototype source and live only in the local scratch
tree, and the screenshots I worked from are described here rather than embedded.

### Why `equip_p` and not `character_p`

Chosen on counts, not taste:

```
character_p  56 controls  {Label:50, Button:4, Panel:1, Slider:1}
             states {BORDER:56, HILIGHT:5}   DIMENSION {0:53, 16:8}
equip_p      54 controls  {Label:32, Button:17, ListBox:2, ScrollBar:2, Panel:1}
             states {BORDER:54, HILIGHT:17}  DIMENSION {0:36, 4:2, 16:33}
```

`equip_p` is the only one of the two with a ListBox and a ScrollBar, which the
brief requires, and it has four times as many hilightable controls to test
states against.

**⚠ A correction to something I said mid-spike.** I reported that `equip_p`
contains zero ProtoItems. **That was wrong.** It has two — one per ListBox,
tagged `PROTOITEM`, typed as buttons, parented to `LB_ITEMS`. My census counted
the `type` field and missed them because they are typed `button`, not
`protoitem`. The list in the spike is stamped from the real template at
`94,150 270x62`, `DIMENSION 16`, `INNEROFFSET 10`, `dialogfont16x16`,
`ALIGNMENT 18`.

---

## 2. Environment — and which half is Flutter's fault

Per the exclusion in the fail conditions, container friction is reported
separately from Flutter friction.

**Container (not Flutter's problem, and not the owner's):** no root, no
`clang`, `cmake` or `ninja`. Solved without root by fetching Debian `.deb`
packages with `apt-get download` and extracting them with `dpkg-deb -x` into a
prefix on `PATH`. That yielded clang 19.1.7, cmake 3.31.6, ninja 1.12.1.
`libgtk-3-dev`, `pkg-config` and GTK 3.24.49 were already present. About forty
minutes, most of it a 1.5 GB SDK download.

**Flutter:** 3.47.2 stable, Dart 3.13.2. `flutter doctor` reports the Linux
toolchain green once clang is visible. No patching, no forks, no unsupported
flags.

**Build times measured on this machine:**

```
warm debug rebuild        9.1 s
release build            29.8 s
release bundle size      23 MB
```

The release binary runs with `PATH` and `LD_LIBRARY_PATH` stripped entirely —
it needs nothing from my hand-built prefix, which was only ever a build-time
requirement.

---

## 3. The hard fails, answered

### F1 · Nine-slice with border thickness decoupled from texture size — **DID NOT HAPPEN**

The premise is real and measurable. All six border textures used by `equip_p`
are **32×32**, and the panel draws them at **`DIMENSION` 16** — thickness is
exactly half the source. A ListBox at `318×364` and a button at `54×54` share
the same textures at the same `DIMENSION`.

`CustomPainter` draws this without complaint. The destination rect is whatever
you pass to `drawImageRect`; it has no relationship to the source size. There is
no nine-slice API to fight because I did not use one — `centerSlice` is the
thing that would have constrained me, and it is simply not what this needs.

**What I got wrong, twice, before getting it right:**

1. I stretched the edge and fill textures across the run. KOTOR **tiles** them.
   Stretching a 32-pixel edge across 300 pixels produced horizontal smears
   across the whole panel.
2. I set `FilterQuality.none` globally, for exactness. Correct for a 32-pixel
   mask, wrong for a 1024-pixel backdrop drawn into 800 pixels, which moirés
   into stripes.

The fix for both is one function, and it is the transferable lesson:

```dart
// ⚠ FILTER QUALITY IS PER-DRAW, NOT GLOBAL.
Paint _paint(Rect src, Rect dst) => Paint()
  ..colorFilter = ColorFilter.mode(tint, BlendMode.modulate)
  ..filterQuality = (dst.width < src.width || dst.height < src.height)
      ? FilterQuality.medium
      : FilterQuality.none
  ..isAntiAlias = false;
```

Neither mistake was Flutter resisting. Both were me not having read the source
data carefully enough.

### F2 · Runtime tint of a greyscale source without a shader — **DID NOT HAPPEN**

`ColorFilter.mode(tint, BlendMode.modulate)` on the `Paint`. One line. No
fragment shader, no `FragmentProgram`, no `.frag` asset, no build step.

This matters more than I expected, because **every texture in the panel is a
mask**. The 1024×1024 backdrop included. Nothing in `equip_p` is pre-coloured.
Tint-at-runtime is not a feature of this UI, it is the entire rendering model,
and it costs one property on a `Paint`.

`modulate` is the right blend, not `srcIn`. `srcIn` works only where the source
RGB is white. Two of the textures are not: `uibit_brdr_16gc` and `_16ge` carry
RGB 24, and the backdrop is a real image. Multiply handles all three cases;
`srcIn` would have flattened two of them.

### F3 · Exact integer glyph placement — **DID NOT HAPPEN**

Flutter's *text stack* would indeed have fought this — it shapes, hints and
subpixel-positions, which is right for prose and wrong for a 16×16 atlas. So I
did not use it. `canvas.drawAtlas` takes a list of `RSTransform` and source
rects and blits cells, one draw call for a whole run, with positions I round
myself:

```dart
x = x.roundToDouble(); y = y.roundToDouble();
```

The atlas maps cleanly: **cell index equals codepoint**. `@` sits at 0x40, `A`
at 0x41, and the 16×16 grid of 16×16 cells covers 0–255. Verified by eye
against the decoded atlas.

The fail condition was about whether Flutter *insists*. It does not — the
canvas API is right there underneath the text stack, unguarded.

**Two honest limits of what I built, neither of which is F3:**

- **The font is proportional and I rendered it monospaced.** I advance a fixed
  16 pixels per glyph. Real KOTOR stores per-character metrics outside the
  texture, in the `.txi`. This is visible: "DEMOLITIONS" spaces its narrow
  letters oddly. Exactness is reachable, and it needs the `.txi` read.
- **The atlas has 256 cells, so an em dash cannot be drawn.** `PT-1326`'s
  rendered string contains one. In my capture it comes out as a gap. Either the
  string uses a substitutable glyph or the font needs extending — a content
  decision, not a rendering one, but it needs deciding.

### F4 · Restyleable text input — **DID NOT HAPPEN**

The pattern: `EditableText` at `Opacity(0.0)` keeps Flutter's IME, key handling,
selection and platform integration; every visible pixel is drawn by us in the
KOTOR frame and the KOTOR font, with our own blinking caret.

Typed "I know that name" through it and the app rendered `SAID: I KNOW THAT
NAME` in the bitmap font, inside a nine-sliced frame. No native caret, no
foreign selection colour, no platform context menu.

**Worth stating plainly:** KOTOR ships **no text-entry control at all** — the
GUI format has nine control types and none of them is a field. This one is ours,
so "matches" means matches the eight we are copying, and it does.

### F5 · A working Linux build — **DID NOT HAPPEN**

Debug and release both build and run. A real window, real GTK integration, real
mouse and keyboard, Impeller on OpenGLES against the GPU. Numbers in §2.

The only difficulty was assembling a C toolchain without root, which the fail
conditions excluded in advance as a property of this container.

---

## 4. The soft fails, answered

### S1 · Unmaintained package — **DID NOT HAPPEN**

I leaned on exactly one non-Flutter package.

| package | version | publisher | latest published |
|---|---|---|---|
| `file_selector` | 1.1.0 | **flutter.dev** | 2025-11-21 |
| `file_selector_linux` | 0.9.4+1 | **flutter.dev** | **2026-08-28** |
| `cross_file` | 0.3.5+5 | **flutter.dev** | 2026-08-25 |

All published by the Flutter team; the Linux implementation shipped nine days
ago. Nothing here is a single-maintainer risk. Everything else — the painter,
the font, the states, the list, the scrollbar, the text input — is framework
plus my own code, no third parties.

### S2 · More than half a day fighting rather than typing — **DID NOT HAPPEN**

**I did not stopwatch each piece and will not invent numbers.** What I can
report accurately is iteration count, which is the honest proxy.

- Nine-slice: **three builds** to correct. First stretched, second filtered
  wrong, third right. All three corrections were data misreadings.
- Bitmap font: **one build**, correct first time once the atlas was decoded.
- Text input: **one build**, correct first time.
- Panel, list, scrollbar, four states: **one build**, correct first time.
- Engine call and its rendering: **one build**.
- Desktop spine: **three builds** — one to discover `PlatformMenuBar` is inert
  on Linux, one for the multi-window probe, one for the drawn menu bar.

Total across the whole spike: **eleven builds**, none longer than thirty
seconds. The time went into reading TPC and GUI data, not into arguing with the
framework.

### S3 · Engine interface contorted to be callable from a widget — **DID NOT HAPPEN**

`resolve(check)` is a plain synchronous function returning a plain object. No
async plumbing, no global state, no rebuild storm. The whole contract:

```dart
Derivation resolve(Check c, {int? forcedRoll});

class Derivation {
  final Check check;
  final List<Term> terms;   // ("d20", 11), ("rank", 4), ("aptitude", 2)
  final int total, needed;
  bool get success => total >= needed;
  String render();
}
```

The widget calls it in a pointer-up handler, holds the `Derivation`, and draws
it. `render()` reproduces `PT-1326`'s shape, and the panel showed
`ROLLED 10  D20 5 + RANK 2 + APTITUDE 3 · NEEDED 12` in red for a failed check
and green for a passed one.

**⚠ This finding is provisional.** See §6.

### S4 · Close but not exact, with no route to exact — **DID NOT HAPPEN**

Exact is reachable and I know the route. Two known gaps, both with a named fix:

- **Proportional metrics.** Read the `.txi` per-character widths. Not done.
- **Per-control visibility.** The GUI format carries none. `LBL_CANTEQUIP` — a
  genuine red warning label at `171,245` with colour `(0.698, 0, 0)` — draws
  unconditionally in my version and is hidden by the running game. Visibility is
  engine-driven by tag, not data. The route is a visibility map, and it is a
  design decision rather than a rendering limit.

Neither is a rendering-stack constraint. Both are work I did not do.

### S5 · Native dialogs, menus or a second window need a workaround — **PARTIAL FAIL**

This is the one place the answer is not clean. Three sub-answers:

**Native file dialogs — PASS, no workaround.** `openFile()` opens a real GTK
chooser, carrying the `XTypeGroup(label: 'campaign package', extensions:
['json','zip'])` filter I declared in Dart into the dialog's own type dropdown.
I drove it to a real selection and the path came back and rendered in the panel:
`PATH: /HOME/AIDAN/DEMO_PACKAGE.JSON`. Full round trip, Dart to GTK to Dart.

**Menu bar — PASS, but not the one I first reached for.** `PlatformMenuBar` is a
**silent no-op on Linux**. It throws nothing and renders nothing. This is
documented in the framework's own source, which says Flutter "only includes
support for macOS out of the box" and marks its example "will only work on
macOS". Flutter's drawn `MenuBar` / `SubmenuButton` / `MenuItemButton` works
fine, and File → Open Package… / Save As… / New Window plus an Edit menu render
and invoke correctly.

Whether that counts as a workaround is a judgement. **I score it as not a
workaround** — it is a supported first-party widget, and for a KOTOR-styled
Builder a drawn menu bar is arguably what you want anyway. But it is a trap: the
API that *looks* right is the one that does nothing, and it fails silently.

**Second window — FAIL. No route on the stable channel.**

I tested this rather than assuming it. The API exists in 3.47.2:
`RegularWindowController`, `RegularWindow`, `WindowingOwner`, and a real
`_window_linux.dart` implementation. But it is `@internal`, not exported from
`package:flutter/widgets.dart`, and gated behind a flag:

```dart
bool isWindowingEnabled = debugEnabledFeatureFlags.contains('windowing');
```

I tried both routes. `--dart-define=FLUTTER_ENABLED_FEATURE_FLAGS=windowing` is
explicitly refused by the tool. `flutter config --enable-windowing` is accepted
but documented as applying "only to the master channel", and a probe binary
reports:

```
isWindowingEnabled = false
PROBE FAILED: Unsupported operation: Windowing APIs are not enabled.
```

The framework's own message says: switch to the main channel. **On stable, a
second native window is not available.** That is a real constraint on a Builder
that wants a floating palette or a detached preview.

**Scoring:** one soft fail (S5, on the second window alone) and no other. The
threshold in the fail conditions was two. **The recommendation is not in doubt.**

---

## 5. What fought me — and it was not Flutter

Three bugs, all mine. The third is worth carrying forward.

**⚠ Every one of these textures is DXT5, not 8-bit greyscale.**

TPC's header has `dataSize` at offset 0, and **it is zero for uncompressed
data**. Every texture in `equip_p` has a non-zero `dataSize`. For DXT5 that size
is `blocks × 16`, which for any width and height is **exactly `width × height`**
— indistinguishable by size from one byte per pixel.

So a size check cannot tell them apart, and my greyscale decode did not produce
an obvious error. It produced *plausible vertical stripes*. I rendered a whole
panel from them and it looked like a deliberate scanline effect. What exposed it
was magnifying a corner texture and finding stripes where a rounded arc should
be.

The rule, stated so it does not recur: **decide compression from `dataSize != 0`
first, then read `encoding`. Never infer the format from the byte count.**

Once decoded properly the data reads exactly as designed: `uibit_fill_2wt` is
solid white at alpha 49, a 19% wash; `uibit_fill_2bt` is black at alpha 199;
the borders are white with the shape in alpha; the backdrop is a real image.

The other two — stretching instead of tiling, and one global filter quality —
are in §3 under F1.

**One thing that did fight, and it is not Flutter either.** Driving the app with
`xdotool` was awkward because this desktop has VS Code fullscreen and a Dolphin
window stacked above, and Flutter's GTK shell creates several X windows of which
only one is viewable — I spent several attempts driving an unmapped helper
window. The clean answer was to stop grabbing the screen and have the app
photograph itself from its own render tree via `RepaintBoundary.toImage` at
`pixelRatio: 1.0`. That is also strictly better evidence: it is what the app
drew, not what a compositor showed.

---

## 6. ⚠ Item 4 is provisional, and this needs resolving

**`design/ENGINE-INTERFACE-01.md` does not exist in this repository.** Stated as
blocker B1 before any code and unchanged now. Searched by filename, by content,
and for both `PT-1326` and `resolve(check)`. `STUDY/_reference/` holds thirteen
documents and this is not among them.

What I built for item 4 is my reconstruction from the brief's single sentence.
The shape — a list of labelled terms, a total, a threshold, and a `render()`
that reproduces the string — is inferred from **one rendered example**. It is
very likely wrong in detail: I do not know whether terms carry sources, whether
a failed check reports a margin, whether critical results are terms or flags,
whether the check names a skill or an id, or what happens with zero and negative
modifiers.

**Every S3 finding above is provisional until that document is readable.** This
is the same pattern as the `SKILLS-01` episode — believed pushed, not present —
and the lesson recorded then applies: I verified my reading, not my source.

---

## 7. What I did not check

- **Performance under load.** One panel, 54 controls, no profiling, no frame
  timings. I did not measure whether 500 list rows or a full inventory holds 60 fps.
- **Any panel other than `equip_p`.** Notably nothing with a `Slider`, which
  `character_p` has and this does not.
- **Text input beyond ASCII.** No IME, no composing text, no clipboard paste, no
  selection by drag. The machinery is Flutter's and should work; I did not test it.
- **The `.txi` font metrics.** Known gap, named above.
- **Windows or macOS.** The brief said Linux and I did Linux only.
- **Hot reload.** I built and ran; I never exercised the edit-and-reload loop
  that would dominate day-to-day Builder work.
- **Animation, pulsing, cutscene staging.** `PULSING` is in the data and I read
  it into the model but never drew it.
- **Whether any of this survives contact with a second developer.** It is 746
  lines written to be deleted.

---

## 8. Verdict

**Flutter does not fight us.** On the specific question the spike was built to
answer — can we reproduce KOTOR's UI exactly — the framework got out of the way
every time. The canvas is directly reachable, tinting is one property, glyph
blitting is a supported call, and the editable-text machinery separates cleanly
from its chrome.

Everything that went wrong was KOTOR's data being subtler than I read it: DXT5
masquerading as greyscale, tiled edges, a proportional font in a fixed grid.
Those costs are the same in any framework. They are the real cost of "identical
to KOTOR", and they are paid in reading, not in rendering.

**The one thing to weigh:** no second native window on stable. If the Builder
needs detached palettes, that is a channel decision — and depending on the main
channel for a production tool is a bigger commitment than it sounds.

**This is a spike and should be deleted.** Nothing in `code/` is a foundation.
It exists to have answered the question, and the question is answered.
