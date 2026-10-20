import math
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    # Python ints are arbitrary precision, so 100! needs no manual big-num code.
    out = [str(math.factorial(int(data[1 + i]))) for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
