import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # A_1 = 1, then the smallest distinct evens 0, 2, ..., 2(N-2).
        out.append(str(1 + (n - 2) * (n - 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
