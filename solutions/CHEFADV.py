import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m, x, y = map(int, data[1 + 4 * i:5 + 4 * i])
        plain = (n - 1) % x == 0 and (m - 1) % y == 0
        # ShareChat raises both counters or neither, so both tests apply.
        boosted = n >= 2 and m >= 2 and (n - 2) % x == 0 and (m - 2) % y == 0
        out.append("Chefirnemo" if plain or boosted else "Pofik")
    sys.stdout.write("\n".join(out) + "\n")


main()
