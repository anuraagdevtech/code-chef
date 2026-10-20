import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = [int(v) for v in data[pos + 2:pos + 2 + k]]
        pos += 2 + k
        perm = []
        prev = 0
        for end in a:
            # Largest value first, so no prefix closes before the block ends.
            perm.append(end)
            perm.extend(range(prev + 1, end))
            prev = end
        out.append(" ".join(map(str, perm)))
    sys.stdout.write("\n".join(out) + "\n")


main()
