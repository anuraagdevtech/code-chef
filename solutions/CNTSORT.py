import sys

MAX_VALUE = 100


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        # Values are bounded by 100, so tally rather than compare.
        counts = [0] * (MAX_VALUE + 1)
        for v in data[pos + 1:pos + 1 + n]:
            counts[int(v)] += 1
        pos += 1 + n
        parts = []
        for value in range(1, MAX_VALUE + 1):
            if counts[value]:
                parts.extend([str(value)] * counts[value])
        out.append(" ".join(parts))
    sys.stdout.write("\n".join(out) + "\n")


main()
