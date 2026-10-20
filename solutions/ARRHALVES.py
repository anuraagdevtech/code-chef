import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        p = data[pos + 1:pos + 1 + 2 * n]
        pos += 1 + 2 * n
        # Only which half each value lands in matters, not the order within.
        swaps = 0
        target = 0
        for idx, v in enumerate(p):
            if int(v) <= n:
                swaps += idx - target
                target += 1
        out.append(str(swaps))
    sys.stdout.write("\n".join(out) + "\n")


main()
