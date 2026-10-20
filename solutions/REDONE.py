import sys

MOD = 10 ** 9 + 7
LIMIT = 10 ** 6 + 2


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    # (1 + x)(1 + y) = 1 + (x + y + xy), so the whole list telescopes to (n+1)!
    fact = [1] * LIMIT
    for i in range(1, LIMIT):
        fact[i] = fact[i - 1] * i % MOD
    out = [str((fact[int(data[1 + i]) + 1] - 1) % MOD) for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
