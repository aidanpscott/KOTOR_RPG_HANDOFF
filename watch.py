#!/usr/bin/env python3
"""watch.py — block until the other side pushes, or time out.

Neither agent runs on a timer, but a bash call can block. Poll the handoff
repo and return the moment a new file lands in the directory you are
watching.

⚠ TWO DEFECTS LIVED IN THIS FILE. Both are worth knowing.

  1. It printed `[:4000]`. Both agents read the first third of every file
     for four exchanges and neither noticed. A watcher reports WHAT
     LANDED; reading is a separate act done from the working tree, in
     full, by whoever needs it.

  2. It hard-coded a direction, and was then copied to the other agent
     with a sed that caught one of two references. Half-renamed, it
     listed one directory and stat'd files in the other.

Both are the same mistake: a script that knows which side it is on.
It does not any more -- pass the direction.

Usage:  python3 watch.py WATCH_DIR [seconds]

    main agent:      python3 watch.py from-designer 240
    class designer:  python3 watch.py to-designer   240
"""
import subprocess, sys, time, os

if len(sys.argv) < 2 or sys.argv[1].startswith('-'):
    sys.exit("usage: python3 watch.py WATCH_DIR [seconds]\n"
             "  e.g. python3 watch.py from-designer 240")

WATCH = sys.argv[1].strip('/')
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 240
D = os.path.dirname(os.path.abspath(__file__))

if not os.path.isdir(os.path.join(D, '.git')):
    sys.exit(f"not a git checkout: {D}")

def ls():
    subprocess.run(['git', '-C', D, 'fetch', '-q', 'origin'], capture_output=True)
    subprocess.run(['git', '-C', D, 'reset', '-q', '--hard', 'origin/main'], capture_output=True)
    p = os.path.join(D, WATCH)
    return set(os.listdir(p)) if os.path.isdir(p) else set()

before = ls()
print(f"watching {WATCH}/ for {limit}s — {len(before)} file(s) present")
t0 = time.time()
while time.time() - t0 < limit:
    time.sleep(15)
    new = ls() - before
    if new:
        print(f"\nNEW after {int(time.time()-t0)}s:")
        for f in sorted(new):
            p = os.path.join(D, WATCH, f)
            print(f"  {f}  {os.path.getsize(p):,} bytes  ->  {p}")
        sys.exit(0)
print(f"nothing new in {limit}s.")
