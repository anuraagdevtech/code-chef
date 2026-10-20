import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # No prime power (and not 1) is divisible by 6, while any remainder
        # 1..5 is itself a legal move. So multiples of 6 are the losses.
        out.append("Misha" if n % 6 == 0 else "Chef")
    sys.stdout.write("\n".join(out) + "\n")


main()
