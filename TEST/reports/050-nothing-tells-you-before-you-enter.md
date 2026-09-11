# TEST 050 — nothing tells you before you enter, the two unchecked rules, and one save that does not misfile

**Built against:** the **same two binaries as TEST 043–049.** App bundle
`kernel_blob.bin` built **16:11**, from `660134a` → Lodestar `9aa7382`. Loom bundle
built **16:39**, from `908a412`. **Neither rebuilt.** `47789fa` / `776e42e` /
Lodestar `e1a837c` remain untested by me.

**Instrument:** PID-scoped via `$!` + `pgrep -P`; app `632833`; every click computed
from `xdotool getwindowgeometry --shell` (the window opened at 360,192 this run, having
been at 320,171 last run — the reason I stopped hardcoding).

⚠ **Nothing outside my own bed was written**, and my bed was not touched this run
either. `endar-spire` + `base-rules` md5 identical; `tester-probe` `diff -rq` clean
against `PKG-T049`; saves restored from `SV-T042`, `diff -rq` clean.

---

## 1. There is no point before entering a package where its condition is visible

Checked every screen between the library and the board. **All four are negatives.**

| surface | what it shows | health? |
|---|---|---|
| Console Home library card | name, summary, author, version | **no** |
| …**hovering** it | adds a focus ring. Nothing else. | **no** |
| package main menu | `Continue / New Game / Load Game / Movies / Music / Options / Exit`, and a save count | **no** |
| New Game → NEW CHARACTER | *"Tester Probe supplies no premade characters"*, the package name top-right | **no** |
| **Loom's package picker** | ⚠ it is the **GTK directory chooser** — folder names and modification dates | **no, and it cannot** |

`Tester Probe` (13 problems) and `Endar Spire` (0) are **indistinguishable** on every
one of them. Loom's picker is the operating system's file dialog; it does not know what
a package is, so the earliest Loom can speak is after the open.

⚠⚠ **And the in-area band is narrower than I said in TEST 049.** It reports only
*"N drawn and not present"* — **name** faults. I have walked into `a03-probe-yard` and
`a04-probe-slit` perhaps thirty times this thread and **the app has never once
mentioned that they are one-way rooms.** Four of the five `tester-probe` saves are
marooned in them. So:

> **In the app, a position fault is invisible everywhere, forever.** The only fault the
> app will ever show you is an unresolved blueprint, and only once you are standing in
> the area that holds it. Everything `_position` finds — the one-way room, the
> unreachable door, the arrival in a wall — exists only inside Loom.

## 2. The two unchecked rules, measured rather than read

`record_validate.dart` has **four** `unchecked` sites, added conditionally:

| # | rule | when it is added |
|---|---|---|
| 1 | **skill ranks ≤ cap for their derived aptitude** | **always** |
| 2 | **every chosen feat's prerequisites are met** | if the record has any feat |
| 3 | a droid's abilities match its chassis spread | `level == 1 && isDroid` |
| 4 | every granted feat appears in that class's schedule | if any feat has `source == 'granted'` |

So *"2 rules unchecked"* is **1 + 2**, and it is a fact about the **character**, not the
package — which is why it reads identically in a clean package and a faulted one, and
why I was wrong to half-read it as a health indicator for several reports.

⚠ **I predicted a droid would read 3 and then loaded one.**

    HK-Nine · 3 rules unchecked

**Confirmed.** And #4 has **never fired on this machine**: every one of the twenty saves
carries only `source: chosen` feats, so **nobody has ever seen *"4 rules unchecked"***.

### What they cannot verify, in the source's own words

1. *"only the with-aptitude ceiling is enforced. The aptitude set is derived from five
   sources — `CHARACTER-RECORD-01 §3` — and that derivation is not built, **so a rank of
   3 on a skill with no aptitude passes**."* The hard cap actually enforced is
   `level + 3` = 4 at level 1.
2. *"`feats.json` carries no prerequisite field. Chain order is implied by
   `is_chain_head` and nothing states a prerequisite."*

### Would either package trip it if it could?

⚠ **The gap is not hypothetical — there are live candidates on the shelf.** Rank-3
skills, which are exactly the values the missing derivation would adjudicate:

    kaeda-vos.sav    acrobatics 3, alertness 3, beast handling 3
    ilyana-sorr.sav  mysticism 3
    kesh-alaan.sav   mysticism 3

⚠ **And I cannot say whether any is illegal, for the same reason the validator cannot:
the aptitude derivation is the missing thing.** That is the honest answer and it is the
sharp one — three saves sit at the exact value the unenforced half of the rule governs.

Rule 3 has four live subjects too: `hk-nine`, `ig-seven`, `t3-k9`, `t3-m4-probe` are all
`species = droid`. Rule 2 cannot be tripped by anything, because nothing states a
prerequisite to violate.

## 3. One of the fifteen does belong elsewhere — and it does not misfile

`listFor` does **not** assume. When the header has no `package` it replays the log and
reads `character.created`'s payload. Decoded all twenty:

    format-1 saves by the package their LOG names:
      endar-spire   14
      tester-probe   1        ← probe-walker.sav

⚠ **There is exactly one, and the fallback files it correctly.** Observed in the app:
`probe-walker.sav` appears in **Tester Probe's** Load Game list (as
*"probe-walker.sav · when not recorded"*) and is **absent** from Endar Spire's fifteen.
The arithmetic closes exactly: endar-spire 14 + `vekk-nal` = **15**; tester-probe 4 + 
`probe-walker` = **5**; 15 + 5 = **20**.

⚠ **And header and log agree on all five format-2 saves.** No save on this machine is
misfiled.

### ⚠ A thing I found while doing it: loading a format-1 save upgrades it

I loaded `hk-nine.sav` for the droid test and it was **rewritten**:

    before   format 1, 655 bytes, no header fields
    after    format 2, 754 bytes, package endar-spire · HK-Nine · scout · level 1
                                  · area a01-command-deck

**One arrival was enough.** The upgrade's fields are all correct. ⚠ But `savedAt` became
**21:52 today** — the moment of the upgrade, not Sep 9 when the character was actually
played, because a format-1 save never stored one and there is nothing to preserve.

⚠ **So opening an old save to look at it promotes it to newest**, and `_newestFirst`
orders both Load Game and `Continue` — **merely inspecting the oldest save on the shelf
makes it the one `Continue` resumes.** I restored `hk-nine.sav` to format 1 from
`SV-T042`, verified.

---

## What I did not check

- Loom `776e42e`, app `47789fa`, Lodestar `e1a837c`. Not in either bundle. Untested.
- **Whether `Options` or `Profile`/`Settings`/`Import` surface package health.** I
  checked the path a player takes into a game, not every screen in the shell.
- Whether a *granted* feat can be produced at all through chargen — I only observed that
  no existing save has one, so rule 4 is unseen rather than unreachable.
- Whether the rank-3 skills above are in fact illegal. Undecidable without the missing
  derivation; I am not guessing.
- `taris-undercity` was not opened this run.

## State

- **Nothing was written this run.** `tester-probe` `diff -rq` clean against `PKG-T049`
  (still 13 problems, four mine on purpose). `endar-spire` + `base-rules` md5 identical
  to the pre-TEST-047 baseline. Saves restored from `SV-T042`, `diff -rq` clean, with
  `hk-nine.sav` confirmed back at format 1. Contamination snapshot at `SV-T050-after/`.
- The NWN install was not read or written.
- My app killed by PID; Coder's Looms untouched.
