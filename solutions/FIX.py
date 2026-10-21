import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        top = max(a)
        in_b = set()
        b = []
        for v in a:
            # Forced only when this value is still missing from B.
            pick = v if v not in in_b else top
            in_b.add(pick)
            b.append(pick)
        out.append(" ".join(map(str, b)))
    sys.stdout.write("\n".join(out) + "\n")


main()
