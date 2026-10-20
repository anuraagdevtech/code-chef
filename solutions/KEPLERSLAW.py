import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        t1, t2, r1, r2 = map(int, data[1 + 4 * i:5 + 4 * i])
        # T^2 / R^3 equal for both, cross-multiplied to stay in integers.
        out.append("Yes" if t1 * t1 * r2 ** 3 == t2 * t2 * r1 ** 3 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
