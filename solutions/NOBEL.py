import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        topics = set(data[pos + 2:pos + 2 + n])
        pos += 2 + n
        # Chef needs an entirely empty field, so only coverage matters.
        out.append("Yes" if len(topics) < m else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
