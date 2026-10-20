import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        if n == 1:
            out.append("1 1")
            continue
        # 1..n-1 distinct, then repeat n-1, then absorb the remainder.
        vals = list(range(1, n)) + [n - 1]
        vals.append((1 << n) - n * (n - 1) // 2 - (n - 1))
        out.append(" ".join(map(str, vals)))
    sys.stdout.write("\n".join(out) + "\n")


main()
