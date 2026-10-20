import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        total = sum(v for v in a if v > 0)
        # Ascending order puts the most negative first; flipping one is worth
        # its magnitude. Flipping a positive would never help.
        for i in range(min(k, n)):
            if a[i] >= 0:
                break
            total += -a[i]
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
