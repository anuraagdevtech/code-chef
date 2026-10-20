import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        h, x, y = map(int, data[1 + 3 * i:4 + 3 * i])
        plain = (h + x - 1) // x
        rest = max(0, h - y)                       # the special may finish it
        with_special = 1 + (rest + x - 1) // x
        # The special only helps when it saves a whole plain attack.
        out.append(str(min(plain, with_special)))
    sys.stdout.write("\n".join(out) + "\n")


main()
