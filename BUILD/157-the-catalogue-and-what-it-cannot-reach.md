# BUILD 157 — a class that was never casing, and a catalogue with three verbs it cannot reach

---

## 1 · ⚠⚠ `PT-1810` — IT WAS NOT A CASING DIFFERENCE

`Tester` saw `Soldier` on the player's row and `soldier` on a companion's, and
traced it to two sources. **It is not casing — they are two different KINDS of
value:**

    the player's row     ClassRecord.name           the DISPLAY NAME
    a companion's row    character.characterClass   the blueprint's class ID

They coincide up to capitalisation for **exactly the single-word classes**,
which is why it looked like casing. **`bounty_hunter` is `Bounty Hunter`, which
no capitalisation of the id produces.**

So the id is resolved through the same `classes` map `baseAttackAt` already
reads, and **the case that holds it names a multi-word class on purpose** — a
fix that upper-cased the first letter passes on `soldier` and fails there.
Mutation-checked exactly that way: the capitalising version kills two cases.

**⚠ THE RAW ID SURVIVES AS THE FALLBACK**, deliberately. A blueprint naming a
class the rules do not carry still deserves a label, and showing what it
actually said is how somebody finds the typo — the standing `PT-1493` gives a
placement whose blueprint will not open.

**⚠⚠ AND THE BED COULD NOT HAVE SEEN IT.** It never passed `classes` at all, so
a lookup through that map could not fail visibly — **`PT-1708`'s shape in a test
bed.** `main.dart` has always filled it from the shelf, so the product was fine
and the bed was blind. It passes them now.

## 2 · ⚠⚠ `§3a` — THE EXPLORATION ACTION CATALOGUE

> *"One flat table of possible verbs, each filtered in or out by context —
> shown only when genuinely relevant to whatever's currently clicked or nearby,
> **never a fixed menu everyone sees regardless of situation.**"*

A **table plus a filter**, not a sixth budget — which is the ruling's own point:
combat is closed *"because fairness depends on everyone having the same defined
choices"*, and exploration has no such pressure.

**⚠ A CONSTANT IN THE ENGINE RATHER THAN SHIPPED DATA.** `roleNames`, `gateKeys`
and `engineWrittenKinds` are the precedent: a closed vocabulary **the product
owns** lives in the engine, and only what an **author** varies lives in
`base-rules`. **A package does not invent verbs.** But every skill a verb names
is the shelf's, and a case holds that — a verb naming a skill `skills.toml`
does not carry rolls nothing, silently.

`PT-1123`'s governing rule is a **set** rather than two string comparisons,
because the reasoning generalises:

> *"If using a skill on a person requires communicating with them, it belongs to
> dialogue alone; if it's something physical done to a person or their things
> without requiring exchange — Pick Pocket, for instance — it's a normal
> exploration-catalog verb."*

## 3 · ⚠⚠ AND THREE VERBS ARE UNREACHABLE — ASSERTED, NOT HIDDEN

`Search`, `Track` and `Examine` aim at things **`AREA-FORMAT-01` cannot hold.**
An area carries creatures, connections and arrivals: there is **no container, no
vehicle, no beast marker**, and nothing that says what a thing is *about* — which
is exactly what `Examine` needs to *"auto-pick Xenology, Archaeology, Mysticism,
or Science by what's actually clicked."*

They are in the catalogue **because `PT-1123` locked them**, and unreachable
because the format has nowhere to put their targets.

> **A filter that silently never returned them would look like a working
> filter.** So a case names all three, asserts they are offered for no target
> kind — and **fails the day the format gains an object kind**, which is when
> somebody should look at them again.

Every omission carries its reason too — Alertness passive, Beast Handling and
Pilot only when present, Acrobatics/Athletics/Swim folded into movement —
because *"confirmed gaps rather than oversights"* only works if the reason is
written next to the gap.

## 4 · ⚠ WHAT `§3a` STILL NEEDS, AND IT IS THE SAME DOOR AS EVERYTHING ELSE

    object-directed   a context menu at the point of contact — ⚠ THE FIRST
                      POINTER IN THIS SCREEN, which is `PT-1443`'s question
    self-directed     the player's own card — `§2`, behind the same door
    party-directed    ⚠ THE SIDEBAR, WHICH EXISTS as of `PT-1794`

**The party-directed three are the only ones with a home already built**, and are
what I would wire next.

---

## What ran

    Lodestar   690 tests   exit 0   (+8)
    Lens        13 tests   exit 0
    Loom       263 tests   exit 0
    app        562 tests   exit 0   (+2)
    flutter build linux     built
    check_engine_pin        4 compared · all level

Mutation-checked: a second path into Persuade kills four cases; one verb
offered on two target kinds kills the filter case; capitalising the class id
kills two.

## Heads

    Lodestar        1e17025
    Lens            e79bc06   (unchanged)
    Loom            e60942b
    KOTOR-RPG-APP   24ade3d
    MAIN_WORK       461753b   (unchanged)
