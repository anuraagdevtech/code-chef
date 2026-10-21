import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        vals = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # A_i | i is invariant, and conversely pairing i with index B_i
        # realises any divisor without disturbing the pivot.
        ok = all(i % int(v) == 0 for i, v in enumerate(vals, 1))
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
