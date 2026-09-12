# Armory — Editorial Notes

**⚠ NOT PART OF THE BOOK. Internal record, for MAIN, Coder and the owner.**

**This file exists because of `PT-1844`**, and mirrors `BOOKS/timeline/EDITORIAL-NOTES.md`.
The chapters used to carry their findings in an *"Open items, carried from review"* section
citing internal documents and ruling numbers a reader cannot look up. **Those sections are
moved here as each chapter is passed — preserved, not deleted.**

---

# Chapter One — Weapon Damage and the Defence Formula

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED by MAIN**, checked against `EQUIPMENT-01` and
`ACTION-ECONOMY-01` directly. **Sources it stood on:** `EQUIPMENT-01 §1` (melee damage),
`EQUIPMENT-01` with `PT-340` (ranged adds Dexterity), `PT-1` (the provisional lightsaber
line), `PT-341` (the Massive Criticals cap), `PT-339`.

**`ATTACKS-01`'s ranged-damage line is stale against `EQUIPMENT-01`'s own `PT-340`
amendment** — reported at `TO-MAIN-30-AUTHOR.md`, not fixed here. This chapter draws its
ranged-damage value from `EQUIPMENT-01` directly, which already has it right.

**The lightsaber-damage-ability line is provisional in its own source (`PT-1`).** Carried
through as a flag rather than smoothed into a stated fact.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 8 internal citations**, including the whole *Source* column of the damage
table.

**⚠ The damage table's source column could not be handled by the approved rule alone**, and
this is the first Armory exception worth recording. **The rule is "attribute to the game's
own data rather than the internal ruling" — but the four rows are not the same kind of
claim:**

- **Melee one- and two-handed** are straightforward extracted values.
- **Ranged adding Dexterity** is a d20 convention rather than something the games state.
- **The lightsaber line is explicitly provisional** — a reading of an ambiguous source.
- **The Massive Criticals cap is a deliberate departure** from the games, which leave it
  uncapped.

**Blanket-attributing all four to "the game's own data" would have been false for three of
them.** So the column was dropped and **provenance is now stated in prose exactly where it
differs from the games** — which is the `⚠ AUTHORED` discipline the Armory already uses,
turned reader-facing.

**The lightsaber warning is stated more strongly than before, not less.** It now says
plainly that this is **this game's reading of an ambiguous source**, that the source calls
lightsabers *"not melee weapons"* about upgrades and criticals rather than damage, and that
**being wrong is worth roughly ±3 damage on every hit a Jedi lands.**

**The Massive Criticals cap now says outright that it is a departure** — *"one of the few
places where this book knowingly differs from its source rather than reporting it"* — which
the old text conveyed only through a ruling number.

**⚠ And a self-caught over-removal.** My first pass at the armour restrictions dropped the
names **`Soresu`** and **`Well Guarded`**, treating them as internal jargon. **They are not
— they are a lightsaber form and a class feature, both real in-game things a reader can look
up in the Player's Handbook.** The audio rendition of this chapter still named them, which
is how the loss was spotted. **Restored, and the passage is now stronger than either
version:** the restriction decides what kind of defence a character can build.

**✔ The audio rendition needed no pass.** `01-weapon-damage-and-defence-formula-audio.md`
was written as continuous prose for a text-to-speech reader and **carries zero internal
citations already** — checked, not assumed. It remains substantively consistent with the
revised chapter.

**⚠ Deliberately NOT loosened.** Every value survives: the three damage formulas, the six
wield classes and their pairing rules, threat ranges and multipliers, the `2d6` cap, the
sum-of-9 armour rule with both organic exceptions, the uncapped-robe rule and the Jedi
Defence-12 example, and both droid plating tables with K2's uncapped sentinel.

---

# Chapter Two — Melee Weapons

*`PT-1844` pass. This chapter had no "Open items" section of the usual shape; what it
carried instead was a work-tracking section on an incomplete sweep, reproduced here.*

**Chapter status: DRAFT, full-catalogue standard applied.** Eleven families, 62 entries.
**Scope rule:** `PT-342`'s K1-overrides-on-shared-items applied where a genuine difference
appears.

## ⚠ Four weapons still carrying the pre-`PT-1747` Vibrosword die

`PT-1747` moved Vibrosword from `2d6` to `1d12`. The sweep covered the nine
`vbroswrd`-stemmed resrefs. **Four more melee weapons still read `2d6, 19–20 ×2` — the
exact pre-ruling Vibrosword signature — and none of them carry that stem, which is why a
stem-matched sweep would pass over them:**

