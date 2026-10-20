import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        # Input order is X, Y, P, Q: both times, then both wrong counts.
        x, y, p, q = map(int, data[1 + 4 * i:5 + 4 * i])
        chef, chefina = x + 10 * p, y + 10 * q
        # Penalty, so the lower value wins.
        out.append("Chef" if chef < chefina else "Chefina" if chefina < chef else "Draw")
    sys.stdout.write("\n".join(out) + "\n")


main()
