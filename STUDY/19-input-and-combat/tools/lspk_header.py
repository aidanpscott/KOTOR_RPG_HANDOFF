#!/usr/bin/env python3
"""Read an LSPK (Larian pak) HEADER only. No decompression, no dependencies.

⚠ FileListSize INCLUDES the 8-byte numFiles+compressedSize prefix, so a whole
archive satisfies FileListOffset + FileListSize == filesize EXACTLY.
An earlier version added 8 again and declared four intact archives truncated
by exactly 8 bytes each -- the identical shortfall was the tell.
"""
import struct, sys, os

for path in sys.argv[1:]:
    size = os.path.getsize(path)
    with open(path, 'rb') as f:
        head = f.read(64)
    magic, ver = struct.unpack_from('<4sI', head, 0)
    if magic != b'LSPK':
        print(f"{os.path.basename(path)}: NOT LSPK (magic={magic!r})"); continue
    flo, fls, flags, prio = struct.unpack_from('<QIBB', head, 8)
    parts = struct.unpack_from('<H', head, 38)[0] if ver >= 16 else 1
    with open(path, 'rb') as f:
        f.seek(flo); nf, csz = struct.unpack('<II', f.read(8))
    tail = flo + fls
    print(f"{os.path.basename(path):22s} v{ver} parts={parts} size={size:,}")
    print(f"{'':22s} filelist @{flo:,} len {fls:,} -> {tail:,}  "
          f"{'ENDS EXACTLY AT EOF ✓ complete' if tail == size else f'⚠ off by {tail-size:+,}'}")
    print(f"{'':22s} numFiles={nf:,}  compressedList={csz:,}  "
          f"(+8 = {csz+8:,} vs fls {fls:,} {'✓' if csz+8==fls else '⚠'})")
