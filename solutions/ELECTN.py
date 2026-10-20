import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        ages = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        # "At least X" is inclusive, so age == x still votes.
        out.append(str(sum(1 for a in ages if int(a) >= x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
