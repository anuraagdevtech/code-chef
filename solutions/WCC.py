import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + 2 * i])
        s = data[2 + 2 * i].decode()
        draws = s.count("D")
        carlsen = 2 * s.count("C") + draws
        chef = 2 * s.count("N") + draws
        # A tie still crowns Carlsen, but pays 55 rather than 60.
        if carlsen > chef:
            out.append(str(60 * x))
        elif chef > carlsen:
            out.append(str(40 * x))
        else:
            out.append(str(55 * x))
    sys.stdout.write("\n".join(out) + "\n")


main()
