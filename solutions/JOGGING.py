import sys

MOD = 10 ** 9 + 7


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Each kilometre doubles the running total, starting from x.
        out.append(str(x % MOD * pow(2, n - 1, MOD) % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
