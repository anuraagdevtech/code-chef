import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k, m = map(int, data[1 + 3 * i:4 + 3 * i])
        cap = k * m          # compose the capacity, then round up once
        out.append(str((n + cap - 1) // cap))
    sys.stdout.write("\n".join(out) + "\n")


main()
