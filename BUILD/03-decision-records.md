# 03 · Reconciling the two decision records

**Read six of the Atlas's 34. Nothing resolved — one contradiction found and
reported, two defects in my own export fixed.**

---

## ⚠ First: THERE ARE THREE REGISTERS, NOT TWO

| Scheme | Where | Example |
|---|---|---|
| `PT-*` | `MAIN_WORK` | `PT-1396` |
| `D-NAME-NN` | `KOTOR_RPG_ATLAS/decisions/` (34 files) | `D-MENU4`, `D-CARD-01` |
| ⚠ `D-XY` | `KOTOR_RPG_Library/consolidated/C12-DECISION-REGISTER.md` | `D-AB`, `D-AJ`, `D-AK` |

**The third was not in the brief.** `SKILLS-01 §9.3` cites `D-AJ`;
`FORCE-POWERS-01`'s neighbours cite `D-AK`. These are **not** Atlas decisions —
no `D-AJ.md` exists in `decisions/`. Two of the three schemes share the `D-`
prefix and mean different registers.

## 3 · The citation check — ⚠ WORSE THAN THE ONE YOU FOUND

**Seven distinct Atlas decisions are cited across eleven `MAIN_WORK` documents,
and NOT ONE of them exists as a file in `MAIN_WORK`.**

| Decision | Cited by |
|---|---|
| `D-CARD-01` ×7 | `ENGINE-SPEC-02-GENERATOR` · `CHARGEN-FLOW-MAP-01` · `CONSTRAINTS-01` · `SKILLS-01` · `CHARACTER-CREATION-01` |
| `D-OPEN-01` ×6 | `CONSTRAINTS-01` · `ENGINE-SPEC-02-GENERATOR` · `ENCOUNTER-01` · `DROID-MODELS-01` |
| `D-MENU4` ×4 | `CHARGEN-DATA-01` · `CHARACTER-CREATION-01` · `DROID-MODELS-01` |
| `D-CURRENCY-01` ×3 | `QUESTIONS-01` · `ROADMAP-02` |
| `D-TIEBREAK-01` | `METHOD-RECORD-01` |
| `D-ROLE-01` | `CONSTRAINTS-01` |
| `D-NOMENU-01` | `CHARGEN-DATA-01` |

Plus eight `D-XY` citations pointing at the **Library's** register.

## 1 · The six, and what they rule

### `D-AGE-01` — `min_age` on a world record
`min_age` is populated **only where a world's population ended before 3956 and
never resumed**. One world qualifies: **Urkupp, 40**, after the 3996 Cron Cluster
supernova. *"If it ever fires on more than a handful of worlds, that is a signal
to re-check the dates — not a signal to build machinery."*

**MAIN_WORK: SILENT.** Chargen has no age concept at all — no step, no field, no
record. ⚠ Not a contradiction, but the rule is unenforceable until one exists.

### `D-VIT-01` — ⚠ NOT ABOUT VITALITY
**It is the *Vitiate* exception**: a bounded admission of a SWTOR character,
splitting pre-3951 as **setting fact** from post-3951 as **destiny, not setting**.

> **⚠ The brief expected this to bear on `PT-648`'s vitality formula. It does
> not touch vitality at all.** The ID reads as an abbreviation of a mechanic and
> is an abbreviation of a name. **No contradiction, because there is no overlap.**

### `D-ROLE-01` — `homeworld` versus `place`
Every world is one or the other. `homeworld` **needs a teaching menu, because
the menu is the mechanical payload**; `place` needs terrain and history and **no
menu at all**. Default `homeworld`.

**⚠ THIS PROBABLY EXPLAINS THE 12 MENULESS WORLDS BETTER THAN `D-NOMENU-01`
DOES** — they may be `place` records rather than worlds awaiting a menu. **Not
determined here**, because the field does not exist in the data (below).

### `D-NAMES-01` — the register lists SYSTEMS, not planets
Adding a `world` field beat renaming: *"Renaming would have broken the register's
own convention across all 4,931 rows to fix a lookup problem in six."*

**⚠ AND THIS WAS A DEFECT IN MY EXPORT.** `worlds.toml` used the **system** name
for all 301. A player would have been offered **`Rakata Prime`** as a homeworld
rather than **`Lehon`**, `Mon Calamari` rather than `Dac`, `Telos` rather than
`Telos IV`. **14 rows carry a distinct planet name — not six; the ruling was
written against six and the field has since grown.** Fixed: `name` is the planet
where one is given and `system` carries the register's own name.

### `D-CRYSTAL-01` — the Dantooine crystal cave
Setting lore. **No chargen bearing. MAIN_WORK silent.**

### `D-OPEN-01` — `openness`, three values on every world
`dense` 41 · `open` 247 · `blank` 10. **Not a quality grade** — *"`open` is the
most useful state a world can be in, and a table will spend more time on one
`open` world than on ten `dense` ones."*

**⚠ ALSO MISSING FROM MY EXPORT, and cited by four `MAIN_WORK` documents.**
Fixed: 292 of 301 now carry it.

## 2 · The reverse direction — does MAIN_WORK supersede any of the six?

**No.** On the five that touch anything we build, `MAIN_WORK` is **silent**
rather than contrary: no age concept, no world `role`, no `openness` consumer, no
planet-versus-system distinction, and `D-VIT-01` does not overlap `PT-648`.

**⚠ The traffic ran one way this time.** `D-MENU4` superseded us; nothing of ours
supersedes these six. That is not evidence it cannot happen — **nobody has looked
at the other 28.**

## ⚠ Two fields are RULED and NOT IN THE DATA

`selection.json` carries `tier · system · sector · region · coord · no · note ·
sector_source · world · world_note · added`. **There is no `role` and no
`min_age`.** So `D-ROLE-01` and `D-AGE-01` are decisions whose fields nothing
populates. Neither is exported, because exporting an absent field would invent
one.

## 4 · Is this checkable? ⚠ PARTLY, AND THE USEFUL PART IS CHEAP

`check_stale_claims.py` works because a ruling ID and its entry are in one
repository. These are not, so it structurally cannot see them.

**What a check COULD do, with only `gh` and read access:**

1. **Existence.** Grep `MAIN_WORK` for `D-*`, resolve each against
   `ATLAS/decisions/` and the Library's `C12` register, and fail on any that
   resolves to neither. ⚠ **This would have caught `D-CURRENCY-01` and the other
   six the day they were written.**
2. **Last-changed.** `gh api .../commits?path=decisions/D-X.md` gives a date per
   decision. **A citation older than the decision it cites is exactly the
   `D-MENU4` failure**, and that comparison is two API calls.

**What it CANNOT do:** tell whether a decision's *content* still agrees with the
document citing it. `D-MENU4` changed three to four **without changing its
filename**, and only reading it catches that. **Same limit as
`check_extracts.py`: a fingerprint proves a match, never that the thing matched
was right.**

**⚠ And it needs a token that can read the Atlas.** This agent's can; the owner's
404s. **A check that only runs for one participant is a check with a gap in it**,
and that is a decision above this agent.

## Not done, deliberately

Did not read the other 28. Did not resolve anything — `D-MENU4` was an owner
ruling and superseding one belongs to whoever made both. Did not populate `role`
or `min_age`. **Did not rule on the three ID schemes**, which is the owner's.
