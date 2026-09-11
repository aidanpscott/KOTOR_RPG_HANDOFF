# TEST 051 — format-2 saves are not immune, and PT-1654 is not here yet

**Built against:** the **same app bundle as TEST 043–050** — `kernel_blob.bin` built
**16:11**, from `660134a` → Lodestar `9aa7382`. **Not rebuilt.**

⚠ **PT-1654 IS NOT IN THE TREE, LET ALONE MY BINARY.** `KOTOR-RPG-APP` HEAD is
`1721be8` (*PT-1648 — package health at the screen where a package is chosen*), and:

    strings kernel_blob.bin | grep -c PT-1654   →  0
    strings kernel_blob.bin | grep -c PT-1626   →  0
    strings kernel_blob.bin | grep -c PT-1523   →  9

**So §1 of the brief cannot be run.** Everything below measures `660134a`.

⚠ **And four slices have landed in the tree that answer things I filed, none of them
in my bundle**, so all four are **untested by me**:

    1721be8  PT-1648 — package health at the screen where a package is chosen   ← TEST 050 §1
    e2be241  repin lodestar — PT-1646's areaHasNoWayIn and PT-1647's sentences  ← TEST 048 §1, §2
    0b9370b  PT-1642 — the panel K2 ships, and Continue shows it
    17efc48  PT-1636 — three rulings that had landed in Lodestar reach a screen

**Instrument:** PID-scoped, app `635894`, clicks computed from geometry.

---

## 1. PT-1654 — what I will check when it lands

Not testable yet. Setting out the fixture now so it is not designed after the fact:

- **The save must be made beside a creature**, which is the case that exposed it.
  `a08-probe-orphan` is the wrong bed (unreachable); **`a01-probe-room`'s
  `from-probe-hall` arrival at 4,2 is the right one** — it is hemmed in by
  `probe-warden.probe-room.03` at 4,1 (a talker), `probe-sentinel.probe-room.04` at 4,3
  and `probe-sentinel.probe-room.08`'s neighbourhood, and TEST 044 §4 already showed it
  strands a player who cannot step diagonally.
- **The two outcomes to separate:** resume *beside* the talker (correct) versus resume
  *into* the conversation, or resume at the package's front door.
- **And I will re-run TEST 046's controlled sequence**, because PT-1654 touches the same
  writes: header vs ledger, load, then two transits.

## 2. ⚠⚠ Format-2 saves are NOT immune. The bug is live on every shelf, always.

**Measured, not reasoned.** Baseline of the five format-2 saves, newest first:

    2026-09-10 11:12:17  grave-digger      Grave Digger  @ a03-probe-yard
    2026-09-10 10:48:27  yard-tester       Yard Tester   @ a04-probe-slit
    2026-09-10 09:09:35  vekk-nal          Vekk Nal      @ a01-command-deck
    2026-09-10 08:42:04  grukk-ironjaw     Grukk Ironjaw @ a03-probe-yard
    2026-09-09 23:21:24  blade-tester      Blade Tester  @ a04-probe-slit   ← oldest by 9h

`Blade Tester` was **4th of 5** in Tester Probe's Load Game list, reading `22 ho…`.

I clicked it, let it arrive, and **pressed no key at all**. Read the file straight off
disk before doing anything else:

    format 2   size 893 → 896
    savedAt    2026-09-09 23:21:24  →  2026-09-10 21:59:44      ← the moment I opened it

Then Escape → Load Game:

    Blade Tester    level 1 duelist · a04-probe-slit · just n…     ← now FIRST
    Grave Digger    … 10 h…
    Yard Tester     … 11 ho…
    Grukk Ironjaw   … 13 h…
    probe-walker.sav  when not recorded

⚠⚠ **A 22-hour-old save became "just now" and jumped from 4th to 1st because I looked
at it.** `_newestFirst` orders **both** Load Game and `Continue`, so **opening a save to
see who it is makes it the save `Continue` will resume.**

> **Looking at a save is indistinguishable from playing it.**

### So the scoping question is answered: it will NOT age out

TEST 050 found this on `hk-nine.sav` and could not tell whether it was the format-1
upgrade path. **It is not.** `blade-tester.sav` was already format 2, already had every
header field, and behaved identically. The upgrade is incidental —
`main.dart:183` sets `savedAt: DateTime.now().toUtc()` on **every** `_saveBytes`, and
the arrival persists unconditionally, so **any open rewrites the file.**

### And the log grows from being looked at

    BEFORE  …character.died · character.moved {a04-probe-slit, 2,0}
    AFTER   …character.died · character.moved {2,0} · character.moved {2,0} · character.moved {2,0}

**Two more identical position rows**, at a square that did not change, for one open.
⚠ I did **not** separate which write produced which row — the sequence was load *then*
Escape, and TEST 046 established that `_leaveScreen` also writes. What is unambiguous is
the timestamp: it had already moved to 21:59:44 **before** the Escape, with no keypress.

⚠ This sharpens TEST 044 §3 rather than correcting it. That report said position is
written *"on load, on leaving, and when a fight starts"* — correct. What is new is that
**a load writes it even when nothing moved**, so `grave-digger.sav`'s six identical rows
need no fight-round explanation: **a save accumulates duplicate rows just from being
opened**, without bound.

## 3. The three rank-3 saves — logged as a watch item, not re-opened

`kaeda-vos` (acrobatics 3, alertness 3, beast handling 3), `ilyana-sorr` (mysticism 3)
and `kesh-alaan` (mysticism 3). ⚠ **Nothing to test and I did not touch them** — and
after §2 that abstention is load-bearing: **opening one to look would have rewritten it
and promoted it.** The day `CHARACTER-RECORD-01 §3`'s aptitude derivation is built,
those three are the bed; until then they are best left unopened.

⚠ And the format-1 arithmetic from TEST 050 — 14 + 1 + 5 = 20 — **stays closed. Not
re-opened.**

---

## ⚠ PT-1617 — a change in `endar-spire` that is not mine

    endar-spire/dialogue/trooper-challenge.toml   modified 21:56 today
    md5  a7dfe968… → 40087cc2…    now 1652 bytes, 66 lines

**Reported, not reverted.** I did not touch `endar-spire` this run — I loaded a
`tester-probe` save — and 21:56 falls between my TEST 050 run and this one. It is the
only file in either package that moved; the other 39 are byte-identical. Presumably part
of `PT-1642`/`PT-1636`. **I have re-baselined my md5 file to the new state** so the next
run compares against what is there now rather than reporting this twice.

## What I did not check

- **PT-1654, PT-1648, PT-1646, PT-1647, PT-1642, PT-1636.** None are in my bundle.
  Untested, all six.
- Whether the **load** alone writes one position row or two. I read the timestamp before
  the Escape but the log after it.
- Whether `Continue` (rather than `Load Game`) also rewrites on open. I used Load Game.
- Whether an open that ends in **Exit to Library** rather than Escape writes the same way.
- The three rank-3 saves, deliberately.

## State

- Saves **restored** from `SV-T042`, `diff -rq` clean; contamination at `SV-T051-after/`.
- `tester-probe` **unchanged** — `diff -rq` clean against `PKG-T049`. Still 13 problems,
  four mine on purpose.
- `base-rules` unchanged. `endar-spire` changed by **someone else**, reported above,
  re-baselined at `pkgs-baseline-T051.md5`.
- The NWN install was not read or written.
- My app killed by PID; Coder's Looms untouched.
