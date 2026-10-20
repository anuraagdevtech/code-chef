import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        # Each day is one block of two and must hold one of each sister.
        ok = all(s[j] != s[j + 1] for j in range(0, len(s), 2))
        out.append("yes" if ok else "no")
    sys.stdout.write("\n".join(out) + "\n")


main()
