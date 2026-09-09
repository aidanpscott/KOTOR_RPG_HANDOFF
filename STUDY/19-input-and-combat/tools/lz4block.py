#!/usr/bin/env python3
"""lz4block.py — LZ4 *block* decompression, pure stdlib.

⚠ BLOCK format, not FRAME. Larian's LSPK stores raw LZ4 blocks with the
uncompressed size known from the container, so there is no frame header and
no magic number to check.

A block is a series of sequences:
  token byte : high nibble = literal length, low nibble = match length - 4
  a nibble of 15 means "read more": add 0xFF bytes until one is < 0xFF
  then the literals, then (unless this was the final sequence)
  a 2-byte little-endian match OFFSET counting BACK from the output cursor,
  then the match length, copied byte-by-byte because matches may overlap.
"""


def decompress(src: bytes, uncompressed_size: int) -> bytes:
    dst = bytearray(uncompressed_size)
    s, d, n = 0, 0, len(src)
    while s < n:
        token = src[s]; s += 1
        lit = token >> 4
        if lit == 15:
            while True:
                b = src[s]; s += 1
                lit += b
                if b != 255:
                    break
        if lit:
            dst[d:d + lit] = src[s:s + lit]
            s += lit; d += lit
        if s >= n:
            break                      # final sequence: literals only
        off = src[s] | (src[s + 1] << 8); s += 2
        if off == 0:
            raise ValueError(f'zero match offset at src {s - 2}, dst {d}')
        mlen = (token & 0x0F) + 4
        if (token & 0x0F) == 15:
            while True:
                b = src[s]; s += 1
                mlen += b
                if b != 255:
                    break
        p = d - off
        if p < 0:
            raise ValueError(f'match before start of output (off={off}, d={d})')
        for _ in range(mlen):          # byte-wise: overlapping matches are legal
            dst[d] = dst[p]
            d += 1; p += 1
    if d != uncompressed_size:
        raise ValueError(f'produced {d} bytes, expected {uncompressed_size}')
    return bytes(dst)


if __name__ == '__main__':
    # control: round-trip a known LZ4 block produced by a different implementation
    # is unavailable offline, so verify against a self-describing property --
    # decompressing must yield EXACTLY the declared size, which decompress()
    # already asserts. Structural test with a hand-built block:
    #   token 0x30 -> 3 literals, no match  => b'abc'
    print(decompress(bytes([0x30]) + b'abc', 3))
    #   3 literals 'abc', then offset 3, matchlen 4 -> 'abcabca'
    print(decompress(bytes([0x30]) + b'abc' + bytes([0x03, 0x00]), 7))   # abcabca
    print(decompress(bytes([0xF0, 0x02]) + b'a' * 17, 17))                # 15+2 literals
