import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        x1, y1 = int(data[pos + 2]), int(data[pos + 3])
        x2, y2 = int(data[pos + 4]), int(data[pos + 5])
        pos += 6
        base = (x1 + y1) % 2
        # Same parity means two colours cannot separate the fixed cells.
        other = 2 if (x2 + y2) % 2 != base else 3
        for r in range(1, n + 1):
            row = [1 if (r + c) % 2 == base else other for c in range(1, m + 1)]
            if other == 3 and r == x2:
                row[y2 - 1] = 2        # its neighbours all carry 3
            out.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out) + "\n")


main()
