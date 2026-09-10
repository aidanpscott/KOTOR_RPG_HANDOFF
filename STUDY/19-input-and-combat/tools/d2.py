#!/usr/bin/env python3
"""Dump a 2DA straight out of a KEY/BIF index.

⚠ TWO FORMATS. KOTOR ships '2DA V2.b' (binary, parse2da.py). NWN:EE ships
'2DA V2.0' (plain text, shlex-quoted). Detected from the magic, not the game.
"""
import sys, os, shlex, tempfile
# ⚠ THE READER MOVED TO `MAIN_WORK/scripts/` — `PT-1642`, owner ruling: a tool
# goes in `scripts/`, not in a study folder. Repaired in place rather than left
# broken; this file is `Scholar`'s and only its import changed.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..', '..', 'MAIN_WORK', 'scripts'))
from keybif import KeyIndex
from parse2da import parse as parse_binary


def parse_text(data):
    lines = data.decode('utf-8', 'replace').splitlines()
    assert lines[0].startswith('2DA V2.0')
    i = 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    if lines[i].strip().upper().startswith('DEFAULT:'):
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
    cols = shlex.split(lines[i]); i += 1
    labels, rows = [], []
    for ln in lines[i:]:
        if not ln.strip():
            continue
        parts = shlex.split(ln)
        if not parts:
            continue
        labels.append(parts[0])
        cells = parts[1:]
        cells += [''] * (len(cols) - len(cells))   # ragged tail
        rows.append(cells[:len(cols)])
    return cols, labels, rows


def load(key, name):
    data = KeyIndex(key).read(name, 2017)
    if data[:8] == b'2DA V2.b':
        with tempfile.NamedTemporaryFile(suffix='.2da', delete=False) as f:
            f.write(data); tmp = f.name
        try:
            return parse_binary(tmp)
        finally:
            os.unlink(tmp)
    return parse_text(data)


if __name__ == '__main__':
    key, name = sys.argv[1], sys.argv[2]
    want = sys.argv[3].split(',') if len(sys.argv) > 3 else None
    cols, labels, rows = load(key, name)
    idx = list(range(len(cols))) if not want else [cols.index(c) for c in want]
    print(f'# {name}: {len(rows)} rows, {len(cols)} cols')
    print('# cols: ' + ' | '.join(cols))
    print('-' * 100)
    w = [max([len(cols[i])] + [len(str(r[i])) for r in rows]) for i in idx]
    w = [min(x, 22) for x in w]
    print('  '.join(['#'.ljust(4)] + [cols[i][:22].ljust(w[j]) for j, i in enumerate(idx)]))
    for n, r in enumerate(rows):
        print('  '.join([str(n).ljust(4)] + [str(r[i])[:22].ljust(w[j]) for j, i in enumerate(idx)]))
