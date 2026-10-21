import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, p, q = map(int, data[1 + 4 * i:5 + 4 * i])
        if p % a or q % b:
            out.append("NO")
            continue
        # They alternate, so the two work counts differ by at most one.
        out.append("YES" if abs(p // a - q // b) <= 1 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
