import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i].decode()
        # "pawri" never contains "party", so one pass cannot cascade.
        out.append(s.replace("party", "pawri"))
    sys.stdout.write("\n".join(out) + "\n")


main()
