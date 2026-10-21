import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        vals = [int(x) for x in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        whole = 0
        for v in vals:
            whole = gcd(whole, v)
        pieces = 0
        run = 0
        for v in vals:
            run = gcd(run, v)
            if run == whole:      # cut at the earliest chance and reset
                pieces += 1
                run = 0
        out.append("YES" if pieces >= k else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
