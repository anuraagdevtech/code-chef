import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, k, p = int(data[0]), int(data[1]), int(data[2])
    pos_of = [int(x) for x in data[3:3 + n]]
    order = sorted(range(n), key=pos_of.__getitem__)
    comp = [0] * n
    group = 0
    for rank, idx in enumerate(order):
        # A gap above K cannot be bridged by any edge, so it cuts the line.
        if rank and pos_of[idx] - pos_of[order[rank - 1]] > k:
            group += 1
        comp[idx] = group
    base = 3 + n
    out = []
    for i in range(p):
        a, b = int(data[base + 2 * i]), int(data[base + 2 * i + 1])
        out.append("Yes" if comp[a - 1] == comp[b - 1] else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
