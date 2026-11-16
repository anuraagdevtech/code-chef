import sys


def main() -> None:
    n, base = map(int, sys.stdin.buffer.read().split())
    MOD = 998244353
    inv = pow(base, -1, MOD)
    half = (MOD + 1) // 2
    mean = second = 0
    weight = 1
    out = []
    for i in range(n):
        second = (second + mean * weight + half * weight * weight) % MOD
        mean = (mean + half * weight) % MOD
        out.append(str(second))
        weight = weight * inv % MOD
    print(' '.join(out))


if __name__ == "__main__":
    main()
