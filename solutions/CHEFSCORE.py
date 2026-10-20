import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, y = map(int, data[1 + 3 * i:4 + 3 * i])
        # Reachable scores are k * x for 0 <= k <= n: need both conditions.
        ok = y % x == 0 and y // x <= n
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
