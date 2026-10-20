import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        out.append("<" if a < b else ">" if a > b else "=")
    sys.stdout.write("\n".join(out) + "\n")


main()
