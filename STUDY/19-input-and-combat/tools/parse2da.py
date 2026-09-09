#!/usr/bin/env python3
"""
parse2da.py — BioWare 2DA V2.b binary parser (KOTOR 1 / KOTOR 2).

Format notes, in case a file fails to parse:
  bytes 0-8    : b'2DA V2.b\n' magic
  then         : column headers, tab-separated, terminated by NUL
  then         : uint32 little-endian row count
  then         : row labels, each terminated by TAB
  then         : uint16 offset per cell, row-major (rowcount * ncols of them)
  then         : uint16 total size of the string blob
  then         : the string blob; each cell offset points at a NUL-terminated string

Empty cells point at a zero-length string, which reads as ''. The games also
use '****' as an explicit "no value" marker, so treat BOTH '' and '****' as
absent when filtering.

Library use:
    from parse2da import parse
    cols, rowlabels, rows = parse('classes.2da')
    # cols      -> list[str]         column names
    # rowlabels -> list[str]         the leading index column (usually '0','1',...)
    # rows      -> list[list[str]]   every cell as a string; cast as needed

CLI use:
    python3 parse2da.py FILE.2da                 # summary: columns + row count
    python3 parse2da.py FILE.2da --dump          # every row, aligned
    python3 parse2da.py FILE.2da --cols a,b,c    # only those columns
    python3 parse2da.py FILE.2da --grep TEXT     # rows containing TEXT (any cell)
    python3 parse2da.py FILE.2da --json          # full parse as JSON
"""

import struct
import sys
import json

MAGIC = b'2DA V2.b\n'
ABSENT = ('', '****')


def parse(path):
    """Parse a 2DA V2.b file. Returns (cols, rowlabels, rows)."""
    with open(path, 'rb') as fh:
        d = fh.read()

    if d[:9] != MAGIC:
        raise ValueError(
            f"{path}: not a 2DA V2.b file (magic was {d[:9]!r}). "
            "V2.b is the binary format shipped inside the .bif archives; "
            "a file exported as plain text will not parse here."
        )

    p = 9

    # Column headers: tab-separated, NUL-terminated.
    end = d.index(b'\x00', p)
    cols = d[p:end].decode('ascii', 'replace').split('\t')
    cols = [c for c in cols if c != '']
    p = end + 1

    # Row count.
    rowcount = struct.unpack_from('<I', d, p)[0]
    p += 4

    # Row labels, each TAB-terminated.
    rowlabels = []
    for _ in range(rowcount):
        e = d.index(b'\t', p)
        rowlabels.append(d[p:e].decode('ascii', 'replace'))
        p = e + 1

    # Cell offsets into the string blob, row-major.
    ncells = rowcount * len(cols)
    offsets = struct.unpack_from('<%dH' % ncells, d, p)
    p += 2 * ncells

    # Blob size, then the blob.
    datasize = struct.unpack_from('<H', d, p)[0]
    p += 2
    blob = d[p:p + datasize]

    def s(off):
        e = blob.index(b'\x00', off)
        return blob[off:e].decode('ascii', 'replace')

    rows = []
    for r in range(rowcount):
        base = r * len(cols)
        rows.append([s(offsets[base + c]) for c in range(len(cols))])

    return cols, rowlabels, rows


def present(value):
    """True if a cell carries an actual value ('' and '****' mean absent)."""
    return value not in ABSENT


def as_dicts(path):
    """Parse into a list of {column: value} dicts, with '_row' as the label."""
    cols, rowlabels, rows = parse(path)
    out = []
    for label, row in zip(rowlabels, rows):
        rec = {'_row': label}
        rec.update(dict(zip(cols, row)))
        out.append(rec)
    return out


def _widths(cols, rows, idx):
    w = []
    for c in idx:
        longest = max([len(cols[c])] + [len(r[c]) for r in rows]) if rows else len(cols[c])
        w.append(min(longest, 40))
    return w


def _print_table(cols, rowlabels, rows, idx):
    w = _widths(cols, rows, idx)
    header = '  '.join(cols[c][:w[i]].ljust(w[i]) for i, c in enumerate(idx))
    print(f"{'row':>5s}  {header}")
    print(f"{'-' * 5}  {'-' * len(header)}")
    for label, row in zip(rowlabels, rows):
        line = '  '.join(row[c][:w[i]].ljust(w[i]) for i, c in enumerate(idx))
        print(f"{label:>5s}  {line}")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1

    path = argv[1]
    flags = argv[2:]
    cols, rowlabels, rows = parse(path)

    if '--json' in flags:
        print(json.dumps(
            {'cols': cols, 'rowlabels': rowlabels, 'rows': rows},
            indent=2,
        ))
        return 0

    # Restrict to named columns if asked.
    idx = list(range(len(cols)))
    if '--cols' in flags:
        wanted = flags[flags.index('--cols') + 1].split(',')
        idx = []
        for name in wanted:
            name = name.strip()
            if name not in cols:
                print(f"[warn] no column named {name!r}", file=sys.stderr)
                continue
            idx.append(cols.index(name))
        if not idx:
            print("[error] none of the requested columns exist", file=sys.stderr)
            return 1

    # Filter rows if asked.
    shown_labels, shown_rows = rowlabels, rows
    if '--grep' in flags:
        needle = flags[flags.index('--grep') + 1].lower()
        pairs = [(l, r) for l, r in zip(rowlabels, rows)
                 if any(needle in cell.lower() for cell in r)]
        shown_labels = [l for l, _ in pairs]
        shown_rows = [r for _, r in pairs]

    if '--dump' in flags or '--grep' in flags or '--cols' in flags:
        _print_table(cols, shown_labels, shown_rows, idx)
        print(f"\n{len(shown_rows)} of {len(rows)} rows, {len(cols)} columns")
        return 0

    # Default: summary only.
    print(f"file    : {path}")
    print(f"rows    : {len(rows)}")
    print(f"columns : {len(cols)}")
    print()
    for i, c in enumerate(cols):
        filled = sum(1 for r in rows if present(r[i]))
        print(f"  {i:>3d}  {c:<28s} {filled:>4d}/{len(rows)} filled")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
