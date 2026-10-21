import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        s = data[2 + 2 * i]
        first = s.find(b"1")
        # A right-to-left cascade from the first one zeroes the whole tail.
        if 0 <= first <= n - 3:
            out.append("0" * first + "1" + "0" * (n - first - 1))
        else:
            out.append(s.decode())
    sys.stdout.write("\n".join(out) + "\n")


main()
