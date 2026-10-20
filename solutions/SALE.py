import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        prices = list(map(int, data[1 + 3 * i:4 + 3 * i]))
        # Exactly one item is free, even if several tie for cheapest.
        out.append(str(sum(prices) - min(prices)))
    sys.stdout.write("\n".join(out) + "\n")


main()
