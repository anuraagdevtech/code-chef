import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        m = int(data[pos + 1])
        chains = sorted(int(x) for x in data[pos + 2:pos + 2 + m])
        pos += 2 + m
        # Sacrificing the d cheapest chains supplies pre[d] links but leaves
        # M - d pieces still needing M - d - 1.
        best = m - 1
        used = 0
        for d in range(1, m):
            used += chains[d - 1]
            cost = used if used > m - d - 1 else m - d - 1
            if cost < best:
                best = cost
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
