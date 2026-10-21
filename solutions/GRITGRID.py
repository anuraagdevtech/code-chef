import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m, x, y = (int(data[1 + 4 * i]), int(data[2 + 4 * i]),
                      int(data[3 + 4 * i]), int(data[4 + 4 * i]))
        # Equal move parities fix the colour gap; unequal ones let k choose it.
        ok = x % 2 != y % 2 or (n + m) % 2 == x % 2
        out.append("Yes" if ok else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
