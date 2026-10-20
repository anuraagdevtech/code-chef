import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = [int(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        motu = sorted(a[0::2], reverse=True)       # Motu plays first
        tomu = sorted(a[1::2])
        ms, ts = sum(motu), sum(tomu)
        for i in range(min(k, len(motu), len(tomu))):
            # Trade Motu's biggest for Tomu's smallest while that still helps.
            if motu[i] <= tomu[i]:
                break
            ms += tomu[i] - motu[i]
            ts += motu[i] - tomu[i]
        out.append("YES" if ts > ms else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
