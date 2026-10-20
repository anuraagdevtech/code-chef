import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Swaps beyond a full reversal cannot add anything.
        k = min(k, n // 2)
        # Sum over i of 2(n - 2i + 1) - 1, in closed form.
        out.append(str(k * (2 * n + 1) - 2 * k * (k + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
