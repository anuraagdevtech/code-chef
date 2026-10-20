import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Odd positions take odd values, even positions take their doubles.
        a = []
        for j in range(1, n // 2 + 1):
            a.append(2 * j - 1)
            a.append(4 * j - 2)
        if n % 2:
            a.append(n)                  # a lone odd tail has no condition
        out.append(" ".join(map(str, a)))
    sys.stdout.write("\n".join(out) + "\n")


main()
