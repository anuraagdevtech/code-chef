import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        rows = set(data[pos + 2:pos + 2 + n])
        pos += 2 + n
        # Only the K single-bit strings matter; everything else follows by OR.
        ok = all(("0" * b + "1" + "0" * (k - b - 1)).encode() in rows
                 for b in range(k))
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
