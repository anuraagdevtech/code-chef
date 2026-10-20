import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Captain and vice-captain are different roles, so order matters.
        out.append(str(n * (n - 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
