import sys


def build_spf(limit):
    spf = list(range(limit + 1))
    i = 2
    while i * i <= limit:
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


def divisors_below(v, bound, spf):
    """How many divisors of v are strictly below bound."""
    divs = [1]
    while v > 1:
        p = spf[v]
        power = 0
        while v % p == 0:
            v //= p
            power += 1
        divs = [d * p ** e for d in divs for e in range(power + 1)]
    return sum(1 for d in divs if d < bound)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(t)]
    spf = build_spf(max(m for _, m in cases))
    out = []
    for n, m in cases:
        total = 0
        for b in range(2, n + 1):
            # The nested modulo reduces to a | b * floor(M / b).
            v = b * (m // b)
            if v == 0:              # b > M, so every a < b divides 0
                total += b - 1
            else:
                total += divisors_below(v, b, spf)
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
