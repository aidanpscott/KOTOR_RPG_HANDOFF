# BUILD 142 — the Ion Blaster, and a flake that stopped being one

---

## 1 · ⚠⚠ `PT-1740` — DAMAGE THAT ONLY LANDS ON ONE KIND OF TARGET

`TEST 065` found the Engineer's Ion Blaster equipping, opening, and **swinging
as a fist**: `PT-1452`'s reader takes `NdM` or a flat number, `1d4 + 1d10 vs
droid` is neither, and it refused the whole string — **correctly**, then fell
back to `unarmed` silently.

**⚠ THE PRECEDENT `PT-1740` CITES IS A RULES PRECEDENT, NOT A CODE ONE.**
Nothing in the tree implements Sneak Attack, so this is the **first conditional
damage in the product** — built in the shape the corpus already accepted rather
than one chosen at the keyboard, and the file says so.

**⚠ THE GRAMMAR IS STILL CLOSED.** A base term, then optionally **one**
`+ NdM vs <kind>`. `PT-1452`'s *"anything else is refused rather than guessed
at"* survives, widened by exactly what the data contains — **censused: ten
distinct damage strings in `equipment.toml` and this is the only one** that is
not `NdM` or flat. A second clause is **refused rather than dropped**, because
silently keeping the first is a weapon quietly weaker than its own datasheet.

**⚠ AND THE PARSER ALONE IS NOT THE FIX.** The bonus only lands if the **fight**
tells `strike` what the target is — a different seam, and one a unit test of the
parser cannot reach. That seam has its own case, and the mutation that severs it
fails only that case.

**⚠ `Fight.droids` BECAME `Fight.kinds`.** The melee gate asks *is this a droid*
and the Ion Blaster asks *what is this*, and **those are the same fact read
twice.** A second field beside the first is how two answers to one question
start.

## 2 · ⚠⚠ AND THE SHELF FLAKE STOPPED BEING A FLAKE

`BUILD 140` could only call the cause **evidence-fits**: three sightings, no
reproduction. `BUILD 141` got a fourth in a second file. This slice got the
confirmation neither could give — **the shelf grew two more packages and the
failure became deterministic.**

> Ten packages now. `Endar Spire` is **no longer built at all**, so five more
> files failed every run with the same sentence: *"Found 0 widgets with text
> `Endar Spire`."*

**That is the same defect the whole way down** — intermittent at eight, constant
at ten. Every test that **taps a package by name** now reads a **copied** shelf;
the many that merely read it still use `sandboxed()`, which is what that helper
is for and what its own doc argues for.

## 3 · ⚠ AND TWO TESTS WALK THE OWNER'S LIVE SAVE FOLDER

*"Damaged save: the contents could not be unpacked"* — and a re-scan a minute
later read **all 42**. `Tester` plays the app on this machine, so **a file
caught mid-write is a partial file, not a corrupt one.**

Skipped and counted rather than thrown, which is `save_listing`'s own
discipline: *"a candidate that cannot be read does not vanish and does not throw
— it is rejected with a reason."* The count is printed, so a genuinely corrupt
save stays visible.

**⚠ ONE OF THEM HAD THREE UNGUARDED PASSES OVER THE SAME FOLDER**, and I guarded
two before the third still threw. Three walks of a directory somebody else is
writing is three chances to catch a partial file, and fixing the first two
looked like a fix.

## 4 · ⚠⚠ AND I PUSHED A COMMIT WITH A FAILING TEST

`96f9d6d`. `flutter test | tail -1` — **`tail` exits 0 whatever the suite did**,
so the `&&` chain ran the commit on `tail`'s status.

The failure was one superseded case (`item_test`'s *"a compound damage string is
refused"*, asserting the behaviour the ruling replaces) and it was fixed four
minutes later in `ea486f7` — **but I did not know that when I pushed**, which is
the part worth recording. Every suite run in this slice since then reports
`${PIPESTATUS[0]}`.

**⚠ AND THAT IS WHAT CAUGHT THE REST.** Checking the real exit code is what
surfaced Loom's superseded case and all five shelf failures; the `tail -1` habit
would have shown me a green last line for a red suite.

## 5 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| the fight stops telling `strike` what the target is | the seam case |
| the bonus fires against everybody | 2 |
| the bonus does not multiply on a critical | 1 |

Plus the parser's own closed-grammar cases — four malformed strings and a
double clause, each refused with a sentence.

## 6 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 633 | **644** |
| `Loom` | 261 | **261** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 507 | **509** |
| | 1,411 | **1,424** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓.

## 7 · ⚠ Named, not built

- **Two superseded tests were rewritten rather than deleted** — `item_test`'s
  and `bed_weapons_test`'s — because each said *"the engine has no model for
  this"* and **saying so is why the gap did not look solved.** The wording
  survives above the new assertion.
- **Companions**: nothing recruits, nothing switches control, and `§10`'s
  enemy-side trigger is still undriven.
- **`PREGENS-01`'s two droid Defence figures** still await the owner — `15` and
  `16`, computed in `BUILD 140`, in a file `PT-1446` makes theirs.
