import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        # Each coordinate appears twice per rectangle, so XOR leaves the
        # one whose partner is missing. The two axes fold independently.
        x = y = 0
        for i in range(4 * n - 1):
            x ^= int(data[pos + 2 * i])
            y ^= int(data[pos + 2 * i + 1])
        pos += 2 * (4 * n - 1)
        out.append(f"{x} {y}")
    sys.stdout.write("\n".join(out) + "\n")


main()
