# BUILD 54 — `PT-1473` / `PT-1474`: eleven of eleven, the `targets` column, and three defects in my own convention

---

## 1 — `PT-1473`: the producer is unblocked

`EQUIPMENT-01` now states both. Re-extracted: **34 base types → 36**, and both
resolve through `weaponFromBase` — Marksman Rifle `1d12` critOn 19, Training
Lightsaber `1d8` critOn 19. The `19–20 / ×2` threat spelling in the Lightsabers
table parses like the plainer one.

Both were **refused** by `author_bed_weapons` until they were ruled, because a
base type is a number and inventing one is inventing a rule. **Eleven of eleven
weapons now resolve.** `noBaseType` is kept and empty — an empty map says
nothing is unaccounted for; a deleted one says nothing at all.

## 2 — `PT-1474`: `targets` is a column

**17 of 104 powers** carried `⚠ targets: sentient · beast — PT-459` fused into
the Effects prose, and the Powers screen printed it verbatim to the first
player who ever reached that step. Seven distinct target sets.

**The other 87 are `null`, and that is the document being silent** — not a
claim that the power hits everything. `ONLY` is dropped from the values and
recorded: a targets list is already exhaustive, so it is emphasis.

⚠ **The editorial prose in `effect` is NOT touched, deliberately.** Sentences
like *"Renamed from Beast Control, and the DC corrected: our entry dropped the
two ability modifiers"* are asides a player should not read — and **nothing
mechanical distinguishes them from the `⚠` rulings beside them that a player
MUST read.** `⚠ ALLIES AND BYSTANDERS ARE INCLUDED` is marked identically.
`PT-1467` ruled the test is not *"does it look like prose"*, so this is
reported rather than guessed at.

---

## 3 — Your question: were species in the four?

**No, and it is not the nested `fields`.** The check walks into
`[species.fields]` correctly — that is where it found and fixed eight cells at
`PT-1467`.

⚠⚠ **The mark was too narrow. It matched `PT-\d+` and `TRACE-\d+` and nothing
else, so a citation naming a DOCUMENT was invisible** — `ATTACKS-07`,
`FEATS-LIBRARY-01`, `PLAYTEST-RULINGS-01`. **33 cells across 7 files, in the
instrument built to find exactly them.** Species reported 1 and had 8.

Reconciled against your count: species carries **13 citation cells — 8 in value
fields, 5 correctly in `note`**. `professions` 1 renders; `programmings` 2
render, 1 correctly in a note; `profession_grants` 2, both correctly in notes.

The broadened mark is three capitals and two digits, so `HK-47` and `HKB-3`
stay names, plus the whole-cell exemption that already covered resrefs.

## 4 — And two more in the same convention

**`apply_to` only ever looked at string values.** `powers.prerequisites` is a
**list**, so `Officer 1 — PT-220` went through two slices untouched. **The
check saw them and the fixer could not reach them**, which is the worse half of
that pair.

⚠⚠ **And `PT-1467`'s splitter damaged five shipped cells and I did not
notice.** It guarded a citation used as a **subject** and not the same token
used as the **object of a preposition**:

    maximum 20d4, cap lowered at `PT-472`.    →   cap lowered at.
    AUTHORED at `PT-XXX`.                     →   AUTHORED at.
    Opened from lightsaber-only by `PT-XXX`.  →   … only by.

**Wrong in `base-rules` for two slices.** A convention written to keep asides
off a player's screen left five sentences broken on it instead — the second
time this splitter has done damage, and the first time it shipped.

The rule now: a citation is removable only when something **separates** it — an
em dash, a bracket, a comma, a full stop. Attached to a lower-case word it is
grammar and it stays. All five restored verbatim by re-extraction from source.

---

## Where the count is

**51 → 48 shipped cells, and that number is honest rather than good.**

| file | was | now | why |
|---|---|---|---|
| `species` | 8 | **3** | five moved into `note` |
| `professions` · `programmings` | 3 | **0** | |
| `powers` | 44 | **7** | the `targets` column, and ⚠ +2 the guard now refuses to mangle |
| `items` · `feats` | 0 · 8 | **7 · 10** | ⚠ the broadened mark can finally see them |
| `equipment.section` | 6 | 6 | `PT-1467` slice 2, still open |
| `worlds` | 0 | 14 | ⚠ newly visible — `no_menu_reason` names a decision document |

**Everything left is a citation doing grammatical work** — an authoring
decision, not a formatting one, and the splitter now says so instead of
breaking the sentence.

## Tests

**661 green** — Lodestar 297 · Lens 4 · Loom 119 · app 241.

`base_rules_test`'s total moved 2547 → 2549 for the two new base types. A total
that moves when the corpus grows is doing its job: it is there to catch a file
that stops loading, not to freeze the rules.

## Still open

- **The producer** — chargen writing `[equipment]`. Fully unblocked now.
- `equipment.section` — a value used as a key.
- 48 cells where a citation is load-bearing in a sentence. **Two are named:**
  the Droid/Assassin design-rationale paragraph, and Wookiee
  `extraordinary_recuperation`.
- Conditional damage (`1d4 + 1d10 vs droid`) still unmodelled, so the Ion
  Blaster is authored and still arms nobody.
