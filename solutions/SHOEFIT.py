import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = sum(map(int, data[1 + 3 * i:4 + 3 * i]))
        # All-left (sum 0) or all-right (sum 3) are the only failures.
        out.append("1" if 0 < s < 3 else "0")
    sys.stdout.write("\n".join(out) + "\n")


main()
