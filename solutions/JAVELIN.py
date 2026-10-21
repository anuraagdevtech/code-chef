import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m, x = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        a = [int(v) for v in data[pos + 3:pos + 3 + n]]
        pos += 3 + n
        qualified = {i + 1 for i, v in enumerate(a) if v >= m}
        if len(qualified) < x:
            # Top up from the non-qualifiers only, longest throws first.
            rest = sorted(((v, i + 1) for i, v in enumerate(a)
                           if i + 1 not in qualified), reverse=True)
            for _, pid in rest[:x - len(qualified)]:
                qualified.add(pid)
        ids = sorted(qualified)
        out.append(" ".join(map(str, [len(ids)] + ids)))
    sys.stdout.write("\n".join(out) + "\n")


main()
