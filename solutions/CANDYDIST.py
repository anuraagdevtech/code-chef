import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # "n divisible by m, and n // m even" is exactly "n divisible by 2m".
        out.append("Yes" if n % (2 * m) == 0 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
