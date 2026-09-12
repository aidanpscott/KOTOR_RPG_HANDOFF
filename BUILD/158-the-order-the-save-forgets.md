# BUILD 158 — solo mode walks, and the order the save forgets

---

## 1 · ⚠⚠ `PT-1122` — SOLO MODE IS A VERB, NOT A MODE

> *"Solo Mode lives here now, as one verb aimed at your own companions
> ('wait here') rather than a separate mode with its own rules."*

So the observable is **a door**, not a flag. `_bringTheParty` brings every
party member the room does not already declare; *wait here* means **not
coming**, and that has to hold across rooms.

## 2 · ⚠ TWO KINDS, PROPOSED RATHER THAN SMUGGLED

`EVENT-KINDS-01` has no kind for a standing order. `ledger.dart`'s own header
says what to do about that, and it is the file's established practice:

> *"said rather than smuggled: proposed here, in `EVENT-KINDS-01`'s own shape
> (kind · subject · lifetime · payload)… **They are a reading and not a
> ruling.**"*

    party.waiting    subject · area · x · y         campaign
    party.following  subject: the companion's tag   campaign

**⚠⚠ WAITING CARRIES A PLACE AND FOLLOWING DOES NOT**, which is not an
asymmetry for its own sake: *wait here* names a HERE, and a companion left
behind has to be standing somewhere the next time that room is opened.
Following is the **absence** of an order and needs no square — they are
wherever you are.

**⚠ AN ORDER WITH NO PLACE IS DROPPED**, exactly as `partyIn` drops a join with
no `from` — the same file, six lines up. A companion who is not following and
is not anywhere would be **in the party, drawn by no board, and reachable by
nothing**: the log would say they are with you and no room would ever show
them. Skipping the row leaves them following, which is a state the player can
see and undo.

**⚠ AND LEAVING THE PARTY CLEARS IT**, or a rejoined companion comes back
holding a position **nobody remembers ordering**.

Both of those were watched to fail before being kept. The first mutation did
not even compile — `WaitingOrder`'s `int x, y` refused `Object?`, which is its
own guard and worth naming as one.

## 3 · ⚠⚠ THE ROW GAINS `holding`, NOT A SECOND MEANING FOR `waiting`

`SidebarEntry` already had `waiting`: `PT-1686`'s *arrived this round, acts the
next*. **Two meanings on one word in one record** is this corpus's own
recurring defect, and the second one is called what it is.

## 4 · ⚠ THE VERBS ARE THE CATALOGUE'S, AND TWO FILTERS SIT ON TOP

`_verbs` calls **`verbsFor(Aimed.companion)`** rather than keeping a list — a
catalogue that existed twice would drift the day it did. Then `§3a`'s own rule
that a verb is shown *"only when genuinely relevant"*, applied twice:

- **never both halves of one switch on one row.** Offering *wait here* to
  somebody already waiting is a button that does nothing, which is the fixed
  menu the ruling forbids.
- **none at all during a fight.** `PT-1123` is explicit that combat is closed
  *"which is exactly why `ACTION-ECONOMY-01`'s five budgets exist"* — an
  uncosted exploration verb on a turn would be a sixth by the back door.

**⚠⚠ TRADE / GIVE ITEM IS SHOWN AND REFUSES.** `verbsFor`'s own note is the
argument: a filter that silently never returned a verb *"would look like a
working filter"*. `Search`, `Track` and `Examine` are unreachable because the
area format has nowhere to put their targets; this one **has** a target kind —
what it lacks is `§2`'s character screen. So it is offered and answers
*"there is nowhere to trade from yet — a pack needs a screen"*, which is
`PT-1493`'s standing for anything that cannot be resolved.

## 5 · ⚠ `_bringTheParty` ASKS THE LOG

Somebody holding position does not follow — **except into the room they are
holding**, which is the same rule rather than an exception: the order names a
place, and they are standing in it whenever the player opens that room. The
recorded square is checked exactly as any other is — on the board, passable,
unoccupied — so an author who edits a room out from under a standing order
gets the beside-the-player fallback rather than a companion inside a bulkhead.

