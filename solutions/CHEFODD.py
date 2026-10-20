import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        odds = (n + 1) // 2
        # Each part needs two elements, and each needs an odd count of odds.
        ok = n >= 2 * k and odds % 2 == k % 2
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
