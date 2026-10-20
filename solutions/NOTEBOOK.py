import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # 1000 pages per kg / 100 pages per notebook = 10 notebooks per kg.
        out.append(str(10 * n))
    sys.stdout.write("\n".join(out) + "\n")


main()
