import sys


def works(a, b, x):
    """Can B be A shifted by x with exactly one element of A dropped?"""
    if x <= 0:
        return False
    i = j = skipped = 0
    while i < len(a) and j < len(b):
        if a[i] + x == b[j]:
            i += 1
            j += 1
        else:
            skipped += 1
            if skipped > 1:
                return False
            i += 1
    return j == len(b)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted(int(v) for v in data[pos + 1:pos + 1 + n])
        b = sorted(int(v) for v in data[pos + 1 + n:pos + 2 * n])
        pos += 2 * n
        # B[0] comes from A[0] or A[1]; the latter gives the smaller offset.
        for cand in (b[0] - a[1], b[0] - a[0]):
            if works(a, b, cand):
                out.append(str(cand))
                break
    sys.stdout.write("\n".join(out) + "\n")


main()
