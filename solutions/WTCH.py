import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        towers = bytearray(data[2 + 2 * i])
        placed = 0
        for j in range(n):
            # Placing as early as legal never blocks a later opportunity.
            if towers[j] == 0x30 \
                    and (j == 0 or towers[j - 1] == 0x30) \
                    and (j == n - 1 or towers[j + 1] == 0x30):
                towers[j] = 0x31
                placed += 1
        out.append(str(placed))
    sys.stdout.write("\n".join(out) + "\n")


main()
