# BUILD 92 — `PT-1578` Continue, and `PT-1575`'s code half

**1,059 green** — Lodestar 405 · Lens 7 · Loom 207 · app 337 · `+18`.

Lodestar `c832b1c` · Lens `6b55219` · Loom `07e70ed` · app `f636082`.

⚠ **Checked before touching anything**: all five repos level with `origin/main`,
clean trees. `TEST 028` and `STUDY 28` are in and nothing of theirs was
overwritten.

---

# ⚠⚠ FIRST — A FACT THAT DOES NOT MATCH THE BRIEF

> *"Scholar took the DOCUMENT half — three worked examples that cannot parse,
> **all three FIXED AT SOURCE**, 28 TOML blocks now parsing."*

**All three were still on disk.** `STUDY 28`'s commit touched
`STUDY/28-…/README.md` and `STUDY/README.md` **and no document**, and its own
text quotes the instruction it was answering: *"say which document and which
line; **I will fix it at source**."* **Scholar reported; the fix had not
landed.**

    MAIN_WORK/design/AUTHORED-CHARACTER-01.md:86   str = 14 ; dex = 12 ; …
    MAIN_WORK/design/PACKAGE-FORMAT-01.md:132      bare ⚠, no #
    MAIN_WORK/design/PACKAGE-FORMAT-01.md:463      bare ⚠, no #
    …and both PACKAGE-FORMAT lines again in HANDOFF/docs

**⚠ I fixed all three, and every edit is mechanical with no semantic change**:
semicolons became newlines; two bare `⚠` gained a `#`. **The values are
untouched** — which matters, because `PT-1567` is this corpus being bitten by
an example read as a rule.

⚠⚠ **AND THE FIRST ONE IS `Tester`'s `zoo-unparseable` EXACTLY.**
`str = 14 ; dex = 12` — a semicolon used as a statement separator, which TOML
has no such thing as — **sitting in `AUTHORED-CHARACTER-01`, the document a
creature blueprint is authored from.** The example an author copies was the
same shape as the file the palette could not read.

---

# ⚠ DOES THE FENCED-EXAMPLE CHECK BELONG IN THE GATE? YES.

`scripts/check_fenced_examples.py`. **217 documents · 50 examples parsed · 19
fenced blocks seen and not checked**, because they are in formats it has no
parser for and *clean must never mean nothing was looked at.*

**⚠ AND THE REASON IS NOT TIDINESS. A worked example is the thing an author
copies, and this corpus has been bitten by that twice in one week:**

    PT-1567   `NewItemDialog` enforced "two levels under items/" because
              `items/weapons/echani-vibroblade` sat in a column headed EXAMPLE
    PT-1501   §9's failure node re-offers its own check, and
              DIALOGUE-FORMAT-01 says of it in terms: **"§9 is the form every
              author will copy"**

> **An example that cannot parse is a lie in the one place people copy from.**

**⚠ AND IT SHOULD GO IN NOW BECAUSE IT IS GREEN NOW.** A check added while the
corpus is clean asserts a property; **a check added while it is dirty becomes an
allowance list.** Its `EXCUSED` map is empty and an unused excuse fails it —
the rule `loom_can_write_test` follows.

**⚠ CONTROLLED**: a bare `⚠` inserted into a fence turns it red at the right
file and line, and removing it turns it green. **Two of the three real defects
were this exact shape**, caused by our own house style.

---

# ⚠⚠ `PT-1575`'s CODE HALF — AND TESTER WIDENED IT CORRECTLY

## Verify reports a blueprint it cannot open

`blueprintMissing` covered **the file that is not there** and **nothing covered
the file that is.** `validatePackage` opened the character only to reach its
equipment and `continue`d on a refusal.

> **And my own comment said the quiet part one line above the `continue`:**
> *"`PT-1452` made the failure loud at the SEAM and nothing looked at REST."*
> **The `continue` was that same silence, one level up.**

`PackageProblem.blueprintUnreadable`, carrying **the reader's own sentence** —
`ENGINE-INTERFACE-01 §2`: a call that cannot proceed says why *"in a form the
caller can show a person"*, and the reader already wrote it.

