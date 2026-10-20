import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        out.append("wins" if s == s[::-1] else "loses")
    sys.stdout.write("\n".join(out) + "\n")


main()
