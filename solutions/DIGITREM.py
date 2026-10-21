import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, d = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        s = str(n)
        fill = "0" if d else "1"
        bad = next((j for j, ch in enumerate(s) if int(ch) == d), -1)
        if bad < 0:
            out.append("0")
            continue
        best = None
        # M first differs from N at some position at or before the leftmost D.
        for j in range(bad, -1, -1):
            v = int(s[j]) + 1
            if v == d:
                v += 1
            if v > 9:
                continue
            cand = int(s[:j] + str(v) + fill * (len(s) - j - 1))
            if best is None or cand < best:
                best = cand
        if best is None:
            # Every digit position overflowed, so M needs one more digit.
            best = int(("2" if d == 1 else "1") + fill * len(s))
        out.append(str(best - n))
    sys.stdout.write("\n".join(out) + "\n")


main()
