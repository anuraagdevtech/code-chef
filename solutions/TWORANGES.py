import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c, d = map(int, data[1 + 4 * i:5 + 4 * i])
        # Overlap can be empty, in which case its size must clamp to zero.
        overlap = max(0, min(b, d) - max(a, c) + 1)
        out.append(str((b - a + 1) + (d - c + 1) - overlap))
    sys.stdout.write("\n".join(out) + "\n")


main()
