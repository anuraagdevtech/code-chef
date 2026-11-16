import sys


def main() -> None:
    MOD = 1000000007
    inv5 = pow(5, MOD - 2, MOD)

    def fib(n):
        a, b = (0, 1)
        for bit in bin(n)[2:]:
            c = a * ((2 * b - a) % MOD) % MOD
            d = (a * a + b * b) % MOD
            if bit == '0':
                a, b = (c, d)
            else:
                a, b = (d, (c + d) % MOD)
        return (a, b)
    out = []
    for n in list(map(int, sys.stdin.buffer.read().split()))[1:]:
        fib_n1, fib_n2 = fib(n + 1)
        fib_n3 = (fib_n1 + fib_n2) % MOD
        fib_n4 = (fib_n2 + fib_n3) % MOD
        c1 = ((n + 3) * (2 * fib_n4 - fib_n3) - fib_n3) * inv5 % MOD
        c2 = ((n + 4) * (2 * (fib_n3 + fib_n4) - fib_n4) - fib_n4) * inv5 % MOD
        out.append(str((c1 + c2 - 3 * fib_n2 - 2 * fib_n3 - 3 * fib_n1) % MOD))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
