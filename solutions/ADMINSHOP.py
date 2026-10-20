import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        # Each admin needs n hours; each shop needs ceil(x / a) hours.
        worst = max((x + int(v) - 1) // int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        out.append(str(max(n, worst)))
    sys.stdout.write("\n".join(out) + "\n")


main()
