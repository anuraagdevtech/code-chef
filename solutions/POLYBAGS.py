import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Every item must be carried, so a part-full bag still counts.
        out.append(str((n + 9) // 10))
    sys.stdout.write("\n".join(out) + "\n")


main()