| Weapon | Resref | Confidence |
|---|---|---|
| **Vibrosword** (K2's own) | `w_melee_06` | **Certain** — same weapon, same name, same 120-credit price as K1's |
| **Echani Vibrosword** | `w_melee_21` | **Certain** — names the family |
| **Sith Tremor Sword** (K2's) | `w_melee_22` | **Certain** — direct counterpart of K1's `g_w_vbroswrd03` |
| **GenoHaradan Poison Blade** | `geno_blade` | **⚠ Suspected only** — die and threat match exactly, but the name doesn't say Vibrosword and `BaseItem` could not be read from this copy |

**⚠ UPDATE — three of these four are now fixed at source.** `w_melee_06`, `w_melee_21` and
`w_melee_22` all read `1d12` in the live `ITEMS-01`. **`GenoHaradan Poison Blade` was not
changed and still reads `2d6`** — so either it genuinely isn't a Vibrosword-family weapon,
or it is a fifth miss. **Settling it needs a `BaseItem` read rather than a die-signature
match.**

**Two resref-versus-base-type disagreements worth noting for whoever runs that check:**
`Raito's Gaderffii` sits at `g_w_qtrstaff03` while carrying the Gaffi Stick's `1d8` die,
and `Baragwin Assault Blade` sits at `g1_w_vbroswrd01` with a `g1_` prefix no other weapon
in the family uses. **Resref stem is not a reliable proxy for base weapon type in either
direction** — the same lesson the `Energy Baton` resolution taught from the opposite side.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 5 internal citations**, and one whole section.

**⚠ The proper-noun check was run deliberately this time, and it changed the outcome.**
Following the `Soresu` lesson from Chapter One, every code-formatted term was checked
rather than pattern-matched. **The resrefs stayed** — all 92 of them. **They are the games'
own item identifiers, not internal project references, and a reader can look them up in the
game files.** Stripping them would have destroyed the catalogue's usefulness.

**The Vibrosword sweep section moved here in full.** It was work-tracking — a ruling
number, a sweep's coverage, confidence ratings and what has since been fixed at source.
**None of it is reader content.**

**⚠ But it left a real residue, and that stayed in the chapter.** The `GenoHaradan Poison
Blade`'s die is genuinely unsettled, and a reader using that weapon needs to know. **The
note is now self-contained rather than pointing at a section that no longer exists:** it
reads `2d6` where its family reads `1d12`, it may belong to a different family than its
damage suggests, **and a Gamemaster is told to treat `1d12` as the working value with `2d6`
as a defensible reading.** That is more useful than the cross-reference was.

**⚠ And a dangling reference caught mid-pass.** Removing the sweep section orphaned the
GenoHaradan entry's *"see the note at the top of this chapter"* — **the same failure mode
caught in the Timeline's Chapter Three.** Found by re-reading the entry after the removal
rather than by trusting the edit.

**The tail section became a caution on item codes**, which is the reader-facing half of the
resref finding: **the code is the games' own identifier and is not a reliable guide to what
kind of weapon something is. Read the family heading, not the code.**

**⚠ Deliberately NOT loosened.** All 11 families, all 62 entries, every die, threat range,
price and property line survives. **The K1-over-K2 rule is stated in reader terms rather
than by ruling number, and the one place a genuine divergence is called out — the Sith
Tremor Sword's sonic value — still names both figures.**

---

# Chapter Three — Ranged Weapons

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: catalogue complete, 122 items across 14 families.** Base table drafted
against `MAIN_WORK/rules/`. **Rulings it stood on:** `PT-1783` (the two long rifles),
`PT-1782` (the perception extension), `PT-1477` (the Hold Out Blaster name), `PT-1473`,
`PT-345` (crystals), `PT-1747`/`PT-339`/`PT-340` (the ceiling comparison), `PT-1825` /
commit `f408708` (the ×3 revert).

**✔ The family catalogue is complete** — 122 items across fourteen families, replacing the
placeholder this section previously carried.

**✔ Flag 1 — the ruled corrections have landed, and this catalogue matches the corrected
file exactly.** The owner ruled that **K2's dice stand**, with two exceptions: **Blaster
Carbine's threat moves to 19–20** (die stays `1d12`) and **Ion Blaster and Ion Rifle revert
from ×3 to ×2**. `EQUIPMENT-01` now carries all three.

**Re-verified after the sync:** of this catalogue's 122 entries, **zero are absent from the
corrected file, zero changed stat line, and zero real rows are missing from the
catalogue.** The membership capture held.

**✔ The ×3 revert is now complete** (`PT-1825`, commit `f408708`) — **all nine ion variant
rows and all six Bowcaster rows corrected to ×2.** Verified by reading the file at that
commit directly: **the only ×3 rows remaining are the seven nameless `prop*` placeholders**,
which this catalogue already excludes. **The Bowcaster was extended into scope on the
reasoning that ×3 is unsupported by either game's raw data** — K1's `Bowcaster` base row
carries `crithitmult` 2 — **which is the same reasoning the ion revert rested on.**

*Recorded for the history, since the flag-resolution convention keeps what was raised:* the
nine ion variants were —

    Ion Blaster   w_blaste_10   Aratech Droid Oxidizer
                  w_blaste_21   Aratech Ionmaster
    Ion Rifle     g_w_ionrfl02  Bothan Droid Disruptor
                  g_w_ionrfl03  Verpine Droid Disruptor
                  w_brifle_02   Ion Carbine
                  w_brifle_15   Bothan Droid Disruptor
                  w_brifle_20   Verpine Droid Disruptor
                  w_brifle_29   Verpine Droid Disintegrator
                  g1_w_ionrfl01 (the corrupted-name row, Flag 4)

— **all now ×2**, along with the six Bowcaster rows.

**The family headings above state ×2 throughout and always did**, so nothing in this
catalogue changed when the fix landed.

**⚠ Flag 2 — `ITEMS-01`'s ion rows are internally inconsistent, which is how this was
caught.** Two base Ion Rifles (`g_w_ionrfl01`, `w_brifle_07`) already read ×2 while their
own variants read ×3. **That inconsistency is corroboration for the ruled ×2**, and it is
why Ion and Sonic rifles cannot be separated by stat line alone once the fix lands — both
become `1d10, 20 ×2`. **Damage type is the discriminator, and it is recorded per entry.**

**⚠ Flag 3 — 30 of 122 descriptions are truncated mid-sentence in `ITEMS-01`**, several at
identical points — the disruptor description cuts at *"disruptors igno"* in three separate
items. **This is an extraction defect, not a source one:** a character limit applied during
extraction. **Each affected entry is marked in place** rather than completed by invention.
**A re-extraction would fix all thirty at once.**

**⚠ Flag 4 — a fourth instance of the corrupted Name-field pattern.** `g1_w_ionrfl01` is an
ion rifle whose Name field reads **`Mastercraft: Armor II`** — an armour upgrade's name on
a weapon's resref. **Left unnamed in the catalogue rather than given an invented one.**
Same shape as the Baragwin, Weapon Master and spike-mount cases.

**⚠ Flag 5 — `Sniper Rifle` and `Marksman Rifle` have one entry each**, both `⚠ AUTHORED`
(`a_w_snprrfl01`, `a_w_mrksmnrfl01`). **They are the only families here with no extracted
members**, which is expected — both were added by ruling (`PT-1473`, `PT-1783`) and no game
item carries them.

**Closed from the earlier draft:** `Hold Out Blaster`'s naming flag (`PT-1477`) and the
Sniper Rifle catalogue gap, both resolved above.

`Hold Out Blaster`'s earlier "could not be confirmed" flag is closed; `PT-1477` explains
both why it existed and why searching for the hyphenated form missed it.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 10 internal citations from the body**, plus the five-flag section. **The
catalogue itself was almost untouched:** 124 entries, 14 family headings and all 29
truncation markers survive unchanged.

**⚠ The `⚠ AUTHORED` marking became the chapter's most important rewrite.** The Sniper
Rifle and Marksman Rifle section was headed *"Sniper Rifle — ruled, and now catalogued"*
and described a gap being closed. **A reader does not know there was a gap.** The section is
now headed **"The two rifles this game added"** and opens by saying plainly that **neither
weapon exists in either game** and both were written for this book. **That is the
ours-versus-extracted discipline stated where a reader meets it**, rather than signalled by
a ruling number.

**The price caveat became advice rather than a note to ourselves.** It read *"open to a
second look if it doesn't sit right in play."* It now says the 800 credits is **"the kind
of number a table should feel free to adjust."**

**⚠ The ceiling paragraph lost a stale-value confession it should never have carried.** Two
sentences explained that the figures had previously been wrong, why, and which rulings
fixed them. **A reader needs the comparison, not its repair history.** What replaced it is
a fact the old paragraph only implied: **ranged weapons add Dexterity, so the gap closes
for a character built that way — but it closes by the shooter's ability, not the weapon's.**

**The corrupted-name entry now warns a reader rather than counting instances.** It said
*"fourth instance of the corrupted-Name pattern."* It now says **this item has no usable
name**, its name field holds an armour upgrade's name, **the weapon is real and the name is
not.**

**✔ Resrefs kept throughout**, per Chapter Two's finding, and the families note now points
at Chapter Two's caution rather than restating the resref lesson.

**✔ The standing orphan check was run** after every removal — the new step adopted in
Chapter Two. **Zero dangling cross-references.** The `KillBlaster`'s crystal note was the
one at risk; it cited a crystal ruling and now points at Chapter Six, which is where
crystals are actually catalogued.

**⚠ Deliberately NOT loosened.** All 14 base weapons keep their dice, threat ranges and
ranges; both long rifles keep their full treatment including the perception extension's
three properties; the 122-item catalogue is untouched; and **the 50 excluded entries are
still listed with the reason for each exclusion.**

---

# Chapter Four — Lightsabers

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: DRAFT.** Split from the combined melee/ranged/lightsabers chapter per
MAIN's ruling. **Base table checked against the raw `.2da` files directly** —
`data/k1_baseitems.2da`, `data/k2_baseitems.2da` — **not `ITEMS-01`'s markdown copy**,
whose merged `K2+K1` tag masks the two games' different values for these three weapons.
**Rulings:** `PT-1472` (training sabers take crystals), `PT-345` (the crystal subsystem),
`PT-1747` (the stale Vibrosword comparison).

**⚠ The `K2+K1` tagging finding, in its internal form:** `ITEMS-01` tags all three
lightsaber resrefs `K2+K1` and shows **only K2's numbers** under that combined tag
(`2d8`/`2d10`/`2d12`). **A `K2+K1` tag in that catalogue does not mean the two games share
a value — it can mean the extraction recorded only one game's number for a resref present
in both.** Confirmed for lightsabers against the raw `.2da`; **not confirmed or ruled out
for anything else tagged the same way.**

**⚠ The stale rationale, recorded because it was deliberately not rewritten in the
chapter:** `EQUIPMENT-01 §4b`'s reason for preferring K1's dice had two parts. *"Our
campaign is 3956 BBY and K1 is the era"* stands. *"A Vibrosword is `2d6`, so a K1
lightsaber sits exactly one die step above it"* **is stale twice over** — Vibrosword is
`1d12` since `PT-1747`, and even before that the comparison ran against the *wrong*
standard-Lightsaber die of `2d10`, which was never one step above `2d6`. **The `PT-1844`
pass removed the sentence from the chapter entirely rather than repairing it**, since the
era reason carries the choice alone.

The lightsaber-damage-ability flag from Chapters One through Three — genuinely this
chapter's own subject now, not just carried for continuity. `EQUIPMENT-01 §4b` itself
raises the same caveat independently: *"lightsabers are not melee weapons,"* a
statement the source makes about upgrades and criticals rather than damage, which is
exactly why treating lightsabers as melee-for-damage is a working assumption rather
than a confirmed rule. Two independent paths to the same open question, not two
separate ones.

New this chapter: the K1/K2 rationale paragraph (editorial), and the `K2+K1` tagging
caution above, which isn't this chapter's to resolve but felt worth surfacing where it
was found.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 12 internal citations from 103 lines**, the densest concentration in the Armory
so far.

**⚠ The raw-file citation survived, exactly as predicted, and it reads well.** The die
correction is the chapter's centrepiece, and the approved method says a citation to the
games' own data stays. **It does — but the framing changed from a document-versus-document
dispute into a warning a reader can use:**

> **You will find the standard Lightsaber's K1 die quoted elsewhere as `2d10`. It is
> `2d8`.** The figure above was read out of KOTOR 1's own weapon table — row 8, label
> `Lightsaber`, two dice of eight — **not from any summary of it.**

**The internal document that had it wrong is gone; the game table that has it right
stayed.** That is the method working as intended.

**⚠ The `K2+K1` methodological note became a reader caution**, and this is the pass's best
gain here. It was a warning to whoever next reads the item catalogue. **It is now a warning
to whoever next builds a character:** where a weapon appears in both games it is easy to
assume both give it the same numbers, these three prove otherwise, and **a summary listing
a weapon once without saying which game it quotes will silently give you one game's value
for both.** Ending with: **if a weapon matters to your table and appears in both games,
check both.**

**⚠ The Training Lightsaber got the authored-marking treatment** approved at Chapter Three.
It read *"a fourth entry, authored rather than extracted"* — accurate and meaningless to a
reader. **It now opens: this weapon does not exist in either game; it was written for this
book.**

**And its unsettled threat range became advice.** The old text named the two documents that
disagreed and declined to choose. **The chapter still declines — but now tells a Gamemaster
that `20` is the safer ruling**, which is what the old note's own reasoning implied and
never said.

**⚠ Deliberately NOT loosened.** Both games' dice for all three lightsabers survive, the
K1-versus-K2 table is intact, the die-progression argument is unchanged, all three training
sabers keep their dice, and the crystal subsystem still points at Chapter Six with Rubat and
the 104-crystal count.

---

# Chapter Five — Armour

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED.** Source is `ITEMS-02` — **already the primary-source
catalogue**, converted from the game files under `PT-339` (dice), `PT-341` (Massive
Criticals), `PT-308` (tiers), `PT-327` (unique), `PT-345` (crystals), `PT-349`
(Upgradeable) and `PT-384` (the feat remap). **It did not need the cross-check against a
more primary source that caught real errors in Chapters Two through Four — it largely *is*
that source.** `PT-980` priced the Dark Padawan Robe down from 900 to 700.

Same lightsaber-damage flag, unaffected by this chapter. `DecreaseAC` closed above —
confirmed, not a real gap. Still worth stating plainly: this chapter samples five of
173 items rather than auditing the full catalogue line by line, the way
the eleven-row weapon tables in Chapters Two through Four could be. A category count
and a representative sample is the right grain for a browsable-reference chapter; a
full 173-item transcription would belong to `ITEMS-02` itself, not to prose built on
top of it.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 11 internal citations from 71 lines**, almost all of them in a single opening
paragraph that existed to explain this chapter's provenance to a colleague.

**⚠ That paragraph is the clearest example yet of a citation load with a real point buried
in it.** It listed seven ruling numbers and two document names to say that this chapter's
source *"largely is"* the primary source rather than a summary of one. **A reader cannot
use any of that — but the conclusion matters to them, because it tells them how far to
trust the numbers.** It now reads:

> **One difference worth knowing, because it affects how much to trust these numbers.** The
> armour figures in this chapter were converted straight from the games' own item files.
> **They did not pass through a summary first**, which is where the errors corrected in
> Chapters Two, Three and Four came from.

**Same claim, and it now earns its place** by telling a reader why this chapter is less
likely to be wrong than the three before it.

**⚠ The `DecreaseAC` explanation kept its game-data citations and lost its method
narration.** The two `.2da` file names stayed on the approved rule — they are the games'
own tables — **but the passage no longer walks through the resolution as a procedure.** It
gives the worked example (`Light Combat Suit`: base armour 4, cap +5, penalty applies to the
armour component, **true protection `+3` with the full `+5` cap kept**) and then states the
general rule in one sentence.

**⚠ The Dark Padawan Robe repricing got the authored-marking treatment.** It read *"an owner
ruling rather than an oversight… by ruling."* **A reader does not know what an owner ruling
is.** It now says plainly: **one price in this chapter is deliberately not the games' own**,
because two items that do exactly the same thing now cost the same. **That is this game
changing something on purpose, and a reader is told so.**

**⚠⚠ A content gap noticed during the pass and NOT addressed by it.** **This chapter
samples five of 173 items** where Chapters Two and Three carry full catalogues.

**✔ RULED — `PT-1770` already required this, retroactively.** MAIN checked: the
full-catalogue standard was not a convention Chapter Five was written before, it was **an
explicitly retroactive rule that already governed this chapter and was never enforced on
it.** So this is compliance, not a new decision.

**⚠⚠ OUTSTANDING TASK — expand Chapter Five to the full 173-item catalogue**, matching
Chapters Two and Three: six categories, Base/Advanced where it applies, ordered by tier.

**Sequenced AFTER the `PT-1844` sweep completes, by AUTHOR's call, for a practical
reason:** writing the 173 entries fresh means **they are born compliant with both standards
at once.** Expanding first would produce 173 entries that then need a de-jargoning pass of
their own — the same work twice. **Recorded here so it cannot be lost between tasks.**

**⚠ Deliberately NOT loosened.** All six category counts, the 173 total, the nine
both-games items, every representative entry with its armour value, the Dark Padawan Robe's
two prices, and the `DecreaseAC` worked example's exact figures all survive.

---

# Chapter Six — Upgrades and the Upgrade Tree

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: DRAFT.** Sources `ITEMS-03` (164 items) and `ITEMS-09` (118 rows, *"the
upgrade tree"*, refiled at `PT-781` from material originally scattered across the `plot`,
`device`, `sensor`, `clothing` and `creature` categories). `PT-345` governs crystals.

Same lightsaber-damage flag as every chapter so far. New here: the deferred
unique-weapon mechanic is explained rather than mechanically resolved, and how common
its four-resref shape is across the rest of the catalogue is an open, unscoped
question rather than a closed one.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 7 internal citations from 96 lines.** Four were section headings that carried a
source document's name as a subtitle, which told a reader nothing and made the contents page
unreadable.

**The unique-weapon survey question became a reader-facing caveat.** It read as a scoping
note about what *"hasn't been budgeted for."* It now tells a reader what to do with the
uncertainty: **treat the pattern as demonstrated for the two weapons named and unproven
elsewhere.**

**⚠ And the pass caught an inaccuracy I introduced myself, two chapters ago.** Chapter
Four's crystal pointer — written during this task's Chapter Four pass — said **"Chapter Six
catalogues 104 crystals."** **It does not catalogue them. It describes them.** Corrected to
*"covers"*. **The forward-reference check exists for exactly this, and it caught a false
claim of my own making rather than an inherited one.**

## ⚠⚠ And the pass measured the real scope of the `PT-1770` gap

**Chapter Five is not an isolated case.** Counting catalogue entries against claimed item
totals across every item chapter:

| Chapter | Entries present | Items claimed |
|---|---|---|
| Two — melee weapons | **62** | complete |
| Three — ranged weapons | **124** | complete |
| **Five — armour** | **0** | **173** |
| **Six — upgrades** | **0** | **164** + 118 rows |
| **Seven — droid equipment** | **0** | **135** |
| **Eight — worn gear** | **0** | **241** |
| **Nine — usable items** | **0** | **58** |
| **Ten — quest and miscellaneous** | **0** | **20** |

**Six chapters carry a category table and a handful of representative entries instead of a
catalogue. Roughly 791 items are uncatalogued.**

**Verified by inspection, not by pattern-match** — Chapters Eight and Nine were opened
directly to confirm they use the same category-table-plus-sample shape as Chapter Five
rather than a format the entry count was failing to recognise.

### ✔ RULED — the catalogue-completion task, scoped and sequenced

**All six chapters get full catalogues. No exceptions carved out for the smaller ones**,
and none for the larger. `PT-1770` was already decided; the size of the gap is a
sequencing question, not a reason to revisit whether the rule applies.

**Sequenced after `PT-1844` completes across all sixteen chapters**, not interleaved — so
every new entry is born compliant with both standards and nothing is written twice.

**Order within the task: smallest first**, for momentum, the same shape the original
sixteen chapters were written in:

    1.  Ten — quest and miscellaneous        20 items
    2.  Nine — usable items                  58 items
    3.  Seven — droid equipment             135 items  ⚠ WRONG — it is 129
    4.  Six — upgrades                      164 items + 118 rows
    5.  Five — armour                       173 items
    6.  Eight — worn gear                   241 items

**~791 items total.** Comparable in size to writing the Armory's sixteen chapters in the
first place.

---

# Chapter Seven — Droid Equipment

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED.** Source `ITEMS-04`, a primary-source catalogue on the same
footing as `ITEMS-02` and `ITEMS-03` — no cross-check against a more-primary source needed,
unlike Chapters Two through Four.

Same lightsaber-damage flag, unaffected. The four-way split proposal above was
approved and the other three chapters are drafted.

**The `spike-mount` corrupted-Name row is resolved.** It is `Advanced Droid Interface`
(`g1_i_drdcomspk01`, Tier 3, 9,000 credits), gated behind `Droid Upgrade 3` and granting
skill 7 in Awareness, Computer Use, Demolitions and Security — *"a self-contained
artificial intelligence system... to provide them with additional resources useful in
the bypassing of computer and conventional"* security. The four skill bonuses, which had
also been showing as unmapped subtypes, resolve cleanly and match the item's own flavour
text. Third instance of that corruption pattern, and the third to resolve the same
way — by reading the raw file rather than the markdown copy.

## ⚠ The stale scoping proposal, removed from the chapter

**This section sat in the chapter as an open question when it had already been answered.**
It proposed splitting a combined outline row into four chapters and closed with *"not
drafting the other three until this is confirmed"* — while the flags directly beneath it
recorded **"the four-way split proposal above was approved and the other three chapters are
drafted."**

**That is `PT-961`'s shape in this project's own book**: a resolved proposal left standing
as though still pending, with its own resolution sitting twenty lines below it. **The fifth
instance of that pattern found during this work, and the first in something I wrote.**

Preserved in full:

## A scoping proposal, not yet decided

**The outline currently bundles `ITEMS-04` through `08` — droid equipment, worn gear,
usable items, and quest/miscellaneous items — into one chapter.** Having looked at all
five, they aren't one category the way Armour's sub-categories were:

- **Droid equipment** (this chapter) — its own coherent, thematically distinct set.
- **Worn gear** (`ITEMS-05`, 241 items — belts, forearms, gauntlets, implants, masks) —
  the single largest catalogue after weapons, and mechanically its own thing: passive
  body-slot gear, not weapons or armour.
- **Usable items** (`ITEMS-06`, 58 — adrenals, medical, trap kits) — active consumables,
  a different kind of object entirely from anything worn or equipped.
- **Quest and miscellaneous items** (`ITEMS-07` + `ITEMS-08`, roughly 60 combined) —
  both small enough to share one chapter, and both are genuinely miscellaneous rather
  than a coherent category in their own right.

**Proposing four chapters rather than one**, same reasoning as the Melee/Ranged/
Lightsabers split — different mechanical shapes, and a single chapter covering all
five `ITEMS` files' combined ~500 items would strain this book's own browsable-
reference identity. Not drafting the other three until this is confirmed.

---

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 6 internal citations, and the stale proposal section above**, which was a third
of the chapter's length.

**The opening now says what the chapter is for rather than how it came to exist.** It
explained its own split from an outline row and named three source documents. It now opens:
**droids do not wear armour and cannot use most of what Chapters Two through Six catalogue,
and this chapter is what they get instead.**

**⚠ Removing the flags orphaned a live cross-reference, caught by the standing check.** The
category table's Spike-mount row pointed *"see below"* at a detail that lived only in the
flags. **That detail is genuinely reader-facing** — the best item in the category is
effectively unfindable by name.

**So it was restored into the chapter as its own section** rather than moved out: the
**Advanced Droid Interface**, `g1_i_drdcomspk01`, Tier 3, 9,000 credits, `Droid Upgrade 3`,
granting skill 7 in Awareness, Computer Use, Demolitions and Security — **with the practical
warning a reader needs: if you search the game files for this item by name you will not
find it, so search by code.**

**What stayed in the notes is the part that was never reader-facing:** that this is the
third instance of the corrupted-Name pattern, and that it resolved the same way as the
others — by reading the raw file rather than a markdown copy.

**⚠ Deliberately NOT loosened.** All eight categories and their counts survive, both
representative-entry tables are intact including the `Droid Desh Plating` `DecreaseAC`
cross-reference to Chapter Five, and the Advanced Droid Interface's full specification is
now in the book rather than in a footnote about it.

---

# Chapter Eight — Worn Gear

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED.** One of four chapters split out from a combined outline row.
Source `ITEMS-05`, a primary-source catalogue on the same footing as Chapters Five through
Seven.

Same lightsaber-damage flag, unaffected. Same unmapped-subtype question as above,
explicitly deferred rather than picked at piecemeal. Two categories (Belt beyond the
one sample, Gauntlets and Implant beyond their authored examples) not deeply sampled —
the same browsable-reference grain as Chapter Five's five-of-173, applied here to a
larger catalogue.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 6 internal citations from 62 lines.**

**⚠ The authored-item section got the Chapter Three treatment, and it was the most
important change here** — this is one of only two chapters that mix invented items in with
extracted ones.

It was headed *"Two of these categories mix original content in with the games' own items"*
and explained the `⚠ AUTHORED` mark by describing **the provenance discipline** — *"every
asset declares whether it's ours or extracted, and nothing ships without that
declaration."* **That is a statement about how this project works, offered to someone who
does not know this project exists.**

It is now headed **"Two items in this chapter do not exist in either game"** and says what
the mark means in use: **an invented item should never sit beside an extracted one as though
the two came from the same place**, and where you see the mark, **the item is this game's
own work rather than BioWare's or Obsidian's.**

**⚠ The unmapped-skill-subtype section was rewritten from a scoping note into a table
ruling.** It previously explained why the author was *not* resolving these — that it belongs
to a commissioned pass, and that duplicating effort would waste a slice. **All true, and all
addressed to a colleague.**

**A reader needs something else entirely: what to do when they meet one.** The section now
explains that the entry records a bonus and its size **but not which skill**, that it is a
known and separately-tracked problem, and that **until it is fixed a Gamemaster should
assign the bonus to whichever skill the item's description and slot most plausibly
support** — with `Safety Harness` named as the clearest example.

**⚠ Two directional errors caught by the standing checks**, one inherited and one mine.
The Forearm category compared itself to `ITEMS-04`'s droid shields; **it now points at
Chapter Seven**, where a reader can actually look. And my own rewrite said `Safety Harness`
was *"in the sample below"* **when the table sits above that section** — the same class of
error as the Timeline's Chapter Three *"Ossus below"*. **Third time a directional reference
has gone wrong in this task, and the third time the check caught it rather than luck.**

**⚠ Deliberately NOT loosened.** All five categories and their counts survive, both authored
items keep their full specifications, and the representative-entry table is unchanged.

---

# Chapter Nine — Usable Items

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED.** Second of four chapters split from a combined outline row.
Source `ITEMS-06`. **Medpac values are `PT-1` B3's deliberate replacement of the source
game's WIS/skill-scaled mechanic.**

Same lightsaber-damage flag, unaffected. Same unmapped-subtype deferral as Chapter
Eight — none of this chapter's own categories happened to carry one, but the
commissioned pass (once run) may still touch entries here.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 6 internal citations from 59 lines.**

**⚠ The medical section got the Chapter One treatment**, as the second of only two places
in the Armory where a value is knowingly not the source's own.

It was headed *"Medical — where a ruling deliberately replaces the source mechanic"* and
opened by explaining that this is *"not a contradiction to resolve"* — **which is an answer
to a question only someone auditing the corpus would ask.** A reader meeting different
numbers in the games does not think *contradiction*; they think **which one is right.**

It is now headed **"Medical items — where this game knowingly differs from the games"** and
opens by telling them directly: **you will find different numbers in the games, and the
difference is on purpose.** The comparison table's columns changed from *"Source game's own
mechanic / This game's ruling"* to **"What the games do / What this game does"**, which is
the same distinction without the word *ruling*.

**⚠ And the proportionality argument was kept in full, because it is the part that
justifies the change.** The games triple both base healing and the skill multiplier from
Medpac to Life Support Pack; **this game triples the average healing across the same three
items.** Different mechanic, same shape. **That reasoning is why the replacement is
defensible rather than arbitrary, and a reader deserves it.**

**Closed with the line the section was always making and never said:** *a medpac is a
medpac — in this game, who hands it to you does not change what it does.*

**Two smaller fixes.** The `Components` row pointed at the crafting rules by document name;
**it now points at Chapter Twelve**, where those rules actually live in this book. And the
`Antidote Kit` / `Squad Recovery Stim` paragraph described them by reference to *"the
earlier medpac ruling"* — **it now simply says they sit outside the three tiers**, with the
Squad Recovery Stim correctly characterised as **a different kind of thing rather than a
stronger medpac.**

**⚠ Deliberately NOT loosened.** All six categories and counts survive, the 30-item
cross-game overlap is kept, all three medpac tiers keep both the games' formula and this
game's dice, and the tripling argument is unchanged.

---

# Chapter Ten — Quest and Miscellaneous Items

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED.** Last of four chapters split from a combined outline row.
Sources `ITEMS-07` (quest) and `ITEMS-08` (other). **Authored content:** `Shock-arm`
(`PT-713`, `PT-712`, `PT-714`) and `Boots` (`PT-690`).

Same lightsaber-damage flag, unaffected. The category-count question and the
Shock-arm design are both closed above. Still open: the cross-reference worth someone
picking up later — Pazaak's cards exist here while its rules chapter is still
unplaced in Book Five.

## ⚠ The two count-correction histories, removed from the chapter

**Both were internal and both are preserved here.**

**Quest items:** the header once read **"154 items"**. `PT-781` moved 134 upgrade rows out
of the `plot` category into `ITEMS-09` — dropping `plot` from 147 to 13 — **and the header
was not updated until `PT-871` caught it.** True count: **20.**

**Miscellaneous items:** the file stated **42 items against a five-category sum of 69**.
**The header was wrong, not the arithmetic** — corrected to 69, matching the sum exactly.
**The same stale-header shape the quest catalogue had already shown**, in the same file
family.

**Also removed: the shock arm's redesign history** — that a free, auto-upgrading
T3-M4-unique version existed and was deleted, leaving one purchasable line at two price
points. **A reader needs the design that exists, not the one that did not survive.**

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 9 internal citations and two correction histories**, the heaviest combination
in the Armory.

**⚠ The authored section is the strongest ours-versus-extracted case in the book, and it
now reads like it.** It was headed *"Two of these five categories are original content, not
extracted from either game"* — accurate, and phrased in the project's internal vocabulary.

It is now **"Two categories here do not exist in either game"**, opening: **this is the
furthest this book goes beyond its source.**

**⚠ And the Boots justification became checkable rather than asserted.** It cited the ruling
and named the game's equipment table. **The table is game data and stayed** — but the claim
is now framed as something a reader can verify: **"That is not an oversight on this book's
part — it is verifiable in the games' own equipment table, which covers implant, head,
armour, hands, arms, weapons and belt, and nothing below the waist."**

**The shock arm's three consequences were pulled out of a citation-dense paragraph into
plain statements:** it occupies no weapon slot, cannot be disarmed, dropped or sold, and a
droid may still carry a blaster. **And the reason that matters — it is chassis hardware, the
same category a beast's claws belong to, so it never passes through the wield classes —
now also explains why droids being barred from melee weapons does not bar them from this.**
**That last connection was implicit in a ruling number and is now stated.**

**The pazaak note became a Gamemaster's instruction.** It described a rules chapter as
`UNPLACED` in another book. **It now says the cards are catalogued regardless, and a
Gamemaster who wants to run a hand has the props and will need to supply the game.**

**⚠ Deliberately NOT loosened.** Both authored categories keep their full specifications
including prices, dice and gating; all five miscellaneous categories and their counts
survive; and the quest-item categories are unchanged.

---

# Chapter Eleven — Tiers, Pricing, and Availability

*`PT-1844` pass. **This chapter was rewritten rather than edited**, because more of it was
addressed to the project than to a reader. The removed material is preserved below.*

**Chapter status: DRAFT.** Rulings: `PT-308` (loot tiers), `PT-327` (unique items),
`PT-384` (the feat remap, confirming `PT-352` was applied). Currency is
`STARTING-EQUIPMENT-01`, **not** `D-CURRENCY-01`.

## ⚠ The `D-CURRENCY-01` miscitation — removed from the chapter, still outstanding at the outline level

## ⚠ `D-CURRENCY-01` was miscited from the start — not this chapter's fault to fix quietly

**The outline's own row for this chapter, and separately Book Seven's Planetary Atlas
row for "currency and trade," both cite `D-CURRENCY-01` as the source. It isn't.**
Read the actual document: 217 lines, entirely about *which Atlas world-record source
governs* — a corpus-authority ruling for the Planetary Atlas's own data, unrelated to
in-game currency. The word "currency" appears exactly once, in a single aside about
*"the currency question"* being asked in the same letter as the actual subject —
incidental, not the topic.

**This isn't a gap, just a wrong pointer.** The real currency mechanic — credits as
the sole medium of exchange, starting purses, item costs — is already `RULED` and
held, in `STARTING-EQUIPMENT-01`: the Purse/Array choice (`PT-728`, *"the array may
contain what the purse could not afford... a player who takes the purse gets freedom,
a player who takes the array gets value"*), per-class starting credits, and the cost
columns already running through every `ITEMS` file in this book. **Both outline rows
citing `D-CURRENCY-01` should point to `STARTING-EQUIPMENT-01` instead — flagging this
for correction at the outline level, not just inside this one chapter.**

Same lightsaber-damage flag, unaffected. New here: the `D-CURRENCY-01` miscitation,
which needs fixing at the outline level in both Book Four's and Book Seven's rows —
not something one chapter file can close on its own. The loot-tier character-vs-area
question is named as undecided rather than resolved.

## ⚠⚠ A contradiction between two chapters, found and fixed by this pass

**Chapter Eleven said the loot-tier gate was undecided. Chapter Thirteen answers it.**

The old text read: *"What's still undecided: whether the tier gate keys off character level
or area danger. Area is the recommended direction… but that's a recommendation, not a
ruling."*

**`LOOT-01` resolved this, and Chapter Thirteen states it in full** — a character-level
table (1–5 → tier 1, through 21–30 → tier 4), **and** an area tier derived as
`max(encounter level, container difficulty)`, **and** world danger capping both. **The
answer turned out to be *both*, not one or the other.**

**So Chapter Eleven was carrying an open question that a later chapter in the same book had
already closed** — a reader consulting Eleven would have been told the system was unsettled
while Thirteen described it working. **Chapter Eleven now defers to Chapter Thirteen
instead.**

**That is the sixth instance of the self-description pattern found in this work, and the
second in a chapter I wrote.**

## ⚠ What the `PT-1844` pass changed in this chapter

**This was the heaviest rewrite of the task.** The chapter opened with a section about a
miscitation in the project's own outline, and three of its four remaining sections were
organised around ruling numbers.

**What survived, because it is genuinely reader-facing:** the unique-item rule in both its
halves, the 85-item count and — the best thing in the chapter — **how the 29 unflagged ones
were found.** *"There was one Nomi Sunrider, and she had one robe"* is now supported by the
rule it demonstrates: **if an item is named after a person, there was only ever one of it.**

**What was added, because the chapter's title promised it and the text never delivered it:**
**a section on currency.** The chapter was called *Tiers, Pricing and Availability* and said
nothing about money except inside the miscitation report. **It now states that credits are
the only medium of exchange, and that a character chooses between a purse and an array at
creation** — with the purse-versus-array line kept, since it explains the trade in one
sentence.

**What was reframed:** the feat remap. It was a confirmation that a data pass had been
applied. **A reader needs the consequence instead** — that where this book says an item
gates or grants something, **that came from the item itself** — with the four counts kept as
evidence.

**⚠ Deliberately NOT loosened.** Every figure survives: 85 unique items split 56 and 29, the
feat-property counts of 84, 120 and 9, and the purse-versus-array choice. **The one thing
genuinely removed is an open question that was no longer open.**

---

# Chapter Twelve — The Weapon Matrix and Crafting

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

*Sources: `WEAPON-MATRIX-01` (⚠ a derived view — `STARTING-EQUIPMENT-01 §2`, `§4a`, `§5`
are the record) for Part One, with `PT-760`, `PT-763`–`PT-767`, `PT-692`, `PT-702`,
`PT-714`, `PT-109`, `PT-567`. `CRAFTING-01` for Part Two, with `PT-203`, `PT-225`,
`PT-482`; `SKILL-RESOLUTION-01` for take-10 and `REST-AND-MEDITATION-01` for the downtime
period. Source tables `k2_itemcreate.2da`, `k2_chemicalcreate.2da`, `k2_upgrade.2da`.*

**⚠ Flag 1 — Part One restates a document that is itself a restatement, and I have said so
rather than hidden it.** `WEAPON-MATRIX-01` declares itself `DERIVED` and names
`STARTING-EQUIPMENT-01 §2`/`§4a`/`§5` as the record. **This chapter is therefore a third
copy**, and `D-W32`'s reasoning applies — *cite, do not restate, because copies drift.*
**The table is reproduced here because a player-facing book cannot send a reader to a rules
document for their own starting kit**, but the pointer is stated at the top of Part One and
the source governs on conflict. **A future sweep should check this table against
`STARTING-EQUIPMENT-01` directly, not against `WEAPON-MATRIX-01`.**

**⚠ Flag 2 — fifteen item names in this table resolve to more than one item.**
`WEAPON-MATRIX-01 §4` records it: *"which row each item name means — `§2c`, because fifteen
of these names resolve to more than one item."* **Chapter Three proves the point** — thirty
separate items are called some variety of Blaster Pistol. **A GM handing out a "Blaster
Pistol" at character creation should take the base row**, `g_w_blstrpstl001`, not whichever
variant a search returns first.

**⚠ Flag 3 — the crafting item catalogue is deliberately deferred and stays deferred.**
994 blueprints are extracted and joined; **turning them into readable entries is a separate
job** and is not attempted here. Also deferred at source: `k2_itemcreatemira`'s 214
character-specific recipes (companion content, and there is no companion system yet) and
the 99 upgrade rows whose blueprints live in module archives rather than `templates.bif`.
**This chapter documents the system, not the recipe list.**

**⚠ Flag 4 — the recipe count in circulation is 73 and the true figure is 68.**
`CRAFTING-01` corrects it in place, but **73 is the number printed on the source table** and
will keep resurfacing. **The five removed are the HK parts above**, which are a droid rather
than recipes.

**Not a flag, but worth stating: nothing in this chapter needed the base weapon dice.**
Part One names weapons; it does not restate their stat lines, which Chapters One through
Four already carry. **That insulates it entirely from the ranged-dice question** that
stopped Chapter Three's catalogue.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 17 internal citations from 379 lines**, plus the four-flag section. **The
highest raw count of any chapter in the task**, though most were single ruling numbers
attached to otherwise clean sentences rather than dense passages.

**⚠ The derived-view warning was the important one.** Part One opened by quoting
`WEAPON-MATRIX-01`'s own status line — *"THIS DOCUMENT RESTATES `STARTING-EQUIPMENT-01`…
THOSE ARE THE SOURCE; THIS IS THE VIEW"* — and explaining that this chapter is therefore a
third copy.

**All true, all internal, and the reader-facing half is one sentence:** **the Player's
Handbook is the authority on starting equipment, this is a summary of it, and where the two
differ the Player's Handbook is right.** A reader does not need to know how many copies
deep the summary is; they need to know which one wins.

**⚠ The feat-versus-profession correction was re-pointed at the reader.** It read *"`PT-764`
corrects a mistake worth understanding"* — a mistake *this project* made. **The reader's
version of that mistake is different and more likely:** it is tempting to read *"two Heavy
Blasters"* as something the feat alone provides. **It is not.** Same correction, aimed at
the person who will actually make it.

**The `hkpart` entries now point at Chapter Fourteen** rather than at the ruling that
deferred droid construction — **which is where a reader can actually follow them.**

**The take-10 rule, the DC ladder, the downtime period and the droid-construction
permissions all lost their citations and kept their content**, including the Machinist's
exclusive right to build *for another character*, which was corrected during this same task
at Chapter Fourteen.

**⚠ Deliberately NOT loosened.** All thirteen standard classes, six Force classes and nine
droid arrays keep their full four-column entries; the `Brawler`'s empty row keeps its
explanation; the ceiling ruling keeps both weapons and both prices; every crafting DC,
skill reassignment and implant split survives; and **the five `hkpart` entries are still
named individually.**

---

# Chapter Thirteen — Loot

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

*Sources: `LOOT-01`, with `PT-307` (the bands, ported), `PT-308`/`PT-309` (the tier gate,
authored), `PT-323` (party composition), `PT-327` (unique items), `PT-404` (world danger),
`PT-651` (every item carries a tier), `PT-655` (party level), `PT-666` (authored versus
generated), `PT-912`/`PT-922` (named sites). `SKILL-RESOLUTION-01` for take-10;
`PARTY-01 §2` for party level; `ITEMS-01`–`08` for the tier data.*

**⚠⚠ Flag 1 — the band-to-table mapping is an inference, and the source document says so.**
This is the largest open item in the chapter. `PT-307` **read the constants out of
`a_give_treas`, not the control flow** — so the band *thresholds* (60/70/80/90) are
verified, but **which band draws from which list is unverified** until someone disassembles
the script properly.

**Everything above is written as though band 5 draws the best item on the table**, which is
the natural reading and matches observed play. **It is not confirmed.** If the mapping turns
out to be different, the bands table stands and only the interpretation moves.

**⚠ Flag 2 — every item carries a tier, and the count in circulation is stale.** `PT-651`
closed this: **1,385 rows across `ITEMS-01`–`08`, zero blanks** — tier 1: 634, tier 2: 427,
tier 3: 213, tier 4: 111. **The figure of 994 still appears in places** and is the blueprint
count, not the item count. `LOOT-01` notes the drift against itself: *"the corpus grew past
it and the paragraph did not."*

**⚠ Flag 3 — `LOOT-01` carries a duplicated paragraph with a broken cross-reference.** Its
`§7b` states *"Procedurally generated areas are not covered by ."* — the reference is
missing entirely — and then repeats the same paragraph immediately with the reference
filled in as *"section 4"*. **The first copy should be deleted.** Same shape as the
`EVENTS-01` heading defect from the Galactic Timeline: an edit that added a corrected
version without removing the broken one. **Reported, not fixed — `LOOT-01` is a rules
document.**

**⚠ Flag 4 — the named-site count appears twice with different values.** `PT-912` records
**45 sites across 31 worlds**; `PT-922` records **47 across 32**, hand-curated, delivered.
**Both sit in the document.** The later supersedes under `§3b`'s later-wins rule and this
chapter uses **47 / 32** — but a reader meeting 45 first has no way to know it is
superseded. **Same class as the Timeline's stale `"ranking fifth"` numeral.**

**⚠ Flag 5 — the world count does not match the Atlas's.** `LOOT-01` reports **288 worlds**
carrying a `danger` value; `PT-1705` establishes that `data/extracted/worlds.json` holds
**301 world entries** — a figure it explicitly corrected from 290 *"before it became the
working number."* **Thirteen worlds are unaccounted for.** They may simply lack a danger
value, in which case the fallback is party level and nothing breaks — **but the chapter
cannot say so, because no held source states it.** Worth one check by whoever owns the
Atlas.

**Not a flag: `§7` and `§7b` state `PT-651` twice in near-identical terms.** Harmless
duplication rather than contradiction, but it is the same edit pattern as Flag 3 and the
two were probably introduced together.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — only 4 internal citations from 308 lines**, the lightest body load of any Armory
chapter. **This chapter was written late and already spoke to a reader.**

**⚠ But Flag 1's reader-facing half was promoted into the chapter, and that is the
important change.** The band-to-table mapping being an inference is **not a project
housekeeping note** — it affects how every loot roll in a campaign resolves, and a
Gamemaster is entitled to know which part of the system is certain and which is inferred.

The chapter now carries it directly, immediately after the bands table:

> **One honest caveat about the bands.** The roll thresholds above — 60, 70, 80, 90 — were
> read directly out of the game's own script and are certain. **Which band draws from which
> list is an inference**… **If that turns out to be wrong, the bands stand and only their
> mapping moves.**

**The project-facing half stayed here:** that the reading came from constants rather than
control flow, and that settling it means disassembling the script properly.

**That is the split-by-audience default doing exactly what it was adopted for — and this is
the case where burying the caveat would have mattered most**, because Chapter Eleven now
defers to this chapter for the whole tier system.

**⚠ And the authority Chapter Eleven handed over was preserved rather than weakened.** The
sources section states plainly which half of this system is KOTOR 2's and which is this
game's addition: **the roll and its bands are ported unchanged; the tier gate, the
`Security`-DC ladder, the world-danger ceiling and the named-site override are all new.**
The `376 sampled` evidence for KOTOR having no lock difficulty at all is kept, because it is
what makes the authored half defensible.

**Three smaller fixes.** The `Atlas` references now name the **Planetary Atlas** as a book in
this set rather than a data source; the `danger` **field** became a **rating**; and the
take-10 and party-level rules lost their document citations while keeping their content
exactly.

**⚠ Deliberately NOT loosened.** Every threshold, tier boundary, DC band, formula and count
survives — including `area tier = min( max(encounter, container), world danger + 1 )`, the
180-of-288 constraint, the 47 named sites, and both unique-item halves.

---

# Chapter Fourteen — Droid Construction and Upgrade

*Original source line, as it stood before the `PT-1844` pass:*

> *Sources: `DROID-CONSTRUCTION-01` (`PT-572`, `PT-607`–`PT-613`, `PT-225`, `PT-558`,
> `PT-594`, `PT-598`, `PT-599`, `PT-609`, `PT-953`) and `DROIDS-UPGRADE-01` (`PT-274`,
> `PT-316`, `PT-323`, `PT-577`, `PT-616`, `PT-654`). `CLASS-ROSTER-01` for the
> prestige-class check. `DEATH-AND-DIFFICULTY-01 §5b` for rebuild by difficulty mode.*

## Flags, carried from review

**⚠⚠ Flag 1 — this chapter contradicts Chapter Twelve, and Chapter Twelve has the weaker
source.** `CRAFTING-01` states the `Machinist` *"is the **only class** that can build a
droid — `PT-225`"*, and **Chapter Twelve repeats that.** `DROID-CONSTRUCTION-01 §4` says
otherwise: **Machinist, Droid Master and Engineer may all build**, and explains the
relationship — *"`PT-225` is explicit that construction belongs to the Machinist, and
`PT-572` does not take it away — it **extends** it to the two classes whose premise is
droids."*

**`PT-572` is the later and more specific ruling, and it is the one this chapter follows.**
`CRAFTING-01`'s sentence was true when written and was not updated when `PT-572` extended
it — **`PT-961`'s shape again.**

**✔ Fixed.** Chapter Twelve now reads that the Machinist is **the only class that can build
a droid *for someone else***, and states that `PT-572` extended building itself to
`Droid Master` and `Engineer`. **Both citations were verified against `PT-225`'s own
heading and `DROID-CONSTRUCTION-01`'s reconciling text before the edit.**

**⚠ Flag 2 — `DROID-CONSTRUCTION-01 §6` uses part names that `PT-612` retired.** The
rebuild section reads *"the **Motivator**, **Processor Core** and **Power Cell** are
destroyed"*. But `PT-612` **renamed `Motivator` to `Control Cluster`**, uses **`Droid
Processor`** rather than *Processor Core*, and **withdrew `Power Cell` entirely** — *"the
droid quest has no power component and we should not invent one."*

**So §6 lists a part that no longer exists.** This chapter states the three current parts
instead. **Reported, not fixed.**

**⚠ Flag 3 — and the same section carries a figure from the superseded flat-cost model.**
§6 gives the rebuild cost as **2,800 credits** and *"one day, regardless of chassis"*. But
`PT-608` replaced the flat 2,800 with the tiered ladder — **700 / 1,400 / 2,800.** 2,800 is
now the **heavy-tier** figure only; **rebuilding a Remote should cost 700, not 2,800.**
This chapter states it as *"its parts bill"* rather than repeating the stale number.
**Same edit-lag as Flag 2 and probably the same moment.**

**⚠ Flag 4 — the Armory references a class the Player's Handbook does not contain.**
`Droid Master` appears in this chapter's build permissions and in the bay-grant ladder, and
`CLASS-ROSTER-01` lists it among the **prestige** classes. **`PT-1705` moved prestige
classes to the Advanced Player's Guide**, so a reader of the Armory and the PHB together
will not find it. **Not an error — a cross-book reference that wants a pointer** when Book
Eight exists.

**⚠ Flag 5 — `DROIDS-UPGRADE-01` documents its own staleness and leaves it.** Its closing
paragraph reads: *"`LOOT-01` answered this in the same words as the worry — 'a party with no
droid gets nothing' — **and this paragraph never moved.**"* The document knows the text is
superseded, says so, and keeps it. **Harmless here because the two agree**, but it is the
third instance in two chapters of a rules document carrying a retracted or superseded
passage alongside its replacement.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 13 internal citations from 407 lines**, plus the `Status: DRAFT, for review`
header and its *"third of the Armory's four remaining chapters"* build-state claim, which
told a reader nothing and would have been wrong within the week.

**⚠ Flag 3's reader-facing half was promoted, and it is the change that matters most.** The
rebuild section said a destroyed droid *"costs its parts bill"* — true, and useless at a
table, because a Gamemaster mid-session needs a number. **The chapter now states all three:
700 light, 1,400 medium, 2,800 heavy**, with the two worked cases the flag itself supplied —
**an Assassin rebuilds for 2,800 against 6,900 to build fresh; a Remote rebuilds for 700.**

**That was the flag's whole point.** The stale figure in `DROID-CONSTRUCTION-01 §6` is a flat
2,800 for every chassis, which over-charges a Remote fourfold. **Stating the ladder in the
chapter closes the reader's exposure to it regardless of when the rules document is fixed.**
The project-facing half — that §6 is still stale — stayed here.

**⚠ Flag 4's reader-facing half was promoted too.** `Droid Master` is used twice in this
chapter and does not appear in the Player's Handbook. The chapter said *"see Flag 4"* — a
pointer to a note that has now moved out of the book entirely. **It now says plainly that
prestige classes live in the Advanced Player's Guide and that a reader with only the
Player's Handbook will not find the class there.** The project-facing half — that this wants
a real cross-book pointer once Book Eight exists — stayed here.

**⚠⚠ A real content find, reported rather than papered over: the fifth crafting-bench
entry.** Chapter Twelve identifies **five** entries that are not recipes, `hkpart01` through
`hkpart05`, and says all five belong in Chapter Fourteen. **This chapter built from four.**
The opening paragraph named four and called them five.

**`hkpart05` — the HK Protocol Pacifist Package — has no ruling anywhere in the corpus.** A
search of the rules documents and the ledger returns nothing but Chapter Twelve's own
listing. **So there is no crunch to borrow and none was invented.** The chapter now names the
part, says it belongs to KOTOR 2's rebuild of one particular droid rather than to general
construction, and states plainly that it has no cost, no tier and no place in a build.

**⚠ This is a gap, not a fix.** If the owner wants the Protocol Pacifist Package to be a
buildable part, it needs a ruling; the chapter's current sentence is honest about its absence
and nothing more. **Raised for a decision.**

**⚠ One precision fix inside a rule, changing no rule.** The chassis-cap section read *"a
light chassis caps at six bays"* while the parts ladder four sections earlier sorts
`Astromech` as **medium**. **The cap applies to `Astromech` and `Remote` specifically**, so
the line now reads *"those two chassis cap at six bays, permanently."* **Same gate, same two
chassis, no longer contradicting the tier table on the same page.**

**Smaller rewrites.** The Vocabulator passage stated two rulings-made-from-lore and now
states the two facts themselves; the `LB-series` quote is kept and attributed to the setting
rather than to a ruling number. The three-tier parts shape is now attributed to the game's
own plating items, by resref — **`g_i_drdltplat001`–`003`, `g_i_drdmdplat001`–`003`,
`g_i_drdhvplat001`–`003`** — which is a stronger justification than the ruling number was,
because a reader can check it.

**Three passages lost their development history and kept their content.** The flat-2,800
problem is now stated as what a flat price *would* do rather than as what an earlier draft
did; the brain-first build order no longer mentions that a draft had it backwards; the
six-socket count no longer records that it was first read as four. **The corrections
themselves all survive, stated directly — which is the standing method for rulings that exist
because something is commonly got wrong.**

**⚠ Deliberately NOT loosened.** Every price, tier, DC, bay count, class grant, cap and
formula survives unchanged: the 700 / 1,400 / 2,800 ladder and its per-part breakdown, all
seven build-or-buy rows, the `Repair` DC ladder 15–30, one day per 1,000 credits, the junk
droid's half price / DC +5 / `−2` / natural-1 / `Droid Upgrade 1` ceiling, the six sockets,
the 3 / 6 / 9 bays, the whole class-grant table, the `Astromech`/`Remote` cap, and
`Juggernaut`'s exclusion by it.

---

# Chapter Fifteen — Starships and Space Combat

*Original source line, as it stood before the `PT-1844` pass:*

> *Sources: `STARSHIPS-01` (`PT-669`, `PT-670`, `PT-672`, `PT-673`, `PT-800`, `PT-825`),
> `SPACE-COMBAT-01` (`PT-791`–`PT-808`, `PT-819`, `PT-820`, `PT-879`), and
> `MOUNTED-COMBAT-01 §§7, 9` for the pilot/passenger split, the movement rule and the range
> bands. `CRAFTING-01 §5` for the base definition; `ENCOUNTER-01` for CR; `SKILLS-01` for
> `Pilot` and `Awareness`.*

## Flags, carried from review

**⚠⚠ Flag 1 — `STARSHIPS-01 §3` says space combat and ship stats are not built. Both are.**
Its *"What is NOT built"* list reads **`SPACE COMBAT — NOTHING`** and **`SHIP STATS —
NOTHING`**, with no ✓, while the same list marks travel time and the ship-as-base as closed.
**`SPACE-COMBAT-01` built both**: eight components at `PT-791`–`PT-808`, and ship stats
specifically at `PT-796` — Vitality `10 × CR`, Defence `10 + CR`, Speed 4.

**A reader consulting `STARSHIPS-01` alone would conclude this chapter's entire second half
does not exist.** **Reported, not fixed.**

**⚠ Flag 2 — `SPACE-COMBAT-01`'s own title contradicts its own status line.** The document
is titled ***"the plan, not the rules"*** and its status line immediately beneath reads
**"ALL EIGHT COMPONENTS BUILT."** The title is a fossil from when it was a plan. **Harmless
to anyone who reads two lines; misleading to anyone who reads one.**

**⚠⚠ Flag 3 — this chapter summarises four components rather than reproducing them, and
that is a judgement call worth your review.** Components 5 through 8 — upgrades, seats per
hull class, the unwinnable fights, enemy ships and boarding — plus the 24-part ship-parts
table and the specialist-parts material, run to several hundred lines of ruled content.

**Part Three names them and gives each its governing idea; it does not carry their tables.**
**My reasoning:** the Armory is an equipment book, and this chapter is already the longest
in it. **The enemy-ship roster and the ship-parts catalogue are catalogue material** of the
same kind Chapter Three carries for ranged weapons — **and they would be better as their own
chapter than as an appendix to this one.**

**Recommend a Chapter Sixteen** covering ship parts, specialist parts and the enemy roster.
**Say if you would rather it folded in here instead and I will expand Part Three.**

**✔ Resolved. Chapter Sixteen was approved and written**, and carries ship parts, specialist
parts, boarding and the enemy roster in full. **The `PT-1844` pass rewrote Part Three to
match**: it now summarises only the three systems that genuinely have no chapter of their own
— upgrades, seats per hull class, and the two unwinnable fights — and points the other four
at Chapter Sixteen by name.

**⚠ Flag 4 — three numbers in the combat system are flagged as unverified in their own
source.** `SPACE-COMBAT-01` marks them itself: **whether `Repair` at DC 20 is the right
number**; **`LINE UP`'s `+2`, which is authored with no antecedent** (*"half of `Aid
Another`, because it reaches every gunner rather than one target"*); and the **`EVASIVE`
check, which `PT-879` converted from an opposed roll** — the only one in the system — to a
flat DC. **All three are the kind of number that only play settles.**

**⚠ Flag 5 — `STARSHIPS-01 §4` is headed *"Recommendation, not yet ruled"* and this chapter
does not draw on it.** Recorded so a later reader knows the omission is deliberate rather
than an oversight.

**Not a flag, but the pattern is now worth naming.** This is the **fifth** rules document in
four chapters carrying a superseded or self-contradicting passage alongside its replacement
— after `LOOT-01`'s duplicated paragraph, `DROID-CONSTRUCTION-01`'s retired part names and
flat rebuild cost, and `DROIDS-UPGRADE-01`'s self-documented stale paragraph. **Each
instance is minor and every one was caught by reading the source rather than the summary.**
**A sweep for "documents that describe their own content as unbuilt" would likely find
more.**

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 11 internal citations from 480 lines**, plus the `Status: DRAFT, for review`
header, whose *"roughly 1,950 lines of source across three documents"* measured the
development record rather than the chapter.

**⚠ And that header carried a claim that had since become false.** It called this **"the
Armory's last chapter."** Chapter Sixteen was approved and written after it was drafted.
**Second chapter in this task whose status line had quietly gone wrong** — the same shape as
Chapter Fourteen's *"third of the four remaining."* **A status line is the part of a document
nobody rereads, which is exactly why it rots.**

**⚠⚠ Flag 4's reader-facing half was promoted, and it is the important change.** Three
numbers in the space-combat system are marked unverified in their own source, and a
Gamemaster running the system is the person who needs to know which three. The chapter now
carries them directly, right after the four-line summary of what each seat rolls:

> **Three numbers in this system that only play will settle.** Everything else in Part Two is
> a rule. **These three are rules with a question mark against them**, and a table that finds
> one wrong should change it rather than work around it — `Repair` at DC 20, `LINE UP`'s
> `+2`, and `EVASIVE`'s check.

**And the note draws the line rather than vaguely hedging the chapter.** It says explicitly
that these are the three least anchored numbers, that they are not suspected of being wrong,
and that **every other figure is either derived from the games' own data or falls out of
rules the rest of the book already uses.** A caveat that spreads doubt over a whole system is
worse than no caveat; this one is bounded to three lines.

**⚠⚠ Flag 3 is resolved, and resolving it turned up a real error in Part Three.** Part Three
opened with *"four further components exist in full and are summarised here rather than
reproduced; see Flag 3"* — **an orphan pointer into a note this pass was removing**, and
worse, **no longer true.** Chapter Sixteen now carries ship parts, specialist parts, boarding
and the enemy roster **in full, with their tables.**

**But it does not carry all four of the summarised components.** Upgrades, seats per hull
class and the two unwinnable fights have no chapter of their own and are genuinely summary
here. **So Part Three was split along the real line**: three systems summarised because they
are summaries, four pointed at Chapter Sixteen by name because they are there in full. The
heading changed from *"What else is built"* — a build-state description — to **"Three more
systems, in brief."**

**Five passages lost their development history and kept their content.** *"The project draws"*
the `HK-47`/`HK-50` distinction became the distinction itself; *"both shipped packages"*
became *"the two this game comes with"*; *"carrying capacity was killed and encumbrance
deferred"* became **"this game has no carrying capacity and no encumbrance rule at all"** —
which is what a reader needs and is a stronger statement, not a weaker one; *"the project
already parsed"* 205 creatures became **"the 205 creatures in KOTOR's own files"**; and *"the
owner's brief"* became the design statement itself, set as a pull quote, since it summarises
the whole of Part Two better than any paraphrase.

**⚠ One directional reference was repaired in passing.** *"That was the rule before this
system existed"* dated a rule against the project's own build order. It now reads **"as Part
One sets out"** — verified: the authored-loss rule is in Part One, above.

**⚠ The sources section states the honest proportion, which this chapter needed more than
most.** Almost nothing in Part Two came from the games: **KOTOR has no ship statistics
anywhere in its 637 data tables, and its space combat is a rail shooter with two verbs.** The
section says so plainly and then lists what is this game's — which is nearly all of it —
rather than letting the chapter's confident tone imply a source it does not have.

**⚠ Deliberately NOT loosened.** Every price in all three tables, the map scale, all three
range bands, the `−2` at LONG, the 90-degree turn and its `Pilot` DC 15 / DC 20 exceptions,
the half-Vitality turret loss, `Repair` DC 20, the beat-Defence-by-10 station hit, all three
pilot actions, all three co-pilot actions, `10 × CR` / `10 + CR` / Speed 4, the 21% mean
absolute error, the `2d8`–`5d8` turret ladder, and the fully statted `Ebon Hawk` all survive
unchanged.

---

# Chapter Sixteen — Ship Parts and the Enemy Roster

*Original source line, as it stood before the `PT-1844` pass:*

> *Sources: `SPACE-COMBAT-01` — Component 5 (`PT-797`), Component 7 (`PT-803`), Component 7a
> (`PT-805`), Component 8 (`PT-808`), Ship Parts (`PT-819`), Specialist Parts (`PT-820`), and
> the boarding-resolution ruling at `PT-1128`. Prices cross-checked against
> `STARSHIPS-01 §2a` and `§9` (`PT-800`).*

## Flags, carried from review

**⚠ Flag 1 — the parts list doubled and the earlier figure is still in the document.**
Component 5 specifies **three groups and "12 items to author"** — Engine, Frame, Weapon,
with `Accel` cut. **`PT-819` delivered six groups and 24 parts**, adding Shield, Turret and
Sensor. **That is growth rather than contradiction**, but *"12 items to author"* still reads
as current where it sits, and the true figure is **24 standard parts plus 6 specialist
parts — 30.**

**⚠ Flag 2 — the Turret group has its own price ladder and it is easy to miss.** Every other
group uses 15,000 / 40,000 / 90,000 / 180,000. **Turret parts are double throughout —
30,000 / 80,000 / 180,000 / 360,000** — which is why the full four-part conversion reaches
650,000. **Stated in the table above so a reader does not price a turret ring off the
standard band.**

**⚠ Flag 3 — two acknowledged gaps in the enemy roster.** The source names both:

- **No Mandalorian fighter is listed**, and **they fought a war.** The Basilisk fills the
  grunt role in the doctrine section, which may be the intended answer — but the roster
  table shows *none*, and the two are not reconciled in the document.
- **No Sith freighter is listed.** The note says *"they used captured ones"*, which is a
  reasonable in-fiction answer and leaves the table cell genuinely empty.

**⚠ Flag 4 — the Corellian hardpoint is the only part that breaks a structural rule, and
that is deliberate.** Every other part obeys *one per group*; the `CEC Modular Hardpoint`
permits a second from one group. **Recorded prominently because a rule with exactly one
exception is the kind of thing a later sweep "corrects" by mistake.**

**⚠ Flag 5 — boarding's resolution is explicitly a floor, and the source says so.** Boarding
hands off to ordinary ground combat with no new geography. **A real ship-interior map is
wanted and explicitly deferred** — *"the honest floor, not a ceiling."* **Recorded so the
simplicity reads as a decision rather than an omission.**

**Not a flag — the `Accel` group's fate is worth knowing.** The swoop table has Engine,
`Accel` and Frame; **`Accel` was cut** because *"acceleration matters in a race, where the
track is fixed and the clock decides. In a fight, speed is speed."* It **goes back on the
shelf for swoop racing, which is where it came from.**

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 8 internal citations from 370 lines**, plus the `Status: DRAFT, for review`
header, which explained the chapter's own commissioning: *"written on the recommendation made
at the end of Chapter Fifteen and approved."* **A reader does not need to know a chapter was
recommended before it was written.** What survives from it is the one part that was about the
book rather than the process — that this is catalogue material of the kind Chapter Three
carries, which is why it is a chapter and not an appendix.

**⚠⚠ Flag 3's reader-facing half was promoted, and it is the change that matters most.** The
faction table has two cells a Gamemaster will build an encounter from and be wrong about:
the Mandalorians read *none on the roster* for fighters, and the Sith have an em dash where
their freighter should be. **A blank cell tells a reader nothing about whether it is a gap or
a statement.** The chapter now says which, directly after the table:

> **Two cells in that table are gaps, not statements.** The Mandalorians have no fighter on
> the roster, and they fought a war. The `Basilisk war droid` does a fighter's job in the
> doctrine section below — **but a Basilisk is a ridden war droid rather than a starfighter,
> and the table still reads *none*. The two have not been reconciled.** … The Sith have no
> freighter, and that gap has an answer: **they used captured ones.**

**⚠ And the unreconciled one was left unreconciled.** The flag says the Basilisk *"may be the
intended answer"* — **may be is not is**, and this pass had no standing to close it. The
chapter states both halves and tells a Gamemaster who wants a Mandalorian starfighter
specifically that they are inventing one. **Naming the gap is the service; closing it by
assumption would have been the error.**

**⚠ Flag 5's reader-facing half was promoted too, and it had been attributed to a document a
reader cannot open.** The boarding rule read *"the source is honest that this is a floor
rather than a ceiling"* — **which asks a reader to trust a source they have never seen.** It
now says the thing itself: a real ship-interior map would be better, this game does not have
one, and **the handoff to ground combat always works and is not the last word.**

**⚠ Flag 1's number was promoted; its stale-source half stayed here.** The flag exists
because the parts list doubled and *"12 items to author"* still reads as current in the
source. **A reader has no exposure to that** — but they do benefit from knowing the list is
closed, so the chapter now states the total: **24 standard parts plus six specialist parts,
thirty, and there is nothing else to bolt to a ship.**

**⚠ A real content promotion from the "not a flag" note: `Accel`.** The swoop table has
Engine, `Accel` and Frame; this chapter has Engine and Frame and never said why. **A reader
who knows the swoop table would notice a missing group and have no explanation.** The
reasoning was sitting in the notes and is good, so it went into the chapter beside the Engine
table: *"acceleration matters in a race, where the track is fixed and the clock decides. In a
fight, speed is speed."* **`Accel` goes back to the swoop table it came from.**

**Flags 2 and 4 needed no promotion** — both were already stated in the chapter body, the
turret group's doubled price ladder in its own table and the Corellian hardpoint's
rule-breaking in a ⚠ line. **Their project-facing halves stayed here**, including Flag 4's
real point: a rule with exactly one exception is the kind of thing a later sweep "corrects"
by mistake.

**Three passages lost their development history and kept their content.** The shield ruling
no longer explains itself by which earlier rulings it threatened to reopen — **it states what
the rule is and what it keeps true**, one Vitality pool and no systems-officer seat. The
upgrade design principle and the specialist-part test both became statements of the principle
rather than quotations of a brief.

**⚠ The sources section draws the line this chapter most needed drawn.** Every part here is
authored — **KOTOR has no ship parts at all, only a swoop-bike table** — while every ship in
the enemy roster is real, and so are the manufacturer names the parts are built on. The
section says which is which, and names the one thing that is the chapter's own argument
rather than anyone's source: **that each navy's doctrine falls out of its lore rather than
out of its statistics.**

**⚠ Deliberately NOT loosened.** Every part name, effect and price survives: both price
ladders including the turret group's doubled one, the 650,000 four-part conversion, all six
specialist parts, the five untouched axes, the boarding gates, every roster row, all three CR
formulas, the five combat roles and their CR offsets, and the pirate rule.

---

# ⚠ `PT-1844` complete — 24 of 24

**Both finished books are through.** Galactic Timeline, eight chapters; the Armory, sixteen.
**Zero internal citations remain in either**, verified chapter by chapter by search rather
than by assumption.

**What the task actually turned out to be.** Removing a citation was the easy half. **The
work was in the sentences the citations were holding up** — and the recurring finding across
all twenty-four passes was the same one: **a citation frequently hid a decision more
interesting than the citation itself.** The Katarr entry, the Telos warning, the loot bands'
inferred mapping, the droid rebuild's real price, the three unsettled space-combat numbers,
and this chapter's two roster gaps were all buried behind a ruling number that told a reader
nothing.

**The split-by-audience default did most of the work.** Where a flag had a reader-facing
half, it went into the chapter; where it was project housekeeping, it stayed in these notes.
**Every flag that had a reader-facing half had it promoted; none were dropped, and none were
softened on the way.** No count is given here because counting them reliably would mean
re-reading twenty-four chapters, and an unchecked number is exactly the kind of thing this
task existed to remove.

**Two stale status lines were caught in passing** — Chapter Fourteen's *"third of the four
remaining"* and Chapter Fifteen's *"the Armory's last chapter"*, both written before the work
that made them false. **A status line is the part of a document nobody rereads.**

**And one content gap was found rather than fixed:** `hkpart05`, the HK Protocol Pacifist
Package, which Chapter Twelve sends to Chapter Fourteen and which has no ruling anywhere.
**Named as unbuildable rather than invented.**

---

# ⚠ `PT-1844` pass 25 — front matter, bibliography, and three chapter misses

**Scope: the three reader-facing files that were never in the twenty-four-chapter count** —
both books' front matter and the Timeline's bibliography. **Approved as a single pass because
all three are short and of a kind.**

## What was removed

**Both books' `Status: per PT-1813` headers**, and both `Placement: page two or three`
citations. **A reader needs to know a book has a disclaimer and where it sits. They do not
need the ruling number that required it.** The non-negotiable-wording warning on the
disclaimer stayed — that is a production instruction, not a citation.

**`PT-1800` in the Timeline bibliography, per the owner's ruling: keep the rank, drop the
number.** The entry now reads that both titles sit at **rank 8 on the ladder Chapter One sets
out**, which is where the ladder is actually explained. Same treatment as every other rank
marking in that book.

**`PT-1352` in the Armory's authored-marking paragraph.** The `⚠ AUTHORED` tag is the thing a
reader uses; the ruling that created it is not.

**`D-W32` in the Timeline bibliography**, which justified keeping one credit list in one
place. **The reason is better than the citation was** and now states itself: so that a
correction to a credit has one place to be made.

**Three references to MAIN** — one in the Armory's confidence-tier table, one in the
Timeline's relay note, one implicit in the Armory's. **MAIN is a coordinating role inside
this project's development, and no reader has any idea what it is.** Externally researched
and corroborated says the same thing and is true on its own terms.

**Four uses of "this project's own corpus."** A reader cannot resolve *corpus*. Both games'
authorship credits now name the thing that was actually read: **KOTOR's `.uti` item files,
which carry the studio's internal developer comments**, and K2's data, which reads
extensively and never names its own staff.

**`STARSHIPS-01` and `SPACE-COMBAT-01` in the Armory's "Not used in this book" section.**
**The warning underneath them was the point and it survives at full strength** — Chapters
Fifteen and Sixteen's ship roster was not read from any source held here, traces to a Legends
wiki index at the bottom of the ladder, and is unverified.

**A build-state note on the Armory's credit page** — *"refreshed after Chapters Twelve
through Sixteen were drafted; Chapter Three's family catalogue is complete at 122 items."*
**The 122 figure belongs in Chapter Three and is stated there**; a credits page is not where
a reader looks for a catalogue count.

## ⚠ Both books' "This project's own documents" sections are gone, and that needs explaining

Each book carried a list of internal documents *"recorded so the chapters' citations
resolve."* **Those citations no longer exist. The section's entire stated purpose was removed
by this task**, and a list of unreadable filenames is worse than nothing on a credits page.

**But each section carried a rider that was not housekeeping**, and the two books needed
different answers.

**The Armory's rider — that this book's rulings govern over any source above — is true and
is now stated as what it is:** a game supplies what a weapon *was*; it never supplies what a
mechanic *does* at a table. **The section was replaced rather than deleted**, and it points
at the `⚠ AUTHORED` marks and the confidence tiers as how a reader checks that claim instead
of taking it on trust.

**⚠ The Timeline's identical rider sat in tension with its own Chapter One**, which says in
plain words that *"if a date here contradicts the sources, the sources win and this book has
a mistake in it."* **A bibliography claiming the project's rulings govern over any source
contradicts the chapter a reader has just read.** The replacement follows Chapter One rather
than the rider, points at Chapter One for the full ladder, and **the tension was reported
rather than quietly resolved** — it is a disagreement between two reader-facing pages, which
is the owner's to settle, not this pass's.

## ⚠⚠ And the sweep caught three misses in chapters already passed and approved

**This is the part worth recording.** Running one uniform pattern across every file in both
books found internal citations in **three places the per-chapter passes had cleared:**

    Ch7   FEATS-LIBRARY-01, inside the bay-gate paragraph
    Ch12  Status: DRAFT, for review — "the first of the Armory's four
          remaining chapters"
    Ch12  CLASS-ROSTER-01, inside a monospace block

**The cause is mine and it is worth naming exactly.** Each chapter pass ran its own
verification grep, and **the patterns were not identical from pass to pass** — the earlier
ones were weaker, and two of these three sit in formatting a reading eye skips: a monospace
block and a header nobody rereads. **Every pass verified itself. No pass verified the same
way as the others.**

**A third stale status line**, after Chapter Fourteen's and Chapter Fifteen's — and this one
survived its own chapter's dedicated pass.

**The lesson, recorded because it generalises past this task: a per-item check that varies
between items is not a check on the set.** The uniform sweep at the end is what caught this,
and it is the thing worth keeping, not the individual fixes. **All three are fixed and both
books now return zero under a single pattern run over every file.**

---

# ⚠ `PT-1770` — Chapter Ten expanded to a full catalogue

**89 items, every one of them now on the page.** Built programmatically from the ruled item
catalogue rather than transcribed, on Chapter Three's method — every count read back from
the source's own category headings and compared before anything was written.

    quest   datapad 2 · droid-parts 5 · plot 13                 = 20
    other   credits 15 · misc 3 · pazaak 24 · shock-arm 2
            · boots 25                                          = 69
                                                          TOTAL = 89

**All eight category counts agreed with the source's own stated figures on the first pass.**
Resrefs are unique across all 89. Six descriptions are truncated in the games' own data and
are marked in place, on Chapter Three's convention.

## ⚠⚠ The scope table below undercounted this chapter by 69 items

**It recorded Chapter Ten as 20 items. It is 89.**

**The cause: the chapter draws on two source files, and the count read only the first.**
Quest items are one file, miscellaneous items another, and the scope table took the quest
figure as the chapter's whole. **The chapter's own prose had both numbers right the whole
time** — *"20 items"* for quest and *"69 items across five categories"* for miscellaneous —
**so the error was in the survey, not in the book.**

**⚠ And it inverts the ruled ordering.** Chapter Ten was sequenced first as the smallest at
20 items. **At 89 it is larger than Chapter Nine's 58.** No harm done — it is finished — but
the remaining order should be taken from verified counts rather than from this table.

## ⚠ Three more count disagreements found while checking that, reported not fixed

**Checking whether the same two-file mistake affected the other five chapters** turned up a
different problem in three of them: **the source file's stated total disagrees with the sum
of its own category headings.**

    armour    header 173   categories sum 172    short by 1
    droid     header 135   categories sum 129    short by 6
    worn      header 241   categories sum 248    OVER by 7

**The worn-gear one is the interesting case**, because the sum is *larger* than the header —
which is the opposite of a truncation and cannot be explained by a category being dropped.

**Usable items and upgrades both reconcile exactly** (58 and 164), so this is not a
systematic fault in how the files are written.

**⚠ Each is that chapter's own problem to settle when its catalogue pass comes up**, and
settling it means counting rows rather than trusting either figure — which is what this
chapter's pass did, and why its counts can be relied on. **Recorded here so no pass starts
by believing a header.**

## ⚠ A correction to Chapter Fourteen, caught by building this catalogue

**Chapter Fourteen said `hkpart05` had *"no cost, no tier and no place in a build."*** The
first two are wrong. **The ruled catalogue gives it Tier 1 at 215 credits**, with its own
description — a behaviour-core download for one particular droid.

**The ruled treatment is unchanged and unchallenged**: it is a real item, it is named, and
it is explicitly not something a droid is built from. **Only the factual claim about cost and
tier was wrong**, and it was wrong because it was written from the absence of a
*construction* ruling and then overstated into the absence of an item.

**Chapter Fourteen now points at Chapter Ten for the entry and keeps the ruling**, and the
Armory's front matter row was updated to match. **The two chapters now agree and neither
loses anything.**

---

# ⚠ `PT-1770` — Chapter Nine expanded to a full catalogue

**58 items, all six categories, every stated count agreed on the first pass.** 71 lines in,
234 out. Zero internal citations. Resrefs unique across all 58.

    adrenal 10 · components 2 · light-source 3 · medical 8
    spike 6 · trap-kit 29                                  = 58

## ⚠⚠ The finding: most of this chapter's effects are unconverted game data

**The source catalogue's `Properties` column is the games' own raw text**, and for this
chapter that is nearly all of it: **stuns lasting `9sec`, blast radii of `3.3m`, mines
dealing `Piercing, 18pts`, saves at `DC35`.** Seconds, metres, flat damage points and the
games' DC scale — **none of which this game runs on.**

**The seven conversions the source catalogue names do not cover any of it.** They convert
dice, Massive Criticals, tiers, uniqueness, crystals, upgradeability and the feat remap.
**There is no conversion for adrenal durations or trap-kit effects, and none was invented
here.**

**So the chapter catalogues all 58 and marks the column for what it is.** A Gamemaster can
read a Deadly Frag Mine's 54 points and its DC 25 and judge the shape of it; what they
cannot do is mistake those for this game's rules. **Recorded rather than converted, and said
plainly rather than left to look like crunch.**

**⚠ This is a real conversion gap and it is the largest one the catalogue work has turned up
so far — 39 items across two categories.** It is not this pass's to close. **Raised for a
decision.**

## ⚠ The medpacs were the trap, and they nearly went in backwards

**Chapter Nine's own prose already rules that a medpac heals `2d8`, an Advanced Medpac
`4d8`, and a Life Support Pack `6d8`, dropping the games' Wisdom-and-skill dependency.**
**The source catalogue's properties column still carries the games' formula** — *"10 vitality
points + WIS modifier + user's skill in Treat Injury."*

**A verbatim dump would have put the superseded formula three lines under the conversion
table that supersedes it, in the same chapter.** Caught before writing; the five affected
rows now carry the ruled dice instead.

**⚠ And the descriptions repeat the formula too**, which the properties substitution did not
fix. The item's own description text says it as well. **The quote is left intact and marked
in place** — *"the description states the games' formula; this game's value is the one
above"* — because editing a quoted description silently is worse than the contradiction.

**This is exactly the re-import-a-stale-value trap**, and the only reason it did not land is
that the chapter's prose was read before the catalogue was generated rather than after.

## ⚠ Two smaller conventions, both declared in the chapter

**Twenty-three descriptions open by restating the identical stat block already in the Effect
column**, then continue into real description. **The repeated opening is trimmed and the rest
quoted**, and the chapter says so rather than letting a reader wonder why some quotes start
mid-thought.

**Three rows have no name in the source** — `ptar_rakghoulser`, `g_i_progspike003` and
`g_i_progspike02`. **The last carries a full description and a working effect and is plainly
a real item whose name did not resolve**; the other two carry nothing but a resref and a
price of zero.

**All three are listed, marked, and un-named.** The resrefs are suggestive — one of them
obviously points at a specific Taris plot item — **but a resref is not a name, and guessing
one into a catalogue is how a wrong name becomes permanent.** Worth someone resolving
against the string table.

## What matched, and what that confirms

**Chapter Nine's header and its category sum both read 58 and agree** — one of the two
chapters whose counts reconciled in the earlier survey, and the counts held when the rows
were actually counted. **The survey's arithmetic was right here; it was the Chapter Ten
undercount that was the outlier, not this.**

---

# ⚠ `PT-1770` — Chapter Seven expanded to a full catalogue

**129 items, all eight categories, every category count agreed on the first pass.** 68 lines
in, 358 out. Zero internal citations. Resrefs unique across all 129.

## ⚠⚠ The chapter's item total was wrong, and it disagreed with its own table

**The count had stood at 135. It is 129.**

    device 29 · interface 15 · named 10 · plating 25
    sensor 12 · shield 13 · spike-mount 7 · tool 18   = 129

**All eight category figures were already right and already summed to 129.** The total was
the only wrong number — **and it sat directly above a table that contradicted it.**

**This was the one flagged in the Chapter Ten pass as *"droid, header 135, sum 129, short by
6"*, and counting the rows settled which of the two was wrong.** The rows are 129. **The
header was the error, in the source catalogue and in the chapter that copied it.**

**⚠ And it had cross-records.** Chapter Fourteen opened with *"Chapter Seven covers 135
droid items"*, and the live outline carried `ITEMS-04 — 135 items`. **Both corrected.** The
superseded outline was left alone; it is tombstoned. **Found by grepping the value rather
than the document — which is the only thing that finds this class of error.**

## ⚠⚠ Forty-nine of the 129 rows carry a property the data does not resolve

**The commonest shape is a skill bonus whose size is known and whose skill is not** — `Skill
bonus +4`, with no name attached. The games store the skill as a numeric index and that
index was never mapped back to a name for most of these rows.

    interface 13 · named 10 · sensor 9 · tool 7
    spike-mount 6 · plating 4                        = 49

**The magnitude is real and usable; only the label is missing.** The chapter says so
directly, keeps each unresolved property's index in the margin so it can be resolved from
the page, and **guesses at nothing.** A `Droid Motion Sensors Type 2` grants `+4` to
something that its own name makes obvious — **and obvious is not recorded.**

**⚠ One row proves the resolution exists.** The `Advanced Droid Interface` carries its four
skills **by name** — Awareness, Computer Use, Demolitions, Security — where its six
neighbours in the same category carry bare indices. **So this is not missing data. It is
data that was resolved once and not applied to the rest.**

**⚠ I did not resolve them, and the reason is worth recording.** The index almost certainly
maps through the games' skill table, and four items corroborate a reading by name alone
(motion sensors to Awareness, a lockout bypass to Computer Use and Security, a stealth
booster to Stealth, a machine interface to Repair). **But the repo's own copy of that table
is a binary file that cannot be read as text** — the same trap the Armory's front matter
already records about `k2_baseitems.2da`.

**More importantly it is not a catalogue pass's call.** Resolving 49 rows changes what ruled
material means, it would apply to the remaining chapters as much as this one, and **it is
better done once, globally, than improvised here.** **Proposed as a follow-up.**

## What was verified rather than assumed

**Every specific value the chapter already claimed was checked against the data before the
rewrite**, not after: the five representative device prices, the five plating entries, the
`Droid Desh Plating` `−3` penalty, *"three appearing in both games"* — **three rows carry
`K2+K1`, exactly** — and the `Advanced Droid Interface`'s tier, price, `Droid Upgrade 3`
gate and all four skill values. **All correct.**

**The corrupted-name warning was kept and extended.** It is still true of the game files;
the chapter now adds that the item is catalogued below under its real name, which it was not
before.
