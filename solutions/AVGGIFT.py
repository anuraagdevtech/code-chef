import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        vals = [int(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        # Zero is reachable iff some shifted value is 0, or signs differ.
        out.append("YES" if min(vals) <= x <= max(vals) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
