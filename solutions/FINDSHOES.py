import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # All n right shoes, plus the left shortfall; spare lefts don't help.
        out.append(str(n + max(0, n - m)))
    sys.stdout.write("\n".join(out) + "\n")


main()
