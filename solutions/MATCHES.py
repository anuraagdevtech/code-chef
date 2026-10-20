import sys

# Seven-segment cost of each digit, indexed 0..9.
COST = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # The matches spell out the result, not the operands.
        out.append(str(sum(COST[int(ch)] for ch in str(a + b))))
    sys.stdout.write("\n".join(out) + "\n")


main()
