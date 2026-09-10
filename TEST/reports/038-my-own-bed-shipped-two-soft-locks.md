# 038 · My own bed shipped two soft-locks, and a check that did not exist this morning found them

**From `Tester`. Unrequested number.** `PT-1512` followed: `BK14/` and
`SV-T037/` before anything was opened.

**⚠⚠ BUILT AND MEASURED AGAINST — pins read from the commits I BUILT:**

    app  fb666f0  → Lodestar bef95c7      built 14:12
    Loom 813d58d  → Lodestar bef95c7      built 14:00
    Lens 5534554

**⚠ Both pins verified in `~/.pub-cache/git/Lodestar-bef95c7…/` AND in the
binaries** — `grep -c "can never leave"` → 2 in Loom's blob, `"not standable"` →
2 and `"at nowhere in it"` → 1 in the app's. **The checks are in what I ran.**

**⚠ The tree moved three times while I worked.** As I write: app `d11b724` ·
`Lodestar 5031aed` · `Loom 7d04511` · `MAIN_WORK 9b9cca6` · `HANDOFF ad37865`.
**Nothing below is against those.**

**⚠⚠ AND `base-rules` MOVED TOO, WHICH IS A FOURTH ARTIFACT AND A NEW ONE.**
`event_kinds.toml` was regenerated at **14:11**, five minutes after my backup —
`encounter.began` campaign → transient, `PT-1612`. **It is Coder's, not mine, and
a blind `PT-1512` restore would have reverted it.** The diff is what caught it;
**the shelf is shared and I had been treating it as mine to put back.**

---

# ⚠⚠ 1 · THE CHECK IS A FIND, NOT A FALSE POSITIVE. I CONFIRMED IT THREE WAYS

**`Verify` went 9 → 11:**

    a03-probe-yard
    "a03-probe-yard" declares no connections, so a character who walks into it
    from another area can never leave.

    a04-probe-slit
    "a04-probe-slit" declares no connections, so a character who walks into it
    from another area can never leave.

## It is true, and I did not need the app to know it

    a01-probe-room   connections=3   → a02, a03, a04
    a02-probe-hall   connections=1   → a01        ⚠ the one I PAINTED last session
    a03-probe-yard   connections=0   ⚠⚠
    a04-probe-slit   connections=0   ⚠⚠

## And true on a board, twice over

**✅ The whole of `a03` in one frame carries not a single orange doorway** —
every connection in `a01` and `a02` draws as an orange double-bar, and `a03`'s
only marker is the **teal arrival** `from-probe-room`, which is a landing.

**✅ And I walked twelve squares to stand on it:**

    a03-probe-yard · 0, 0        ⚠ standing ON the arrival, still in a03

**Nothing travels. `_step` only travels on `a.connections`, and there are none.**

## ⚠⚠ AND I HAD ALREADY WALKED INTO THIS AND NOT NAMED IT

**`034` says, in my own words:** *"a03 is a dead end — no connection back — and
all my saves are in a03/a04."* **I wrote that as a ROUTING NOTE while working
around it, and painted a door in `a02` rather than filing the category.**
`026` had flagged the hazard and could not construct one; **I was standing in
two of them.**

> **⚠ A check found in one slice what I had lived with for four. That is the
> right way round, and it is worth saying plainly.**

## ⚠ Two small things about the fault

**✅ It names the area and does NOT name a missing door — correctly.** There is
no door to name; the area declares zero. **The other branch** — *"has N
connections and none of them can be walked to"* — is where naming would matter,
and I did not exercise it.

**⚠ And the module tree does not flag it.** `a03` and `a04` render in plain teal
like any other area; the only trace is a **missing `doorways` group**, which
looks exactly like an empty collapsed one. **The tree already draws alert
markers — `⚠ unknown kind` in red — so it has the vocabulary and does not use
it here.** The fault lives in `Verify`; the author is working in the tree.

---

# ✅ 2 · `PT-1605` — CONFIRMED ON THE SCREEN, BOTH FORMS, VERBATIM

**Your rule, applied to your own fix: I read it on the screen and not in the
commit.**

**Walled only the arrival square:**

    Probe Hall — arrived at from-probe-room · the arrival "from-probe-room"
    is not standable, so you are at 1,0

**✅ It names the arrival, says WHY, and says WHERE YOU ACTUALLY ARE — and keeps
the original arrival clause, so both facts survive.** *"Silently rescuing a
character was only half better than silently burying one"* is answered.

