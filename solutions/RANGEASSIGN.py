import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        if a[0] == a[-1]:
            out.append("YES")                 # one sweep flattens everything
            continue
        # The two values can spread no further than their outermost copies.
        last_first = max(i for i in range(n) if a[i] == a[0])
        first_last = min(i for i in range(n) if a[i] == a[-1])
        out.append("YES" if first_last <= last_first + 1 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
