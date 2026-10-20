import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        cats = data[pos + 2:pos + 2 + n]
        times = data[pos + 2 + n:pos + 2 + 2 * n]
        pos += 2 + 2 * n
        # Cheapest dish per category; times may legitimately be zero.
        best = {}
        for c, b in zip(cats, times):
            v = int(b)
            if c not in best or v < best[c]:
                best[c] = v
        if len(best) < k:
            out.append("-1")
        else:
            out.append(str(sum(sorted(best.values())[:k])))
    sys.stdout.write("\n".join(out) + "\n")


main()
