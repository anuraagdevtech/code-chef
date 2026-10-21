import sys

HASH = 0x23
A = 0x61


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for s in data[1:1 + t]:
        n = len(s)
        hs = [i for i, c in enumerate(s) if c == HASH]
        k = len(hs)
        if k < 3:
            out.append("0")
            continue
        # Best single letter in S[0, h_t) and in S(h_t, n), per '#'.
        counts = [0] * 26
        pre = []
        at = 0
        for i in range(n):
            if s[i] == HASH:
                pre.append(max(counts))
                at += 1
            else:
                counts[s[i] - A] += 1
        counts = [0] * 26
        suf = [0] * k
        at = k - 1
        for i in range(n - 1, -1, -1):
            if s[i] == HASH:
                suf[at] = max(counts)
                at -= 1
            else:
                counts[s[i] - A] += 1
        # Best single letter strictly between consecutive '#'.
        gap = []
        for i in range(k - 1):
            counts = [0] * 26
            for j in range(hs[i] + 1, hs[i + 1]):
                counts[s[j] - A] += 1
            gap.append(max(counts))

        best = 0
        for i in range(k - 2):
            sides = (pre[i], gap[i], gap[i + 1], suf[i + 2])
            if 0 in sides:            # every arm of the W must be non-empty
                continue
            best = max(best, 3 + sum(sides))
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
