import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        count = Counter(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        if x == 0:
            out.append(f"{max(count.values())} 0")
            continue
        best = (0, 0)
        for a, c in count.items():
            other = count.get(a ^ x, 0)
            # Either side of the orbit can be the target; flip the smaller one.
            cand = (c + other, -min(c, other))
            if cand > best:
                best = cand
        out.append(f"{best[0]} {-best[1]}")
    sys.stdout.write("\n".join(out) + "\n")


main()