**Then walled every square of the area:**

    Probe Hall — arrived at from-probe-room · the arrival "from-probe-room"
    is not standable, so you are at nowhere in it

**✅ It ARRIVES. ✅ It KEEPS DRAWING** — board, arrival marker, doorway,
`probe-feeble` all render. **✅ It took five keypresses (`←→↑↓ m`) without
throwing** — three processes still alive, nothing in the log.

**⚠ One residual, small and stated rather than filed: the state is announced
ONCE, on arrival, and the arrows stay silent afterwards.** The standing sentence
is what carries it, which works because `_said` persists — **but a player who
presses an arrow a minute later gets no answer to the arrow.**

---

# ✅ 3 · `PT-1607` — THREE OF THE FOUR, ON THE BOARD, AND THE FILE IS UNCHANGED

**`sentinel-challenge.toml` still says `owner = "probe-sentinel.probe-room.04"`.
I walked into three different placements of `probe-warden` and the panel named
each one:**

| walked into | panel header |
|---|---|
| `a04-probe-slit` `4,1` | ✅ **`PROBE-WARDEN.PROBE-SLIT.02`** |
| `a04-probe-slit` `20,1` | ✅ **`PROBE-WARDEN.PROBE-SLIT.05`** |
| `a01-probe-room` `4,1` | ✅ **`PROBE-WARDEN.PROBE-ROOM.03`** ⚠ *the one `035` found it on* |

> **⚠⚠ THE FIX IS IN THE DERIVATION, NOT THE DATA — the `owner` that renamed the
> speaker is still sitting in the file and no longer reaches the screen.**

**⚠ The fourth, `probe-warden.probe-room.10`, I did not reach** — same blueprint,
same area as `.03`. Three of four is what I measured.

---

# ✅ 4 · `PT-1603` — A CONVERSATION IS RECORDED, AND THE LIFETIME FILTER DISCRIMINATES

**After one reply, in the save:**

    {"kind":"dialogue.choice-made","step":"play",
     "payload":{"conversation":"sentinel-challenge","reply":"back-away"}}

    dialogue.choice-made   1     ✅ campaign — persists
    dialogue.node-reached  0     ✅ session  — correctly does NOT

**`035 §2` and `036 §2` are closed, and the filter is not a blanket: it keeps the
campaign one and drops the session one in the same conversation.**

**✅ And `encounter.began` is now `transient` in BOTH the extract and the shipped
rules**, with its own history in the note — *"transient — until the encounter
ends · PT-1612 — was campaign"*. **So `037`'s "94 ended, 0 begun" was a
mis-declared lifetime, and the ruling corrected the declaration rather than the
plumbing.** The data and the code agree.

---

# ⚠⚠ 5 · AND `character.downed` IS STILL ZERO — THE FILTER IS NOT THE STORY, AND I CAN SAY WHAT IS

**You said to count again and that if it still showed zero the filter would not
be the whole story. It shows zero. ⚠ Across ALL TWENTY SAVES:**

    character.downed     0
    character.died      16
    character.revived   92
    dialogue.choice-made 2      ⚠ was 0 before this build

> **⚠⚠ NINETY-TWO REVIVALS AND NOT ONE DOWN, ON A BUILD WHERE THE FILTER
> DEMONSTRABLY WORKS.**

## The reason, and it is not plumbing — there is nothing to plumb

    CharacterEventKind.died      play_screen.dart:1928  ⚠ WRITES an event
                                 play_screen.dart:2128  reads it
                                 play_state.dart:264    folds it
                                 pools.dart:206         names it in ledgerKinds
    CharacterEventKind.revived   play_screen.dart:1909  ⚠ WRITES an event
                                 play_state.dart:237    folds it
                                 pools.dart:210         names it in ledgerKinds
    CharacterEventKind.downed    pools.dart:208         ⚠⚠ AND NOWHERE ELSE

**`died` and `revived` each have their own writer in the play screen. `downed`
has none.**

**⚠ And `ledgerKinds` is not a writer.** It is a `List<String>`, and it reaches
exactly two consumers: an accumulator at `fight.dart:100`, and
**`play_screen.dart:1677`, where it is appended to a display string** —
`'${r.line} · ${r.ledgerKinds.first}'`.

> **⚠⚠ SO `character.downed` IS A WORD THE STRIKE LINE CAN PRINT. IT IS NOT AN
> EVENT ANYWHERE. It was never lost — it was never written**, and the shipped
> rules declare it `campaign` as though it were.

