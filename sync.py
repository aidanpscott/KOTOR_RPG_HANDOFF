#!/usr/bin/env python3
"""sync.py — CATCH UP FIRST, then watch.

⚠ THE DEFECT THIS EXISTS TO FIX

watch.py computes `now - before`. `before` is sampled the instant the watch
starts, so anything already sitting in the directory is invisible for the
whole run and for every run after it. Twice in this project a reply landed
in the gap between a push and the next watch, was folded into the baseline,
and was never reported: REPLY-06 and REPLY-09. Both times the agent reported
"nothing new" while the answer was on disk, and both times the other side was
waiting on a reply that had already been sent.

A set difference answers "what arrived while I was looking".
The question that actually matters is "what have I not read yet".
Those differ exactly when it is expensive.

So: a read cursor, on disk, per instance. Anything past it is UNREAD whether
it arrived one second ago or twenty minutes before this process started.

Usage:
    python3 sync.py to-designer REPLY  [seconds]
    python3 sync.py from-designer FINDINGS [seconds]   # what the sibling wrote

Exit 0 with UNREAD listed, or exit 0 with "nothing unread" after the timeout.
The cursor only advances when you call --mark, after you have actually read
the file. Reading is a separate act from being told the file exists; that is
the same lesson as watch.py's [:4000] truncation.
"""
import subprocess, sys, os, re, time, json, hashlib

D = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(os.path.expanduser("~"), ".sync_cursor.json")


def load():
    try:
        return json.load(open(STATE))
    except Exception:
        return {}


def save(s):
    json.dump(s, open(STATE, 'w'), indent=1)


def refresh():
    subprocess.run(['git', '-C', D, 'fetch', '-q', 'origin'], capture_output=True)
    subprocess.run(['git', '-C', D, 'reset', '-q', '--hard', 'origin/main'], capture_output=True)


def present(watch_dir, prefix):
    p = os.path.join(D, watch_dir)
    if not os.path.isdir(p):
        return {}
    out = {}
    for f in os.listdir(p):
        m = re.match(rf'{prefix}-(\d+)\.md$', f)
        if m:
            out[int(m.group(1))] = os.path.join(p, f)
    return out


def digest(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:12]


def amended(have, key):
    """⚠ A file already read can be REWRITTEN IN PLACE. REPLY-11 was, at 00:59,
    after it had been read and acted on at 00:10. A cursor keyed on the highest
    number cannot see that -- max N does not move. So hash what we read."""
    seen = load().get(key + ':hash', {})
    out = {}
    for n, p in have.items():
        h = digest(p)
        if str(n) in seen and seen[str(n)] != h:
            out[n] = p
    return out


def report(files, watch_dir, prefix, label='UNREAD'):
    print(f"{label} in {watch_dir}/ — {len(files)} file(s):")
    for n in sorted(files):
        print(f"  {prefix}-{n:02d}.md  {os.path.getsize(files[n]):,} bytes  ->  {files[n]}")
    print("\n(cursor NOT advanced. run: python3 sync.py --mark <dir> <prefix> <N>)")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--mark':
        _, _, wd, prefix, n = sys.argv[:5]
        s = load()
        s[f'{wd}:{prefix}'] = int(n)
        h = s.setdefault(f'{wd}:{prefix}:hash', {})
        for k, p in present(wd, prefix).items():
            if k <= int(n):
                h[str(k)] = digest(p)
        save(s)
        print(f"cursor {wd}:{prefix} = {n}")
        return

    watch_dir = sys.argv[1] if len(sys.argv) > 1 else 'to-designer'
    prefix = sys.argv[2] if len(sys.argv) > 2 else 'REPLY'
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 180

    key = f'{watch_dir}:{prefix}'
    cursor = load().get(key, 0)

    # STEP 1 — catch up. Always. Before any waiting happens.
    refresh()
    have = present(watch_dir, prefix)
    unread = {n: p for n, p in have.items() if n > cursor}
    changed = amended(have, key)
    if changed:
        print(f"[catch-up] ⚠ AMENDED SINCE READ — content changed under a number "
              f"already consumed:")
        report(changed, watch_dir, prefix, label='CHANGED')
    if unread:
        print(f"[catch-up] cursor was {prefix}-{cursor:02d}; "
              f"highest present is {prefix}-{max(have):02d}")
        report(unread, watch_dir, prefix)
    if unread or changed:
        return

    # STEP 2 — only now is waiting justified.
    print(f"[catch-up] nothing unread past {prefix}-{cursor:02d}. watching {limit}s.")
    t0 = time.time()
    while time.time() - t0 < limit:
        time.sleep(15)
        refresh()
        have = present(watch_dir, prefix)
        unread = {n: p for n, p in have.items() if n > cursor}
        if unread:
            print(f"\nafter {int(time.time()-t0)}s:")
            report(unread, watch_dir, prefix)
            return
    print(f"nothing unread and nothing new in {limit}s.")


main()
