import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        ages = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # Both 10 and 60 are eligible, so the range is closed at both ends.
        out.append(str(sum(1 for a in ages if 10 <= int(a) <= 60)))
    sys.stdout.write("\n".join(out) + "\n")


main()
