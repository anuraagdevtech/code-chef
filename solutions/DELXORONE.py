import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        # Values are bounded by n, so a plain list beats a dictionary here.
        groups = [0] * (n // 2 + 2)
        for v in data[pos + 1:pos + 1 + n]:
            groups[int(v) >> 1] += 1
        pos += 1 + n
        # Every kept pair must XOR to 0 or 1, so they share v >> 1.
        out.append(str(n - max(groups)))
    sys.stdout.write("\n".join(out) + "\n")


main()
