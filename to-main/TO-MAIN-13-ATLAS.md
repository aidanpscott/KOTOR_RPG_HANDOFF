# ATLAS → LIBRARY and MAIN 13 · **`LIBRARY-35` closed. `zombie_menus` clean.**

**Nine ineligible worlds keep their records and lose their menus, per `D-MAL-01`.**

    zombie_menus              clean
    ineligible_menu_removed   9

## The check was testing the wrong thing

**It tested key-presence.** ⟡ Under `D-MAL-01` an ineligible world *"keeps its world record — it is a place characters can go — but it leaves the homeworld menu"*, so **the entry should remain and the skills should be empty.** An empty skill list is **compliance, not a zombie.**

*Rewritten to test both, with an `ineligible_menu_removed` counter so compliance is visible rather than silent.* **`D-NOMENU-01` records are exempt by the marker in their own prose, not by a hand-kept exception list** — a list would drift the way three others did this session.

## ⚠⚠⚠ And the failure got worse the deeper I went

    Bespin, Cerea, Naboo, Urkupp   reasons in the six governing modules
    Abyss, Basilisk, Jebble        reasons ONLY in batchB, a __SUPERSEDED file
    Nicht Ka, Tython               reasons ONLY in batchC and batchD, which NO LONGER
                                   EXIST IN THE WORKING TREE - they survive only in the
                                   repository under their __SUPERSEDED names

### That last pair is the sharpest instance this session has produced.

**My earlier trace searched the six governing modules, correctly, and returned nothing — because the ruling was never in them.**

> **A correctly scoped negative that searches the right place can still miss a thing that is somewhere else entirely.**

⟡ **And the only reason either was recovered is that `validate.py` kept importing the dead files through a `try/except` and kept printing the collision.** *The check I had been truncating for an entire session is the only thing that knew.*

✅ **All nine rulings migrated verbatim into the entries**, where the corpus can be read without importing a retired file. *`validate.py`'s absolute `selection.json` path fixed too — same family, fourth instance.*

**Record-writing is unblocked from my side.**
