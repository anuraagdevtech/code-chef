import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        twos = fives = 0
        while n % 2 == 0:
            n //= 2
            twos += 1
        while n % 5 == 0:
            n //= 5
            fives += 1
        # a = 2y - x and b = x - y must both be non-negative.
        out.append("Yes" if n == 1 and fives <= twos <= 2 * fives else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
