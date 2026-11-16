import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    LIMIT = 100000
    sieve = bytearray(b'\x01') * (LIMIT + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, 317):
        if sieve[p]:
            sieve[p * p:LIMIT + 1:p] = b'\x00' * ((LIMIT - p * p) // p + 1)
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        isolated = [1] + [p for p in range(n // 2 + 1, n + 1) if sieve[p]]
        if k <= len(isolated):
            out.append('YES')
            out.append(' '.join(map(str, isolated[:k])))
        elif n - k <= len(isolated):
            removed = set(isolated[:n - k])
            out.append('YES')
            out.append(' '.join((str(i) for i in range(1, n + 1) if i not in removed)))
        else:
            out.append('NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
