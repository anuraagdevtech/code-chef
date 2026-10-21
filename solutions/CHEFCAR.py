import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, v = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        legs = n - 1
        most = n * legs // 2                 # one litre bought at each checkpoint
        if legs <= v:
            least = legs                     # every litre can come from checkpoint 1
        else:
            # V legs at price 1, then prices 2, 3, ... up to N - V.
            least = v + (n - v) * (n - v + 1) // 2 - 1
        out.append(f"{most} {least}")
    sys.stdout.write("\n".join(out) + "\n")


main()
