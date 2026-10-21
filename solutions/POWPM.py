import sys
from bisect import bisect_right


def iroot(a: int, j: int) -> int:
    """Largest r with r**j <= a."""
    if j == 1:
        return a
    r = int(round(a ** (1.0 / j)))
    while r > 1 and r ** j > a:
        r -= 1
    while (r + 1) ** j <= a:
        r += 1
    return r


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        ordered = sorted(a)
        ones = bisect_right(ordered, 1)
        total = ones * n                  # A_i = 1 pairs with every j
        # A_i >= 2 forces 2^j <= 10^9, so only j <= 29 can ever work.
        for j in range(1, min(n, 30) + 1):
            limit = iroot(a[j - 1], j)
            if limit >= 2:
                total += bisect_right(ordered, limit) - ones
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
