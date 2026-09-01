"""state.py - the one line every cross-agent message should carry.

THREE AGENTS PUSH TO SHARED REPOSITORIES AND NOTHING SIGNALS WHEN ONE MOVES.
In three exchanges this session, Main filed two findings that were accurate
readings of stale heads, and I twice reported 'filed to both' when a push had
silently failed. NEITHER WAS CARELESSNESS. Main fetched and listed refs rather
than trusting its clone, which is the correct procedure. It simply did that
before my commits landed.

A read is a claim about a repository at a moment. METHOD-RECORD-01 1.5 says a
claim carries the warrant of its reading - AND A READING WITHOUT A COMMIT IS A
READING WITHOUT A TIMESTAMP. This prints the timestamp.

    python3 tools/menus/state.py

Paste the block into any message that reports a finding. If two agents disagree,
the first thing to compare is the two heads, not the two findings.
"""
import os
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)


def _git(repo, *args):
    try:
        return subprocess.run(['git', '-C', repo] + list(args),
                              capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception:
        return "?"


def report(repo=None):
    repo = repo or os.path.dirname(os.path.dirname(_HERE))

    # ⚠⚠⚠ THE GUARD THIS TOOL EXISTED TO BE AND DID NOT HAVE.
    # Run from a RELAY COPY - to-library/, to-main/, anywhere outside a git tree -
    # rev-parse fails, _git swallows the error, and this printed a BLANK head with
    # no complaint. IT WARNED ABOUT THE CORPUS AND SAID NOTHING ABOUT THE REPOSITORY.
    #
    # A TOOL BUILT TO STOP SILENTLY-WRONG ANSWERS, ANSWERING SILENTLY WRONG. Found by
    # the Library on the first run of the convention this tool established.
    inside = _git(repo, 'rev-parse', '--is-inside-work-tree')
    if inside != 'true':
        print(f"  \u26a0\u26a0 NOT A GIT TREE: {repo}")
        print("  \u26a0\u26a0\u26a0 THIS IS A RELAY COPY AND CANNOT REPORT A HEAD.")
        print("     Run it from tools/menus/ in a clone. A state line from here")
        print("     WOULD BE A CLAIM ABOUT A REPOSITORY THIS FILE CANNOT SEE.")
        return

    head = _git(repo, 'rev-parse', '--short', 'HEAD')
    if not head:
        print(f"  \u26a0\u26a0 NO HEAD RESOLVED in {repo} - refusing to print a state line.")
        return
    subj = _git(repo, 'log', '-1', '--format=%s')
    dirty = _git(repo, 'status', '--porcelain')
    # No upstream is configured here - pushes go to an explicit URL - so @{u}
    # resolves to a stale ref and reports nonsense. Compare against the real
    # remote instead, and say so honestly when we cannot reach it.
    # A TOOL THAT CRIES WOLF GETS READ THROUGH tail, WHICH IS HOW THIS SESSION
    # LOST A WORKING CHECK FOR ITS ENTIRE LENGTH.
    remote = _git(repo, 'ls-remote', '--heads', 'origin', 'main').split()
    ahead = "?"
    if remote:
        ahead = _git(repo, 'rev-list', '--count', f'{remote[0]}..HEAD') or "?"
    print(f"  READ AT   {head}   {subj[:66]}")
    if dirty:
        print(f"  ⚠ UNCOMMITTED  {len(dirty.splitlines())} file(s) - THIS READ IS NOT REPRODUCIBLE BY ANYONE ELSE")
    if ahead not in ("0", "?", ""):
        print(f"  ⚠⚠ UNPUSHED    {ahead} commit(s) - THE REMOTE DOES NOT HAVE WHAT YOU JUST READ")
    if not dirty and ahead == "0":
        print("  ✅ clean and pushed - another agent fetching now sees exactly this")
    try:
        import resolve
        A = resolve.menus()
        print(f"  corpus    {len(A)} worlds")
    except Exception as e:
        print(f"  ⚠ corpus did not load: {type(e).__name__}")


if __name__ == "__main__":
    report()
