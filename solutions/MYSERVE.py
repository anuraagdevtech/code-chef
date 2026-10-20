import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        p, q = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Serves run in blocks of 2; Alice owns the even-numbered blocks.
        out.append("Alice" if ((p + q) // 2) % 2 == 0 else "Bob")
    sys.stdout.write("\n".join(out) + "\n")


main()
