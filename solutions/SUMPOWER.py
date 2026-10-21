import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 3 * i]), int(data[2 + 3 * i])
        s = data[3 + 3 * i]
        steps = n - k
        total = 0
        for p in range(1, n):            # boundary between S_p and S_{p+1}
            if s[p - 1] == s[p]:
                continue
            # How many windows cover this boundary.
            hi = min(steps, p)
            lo = max(1, p - k + 1)
            if hi >= lo:
                total += hi - lo + 1
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
