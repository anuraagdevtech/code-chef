import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        top = second = 0
        for tok in data[pos + 1:pos + 1 + n]:
            v = int(tok)
            # Track distinct values: a duplicate maximum is not a runner-up.
            if v > top:
                top, second = v, top
            elif second < v < top:
                second = v
        pos += 1 + n
        out.append(str(second))
    sys.stdout.write("\n".join(out) + "\n")


main()
