import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        full = sum(map(int, data[1 + 3 * i:4 + 3 * i]))
        # At least two empty  <=>  at most one full.
        out.append("Water filling time" if full <= 1 else "Not now")
    sys.stdout.write("\n".join(out) + "\n")


main()
