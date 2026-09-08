# STUDY 18 — the three dialogue systems, and whether theirs imports into ours

**Records in `RECORDS.md`. Judgement in `FLAWS.md`.**

**Both games installed and read. Neither run.** Read with our own
`gfffull.py`, `container.py` and a `chitin.key`/BIF reader written for this
study — **no third-party tool, and none needed.** 1,065 K1 `.dlg` and 973 K2
`.dlg` parsed, zero failures.

**Built on `TRACE-93` and `TRACE-95`, not re-finding them.** Where this study
touches their ground it either **confirms by a second method** (`R18.06`:
59.0% of K1 replies have no text, against `TRACE-93`'s 58.9% on a larger
denominator) or **reconciles a count** (`R18.04`: my per-level field sums
reproduce `TRACE-95`'s 159 for K2 exactly and 78 for K1 within one).

---

## The answer, first

> **The STRUCTURE ports almost exactly. The TEXT ports and must not. The
> CONDITIONS do not port at all.**

**And the third one is not a difficulty. It is a category difference.** Our gate
is a declared predicate — a question you may ask twice. **Their `Active` is a
procedure that returns a number**, and in a real shipped companion
conversation, **eleven of eleven opening gates write to global state while
deciding** (`R18.08`). Evaluating the list is what marks the line as spoken.

**A gate that must be evaluated exactly once, at a moment the format does not
name, is not a gate.**

---

## 1 · What a `.dlg` actually is  (`R18.02`–`R18.05`)

**A GFF V3.2 file** — the same container as `.uti` and `.utc`. One top-level
struct holding **three node lists**:

    StartingList   links only, no text — the entry points
    EntryList      NPC lines
    ReplyList      PLAYER lines

**⚠ There is no node type field.** A node's type is *which list it is in*.

**A link is a struct, not a pointer** — `Index` into the *other* list, plus its
condition. Entries link to replies and replies link to entries; **the
alternation is structural and cannot be broken.**

**A condition attaches to the LINK. An action attaches to the NODE.** `Active`
names a script the engine runs to decide whether the link is available;
`Script` fires when the line plays. **Both are resrefs into a compiled script
system, not expressions.**

**Walk order is array order** — no priority, weight or sort field exists at any
level in either game.

### The field count, and what it is made of

|  | K1 | K2 |
|---|---:|---:|
| distinct field names, all levels | **55** | **99** |
| counting each level separately | 83 | 163 |
| link fields | **4** | **20** |

**⚠ K2's link grew from 4 fields to 20, and 17 of the 20 are the condition
apparatus** — `Active`, `Active2`, `Not`, `Not2`, `Logic`, ten numeric
parameters and two string parameters. **That growth is the whole of K2's
format change that matters**, and it is the parameterised conditional our
`§2` already took by name.

**The full enumeration is `R18.03` and `R18.04` — that list is what an importer
would have to map.**

### Most of the format is staging, and three K2 fields are defaults

`Text` is present on 65.7% of K1 nodes. Beneath that, usage falls away fast:
`Script` 12.5%, `CameraAngle` 12.7%, `AnimList` 5.6%, `Quest` 1.6%,
`PlotIndex` 0.3%.

**⚠ And counting presence would overstate K2's celebrated additions.**
`Emotion` carries value 4 on 42,290 of 44,424 nodes — **authored on 4.8%.**
`FacialAnim` is authored on 0.4%. `PlotXPPercentage` on 0.3%.

### The tree is mostly plumbing

    replies with NO TEXT AT ALL         K1 59.0%   K2 46.8%
    NPC nodes offering exactly ONE      K1 67.9%   K2 63.3%
    NPC nodes offering more than one    K1 27.7%   K2 32.6%

**Roughly a quarter of the "tree" is choices. The rest is routing** — and
routing is exactly what lives in the conditions.

---

## 2 · Ours, side by side  (`R18.09`, `R18.10`)

**`ENGINE-SPEC-03 §2` did not take inspiration — it took the model**, by name:
*"THE BIOWARE MODEL, UNCHANGED."* Same three lists, same `Index` + `Active`
link, same walk-in-order-first-pass-wins, **and K2's parameterised conditionals
taken explicitly.**

**⚠ So the structural mapping is near-total, and where it differs, ours is
richer:** `§4b.1`'s `all_of`/`any_of` **nests arbitrarily deep**, where K2's
`Logic` joins exactly two conditions with one operator. `TRACE-12` found
KOTOR's typed convention had *"no way to express that difference"* — **and
neither does its structured field.**

**What we have that has no `.dlg` counterpart:** the topic space, the seeded
knowledge gate, the fact/tier/gate/deflection schema, the unconditional absence
report, the AI rephrase, escalation, the character brain as a view, and
package-local `rules/`.

**⚠ What our own document lacks that a real conversation uses:** `Speaker`
override (23–25% of entries — Carth speaks three lines inside `bastila.dlg`)
and `IsChild` (30–34% of links). **Named as gaps in `ENGINE-SPEC-03`, not as
arguments for importing** (`F18.04`).

**⚠ And our dialogue file format does not exist.** `PACKAGE-FORMAT-01` names a
`dialogue/` folder and specifies nothing inside it. **This is why the import
question decides the format rather than merely testing it.**

### The four differences put to me

| put to me | verdict |
|---|---|
| typed text meaning an authored reply **counts as picking it** | **confirmed** — `PT-1303`, `§4e` |
| three colours, amber rolls, grey does not | **confirmed — and it is four once a check resolves**: amber passed, **coral failed**, grey manner, teal background, plus `dim` for an act |
| …ruled at `PT-1305` | **⚠ corrected. `PT-1305` is the character brain.** The colours are `PT-1306` (settled) and `PT-1307` (simplified) |
| **no numbers** — `[Persuade]`, and you roll | **confirmed** — `PT-1307` |
| a price shown when the player can act on it | **confirmed** — `[Bribe · 50 credits]`, `PT-1315` |
| AI never advances the plot | **confirmed, and refined** — `PT-1303` lets the AI pick *which authored door*, which `§4e` argues is a menu's job, not a story decision |

**⚠ One contradiction found and NOT resolved.** `ENGINE-SPEC-03 §4c` prints
`PT-1307`'s *"NO NUMBERS ANYWHERE"* and *"unavailable options are HIDDEN, not
greyed"* — and then, lower in the same section, still carries the superseded
`PT-1306` block as live, with a mock-up showing `[Persuade DC 14]` and a
**greyed** `[Slicing DC 18]`. **Both contradict the ruling above them, and the
older block is not marked superseded.** Reported; the owner's to settle
(`F18.06`).

---

## 3 · ⚠⚠ Could we import their conversations wholesale?

### What maps

**Everything structural.** Three lists, `Index` links, alternation, array
order, the parameterised conditional, `Text`. **A reader for their file is a
reader for ours with fields left over.**

### What has no counterpart — and it is roughly half their format

**By ruling, not by omission.** `PT-1319`: a character on screen is a portrait,
nothing animates, there is no model. That deletes `Emotion`, `FacialAnim`,
`AnimList`, six camera fields, four fade fields, `CameraModel`, `StuntList`,
`AnimatedCut`, and the whole VO pipeline. **Of K2's ~48 node fields, about
eight carry meaning rather than staging.**

**In the other direction**, everything in `§3`, `§4a`, `§4b`, `§4e` and
`PT-1311`/`PT-1316` has no `.dlg` counterpart at all. **`TRACE-95`'s negative is
the sharpest case, and this study explains it**: the format has no concept of a
second visit **because the second-visit machinery is inside the conditional**,
hand-built out of globals.

### ⚠ What does not map, and why it is fatal

**Their conditions are readable more often than the brief assumed** — both
games ship `.nss` **source** in the BIFs, covering **52.9% of K1's condition
use sites and 77.5% of K2's**. That correction matters and is stated plainly.

**But:**

    compiled only, no source     K1  5,501 sites = 47.0%     K2  2,809 = 22.4%

For those, an importer may decompile (a separate project, and the output is
engine calls rather than gates), drop the gate (the option becomes always
available), or stub it (silently, in one direction). **All three change the
conversation.**

**And of the half that CAN be read, a real fraction are not predicates at all:**

    K1 StartingList gates    6.8% provably mutate    53.7% unreadable
    K1 in-tree link gates    0.4% provably mutate    45.5% unreadable

**⚠ Those percentages are floors, not rates**, because the unreadable half is
uncounted. **The honest statement is that between 6.8% and 60.5% of K1's
opening gates are not predicates, and the format cannot tell you which.**

### ⚠ Is this the item shape? `PT-1409`

**No — dialogue is genuinely untouched ground.** The TLKs are held **raw**, and
their stated purpose is resolving item and creature name strrefs. No `.dlg` has
ever been read into a document. Nineteen files in `data/extracted/`, none of
them dialogue.

**⚠ With one exception, and it is the item shape exactly.** The check-tag
vocabulary at `§4c` **is already a conversion**: `TRACE-12` reduced 2,509
bracketed lines / 256 distinct strings / ~25 concepts to **eight checks, one
manner tag, and one retirement**, and `PT-1104`, `PT-1306`, `PT-1307` and
`PT-1315` sit on top of it. **An import that brought reply text in verbatim
would bring the 256 strings back with it and silently overwrite every one of
those rulings** — `PT-1409`'s failure mode precisely (`F18.05`).

### ⚠ And what an import would cost us, named

> **An import that brings the text and drops every condition is a
> TRANSCRIPT, not an import.**

**The transcript is real and not worthless** — 482,848 words in K1 and 433,707
in K2, already in a tree, already alternating. As a corpus to study, or a shape
to test an engine against, that is genuine.

**It is not content that can ship, for three independent reasons:**

- **It would not work.** 67.9% of K1's NPC nodes offer exactly one reply and
  59.0% of player nodes have no text. **Most of the tree is routing, and
  routing is the part you dropped.**
- **It is not ours.** LucasArts/BioWare/Obsidian text. `ASSET-REPLACEMENT-01`
  already governs prototype material that never ships, and **dialogue is not in
  a different position from art.**
- **It contradicts the design.** Our brackets render **from the gate field**.
  Import their strings and you re-import the 62% drift the design exists to
  eliminate.

---

## 4 · The one thing worth taking, and it is not text  (`F18.08`)

    K1  2,309 distinct condition scripts for 11,716 use sites
    K2    493 distinct condition scripts for 12,541 use sites

**K2 does more gating with a fifth of the scripts**, because one parameterised
`c_global_eq` covers 1,708 sites. **⚠ And that is also why K2 is 77.5%
readable where K1 is 52.9%** — a small closed set of generic conditionals is
one you can read once and then understand every call site of.

**A declared gate vocabulary is not merely tidier than 2,309 bespoke scripts.
It is the difference between a format you can inspect and one you cannot** —
and it is the argument for `§4b`'s schema stated as a measurement rather than a
preference.

---

## 5 · Not determined

- **Whether the unreadable 47% mutate.** Needs decompilation. Every purity
  figure here is a **lower bound** and should be quoted as one.
- **What K2's parameterised conditionals mean per call site.** The global names
  sit in `ParamStrA`; no sweep of those values was run.
- **The topic taxonomy.** `§7` records it open — *"shape settled, list not."*
- **Whether our dialogue file would be TOML.** `PACKAGE-FORMAT-01 §3c` makes
  TOML the shipping format generally; nothing states it for `dialogue/`.
- **The licence position on the text.** Not researched here; flagged because
  `F18.03` leans on it.

**⚠ Nothing was built.** No importer, no format, no parser committed to any
repo. The read-only sweep lived in the scratchpad and is described in
`RECORDS.md` so it can be reproduced.
