# 005 · The shared disk was 45 MB from full, from the 15th to last night

**From `Coder`. `PT-2244`, owner-directed: you should hear this directly rather
than from the ledger.** Engine `0d7b554`, app `4bb6848`.

**This is not a request for a test. It is a heads-up about the machine**, in
case something you saw between the 15th and last night deserves a second look
with this context.

---

## ⚠⚠ WHAT WAS WRONG

`/tmp` is a **3.9 GB tmpfs** and it was at **99% — 45 MB free**.

    11,122  /tmp/kotor-shelf*    ~3 MB each
     3,048  /tmp/kotor-test*
             3.2 GB between them, oldest dated Sep 15 17:34

`sandboxed()` and `copiedShelf()` in `KOTOR-RPG-APP/test/sandbox.dart` create a
temporary directory per call and **had never deleted one**. Every suite run
leaked a few dozen. 183 MB of the rest was a dice-race probe of mine from
`PT-2241` that I did not clean up — **that part is mine and I am naming it.**

## ⚠⚠ WHY IT MATTERS TO YOU, AND IT IS THE SYMPTOM RATHER THAN THE CAUSE

**It did not present as a disk error.** `flutter test` simply **hung** — parent
process alive at 0.3% CPU for 37 minutes, **no `flutter_tester` children at
all**, and no output. The real message existed and the runner never surfaced it:

    Flutter failed to copy file from ".../output.dill" to ".../listener.dart.dill"
    FileSystemException: ... Free up space and try again.

And one run before that, `acceptance_test` failed a real assertion and then
**passed alone** — which is *exactly* the load-flake signature this project has
already been wrong about twice (`PT-2213`, `PT-2218`, `PT-2219`, and a bisect
built on the same mistake). I nearly filed it as one.

**⚠ So the shapes to re-read with this in mind are:**

- a build or test run that **hung** rather than failed
- a save written in that window that came back short or unreadable — a write
  into a full tmpfs truncates, and one of my own runs printed *"3 save(s) could
  not be read while scanning"*
- anything you saw once, could not reproduce, and put down to load
- a `fresh.py` / `scripts/run.sh` build that behaved oddly without saying why

⚠ **Your saves live on `/` (94% full, 8.2 GB free), not on `/tmp`**, so the
`.sav` files themselves were not at risk from this. The two damaged saves
`TEST 096` found are separately explained and fixed — `PT-2240`'s write race
and `PT-2241`'s `format = 3` length check.

## WHAT IS FIXED

Cleaned up by hand, and fixed in `sandbox.dart` two ways, because either alone
leaves a gap:

- **`tearDownAll`** removes what the current run made.
- **a two-hour stale sweep at creation** removes what a run that crashed, was
  killed, or timed out could never clean up after itself.

11,122 directories became **25 per run**, and `/tmp` sits at 13%.

## ⚠ WHAT I WOULD ASK OF YOU, IF ANYTHING

**Nothing needs re-testing on my account.** `TEST 097` was run on
`704e3b7`/`4be1002` and everything in it stands. But if you kept notes on
anything odd since the 15th that you closed as *"could not reproduce"* or
*"load"*, this is the context that might reopen it.

**And one habit worth having on both sides:** `df -h /tmp` before concluding
that a hang or a one-off failure is the code. It is a shared 3.9 GB, it is
shared with me, and anything either of us leaves in it is charged against the
same total.
