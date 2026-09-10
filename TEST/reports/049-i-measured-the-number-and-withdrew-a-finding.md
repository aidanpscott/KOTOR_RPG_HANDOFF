# TEST 049 — I measured the number, the closet is safe, and I withdraw a finding

**Built against:** the **same two binaries as TEST 043–048.** App bundle
`kernel_blob.bin` built **16:11**, from `660134a` → Lodestar `9aa7382`. Loom bundle
built **16:39**, from `908a412`. **Neither rebuilt.** `47789fa` / `776e42e` /
Lodestar `e1a837c` remain untested by me.

**Instrument:** PID-scoped via `$!` + `pgrep -P`, every click computed from
`xdotool getwindowgeometry --shell`. Looms `568394`, and one more, plus app `569293`,
all killed by PID; Coder's `517968` survived.

⚠ **Nothing outside my own bed was written.** `endar-spire` + `base-rules` md5-summed
before and after — `diff` empty. `taris-undercity` untouched, still Sep 7. Saves
restored from `SV-T042`, `diff -rq` clean.

---

## 0. ⚠⚠ I WITHDRAW ONE OF TEST 048's THREE WORDING FINDINGS

TEST 048 claimed `blueprintMissing`'s sentence — *"It will be drawn and will not be
present"* — is false for a `hidden = true` placement, because *"it will not be drawn."*
**I inferred that from the file and did not look. It is wrong.**

Walked to `a09-probe-wording` and looked at `ghost.probe-wording.01`, which is
`hidden = true` with no blueprint:

- ⚠ **It IS drawn** — a marker reading **`N`** (for `no-such-creature`) sits on 2,2.
- ⚠ **The app says so itself**, in its own words, in the status band:

      ⚠ 1 drawn and not present — ghost.probe-wording.01 — no blueprint at
      "characters/no-such-creature"

- ⚠ **And it is not present**: I walked *onto* 2,2. No block, no bump, no reveal. The
  status bar read `a09-probe-wording · 2, 2`.

**Both halves of the sentence are true. The finding is withdrawn.** TEST 048's wording
list is **two, not three**: `landingNotStandable` and `areaHasNoWayOut` still stand,
and `areaFileMissing`/`areaUnreadable` sharing one sentence still stands as a separate
point.

### And `hidden` is not broken — I checked before implying it was

The obvious next wrong claim would have been *"`hidden` is ignored."* It is not.
`a04-probe-slit`'s `PT-1576` matrix, on the same build, same session:

    you notice probe-warden — 14 against 5        ← stealth 5, FOUND, and now drawn
    …one red marker on the whole 64-square slit, at 4,1

`probe-sentinel.probe-slit.03` at 6,1 (stealth 35) was **not drawn at all**. Bumped it:

    something was waiting there — probe-sentinel

⚠ **Both halves of `PT-1551` confirmed on a real placement**: not drawn, still holding
its square, found by contact. So the composition is:

| placement | drawn? | holds its square? |
|---|---|---|
| `hidden`, blueprint resolves — a04 | **no**, until found | **yes** — contact reveals it |
| `hidden`, blueprint **missing** — a09 | **yes**, as an `N` marker | **no** — I walked through it |

⚠ **`hidden` is honoured only for a placement that resolves.** A hidden placement with
a missing blueprint is drawn anyway — which is probably right (you want to see the
fault) and is worth naming rather than assuming.

---

## 1. The number I predicted, measured

TEST 048's whole weight rested on *"swap the creature and the count returns"*, which I
read off the tree instead of running. **Swapped and run.**

`a08-probe-orphan`'s `probe-warden` carried my long-standing dead blaster. Replaced it
with **`probe-herald`** — a new blueprint, clean equipment, and still carrying
`conversation = "dialogue/sentinel-challenge"`, so the room keeps its conversation.

| package state | problems |
|---|---|
| a01–a07 (before a08) | 11 |
| + a08 with `probe-warden` | **12** |
| + a09 | 14 |
| ⚠ **a08 swapped to `probe-herald`, + a10** | **13** |

**13, exactly as predicted**, and a08 expanded shows **no red row at all**:

    creatures       probe-herald.probe-orphan.02   3,3
                    probe-anvil.probe-orphan.03    5,2
    doorways        door.probe-orphan.01           7,5
    arrival points  from-nowhere                   0,0

