import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        first = next(tokens)
        target = next(tokens)
        answer = -1
        if target % first == 0:
            units = target // first
            for streaks in range(1, 61):
                shifted = units + streaks
                if shifted % 2 == 0 and shifted.bit_count() == streaks:
                    answer = sum((i for i in range(1, shifted.bit_length()) if shifted >> i & 1)) + streaks - 1
                    break
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
