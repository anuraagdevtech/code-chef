import sys


def solve(vals):
    target = sorted(vals)
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            s, d = vals[i], vals[j]
            if (s + d) % 2:
                continue
            a, b = (s + d) // 2, (s - d) // 2
            if not (1 <= a <= 10000 and 1 <= b <= 10000):
                continue
            # Verify the whole multiset, which handles duplicates for free.
            if sorted((a + b, a - b, a * b, a // b)) == target:
                return a, b
    return -1, -1


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        vals = [int(v) for v in data[1 + 4 * i:5 + 4 * i]]
        a, b = solve(vals)
        out.append(f"{a} {b}")
    sys.stdout.write("\n".join(out) + "\n")


main()
