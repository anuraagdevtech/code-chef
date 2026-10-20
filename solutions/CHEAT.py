import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Today (Monday) is day 1, so Tuesdays are the days d = 2 (mod 7).
        out.append(str((n + 5) // 7))
    sys.stdout.write("\n".join(out) + "\n")


main()
