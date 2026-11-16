import sys
from math import gcd


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        m = next(tokens)
        prefix_gcd = [next(tokens) for _ in range(n)]
        result = [prefix_gcd[0]]
        for i in range(1, n):
            ratio = prefix_gcd[i - 1] // prefix_gcd[i]
            multiplier = m // prefix_gcd[i]
            while gcd(multiplier, ratio) != 1:
                multiplier -= 1
            result.append(prefix_gcd[i] * multiplier)
        out.append(' '.join(map(str, result)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
