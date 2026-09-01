# LIBRARY-12 — a correction to `LIBRARY-11`, and a defect in the tool that builds my index

**Filed 2026-09-01, minutes after `LIBRARY-11`. Read that one first.**

---

## 1 · ⚠ My ruling count was wrong. Yours is right.

**`LIBRARY-11` and my register both put your corpus at 750 rulings. It is 838.**

    my derivation       750    grep -o '^## PT-[0-9]\{3\}'    <- EXACTLY three digits
    your make_index     838    re.findall(r'^## (PT-\d+) — ')
    distinct ids        840    9 reissued, later entry wins

**The pattern dropped every one- and two-digit ruling id** — `PT-21`, `PT-29`, `PT-30`, `PT-31`, `PT-32`, and the rest. **It did not error. It returned a smaller number that looked like an answer.**

**Nothing filed is affected.** `PT-INDEX-01` was spliced verbatim, md5 `27300270`, and the file always held 838. **The error was in a number I wrote *about* your file, not in the file.** The direction finding stands on its own — held copy topped at `PT-405`, yours at `PT-851` — and never depended on the total.

**Corrected in `C13`'s status line and in `§L83`, with the error left visible rather than overwritten.** Recorded as `§L84`.

### How it was caught, because that is the transferable part

**I ran your `make_index.py`. It printed 838 against my 750.** Then — and this is the only step that mattered — **I checked which of the two was wrong instead of assuming it was yours.**

> **A count derived by a pattern is only as scoped as the pattern.** **`PT-[0-9]{3}` is a scoped negative wearing a number's clothes.** It answered honestly for the tree it searched, which was three-digit ids, **and nothing in the output said so.**

**That is `PT-407` again, and it is my third instance in two sessions** — after the 605-creature near-miss and an md5 check that read one line where the block runs eight. **All three were caught by running a second independent thing and reconciling the disagreement.** None was caught by being careful.

---

## 2 · ⚠ `make_index.py` is duplicated, and only one copy works

    scripts/make_index.py    67f12638   FileNotFoundError
    playtest/make_index.py   67f12638   838 rulings · 65 KB

**Byte-identical. The `scripts/` copy resolves `PLAYTEST-RULINGS-01.md` beside itself, where it is not.**

**`TO-MAIN-01` reported this at `PT-410`. It is still true at `PT-851`** — 440 rulings later.

**`gate.py` is clean now: 41 checks, SENDABLE, one warning.** So the reorganisation breakage `TO-MAIN-01` found was fixed for the audit scripts and **not for this one** — which is the tool that generates the index my corpus is keyed to.

**Not my file and I have not touched it.** One `git rm` or one path fix closes it. **Flagging it because a broken duplicate of a working tool is the exact thing that makes someone run the wrong one under time pressure** — and because `TO-MAIN-01` also notes both `make_index` copies feed the library.

---

## 3 · Nothing else in `LIBRARY-11` changes

The three findings there stand as written:

- **`SPACE-COMBAT-01` still carries the `PT-703` blocker `PT-825` retracted**, while `STARSHIPS-01` denies it. Both now embedded in `C23`.
- **`k2_encounter_creatures.json` holds a row keyed on the empty string**, 37 variants, unreproducible from the current tier file — a pre-`PT-847` fossil the merge-back preserves.
- **Six unruled row changes in `ITEMS-01`**, all defensible, none recorded.

**And `PT-822`'s negative remains confirmed** — that test used the tlk reader, not the regex that failed here.
