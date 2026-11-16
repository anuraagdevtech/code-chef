import sys
from math import hypot


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        x, y = (next(tokens), next(tokens))
        n, m, k = (next(tokens), next(tokens), next(tokens))
        first = [(next(tokens), next(tokens)) for _ in range(n)]
        second = [(next(tokens), next(tokens)) for _ in range(m)]
        finish = [(next(tokens), next(tokens)) for _ in range(k)]
        start_to_first = [hypot(u - x, v - y) for u, v in first]
        start_to_second = [hypot(u - x, v - y) for u, v in second]
        first_to_finish = [min((hypot(u - r, v - s) for r, s in finish)) for u, v in first]
        second_to_finish = [min((hypot(u - r, v - s) for r, s in finish)) for u, v in second]
        best = float('inf')
        for i, (u, v) in enumerate(first):
            for j, (r, s) in enumerate(second):
                best = min(best, hypot(u - r, v - s) + min(start_to_first[i] + second_to_finish[j], start_to_second[j] + first_to_finish[i]))
        out.append('%.10f' % best)
    print('\n'.join(out))


if __name__ == "__main__":
    main()
