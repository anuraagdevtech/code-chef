import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a, b = data[pos + 1], data[pos + 2]
        pos += 3
        # Equal suffixes do not count, so the chain starts false.
        less = False
        total = 0
        for i in range(n - 1, -1, -1):
            if a[i] != b[i]:
                less = a[i] < b[i]
            total += less
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
