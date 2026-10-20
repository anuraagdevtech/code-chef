import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        g = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        best = 0
        lowest = int(g[0])
        for v in g[1:]:
            x = int(v)
            # Compare before updating, so the earlier match is strictly earlier.
            if x - lowest > best:
                best = x - lowest
            if x < lowest:
                lowest = x
        out.append(str(best) if best > 0 else "UNFIT")
    sys.stdout.write("\n".join(out) + "\n")


main()
