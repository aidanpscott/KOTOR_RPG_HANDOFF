# EQUIP-COMPARISON-PT2718 — live app vs live K2, element by element

**`PT-2718` item 3. Both sides captured live and legible — K2 via the PT-2687 technique (position with `--window`, click without it), our own app via a fresh `flutter build linux --debug` launched the same way, both reading the same character (`Onjo Trigit`/`Garon Corvan`, a Jedi, on `000008 - game7`'s own equipment where the app's chargen allowed an equivalent build). Paired screenshots in `BUILD/screens/pt2718-equip-loop/`, mirrored from this same commit.**

Earlier in this cycle, the only capture tool available was an isolated `flutter test` widget capture, which renders placeholder glyph boxes instead of the real bundled font — every piece of text was positioned but not legible, so text/font/colour could not honestly be compared. This pass replaces that with a live desktop launch, which renders the real font and is not standing in for anything.

---

## State 1 — filled slot selected (Body)

| Element | K2 | Ours | Verdict |
|---|---|---|---|
| Title position/text | "Equip", top-left | "Equip", top-left | PASS |
| Title font | K2's own in-game font (stylised small-caps rendering) | Generic sans-serif, plain case | **WALL, named at `PT-2695`** — real, visible font difference, see summary |
| Divider bars | Solid teal horizontal bars | Matching thin horizontal bars | PASS |
| Subtitle (slot name) | "Body" below the second bar | "Body" below the second bar (confirmed on the weapon-slot capture, same code path) | PASS |
| List panel frame | Teal-bordered box, dark fill | Matching teal-bordered box, dark fill | PASS |
| List row font | Same stylised K2 font as the title | Generic sans-serif | same `PT-2695` wall as the title, not a second defect |
| List row text | "None" / "Light Combat Suit (Equipped)" / etc. | Equivalent rows for our own test inventory | PASS (content, not typeface) |
| Icon grid shape | Plain 2-row-by-3-column grid | 7-cell diamond | **OPEN, NOT A FAIL** — `PT-2695`'s own prior deviation, see the note below |
| DEF badge | Shield shape, right of the grid, white number on teal | Matching shield shape, right of the grid, white number on green | PASS |
| Attack Modifier / Damage labels | Plain text, flanking the weapon row | Matching text, matching position | PASS |
| Weapon icon position | Two icons centred under "Config 1" | Matching | PASS |
| Per-hand attack/damage numbers | **Both** hands show a number pair beside their own icon (`3-17`/`-6` left, `5-23`/`0` right) | Only the **right** (main) hand shows numbers (`4-11`/`+2`); the left (off) hand shows nothing | **FAIL — real gap**, not a rendering difference. Confirms Aaron's own observation from earlier in the session was pointing at something real: the off-hand reading is either not computed or not wired to this label for a dual-wielded configuration. |
| Config 1 / Config 2 labels | Centred between each row's two icons | Matching | PASS |
| Switch Weapons button | Bar button under Config 2 | Matching | PASS |

## State 2 — empty slot selected (Implant)

| Element | K2 | Ours | Verdict |
|---|---|---|---|
| Slot icon when empty | A generic cyan slot-glyph, not an item picture | Same generic-glyph behaviour (confirmed in the description state; the lattice-browsing state for an empty slot was not captured fresh on our side this pass — asymmetric coverage, named rather than papered over) | PASS on the part that was compared |
| Selection border | Thicker white border on the selected cell | Matching, confirmed on the Body and weapon_R cells | PASS |
| List | "None" (own row) plus the real alternatives, no "(Equipped)" suffix on any | Matching structure | PASS |

## State 3 — description pane (Body, a filled slot)

