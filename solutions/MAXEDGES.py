import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k, l = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        # Vertices that must be both source and sink end up isolated.
        both = k + l - n
        if both < 0:
            both = 0
        n -= both
        k -= both
        l -= both
        out.append(str(n * (n - 1) // 2 - k * (k - 1) // 2 - l * (l - 1) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
