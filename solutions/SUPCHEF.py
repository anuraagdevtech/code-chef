import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        m, n, k = map(int, data[1 + 3 * i:4 + 3 * i])
        # "Strictly before" - finishing exactly at minute M is too late.
        out.append("YES" if n * k < m else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
