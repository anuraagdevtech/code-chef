import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        a = [int(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        worst = 0
        prefix_max = a[0]
        for j in range(1, n):
            # The costliest inversion ending at j pairs A_j with the largest
            # value before it, when that value is bigger.
            if prefix_max > a[j]:
                worst = max(worst, prefix_max + a[j])
            else:
                prefix_max = a[j]
        out.append("YES" if worst <= x else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
