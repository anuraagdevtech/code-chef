import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        if (a - b) % 2 or (b - c) % 2:
            out.append("-1")          # pairwise parities never change
            continue
        total = a + b + c
        low = min(a, b, c)
        # The smallest number must not need a negative decrement count.
        floor = max(0, (total - 3 * low + 1) // 2)
        out.append(str(floor + (-total - floor) % 3))
    sys.stdout.write("\n".join(out) + "\n")


main()
