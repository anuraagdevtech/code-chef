import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # a buys 10% so values the firm at 10a; b buys 20% so values it at 5b.
        first, second = 10 * a, 5 * b
        out.append("FIRST" if first > second else "SECOND" if second > first else "ANY")
    sys.stdout.write("\n".join(out) + "\n")


main()
