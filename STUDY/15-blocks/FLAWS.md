# STUDY 15 — judgement

Records are in `RECORDS.md`, cited by number.

---

## F15.01 · ⚠ The transferable mechanism is rotation, and it is the whole answer to question 3

**You asked what makes a block reusable. The binary answers in two bits.**

Every placed piece inside an RMB carries a quarter-turn (`R15.05`), proven
across 29,440 entries with exactly four values and no others. **A corridor
section is authored once and used four ways.**

That is the difference between 920 shipped blocks and the ~3,600 it would have
taken to author each orientation, and it is the cheapest thing in this study to
copy: **a prefab is a piece plus a rotation, and rotation is a field on the
placement, not a variant of the piece.**

**⚠ For a hand-painted grid this matters more, not less.** Generation can afford
a big library because nobody browses it. An author browses. A palette of 900
corridor pieces is unusable; a palette of 225 with a rotate key is a palette.

## F15.02 · ⚠ Shape and identity are separated, and that is the design worth stealing

**Question 4 asked whether blocks carry contents or only shape. Daggerfall's
answer is: both, split across two files, and the split is the interesting part.**

- **The block file carries shape AND props.** Its first four bytes count block
  data records, 3D objects and **flat objects** (`R15.04`) — the sprites that
  are furniture, clutter and people. A tavern block is not an empty room.
- **The location file carries the instances.** A per-building array (`R15.08`)
  and a door list (`R15.07`) live with the *placed* location, not with the
  reusable block.

**So the same `TVRNAS00` tavern is the same shape and the same furniture
everywhere it appears, while the shopkeeper's quality, faction and name belong
to the town it was stamped into.**

**⚠ That is exactly the distinction our format already draws** and it is worth
noticing that we drew it independently: `AREA-FORMAT-01 §3` has contents
referencing a template by path with a per-instance `tag`, and `PACKAGE-NAMING-01
§1` separates `path` (identity of a definition) from `tag` (identity of a placed
instance). **Daggerfall put the same seam in the same place.**

**The lesson for prefabs:** a prefab may carry props, but anything that differs
between two stampings must live on the stamping, not in the prefab. If our
corridor prefab carries a footlocker, the footlocker's *contents* cannot be in
the prefab.

## F15.03 · ⚠ There is no evidence of edge-matching, and that shapes what we build

**You asked whether blocks have edges that must match, connection points,
anything that makes one piece fit beside another. I looked and found nothing
that says so, and the absence is informative rather than a gap in the study.**

The positive evidence points the other way:

- **The size letter is S/M/L on the same function** (`R15.03`), so variation is
  by *bulk*, not by edge profile. A `TVRNAL` is a bigger tavern, not a tavern
  with a different north edge.
- **Function codes describe what a block IS** — tavern, graveyard, wall, farm —
  **not how it connects.** A `WALL` block is the only one whose name implies an
  edge condition, and there are only 12 of them plus `SENT` variants.
- **920 blocks with no visible connection vocabulary** would be an enormous
  number of edge profiles to keep consistent by hand.

