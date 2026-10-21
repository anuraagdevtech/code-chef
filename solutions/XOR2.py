import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        total = 0
        for v in data[pos + 1:pos + 1 + n]:
            total ^= int(v)
        pos += 1 + n
        # Operations preserve the total XOR; an even-length all-equal array
        # must have total 0.
        out.append("YES" if n % 2 or total == 0 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
