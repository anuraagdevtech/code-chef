import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Winner takes 3(n-1); the rest must share wins among themselves, so
        # the runner-up cannot be held below 3*ceil((n-2)/2). This simplifies.
        out.append(str(3 * (n // 2)))
    sys.stdout.write("\n".join(out) + "\n")


main()
