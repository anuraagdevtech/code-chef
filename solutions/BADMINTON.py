import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        p = int(data[1 + i])
        # Chef serves once at each of his scores 0..p; even scores are right.
        out.append(str(p // 2 + 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
