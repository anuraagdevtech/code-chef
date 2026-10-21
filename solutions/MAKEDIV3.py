import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Digit sum 6: divisible by 3, not by 9. Last digit odd, no leading zero.
        out.append("3" if n == 1 else "1" + "0" * (n - 2) + "5")
    sys.stdout.write("\n".join(out) + "\n")


main()
