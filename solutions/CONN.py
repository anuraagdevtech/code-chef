import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Even n splits into 2s. Odd n needs one 7, so it must reach 7.
        out.append("YES" if n % 2 == 0 or n >= 7 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
