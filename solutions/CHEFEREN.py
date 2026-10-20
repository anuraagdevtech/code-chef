import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, a, b = map(int, data[1 + 3 * i:4 + 3 * i])
        # Episodes are numbered from 1, so the odd positions take the extra one.
        odd, even = (n + 1) // 2, n // 2
        out.append(str(b * odd + a * even))
    sys.stdout.write("\n".join(out) + "\n")


main()
