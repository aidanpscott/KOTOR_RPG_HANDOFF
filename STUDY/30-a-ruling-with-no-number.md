# STUDY 30 — a ruling with no number, and ten with the same one

**Following `Coder`'s closing remark on the diagonal thread:** *"A ruling with no
number is one nobody can cite."* **Checked. The concern is right, the case is
bounded — and an adjacent defect is not.**

---

## 1 · THE UNNUMBERED RULING IS A CASE, NOT A CLASS

`PLAYTEST-RULINGS-01.md` is **56,185 lines** and carries **1,547 numbered ruling
headings**.

**The phrase `"Ruled here"` occurs exactly ONCE in the whole file** — line 238,
the diagonal.

**And searching for ruling language in table rows** — `Ruled`, `Adopted`,
`Settled`, `Decided`, `Confirmed` in bold at the head of a `|` row — **returns
exactly one line: 238.**

> **So line 238 is the only ruling in the record that lives in a summary table
> rather than under a numbered heading.** `Coder`'s worry is correct and it
> applies to one ruling, not to a family.

**⚠ Scoped:** two keyword searches, not a read. **A ruling phrased some other way
inside a table would be missed**, and 56,185 lines were not read by anyone in
this thread.

---

## 2 · ⚠⚠ BUT TEN PT- IDS CARRY TWO HEADINGS EACH — AND THAT *IS* A CLASS

**1,547 headings, 1,537 distinct ids.**

```
PT-21  PT-29  PT-30  PT-31  PT-32  PT-368  PT-394  PT-426  PT-484  PT-1085
```

**These are not collisions between unrelated rulings. Each is a ruling and its
own later revision, both live, under one number:**

| id | first heading | second heading |
|---|---|---|
| `PT-30` | *Surprise: no action in round 1* | *Surprise removes the round* |
| `PT-484` | *Herd Animal weapons are per-beast…* | *⚠ NATURAL WEAPONS ARE PER-BEAST, NOT PER-TYPE. Iriaz corrected* |
| `PT-1085` | **✓** *`PT-853` UPDATED WITH EVIDENCE* | **⚠⚠** *`PT-853` UPDATED, **NOT CLOSED*** |

**⚠ And the earlier one is not marked.** `PT-30` at line 490 reads as a plain
live ruling — *"`ACTION-ECONOMY-01 §9`. A surprised character takes no move,
Action, Bonus, Gear, or reaction in the first round."* **No strikethrough, no
"superseded", nothing pointing at line 534.**

> **A citation to `PT-30` is ambiguous. Two headings answer to it and only the
> second is current.**

**`PT-1085` is the sharpest:** the two headings carry **opposite status markers**
— `✓` against `⚠⚠`, *"UPDATED WITH EVIDENCE"* against *"UPDATED, NOT CLOSED"* —
**under one id, both live.**

⚠ **This is `STATE.md`'s own confessed shape**, one register over: *"it carried a
row struck through as answered **and the same row live below it**."* **Here
neither is struck through.**

---

## 3 · ⚠ `audit_superseded.py` DOES NOT COVER THIS

**CHECK 38 detects *"live documents citing an overturned ruling"* — citation
staleness, across documents.** Its own header is careful about its yield and
warns against wiring it as blocking.

**It does not look for two headings sharing one id inside the ruling record
itself.** That is a different relation: **not *"does this citation point at a
superseded ruling"* but *"does this id resolve to one ruling at all."***

**And it is checkable in the cheapest way, again:**

```
group ruling headings by PT- id
red if any id has more than one heading that is not marked superseded
```

**⚠ Third time this shape has appeared** — the stale index (`STUDY 25 §1`), the
unparseable worked example (`STUDY 28 §3`), and now this. **All three need
nothing recorded: the file already contains both halves of the comparison and
nobody had compared them.** That is `check_extracts`' own opening complaint,
now four times over.

**⚠ What it cannot see:** whether the *later* heading is genuinely the current
one. Order in the file is not authority. **It flags ambiguity; a human resolves
which wins.**

---

## 4 · What this does and does not change

**Nothing about the diagonal.** `PLAYTEST-RULINGS-01:238` is unaffected — it is
unnumbered, not duplicated, and `Coder` has already cited it by file and line in
`AREA-FORMAT-01 §3c` and in `Lodestar`'s `squaresBetween`.

**⚠ It is the owner's record.** `PT-1446` gives `MAIN_WORK`'s ruling record to the
owner; assigning line 238 a number, and resolving which of the ten pairs is
current, are both theirs. **Reported, not edited, and no check was built —
`MAIN_WORK/scripts/` is `Coder`'s path.**

---

## 5 · What was NOT checked

* **56,185 lines were not read.** Everything here is keyword and structure.
* **Only `##`/`###` headings matching `PT-<n>` were counted.** A ruling under a
  differently-shaped heading — or the `⚠ Saboteur` problem from `STUDY 25`, a
  glyph inside the heading — **would not have been counted**, and the heading
  regex here does allow a leading `⚠` precisely because of that finding.
* **The other ruling records were not swept** — `MAIN_WORK/decisions/` (34 files
  `STATE.md` records as never read by `MAIN_WORK`), `PT-INDEX-01.md`, and the
  `D-*` decision ids. **The ten duplicates are a `PLAYTEST-RULINGS-01` figure
  only.**
* **Whether any document actually cites one of the ten ambiguously** was not
  checked — that is `audit_superseded.py`'s register and it was not run.
