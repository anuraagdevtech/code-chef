import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        n = len(s)
        left = [1] * (n + 1)
        for j in range(1, n + 1):
            ch = s[j - 1]
            if ch == 60:        # '<'
                left[j] = left[j - 1] + 1
            elif ch == 61:      # '='  propagates, it does not reset
                left[j] = left[j - 1]
        right = [1] * (n + 1)
        for j in range(n - 1, -1, -1):
            ch = s[j]
            if ch == 62:        # '>'
                right[j] = right[j + 1] + 1
            elif ch == 61:
                right[j] = right[j + 1]
        # Each slot must satisfy both directions at once.
        out.append(str(max(max(a, b) for a, b in zip(left, right))))
    sys.stdout.write("\n".join(out) + "\n")


main()
