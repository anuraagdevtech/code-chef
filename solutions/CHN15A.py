import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        vals = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        # Equivalently: count the values already congruent to -k (mod 7).
        out.append(str(sum(1 for v in vals if (int(v) + k) % 7 == 0)))
    sys.stdout.write("\n".join(out) + "\n")


main()
