import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        ok = True
        prev = None
        for j in range(n // 2):
            # Prefix increments make the coverage non-increasing, so the
            # mirror gaps must be non-negative and non-increasing too.
            gap = a[n - 1 - j] - a[j]
            if gap < 0 or (prev is not None and gap > prev):
                ok = False
                break
            prev = gap
        out.append(str(a[n - 1] - a[0]) if ok else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