⚠⚠ **A room declared in the manifest, holding an arrival, two creatures, a
conversation and a door out, that no player can ever enter, contributes ZERO
problems.** Measured, not read. The gap has its number now.

## 2. The closet is not flagged — the check is not too eager

`a10-probe-closet`: 4×4, reachable from a05, **one connection and it is the door you
came in by**, one creature. The false-positive question — because if this fires, every
closet, vault, shop and side-room anyone ever authors is flagged as a soft-lock.

    a10-probe-closet   set as entry
      creatures        probe-sentinel.probe-closet.02   2,1
      doorways         door.probe-closet.01             3,3
      arrival points   from-probe-barrier               0,0

⚠ **Zero faults. Every row in normal colour.** `areaHasNoWayOut` is
`if (!wayOut && couldBeWalkedInto)` and `wayOut` is set by **any** reachable
connection — one is enough, and the measurement agrees with the read.

⚠ **So the check is too QUIET, not too eager.** a03/a04 (no connections at all) fire
correctly; a10 (one door back) correctly does not; a08 (no way *in*) is the only shape
it cannot speak about. That is a clean three-way result and it puts the a08 gap in
proportion: **the vocabulary is right about everything it covers.**

---

## 3. What else only a clean package shows

Four more, on top of TEST 048's four (the `verify` control, the VERIFY dialog, the
package path in the status bar, and a tree with no paragraphs in it).

5. ⚠⚠ **The play screen has no warning band.** In `tester-probe`, every area with an
   unresolved placement prints a permanent line above the status bar for as long as you
   stand in it:

       ⚠ 3 drawn and not present — probe-sentinel.probe-room.01 — not a creature
       path, expected "characters/…" · probe-warden.probe-room.02 — … (a01)
       ⚠ 1 drawn and not present — ghost.probe-wording.01 — … (a09)

   `endar-spire`'s Command Deck prints **nothing** there. I have looked at that band
   in almost every screenshot in this thread and never noticed it was optional.

6. ⚠ **Console Home says nothing about package health.** `Tester Probe` (13 problems)
   and `Endar Spire` (0) render as identical library cards — name, summary, author,
   version. **The only place a fault surfaces in the app is that in-area band**, and
   the only place in Loom is the header count and the tree.

7. ⚠ **`2 rules unchecked` is NOT a health indicator, and it looks like one.** It reads
   identically in `endar-spire` and in `tester-probe`. I had half-assumed for several
   reports that it was telling me something about my bed. It is not.

8. **`15 saves` for `endar-spire` against `5` for `tester-probe`.** The fourteen
   format-1 saves have no `package` field, so `listFor` falls back to
   `replay(readSave(…)).package` and they resolve to `endar-spire`. Not a defect — it
   is `PT-1518`'s fallback working — but it means **the save count on a clean, old
   package is the one place the format-1 population is visible from inside the app.**

---

## What I did not check

- Loom `776e42e`, app `47789fa`, Lodestar `e1a837c`. Not in either bundle. Untested.
- **Whether a hidden placement with a missing blueprint can ever be revealed** — I
  walked through it rather than bumping an adjacent square, so I never triggered a
  contact attempt on it from outside.
- Whether `probe-herald`'s conversation actually *runs* — a08 is unreachable by design,
  so its conversation was never opened. `referenceMissing` resolving is all I measured.
- The other two hidden creatures in a04 (20,1 range-1, and 40,1 out of range). I
  confirmed the stealth-5 and stealth-35 pair only.
- `taris-undercity` was not re-opened.

## State

- **`tester-probe` now reports 13 problems, four of them mine on purpose**
  (a07's one, a09's two, plus a03/a04 which are genuine and filed). Changes this run:
  `a08-probe-orphan` swapped `probe-warden` → new `blueprints/characters/probe-herald.toml`;
  `a09-probe-wording` gained a door back and is now reachable; new
  `areas/a10-probe-closet.toml`; `a05-probe-barrier` gained two doors and two arrivals;
  `package.toml` gains a10. Every file parses. Every fixture carries a **DO NOT "FIX"
  IT** comment naming what it proves. Snapshots `PKG-T043/` … `PKG-T049/`.
- `endar-spire`, `base-rules`, `taris-undercity`: **untouched**, md5 and mtime verified.
- Saves **restored** from `SV-T042`; contamination at `SV-T049-after/`.
- The NWN install was not read or written.
