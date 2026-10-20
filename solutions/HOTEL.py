import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        arrive = data[pos + 1:pos + 1 + n]
        depart = data[pos + 1 + n:pos + 1 + 2 * n]
        pos += 1 + 2 * n
        events = [(int(v), 1) for v in arrive] + [(int(v), -1) for v in depart]
        # Sorting by (time, delta) puts -1 before +1, so a guest leaving at
        # time x never overlaps one arriving at x.
        events.sort()
        cur = best = 0
        for _, delta in events:
            cur += delta
            if cur > best:
                best = cur
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
