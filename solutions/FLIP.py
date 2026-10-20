import sys


def runs(diff, start, n):
    """Maximal runs of True in diff[start], diff[start+2], ..."""
    count = 0
    prev = False
    for i in range(start, n, 2):
        if diff[i] and not prev:
            count += 1
        prev = diff[i]
    return count


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = data[1 + 2 * i], data[2 + 2 * i]
        n = len(a)
        diff = [a[j] != b[j] for j in range(n)]
        # An operation flips a contiguous run inside one parity class only.
        out.append(str(runs(diff, 0, n) + runs(diff, 1, n)))
    sys.stdout.write("\n".join(out) + "\n")


main()
