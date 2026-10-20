import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Summing all equations counts each variable n - 1 times.
        total = sum(a) // (n - 1)
        out.append(" ".join(str(total - v) for v in a))
    sys.stdout.write("\n".join(out) + "\n")


main()
