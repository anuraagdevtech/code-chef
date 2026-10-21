import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1 + 2 * n          # the coordinates do not matter at all
        total = 0
        while n >= 3:
            total += n
            n //= 2               # every second vertex is the largest child
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
