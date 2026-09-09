# 41 · The runner faked a pass, and the wound survives a quit

**595 tests green** — Lodestar 270 · Lens 4 · Loom 111 · app 210.
App `4f8a242`. **Three things from `Tester`'s first report, all `Coder`'s.**

---

## 1 · ⚠⚠ The runner only built when the binary was MISSING

    [ -x build/.../kotor_rpg_app ] || flutter build linux --debug

**So an edited source with a built binary ran the old code and said nothing.**
`Tester` caught it live: the bundle was `21:31` while `hub.dart` and
`save_store.dart` — the two files carrying the save work — were `22:10` and
`22:11`. **Following `requests/001` literally would have confirmed six fixes
against a build containing none of them**, with nothing anywhere looking wrong.

**⚠ AND IT IS WORSE THAN "SOMETIMES STALE".** `[ -x ]` tests **existence**, so
after the first successful build it would never rebuild again — for any change,
ever. The binary's own mtime is not even a signal: `kotor_rpg_app` is the C++
runner and **does not change when Dart changes**; the Dart lives in
`data/flutter_assets/kernel_blob.bin`.

**Fixed by deleting the conditional.** Both runners always build.

**⚠ It was buying 3.4 seconds** — measured, the cost of a no-op build here; a
real change is ~7s. **A cleverer staleness check is just a second thing that
can be wrong**, and `flutter build` already knows what is stale.

**Verified rather than assumed:** an observable Dart edit changes
`kernel_blob.bin`, so a source change now reaches what runs. *(The blob is not
byte-identical across builds, so no determinism is claimed.)*

**⚠ And the fix lives in an unversioned file.** `run-app.sh` is in the tree
root, which is not a repository — so the reasoning is written into `README.md`
and its versioned copy `docs/RUNNING-ON-THIS-MACHINE.md`, the same way
`env.sh`'s `clang` shim was.

### ⚠ Does anything else have that shape? — asked, and answered with scope

**Instruments that report success without having looked. Three kinds:**

| | |
|---|---|
| **Shell scripts that skip work when an artifact exists** | ⚠ **None left.** Grepped every `*.sh` in the tree for `[ -x`/`[ -f`/`[ -e`/`[ -d`; the only hit is the comment in `run-app.sh` describing the bug |
| **Tests with no assertion at all** | **Two, both known and both deliberate** — `capture_test` and `capture_dialogue_test` write 29 PNGs and assert nothing. That is what a capture is for; it is named here so it is not mistaken for coverage |
| **Checks that pass having examined nothing** | ⚠ **The shape exists.** Run from an empty tree, `check_derived`, `check_absence_claims` and `check_stale_claims` all **exit 0** — reporting *"0 declared pair(s)"* and *"0 documents known"*. **They print the denominator, so a reader sees the zero, but the EXIT CODE lies** and automation reads the exit code |

**⚠ AND A FOURTH KIND FOUND WHILE FIXING §3: a test that lies about its
viewport.** `MediaQuery` said 1280×720 while the test surface stayed Flutter's
default **800×600**, so widgets sized themselves for one screen and were laid
out in another. It produced a **78px "overflow" that does not exist in the
product**. **23 test files across the app and Loom have that shape** — the one
that mattered here is fixed and the rest are **reported, not swept**, because
a 23-file sweep unasked is how a slice stops being reviewable.

**Two incidental findings, pre-existing and not mine:** `check_citations` exits
**1** on `TEMPORAL-LEAKAGE-FINDINGS-01 §2`, and `check_extracts` reports
**`stale 1`**.

---

## 2 · ⚠⚠ The wound did not survive a quit — `PT-1427` was filed as done

**`PT-1427` built the second projection and nothing wrote what it folds.** The
exploit it closed closed only **within a session**: walk out and back and the
trooper is hurt; **quit and reopen and he is whole.** `play_screen.dart` said
so in its own comment — *"in memory for this session only. Nothing appends it."*

> **`PT-1427`'s own line is the test: *"a fight is not a fact, its outcome
> is."* An outcome that dies with the process is not an outcome.**

### ⚠ The question the old comment called undecidable was already decided

It said this *"needs a decision about whether play events join the character's
log or a campaign log, which is not mine to make."* **Two rulings already
answer it:**

- `encounter.ended` is **`campaign`** lifetime — `EVENT-KINDS-01`, confirmed in
  the shipped `event_kinds.toml`.
- `PT-1415` makes the character's log **one log per character PER CAMPAIGN**.

**A campaign-lifetime event about this character in this campaign has exactly
one home, and it is that file.** No new ruling was needed, and none is claimed.

### ⚠ Two paths end an encounter and only one was persisted

`_endFight` when the fight is over, and **`_enter` when you walk out of the
area** — and the second is the one `Tester` actually walked. It wrote the
outcome into the in-memory log and handed it nowhere. **Both persist now.**

### ⚠ And the log was being thrown away after replay

`_open` folded the save into a record and **dropped the events**, so play had
nothing to append to and the screen had nothing to project a wound from. The
App keeps the log and the save id; `PlayScreen` is **seeded** from it instead
of starting empty.

**It rewrites the whole file rather than appending**: the format has no append,
the files are under a kilobyte, and a partial write of a gzip payload is a save
that will not open.

### ⚠ The test is controlled in both directions

It asserts the save carries **no** outcome before leaving and **one** after —
and **with persistence disabled it fails on exactly that line.** It is
`Tester`'s repro end to end: fight, leave the area, quit, reopen, `Continue`.

---

## 3 · The migration allowance is gone

`PT-1445` kept a branch matching a package's **display name** for saves written
before the id ruling, and said it could go once no save carried one.

**`Tester` checked the folder. I checked it again independently:** all three
saves on the machine carry an **id that exists in the library**, and nothing
can create otherwise — the single writer is `LedgerWriter.preHub` and it is
given `packageId`.

**Dead code that looked like caution. A branch no input reaches is a branch no
test can prove.** Removed.

---

## 4 · ⚠ What of `Tester`'s report is NOT addressed here

**Eight defects and three questions were filed. This slice took the two the
owner assigned plus the dead code.** Left open, and named so they are not
lost: **D1** the hub saying nothing is saved directly above the button that
saves — *the sentence that produced `PT-1443`* · **D2** the speaker shown as a
tag, and the wrong tag (`.07` in conversation, `.39` in the fight log) · **D3**
raw spec text rendered as a player-facing choice · **D4** `Back` from the
pre-hub boundary discarding species · **D5** two contradictory health numbers
on screen · **D6** *"left you at"* printed for the NPC · **D7** overlapping
text at the foot of the play screen · **D8** Loom's entry-area chooser below
the fold, **which is `BUILD/34`'s rule a fourth time**.

**And three for the owner:** a character at **negative vitality walking around
normally**; **droid-only feats offered to an organic**, which is the same
missing format `STATE.md` lists as *feat prerequisites*, seen from the offer
side; and a package getting `base-rules` **without declaring it**.