**The likely mechanism is a uniform footprint**: every block occupies one cell
of the same size, streets meet streets because every block puts its street in
the same place by convention. **Convention, not declaration** — which is exactly
what `PACKAGE-FORMAT-01 §4` criticises NWN for (*"A convention is not a
declaration"*).

**⚠ So this is a place NOT to copy Daggerfall.** If our prefabs are corridor
sections and junctions rather than city blocks, they genuinely do need edges
that match, and Daggerfall has no answer to lend. **A declared edge vocabulary —
this side is wall, this side is opening — is ours to invent**, and `§2`'s legend
notation is already the right shape to carry it.

## F15.04 · ⚠ THE DOOR ANSWER, and two games disagree usefully

**You asked because our format does the connection half and not the object half.
Three answers now exist:**

| | Where the door lives | What it carries |
|---|---|---|
| **Daggerfall** | a list on the **location** (`R15.07`) | 8 bytes. A third of locations have none |
| **Aurora / Odyssey** | its own **blueprint type**, `UTD` (`R15.10`) | **56 fields** — 9 lock, 7 damage, 7 trap, 3 saves, **16 script hooks** |
| **Ours** | a `[[connections]]` entry (`R15.11`) | a tag, a position, a destination, an arrival point |

**⚠ The spread is the finding. Eight bytes against fifty-six fields is not a
disagreement about doors; it is a disagreement about what a game is.**

Daggerfall's door is a hole with a flag, because its doors exist to move you
between an exterior and an interior that were generated separately. Aurora's
door is a full object because NWN's doors are *content* — locked, trapped,
scripted, plot-critical, opened by a key an author placed three areas away.

**We are building the second kind and have written the first.**

**⚠ And the answer is NOT to copy the UTD.** Fifty-six fields on a door is the
same disease `STUDY/03` found in the 112-field creature: a blueprint that
carries every question anyone ever asked. Sixteen script hooks on a door is
Aurora's event model, not ours — `PLAY-STATE-01` makes state a projection of a
log, so `OnOpen` is an event kind, not a field.

**What our door actually needs, stated as a need rather than a design:** a
connection is a position and a destination; a *door* is additionally a thing
that can be **shut, locked, opened by a key, and broken**. Those are four
capabilities, not fifty-six fields, and `AREA-FORMAT-01 §5` has already ruled
where their **runtime** state lives — in the log, not the area. **What is
unresolved is where their AUTHORED state lives**, and that is one decision:
either a connection gains an optional lock, or a door becomes a content template
that a connection references by path the way `§3`'s contents do.

**⚠ I did not make that decision.** It changes `AREA-FORMAT-01` and it is
exactly the kind of thing the stop protocol says an agent inside one task should
not settle.

## F15.05 · What exists only to serve generation, and must not be copied

**Question 6, and the list is short because most of Daggerfall's block design is
generation-neutral.**

**DO NOT COPY:**

- **The 62-region file split** (`R15.06`), including a region whose four files
  are empty. That is a shipping-a-continent problem. We ship a package.
- **`RDI`** — 187 fixed 512-byte records, one per dungeon block (`R15.02`). A
  fixed-size companion per block smells like a generator's lookup table. Its
  purpose was not established, and **you should not copy a structure nobody has
  read.**
- **The function-code taxonomy itself** — `ALCH`, `TVRN`, `BANK`, `RESI`
  (`R15.03`). Those exist so a generator can ask for "a medium tavern" and get
  one. **An author does not need a taxonomy to pick a prefab; they need a
  picture.** Copying the codes would be importing a lookup key as a naming
  convention, and `PACKAGE-NAMING-01 §5a` already names that failure — *a
  category posing as a thing*.
- **Variable-size blocks with a fixed grid footprint** (`R15.02`). A fourteen-fold
  file-size range is fine when a machine loads them; it tells an author nothing.

**DO COPY:**

- **Rotation as a placement field** (`F15.01`).
- **The shape/identity seam** (`F15.02`).
- **Size variants of the same function** — S/M/L is a genuinely good palette
  idea and is orthogonal to generation. An author wants a big room and a small
  room, and naming them as variants of one thing beats 900 unrelated entries.

## F15.06 · ⚠ What this study did not establish, stated once, plainly

**The block-to-grid mapping (`R15.09`) is the centre of question 2 and I did not
get it.** I could not find the arrays that say which block sits in which cell,
and I tried three approaches. `MAPDITEM` was not opened at all.

**Consequences for what you can rely on:**

- **Determinism is unanswered.** `TRACE-95` found Daggerfall seeding dialogue
  from `hash(NPC + topic + building)` rather than re-rolling, and the natural
  question is whether city layout works the same way. **I found a per-building
  field that behaves like a seed and could not confirm it is one.** The
  structural argument in `R15.09` — that 920 named blocks and 10 KB location
  records imply *stored* choices rather than derived ones — is reasoning, not
  evidence.
- **The 8×8 city grid is folklore here, not a finding.** I did not measure it.

**⚠ None of that blocks the thing the study was for.** Rotation, the shape/
identity seam, and the door comparison are all established, and all three are
about *authoring a prefab*, not about generating a city. **The part I failed to
read is the part `F15.05` says we should not copy anyway** — which is lucky
rather than clever, and I would rather say so than let the gap pass as a
judgement.

---

## Judgements about our own design, kept separate

**On prefabs in a hand-painted grid.** `PT-1360`/`PT-1361` admit tilesets
carrying prefab pieces. The Daggerfall evidence says the cheap win is rotation
and the expensive unsolved problem is edges — and that our situation is
*harder* than Daggerfall's, because corridor sections must actually meet where
city blocks only had to sit side by side.

**On the door, which is the more urgent of the two.** `AREA-FORMAT-01 §5` names
this as "the rule most likely to be broken first" and it was right. The format's
own example calls a connection `door.command-deck.aft`. **A format that names a
thing a door and cannot lock it will grow a lock field in the first package that
needs one**, and it will grow it in whichever place the person writing that
package found convenient. Deciding it deliberately costs one ruling; discovering
it costs a migration.
