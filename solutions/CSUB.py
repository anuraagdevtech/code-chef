import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        # data[pos] is N, which Python does not need.
        s = data[pos + 1]
        pos += 2
        c = s.count(b"1")
        # Choose any two 1s as the ends, plus the single-character cases.
        out.append(str(c * (c + 1) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
