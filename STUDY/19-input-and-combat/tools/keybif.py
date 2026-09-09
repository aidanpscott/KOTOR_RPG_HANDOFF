#!/usr/bin/env python3
"""keybif.py — read BioWare KEY/BIF archives (KOTOR 1, KOTOR 2, NWN).

⚠ Written because it did NOT already exist. The project has readers for GFF,
2DA, ERF/RIM/MOD and TLK; nothing in any of the six repos reads chitin.key or
a BIF. Prior studies used loose files and an external toolset.

KEY V1
  0  char[4] "KEY "   4  char[4] "V1  "
  8  uint32 BIFCount   12 uint32 KeyCount
  16 uint32 OffsetToFileTable   20 uint32 OffsetToKeyTable
  file table entry (12): FileSize(4) FilenameOffset(4) FilenameSize(2) Drives(2)
  key table entry  (22): ResRef(16) ResourceType(2) ResourceID(4)
       ResourceID: bif index = ID >> 20, resource index = ID & 0xFFFFF

BIFF V1
  0  "BIFF" "V1  "  8 VarResCount(4) 12 FixedResCount(4) 16 VarTableOffset(4)
  variable table entry (16): ID(4) Offset(4) FileSize(4) ResourceType(4)
"""
import struct, os, sys

RESTYPE = {2017:'2da', 2029:'ncs', 2010:'nss', 2023:'git', 2012:'are',
           2014:'ifo', 2009:'utc', 2025:'uti', 2027:'utp', 2032:'utw',
           2035:'utt', 2040:'uts', 2044:'ute', 2051:'utm', 2002:'txt',
           2022:'dlg', 2065:'gui', 2064:'ini', 1:'bmp', 2013:'set',
           2036:'dds', 2060:'jrl', 10:'tga', 2005:'wav', 2038:'ltr'}


class KeyIndex:
    def __init__(self, keypath):
        self.root = os.path.dirname(os.path.abspath(keypath))
        d = open(keypath, 'rb').read()
        if d[:4] != b'KEY ':
            raise ValueError(f'not a KEY file: {d[:4]!r}')
        nbif, nkey, ftoff, ktoff = struct.unpack_from('<4I', d, 8)
        self.bifs = []
        for i in range(nbif):
            fs, noff, nsz, drives = struct.unpack_from('<IIHH', d, ftoff + i*12)
            name = d[noff:noff+nsz].split(b'\0')[0].decode('ascii','replace')
            self.bifs.append(name.replace('\\', '/'))
        self.index = {}          # (resref.lower(), restype) -> (bifidx, residx)
        for i in range(nkey):
            o = ktoff + i*22
            ref = d[o:o+16].split(b'\0')[0].decode('ascii','replace').lower()
            rt, rid = struct.unpack_from('<IH', d[o+16:o+22]+b'\0'*4, 0) if False else \
                      struct.unpack_from('<HI', d, o+16)
            self.index[(ref, rt)] = (rid >> 20, rid & 0xFFFFF)

    def _bifpath(self, i):
        # ⚠ the KEY stores BIF paths relative to the INSTALL ROOT. In KOTOR the
        # key sits at the root; in NWN:EE it sits in data/, so 'data/x.bif'
        # must resolve against the PARENT. Try both.
        for base in (self.root, os.path.dirname(self.root)):
            p = os.path.join(base, self.bifs[i])
            if os.path.exists(p): return p
        p = os.path.join(self.root, self.bifs[i])
        # case-insensitive fallback: the archives are named lowercase on disk
        parent, base = os.path.split(p)
        if os.path.isdir(parent):
            for f in os.listdir(parent):
                if f.lower() == base.lower():
                    return os.path.join(parent, f)
        raise FileNotFoundError(p)

    def read(self, resref, restype=2017):
        """Return the bytes of one resource. restype 2017 = .2da"""
        k = (resref.lower(), restype)
        if k not in self.index:
            raise KeyError(f'{resref} type {restype} not in index')
        bi, ri = self.index[k]
        with open(self._bifpath(bi), 'rb') as f:
            hdr = f.read(20)
            if hdr[:4] != b'BIFF':
                raise ValueError(f'not a BIF: {hdr[:4]!r}')
            nvar, nfix, vtoff = struct.unpack_from('<3I', hdr, 8)
            f.seek(vtoff + ri*16)
            _id, off, sz, _rt = struct.unpack('<4I', f.read(16))
            f.seek(off)
            return f.read(sz)

    def listing(self, restype=None):
        for (ref, rt), (bi, ri) in sorted(self.index.items()):
            if restype is None or rt == restype:
                yield ref, rt, RESTYPE.get(rt, str(rt)), self.bifs[bi]


if __name__ == '__main__':
    k = KeyIndex(sys.argv[1])
    if len(sys.argv) == 2:
        print(f'{len(k.bifs)} BIFs, {len(k.index)} resources')
        from collections import Counter
        c = Counter(rt for _, rt in k.index)
        for rt, n in c.most_common(15):
            print(f'  {str(RESTYPE.get(rt, rt)):8s} {n:6d}')
    elif sys.argv[2] == '--list':
        want = int(sys.argv[3]) if len(sys.argv) > 3 else None
        for ref, rt, ext, bif in k.listing(want):
            print(f'{ref}.{ext}\t{bif}')
    else:
        sys.stdout.buffer.write(k.read(sys.argv[2],
                                int(sys.argv[3]) if len(sys.argv) > 3 else 2017))
