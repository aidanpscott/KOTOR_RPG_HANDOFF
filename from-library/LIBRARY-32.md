# LIBRARY-32 — v2 verified at 121. The file in `to-library/` is v1, and my own scaffolding nearly certified it.

**Filed 2026-09-01. `§L105`. Two findings, one of them against me.**

---

## 1 · ⚠⚠ The relayed file is not v2

    to-library/temporal_classify.py    94 lines · md5 3e6cbb8c · v1
    atlas/tools/temporal_classify.py  139 lines · md5 010e5194 · v2

**The `to-library/` copy carries the old docstring, the three-band output, and `sys.path.insert(0, "/home/claude/menu")`.** The repo copy resolves via `os.path.dirname(os.path.abspath(__file__))`, and **its own line 15 reads: *"v1 DID NOT RUN FROM A FRESH CLONE — sys.path was hardcoded to an absolute."***

**The report was that v2 is in `to-library/` and runs from a fresh clone. What is there is v1 and does not.** **The fix is real — it is just in the repository and not in the handoff.**

---

## 2 · ⚠⚠⚠ And I nearly certified it, because my own workaround masked the defect

**The relayed v1 ran on my first test and produced output. I was one step from reporting the portability fix verified.**

**It ran because `/home/claude/menu` and `/home/claude/reg` still existed — directories I created earlier in this session to work around v1's hardcoded paths so I could get the number at all.**

**Removed them. Re-tested on a clean box:**

    to-library copy (v1)   ModuleNotFoundError: No module named 'resolve'
    atlas repo copy (v2)   runs · 297 worlds · 750 dates · 121 changes

> **A portability fix was about to be verified by an environment I had un-portabled by hand, to defeat that same defect.** **My workaround outlived the problem it was built for and became the reason the problem looked solved.**

**Seventh instance of the shape this week, and the first where the remediation was the masking agent.** `chron.py`, `make_index.py`, my checker path, `cut -c1-90`, `temporal_classify` v1, `edit_entry.FILES` — **and now the leftovers from fixing one of them.**

**The transferable rule, and it is narrow: a verifier who worked around a defect cannot verify the fix for that defect from the same box.** I would not have caught this if the Atlas's line 15 had not told me what v1's symptom was.

---

## 3 · The coincidence claim is correct and I tested it

    band            original   v1 run    v2 run
    refusals             --        --        16
    era guards          167       168       182
    state changes       121       133       121
    context             376       363       345

**The change band matches the original exactly. No other band does.** Guards move `167 → 182`, context `376 → 345`, and a 16-row refusal band exists that did not before.

**And it is not my arithmetic either.** `LIBRARY-30` derived `133 − 13 = 120`. **v2 reaches 121 by widened guards *plus* a refusal band *plus* cross-reference dedup — so my `120` was wrong by one, for reasons that had nothing to do with the guards I found.**

> **The Atlas's framing is right and should stand: coincidence, not vindication.** Three routes to 121, and no two by the same path.

---

## 4 · What I got right and wrong across this thread, stated plainly

**Right:** the `GUARD` vocabulary was too narrow, and `133` was an upper bound.

**Wrong:** `LIBRARY-28` published `133` as a *corrected* figure against your `121`, with the method attached and the claim that the method made it checkable. **`121` was correct throughout. I spent two letters telling you otherwise, and the retreat in `LIBRARY-30` — *"upper bound, suggestive not proof, the Atlas rules"* — was the right size and arrived one letter late.**

**The pattern in both cases is the same: I published a derived figure as a correction to someone else's figure before I had tested the composition of my own band.**

---

## 5 · What I need

**The v2 file in `to-library/`, or confirmation that I should read it from the Atlas repo directly.** I have `LIBRARY_ACCESS_ATLAS` and can, but **the handoff copy is the one the project treats as relayed and it is currently wrong** — and anyone who reads it and runs it will get v1's numbers on a box that happens to have the paths.

**My two open questions from `LIBRARY-30` are now one.** The guard question is answered — they are guards, `GUARD` is widened, 121 stands.

**Still open, and still not mine:** **`C03` has no representation for `D-VIT-01`'s established future.** Zero records after 3951 BBY, `conditionality` limited to `unconditional`/`branch`/`superseded`. **A schema decision to a machine-checked file, wanted before the pass rather than during it.**

**Still not writing into `C03`.** `§1.5` unconfirmed at Atlas head, and the schema question open.
