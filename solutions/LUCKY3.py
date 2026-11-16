import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        numbers = [str(next(tokens)) for _ in range(n)]
        answer = 0
        for length in range(1, max(map(len, numbers)) + 1):
            padded = [s.zfill(length) for s in numbers if len(s) <= length]
            size = 4 ** length
            count_below = [0] * size
            for s in padded:
                ix = 0
                power = 1
                for ch in reversed(s):
                    d = int(ch)
                    if d > 7:
                        break
                    level = 0 if d <= 3 else 1 if d == 4 else 2 if d <= 6 else 3
                    ix += level * power
                    power *= 4
                else:
                    count_below[ix] += 1
            power = 1
            for _ in range(length):
                for base in range(0, size, power * 4):
                    for j in range(power):
                        for digit in range(1, 4):
                            count_below[base + digit * power + j] += count_below[base + (digit - 1) * power + j]
                power *= 4
            subtotal = 0
            for ix, count in enumerate(count_below):
                sign = 1
                z = ix
                for _ in range(length):
                    if z % 4 in (0, 2):
                        sign = -sign
                    z //= 4
                subtotal += sign * ((1 << count) - 1)
            answer += subtotal
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
