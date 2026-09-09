#!/usr/bin/env python3
"""lspk.py — read Larian LSPK v18 archives (Baldur's Gate 3). stdlib + lz4block.

header (v18): "LSPK" · uint32 version · uint64 FileListOffset ·
              uint32 FileListSize · uint8 Flags · uint8 Priority ·
              byte[16] MD5 · uint16 NumParts
⚠ FileListSize INCLUDES the 8-byte numFiles+compressedSize prefix.

file list: uint32 numFiles · uint32 compressedSize · LZ4-BLOCK data
           decompressing to numFiles * 272 bytes.
entry (272): char[256] name · uint32 offsetLo · uint16 offsetHi ·
             uint8 archivePart · uint8 flags · uint32 sizeOnDisk ·
             uint32 uncompressedSize
flags & 0x0F: 0 = stored, 1 = zlib, 2 = lz4, 3 = zstd
⚠ uncompressedSize == 0 also means stored.
"""
import struct, os, sys, zlib, subprocess
from lz4block import decompress as lz4_decompress

METHOD = {0: 'store', 1: 'zlib', 2: 'lz4', 3: 'zstd'}


class Pak:
    def __init__(self, path):
        self.path = path
        self.size = os.path.getsize(path)
        with open(path, 'rb') as f:
            h = f.read(40)
            magic, self.version = struct.unpack_from('<4sI', h, 0)
            if magic != b'LSPK':
                raise ValueError(f'not LSPK: {magic!r}')
            flo, fls, self.flags, self.priority = struct.unpack_from('<QIBB', h, 8)
            self.parts = struct.unpack_from('<H', h, 38)[0] if self.version >= 16 else 1
            if flo + fls != self.size:
                raise ValueError(f'file list ends {flo+fls} but file is {self.size} '
                                 f'({flo+fls-self.size:+d}) -- archive incomplete?')
            f.seek(flo)
            nfiles, csize = struct.unpack('<II', f.read(8))
            raw = lz4_decompress(f.read(csize), nfiles * 272)
        self.entries = {}
        for i in range(nfiles):
            o = i * 272
            name = raw[o:o+256].split(b'\0')[0].decode('utf-8', 'replace').replace('\\', '/')
            lo, hi, part, fl, sod, usz = struct.unpack_from('<IHBBII', raw, o+256)
            self.entries[name] = (lo | (hi << 32), part, fl, sod, usz)

    def _partpath(self, part):
        if part == 0:
            return self.path
        base, ext = os.path.splitext(self.path)
        return f'{base}_{part}{ext}'

    def read(self, name):
        off, part, fl, sod, usz = self.entries[name]
        with open(self._partpath(part), 'rb') as f:
            f.seek(off); blob = f.read(sod)
        m = fl & 0x0F
        if m == 0 or usz == 0:
            return blob
        if m == 1:
            return zlib.decompress(blob)
        if m == 2:
            return lz4_decompress(blob, usz)
        if m == 3:
            # no zstd module on this machine; /usr/bin/zstd handles the frame
            r = subprocess.run(['zstd', '-d', '-c', '-'], input=blob,
                               capture_output=True)
            if r.returncode:
                raise ValueError(f'zstd failed: {r.stderr[:200]!r}')
            return r.stdout
        raise ValueError(f'unknown compression method {m} (flags 0x{fl:02x})')


if __name__ == '__main__':
    p = Pak(sys.argv[1])
    if len(sys.argv) == 2:
        from collections import Counter
        c = Counter(METHOD.get(v[2] & 0x0F, v[2] & 0x0F) for v in p.entries.values())
        print(f'v{p.version} parts={p.parts} {len(p.entries):,} entries  {dict(c)}')
    elif sys.argv[2] == '--list':
        pat = sys.argv[3].lower() if len(sys.argv) > 3 else ''
        for n in sorted(p.entries):
            if pat in n.lower():
                off, part, fl, sod, usz = p.entries[n]
                print(f'{usz:>10,}  {METHOD.get(fl & 0x0F, fl & 0x0F):5s}  {n}')
    else:
        sys.stdout.buffer.write(p.read(sys.argv[2]))
