import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Every move preserves a + b, so the halves must be whole numbers.
        out.append("Yes" if (a + b) % 2 == 0 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
