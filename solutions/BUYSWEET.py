import sys
from bisect import bisect_right


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, money = int(data[pos]), int(data[pos + 1])
        price = [int(x) for x in data[pos + 2:pos + 2 + n]]
        back = [int(x) for x in data[pos + 2 + n:pos + 2 + 2 * n]]
        pos += 2 + 2 * n
        order = sorted(range(n), key=price.__getitem__)
        prices = [price[i] for i in order]
        # Prefix minima of the burn rate, with the price that achieves it.
        best_burn, best_price = [], []
        burn = cheap = None
        for i in order:
            b = price[i] - back[i]
            if burn is None or b < burn:
                burn, cheap = b, price[i]
            best_burn.append(burn)
            best_price.append(cheap)

        bought = 0
        while True:
            j = bisect_right(prices, money) - 1
            if j < 0:
                break
            b, a = best_burn[j], best_price[j]
            k = (money - a) // b + 1
            bought += k
            money -= k * b          # now below a, so the prefix must shrink
        out.append(str(bought))
    sys.stdout.write("\n".join(out) + "\n")


main()
