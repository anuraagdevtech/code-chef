import math
import sys


def is_prime(n: int) -> bool:
    if n < 2:              # 1 is explicitly not prime
        return False
    if n < 4:              # 2 and 3
        return True
    if n % 2 == 0:
        return False
    # A composite always has a factor at or below its square root.
    for d in range(3, math.isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = ["yes" if is_prime(int(data[1 + i])) else "no" for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
