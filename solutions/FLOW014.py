import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        hardness = float(data[1 + 3 * i])
        carbon = float(data[2 + 3 * i])      # not an integer: compared to 0.7
        tensile = float(data[3 + 3 * i])
        c1 = hardness > 50
        c2 = carbon < 0.7
        c3 = tensile > 5600
        if c1 and c2 and c3:
            g = 10
        elif c1 and c2:
            g = 9
        elif c2 and c3:
            g = 8
        elif c1 and c3:
            g = 7
        elif c1 or c2 or c3:
            g = 6
        else:
            g = 5
        out.append(str(g))
    sys.stdout.write("\n".join(out) + "\n")


main()
