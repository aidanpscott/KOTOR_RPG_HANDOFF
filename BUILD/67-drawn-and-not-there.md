# BUILD 67 — `PT-1493`: a creature drawn and not there, and three silences

**706 green** — Lodestar 310 · Lens 4 · Loom 122 · app 272.

---

## 1 · The path — one rule, both folders

`Loom` prepended the folder, so it wrote `blueprints/characters/probe-warden`
while the reader checks `startsWith('characters/')` **and prepends the folder
itself**. Three against one, as you had it.

`charactersIn` names the relative form and **`characterFolder` is derived from
it**, so the two cannot drift again. `PT-1452` settled it for items; it is one
rule now.

## 2 · The runtime silence

`combatantsIn` returned a list and continued three times in six lines. **A list
cannot carry a refusal**, so it returns `AreaContents` — what it placed, and
one sentence per row it could not — and the play screen prints them, because
`Lens` renders `area.contents` whatever they name and **this is the only place
that can say so.**

⚠ A `from` that is not a character is **not** reported. A door is not a fault.

## 3 · The structural silence

`PackageProblem` had nine members and not one about a blueprint's contents.
Two now:

    blueprintMissing   a [[contents]] row names a blueprint that is not on disk
    equipmentMissing   a blueprint's [equipment] names an item that is not

Both fire on **the exact string Loom wrote**, the correct form is clean, and
the fault names the **tag and the area** so an author can find the square.

⚠ The second is the same silence one level down: `PT-1452` made every link fail
out loud **at the seam**, and nothing looked **at rest**.

## 4 · The dialog nobody could reach

`NewDoctrineDialog` is wired, and `dialogs_reachable_test` guards every New
dialog against being built, tested and constructed nowhere.

### ⚠⚠ And `NewItemDialog` is not wired, which is a finding rather than an omission

It needs `baseTypes` from `base-rules/rules/equipment.toml` — and **`Loom` has
no TOML reader at all.** It writes TOML by hand and reads through `Lodestar`'s
typed openers, none of which opens a rules file.

⚠ **Its own test hardcodes three base types, which is how it passed while being
unreachable.** The reachability test names which assertion turns red the day
Loom can read a rules file.

⚠ So `PT-1480`'s aim stays **unanswered**, and now the reason is written down
rather than inferred.

## F4 · The ordering trap

A creature's `conversation` is set in `NewCreatureDialog` and **nowhere else** —
nothing outside that file writes the field — while the conversation editor
wants an existing owner. **Exactly one order works and nothing said so.**

The dialog says it now: *set it here or not at all, and the path need not exist
yet.* ⚠ **That turns a dead end into an order. It does not rescue
`probe-sentinel`** — the real fix is a creature editor that can change the
field after creation, which is a new surface rather than a line.

---

## ⚠ And one I did not touch

`RUNNING-ON-THIS-MACHINE` claims `endar-spire` is Loom's output, and the bed
carries the **correct** `characters/` form while Loom wrote the wrong one.
`Tester` flagged it and would not regenerate the fixture. **Neither would I** —
they cannot both be true, and which one moved is worth knowing before either is
overwritten.

## Still open

- ⚠ Loom cannot read a rules file, so `NewItemDialog` stays unreachable.
- ⚠ A creature's conversation cannot be changed after creation.
- ⚠ `endar-spire`'s provenance against `RUNNING-ON-THIS-MACHINE`.
- The effect columns; `PT-1484`; `PT-1485`; 45 annotation cells.
