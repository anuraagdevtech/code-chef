import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        # The LIS value doubles as the digit: >= 1 so no leading zero, and
        # <= 9 because n <= 9.
        out.append(b"".join(data[pos + 1:pos + 1 + n]).decode())
        pos += 1 + n
    sys.stdout.write("\n".join(out) + "\n")


main()
