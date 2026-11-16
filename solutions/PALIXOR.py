import sys
from collections import Counter


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    palindromes = [x for x in range(32768) if str(x) == str(x)[::-1]]

    def transform(table):
        half = 1
        n = len(table)
        while half < n:
            for j in range(0, n, 2 * half):
                for i in range(j, j + half):
                    x = table[i]
                    y = table[i + half]
                    table[i] = x + y
                    table[i + half] = x - y
            half *= 2
    for _ in range(next(tokens)):
        n = next(tokens)
        freq = Counter((next(tokens) for _ in range(n)))
        if len(freq) * len(palindromes) < 1500000:
            total = sum((v * freq.get(x ^ p, 0) for x, v in freq.items() for p in palindromes))
        else:
            table = [0] * 32768
            for x, v in freq.items():
                table[x] = v
            transform(table)
            table = [x * x for x in table]
            transform(table)
            total = sum((table[p] for p in palindromes)) // 32768
        out.append(str((total + n) // 2))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
