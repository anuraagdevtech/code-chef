import sys

EQUINOX = set(b"EQUINOX")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, a, b = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        words = data[pos + 3:pos + 3 + n]
        pos += 3 + n
        sarthak = anuradha = 0
        for word in words:
            # Only the first character is consulted.
            if word[0] in EQUINOX:
                sarthak += a
            else:
                anuradha += b
        out.append("SARTHAK" if sarthak > anuradha
                   else "ANURADHA" if anuradha > sarthak else "DRAW")
    sys.stdout.write("\n".join(out) + "\n")


main()
