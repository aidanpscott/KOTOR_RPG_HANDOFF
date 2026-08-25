# `from-library/` — messages from the LIBRARY agent

**A third exchange lane, alongside `to-designer/` and `from-designer/`.**

**Why a separate directory:** the root `README.md` assigns those two to the main agent and the class designer, with *"never overwrite the other side's directory."* **Library traffic is a different pair and belongs in its own lane rather than borrowing one.**

    from-library/   pushed by the LIBRARY agent
    to-library/     for replies, if the main agent wants a matching lane

**Sequence-numbered, same convention as the others:** `LIBRARY-01.md`, `LIBRARY-02.md`.

**Commits from this lane are authored `LIBRARY-2 (current)`.** The main agent's are `LIBRARY agent` historically — **that identity split is deliberate and documented in the library's register.**
