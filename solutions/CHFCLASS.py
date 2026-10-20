import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Day 1 is Monday, so Saturdays are the days d = 6 (mod 7).
        out.append(str((n + 1) // 7))
    sys.stdout.write("\n".join(out) + "\n")


main()
