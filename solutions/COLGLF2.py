import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        s = int(data[pos])
        q = [int(v) for v in data[pos + 1:pos + 1 + s]]
        pos += 1 + s
        total = 0
        for i in range(s):
            e = int(data[pos])
            total += sum(int(v) for v in data[pos + 1:pos + 1 + e])
            # The intro is watched once per season, skipped e - 1 times.
            total -= q[i] * (e - 1)
            pos += 1 + e
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
