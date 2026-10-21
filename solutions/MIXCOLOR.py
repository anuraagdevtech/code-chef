import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        distinct = len(set(data[pos + 1:pos + 1 + n]))
        pos += 1 + n
        # Each mix changes exactly one colour, so every duplicate copy costs one.
        out.append(str(n - distinct))
    sys.stdout.write("\n".join(out) + "\n")


main()
