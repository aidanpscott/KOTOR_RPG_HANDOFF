# 019 · Fifteen characters, one trooper, ten answers

**From `Tester`. Unrequested number.** `PT-1512`'s rule followed: packages and
saves backed up before anything, packages restored **IDENTICAL**.

**Built 17:22; no commits landed since, so this is the same binary as `018`:**

    Lodestar 7fc7620 · Lens 9ca5982 · Loom cc9dc60 · app 776f088

**Pins honest** — both locks resolve `lodestar` to `7fc7620` = `HEAD`.
**1280×720.**

---

## ⚠⚠ THE SHIPPED BED ALREADY PROVED `PT-1510`, AND NOBODY HAD LOOKED

**I did not need to make a second character. `endar-spire` has FIFTEEN.**

I read the saves off disk rather than guessing — the header is `KRSV`, a `u16`
version, a compressor name and a version string, **19 bytes**, then gzip, then
JSON-Lines. `PACKAGE-FORMAT-01`'s *"a modder can look"* is true of saves too.

**Ten of the fifteen have fought `sith-trooper.command-deck.39`, and they
disagree about what it is:**

| left the trooper at | characters |
|---|---|
| **7** | `second-fight`, `vess-taran` |
| **12** | `kesh-alaan`, `t3-m4-probe` |
| **14** | `ilyana-sorr`, `t3-k9` |
| **16** | `ig-seven`, `sero-kade`, `wren-ossik` |
| **17** | `rell-vantt` |
| **never met it** | `bran-vex`, `dax-roon`, `hk-nine`, `kaeda-vos`, `vekk-nal` |

**⚠ CONFIRMED ON SCREEN, NOT JUST IN THE FILES — both directions:**

- **Vess Taran**, on arrival at the Command Deck:
  *`sith-trooper.command-deck.39: 7 of 18 — encounter a01-command-deck left you
  at 7`*
- **Bran Vex**, same package, same creature, same minute: **no line for the
  trooper at all.** I walked into it and got the bed's full six-option node —
  a whole trooper, no memory of anyone having touched it.

**So `018`'s finding is not a property of a package I built. It is what the
shipped bed does**, at a scale nobody had looked at: **one tagged creature with
ten different current vitalities and five characters who have never heard of
it, all at once.**

**And the trooper's true maximum is 18** — visible only because someone left it
at 17. Nine of the ten values are wounds nobody else can see.

---

## ⚠⚠ `Load Game`'s ORDER IS DIRECTORY ORDER — FIFTEEN ROWS SETTLE IT

**At `018` I said I could not separate alphabetical from directory order with
two saves. Fifteen is decisive.** As listed:

    sero-kade · ilyana-sorr · bran-vex · kesh-alaan · dax-roon · vess-taran
    vekk-nal · t3-m4-probe · hk-nine · ig-seven · kaeda-vos · wren-ossik
    second-fight · t3-k9 · rell-vantt

- **Alphabetical would start** `bran-vex, dax-roon, hk-nine…` — **it does not.**
- **Most-recent-first would start** `bran-vex, ig-seven, wren-ossik…` — **it
  does not.**

**It is the order `Directory.list()` yields**, which `save_store.dart`'s `list()`
appends in and **nothing sorts**. On this filesystem that is hash order:
arbitrary, stable, and meaningless to a person.

**⚠ The consequence, and it is worse than untidy:** `Continue` opens the most
recent, and `Load Game` — the screen that exists so a player can *choose* —
presents the same fifteen in an order that is neither the one `Continue` uses
nor one a person can predict. **A player looking for "the one I played
yesterday" must read fifteen filenames in scrambled order**, and the only
distinguishing field is the id: every row also reads `rules 0.1.0`.

**Fifteen rows do fit at 1280×720**, with roughly three rows of headroom before
the dialog reaches the screen edge. **I did not test what happens past that.**

---

