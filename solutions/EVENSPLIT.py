import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        s = data[pos + 1]
        pos += 2
        if n <= 2:
            # The only even-length subsequence is the whole string, and the
            # move is then the identity, so nothing can be rearranged.
            out.append(s.decode())
        else:
            zeros = s.count(b"0")
            out.append("0" * zeros + "1" * (n - zeros))
    sys.stdout.write("\n".join(out) + "\n")


main()
