# TEST 052 — PT-1654 and PT-1657 confirmed, the fallback earns its event, and two fixes I found by accident

**Built against:** `run-app.sh` and `run-loom.sh`, which **always rebuild** — that is
their whole point, per their own header comments (*"the conditional that used to be
here faked a pass… a build with real changes is ~7s. Three seconds is not worth a
silent wrong answer"*). I have refused to run raw `flutter build` for eight reports
running because that writes into Coder's tree; **the sanctioned launcher is not the
same act**, and using it is the only way to test anything Coder ships. Declaring the
result rather than assuming it:

    git log -1 --oneline      → 7d2c63f PT-1654, PT-1657 — the race is shipped, and a read stops writing
    kernel_blob.bin           → built 22:17 (was 16:11)
    strings … | grep -c PT-1654 → 2
    strings … | grep -c PT-1657 → 1
    strings … | grep -c PT-1658 → 0

⚠ **The brief named "PT-1658"; the shipped commit calls it PT-1657.** Everything below
is PT-1654 and PT-1657, and I am using the commit's own numbers.

**Instrument:** launched via `nohup ./run-app.sh &`/`./run-loom.sh &` with `exec`
replacing the shell, so the backgrounded shell PID **is** the app/Loom PID directly —
no `pgrep -n`, no child-hunting. App `640307`, Loom `644537`, killed by PID at the end;
Coder's Loom `517968` survived, the control.

⚠ One of my own coordinate reads was wrong for the first half of this run (I read
button positions off a `-resize 60%` preview and clicked those numbers as if native —
several early clicks landed on the wrong control). Caught it, switched to cropping
native 1280×720 captures for every click going forward. No damage: every wrong click
either did nothing or was immediately visible and backed out of.

---

## 1. PT-1654 — confirmed on my own fixture, and the fixture is now proven correct too

Built exactly the case set out in TEST 051: a fresh character (**Resume Tester**,
Human Soldier), walked to `a01-probe-room`'s `from-probe-hall` arrival at **(4,2)** —
hemmed in by `probe-warden.probe-room.03` (a talker, `conversation =
"dialogue/sentinel-challenge"`) at (4,1) and `probe-sentinel.probe-room.04` at (4,3) —
and pressed Escape to write the crossing.

⚠ **Correction to my own past reasoning, in passing.** TEST 044/045 treated (4,2) as
permanently sealed on three sides. Two of those "blockers" — `probe-sentinel.probe-
room.01` and `probe-warden.probe-room.02` at (3,2)/(1,2) — carry a doubled
`blueprints/characters/` prefix and **never resolve** (`"not a creature path, expected
'characters/…'"`), so they were never actually there. (4,2) is reachable from the west
side of the room through (3,2). The two REAL neighbours — the talker at (4,1) and the
sentinel at (4,3) — are exactly what the fixture needed anyway.

**Escape → Continue, and the outcome:**

    you notice probe-warden — 14 against 0

Player marker on the exact `from-probe-hall` cell. **No conversation opened. No fight
began. No front-door reset.** The message is an ordinary stealth notice, the same
shape as every other `PT-1576`-matrix discovery this thread — not the talker's
dialogue firing. ⚠⚠ **Resumed beside the talker, which is the correct outcome, and the
other two named outcomes — resume into the conversation, resume at the front door —
did not happen.**

### TEST 046's controlled sequence, re-run: the header staleness is UNCHANGED

Ran it exactly as before — load, then two transits — with header and ledger read from
the file after each:

| step | header `area` | ledger's last `character.moved` |
|---|---|---|
| after Escape at (4,2) | `a01-probe-room` | `a01-probe-room 4,2` — **agree** |
| Continue, walk to a02, Escape | `a01-probe-room` | `a02-probe-hall 0,0` — **disagree** |
| Continue, walk back through a01 to a05, Escape | `a02-probe-hall` | `a05-probe-barrier 5,2` — **disagree** |

⚠⚠ **PT-1654 fixed the RACE and the resume position. It did not touch the header
staleness bug from TEST 045/046.** The header still freezes at the area the *session
began in* and only advances on the next load — identical mechanism, identical
symptom, unchanged by this ship. These are two different bugs sharing one file format,
and only one of them shipped.

## 2. PT-1657 — confirmed on the exact reproduction, twice

**The declared control, byte for byte.** `blade-tester.sav` before touching it:

    md5    f8cd2ad8f8ded4b5a95136a9326d429f
    savedAt  2026-09-09 23:21:24
    events   32

Loaded it from Tester Probe's Load Game list (4th of 5, reading `23 ho…`), let it
arrive, **pressed no key at all**, read the file immediately:

    md5    f8cd2ad8f8ded4b5a95136a9326d429f   ← unchanged
    savedAt  2026-09-09 23:21:24               ← unchanged
    events   32                                ← unchanged

**Byte-identical.** Escaped back out and reopened Load Game: Blade Tester was still
4th, still `23 ho…` — no reordering. ⚠⚠ **This is the exact save and the exact
procedure that found the bug in TEST 051. It is now closed on that reproduction.**

⚠ **And I got a second confirmation by accident.** My first click at the Tester Probe
menu missed Load Game and hit Continue, loading `grave-digger.sav` straight into the
board. I backed out without pressing any other key and diffed the file:

    645a74a3132ddd0c50c7e59bba21ac7a  grave-digger.sav (after)
    645a74a3132ddd0c50c7e59bba21ac7a  SV-T042/grave-digger.sav (baseline)

**Also byte-identical**, on a different save, loaded a different way (Continue rather
than Load Game). The fix holds on both entry points.

## 3. PT-1605's fallback still earns its event — measured with a before/after count

The brief's third question, and I do not think anyone had reasoned through why it was
worth asking: **PT-1657 stops a *read* from writing. A fallback is not a read — the
saved position genuinely could not be honoured, so something must actually change.**
The risk was that the fix, in closing the read path, also closed this one by mistake.

Built it as a controlled edit rather than hunting for a naturally-arising case:

1. Walked Resume Tester to `a05-probe-barrier` (8,3) — plain floor, not an arrival or
   door landing. Escaped. Confirmed the write: `character.moved a05-probe-barrier 8,3`,
   **event count 24**.
2. Backed up `tester-probe` (`PKG-T052-before/`). Edited `a05-probe-barrier.toml`,
   turning (8,3) into a wall — the one square the save now names — with a comment
   explaining the fixture and its expectation, in the same style as `a07`/`a08`/`a09`.
   Verified: `tomllib.load` parses; nothing else in the file touched.
3. `Continue` again, reading the file live from disk.

**Result:**

    Probe Barrier · the square you left is not standable, so you are at 0,0

Player marker on (0,0). Reading the save straight after:

    event count  24 → 25
    new row      {"kind":"character.moved","payload":{"area":"a05-probe-barrier","x":0,"y":0}}

⚠⚠ **One new event, and it is exactly the fallback's landing square.** PT-1605's
guarantee — *"a fallback is a real crossing and earns its event"* — held under the new
write ordering. The fallback path was not silenced along with the ordinary
read-and-do-nothing case.

**Verified the edit introduced no side effects.** Re-opened `tester-probe` in a fresh
Loom: `a05-probe-barrier` expands with every row in normal colour — no new fault from
the wall. The package's count moved 13 → 14, and isolating why (below) shows the wall
contributed **zero** of that.

---

## 4. Two more slices shipped, and one closes a gap I filed myself

⚠⚠ **PT-1646/1647 landed, and `areaHasNoWayIn` now exists.** TEST 048 found the gap —
*"there is an `areaHasNoWayOut` and no `areaHasNoWayIn`… a declared area that nothing
leads to is reported by nothing"* — and TEST 049 measured it precisely (a fully
furnished, unreachable room contributing zero). Opening my bed in a freshly-built
Loom:

    a08-probe-orphan
    "a08-probe-orphan" is in the manifest and no connection anywhere in this package
    leads to it, and it is not the entry area. Nothing in it can ever be reached —
    its placements, its conversations and its own way out included.

