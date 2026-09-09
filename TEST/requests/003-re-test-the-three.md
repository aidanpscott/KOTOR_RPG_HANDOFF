# 003 · Re-test the three you found — and one of them was a hazard to you

**From `Coder`. `BUILD/41`, `PT-1448`.** App `4f8a242`.

**Your report was the most useful thing this project has produced in a
stretch.** Three of your findings are fixed; **eight defects and three
questions are not**, and are named below so you know they were read.

---

## ⚠ THE RUNNER — you were running the wrong build, and so was everyone

**Fixed. Both runners now always build.** The conditional was
`[ -x <binary> ] || flutter build` — and it is worse than you diagnosed:
`[ -x ]` tests **existence**, so after the first successful build **it never
rebuilt again, for any change, ever.**

**⚠ And the mtime you compared could not have told you either way.**
`kotor_rpg_app` is the C++ runner and **does not change when Dart changes** —
the Dart lives in `data/flutter_assets/kernel_blob.bin`. Your conclusion was
right; the signal you used would have looked stale even on a fresh build.

**You no longer need to rebuild by hand.** `./run-app.sh` costs ~3.4s more when
nothing changed.

---

## What to re-test

**1 · The wound survives a quit.** Your repro, exactly: `Continue` → walk into
the trooper → *"Stand aside."* → hit it → walk away → leave the area → **quit
the app** → reopen → `Continue`.

**⚠ Claim: the working line comes back with the character.** Both the trooper's
vitality and yours.

**What changed:** two paths end an encounter — the fight ending, and **walking
out of the area, which is the one you took** — and only the first was ever
handed up to be saved. Neither was persisted at all, because the App threw the
log away after replaying it.

**2 · The migration allowance is gone.** You checked the folder and I checked
it again: all three saves carry an id. **Claim: `Load Game` and `Continue`
still list exactly the right saves per package** — the branch that went was
dead, so nothing should change. **Attack claim 1 of request 001 again briefly**;
if a save stops being listed by its own package, that removal is why.

**3 · The runner.** Edit nothing, run `./run-app.sh`, and confirm it builds
before it opens.

---

## ⚠ What I could not see

- **Whether the working line is legible on return.** It shows the trooper *and*
  you, and **D7 — your overlapping-text finding — is not fixed**, so the line
  it collides with is the one carrying this.
- **Whether a second fight after reloading behaves.** I tested one fight, one
  quit, one reload. **Two encounters across a restart is untested by me.**

---

## ⚠ NOT FIXED — read before re-filing

**All still open, and all read:** **D1** the hub saying nothing is saved
directly above the button that saves *(the sentence that produced `PT-1443` —
the sharpest of the eight)* · **D2** the speaker shown as a tag, and the wrong
one · **D3** raw spec text as a player-facing choice · **D4** `Back` discarding
species · **D5** two contradictory health numbers · **D6** *"left you at"* for
the NPC · **D7** overlapping text · **D8** Loom's entry chooser below the fold.

**⚠ D8 is `BUILD/34`'s rule a fourth time** — *anything you can click must be
laid out where it can be seen* — and you found it in a program I had not
applied it to.

**U1, U2 and U3 are the owner's**, not mine, and they are in `STATE.md` now.

**⚠ Please do not re-file these.** If you have spare capacity, **D4's open half
is the most useful thing you could close**: you scoped it honestly to *species*
and could not tell whether **class** is discarded, because `Soldier` is the
first row. **Pick a non-first class and repeat.**

---

## ⚠ Something your report changed about how I test

**Your viewport finding is mine, not yours, and it is bigger than one test.**
While fixing the wound I hit a 78px overflow that **did not exist in the
product**: `MediaQuery` claimed 1280×720 while the test surface stayed
Flutter's default **800×600**, so widgets sized for one screen were laid out in
another. **23 test files across the app and Loom have that shape.** One is
fixed; the rest are reported.

**So if I ever hand you a layout claim backed only by a widget test, distrust
it.** That is now a documented reason to.

---

## Data safety

**All four suites are hermetic** — 595 green, and the live folder is untouched
by a full run. **`tester-probe` and your two saves are still there and still
yours.** `vess-taran.sav` and `probe-walker.sav` were written before this fix,
so **they carry no encounter outcome** — a fresh fight is needed to see the new
behaviour.

**Report as `reports/003-re-test-the-three.md`.**
