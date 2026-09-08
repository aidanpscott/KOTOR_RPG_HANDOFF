# 24 · A creature in the bed, and the seam reachable

**`Loom` `HEAD` · `KOTOR-RPG-APP` `9d06456`.** 101 Loom tests, 188 app tests,
186 Lodestar tests, all analyze clean.

---

## 1 · Made in Loom, by clicking

**`PT-1346`: the test bed is the Builder's first output, not a hand-written
file.** The bed was built that way at `PT-1379` and the same rule holds for
what goes in it — so this drove **Loom's own dialog and its own grid**, and
**wrote no TOML**.

    New Creature   typed into, then Create   → blueprints/characters/sith-trooper.toml
    the blueprint loaded, then a click on a square
                                             → [[contents]] with a tag Loom proposed

**⚠ And Lodestar reads back what Loom wrote** — the round trip that matters,
across two programs and one format.

**The bed now has:** `blueprints/characters/sith-trooper.toml`, and
`sith-trooper.command-deck.04` standing at `[6, 4]` on the command deck.

### ⚠ A real Loom bug, found by clicking it

**The New Creature dialog overflows by 58 pixels at 1280×720.** Reported, not
fixed — it is Loom's layout and nobody asked for a change to it. The test gives
it a taller surface and says why.

---

## 2 · ⚠ What a player does to attack — **walk into it**

**Flagged as my reading. No document rules it.**

Arrows already move; **a step onto an occupied square strikes instead of
moving.** Three reasons:

- **Nothing else on this screen takes input.** A second key would need a legend
  the screen does not have.
- **It is what the source does** — bumping a hostile in KOTOR attacks it.
- **It keeps the affordance inside the one control a player has already used**
  to get there.

**The line a player reads is the derivation**, `PT-1326`:

    rolled 14 — d20 13 + attack 1 · needed 10 — hit · 23 left

**⚠ The weapon is a fist, named as one.** The character record carries
equipment and no screen resolves it, so this swings the plainest thing there is
rather than inventing a blade.

**⚠ And the die is named and seeded, not `Random()`.** Slice 1's rule was that
a resolution reaching for a global random cannot be replayed, tested or asked
to explain itself — **and that does not stop applying because the caller is a
screen.** Nothing records the seed yet, so it is the smallest honest source and
replaceable the day a log carries one.

---

## ⚠ 3 · THE MARGIN — the wound does **not** survive leaving, and that is deliberate

**Combatants are rebuilt from the blueprint every time an area opens.** Walk
out, walk back, and the trooper is whole.

**`ENGINE-SPEC-04 §4` is the reason**: *"not written — hit/miss, **current
vitality**, position, whose turn it is."* Current vitality is transient by
ruling, so **rebuilding it is what the spec says to do, not a shortcut.**

> **⚠ AND THE OTHER CHOICE WOULD HAVE BEEN THE SECOND PROJECTION ARRIVING.** A
> wound that outlived the screen is state surviving a fight, and
> `PLAY-STATE-01`'s projection stops being deferrable the moment one does.
> **I built the one that does not force it, and it is the one the spec
> already ruled** — but it is worth saying plainly: **a persistent wound is a
> design question, not a line of code**, and this slice did not answer it.

**What it costs today:** nothing a player would notice on a two-area bed with
one creature. **What it will cost:** the first time a fight is meant to be
interrupted and resumed.

---

## ⚠ 4 · The last open behaviour — and placing a real creature did not surface it

`down → dead` in one blow still writes **only `character.died`**.

**Hitting a real trooper hard gives no new reason to write both.** The seam
test drives exactly that case — a trooper at −12 with Constitution 13, one
blaster hit, straight past `down` to `dead` — and **one crossing, one event
reads correctly at the call site**: the report says the character died, which
is what `§4` asks the ledger to record.

**A reason to write both would be a listener that cares about `downed`
specifically** — a reaction bound to it, `ATTACHMENT-01`'s mechanism — and
**nothing binds one.** So it stays open, and it stays the smallest of the six.

---

## The count

**Six across five slices. Five ruled, one open, and this slice added none.**

| | |
|---|---|
| opposed-roll tie · critical confirmation | **`PT-1420`** |
| healing past `max` · negative damage as healing | **ruled by brief** |
| initiative tie · targeting tie | **`PT-1422`** |
| `down → dead` in one blow | **open** |

**⚠ But it added two readings that are not behaviours**, and they are flagged
the same way: **walking into something as the attack affordance**, and **the
wound not surviving the area**. Neither had to behave somehow — both are
choices with a reason, and the reason is written down.

---

## What was NOT built

**No turn order, no initiative, no doctrine in the app.** One attack, not a
fight — **nothing strikes back.** No equipment resolution. No screen affordance
beyond the arrow keys. **No persistence of anything a fight did.**
