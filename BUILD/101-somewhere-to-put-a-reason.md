# BUILD 101 — `PT-1600`: `audit_grid` gets somewhere to put a reason

**Gate SENDABLE** — 49 checks, 30 blocking, 0 failing. MAIN_WORK `6d94fe6`.
No code changed; suites unmoved at **1,144 green**.

---

# ⚠⚠ PER-SITE, NOT PER-CATEGORY — AND THE REASON IS IN THIS CORPUS ALREADY

    EXCUSED[('AREA-FORMAT-01.md', 35)] = "KOTOR's own effective distance,
        quoted at PT-1571 as EVIDENCE for the ten-square default … we do not
        use 35 … §14's own preferred fix is not available for a radius that is
        not ours to restate."

**One entry per (document, value), each carrying why.** Three arguments, and the
third is the one that decided it:

**1 — A category needs a marker, and a marker is a convention.** For the check
to recognise *"a number inside a block attributed to a source"* it must read
something an author remembers to write. **`PACKAGE-FORMAT-01` already names that
shape in another context:** NWN expressed dependency precedence as a *naming
convention* — `_top` and `_core` suffixes — and the document's verdict is
**"a convention is not a declaration."** A category exemption would be that
defect, inside a check.

**2 — The list IS the scope line.** `check_coined_names`' stated discipline:
*"a site nobody adds is a site nobody checks, which is the honest limit and is
printed rather than implied."* Every exception in the corpus is readable in one
place and reviewable. A category exemption is unbounded — **the next attributed
number is excused with nobody looking.**

**3 — The hole is bigger than the one it patches.** `PT-1600`'s defect is *"an
explanation is indistinguishable from a second offence."* **Under a category
rule every explanation becomes an exemption** — so the check stops seeing a
genuinely wrong number that happens to sit in an attributed block. **That is the
same defect inverted, and strictly worse**, because the first one is loud and
this one is silent.

---

# ⚠⚠ AND THE COST YOU FEARED IS NOT THERE — I COULD NOT REPRODUCE THE DOUBLING

> `PT-1600`: *"my note saying `35 m` is a quoted value CONTAINED the string, so
> the check counted two."*

**That mechanism is real for a check that counts occurrences. This one does
not.** It has always collected a **set** of distinct values per file —
`{int(m) for m in re.findall(...)}` — and `bad += len(odd)` counts distinct
values, not hits.

**Verified two ways** rather than assumed:

    appended "**⚠ 35 m is a quoted value, not ours.**" to AREA-FORMAT-01
      → still ">> AREA-FORMAT-01.md: 35 m", one line, count 1

    a3ffe2e's own diff — the only change to that file is
      "97.8% on the 20 m default"  →  "— THEIRS, NOT OURS"
      Neither side carries a second odd number.

**⚠ AND THAT IS WHAT MAKES PER-SITE CHEAP HERE RATHER THAN A TRADE.** Because
the exception is **value-shaped rather than occurrence-shaped**, one entry covers
the evidence line **and every sentence written about it.** So the property
`PT-1600` asks for — *documenting an exception must not be punished* — falls out
of the grain, and does not have to be bought with a category rule.

**Controlled**: a note containing `35 m` added to the excused file, gate green.

---

# ⚠⚠ AND IT IS A RATCHET. FOUR WAYS IT FAILS, ALL FOUR TRIED

    1  a NEW odd value anywhere read       PACKAGE-FORMAT-01: 7 m — 3.5 squares
    2  a DIFFERENT odd value in the
       excused file                        AREA-FORMAT-01: 9 m — 4.5 squares
    3  the excused value HEALED            "no longer carries 35 m — REMOVE THE
                                            EXCEPTION"
    4  a note explaining the exception     green

**Case 2 is the one that matters**: the exemption is `(file, value)`, not the
file. `AREA-FORMAT-01` is not now a document where odd metres are allowed.

**Case 3 is `BUILD 94`'s rule and `loom_can_write_test`'s.** A list that may only
grow is a record of what we have given up on. **An entry that stops firing must
break this file exactly as adding a new one does** — otherwise removing the
`35 m` from the corpus leaves a permanent excuse for a number nobody carries.

---

# ⚠⚠ AND THE CATEGORY ANSWER IS ALREADY IN THIS CHECK, APPLIED WIDER THAN THE 35

`audit_grid` skips `ITEMS-0\d` for `PT-346`'s reason: *"ITEMS-01..08 transcribe
`dialog.tlk` descriptions verbatim — those distances are the SOURCE's prose."*

> **That is the same category as the `35 m`** — a number quoted from KOTOR —
> **expressed as a filename, so nine documents are exempt from a grid rule in
> full.** It is exactly the coarseness argued against above, and it predates the
> ruling.

**⚠ AND ITS OWN COMMENT SAID `01..08` WHILE THE PATTERN READS `ITEMS-0\d`,
WHICH IS NINE.** A scope line one file narrower than the scope, which is what
`PT-62` exists to prevent. **Both the skips and their reasons are printed now**
rather than living in comments nobody runs. Narrowing them is a corpus decision
and I have not taken it.

---

# ⚠⚠ AND `BUILD 92` ANSWERED A QUESTION AND NEVER APPLIED THE ANSWER

> `BUILD 92`: **"DOES THE FENCED-EXAMPLE CHECK BELONG IN THE GATE? YES … AND IT
> SHOULD GO IN NOW BECAUSE IT IS GREEN NOW."**

**It was never added.** It sat outside the gate for eight slices, and so did
`check_ruling_ids`. **A conclusion stated in a report and never applied is the
shape this corpus keeps finding in its own code**, and I put it in a report.

Both are in now, both blocking, **and both are green today** — which is the
condition `BUILD 92` itself gave: *a check added while the corpus is clean
asserts a property; a check added while it is dirty becomes an allowance list.*

    PLAYTEST GATE — 49 checks, 30 blocking, 19 reporting
    SENDABLE — 2 warning(s)

The two warnings are `check_citations` and `audit_docrefs`, both advisory and
both unchanged by this slice.

---

# ⚠ ACCEPTED WITH NOTHING TO DO

**`PT-1599`** — fixed at source, and the third-rung finding is in the document.
**Point blank stays ungated**, and the reasoning lands: the `−4` was a permanent
tax only because nothing could shoot from a distance, and the mover is what
changes that. **The bed hurts because it is telling the truth.**
