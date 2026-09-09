# 50 · `PT-1464` — the bar at the class step, the notes out of the cells

**642 green** — Lodestar 293 · Lens 4 · Loom 115 · app 230.
`app edaf92d` · `MAIN_WORK 25f7472`.

---

## 1 · ⚠⚠ The bar moves, and the regression was mine

**Wiring `droid_arrays` at `BUILD 46` hard-blocked four classes.** Soldier,
Marksman, Brawler and Saboteur reached Equipment and got *"this step cannot
complete for this class"* — **OK disabled, Cancel the only live button.**

> **⚠ And Soldier is the pre-selected default.** Pick Droid, leave the class
> alone, and you cannot create a character. **Before the wire all thirteen
> completed with the wrong kit; after it, four were dead ends.**

**⚠ I called `null` "the honest answer" and asserted it in a test.** It *is*
honest — `STARTING-EQUIPMENT-01 §3` opens nine of eighteen classes to a chassis
and means it, so **a missing droid array is that line, enforced.** What was
wrong is **where** it was enforced.

**Both bars run through one mechanism now**, because a droid meets both — no
Force class (`PT-92`) *and* only the nine. Barred entries are shown,
unselectable, with the reason, which is what `PT-92` already did.

**⚠ And a test asserts the two halves cannot drift:** every class a droid may
take **has** an array, and every class it may not is refused earlier. **If those
ever disagree, Equipment becomes a dead end again** — that is the assertion, not
the count.

---

## 2 · The notes leave the cells — in BOTH tables

**They were inside the values, and the moment something read the droid table
they printed to players** — *"1 Sensor Probe — was Adrenal Stamina"* on the
Equipment screen.

> **A cell holds a value. What was done to it is a note, and a note is not a
> value.**

Both notes moved above their tables, keeping every remark: what each row was
converted from, and the three melee halves a chassis cannot hold.

### ⚠⚠ And I extended scope by four cells, deliberately

**The ORGANIC table has the identical defect and reached a player FIRST**,
because that table has been read all along:

    weapon = "Ion Blaster — w_blaste_02, 50cr"        ← a RESREF, on screen
    weapon = "NONE — the class feature is the weapon"
    weapon = "Vibroblade — ONLY, and the only class that gets one"

**That is `TEST 004`'s `D3` exactly, from inside a value.** Fixing only the
droid half would have left the same defect **where a player already sees it**,
so I took both. **Same file, same edit, four extra cells — flagged rather than
quiet.**

---

## 3 · ⚠⚠ The player's own attack line was never rendered

**`Tester` could not close this and reported it as a gap.** It never saw its own
attack across **four fights** and put it down to the trooper acting last.

**It is structural.** `_playerStrikes` set `_said` and `_enemyTurns` overwrote
it **in the same synchronous call**, so the player's line never reached a frame
— **it would have happened in a round the trooper lost too.**

> **So `PT-1326`'s format was verified on NPC attacks only — not because the
> player's differs, but because it never reached a screen.**

**Two lines now — what you did, then what came back.** ⚠ **Bounded by
construction:** `PT-1453`'s N2 is exactly why this is a composition of two and
**not an accumulating list.**

**Controlled:** with the composition removed the new end-to-end test fails on
that line, and passes when restored.

---

## 4 · One test was relying on the defect

`subrace_test` drove a droid into **Soldier** and completed — **precisely the
behaviour the bar removes.** It takes Scout now, with the reason written in.

**⚠ That is worth naming rather than quietly editing:** a test that passes only
because a rule is unenforced will keep passing after the rule arrives, and the
first sign is a failure that looks like a regression.
