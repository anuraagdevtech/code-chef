import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n, k = (next(tokens), next(tokens))
        ways = [1] * (n + 1)
        for i in range(k, n + 1):
            ways[i] = (ways[i - 1] + ways[i - k]) % 1000000007
        out.append(str(ways[n]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
