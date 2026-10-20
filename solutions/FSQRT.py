import math
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    # isqrt is exact; int(math.sqrt(n)) can round a perfect square down by one.
    out = [str(math.isqrt(int(data[1 + i]))) for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