**⚠ Shape it wants:** either a writer beside `revived`'s at `play_screen:1909` —
they are the same moment, one going down and one coming back — or the
declaration goes the way `encounter.began` just went. **What it must not stay is
a campaign kind with a fold, a lifetime, and no event.**

---

# ⚠ 6 · `STATE.md` — THE HEADS WERE RIGHT, THE TESTS WERE FOUR OUT, AND ITS OWN CHECK BEAT ME TO IT

**You asked whether it describes the product I am actually testing. ⚠ At build
time it did, exactly:**

| STATE.md said | I built |
|---|---|
| `Lodestar bef95c7` | ✅ `bef95c7` |
| `Lens 5534554` | ✅ `5534554` |
| `Loom 813d58d` | ✅ `813d58d` |
| `KOTOR-RPG-APP fb666f0` | ✅ `fb666f0` |

## ⚠ The test line was not right, and I measured it

    STATE.md (BUILD 103):  Lodestar 456 · Lens 7 · Loom 217 · app 367 — 1,047
    measured:              Lodestar 452 · Lens 7 · Loom 217 · app 367 — 1,043

**Lodestar re-run alone, head bracketed before and after on a clean tree:**
`before: 5031aed dirty=0` → `+452: All tests passed!` → `after: 5031aed
dirty=0`. **And 452 at `bef95c7` too. Four out, all in the one repo the owner
cannot see.**

> **⚠⚠ AND ITS OWN CHECK CAUGHT IT BEFORE I COULD FILE IT.** `HANDOFF ad37865`
> — *"STATE.md at `BUILD 104`'s heads — caught by its own new check on the next
> slice"* — and the line now reads **`1,043`**, which is my number.
> **`check_state_fresh.py` works, and this is an independent confirmation of the
> figure it landed on rather than a defect report.**

## ✅ AND THE HERMETIC CLAIM IS TRUE — I CHECKED IT, BECAUSE IT PROTECTS MY BED

**`find ~/.local/share/kotor-rpg -printf '%T@ %p\n' | sort`, 115 files, before
and after a full run of all four suites:**

    diff pre-test.txt post-test.txt   →   NO DIFFERENCE

**✅ Not one file touched.** *"All four suites are hermetic"* is measured, not
asserted.

**⚠ One thing STATE.md cannot promise: it tracks the LAST PUSH, and the tree
moved three times inside this one session.** Its heads were right when I built
and wrong ninety minutes later. **That is its contract working, not failing —
but it is why my reports name a build and not a file.**

---

# 7 · Scoped negatives

- **⚠ `areaHasNoWayOut`'s second branch** — *"has N connections and none can be
  walked to"* — **never exercised.** I only produced the zero-connection form.
- **⚠ `areaHasNoStandableSquare`, `landingNotStandable`, `connectionUnreachable`**
  are in the enum and **I did not confirm any of them fires** — my walled area
  was reverted before I re-verified, and the 11 problems I read were with `a02`
  intact.
- **⚠ `PT-1607`'s fourth placement** — `probe-warden.probe-room.10`, not reached.
- **⚠ The `esc`-from-nowhere path** — I left the no-standable area with `esc` and
  **did not check what it wrote**, unlike `037` where I did.
- **⚠ `character.downed` in a fight that reaches `VitalityState.down` rather than
  `dead`** — I did not construct one. **The zero is explained by the missing
  writer; whether the state is ever entered is a separate question I did not
  settle.**
- **`m` in the nowhere state** — pressed, app survived; **I did not read whether
  the map line rendered.**
- **Loom's tree** — `§1`'s "no marker" is a read of the tree as drawn; **I did
  not check whether Loom has an area-level marker it uses elsewhere.**
- **`doors`/`waypoints` still carry both lines** on `813d58d` — sixth sighting,
  noted in passing, not chased.

## What I left behind — nothing of mine

    diff -rq packages BK14/  →  ONE difference, and it is CODER'S:
        base-rules/rules/event_kinds.toml — regenerated 14:11, PT-1612
    all 20 saves             →  byte-identical to SV-T037/

**`a02-probe-hall` was walled twice and restored byte-identical both times.**
**`base-rules` I left alone deliberately** — see the header.

**Backups: `BK3/`–`BK14/`, `SV-T031/`–`SV-T037/`.**
