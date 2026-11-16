import sys
from functools import cmp_to_key


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        lengths = [next(tokens) for _ in range(n)]
        beauties = [next(tokens) for _ in range(n)]
        rods = sorted(zip(lengths, beauties), key=cmp_to_key(lambda x, y: (x[1] * y[0] > y[1] * x[0]) - (x[1] * y[0] < y[1] * x[0])))
        position = total = 0
        for length, beauty in rods:
            total += position * beauty
            position += length
        out.append(str(total))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
