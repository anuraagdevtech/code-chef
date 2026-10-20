import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        k = int(data[pos])
        words = data[pos + 1:pos + 1 + k]
        pos += 1 + k
        ok = True
        for word in words:
            # Lowercase stops at 'm' and uppercase starts at 'N', so letters
            # outside those ranges belong to neither language.
            lo = all(97 <= ch <= 109 for ch in word)       # a..m
            hi = all(78 <= ch <= 90 for ch in word)        # N..Z
            if not (lo or hi):
                ok = False
                break
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
