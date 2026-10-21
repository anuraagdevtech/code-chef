import sys

BITS = 20
# count[(p, q, r)] = solutions of a|b=p, b|c=q, c|a=r over single bits.
TABLE = {(0, 0, 0): 1, (0, 1, 1): 1, (1, 0, 1): 1, (1, 1, 0): 1,
         (1, 1, 1): 4, (0, 0, 1): 0, (0, 1, 0): 0, (1, 0, 0): 0}


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        p, q, r = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        total = 1
        for b in range(BITS):
            total *= TABLE[(p >> b & 1, q >> b & 1, r >> b & 1)]
            if not total:          # one contradictory bit kills everything
                break
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
