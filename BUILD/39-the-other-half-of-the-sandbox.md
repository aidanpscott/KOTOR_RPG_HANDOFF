# 39 · The other half of the sandbox, and the `Tester` protocol

**591 tests across four suites, all green, and ⚠ the live data folder is
untouched by every one of them.** Verified by an mtime snapshot around a full
run of all four.

---

## 1 · ⚠⚠ `BUILD 38` fixed the app and I had not looked at Loom

**The finding was mine and the fix was half a fix.** `BUILD 38` made the app's
suite hermetic. **`Tester` runs all four**, and Loom's was writing into the
real `endar-spire` on every run — the trooper blueprint, the doctrine, the area
and the conversation.

**⚠ Four of Loom's seventeen test files. The other thirteen already used temp
directories**, so the convention was right and these were the outliers — the
"made by clicking" tests from `BUILD/24`, `31`, `33` and `35`, which author
into the bed because the bed is what they author.

### ⚠ And it matters more here than in the app

The app rewrote **a save**, with identical bytes. Loom rewrites **the fixture
every other suite loads.** `endar-spire` is the Builder's own output and the
app's dialogue, walk and wound tests all read it.

> **A Loom test that failed halfway could leave the bed wrong, and every app
> test would then be testing against it.**

**`BUILD/33` already found two Loom tests colliding over this one conversation
file**, and *"the failure looked like a layout bug for two runs."* **That was
one repo with one agent. Two agents running suites is the same hazard with more
hands**, which is why this stopped being tidiness.

### ⚠ This sandbox COPIES where the app's SYMLINKS, and that is the point

| | tests | so |
|---|---|---|
| app | **READ** the shelf | **symlink** — keeps the real-data coupling that caught `PT-1382`, `PT-1425`, `PT-1417` |
| Loom | **WRITE** packages | **copy** — a symlink would carry every write back to the shipped bed |

**A reader wants a link; a writer wants a copy.** The app's own `sandbox.dart`
predicted this case in its comment and it arrived one slice later.

**Control:** with the copy source pointed at a nonexistent path the four tests
do not pass. ⚠ **They fail at setup rather than on an assertion**, which is a
weaker signal than the app's control — stated rather than dressed up.

---

## 2 · `HANDOFF/TEST/` — the protocol

**⚠ `PT-1446` has a collision in it, and it is written down rather than worked
around.** It says `Tester` writes `HANDOFF/TEST/` **and nothing else**, and it
also says `Coder` files its requests there. Split one level down:
`requests/` is `Coder`'s, `reports/` is `Tester`'s, **neither edits the other's
ever.** A reply to a report is a new request. **Proposed, for the owner to fold
in or overrule.**

**⚠ And the shape follows one line of `PT-1446`:** *"`Tester`'s value is USING
the thing, not verifying it. A tester that only runs suites is a harness with
more overhead."*

> **So a request is a JOURNEY, not a suite. A request that says "run the app
> suite" is a defect in the request.**

Three of the eight required parts exist because omitting them has cost time:
**what `Coder` could not see from where it sits** — a widget test cannot tell
you two greens are a shade apart; **known scaffolding**, without which nine
placeholders come back as nine defects; and **wrong versus undecided**, because
a had-to-behave-somehow is the owner's and not `Coder`'s.

A report owes **scoped negatives** — five wrong-place negatives so far, twice
inside checks built to prevent them — **three buckets rather than one list**, a
repro for anything `Coder` must fix, and **what was tried that found nothing.**

**`requests/001`** covers `PT-1443`'s save defects and `PT-1445`'s ruling: six
falsifiable claims, and the three things the suite cannot judge.
