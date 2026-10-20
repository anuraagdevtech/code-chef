import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Each half must total n(n+1)/4, which is only an integer when 4 | n.
        if n % 4:
            out.append("NO")
            continue
        k = n // 4
        a = list(range(1, k + 1)) + list(range(n - k + 1, n + 1))
        b = list(range(k + 1, n - k + 1))
        out.append("YES")
        out.append(" ".join(map(str, a)))
        out.append(" ".join(map(str, b)))
    sys.stdout.write("\n".join(out) + "\n")


main()
