import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        rows = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # Flipping the diagonal differs from row i exactly at position i.
        out.append("".join("1" if rows[i][i] == 0x30 else "0" for i in range(n)))
    sys.stdout.write("\n".join(out) + "\n")


main()
