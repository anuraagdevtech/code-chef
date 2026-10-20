import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, x, y = map(int, data[1 + 4 * i:5 + 4 * i])
        # Times a/x and b/y, cross-multiplied. Time is not rounded to minutes.
        chef, chefina = a * y, b * x
        out.append("Chef" if chef < chefina else "Chefina" if chefina < chef else "Both")
    sys.stdout.write("\n".join(out) + "\n")


main()
