import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        spans = []
        for _ in range(n):
            spans.append((int(data[pos + 1]), int(data[pos])))   # (right, left)
            pos += 2
        spans.sort()
        bombs = 0
        placed = -1
        for right, left in spans:
            # Bombing the right endpoint reaches as far forward as possible.
            if left > placed:
                bombs += 1
                placed = right
        out.append(str(bombs))
    sys.stdout.write("\n".join(out) + "\n")


main()
