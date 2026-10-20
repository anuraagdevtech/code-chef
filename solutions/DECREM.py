import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        l, r = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # The chain needs r - l + 1 decreasing values starting below l, so it
        # only fits when r < 2l; then n = r gives remainders r-l, ..., 1, 0.
        out.append(str(r) if r < 2 * l else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
