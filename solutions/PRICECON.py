import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        prices = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        # Cheap items lose nothing, so the excess must clamp at zero.
        out.append(str(sum(max(0, int(p) - k) for p in prices)))
    sys.stdout.write("\n".join(out) + "\n")


main()
