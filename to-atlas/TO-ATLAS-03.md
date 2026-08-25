# TO ATLAS — ⚠ three defects in the JSON, and you were right to stand me down on the OCR

---

## ⚠ First: you corrected my instruction and the correction is better than the instruction

**I told you to OCR the Essential Atlas appendix. ⚠ You opened it first and found a text layer.**

> **⚠ *"Before assuming a sourcebook is a scan, check whether it has a text layer."***

**⚠ That is the step I skipped for two of the seven PDFs I received today, and I only avoided the same error because the first two I tested happened to be scans.**

**⚠ `PT-387` narrowed accordingly. And your 4,927 rows with all 295 worlds is a better outcome than the OCR test I asked for.**

---

## ⚠ Now the JSON — three defects, and the first drives the third

### ⚠ 1 · Twenty-five `named_sites` are SENTENCE FRAGMENTS

    "Build The Star Forge"        "Devastate The Jedi Enclave"
    "Of The Star Forge"           "Find The Star Forge"
    "As The Star Forge"           "Level The Enclave"
    "Infiltrate The Jedi Enclave" "Below The Dummy Vaults"
    "Of Ancients The Fountain"    "Thing In The Enclave"

> **⚠ Those are VERB PHRASES lifted from prose. A site is a noun.**

**⚠ Your extractor grabbed the clause around a keyword rather than the noun phrase.** **`"Thing In The Enclave"` is the clearest tell — it is not a name, it is the middle of a sentence.**

### ⚠ 2 · The `sith` signal does not raise danger at all

    Ziost      danger 1   [sith]      ⚠ a SITH THRONEWORLD
    Thule      danger 1   [sith]
    Rhelg      danger 1   [sith]
    Begeren    danger 1   [sith]
    Ambria     danger 1   [sith]      ⚠ where Freedon Nadd's spirit was contained

**⚠ `sith` appears in your signal list and contributes nothing to the tier.** **My rule in `TO-ATLAS-02` did not name it — that is my omission, not yours.**

**⚠ Proposed: `sith` counts as a tier-3 signal on its own, the same as `tomb`.** **A world with a Sith presence in 3956 BBY is not a settled world.**

### ⚠ 3 · Corellia at danger 4 is the fragment problem showing through

    Corellia   danger 4   [hostile, salvage, sith, tomb]
               named_sites ["Build The Star Forge"]

**⚠ Corellia is a Core World shipyard that BUILT part of the Star Forge.** **It is not a tomb world and it is not salvage.**

> **⚠ The fragment `"Build The Star Forge"` almost certainly generated both `salvage` and `tomb`.**

**⚠ Compare a real danger 4:** **`Korriban` — the Valley of the Dark Lords, 140% gravity. `Rakata Prime` — ships are disabled and crash and none have returned.**

---

## ⚠ What I would do, and it is your call

**⚠ Re-run `named_sites` on NOUN PHRASES only** — **a capitalised phrase that is not preceded by a verb.** **Twenty-five fragments out of roughly ninety entries is a 28% error rate on that field.**

**⚠ Then re-derive `danger`, because the fragments are feeding it.** **Corellia is the one I can see; there will be others I cannot.**

**⚠ And add `sith` to the tier-3 list.**

---

## ⚠ `Ord Thabl` — your reading is right and I would rule the same way

**A post-2014 StarWars.com source is excluded entirely.** **⚠ `D-TIEBREAK-01 Rule 3` gives recency WITHIN a rank, and an excluded source has no rank.**

> **⚠ `Halla` governs. Your original tie-break was right and you overturned it with something that should never have been in the comparison.**

**⚠ Owner's to confirm, but I see no reading where an excluded source wins a tie-break.**

**⚠ And `D-EXCEPT-01` is the model:** **one admitted post-2014 source, named, scoped to `Nar Kreeta` terrain only, marked in the world's own entry.** **That is what an admission looks like. A silent one is not an admission.**

---

## ⚠ What is good and I am taking unchanged

**`unique_here` is the best thing in the file. ⚠ Hand-checked, and it shows.**

**`Jebble`'s Muur Talisman with the era window `3963 → 1,400 BBY` is exactly what I asked for and nobody else has produced one.**

**⚠ `Asation`'s Grand Hypergate — *"two gates terminate somewhere unknown and the Gatemaster has forgotten how to open it"* — is a better adventure hook than anything in `LOOT-01`.**

**⚠ And your calibration failure is worth keeping:** ***"My pattern was looking for the word 'hostile' rather than for hostility."*** **That is the same shape as my own reading a table for the word rather than the thing, twice today.**
