import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        total = n * (n + 1) // 2
        # If the whole run is odd, dropping the leading 1 fixes the parity.
        out.append(str(n if total % 2 == 0 else n - 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
