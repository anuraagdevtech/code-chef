import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        runs = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        total = 0
        hits = 0
        for i, r in enumerate(runs, 1):
            total += int(r)
            # Strike rate is 100 exactly when runs == balls faced.
            if total == i:
                hits += 1
        out.append(str(hits))
    sys.stdout.write("\n".join(out) + "\n")


main()
