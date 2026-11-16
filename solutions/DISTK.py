import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        extra = next(tokens) - n
        prefix = 1
        while prefix < n and extra >= prefix:
            extra -= prefix
            prefix += 1
        result = list(range(1, prefix + 1))
        if prefix < n:
            result.append(result[prefix - extra - 1])
            result.extend([result[-1]] * (n - prefix - 1))
        out.append(' '.join(map(str, result)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
