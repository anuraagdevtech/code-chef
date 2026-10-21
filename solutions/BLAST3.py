import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        s = data[2 + 2 * i]
        if n % 3 == 1:
            out.append("YES")             # one surviving character suffices
            continue
        seen = set()
        ok = False
        for j in range(n):                 # j is 0-based, so position j + 1
            if (j + 1) % 3 == n % 3 and s[j] in seen:
                ok = True
                break
            if (j + 1) % 3 == 1:
                seen.add(s[j])
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
