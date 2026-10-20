import sys


def discount(x: int) -> int:
    # Bands are half-open and ordered, so the first match wins.
    if x <= 100:
        return 0
    if x <= 1000:
        return 25
    if x <= 5000:
        return 100
    return 500


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        out.append(str(x - discount(x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
