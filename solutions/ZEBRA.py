import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        s = data[pos + 2]
        pos += 3
        # First index after i whose colour differs: the end of i's own run.
        nxt = [n] * n
        for i in range(n - 2, -1, -1):
            nxt[i] = i + 1 if s[i] != s[i + 1] else nxt[i + 1]
        last = {s[n - 1]: n - 1}
        for i in range(n - 2, -1, -1):
            last.setdefault(s[i], i)

        at = 0
        for _ in range(k - 1):            # land as early as possible
            at = nxt[at]
            if at == n:
                break
        if at == n:
            out.append("-1")
            continue
        far = last.get(s[at] ^ 1, -1)     # then leap as far as possible
        out.append(str(far + 1) if far > at else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