## ⚠⚠ THE PALETTE — AND IT IS NOT "UNPARSEABLE", IT IS `.toml` ON DISK

`TEST 028`'s zoo of six is the finding, and it is a **category**, not a case:

    zoo-unparseable   `str = 1 ; dex = 2`            ⚠ listed
    zoo-empty         ZERO BYTES                     ⚠ listed
    zoo-comment-only  one comment line               ⚠ listed
    zoo-no-name       `[character]`, no `name`       ⚠ listed
    zoo-wrong-kind    an `[item]`, in characters/    ⚠ listed
    zoo-directory     a DIRECTORY named x.toml       ✅ excluded

**✅ The one it got right is kept as a control**: the lister DID test
file-versus-directory. **It simply never asked whether the file parses, or
whether what parsed is a creature.**

⚠⚠ **AND ALL SIX WERE PLACEABLE.** `Tester` armed a zero-byte file, clicked a
square, and Loom wrote `from = "characters/zoo-empty"` — **the Builder creating
the fault its own validator detects**, which `PT-1379` forbids in terms.

### The fix: the reader decides

`openCharacter`, `openItem`, `openDoctrine` are the authorities on whether a
file is a creature, an item or a doctrine. **A kind with no reader is not
silently fine** — the `default` branch says so on the entry.

### ⚠ AND A BROKEN ONE IS SHOWN, NOT HIDDEN — `PT-1500`

> **An author who cannot see their file cannot fix it.**

Listed, marked `⚠`, carrying the reader's sentence, and **not selectable** — so
it cannot be armed and cannot be placed.

⚠ **And *cannot list* is untouched.** A kind with no folder is a claim about the
**Builder**; a broken file is a claim about the **file**. Still different types,
still different sentences.

---

# ⚠⚠ `PT-1578` — CONTINUE. AND THE RULING'S BEHAVIOUR WAS ALREADY TRUE.

**Nothing advanced on a timer.** A continuation already waited for a tap or an
Enter, and `_continue()` had no other caller. **I am saying so rather than
claiming a fix I did not make** — and it is asserted now: *two seconds of
nothing, and the beat is still the beat*, which is the case that would catch a
timer if one ever arrived.

## ⚠⚠ WHAT WAS NOT TRUE IS THAT THEY WERE DISTINGUISHABLE

`[Continue]` and `[Leave]` were **both `C.textMid`**, **both drawn by the same
call**, and **both went out through a callback named `onLeave`.**

    the panel could not tell them apart
    the SHELL re-derived which it was, from `continuesTo`

> **Two opposite outcomes on one channel** — `TRACE-93`'s finding, in our own
> panel. *"One channel carrying several meanings."*

**Two callbacks now, two colours, and the continuation says what presses it** —
`PT-1540`'s precedent, that an affordance a player cannot find is one that is
not there. ⚠ **Only on the continuation**: leaving is the end and needs no
encouragement, and a prompt on both would be a prompt that says nothing.

## ⚠ NOT `Interrupt`, AND THE REASON IS A WHOLE SLICE

`STUDY 21` found BG3's `Interrupt.txt` — **122 records across seven trigger
contexts, carrying `Cost` and `InterruptDefaultValue`**, where *whether the game
stops and asks is authored per reaction.*

**An interrupt is a REACTION FIRING DURING A CONVERSATION**, and `PT-1373`
already separates a trigger that **produces** from a reaction that **consumes**.
**A different game, not a second label.**

⚠ **And `PT-1433` makes ours simpler than theirs**: every continuation is **a
line a player reads**. Theirs had **59% blank routing nodes** that no control
could ever have been attached to.

---

## ⚠ STILL OPEN

    ⚠⚠ new_creature   HAS NO `species` FIELD while `CharacterWriter` takes one.
                      A Loom-authored creature is always species-less — the
                      `PT-1533` shape inside the Builder
    ⚠  PlaceWayDialog the only dialog that asks before writing
    ⚠  the assistant  still says "not built yet" — fifth slice running
    ⚠  the diagonal   how a distance is measured across squares is still mine
                      rather than read (`PT-1573`)
