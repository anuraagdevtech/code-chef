import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # A nibble is 4 bits, so the size must divide evenly by 4.
        out.append("Good" if n % 4 == 0 else "Not Good")
    sys.stdout.write("\n".join(out) + "\n")


main()
