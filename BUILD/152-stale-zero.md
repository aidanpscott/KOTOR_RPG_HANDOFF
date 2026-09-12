# BUILD 152 — the last stale extract, and it was never about the data

---

## 1 · ⚠⚠ `check_extracts` REACHES `stale 0` FOR THE FIRST TIME

`event_kinds.json` has been the one standing stale comparison, and `STATE`
recorded **why re-stamping was refused**:

> *"⚠ `check_extracts` stale 1 — and re-stamping would hide it. The rows are
> byte-identical, so the DATA is current. **The lag is in the code**:
> `PT-1435` says check A must compare against the union of what every
> projection folds, and `emitted_kinds_test` still uses `handledByReplay`."*

**That was right, and it made a check into a to-do marker.** A permanently red
check is one people learn to scroll past — which is the same reasoning
`PT-1608` used to keep `check_state_fresh` out of the blocking set. **So the
repair was to close the code lag and then re-stamp, rather than either alone.**

⚠ Verified before touching it: the rows re-extract **byte-identical**, and only
the `source` line numbers move.

## 2 · ⚠⚠ `replay` WAS THE ONLY PROJECTION WHEN THE CHECK WAS WRITTEN

> `PT-1435`: *"A permanent kind that NO PROJECTION folds is the bug, while
> `emitted_kinds_test` still uses `handledByReplay`. A real lag in the code…
> **the same class again: a check written when `replay` was the only
> projection, still assuming one.**"*

It is one of five now. **A kind the others fold is not missing merely because
`replay` ignores it** — `party.joined` is folded by `partyIn` and by nothing in
`replay`, so asking `handledByReplay` about it **gives the wrong answer with no
sign that the question was wrong.**

    projectPlayState   →  handledByPlayState
    remainsIn/carriedBy→  handledByRemains
    combatRoster       →  handledByRoster
    partyIn            →  handledByParty
    replay             →  handledByReplay   (already declared)
                          ─────────────────
                          foldedByAnyProjection

**⚠⚠ A HAND-KEPT SIXTH LIST IS WHAT THIS PREVENTS.** Each projection declares
what it folds **beside itself** — for the reason `handledByReplay`'s own
comment gives — and the union adds them up. The day a projection is added it
declares its set where it lives, and the union is correct **without being
edited**. That is the difference between a union and a list somebody has to
remember.

**⚠ ITS OWN FILE, because it depends on all of them.** `ledger.dart` is where
`replay` lives and must not import the other four to describe them; the union
is a fact **about** the projections rather than part of any one.

**⚠ `final` AND NOT `const`, AND THE OVERLAP IS THE REASON.** A `const` set
refuses duplicates, and two projections folding one kind is ordinary —
`character.died` by `projectPlayState` **and** `remainsIn`, `encounter.ended`
by `projectPlayState` **and** `combatRoster`.

## 3 · ⚠⚠ AND A UNION OF FIVE STALE LISTS IS WORSE THAN ONE

It looks more thorough. So a case **reads each projection's source**, cuts out
the declaration itself — the claim must not be its own evidence — and compares
what the code names against what the set declares. **Both directions**:

    declares LESS than it folds   → the union is short, and a permanent kind
                                    reads as unfolded while a projection has
                                    been folding it all along
    declares MORE than it folds   → the union is long, and the check it feeds
                                    passes for a kind nothing handles

Mutated both ways before keeping.

## 4 · ⚠ AND THE APP'S CHECK ASKS THE UNION NOW

`emitted_kinds_test` asks `foldedByAnyProjection`, plus an **instrument check**
— because the repair is otherwise invisible: *if the union were
`handledByReplay` under another name, the rule above would be unchanged and the
file would read as if it had been fixed.*

## 5 · ⚠⚠ AND THE RIFLES LANDED MID-SLICE — `PT-1783`, `PT-1786`, `PT-1788`

Four rulings arrived while this was in flight, then a fifth. Checked one by one
against the diff rather than assumed:

    Sniper Rifle          NEW base type   1d12 · 50 m · 19–20 · energy
    Marksman Rifle        1d12 → 1d10
    Marksman Rifle item   1d8/19–20 ×3 → 1d10/19–20 ×2
    Marksman Rifle        `Two-handed` and `may not be fired in the same
                          round it is moved with` — GONE
    Sniper Rifle item     a_w_snprrfl01, Tier 2, 800cr

**Nothing else moved in either extract.** A case now asserts all three rifles
carry `energy` and `19–20` **together**, which is `PT-1786`'s shape: *"same
shape, no exotic exceptions on any of them."*

**⚠ AND THE CHECKS CAUGHT THE FIFTH ONE THEMSELVES.** `PT-1788`'s catalogue row
landed one commit after its base type, while I was pushing: `check_extracts`
flagged `items.json` on the pull and `check_shelf` named `items.toml` before it
was copied. **Two slices after being built, neither needed to be remembered.**

## 6 · ⚠⚠ ONE THING RULED AND NOT IN THE DATA, NAMED RATHER THAN SKIPPED

**`PT-1782`'s perception-extension property reaches no shipped field.**
`EQUIPMENT-01`'s ranged table has five columns — Weapon, Damage, Type, Range,
Threat — and the property lives in the **prose note beneath it**, so
`equipment.toml` ships both rifles without it.

**Ruled and unbuilt rather than shipped wrong**: nothing in the app extends
perception from a weapon at all, and `canSee` takes no weapon. Building it is a
feature with a sight-side half, and adding a column is a document change.
**Named because prose a table cannot carry is exactly how `PT-1718` sat unbuilt
for months.**

---

## What ran

    Lodestar   675 tests   exit 0   (+7)
    Loom       263 tests   exit 0
    app        547 tests   exit 0   (+1)
    flutter build linux     built
    gate.py                 SENDABLE, the same 2 advisory warnings
    check_extracts          38 comparisons · stale 0   ⚠⚠ first time
    check_shelf             ✓ 25 rules files identical

    base types  37 → 38        items 1,423 → 1,424
    records  2,628 → 2,630     priced 1,410 → 1,411

## Heads

    Lodestar        20e0565
    Loom            c48e909   (unchanged)
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   24b903f
    MAIN_WORK       7328920
