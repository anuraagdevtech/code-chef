import sys

PRETTY = (2, 3, 9)


def upto(n: int) -> int:
    """How many pretty numbers lie in [1, n]."""
    if n <= 0:
        return 0
    return sum((n - d) // 10 + 1 for d in PRETTY if n >= d)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        l, r = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Inclusive range count via prefix subtraction.
        out.append(str(upto(r) - upto(l - 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
