import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        s = data[pos + 1]
        pos += 2
        zeros = s.count(b"0")
        # Every move removes one of each, and one is always available while
        # both remain, so the move count is forced.
        moves = min(zeros, n - zeros)
        out.append("Zlatan" if moves % 2 else "Ramos")
    sys.stdout.write("\n".join(out) + "\n")


main()
