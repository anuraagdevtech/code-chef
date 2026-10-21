import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[2 + 2 * i]
        # Each gap v_j - v_{j-1} weights the suffix sum from j onwards.
        run = 0
        ok = True
        for c in reversed(s):
            run += 1 if c == 0x31 else -1
            if run > 1 or run < -1:
                ok = False
                break
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
