# KOTOR RPG — handoff drop

**Cross-agent file exchange for the *Star Wars: Knights of the Old Republic* d20 project.**

**⚠ Files here are pushed by the main agent and fetched by specialist agents. Nothing here is authoritative — the working tree is.**

---

## For the CLASS DESIGNER

**Start with `BRIEF-CLASS-DESIGNER.md` in this directory.** **It tells you what the project is, what is settled, and what you are being asked to do.**

**Then read all ten documents in `docs/` and the nineteen source tables in `data/`.**

### `docs/` — the rules

| File | What it is |
|---|---|
| `CLASS-ROSTER-01.md` | The four class lists. 37 classes |
| `SKILLS-01.md` | 24 skills, class lists, budgets, aptitude rules |
| `CLASS-ATTACKS-01.md` | Rates, chain bands, per-class attack grants |
| `FEAT-SCHEDULE-01.md` | Feat totals to level 30. **The authority rates derive from** |
| `MULTICLASS-01.md` | How classes combine. No entry credit |
| `ATTACKS-01.md` | What an attack chain is. Three currencies |
| `ACTION-ECONOMY-01.md` | What a turn is. Initiative and surprise |
| `SKILL-RESOLUTION-01.md` | The DC ladder |
| `FEATS-LIBRARY-01.md` | The feats |
| `PREGENS-01.md` | Nine worked characters |
| `PLAYTEST-RULINGS-01.md` | **`PT-1` through `PT-85`.** Every ruling, why it was made, and what it superseded |

### `data/` — the KOTOR source tables

**BioWare `2DA` tables from KOTOR 1 and 2.** **⚠ Evidence of design intent, never rules authority.**

**`k2_classes.2da` is the one that matters most** — seventeen rows, including the cut Bounty Hunter and every prestige class.

**Binary `2DA V2.b` where noted, tab-separated text where exported.** **If you cannot parse one, say so rather than guessing at its contents.**

---

## Exchange directories

    to-designer/     pushed by the main agent
    from-designer/   pushed by the class designer

**⚠ Both agents have `git` and a token. Push directly rather than asking the owner to carry a file.**

    git clone https://TOKEN@github.com/aidanpscott/KOTOR_RPG_HANDOFF.git
    # write to from-designer/
    git add -A && git commit -m "..." && git push

**Name files with a sequence number: `from-designer/FINDINGS-01.md`, `to-designer/REPLY-01.md`.** **Never overwrite the other side's directory.**

---

## Reading these by URL

    https://raw.githubusercontent.com/aidanpscott/KOTOR_RPG_HANDOFF/main/BRIEF-CLASS-DESIGNER.md
    https://raw.githubusercontent.com/aidanpscott/KOTOR_RPG_HANDOFF/main/docs/SKILLS-01.md
    https://raw.githubusercontent.com/aidanpscott/KOTOR_RPG_HANDOFF/main/data/k2_classes.2da

**Any file, same pattern:** `.../main/` then the path.

---

## ⚠ Held back deliberately

**Force material** — the pool, the power roster, and how a character becomes Force-sensitive. **Sent when the Jedi and Sith classes come up.**

**⚠ `PLAYTEST-RULINGS-01` was listed here as held back. It was not** — it was in the upload and the designer used it. **Corrected: it is in `docs/` and it is in play.**

**Eighty-five rulings, roughly 127KB.** **It is the reason any number is what it is. Read it when a number looks wrong.**
