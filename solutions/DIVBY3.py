import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        bits = next(tokens).decode()
        n = len(bits)
        ones = bits.count('1')
        even_ones = bits[::2].count('1')
        target = 2 * ones % 3
        if even_ones % 3 == target:
            out.append('0')
            continue
        fewest = max(0, ones - n // 2)
        most = min(ones, (n + 1) // 2)
        if fewest + (target - fewest) % 3 > most:
            out.append('-1')
            continue
        first = -1
        last = -1
        single = False
        for i in range(n - 1):
            if bits[i] == bits[i + 1]:
                continue
            effect = 1 if (bits[i] == '0') == (i % 2 == 0) else -1
            if (even_ones + effect) % 3 == target:
                single = True
                break
            if first < 0:
                first = i
            last = i
        out.append('1' if single else '2' if last - first >= 2 else '3')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
