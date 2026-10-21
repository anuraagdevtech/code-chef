import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        b = [int(x) for x in data[pos + 1 + n:pos + 1 + 2 * n]]
        pos += 1 + 2 * n
        # Strongest ground power first; a trainer survives if its water power
        # beats everything already seen.
        best_water = 0
        qualified = 0
        for i in sorted(range(n), key=lambda j: -a[j]):
            if b[i] > best_water:
                qualified += 1
                best_water = b[i]
        out.append(str(qualified))
    sys.stdout.write("\n".join(out) + "\n")


main()
