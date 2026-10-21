import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted((int(v) for v in data[pos + 1:pos + 1 + n]), reverse=True)
        pos += 1 + n
        if a[0] == a[1]:
            # Copies of the maximum must be kept mutually non-adjacent.
            p = sum(1 for v in a if v == a[0])
            ok = p <= (n + 1) // 2
        else:
            # The unique maximum sits at an end; its neighbour must be below b2.
            q = sum(1 for v in a if v == a[1])
            ok = n >= q + 2
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
