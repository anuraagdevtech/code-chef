import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        l, r = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # 10 = 1 (mod 3), so a number and its digit sum share a remainder.
        out.append(str(r // 3 - (l - 1) // 3))
    sys.stdout.write("\n".join(out) + "\n")


main()
