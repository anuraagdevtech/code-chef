import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        ratings = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # "Keep strictly below 1000" means 1000 itself has to go.
        out.append(str(sum(1 for d in ratings if int(d) >= 1000)))
    sys.stdout.write("\n".join(out) + "\n")


main()
