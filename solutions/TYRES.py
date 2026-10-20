import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # n is even, so the leftover after making cars is either 0 or 2 tyres.
        out.append("YES" if n % 4 == 2 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
