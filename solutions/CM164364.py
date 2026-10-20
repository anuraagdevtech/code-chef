import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        flavours = set(data[pos + 2:pos + 2 + n])
        pos += 2 + n
        # Limited both by how many flavours exist and by how many she may eat.
        out.append(str(min(len(flavours), n - x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
