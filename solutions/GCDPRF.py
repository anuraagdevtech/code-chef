import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        b = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Each prefix GCD must divide the previous one; then B realises itself.
        if all(b[i - 1] % b[i] == 0 for i in range(1, n)):
            out.append(" ".join(map(str, b)))
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