## ⚠ THE VACATED SQUARE — I COULD NOT REACH IT, AND THE REASON IS THE FINDING

**At `018` I reasoned the wall-under-a-creature trap from `passable` rather than
watching it, and you were right that the difference matters. I went to kill the
creature. It cannot be killed.**

I repainted the wall under `probe-sentinel.probe-room.04` and fought it with a
character at 1 vitality until I won:

> `probe-sentinel.probe-room.04: 1 of 8 — encounter a01-probe-room left you at
> **−2 · revived at 1**`

**Struck to −2, and standing again at 1 the moment combat ended** — the same
rule the screen states when I lose: *"anyone left down stands at 1 when combat
ends."* A new fight was already rolling initiative against it.

**So a placement is permanent for the life of a character.** A creature is never
removed from its square, and **the square under it never becomes empty**.

**⚠ Which corrects `018`.** I wrote that the trap arrives the day something is
left on the ground. **It needs TWO absent things, not one:**

1. something that can be left on a square (`INVENTORY-01`), **and**
2. **a way for a square to become empty at all** — which today does not exist,
   because nothing dies.

**The wall under a creature is not merely harmless today. It is unreachable.**
And that is a better answer than the one I reasoned, so the instruction was the
right one.

**⚠ Everything else from `018` held on re-test:** Loom writes the wall without
comment, verify still reports 3 problems and has no `PackageProblem` for a
creature on an impassable tile, the app draws the creature inside the wall, and
occupancy is tested before passability so the wall changes nothing about
reaching it.

---

## ⚠ ONE THING I NOTICED WHILE READING THE SAVES

**`listFor` replays every save's entire log to discover which package it belongs
to.** With fifteen saves in one folder that is fifteen gunzips and fifteen full
replays **every time the hub opens**. It was named as known in request `001`
(*"`listFor` reads every log to find the package"*), and I am not filing it —
**but the folder is now seventeen files and the cost is per-open, not
per-package.** Worth knowing before it is thirty.

---

## ⚠ SCOPED NEGATIVES

- **I made no new characters this run.** `endar-spire`'s fifteen already
  existed, so the second-character case was proved on saves written by earlier
  sessions rather than by this one. **That is exactly what `PT-1512` is about,
  so: the ten outcome values were read from files this run did not write, and
  the two I confirmed on screen (`vess-taran`, `bran-vex`) were loaded and read,
  not authored.**
- **I did not test whether the list order changes** when a save is added or
  removed — I only observed one ordering, twice.
- **The vacated square remains unobserved, because it cannot be constructed.**
  My claim is that nothing vacates, which I watched; the trap beyond it stays
  reasoned and I am labelling it so.
- **I did not check whether a creature revived at 1 stays at 1 across a quit** —
  I saw the revive within one session only.
- **Still untested from `018`:** water or hazard under a creature, a creature
  walled in on four sides, and **line of sight** — `wall.blocksSight` is true
  and nothing I ran reads it.
- **I did not test `Continue` when the most recent save is corrupt**, or after
  deleting a save.
- **Not touched:** the eight inert blueprint kinds, `NewItemDialog`, other
  window sizes.

---

## ⚠ WHAT THIS RUN CHANGED, DECLARED

**Packages: nothing.** `diff -r` against the pre-run backup reports
**IDENTICAL**.

**Saves: two, by playing them, which is the product working —**

- **`bran-vex.sav`** 748 → 823 bytes. **⚠ It was one of only five bed characters
  with no encounter outcome, and I spent it**: walking into the trooper and
  taking `Stand aside` gave it one. **Four untouched controls remain** —
  `dax-roon`, `hk-nine`, `kaeda-vos`, `vekk-nal`. **I did not revert it**,
  because reverting a real play result is a worse lie than declaring it.
- **`yard-tester.sav`** 883 → 914 bytes, from the wall-creature fights.

**Seventeen saves before, seventeen after. Nothing was deleted.**
