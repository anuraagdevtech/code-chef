import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        # Four "name goals" pairs in arbitrary order, so index them by name.
        goals = {}
        for _ in range(4):
            goals[data[pos].decode()] = int(data[pos + 1])
            pos += 2
        # Barcelona takes the title only if Real Madrid lose and they win.
        barca = goals["RealMadrid"] < goals["Malaga"] and goals["Barcelona"] > goals["Eibar"]
        out.append("Barcelona" if barca else "RealMadrid")
    sys.stdout.write("\n".join(out) + "\n")


main()
