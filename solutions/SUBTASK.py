import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m, k = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        a = data[pos + 3:pos + 3 + n]
        pos += 3 + n
        # Full pass must be checked first, or a perfect run scores only k.
        if all(v == b"1" for v in a):
            out.append("100")
        elif all(v == b"1" for v in a[:m]):
            out.append(str(k))
        else:
            out.append("0")
    sys.stdout.write("\n".join(out) + "\n")


main()
