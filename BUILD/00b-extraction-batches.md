# 00b · The extraction batches — and the limit that matters most

**Backfilled.** `KOTOR_RPG_MAIN_WORK` `869e13a`. Ran across four briefs before
`BUILD/` existed.

---

## ⚠ THE FINDING THAT OUTLIVES ALL THE OTHERS

`TRACE-100` extracted `FEATS-LIBRARY-01` and returned **192 entries**. The
document's own summary said 221 and `CHARGEN-DATA-01` said 156. Three numbers,
none agreeing — and the argument was about **which number was right**.

> **⚠ 192 was a COMPLETE AND CORRECT COUNT OF THE WRONG SECTIONS.**

Every one of its 192 entries came from `§5` and `§5c`. Sections **1 to 4 — the
buyable pool — were absent entirely.** `Cautious`, `Toughness`, `Two-Weapon
Fighting`, every weapon proficiency, and **`Skill Focus`**, which
`CHARGEN-FLOW-MAP-01 §4`'s dependency graph names as a source of aptitude.

The re-extraction found **320 entries across 121 chains**, and §1, §2 and §3
match the document's own summary **exactly** — which is the evidence the method
is right, because the same parser that reproduces 16/6, 9/3 and 68/26 without
adjustment is the one reporting 39 where the summary says 36.

## ⚠ AND `check_extracts.py` CANNOT CATCH THAT

The fingerprint check compares an extract's recorded source md5 against the file
on disk. **It proves an extract matches the source AS READ. It cannot prove the
read was right.** A faithful read of the wrong half passes it perfectly.

**What catches it is a CONTROL**: run the rewrite against the OLD source and
check it reproduces the shipped numbers. If it does, the difference is the source
and not the reader. If it does not, the reader changed and you have to say why.

**⚠ The control earned itself on `PROFESSIONS-01`.** A rewrite that read `§1`
alone gave 16 grants where the shipped file had 22, **and looked finished**. The
grants are split across two tables: `§1` has 16 and `§3b` *"RECOMMENDED
ADDITIONS"* has the other six, and `§1`'s own heading counts both.

## What else the batches established

**Ten broken structures**, and none announced itself. `FORCE-POWERS-01`'s table
is interrupted twice with no repeated header — a naive read returns **39 of 104**.
`FEATS-LIBRARY-01`'s §2 breaks once and returns **3 of 9**. `CLASS-TABLES-DROID`'s
main table has a split header with a LaTeX `\multicolumn` leak and **zero data
rows in the first half** — a reader gets nothing and reports nothing wrong.

**⚠ A line-count tolerance is the wrong stop.** `FEATS-LIBRARY-01 §3` breaks
across seven lines of prose. These documents separate tables with a **heading or
a `---` rule** and nothing else.

**Five stale headings.** `CLASS-ROSTER-01` alone has had three. **Trust the list.**

**Every extraction now has a script**, and that is the method finding: the
original passes had none, *which is exactly why a source edit could not be
re-run*. `species.json` sat at 52 for four rulings after `PT-1333` wrote the five
missing parents, because nothing existed to re-run.

**⚠ And the fingerprint's own limit:** it proves an extract matches the source
**as staged**, not that the staged copy matches the corpus. That gap is what
produced the 52-versus-57 confusion — the staged `SPECIES-CHAPTER-v2` was the
stale artifact, not the extraction.
