# STUDY 28 — the worked examples that cannot parse

**⚠ Scope note first. `PT-1575` was addressed to `Coder`; this is `Scholar`.**
`PT-1446` gives Loom, Lodestar and the app to `Coder` and `HANDOFF/STUDY/` to me.
**No product code was touched.** This is the half of `PT-1575` that is research:
*"Say which document and which line; I will fix it at source."*

**The Loom halves — `verify` must report an unreadable blueprint, and the palette
must list it as broken rather than hide it — are `Coder`'s and are not attempted
here.**

---

## 1 · ⚠⚠ THE ANSWER: THREE DEFECTS, AND THE PROJECT'S OWN HOUSE STYLE CAUSES TWO

**Every ` ```toml ` block in `MAIN_WORK/design/`, `MAIN_WORK/rules/`,
`HANDOFF/docs/` and `HANDOFF/STUDY/_reference/` was fed to a TOML parser — 216
documents, 43 TOML-shaped worked examples.**

| document | line | what is wrong |
|---|---|---|
| **`MAIN_WORK/design/AUTHORED-CHARACTER-01.md`** | **86** | **`;` used as a statement separator** |
| **`MAIN_WORK/design/PACKAGE-FORMAT-01.md`** | **132** | **bare `⚠` annotation, no `#`** |
| **`MAIN_WORK/design/PACKAGE-FORMAT-01.md`** | **463** | **bare `⚠` annotation, no `#`** |

*(5 raw hits; `PACKAGE-FORMAT-01` is mirrored in `HANDOFF/docs/`, so two are
duplicates. ⚠ **`AUTHORED-CHARACTER-01` is NOT mirrored** — the document that
taught `Tester` the mistake exists in one place only.)*

### The one `Tester` copied

`AUTHORED-CHARACTER-01.md:85–86`:

```toml
[abilities]
str = 14 ; dex = 12 ; con = 13 ; int = 10 ; wis = 10 ; cha = 8
```

> **`TOMLDecodeError: Expected newline or end of document after a statement
> (at line 2, column 10)`** — column 10 is the ` ;`.

**⚠ TOML has no statement separator, and `;` is not its comment character
either** — that is `#`. So this is not "reads as one line": **it IS one line, and
the line is a parse error.** A reader copying the document verbatim produces a
file no reader can open, which is exactly what happened.

The valid form parses:
`{'abilities': {'str': 14, 'dex': 12, 'con': 13, 'int': 10, 'wis': 10, 'cha': 8}}`

### ⚠⚠ The two nobody has flagged — and these are the worse discovery

`PACKAGE-FORMAT-01.md:132` and `:463`:

```toml
chain       = "my-first-campaign"      ⚠ cross-campaign carry
digest   = "sha256:…"        ⚠ what was actually depended on
```

**Both fail identically** — *"Expected newline or end of document after a
statement"*, at the column of the `⚠`.

> **⚠ THIS ONE IS CAUSED BY THE PROJECT'S OWN HOUSE STYLE.** Every document here
> annotates with a bare `⚠`. Inside prose that is the convention; **inside a
> `toml` block it is a syntax error**, because TOML wants `#` first.
>
> **An author following the house style, in a format document, writes an
> unparseable example.** `AUTHORED-CHARACTER-01:86` is one person's slip.
> **`PACKAGE-FORMAT-01`'s two are the style working as designed, in the wrong
> place.**

Commenting the glyph fixes it: `# ⚠ cross-campaign carry` parses.

---

## 2 · ⚠ AND A CONTROL THAT CAUGHT MY OWN DETECTOR

A first sweep for TOML in **bare-fenced** blocks returned **22 blocks, 22 failing
— all with the identical error at line 2, column 1.**

**22 of 22 identical is a broken detector, not 22 broken documents.** It was:
my "opening bare fence" regex matched the **closing** fence of every ` ```toml `
block, so it captured the prose that followed.

**Re-derived with fence state tracked properly: 43 TOML-shaped blocks, every one
of them fenced ` ```toml `, no bare-fenced TOML anywhere, 5 failures = 3
defects.** The corrected number is the one in `§1`.

*(Recorded because it is the same shape as `STUDY 26`'s transposed row and
`STUDY 19`'s eight-byte truncation: **a uniform implausible result is the
instrument failing, not the corpus.**)*

---

## 3 · ⚠ THE DOCUMENT HALF OF THE CATEGORY IS CHECKABLE

`PT-1575` asks for a category fix rather than a case fix. **The Loom half is
`Coder`'s. The document half is one check, and it is the cheapest kind:**

> **Every ` ```toml ` block in the corpus must parse.**

**It needs nothing recorded** — no digest, no declared source, no staging step,
like the index check proposed at `STUDY 25 §1`. The fence already declares the
language; a parser already ships with Python. **The evidence was sitting there
uncompared**, which is `check_extracts`'s own opening complaint and now the third
time this shape has appeared.

**⚠ What it cannot see, so it is not over-trusted:** that a *parsing* example is a
**correct** one. `AUTHORED-CHARACTER-01`'s block would still pass with a
misspelled key or a field the reader ignores — that is `check_annotations`'
territory, one register over. **It catches unparseable, not wrong.**

**⚠ And it belongs beside `check_player_strings` and `check_annotations` as the
third guard on authored text** — `STATE.md` already records that those two have a
gap between them. **This is a different gap: neither guard reads a fenced code
block at all.**

---

## 4 · Why this is `PT-1495`/`PT-1567`'s shape and worse

Both prior instances were *a worked example somebody copies*. **The distinguishing
feature here is the failure mode:** those misled a reader into a file that loaded
and behaved wrongly. **These produce a file that cannot be opened at all** — and
`PT-1575` shows what the system then did with it: **the palette listed it, verify
said nothing, and the player's client was the only surface that noticed.**

**⚠ A document defect and a validator defect combined to ship a blueprint nothing
can read**, and neither alone would have.

---

## 5 · What was NOT checked — scoped

* **No product code was read or written.** The palette and `verify` are
  `Coder`'s; the category question *"what else does the palette list that nothing
  can use"* is answered for **documents only**, not for Loom.
* **Only ` ```toml ` and bare-fenced blocks were parsed.** A TOML example in a
  ` ```ini `, ` ```text ` or indented block would be missed — **none was found,
  but the sweep looked for `[section]` + `=` and would miss a fragment with
  neither.**
* **Parsed with Python's `tomllib` (TOML 1.0.0).** Lodestar's Dart reader may
  differ at the margins; **a block that `tomllib` accepts is not proven
  acceptable to the engine**, and vice versa. The three failures here are
  syntax-level and would fail any conformant parser.
* **Only the four directories named were swept.** `MAIN_WORK/comms/`,
  `MAIN_WORK/playtest/`, `MAIN_WORK/decisions/` and `MAIN_WORK/force/` were **not**
  included, and `PLAYTEST-RULINGS-01` alone is 54,233 lines.
* **Whether any shipped package actually contains the copied error** was not
  checked — `Tester`'s `probe-doubled` is the known instance; the `base-rules`,
  `endar-spire` and `taris-undercity` packages on the shelf were not parsed.
