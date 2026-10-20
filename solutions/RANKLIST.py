import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, s = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        deficit = n * (n + 1) // 2 - s
        # k edits can absorb at most k(k+1)/2 of deficit, independent of n.
        k = 0
        while k * (k + 1) // 2 < deficit:
            k += 1
        out.append(str(k))
    sys.stdout.write("\n".join(out) + "\n")


main()
