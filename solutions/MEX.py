import sys

LIMIT = 2 * 10 ** 5 + 10 ** 5 + 2


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        present = bytearray(LIMIT)
        for v in data[pos + 2:pos + 2 + n]:
            present[int(v)] = 1
        pos += 2 + n
        # Walk upward, buying each missing value until the budget runs out.
        m = 0
        while m < LIMIT:
            if not present[m]:
                if k == 0:
                    break
                k -= 1
            m += 1
        out.append(str(m))
    sys.stdout.write("\n".join(out) + "\n")


main()
