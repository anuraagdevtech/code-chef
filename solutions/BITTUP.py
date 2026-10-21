import sys

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Per bit, every column of N bits works except the all-ones one.
        out.append(str(pow(pow(2, n, MOD) - 1, m, MOD)))
    sys.stdout.write("\n".join(out) + "\n")


main()
