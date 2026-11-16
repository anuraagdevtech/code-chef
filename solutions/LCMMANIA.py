import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        if n < 3:
            out.append('-1')
        elif n % 3 == 0:
            out.append(f'{n // 3} {n // 3} {n // 3}')
        elif n % 2:
            out.append(f'1 1 {(n - 1) // 2}')
        else:
            power = n & -n
            odd_part = n // power
            out.append('-1' if odd_part == 1 else f'{power} {power} {power * ((odd_part - 1) // 2)}')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
