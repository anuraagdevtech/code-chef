import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Stable sort, so equal values never create a spurious descent.
        order = sorted(range(n), key=a.__getitem__)
        descents = sum(order[r] > order[r + 1] for r in range(n - 1))
        out.append("YES" if descents <= 1 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
