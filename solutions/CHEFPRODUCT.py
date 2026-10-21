import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # k distinct odds need sum >= k^2 and have sum congruent to k mod 2.
        m = isqrt(n)
        out.append(str(m // 2 if n % 2 == 0 else (m + 1) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
