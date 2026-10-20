import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, l, x = map(int, data[1 + 3 * i:4 + 3 * i])
        # The scarcer side caps the pairs; the surplus is unsellable.
        out.append(str(min(l, n - l) * x))
    sys.stdout.write("\n".join(out) + "\n")


main()
