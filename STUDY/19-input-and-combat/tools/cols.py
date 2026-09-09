#!/usr/bin/env python3
"""Print just the column headers + row count of many 2DAs. Answers 'what did
an action CARRY' without dumping thousands of rows."""
import sys
from d2 import load
key = sys.argv[1]
for name in sys.argv[2:]:
    try:
        cols, labels, rows = load(key, name)
        print(f'\n== {name}.2da — {len(rows)} rows, {len(cols)} cols')
        print('   ' + ' | '.join(cols))
    except KeyError:
        print(f'\n== {name}.2da — ABSENT from this index')
    except Exception as e:
        print(f'\n== {name}.2da — ERROR {type(e).__name__}: {e}')
