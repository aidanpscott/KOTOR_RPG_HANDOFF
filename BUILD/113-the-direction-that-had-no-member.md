# BUILD 113 — the direction that had no member, and a slot holding two facts

`PT-1646` and `PT-1647`, both built, plus one thing named and measured.

---

## 1 · ⚠⚠ `PT-1646` — AN AREA NOTHING LEADS TO

`Tester` furnished `a08` completely — declared in the manifest, two creatures, a
conversation, a door out — and predicted zero problems. **One fault fired and it
was about a NAME** (`equipmentMissing`); every fact about POSITION stayed
silent. Swap that creature for one whose rifle is on disk and **the count
returns to normal for a room that can never be played.**

⚠ **THE SILENCE WAS CORRECT REASONING REACHING THE WRONG END.**
`package_validate.dart`'s own comment says an area nothing leads to *cannot be
walked into*, so `areaHasNoWayOut` would be **false** about it — which is why
`couldBeWalkedInto` gates it. **The reasoning stands.** What was missing is that
*being unable to walk in* is itself the fault.

`areaHasNoWayIn` is `areaHasNoWayOut`'s mirror and not its twin: that one is a
room you can enter and cannot leave; this is a room you can never enter, so
**nothing inside it can ever be reached** — its placements, its conversations
and its own exits included.

### Two skips, and both are the discipline this file already holds

⚠⚠ **SKIPPED WHOLE WHEN ANY DECLARED AREA FAILED TO OPEN.** `enterable` is built
from the areas that OPENED, so a room reached only from an unreadable one would
be reported unreachable **falsely** — the exact defect `targetAreaUnreadable`
exists to prevent one field over. The package is not silent while this is
skipped: `areaFileMissing` or `areaUnreadable` is already on the list, and that
is the repair to make first.

⚠⚠ **SKIPPED WHOLE WHEN NO `[entry]` IS DECLARED.** Without one **every area is
unreachable**, so this would fire once per area for a single cause —
`areaHasNoStandableSquare`'s own argument: *"three faults saying the same thing
in three vocabularies is how a person comes to think there are three
problems."* `entryUndeclared` is the fault.

### Verified on the real shelf, not only on fixtures

    taris-undercity   areaHasNoWayIn  a02-rakghoul-warren
    tester-probe      areaHasNoWayIn  a08-probe-orphan

Both are the cases the owner named. `endar-spire` stays at **zero faults**,
which is the control that matters — the new member does not go off on a package
that is right.

⚠ **AND A SECOND AREA MADE IN `Loom` IS UNREACHABLE UNTIL A DOOR IS PAINTED**,
so an author will see this fault during ordinary authoring. That is `PT-1379`
territory — *the Builder must not be able to create the fault its own validator
detects* — and it is **the same standing as `areaHasNoWayOut`**, which a new
area also trips until it is wired. Named rather than treated as new noise: the
fault is true while it is showing.

## 2 · ⚠⚠ `PT-1647` — THREE SENTENCES THAT DESCRIBED ANOTHER BOARD

* **`landingNotStandable`** asserted *"a door landing there puts a character
  inside it"* **when no door lands there at all.** It now says which, and the
  fault still fires on an unused arrival: `§4` lets a connection be added later
  and the trap is already built. `_position` sees one area, so which arrivals
  are landed on is computed from every connection in the package and passed in.
* **`blueprintMissing`** said *"it will be drawn and will not be present"* about
  a placement whose whole point is that it is **not drawn** — `hidden = true`.
* **`areaFileMissing` and `areaUnreadable`** shared one sentence where
  `connectionUnreachable`'s own comment sets the opposite standard: *"the
  sentence says which of the two it is rather than one word for both."* A
  missing file and a refused file are different repairs.

Checked against `Tester`'s own `a09-probe-wording` fixtures rather than only
against new ones.

## 3 · ⚠⚠ THE SLOT, SPLIT — AND IT IS TWO FIELDS, NOT TWO ROWS

