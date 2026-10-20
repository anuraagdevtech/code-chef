import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        profits = list(map(int, data[1 + 4 * i:5 + 4 * i]))
        # Only the largest can dominate: max > sum - max  <=>  2 * max > sum.
        out.append("YES" if 2 * max(profits) > sum(profits) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
