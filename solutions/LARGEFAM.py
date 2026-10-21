import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        claims = sorted(int(x) for x in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # A forest on N nodes has at most N - 1 nodes with a parent.
        budget = n - 1
        told = 0
        for c in claims:
            if c > budget:
                break
            budget -= c
            told += 1
        out.append(str(told))
    sys.stdout.write("\n".join(out) + "\n")


main()
