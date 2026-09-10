# BUILD 108 — I was wrong about cmake, and here is the Builder running

Loom `ee0e7aa`. Loom 239 green. Screenshot:
`BUILD/screens/107-loom-slice-five-opening-state.png`.

---

# ⚠⚠ THE MEASUREMENT WAS RIGHT AND THE INFERENCE REACHED PAST IT

`which cmake` finding nothing **is true of an unsourced shell**, and I turned
that into *"cmake is not installed on this machine"* and asked for an
`apt install`.

    ./env.sh   flutter, cmake, ninja and clang live under ~/spike
               and cmake needs librhash from the same place

**⚠ AND THE DOCUMENT THAT SOLVES IT CARRIES MY EXACT ERROR AS ITS WORKED
EXAMPLE.** `env.sh`'s own header says *"without these lines `flutter build
linux` stops with 'CMake is required for Linux development' — which is
misleading: it IS installed."* **I quoted that sentence back as evidence for the
opposite conclusion.**

**⚠ AND THERE IS A `run-loom.sh` THAT DOES ALL OF IT**, and it always builds,
because `PT-1448` found that the conditional version ran old code and said
nothing.

> **`Tester` builds Loom every session on this machine and has never hit this.
> Two agents, one PATH, and only one of them sources `env.sh`.** The thing I did
> not check was whether my shell was the same shell as the one that works.

---

# ⚠⚠ AND THE STALE-BUNDLE WORRY WAS REAL — VERIFIED, NOT ASSUMED

The launcher stub is still dated 8 September, **and that is not the artifact
that matters.** `PT-1604`'s third artifact, in a binary:

    bundle/loom                        8 Sep   the stub, never changes
    data/flutter_assets/kernel_blob.bin  today  the Dart

**Checked with `Tester`'s own recipe** — `strings kernel_blob.bin | grep -c` —
against four literals that exist only in slices four and five, one of them from
`Lodestar` through the pub cache:

    pick a kind            2      PT-1623, the collapsed palette
    an arrival point       2      the article fix
    not enough to hurt     2      PT-1622's graze, via the engine
    nowhere to walk FROM   2      PT-1619's seed, via the engine

**The running Builder is this slice, and the engine inside it is too.**

---

# ⚠⚠ AND RUNNING IT FOUND TWO THINGS THE SUITE COULD NOT

**1 · `conversations` offered a `+` with no package open.** `areas` guarded on
`_open == null`; `conversations` did not — **the guard was written on one of two
adjacent lines.** Pressing it would have opened a conversation tab with no
package to write into.

> **⚠ And no case saw it, because every case that renders this tree passes a
> package.** The source was right, the suite was green, and the screen was
> wrong.

**2 · The left pane read `conversati…`.** That same `+` carried
`horizontal: 6 * s` of padding its twin did not, and **the ~24px it took
ellipsised the word.** Two shapes for one verb, and the wider one cost the
label.

Both have cases now, and both were invisible from the code.

---

# ⚠⚠ `PT-1621` — WHAT A GLYPH CAN CARRY BEFORE ANY ART EXISTS

**Nothing, for these ten. It genuinely waits for art.**

**⚠ AND THE TILE PALETTE'S FIVE ARE NOT A COUNTER-EXAMPLE — THEY ARE THE REASON
THE REST CANNOT.** `. # ~ : !` are `AREA-FORMAT-01`'s own legend: **the character
an author reads in the `.toml`.** The glyph is not a mark standing for a name, it
IS the name in the other place it appears. **The ten kinds have no such source**
— every glyph would be invented in this file.

    STUDY 27 had to HOVER ALL NINE of Aurora's icons to write down what they
    were — and those are drawn, pictorial, and far more distinguishable than
    any character at text height.

> **If trained pictures needed hovering, a text-height character cannot do
> better.** *"An icon that must be hovered to be read is a label you have
> hidden."*

**⚠ A LETTER COLLIDES THREE TIMES IN TEN** — `d` is doors and doctrines, `s` is
sounds and stores — and a letter beside a word beginning with the same letter
carries nothing at all.

**⚠ A PICTOGRAPH IS ART WE DID NOT DRAW AND CANNOT GUARANTEE.** It comes from
whatever font the machine has and a missing one renders as tofu. `UI-ASSETS-01`
ships no art, and depending on the user's font stack is the same shape as
guessing at a rules file that is not installed.

**So the slot stays reserved and empty**, and `PT-1366`'s drawn set at that
standard is what changes this answer — **nothing smaller does.**

## ⚠⚠ AND `▦` WAS MINE AND IT WENT

I had already put one on the terrain row. **It fails my own argument** — an
invented mark is a second name for a thing that already has one — so it is a
spacer like the other ten, and a case asserts no kind carries a glyph while the
format's own five survive one page in.

---

# WHAT THE BUILDER LOOKS LIKE NOW

    module                  work                    palette  assistant
    ▸ areas                                         terrain
    ▸ conversations         no package open         creatures
                                                    doctrines
                            [ New package ]         doors
                            [ Open package ]          a doorway, painted
                                                    encounters
                                                    items
                                                    placeables
                                                    sounds
                                                    stores
                                                    triggers
                                                    waypoints
                                                      an arrival point, painted
                                                     pick a kind

**Two roots and eleven rows, and nothing under either.** `PT-1623` on screen —
and the right pane fits all eleven with room to spare at 1280×720, which is
`PT-1620`'s *ten short rows and one page* measured rather than argued.

---

# STILL OPEN

`character.downed`'s `campaign` lifetime · the drawn icon set, which `PT-1366`
makes separate work and which is now the only thing between the slot and its
contents · `§5` has no second interaction the product can reach · the two
deferrals in `STATE.md`.