## 6 · ⚠⚠ THE ORDER DOES NOT SURVIVE A SAVE, AND THAT IS ASSERTED

**This is the finding of the slice.**

    _persist keeps only what campaignKinds names
    campaignKinds is every shelf row whose lifetime is `campaign`
    the shelf is generated from EVENT-KINDS-01
    party.waiting and party.following are not rows

So the standing order **works for the whole session and is dropped at the
save**. A player who saves with a companion holding position finds them
following. The ledger's own note promises the opposite: *"an order the save
forgot would be worse than no order."*

**⚠ CHECKED, NOT ASSUMED.** Diffed every `CharacterEventKind` constant against
the shelf's `event_kinds.toml`: **these two are the only undeclared kinds in
the build.** `party.joined` and `party.left` beside them are both declared at
`campaign`, so this is a gap in the document and not a file nothing can read.

`emitted_kinds_test` pins it, with an instrument check beside it, and is
written to **fail the day the debt is paid** — its reason line says to delete
it and add both to `emitted`.

**⚠⚠ AND THE SCREEN TEST DELIBERATELY DOES NOT READ THE PERSISTED STREAM**,
and says why. Handing the bed its own `campaignKinds` would have made the test
pass while the running app dropped the order at every save — **a check aimed at
the wrong subject**, which is the defect this corpus has named more often than
any other. The behaviour is asserted through what a player can see.

## 7 · ⚠ THE ACCEPTANCE IS A ROUND TRIP

`companion_test` walks the whole switch, in one test, on a real board:

    a01   sidebar names Zaalbar · tell them to wait · "will wait here"
    a02   Zaalbar is absent          ← a02 declares nobody, and the order held
    a01   Zaalbar is back · "holding position" · no "Wait here" offered
          tell them to follow · "is with you again"
    a02   Zaalbar is there           ← the switch goes both ways

The fixture gained a **return door**; every companion test before this walked
in one direction only, because a standing order is about what is true when you
come **back**.

**⚠ THE SIDEBAR IS THE INSTRUMENT.** `BUILD 141`'s test had to prove a
companion was on the board by **bumping into them**, because nothing outside a
fight named a creature. `PT-1804` built the thing that does.

## 8 · ⚠⚠ `extract_items.py` WRITES ONLY WHEN GIVEN A DESTINATION

Re-shipping for `PT-1822`/`1825`/`1826`, I ran both extractors bare.
`extract_equipment.py` writes unconditionally. **`extract_items.py` prints a
full, correct, reassuring report and writes nothing** — its write is behind
`if len(sys.argv) > 1`.

A run that looks exactly like a re-extract and is not. `check_extracts` caught
it — `items.json` still stale after an apparently successful run — and without
that gate the old rows would have shipped in silence.

⚠ Recorded, not fixed: `_paths.dest`'s own docstring already names this as
`PT-1470`'s deferred item, and counted the population — *"`argv[1]` is the file
I will OVERWRITE in seven and the file I will READ in six. Near-equal
populations, which is why no habit protects you."* **A third shape now: the
ones for which `argv[1]` is optional and its absence is silent.**

## 9 · THE RE-SHIP

Fifteen rows change on the shelf, all `×3` → `×2` — exactly `PT-1825`/`1826`'s
nine ion variants and six Bowcaster rows, plus `PT-1822`'s Blaster Carbine
threat `19–20` and the two ion multipliers.

`check_shelf` ✓ 25 files identical · `check_extracts` **stale 0** ·
`check_engine_pin` 4 compared, all level.

⚠ Rebased three times during the slice — the owner pushed `PT-1825` through
`1828` while it ran, and the first re-extract was built from a document two
rulings old. **Fetch, rebase, re-extract, re-verify, then push** is the loop
that caught it.

---

## Tests

    Lodestar   697 pass   (party_test +7)
    App        571 pass   (party_sidebar +7 · companion +1 · emitted_kinds +1)

Analyzer clean on both; the 13 remaining app infos are all pre-existing.
