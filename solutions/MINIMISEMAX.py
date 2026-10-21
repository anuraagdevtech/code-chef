import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Biggest run of ones, versus the whole array's fixed sum.
        block = -(-x // (y + 1))
        whole = x - 2 * y
        out.append(str(block if block > whole else whole))
    sys.stdout.write("\n".join(out) + "\n")


main()
