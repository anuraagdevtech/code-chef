import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # P_i = i - 1 for i >= 2, and 0 < i - 1 < i can never be a multiple
        # of i. The wrapped N lands at index 1, which is unconstrained.
        out.append(" ".join(map(str, [n] + list(range(1, n)))))
    sys.stdout.write("\n".join(out) + "\n")


main()
