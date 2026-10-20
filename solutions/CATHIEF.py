import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, k, n = map(int, data[1 + 4 * i:5 + 4 * i])
        d = abs(x - y)
        # Both displacements share the parity of t, so their difference is
        # even - hence the gap must be an even multiple of k.
        ok = d % k == 0 and (d // k) % 2 == 0
        out.append("Yes" if ok else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
