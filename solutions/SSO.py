import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        counts = [0] * 48
        for _ in range(n):
            x = next(tokens)
            while x:
                bit = x & -x
                counts[bit.bit_length() - 1] += 1
                x -= bit
        answer = 0
        for i in range(47):
            if counts[i]:
                answer |= 1 << i
            counts[i + 1] += counts[i] // 2
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
