import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])                 # no test-case count
    a = [int(v) for v in data[1:1 + n]]
    b = [int(v) for v in data[1 + n:1 + 2 * n]]
    # Second element descending, first ascending on ties.
    pairs = sorted(zip(a, b), key=lambda p: (-p[1], p[0]))
    out = []
    for first, second in pairs:
        out.append(str(first))
        out.append(str(second))
    sys.stdout.write(" ".join(out) + "\n")


main()