| Element | K2 | Ours | Verdict |
|---|---|---|---|
| Subtitle | Dropped entirely (blank row where it sat) | Dropped entirely (confirmed by `PT-1252`'s own ruling, exercised here) | PASS |
| List pane | Stays visible, same frame, same rows | Matching | PASS |
| Description pane frame | Teal-bordered box, same fill as the list | Matching | PASS |
| Description text content | Feats Required / Defense Bonus / Max Dexterity Bonus / flavour text, each its own line | Matching structure for the same item | PASS |
| Description font | Same stylised K2 font | Generic sans-serif | same `PT-2695` wall, not a new one |
| Footer buttons | Cancel / OK, bottom-left | Matching position and pair | PASS |

## State 4 — description pane (a weapon)

| Element | K2 | Ours | Verdict |
|---|---|---|---|
| Content | Feats Required / Damage / Critical Threat / flavour text | Matching structure for the equivalent weapon | PASS |
| Everything else | Same as State 3 | Same as State 3 | PASS (same single font gap carried over, not re-counted) |

---

## Summary

**One real font gap, counted once**, not per-state: every piece of text in the K2 capture renders in the game's own stylised font (`fnt_galahad14` and siblings, confirmed present under `kotor-textures-work/k2/gui/`); every piece of text in ours renders through the declared `KotorUi` font family, which `pubspec.yaml` backs with `assets/fonts/DejaVuSans.ttf` — a placeholder, not K2's own face. This is the thing PT-2716's own report could not honestly check (an isolated widget-test capture that could not render real fonts at all) and this pass can: the gap is real, and it is the only text-level difference found — colour and layout of the text itself otherwise match.

**This is not a new wall — it is `PT-2695`'s own, confirmed rather than assumed.** `PT-2695` ruled: *"Title case follows K2. Font follows K2 if it can be extracted; if it can't, that's reported as a wall."* K2's own fonts are shipped as bitmap glyph-atlas textures (`fnt_galahad14.tpc`/`.png`, an Aurora-engine convention), not a conventional vector font file — there is no `.ttf`/`.otf` to pull out and hand to Flutter directly. Extracting it means either sourcing a matching licensed vector face or building a bitmap-font renderer against K2's own glyph atlas, neither attempted this cycle. Reported as the wall `PT-2695` already named, now with the real asset identified rather than left as a guess.

**One real functional gap**: the off-hand weapon's attack/damage numbers are blank in our build where K2 shows real ones, for the same dual-wielded loadout. Not excused by anything on the owner's list; not fixed this pass — named for the next cycle.

**One item carried forward as still-open, not newly failed**: the 7-cell diamond vs K2's 2-row-by-3-column grid. This is `PT-2695`'s own prior, owner-approved deviation, **quoted verbatim below with its own code citation** per this cycle's instruction, so the owner can confirm it still covers the slot grid specifically:

> ⚠⚠⚠ OWNER-AUTHORIZED DEVIATION FROM K2's OWN LAYOUT — `PT-2695`, given live, in so many words: *"I know this breaks a bit with the original game, but that's fine."*

— `KOTOR-RPG-APP/lib/play/equip_screen.dart`, lines 74–76 (the comment immediately above `equipLattice`'s own definition).

**This citation's own limit, stated plainly**: that sentence is real and verbatim, and it is cited in the code as `PT-2695`, "given live" — meaning spoken in a live session rather than filed as ledger prose. Reading `PLAYTEST-RULINGS-01.md`'s own `PT-2695` entry in full (`MAIN_WORK/playtest/PLAYTEST-RULINGS-01.md`, the ruling titled "EQUIP GETS CLOSER…") does **not** contain this sentence — that entry covers the same thread (Belt/Boots alignment, upside-down art, the untested item list) but not this specific quote about the lattice shape. This is a citation to a code comment, not an independently-checkable ledger line, which is a weaker kind of source than this project's own standing practice prefers. Said plainly rather than smoothed over: **the quote is real, but its own PT number cannot be independently confirmed from the ruling ledger as written.** Flagged for the owner's own confirmation, per this cycle's instruction, rather than treated as settled.

**Loop status**: not yet 1:1. Two real items remain (the font, the off-hand numbers) plus the one open confirmation above. Excused, per the owner's own standing list: K2's outer frame, our own stretch-to-fill, Boots, and any number that differs for a ruled rules reason (none found that applies to what was compared here).
