import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        w1, w2, x1, x2, m = map(int, data[1 + 5 * i:6 + 5 * i])
        gain = w2 - w1
        # Monthly gains vary freely, so every total in the range is reachable.
        out.append("1" if m * x1 <= gain <= m * x2 else "0")
    sys.stdout.write("\n".join(out) + "\n")


main()