**That is the exact case, worded almost exactly as the gap analysis predicted it
would need to be.** Package count 13 → 14, and the increase is *entirely* this new
fault — confirmed by expanding `a05` (my wall's actual area) and finding it clean, and
by `diff -rq` showing my pre-edit copy (`PKG-T052-before/`) byte-identical to
`PKG-T049`. **`a07-probe-pinch` and `a09-probe-wording`'s deliberate faults are
unaffected**; I did not re-verify their exact counts individually this run but the
total arithmetic (13 baseline + 1 new = 14, wall contributes 0) leaves no room for a
second change.

**PT-1648 — package health at the point of choice — confirmed live**, not just read
about. Console Home now shows `Taris Undercity … 2 problems` in red directly on the
library tile, and *"4 packages installed · checked, 2 with problems"* under the grid.
TEST 050 filed this as a real gap (*"no surface before entering shows package
health"*); it is now closed on the exact surface named.

⚠ **`Taris Undercity` reads 2 problems, not the 1 I filed in TEST 047.** Consistent
with `areaHasNoWayIn` also catching its `a02-rakghoul-warren` (unreachable, filed in
TEST 047 as the one genuine problem in that package) — I did not open it to confirm
the second fault's wording, since neither of my three tasks touched it and it is not
a fixture I own.

## 5. Wording changed under me, noted and not chased

`"2 rules unchecked"` now reads `"2 rules about this character not checked"` — same
count, same underlying `record_validate.dart` mechanism from TEST 050, clearer
sentence. Not filed as a finding; it is Coder's own copy edit, observed in passing on
every screen this run.

---

## What I did not check

- Whether `PT-1646`/`1647`'s new `areaHasNoWayIn` has its own false-positive risk the
  way `areaHasNoWayOut` did — TEST 049's closet test does not have an inbound analogue
  in my bed. Worth a fixture; not built this run.
- `Taris Undercity`'s second fault's exact wording.
- Whether PT-1654's fix also changed anything about `Load Game`'s resume path
  specifically, as opposed to `Continue` — every resume this run went through
  `Continue`.
- Whether the header-staleness bug (still open, confirmed above) has a ticket of its
  own or is filed under something I've already named.

## State

- **`tester-probe` changed by one file, kept deliberately**: `areas/a05-probe-
  barrier.toml` gains a wall at (8,3) and a comment explaining the PT-1605 fallback
  test, in the same *"DO NOT remove without reading the report"* style as `a07`/`a08`/
  `a09`. Verified parseable; verified zero new Loom faults from it. Backups
  `PKG-T052-before/`, `PKG-T052-after/`.
- Saves **restored** from `SV-T042` — `diff -rq` clean. Contamination (the whole
  `resume-tester.sav` fixture, plus the accidental Grave Digger and Blade Tester
  touches, both confirmed byte-identical to baseline) snapshotted at
  `SV-T052-after/`.
- `endar-spire` + `base-rules`: **unchanged** — md5-identical to the T051 baseline.
- The NWN install was not read or written.
- My app and Loom killed by PID; Coder's Loom `517968` survived.
