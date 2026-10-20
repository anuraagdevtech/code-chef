import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        # One party per day, so friends sharing a day compete for it.
        days = set(data[pos + 1:pos + 1 + n])
        pos += 1 + n
        out.append(str(len(days)))
    sys.stdout.write("\n".join(out) + "\n")


main()
