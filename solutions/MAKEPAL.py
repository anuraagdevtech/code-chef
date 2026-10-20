import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        odds = sum(1 for v in data[pos + 1:pos + 1 + n] if int(v) % 2)
        pos += 1 + n
        # Merging two odd-count characters removes both odd counts at once.
        out.append(str(odds // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
