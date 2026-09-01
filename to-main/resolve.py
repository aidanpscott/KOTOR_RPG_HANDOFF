# -*- coding: utf-8 -*-
"""One resolver, used by every tool.

Written because check.py and validate.py each guessed at name resolution
separately, neither read aliases.py, and both spent the session reporting ten
worlds as MISSING that were sitting in the menus under a different name.

A checker that cries wolf gets ignored. That is the actual risk being fixed.
"""
import sys, json, importlib
for p in ('/home/claude/menu', '/home/claude/b1', '/home/claude/b2'):
    if p not in sys.path:
        sys.path.insert(0, p)

SELECTION = '/home/claude/reg/selection.json'

# Deliberately absent — ruled ineligible, must NOT report as missing.
# Regions, nebulae, clusters and voids are not worlds.
# Destroyed bodies are listed only where no survivor could be a character:
# Ereesus (3970) and Urkupp (3996) ARE eligible and DO have menus.
INELIGIBLE = {
    "Cron Drift":      "region — what the Cron Cluster became after the supernova",
    "Jaga's Cluster":  "cluster, not a world",
    "Radama Void":     "void, not a world",
    "Stygian Caldera": "nebula, not a world",
    "Peragus":         "broken body; Sapient Species: None (owner ruling)",
    "Malachor":        "torn apart in 3960 and empty since (owner ruling)",
    "Omonoth":         "a WHITE DWARF STAR, not a planet \u2014 the ring is asteroids",
}


def menus():
    """Every live menu, reloaded. Never answers from a stale import."""
    import m_a, m_b, m_c, m_d
    import menus as M1, menus2 as M2
    A = {}
    for m in (M1, M2, m_a, m_b, m_c, m_d):
        importlib.reload(m)
        A.update(m.M)
    return A


def aliases():
    """selection name -> menu key. Empty dict if the map is absent."""
    try:
        import aliases as _a
        importlib.reload(_a)
        return dict(_a.A)
    except Exception:
        return {}


def key(name, A=None):
    """Given any selection name, return the menu key that holds it, or None.

    Tries the name itself, then the alias map. This is the whole point of the
    module: one place that knows how a name becomes a key.
    """
    A = A if A is not None else menus()
    if name in A:
        return name
    alt = aliases().get(name)
    if alt and alt in A:
        return alt
    return None


def status(name, A=None):
    """('ok'|'ineligible'|'missing', detail) — the distinction the old checker lacked."""
    A = A if A is not None else menus()
    k = key(name, A)
    if k:
        return ('ok', k)
    if name in INELIGIBLE:
        return ('ineligible', INELIGIBLE[name])
    return ('missing', 'no menu and no ruling')


def selection():
    return {r['system']: r for r in json.load(open(SELECTION))}


def audit():
    """Print the real picture. Anything under MISSING is genuinely wrong."""
    A, sel = menus(), selection()
    buckets = {'ok': [], 'ineligible': [], 'missing': []}
    for w in sel:
        st, detail = status(w, A)
        buckets[st].append((w, detail))
    print(f"  resolved      {len(buckets['ok']):>4d}")
    print(f"  ineligible    {len(buckets['ineligible']):>4d}  (deliberately absent)")
    print(f"  MISSING       {len(buckets['missing']):>4d}")
    for w, d in sorted(buckets['ineligible']):
        print(f"     ok  {w:16s} {d}")
    for w, d in sorted(buckets['missing']):
        print(f"     !!  {w:16s} {d}")
    return buckets

# ---------------------------------------------------------------------------
# PUBLISHED ACCESSOR. Main's proposal, TO-ATLAS-20, adopted.
#
# menus() RETURNS A LIST OF TUPLES, AND A LIST OF TUPLES INVITES INDEXING.
# Main quoted sk[0] every time it read a menu; SEVENTEEN WORLDS HAVE MORE THAN
# ONE STRATUM, and it nearly filed KORRIBAN as a wrong-world assignment after
# extracting Dreshdae's thief menu from a world whose second stratum is the
# Valley of the Dark Lords. The split is deliberate. THE SHAPE INVITED THE BUG.
#
# This does not replace menus(). It gives a caller that wants ONE menu a way to
# say so and BE TOLD WHEN THAT IS THE WRONG QUESTION.
# ---------------------------------------------------------------------------

class Stratum(tuple):
    """(label, skills, text) - indexable as before, readable by name."""
    __slots__ = ()
    def __new__(cls, label, skills, text):
        return super().__new__(cls, (label, list(skills), text))
    label = property(lambda self: self[0])
    skills = property(lambda self: self[1])
    text = property(lambda self: self[2])
    def __repr__(self):
        return "Stratum(%r, %r, %d chars)" % (self[0] or "(single)", self[1], len(self[2]))


def menus_for(world, strict=True):
    """Every stratum of one world, named. NEVER SILENTLY THE FIRST ONE.

    strict=True  raises if the world is unknown, rather than returning [].
                 A missing world is a question about the corpus, not an
                 empty answer to a question about a world.
    """
    A = menus()
    k = key(world, A)
    if k is None:
        if strict:
            raise KeyError("no such world in the corpus: %r" % world)
        return []
    return [Stratum(*s) for s in A[k]]


def sole_menu(world):
    """The ONE menu of a single-stratum world.

    RAISES if the world has more than one. That is the whole point: a caller
    that wants a single menu from KORRIBAN, TARIS or TATOOINE is asking a
    question with no answer, and should be told so rather than handed the
    first of three.
    """
    st = menus_for(world)
    if len(st) != 1:
        raise ValueError(
            "%r has %d strata (%s) - use menus_for() and say which"
            % (world, len(st), ", ".join(s.label or "(unlabelled)" for s in st)))
    return st[0]
