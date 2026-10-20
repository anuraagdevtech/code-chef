import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        # Singletons force every chosen element to be divisible by m, and that
        # is also sufficient, so just count those and take all subsets.
        c = sum(1 for v in data[pos + 2:pos + 2 + n] if int(v) % m == 0)
        pos += 2 + n
        out.append(str((1 << c) - 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
