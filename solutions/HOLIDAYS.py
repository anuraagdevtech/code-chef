import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, w = int(data[pos]), int(data[pos + 1])
        a = sorted((int(v) for v in data[pos + 2:pos + 2 + n]), reverse=True)
        pos += 2 + n
        earned = 0
        worked = 0
        # Work the best-paying days first to reach W in the fewest days.
        for v in a:
            if earned >= w:
                break
            earned += v
            worked += 1
        out.append(str(n - worked))
    sys.stdout.write("\n".join(out) + "\n")


main()
