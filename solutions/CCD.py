import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        q = int(next(tokens))
        source = next(tokens)
        target = next(tokens)
        prefix = [0]
        for i in range(n):
            prefix.append((prefix[-1] + (target[i] - source[i]) * (1 if i % 2 == 0 else -1)) % 26)
        for _ in range(q):
            left = int(next(tokens))
            right = int(next(tokens))
            out.append('YES' if prefix[right] == prefix[left - 1] else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
