import sys


def minutes(n: int) -> int:
    d = 50 - n
    best = None
    # Fixing the number of discharges determines the number of charges.
    for b in range(0, 201):
        num = d + 3 * b
        if num < 0 or num % 2:
            continue
        a = num // 2
        total = a + b
        if best is None or total < best:
            best = total
    return best


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = [str(minutes(int(data[1 + i]))) for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
