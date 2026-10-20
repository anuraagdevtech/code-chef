import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        v = list(map(int, data[1 + 6 * i:7 + 6 * i]))
        a, b = v[:3], v[3:]
        # Best two of three = total minus the single lowest roll.
        sa, sb = sum(a) - min(a), sum(b) - min(b)
        out.append("Alice" if sa > sb else "Bob" if sb > sa else "Tie")
    sys.stdout.write("\n".join(out) + "\n")


main()
