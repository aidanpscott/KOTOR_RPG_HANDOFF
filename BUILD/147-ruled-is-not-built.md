# BUILD 147 — ruled is not built, and the check that stopped measuring

---

## 1 · ⚠⚠ THE ANSWER TO THE QUESTION ASKED: NO, IT WAS NOT WIRED

> *"Confirm Science and Survival are actually selectable/usable for a droid
> character — not just documented as such."*

**They were not.** `PT-1718` ruled them open to every droid; the chapter was
never edited, so:

    DROID-SKILLS-01 §2.1     did not mention them          (fixed at PT-1763)
    droid_skills.json        computed them `unruled`       ⚠ still, this slice
    droid_skills.toml        shipped them `unruled`        ⚠ still, this slice
    the Skills step          "withheld — unruled for droids"

**That line has been on screen over `Science · Survival` for every droid ever
built in this product**, while the ruling said otherwise. `PT-1763` fixed the
document; this carries it the rest of the way.

## 2 · ⚠⚠ THERE IS EXACTLY ONE GATE AND IT IS THE DOCUMENT — SO NOTHING HAD TO BE INVENTED

I looked for the hardcoded list the owner suspected. **There isn't one.**

    the screen          `if (g == null || g.offerable.contains(sk.name))`
    offerable           `available` minus `contested`
    available           computed from §2.1's universal table + §2.3's opens
    unruled             computed as *on the roster and nowhere in the chapter*

**And nothing in play gates it at all.** A play-time skill check reads
`record.skills[name]` — the ranks bought at chargen — and the only readers of
`DroidSkillRecord` in the whole tree are `records.dart`, `hub.dart`,
`skills_screen.dart` and `chargen_source.dart`. **Selectable at chargen IS
usable in play**; there is no second enforcement point to update.

So the repair is the one the shape of this project predicts: **re-extract, ship,
done.** The same chain `designations.toml` uses.

## 3 · ⚠⚠ AND `§2.4` WAS STALE IN EXACTLY THE WAY `PT-1763` WAS OPENED TO FIX

One table further down the same page:

    | Astromech | 9 universal + Pilot, Botany, Medicine, Sleight of Hand = 13 |

Still written from **nine**, in all four rows, plus the summary beneath it
(*"Twelve to fourteen against an organic's twenty-three"*). `PT-1763` checked
`SKILLS-01` and eight other documents for a stale count and found none —
**the stale one was inside `DROID-SKILLS-01` itself.**

**⚠ AND `PT-1405`'s LAG IS PRESERVED RATHER THAN QUIETLY CLOSED.** `§2.4` also
disagrees with `§2.3` about Athletics, by one skill, on the Assassin and Battle
bodies — ruled stale at `PT-1405` and *carried as found*. Updating the
arithmetic by two must not erase it, and it does not: the extract's agreement
pattern is **identical to what it was before the owner's edit.**

              before PT-1763   after this slice
    Astromech   13 = 13 ok      15 = 15 ok
    Assassin    14 ≠ 15 ⚠       16 ≠ 17 ⚠
    Battle      12 ≠ 13 ⚠       14 ≠ 15 ⚠
    Remote      12 = 12 ok      14 = 14 ok

Two staleness, two skills apart, both still on the record.

## 4 · ⚠⚠ AND A CHECK HAD STOPPED MEASURING

`extract_droid_skills.py` reconciles each section's own prose count against its
table. `§2.1` said *"Nine skills"* and the map was:

    WORDS = {'nine': 9, 'six': 6, 'eight': 8, 'four': 4, 'three': 3}

**Only the words the document happened to use.** `PT-1763` wrote *"Eleven
skills"*, the parse returned `None`, and the reconciliation compared `None`
against 11 — which prints as a mismatch and **reads like a document error
rather than like a dead instrument.** Extended through twenty.

> The fourth sighting of *ask whether the instrument is still measuring*. This
> one degraded loudly enough to notice; it was one word from silent.

## 5 · ⚠ WHAT MOVED IN THE SUITE, AND WHY IT IS NOT A WORKAROUND

Five existing cases were pinned to the old facts and now carry the new ones:
`unruled` is empty, the four per-body totals rose by two, and the Astromech
case **asserted `withheld — unruled for droids` was on screen** and now asserts
it is not. **The ruling changed the facts; the cases follow the facts.**

The acceptance is new and is the one the owner asked for: it opens the real
Skills step for an Assassin droid, **scrolls the list, and finds both names on
it.** Not *documented as selectable* — selectable.

---

## What ran

    Lodestar   659 tests   exit 0
    Loom       261 tests   exit 0
    app        531 tests   exit 0   (+1)
    gate.py                 SENDABLE, the same 2 advisory warnings

Mutation-checked: restoring the previously shipped `droid_skills.toml` kills
the new case.

⚠ `check_extracts` reports **five** stale comparisons, up from three. **None is
mine** — `droid_skills.json` is re-stamped and current; the five are
`EQUIPMENT-01`, `EVENT-KINDS-01` and `ITEMS-01`/`04`/`08`, the last two
arriving with `PT-1762`/`PT-1765` while this slice was in flight.

## Heads

    Lodestar        95bc648   (unchanged)
    Loom            5ed6185   (unchanged)
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   7654d6c
    MAIN_WORK       0030f06

⚠ The shelf's `base-rules/rules/droid_skills.toml` was regenerated and
replaced. The whole package was diffed against the installed one first: **that
file was the only difference.**
