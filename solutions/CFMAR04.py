import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n = int(next(tokens))
    counts = Counter()
    for _ in range(n):
        frequency = [0]*26
        for c in next(tokens):
            frequency[c-97] += 1
        counts[tuple(frequency)] += 1
    print(max(counts.values()))

if __name__ == '__main__':
    main()
