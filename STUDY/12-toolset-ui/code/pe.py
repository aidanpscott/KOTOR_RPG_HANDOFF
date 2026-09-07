"""Minimal PE reader: sections, imports, resource tree. No external deps."""
import struct

class PE:
    def __init__(self, path):
        self.d = open(path, 'rb').read()
        e_lfanew = struct.unpack_from('<I', self.d, 0x3c)[0]
        assert self.d[e_lfanew:e_lfanew+4] == b'PE\0\0', 'not a PE'
        coff = e_lfanew + 4
        (self.machine, self.nsec, self.timestamp, _, _,
         self.optsize, self.chars) = struct.unpack_from('<HHIIIHH', self.d, coff)
        opt = coff + 20
        self.magic = struct.unpack_from('<H', self.d, opt)[0]
        self.pe32plus = (self.magic == 0x20b)
        nrva_off = opt + (108 if self.pe32plus else 92)
        self.nrva = struct.unpack_from('<I', self.d, nrva_off)[0]
        dd = nrva_off + 4
        self.dirs = [struct.unpack_from('<II', self.d, dd + 8*i) for i in range(self.nrva)]
        st = opt + self.optsize
        self.sections = []
        for i in range(self.nsec):
            o = st + 40*i
            name = self.d[o:o+8].rstrip(b'\0').decode('latin1')
            vsize, vaddr, rsize, raddr = struct.unpack_from('<IIII', self.d, o+8)
            ch = struct.unpack_from('<I', self.d, o+36)[0]
            self.sections.append((name, vaddr, vsize, raddr, rsize, ch))

    def off(self, rva):
        for name, va, vs, ra, rs, ch in self.sections:
            if va <= rva < va + max(vs, rs):
                return ra + (rva - va)
        return None

    def cstr(self, off, limit=512):
        if off is None: return ''
        e = self.d.find(b'\0', off, off+limit)
        return self.d[off:e if e >= 0 else off+limit].decode('latin1')

    # ---------------- imports
    def imports(self):
        if len(self.dirs) < 2: return []
        rva, size = self.dirs[1]
        if not rva: return []
        o = self.off(rva); out = []
        while True:
            ilt, ts, fc, namerva, iat = struct.unpack_from('<IIIII', self.d, o)
            if namerva == 0: break
            dll = self.cstr(self.off(namerva))
            funcs = []
            t = self.off(ilt or iat)
            if t is not None:
                while True:
                    v = struct.unpack_from('<I', self.d, t)[0]
                    if v == 0: break
                    if not (v & 0x80000000):
                        h = self.off(v)
                        if h is not None:
                            funcs.append(self.d[h+2:self.d.find(b'\0', h+2)].decode('latin1'))
                    else:
                        funcs.append('#%d' % (v & 0xffff))
                    t += 4
            out.append((dll, funcs)); o += 20
        return out

    # ---------------- resources
    def _rdir(self, base, off, depth, path, out):
        chars, tstamp, mj, mn, nnamed, nid = struct.unpack_from('<IIHHHH', self.d, off)
        for i in range(nnamed + nid):
            eo = off + 16 + 8*i
            nameid, dataoff = struct.unpack_from('<II', self.d, eo)
            if nameid & 0x80000000:
                no = base + (nameid & 0x7fffffff)
                ln = struct.unpack_from('<H', self.d, no)[0]
                key = self.d[no+2:no+2+ln*2].decode('utf-16-le')
            else:
                key = nameid
            if dataoff & 0x80000000:
                self._rdir(base, base + (dataoff & 0x7fffffff), depth+1, path+[key], out)
            else:
                do = base + dataoff
                drva, dsize, cp, _ = struct.unpack_from('<IIII', self.d, do)
                out.append((path+[key], self.off(drva), dsize))

    def resources(self):
        if len(self.dirs) < 3: return []
        rva, size = self.dirs[2]
        if not rva: return []
        base = self.off(rva); out = []
        self._rdir(base, base, 0, [], out)
        return out

RT = {1:'CURSOR',2:'BITMAP',3:'ICON',4:'MENU',5:'DIALOG',6:'STRING',7:'FONTDIR',
      8:'FONT',9:'ACCELERATOR',10:'RCDATA',11:'MESSAGETABLE',12:'GROUP_CURSOR',
      14:'GROUP_ICON',16:'VERSION',17:'DLGINCLUDE',19:'PLUGPLAY',20:'VXD',
      21:'ANICURSOR',22:'ANIICON',23:'HTML',24:'MANIFEST',240:'TOOLBAR(MFC)'}
