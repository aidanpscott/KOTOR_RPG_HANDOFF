#!/usr/bin/env python3
"""watch.py — block until the designer pushes, or time out.

Neither agent runs on a timer, but a bash call can block. So instead of
ending the turn and waiting to be told, poll the handoff repo and return
the moment a new file lands in to-designer/.

Usage:  python3 watch.py [seconds]     default 240
"""
import subprocess, sys, time, os
TOK = os.environ.get('GH_TOKEN', '')
URL = f'https://{TOK}@github.com/aidanpscott/KOTOR_RPG_HANDOFF.git'
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'handoff')
limit = int(sys.argv[1]) if len(sys.argv) > 1 else 240

def ls():
    subprocess.run(['git', '-C', D, 'fetch', '-q', 'origin'], capture_output=True)
    subprocess.run(['git', '-C', D, 'reset', '-q', '--hard', 'origin/main'], capture_output=True)
    p = os.path.join(D, 'to-designer')
    return set(os.listdir(p)) if os.path.isdir(p) else set()

before = ls()
t0 = time.time()
while time.time() - t0 < limit:
    time.sleep(15)
    now = ls()
    new = now - before
    if new:
        print(f"NEW after {int(time.time()-t0)}s: {', '.join(sorted(new))}")
        for f in sorted(new):
            print(f"\n--- {f} ---")
            print(open(os.path.join(D, 'to-designer', f)).read()[:4000])
        sys.exit(0)
print(f"nothing new in {limit}s. {len(before)} file(s) already present: {', '.join(sorted(before)) or 'none'}")