> **The identity is dropped exactly when something is wrong**, which is when
> *"am I editing the right copy?"* is the question most worth answering.

⚠ **AND IT WAS NEVER ONLY `_verify`.** The strip held **one string carrying two
kinds of fact** — what package is open, and what just happened — and every
writer overwrote the whole thing. Setting the entry area, creating a blueprint,
saving a conversation: **eleven writers, and all eleven dropped the path.** One
channel, two meanings. **The repair is a second channel, not a careful writer.**

⚠ **`_verify` WAS ALSO REBUILDING THE OTHER HALF FROM ITS OWN OUTPUT** —
`_status.split(" — ").first` — **a string used as a record.** A second `—`
anywhere in a message would have taken more with it.

**Two fields, one row.** Not two rows: the strip is 12 units tall and the tree
already spends its height on wrapped explanations (§4) — a permanent second row
takes from the same budget to say something that fits beside what is there.

⚠ **AND THE HEAD IS WHAT ELLIPSES.** `PACKAGE-NAMING-01` makes the PATH the
identity, and the identifying half of a path is its **end** — two copies differ
in a parent directory, and a truncation that ate the folder name would answer
the question with the half that is the same in both.

⚠⚠ **I BUILT THAT WITH `TextDirection.rtl` FIRST AND TOOK IT OUT.** It is the
clever way to move an ellipsis to the front and it **reorders punctuation at the
ends of a left-to-right string** — a rendering trick that is right about the
ellipsis and wrong about the text. The trim is arithmetic now and can be
asserted.

### ⚠⚠ AND THE CASE FOUND A SECOND DEFECT: THE ROW OVERFLOWED

The package row overflowed by **17 pixels** the moment a package had faults.
`Expanded` already gave the NAME all the slack there was, so the overflow was
the **fixed tail**: `verify` is four letters and `3 problems` is ten, with
`properties` after it.

⚠ **NO EXISTING CASE SAW IT BECAUSE EVERY FIXTURE IN `verify_test` IS A CLEAN
PACKAGE**, where the tail says `verify` and fits. The tail shrinks now and the
name keeps its share — and `properties` is clickable, which this repo's own rule
covers: *anything you can click must be laid out where it can be seen.*

## 4 · ⚠ NAMED, AND MEASURED RATHER THAN ASSERTED

> **The more wrong a package is, the less of it you can see at once.**

**Measured**: at scale 2 in a 280-wide pane, each fault's wrapped explanation
costs **35 pixels**, and the rest of the tree is pushed down by that much per
fault.

| faults | the `conversations` root sits at |
|---|---|
| 0 | y = 282 |
| 1 | y = 317 |
| 3 | y = 387 |
| 6 | y = 492 |
| 12 | y = 702 |

**Twelve faults push the rest of the tree 420px down.** `tester-probe` has
fourteen. On a 720-tall window that is most of the pane spent on prose, **at
exactly the moment an author needs to see the shape of the package.**

### My answer, and it is a recommendation rather than a build

**The mark and a short form belong in the tree; the full sentence does not.**

⚠ `PT-1575`'s argument is that **a red row that does not say why is a mark you
then have to go and look up** — and that argument is about the reason being
AVAILABLE, not about it being inline. The tree's job is navigation: which rows
exist, and which are marked. **A wrapped paragraph inside a navigation structure
trades the structure for the detail, and it does so worst exactly when the
structure matters most.**

⚠ **AND THE MACHINERY ALREADY EXISTS.** The count sits on the package row and
`onVerify` opens the report — *"a dialog, which is Aurora's shape for Verify"*,
in this file's own words. **The tree is currently duplicating the dialog's
content inline.** One line per fault on its row, and the sentence in the panel
the row already points at, keeps both rulings.

⚠ **NOT BUILT: it is a `PT-1575` question and `PT-1575` is not mine to
reinterpret.** The measurement is here so the decision can be made on a number.
