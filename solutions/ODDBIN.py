import sys
from functools import lru_cache


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        count = next(tokens)
        exponents = set()
        for _ in range(count):
            x = next(tokens)
            if x in exponents:
                exponents.remove(x)
            else:
                exponents.add(x)

        @lru_cache(None)
        def solve(values):
            if not values:
                return 0
            if len(values) == 1:
                return 1 << values[0].bit_count()
            bit = 1 << values[-1].bit_length() - 1
            low = set()
            high = []
            for x in values:
                if x & bit:
                    high.append(x ^ bit)
                    x ^= bit
                if x in low:
                    low.remove(x)
                else:
                    low.add(x)
            return solve(tuple(sorted(low))) + solve(tuple(high))
        out.append(str(solve(tuple(sorted(exponents)))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
