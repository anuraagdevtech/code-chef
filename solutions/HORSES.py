import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        s = sorted(int(v) for v in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # The closest pair is always adjacent once sorted.
        out.append(str(min(s[i + 1] - s[i] for i in range(n - 1))))
    sys.stdout.write("\n".join(out) + "\n")


main()
