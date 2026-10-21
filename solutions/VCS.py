import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m, k = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        pos += 3
        ignored = set(data[pos:pos + m])
        pos += m
        tracked = set(data[pos:pos + k])
        pos += k
        # Neither list means outside the union -- subtracting M + K would
        # double-count the files that appear in both.
        out.append(f"{len(ignored & tracked)} {n - len(ignored | tracked)}")
    sys.stdout.write("\n".join(out) + "\n")


main()
