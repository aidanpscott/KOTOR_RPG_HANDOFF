# 027 · A doubled slash is not refused — it is collapsed. And Verify skips the blueprint it cannot open

**From `Tester`. Unrequested number.** `PT-1512` followed; packages backed up
before anything was touched.

**Built and tested against:**

    Loom 4d8be62 · app d3c1dd5 · Lodestar 4501bd2* · Lens 6b55219

**⚠ CONTAMINATION.** The tree moved four times while I worked. `Loom` was
`cf4f5ad` when I began this morning, `4d8be62` when I built, and **`84f49ec` as
I write**; `KOTOR-RPG-APP` is now **`0fa6eec`** and `Lodestar` **`4501bd2`**.
**Everything below is against what I BUILT, not against HEAD.**

**⚠ Three of your six were already answered in `026` (`6ac5ab6`), an hour before
this brief arrived** — the `⚠ unknown kind` group, `sentinel-challenge`, and the
five budget rows. They are summarised in `§6` rather than re-tested.

---

# ⚠⚠ 1 · `items//weapons/x` IS NOT REFUSED. IT IS SILENTLY CORRECT

**You asked me to hand-edit one in and confirm it fails LOUDLY. It does not fail
at all, and that is worse.**

## The mechanism, proved in the shell before I claimed anything

    $ ls blueprints/items//weapons/vibroblade.toml
    -rw-rw-r-- 1 aidan aidan 47 ... vibroblade.toml        ⚠ RESOLVES
    $ ls blueprints/items///weapons/vibroblade.toml
    ⚠ so does a TRIPLE

**POSIX collapses runs of `/`. `a//b` and `a/b` are the same path.**

## And the code takes the path straight to the filesystem

`Lodestar/lib/src/package_validate.dart:192` —

    final item = File('${package.path}$sep$blueprintFolder$sep'
        '${e.value.replaceAll('/', sep)}.toml');
    if (!item.existsSync()) { ... equipmentMissing ... }

**`existsSync()` returns true, so no fault is raised, because from the
filesystem's point of view there is nothing wrong.**

## Confirmed end to end, in play

A creature blueprint equipping **`items//weapons/vibroblade`**, placed at `5,4`:

- **Loom's palette lists it.**
- **Loom's `Verify` reports 5 problems and this is not one.**
- **The app draws it PRESENT** — a filled token, not a placeholder — and the
  alert bar stays at *"2 drawn and not present"*.
- **It resolves to the real vibroblade.**

> **⚠⚠ SO A MALFORMED PATH PRODUCES A WORKING PACKAGE. Nothing will ever surface
> it — until the package is read by something that does not normalise
> separators: an archive, a URL, a case-folding filesystem, or `PT-1334`'s
> exchange.**

**⚠ And `PACKAGE-NAMING-01`'s refusals do not cover it.**
`package_naming.dart:98` refuses an **empty segment** — but that check is
`id.contains('--')`, a doubled **hyphen inside one id**, not a doubled
**separator between two**. **`checkId` takes an id, and nothing takes a path.**

**⚠ Shape it wants:** the check belongs where a path is turned into a file, and
the honest test is `value.split('/').any((s) => s.isEmpty)` — **before**
`File()` is constructed, because after that the OS has already forgiven it.

---

# ⚠⚠ 2 · VERIFY SKIPS THE BLUEPRINT IT CANNOT OPEN — and I proved it by accident

`package_validate.dart:189` —

    final opened = await openCharacter(f.path);
    if (opened is! OpenedCharacterResult) continue;

**A blueprint that fails to open is skipped, silently, and nothing is reported
about it.**

## How I found it, which is the useful part

**I wrote my fixture's abilities on one line, copying the format document:**

    str = 10 ; dex = 10 ; con = 10 ; int = 10 ; wis = 10 ; cha = 10

**That is not valid TOML.** `tomllib` refuses it —
*"Expected newline or end of document after a statement"*. **My blueprint never
parsed.** And with it unparseable and placed in an area:

| surface | what it said |
|---|---|
| Loom's **palette** | **listed `probe-doubled`** as if it were fine |
| Loom's **`Verify`** | **5 problems, and this was not one** |
| the **app** | **"⚠ 3 drawn and not present — … probe-doubled.p…"** |

> **⚠ The Builder listed it, the Builder's validator said nothing about it, and
> the player's client is the only surface that noticed.**

**The comment directly above the `continue` says the quiet part:** *"`PT-1452`
made the failure loud at the SEAM and nothing looked at REST."* **The `continue`
is the same silence one level up** — it inspects what a blueprint *carries* and
skips the blueprint that could not be *read*.

**⚠ Shape it wants:** a thirteenth `PackageProblem` — *a blueprint is on disk and
cannot be opened* — reported with the reader's own refusal. **It is the one file
an author most needs told about, and it is the one that gets nothing.**

---

# ⚠⚠ 3 · `AUTHORED-CHARACTER-01 §2a`'s WORKED EXAMPLE IS NOT PARSEABLE TOML

**Line 86 of `MAIN_WORK/design/AUTHORED-CHARACTER-01.md`:**

    str = 14 ; dex = 12 ; con = 13 ; int = 10 ; wis = 10 ; cha = 8

**TOML has no statement separator. `;` is not a comment and not a delimiter.**
Every shipped blueprint in `tester-probe` and `endar-spire` writes the six on
**separate lines**, which is correct — **only the document is wrong.**

> **⚠ I copied the document, and my blueprint silently became a placeholder.
> The next author will do the same.**

**⚠ This is `DIALOGUE-FORMAT-01`'s own confessed failure in a second document.**
That file records at `§12`: *"`§9`'s worked example shipped without a `start` and
nothing caught it until the validator existed… a format document that omits a
required field is the failure the validator was built for and it found it on its
own example."*

