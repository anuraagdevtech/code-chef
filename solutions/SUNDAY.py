import sys

# Day 1 is a Monday, so in a 30-day month these are the Saturdays and Sundays.
WEEKEND = {6, 7, 13, 14, 20, 21, 27, 28}


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        fests = {int(v) for v in data[pos + 1:pos + 1 + n]}
        pos += 1 + n
        # A festival may fall on a weekend, so union rather than add.
        out.append(str(len(WEEKEND | fests)))
    sys.stdout.write("\n".join(out) + "\n")


main()
