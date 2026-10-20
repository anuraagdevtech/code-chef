import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, n = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        needed = (n + 99) // 100      # a part-full plane still flies
        out.append(str(max(0, needed - x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