**Here the example is not merely incomplete — it does not parse.** And **nothing
validates the documents**, so it will keep being true.

---

# ⚠ 4 · DOORS AND WAYPOINTS — the "cannot list" line is NOT gone, and for those two kinds it is FALSE

**You asked whether it is gone. No.** Both now carry the *correct* sentence
**and** the old one underneath it:

    ▼ doors
        painted as `doorway` above — §4a and §4·0 make it a way, not a blueprint
        ⚠ cannot list — no folder is specified for this kind yet, so this list
          cannot be read — it is not a count

    ▼ waypoints
        painted as `arrival point` above — §4a and §4·0 make it a way, not a blueprint
        ⚠ cannot list — no folder is specified for this kind yet, …

**⚠⚠ AND THE WORDING MAKES IT WORSE THAN REDUNDANT.**

For `encounters`, `placeables`, `sounds`, `stores` and `triggers` the line is
**true** — those kinds have no format **yet**, and those five also carry a
genuinely good second sentence:

> *"a placement names a blueprint by path — `§3` — and this kind has no format,
> so there is nothing a placement could name. **Painting one would write a
> reference nothing can resolve.**"*

For **`doors` and `waypoints` it is false.** `§4a` and `§4·0` make them a **way**,
permanently. **There will never be a folder**, and *"no folder is specified for
this kind **yet**"* promises one.

> **The same sentence is shown for ten kinds and is a lie for two of them.**

**⚠ This is `PT-1553`'s risk in another costume — the right sentence added and
the wrong one left underneath.** The five inert kinds got a bespoke second
sentence; the two `ways` kinds got a bespoke second sentence; **only the generic
first line was never removed from the two that no longer need it.**

---

# ✅ 5 · NESTING AT DEPTH — the pane agrees, and folders sort before files

**Made `blueprints/items/weapons/heavy/repeater/probe-cannon.toml` — three
folders past `items/` — and the palette nests it exactly:**

    ▼ items                    +
      ▼ weapons
        ▼ heavy
          ▼ repeater
              probe-cannon
        blaster-rifle
        vibroblade

**`PT-1567`'s unbounded nesting holds in the pane**, and **folders sort before
files** at each level, which is the readable order.

**⚠ NOT TESTED, and it is half your question:** *"see whether the pane, the
dialog and the reader agree."* **I checked the PANE only.** I did not open the
New Item dialog to see whether it can *create* at that depth, and I did not
place or equip `items/weapons/heavy/repeater/probe-cannon` to see whether the
**reader** resolves it. **Two of the three surfaces are untested.**

---

# 6 · The three from `026`, unchanged

**✅ A `from` nothing declares gets its own group in alert.** Confirmed on
screen: `⚠ unknown kind` holds all three, drawn in alert, **selectable**.

> **⚠ And the finding beside it still stands: LOOM NAMES THREE, THE APP NAMES
> TWO.** Loom's `Verify` reports `mystery.probe-room.11` — `from =
> "widgets/probe-thing"` — and the app's alert bar does not. Re-checked twice
> today, including with a third not-present placement in the room, and the app
> still drops the one whose first segment it cannot classify at all.

**✅ `sentinel-challenge` closed.** My first fix was wrong and Loom's status bar
said why — **`§9` puts the check on the OUTBOUND link**, which is `PT-1326`'s
cause. It validates and writes.

**✅ Five budget rows are unreachable, and not because of the class.**
`bonusGranted = true` occurs **only in tests** across every `lib/` in all four
repos. Three rows in every fight.

---

# 7 · Two smaller ones from today

**⚠ The alert bar truncates before the third entry's reason.** With three
not-present placements it read:

> *"⚠ 3 drawn and not present — probe-sentinel.probe-room.01 — not a creature
> path, expected "characters/…" · probe-warden.probe-room.02 — not a creature
> path, expected "characters/…" · **probe-doubled.p…**"*

**Two entries fit with their reasons. The third is named and its reason is
lost** — and it was the only one whose reason I did not already know.

**⚠ `tag_seq` reached 14 and every placement I made took the next number.**
`PT-1377` continues to hold across a session that placed and deleted four times.

---

# 8 · Scoped negatives

- **The New Item dialog at depth** — not opened. `§5`.
- **The reader resolving a deep path** — not tested. `§5`.
- **Whether the doubled slash is refused on a case-folding or archive-backed
  loader** — untestable here; the finding is that POSIX hides it.
- **Whether `84f49ec` / `0fa6eec` / `4501bd2` change any of this** — they landed
  while I wrote and I have not built them.
- **The conversation wizard (`PT-1559`)** — still never opened.
- **Slice two's Standard/Custom split** — the palette shows one side only for
  `tester-probe`, which supplies no standard content; **I did not open a package
  that has both.**
- **Painting tiles in Loom** — still not done.

---

# 9 · What I left behind

**`tester-probe` carries two new fixtures, both deliberate:**

    blueprints/items/weapons/heavy/repeater/probe-cannon.toml   ⚠ depth fixture
    blueprints/characters/probe-doubled.toml                    ⚠ carries
        weapon_r_1 = "items//weapons/vibroblade"                   the doubled
                                                                   separator
    a01-probe-room  tag_seq 14, 9 placements
        probe-doubled.probe-room.14  at 5,4                     ⚠ places it

**The doubled separator is left in on purpose** — it documents `§1` and it costs
nothing, because it resolves. **Remove it the day something refuses it.**

**Backups in the session scratchpad: `BK3/` (this morning) and `BK4/` (before
today's fixtures).**
